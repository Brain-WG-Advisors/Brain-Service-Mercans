# CHANGELOG: LT-VMI-001 GPM313 Spec v1.2 → v1.3

> Hub [[Lituania]] · Lista de mudanças: [[Research Pipeline/Lithuania/2026-10-30-fontes-vigentes/MUDANCAS|MUDANCAS]] · Anterior: [[Research Pipeline/Lithuania/2026-10-29-correcoes/CHANGELOG-GPM-v1.2|CHANGELOG-GPM-v1.2]]

- **Arquivo:** `Research Pipeline/Lithuania/2026-10-30-fontes-vigentes/LT-VMI-001-GPM313-Spec_v1.3.xlsx`, md5 `703607856164c37056f4640988d02d35` (2ª rodada de 30/10; a 1ª era `7374bfdb2db71400e4565e60ffc4f314`). Só local.
- **Base:** `2026-10-29-correcoes/LT-VMI-001-GPM313-Spec_v1.2.xlsx` (md5 `61285401c648581bdcf48df88b6edfcc`, sem alteração).
- **GPM312:** não muda. O prazo de 15/02/2027 cai numa segunda-feira.
- **Data:** 2026-10-30 (frente Pipeline).
- **Edição:** `build_specs_v12.py` (nesta pasta), cirurgia XML no zip, sem `openpyxl.save`. Só `sheet1.xml` e `sheet8.xml` mudaram; as outras partes (9 desenhos, `persons`, estilos, sharedStrings) foram copiadas sem alteração. Estilos azuis já existentes (xf 44, 47, 49).
- **Destaque:** o azul da v1.2 foi mantido (a v1.2 não foi para o Drive; o Drive tem a v1.1). As células da v1.3 são as 6 abaixo.

## Fonte
- Lei da Administração Tributária IX-2112, redação consolidada em vigor desde 2026-07-01: `raw/docs/oficiais/LT/2026-10-30-IX-2112-MAI-suvestine-2026-07-01.txt` (md5 `2193cda0991bba63b7bc5f72a6bb9bce`; docx `f2af4be59f505b2bded5dcc13ae1ce95`). Art. 162(6): "Tais atvejais, kai paskutinė termino diena tenka ne darbo ar oficialios šventės dienai, termino pabaigos diena laikoma po jos einanti darbo diena."
- Dia da semana conferido em Python: 2026-08-15 = sábado; 2026-08-17 = segunda-feira.

## Alterações célula a célula
| Aba!Célula | Antes (v1.2) | Depois (v1.3) | Fonte |
|---|---|---|---|
| Example Analysis!D5 | "…15 August 2026, which is a Saturday. No primary source held for this build states whether the deadline moves to the next working day (the Law on Tax Administration is not in the source folder), so the date is kept as written and the point stays open." | "…15 August 2026, which is a Saturday. Under the Law on Tax Administration No. IX-2112 art. 162(6) (consolidated redaction in force from 2026-07-01), where the last day of a term falls on a non-working day or public holiday the term ends on the next working day, so this return is due by Monday 17 August 2026." | IX-2112 art. 162(6) |
| Version Control!A5:E5 (linha nova) | (não existia) | `LT-VMI-001` · `1.3` · `2026-10-30` · `Mercans Global Compliance` · "Example Analysis D5: July 2026 return due Monday 17 Aug 2026 (15 Aug is a Saturday; Law IX-2112 art. 162(6) moves the deadline to the next working day)." | este changelog |

## Conferência
- `validate_workbook.py --artifact RSPEC`: **PASS** (0/0/0, inclui lint C29).
- `check_gpm.py LT-VMI-001-GPM313-Spec_v1.3.xlsx <GPM312 v1.2>`: **PASS, 0 erros, 9 avisos** (os mesmos 9 avisos da v1.2).
- Diff openpyxl de todas as células, v1.2 × v1.3: **6 diferenças de valor** (D5 e a linha 5 do Version Control), todas com `FFDDEBF7`; 0 diferenças só de estilo; nenhuma célula de texto começa com "=".

## Fora do pedido (não alterado)
- **Sample File!B4** ainda mostra "Pateikimo terminas: 2026-08-15" (impressão do formulário com a data nominal da regra 12). Não estava na lista de mudanças; decidir se passa para 2026-08-17.
- **Report Matrix!F2** diz "By the 15th day of the month following…" sem a regra do dia útil seguinte. Pode receber "(next working day if a non-working day, IX-2112 art. 162(6))" numa próxima versão.

## Frentes
| Data | Frente | O quê |
|---|---|---|
| 2026-10-30 | pipeline | v1.3 gerada com o art. 162(6) da IX-2112; só local |

## 2ª rodada (30/10, tarde)
Regerada com o mesmo número (ainda só local). 8 células alteradas contra a v1.2, todas em `FFDDEBF7`.
- **Sample File!B4:** "Pateikimo terminas: 2026-08-15" → "2026-08-17".
- **Report Matrix!F2:** acrescentada a regra do dia útil seguinte (IX-2112 art. 162(6)), com o exemplo de 17/08/2026.
- **Version Control!E5:** menciona o alinhamento.

Testes: validate RSPEC **PASS (0/0/0)**; `check_gpm.py` **PASS, 0 erros, 9 avisos**; lint C29 limpo.

# CO-DD-001 v1.2 — conferência (21/10/2026)

**O que é:** a Fase 2C do plano Colômbia (`co-report-crosscheck/HANDOFF-2026-10-21.md` §8), na parte do DD. **Ainda não está no Drive**: só sobe com o ok do usuário (Fase 4).

## Base
- [[Research Pipeline/Colombia/2026-10-21-alinhamento-DD/base/CO-DD-001-v1.1-Drive-2026-10-05.xlsx|CO-DD-001-v1.1-Drive-2026-10-05.xlsx]] = cópia de `G:\...\Colombia\02- DD\CO-DD-001-v1.xlsx` (md5 af2fc9a05b2fccbd7b24d64242ad3723). O Version Control vai até a 1.1 (Draft).
- O Google Sheet `CO-DD-001-v1` do Drive também foi modificado em 05/10, com o mesmo Version Control. Não há edição mais nova.

## Fontes
- Res. DIAN 000227/2025. Cada artigo compilado termina com "(Artículo N, Resolución 13 de 2021)", o que dá o mapa: art. 1 → 1.5.3.1.1, 3 → 1.5.3.2.2, 5 → 1.5.3.3.1, 22 → 1.5.3.8.1. O mapa foi conferido também nas notas "compilado como" do normograma DIAN (`raw/docs/oficiais/CO/2026-10-21-Res-DIAN-0013-2021-normograma.htm`).
- Resposta da BAU de 21/10, Q13: a data de desligamento vem do registro "Termination" do sistema. As specs já dizem o mesmo (CO-DIAN-001 NIE003, CO-PILA-003 T2R2-081, CO-DIAN-004 casilla 31).
- Instrução do Form 220, casilla 31: "Período de la certificación, A".

## Antes → depois (só colunas azuis; nenhuma coluna laranja foi tocada)
| Célula | Antes | Depois |
|---|---|---|
| ID Information V20 | DIAN Resolution 000013 of 2021 arts. 1, 5, 22 | DIAN Resolution 000227 of 2025 arts. 1.5.3.1.1, 1.5.3.3.1, 1.5.3.8.1 |
| Country Fields W28 | Resolution 000013 of 2021 art. 3, com a citação misturando inglês e espanhol | Resolution 000227 of 2025 art. 1.5.3.2.2, 'independientemente de que el sujeto obligado, realice pagos en periodos diferentes o inferiores' (texto oficial) |
| Country Option Mappers G84 | Resolution 000013 of 2021 art. 3 | Resolution 000227 of 2025 art. 1.5.3.2.2 |
| Country Fields W24 (Termination Date) | — | Acrescentado: a origem é o registro "Termination"; para quem saiu no ano, é também o valor da casilla 31 do 220 "Período de la certificación, A" |
| Country Fields I6 e W6 (Second surname) | 'placeholder' (alerta C29 do toolkit) | 'substitute value' (mesmo sentido) — item 6, 21/10 |
| Version Control linha 15 | — | 1.2, 21-Oct-26, mudança descrita, Draft, Wallisson Gomes (mesmo estilo das linhas 13 e 14) |

## Conferência
- Edição direto no XML (sharedStrings e sheet1); nenhum `openpyxl.save`. Mudaram só 2 partes do zip. Imagens e desenhos idênticos byte a byte.
- Diff célula a célula contra a base: 9 células mudaram, exatamente as previstas.
- Verificador independente (`DD-verification.json`): PASS_WITH_MINOR_FIX. Os 2 ajustes (vírgula na citação oficial; redação da casilla 31) foram aplicados e o diff foi conferido de novo.
- Toolkit `validate_workbook --artifact DD`: FAIL com 3 bloqueios que **já existiam na base do Drive**: C12 em 'Country Option Mappers' A4:G4, e C29 'placeholder' em Country Fields I6 e W6 (texto antigo). Nenhum bloqueio novo. Isso fica para decisão do usuário (PENDING item 24).
- Res. 13/2021 nas abas de dados: 0 menções (só aparece no texto do Version Control D15).
- 21/10 (item 6): I6/W6 reescritos sem 'placeholder'; diff contra a base = 11 células previstas; toolkit agora FAIL só no C12 (coluna G 'Constraint / Notes' a mais em 'Country Option Mappers', que guarda notas, inclusive a G84; remover apagaria conteúdo → decisão do usuário).
- md5 da v1.2: db3b8dc6ff95fd2b1cd86b1afabb8f3c

## Frentes
| Data | Frente | O quê |
|---|---|---|
| 2026-10-21 | geral (Colômbia) | v1.2 criada e conferida; não subiu ao Drive |
| 2026-10-21 | geral (Colômbia) | I6/W6 sem 'placeholder' (C29) |
| 2026-10-21 | geral (Colômbia) | Copiado para o Drive com o ok do usuário; md5 da cópia idêntico |

| 2026-10-22 | geral (Colômbia) | Importado no Google Sheet CO-DD-001-v1 (Replace spreadsheet); conferido ao vivo: VC 1.2, Res. 13 x0 nas abas de dados, sem placeholder |

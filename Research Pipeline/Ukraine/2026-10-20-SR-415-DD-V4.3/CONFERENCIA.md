# DD Ucrânia V4.3 — SR-415 (campos do Держстат para o 1-PV)

**Pedido:** Lily Li, SR-415, 19/10 07:44 UTC. Linhas 38, 39 e 45 da spec UA-1PV-002 (C_REG, C_RAJ, RAY): "if not, pls create new field".
**Base:** `Downloads/Ukraine_Data_Dictionary_V4.2 (1).xlsx` (export de 16/10 11:28; a V4.2 é a maior versão no Drive `Ukraine/02- DD`).
**Final:** [[Research Pipeline/Ukraine/2026-10-20-SR-415-DD-V4.3/Ukraine_Data_Dictionary_V4.3.xlsx|Ukraine_Data_Dictionary_V4.3.xlsx]] (md5 `29c35655edb77d3c7d010d6357946e89`). Gerado por `build_dd_v43.py` (cirurgia de XML; só `sheet1.xml` e `sheet5.xml` mudam, as outras partes são copiadas byte a byte).

## Antes → depois
| Aba | Linha | Mudança |
|---|---|---|
| Country Fields | 86 (nova) | `derzhstat_region_code`: Derzhstat Region Code (C_REG), CM, Text, formato "Code as in SPR_SSCU REGION/CODE (e.g. 05, 80)" |
| Country Fields | 87 (nova) | `derzhstat_district_code`: Derzhstat District Code (C_RAJ), CM, Text, formato "Code as in SPR_SSCU REGION/LOCAL/CODE" |
| Country Fields | 88 (nova) | `statistical_district_code`: Statistical District Code (RAY), CM, Text, 3 dígitos, ≠ '000' (STATRAY) |
| Country Fields | 86→89 … | linhas seguintes descem 3 posições, sem outra alteração |
| Version Control | 29 (nova) | 4.3, 2026-10-20, SR-415, status Under Review |

Linhas novas em azul claro `FFDDEBF7`, com os mesmos estilos das linhas 83–85 (V4.1). Elas continuam azuis desde a V4.1, então a cor sozinha não separa as duas versões. Ordinais 10–12 em Employer Information / Reporting Details. A aba SaaS não foi alterada (mesmo critério da V4.1).

## Fontes
- C_REG/C_RAJ: Держстат, Format 3.1, Tabela 1 (`raw/docs/oficiais/UA/2026-10-13-Derzhstat-Format-standart-3_1.doc`): "орган державної статистики… (SPR_SSCU.XML)"; SPR_SSCU (`2026-10-13-Derzhstat-spr_sscu-2016.xml`): 25 regiões com 2 dígitos e 659 distritos com 3 dígitos; Kyiv = 80, 26 = Івано-Франківська. SPR_STI (`spr_sti/SPR_STI.XML`, 06/03/2026): 26 = М.КИЇВ. XSD S0301016/S0301121: C_REG/C_RAJ `xs:string`, obrigatórios.
- RAY: listas de campos técnicos S0301016 e S0301121 (RAY: 3 caracteres, "так", coluna G "Автоматичне заповнення з картки підприємства" = +); `common_types` 2025-05-14: STATRAY `[0-9]{3}`, comentário "крім комбінації '000'"; Кодифікатор КАТОТТГ: o 2º nível tem 2 dígitos.

## Conferência
- Célula a célula V4.2 × V4.3 (valor, cor, fonte, quebra, formato), nas 9 abas: 0 diferenças fora das linhas inseridas.
- Zip íntegro; desenhos e imagens (logo) preservados.

## Ressalvas
- SPR_SSCU: só achei a versão de 2016 (`spr_sscu_2016.ZIP`; Wayback, sem versão mais nova em `elektr_zvit/po_doc`). Os campos não trazem lista de valores; o valor de cada cliente vem do Держстат/Кабінет респондента.
- Fora do pedido: na V4.2, Country Fields O85 (C_STI_ORIG) virou fórmula com `#ERROR!` (o texto começa com "="). Não foi alterado.

## Frentes
| Data | Frente | O quê |
|---|---|---|
| 2026-10-20 | suporte | V4.3 criada a partir da V4.2, conferida; copiada para o Drive (md5 1232791b) |
| 2026-10-20 | suporte | Revisão de 100%: C_REG/C_RAJ sem tamanho fixo e sem validação contra o SPR_SSCU (o Format 3.1 completa o C_REG com zeros à esquerda no nome do arquivo e o exemplo traz C_RAJ = 55; o SPR_SSCU publicado é de 2016); descrição do RAY só com o fato (3 × 2 dígitos); status Under Review. Novo md5 29c35655. A versão anterior sumiu do Drive (pasta alterada às 09:17, sem V4.3.gsheet); a nova não foi copiada, aguarda o usuário |
| 2026-10-20 | suporte | Versão corrigida copiada para o Drive (md5 29c35655 conferido) |
| 2026-10-20 | suporte | Usuário importou (V4.3.gsheet 09:55) e enviou o comentário no SR-415 (12:56 UTC) |

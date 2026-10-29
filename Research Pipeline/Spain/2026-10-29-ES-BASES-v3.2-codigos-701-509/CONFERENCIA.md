# ES-BASES-001 v3.2 — códigos de base 701/702/703/704/801/901 e rótulo do 509 (2026-10-29)

> Hub: [[Espanha]] · Correções: [[correcoes]] · Origem: e-mail da Lily, 29/10 00:05, fio "Fwd: Spain Migration Progress" ([[2026-10-28-triagem-emails]])

## Base
- Gsheet atual da spec (o que a Lily usa): `ES-BASES-001_FicheroBases_Spec` (id 1fo4mwbv…), v3.1 (11/09/2026), exportado em 29/10 10:47 → `ES-BASES-001_FicheroBases_Spec_v3.1-export-2026-10-29.xlsx` (md5 b6bfeab3…).
- A v3.3 de Downloads (09/09, nunca importada) não foi usada: a produção segue o gsheet v3.1.

## Fonte
- TGSS, Manual SLD Especificaciones Técnicas, 14/09/2026, tabela de conceptos (l. 1495–1600 da cópia em `raw/docs/oficiais/ES/`):
  - 701: "Solo si tiene pluriempleo con exclusiones o si se trata del colectivo especial de Artistas (0112)";
  - 702 (FOGASA) e 703 (FP): "Solo si tiene pluriempleo con exclusiones";
  - 704, 801, 802 e 901 não existem na tabela;
  - 509 = CONTING.COM.COTIZ.EMPRESARIAL (l. 1523).
- 509 em pago directo: BNR 7/2024 ponto 3; BNR 3/2023 p. 1; RD 2064/1995 art. 68.6. A fórmula do 509 (v2.3/v2.4, 9 elementos de pago directo do INSS) já estava certa.

## Antes → depois (31 células, azul claro FFDDEBF7)
| Onde | Antes | Depois |
|---|---|---|
| Field Options 39 (701) | desemprego de todo full-time | não gerar para funcionário comum; só pluriemprego com exclusões/Artistas; gatilho OPEN (sem campo no DD) |
| Field Options 40 (702) | "Unemployment part-time" | FOGASA, só pluriemprego com exclusões; não gerar |
| Field Options 41 (703) | "Unemployment fixed-term" | FP, só pluriemprego com exclusões; não gerar |
| Field Options 43/44/128 (801/901/704) | FP / FOGASA / fijo discontinuo | não gerar (não são códigos da TGSS) |
| Field Options 30 (509) | rótulo "IT payment delegation" | "employer-only contribution (pago directo)"; fórmula inalterada |
| Field Options H30, H39–H41, H43, H44, H114, H128 | RA comments "CONFIRMED" errados | nota datada de correção no topo; histórico mantido |
| Fichero de Bases (SSC) Spec M49 | "701=Unemployment, 801=…, 901=FOGASA" | regra da tabela da TGSS |
| Population Rules C4/C5 | 500, 601, 701, 801, 901 / 502, 603, 702 | 500, 601 / 502, 603 |
| Lily Query Resolved C34/D38 | excesso de indenização no 701 | 500 / 601 |
| Version Control linha 29 | — | v3.2, 29-Out-26 |

## Conferência
- Diferença célula a célula com o export: 31 células, todas previstas; abas, merges e imagem (Lily Query Resolved) preservados.
- Cópia no Drive: `Spain/17 - Statutory Reports/Social Security (TGSS – Sistema RED SLD)/ES-BASES-001_FicheroBases_Spec_v3.2.xlsx`, md5 48a3bb35… igual ao local.
- Import no gsheet atual (29/10, pelo Chrome, Arquivo > Importar > "Replace spreadsheet", a pedido do usuário). Export do gsheet depois do import (Downloads, "(12)") × v3.2 local: 0 diferenças de valor nas 8 abas; azul claro e imagem preservados.

## Fora do pedido (não alterado)
- Linha 49: 611 rotulado "Sea Workers" (na tabela: base AT/EP de empresa excluída de IT).
- Regra "502/603 para part-time" (M49): na tabela, 502 = outras horas extras.

## v3.3 (29/10, mesma pasta)
- Erro da v2.3/v2.4 achado na revisão antes do envio: 79418–79424 são pago delegado por padrão (BNR 7/2023, TPC 21/25) → saem do 509 e vão para 500 + 563; 509 = 79429/79430 (risco, RD 2064/1995 art. 68.6) e 79432 (semanas pagas da licença parental = prestação por nascimento e cuidado, RD-ley 9/2025). 11 células (Field Options E27, E30, E145, D30, H30, G145; Version Control linha 30). Drive md5 599bb2e2… igual; import "Replace" e export × local: 0 diferenças. Atenção: o "v3.3" de Downloads de 09/09 é outra linhagem, nunca importada.

## v3.4 (29/10, mesma pasta)
- Licença por nascimento e cuidado (maternidade/paternidade, tempo completo) no 509: unidades 79006/79007 no gatilho do 509 e do 603, excluídas do 500 e do 601 (Field Options E27, E30, E35, E37, D30, H30; Version Control linha 31). Base: RD 2064/1995 art. 68.6; AFI v9.7 ("Pago Directo: Nacimiento y Cuidado de menor"); bate com o pareamento já em D37 (509+603, IDC 31). 79406/79407 (pagamentos da empresa, BCCC=Yes) inalterados. OPEN: gozo a tempo parcial (500 + 535). Drive md5 331923ef… igual; import "Replace" e export × local: 0 diferenças.

## Frentes
- 2026-10-29 · gmail · v3.4 montada, importada (Replace) e conferida.
- 2026-10-29 · gmail · v3.3 montada, importada (Replace) e conferida.
- 2026-10-29 · gmail · import "Replace spreadsheet" no gsheet atual feito e conferido.
- 2026-10-29 · gmail · v3.2 montada a partir do export do gsheet; cópia no Drive; import pendente; país ativo → ticket de alteração ao Development (pedido à Lily no e-mail).

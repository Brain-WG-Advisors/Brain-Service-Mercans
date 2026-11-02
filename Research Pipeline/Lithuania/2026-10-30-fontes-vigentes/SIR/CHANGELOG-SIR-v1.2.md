# LT-SIR-001 v1.2: changelog (30/10/2026)

Hub: [[Lituania]] · Lista de mudanças: [[Research Pipeline/Lithuania/2026-10-30-fontes-vigentes/MUDANCAS|MUDANCAS]] · Anterior: [[Research Pipeline/Lithuania/2026-10-29-correcoes/SIR/CHANGELOG-SIR-v1.1|CHANGELOG-SIR-v1.1]]

Só local. Nada foi para Drive, ticket ou e-mail. A pasta `2026-10-29-correcoes/SIR/` e `raw/` não foram alterados.

## Arquivos
| Arquivo | O quê |
|---|---|
| `LT-SIR-001-v1.2.docx` | Entrega. md5 `804d89c4180a6e2ffbaffd3d7b5b0aa2` (2ª rodada de 30/10; a 1ª era `2730aff9545c357d7838f462eb513e29`). 22 páginas, 24 tabelas, 39 trechos com sombreamento `DDEBF7` (exatamente o que mudou da v1.1) |
| `sections/s00–s08.md` | Cópia das seções da v1.1, editadas (s00, s02, s05, s06, s07, s08; s01, s03, s04 iguais) |
| `edit_sections_v12.py` | As substituições aplicadas às seções (cada trecho antigo conferido: existe 1 vez) |
| `build_sir_docx_lt.py` | Gerador da v1.1 com: saída, rodapé, título e capa em v1.2; **base do sombreamento = v1.1** (seções da v1.1 renderizadas com o gerador da v1.1, só leitura, sem bytecode na pasta antiga) |
| `update_toc_word.ps1`, `finalize_sir_docx.py` | Iguais aos da v1.1, apontando para o arquivo v1.2 |
| `build_lt_sir.py` | Gerador antigo, só histórico (copiado sem alteração) |

Ordem para regerar: `python build_sir_docx_lt.py` → `powershell -File update_toc_word.ps1` → `python finalize_sir_docx.py`.

## Fontes novas (S13, S14)
- **S13:** Ordem da Sodra V-243, redação consolidada em vigor desde 2026-10-03 (e-TAR TAR.34A6775CE75B), `raw/docs/oficiais/LT/2026-10-30-V-243-suvestine-2026-10-03.txt` (md5 `bdd6a96fa8e663d12634d2c5f2c20b49`).
- **S14:** Lei IX-2112 (Administração Tributária), redação consolidada em vigor desde 2026-07-01, `raw/docs/oficiais/LT/2026-10-30-IX-2112-MAI-suvestine-2026-07-01.txt` (md5 `2193cda0991bba63b7bc5f72a6bb9bce`).

## Tabela de alterações
| Seção | Antes (v1.1) | Depois (v1.2) | Fonte |
|---|---|---|---|
| Capa, rodapé, título | v1.1, 29 October 2026; specs LT-SODRA-003 v1.1, LT-VMI-001 v1.2 | v1.2, 30 October 2026; LT-SODRA-003 v1.2, LT-VMI-001 v1.3, LT-VMI-002 v1.2 | versões geradas hoje |
| Document Control (Version; Related deliverables; Version history) | v1.1; SAM v1.1, GPM313 v1.2 | v1.2; SAM v1.2, GPM313 v1.3; linha nova v1.2 (fontes S13/S14, regra do dia útil, G15 fechada, G10 e G16 reduzidas) | este changelog |
| 0.2 | "Version 1.1 follows an independent review … (A1 v1.1, A2 v1.2, A3 v1.2)" | "Version 1.1 followed an independent review of version 1.0. Version 1.2 adds the Sodra and VMI texts in force (S13, S14) … (A1 v1.2, A2 v1.3, A3 v1.2)" | — |
| 0.3 | "S1 to S12" | "S1 to S14" | — |
| 0.6 | "S11 and S12 were read on 29 October 2026. The Sodra sources S1 to S4 are held as extracts only; the originals are not archived" | "…S13 and S14 on 30 October 2026. The SAM and NP-SD2 filling rules behind S1 and S4 are now archived in the V-243 text in force (S13); the other Sodra originals are held as extracts only" | S13 cap. IX (p. 48-56) e X (p. 57-76) |
| 2.2 OUT-01 | "by the 15th of the following month (S1 point 52)" | "(S13 point 52); if that day is a Saturday, Sunday or public holiday, the next working day (S13 point 125)" | S13 p. 52, 125 |
| 2.2 OUT-03, OUT-04 | "Whether a deadline falling on a non-working day moves to the next working day: G15" / "Non-working-day rule: G15" | "A deadline falling on a non-working day or public holiday moves to the next working day (S14 art. 162(6))" | S14 art. 162(6) |
| 2.3 | SAM v1.1; GPM313 v1.2 | SAM v1.2; GPM313 v1.3 | — |
| 5.1 "Correction of filed SAM data" | P35 da DSA; rota PT da redação de 2015 (p. 76, 103.6, 103.7); "text of the SD rules in force today was not available … open (G10)"; fonte S12 | Duas rotas na redação vigente: eletrônica (PT via EDAS, "without delay", p. 87, 88; anexos PT-SAM3SD, PT-SAM3SD-M, PT-SAM3SDP, p. 86.6-86.8; atraso = PT código 01, p. 52, 91.3.1) e escrita (pedido escrito + novo SAM com "x" em P35, P14T/P17T, só os segurados alterados, p. 93-95). Rota a automatizar: aberta (G10). Fonte: S11 p. 10; S13 | S13 p. 52, 86.6-86.8, 87 ("PT elektroninis prašymas teikiamas nedelsiant, kai…"), 88, 91.3.1, 93-95 |
| 5.3 OUT-01 SAM | "correction through the revised-notice fields or PT annexes, current route not confirmed" | "correction through PT annexes (electronic) or a new SAM with P35 (written), S13 points 86-95; route for automation open" | S13 p. 86-95 |
| 6.1 tabela OUT-01 | fonte "S1 point 52" | "S13 point 52" | S13 p. 52 |
| 6.1 parágrafo | "Whether a deadline that falls on a non-working day moves … is not stated in the sources read for this register (G15); only the NP-SD2 instruction states it (S4 point 57)." | Prazo em sábado, domingo ou feriado oficial passa ao dia útil seguinte: SD (SAM incluído) pelo S13 p. 125; GPM313 e GPM312 pelo S14 art. 162(6). Exemplo: GPM313 de julho/2026 vence segunda 17/08/2026 (15/08 é sábado). NP-SD2: S4, S13 p. 57 | S13 p. 57, 125; S14 art. 162(6) |
| 6.3 OUT-01 SAM | "Not established: current correction route open (G10)"; S11; S12 | "A PT request is filed without delay once incorrect data are found or a SAM is filed late (S13 point 87); late SAM: PT reason code 01 (S13 points 52, 91.3.1). Route for automation open (G10)"; S11; S13 | S13 p. 52, 87, 91.3.1 |
| Appendix A intro | S1 a S4 só extratos (G16) | S13 e S14 acrescentadas e arquivadas; regras de S1 (p. 48-56) e S4 (p. 57-76) conferíveis em S13; S1 (página e `sam-v07.mxfd`), S2, S3 continuam só extratos (G16) | S13 |
| 7.1 A1, A2 | v1.1, v1.2 | v1.2, v1.3 | — |
| 7.2 S12 | "superseded text, used only to show the earlier correction route" | "superseded by S13, kept only for the earlier numbering" | S13 |
| 7.2 S13 (nova) | — | V-243 na redação da V-683, consolidada desde 2026-10-03, TAR.34A6775CE75B; arquivada 30/10 | S13 cabeçalho |
| 7.3 S14 (nova) | — | IX-2112, consolidada desde 2026-07-01; arquivada 30/10; art. 162(6) | S14 cabeçalho |
| 8.1 G10 | "The SD rules in force today were not available, so the current route is not confirmed" | Rotas descritas pelo S13 (p. 86-92; 52, 91.3.1; 93-97). Aberto: qual rota a Sodra espera para sistema do empregador e se o DataService aceita PT | S13 |
| 8.1 G15 | Linha da lacuna do dia não útil | **Removida** (fechada; ver 8.4) | S13 p. 125; S14 art. 162(6) |
| 8.2 G16 | "S1 to S4 … save the DataService PDF, `sam-v07.mxfd` and the S2 and S4 pages" | "S1 to S3 … The V-243 rules behind S1 and S4 are archived as S13. To close: save the DataService PDF, `sam-v07.mxfd` and the S1 and S2 pages" (PDFs da DataService e `sam-v07.mxfd` continuam pendentes) | S13 |
| 8.3 | Bullets G10 e G15 | Bullet G15 retirado ("does not claim a next-working-day shift"); G10 reescrito: "does not claim which SAM correction route Sodra expects an employer system to automate" | — |
| 8.4 (nova) | — | "Gaps closed in version 1.2": G15 fechada (S13 p. 125; S14 art. 162(6)) | — |

## Conferência
- O docx abre (python-docx); Word atualizou sumário e campos (`pages=22`); `finalize_sir_docx.py` recolocou `w:updateFields` e core properties (autor e lastModifiedBy "Mercans Compliance", título v1.2). Rodapé: "LT-SIR-001 v1.2 | Mercans Compliance Regulations Team | 2026 | Page N".
- Lint de marcadores (TODO, TBD, FIXME, XXX, placeholder, VERIFY No., "to be confirmed", "to be verified") no corpo, tabelas, cabeçalho e rodapé: **0 ocorrências**.
- Diff do texto extraído v1.1 × v1.2: só as alterações da tabela acima (mais a linha nova "8.4" no sumário e o número de página da 8.2, 22 → 21).
- Sombreamento × alteração, por parágrafo e por célula: 39 trechos sombreados; **0 alterados sem sombreamento; 0 sombreados sem alteração**.

## Frentes
| Data | Frente | O quê |
|---|---|---|
| 2026-10-30 | pipeline | v1.2 gerada com S13 (V-243 vigente) e S14 (IX-2112); G15 fechada; G10 e G16 reduzidas; só local |

## 2ª rodada (30/10, tarde)
`edit_sections_v12b.py` aplicada sobre as seções da 1ª rodada; docx regerado (sombreamento contra a v1.1).
- **G10:** desde 2010 a correção é só eletrônica (S13 ponto 77.1.1, conferido no texto), então a rota a automatizar é o pedido PT. Fica aberto só se o DataService aceita PT. Alterados 5.1, 5.3, 6.3, 8.1 e 8.3.
- **G16:** `sam-v07.mxfd` arquivado (zip da Sodra de 2026-02, definição de 2025-12-31). Fica aberto o PDF do DataService e a página S2. Alterados S1 em 7.2 e 8.2.
- **Document Control:** linha da v1.2 completada.

Conferência: o docx abre; 22 páginas; lint 0; todo trecho novo está sombreado.

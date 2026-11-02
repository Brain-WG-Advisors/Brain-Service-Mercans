# Lituânia: correções de 29/10 (SAM v1.1, GPM313/GPM312 v1.2, SIR v1.1)

> Hub [[Lituania]] · Origem: [[Research Pipeline/Lithuania/2026-10-28-validacao/CONFERENCIA]] · Próximo passo (BAU): [[Research Pipeline/Lithuania/2026-10-29-validacao-BAU/METODO-VALIDACAO-BAU]] · [[correcoes]]

Status: **no Drive desde 29/10, com ok do usuário dado nesta janela.** Ainda não foi para ticket nem para e-mail.
- As 3 specs foram importadas com Replace pelo Chrome nos `.gsheet` (`18 - Statutory Reports`):
  - SAM `1_f4BkM1PeoxLg_NgTuEBGTDoMz4CIMXIQpaprccq4SM`;
  - GPM313 `1WoyBgcc-LJiTdGDk_zOh40lcQ5PZC67zC5RvpkULbgo`;
  - GPM312 `1Y02iqrFzs0qiYPaB5Up0_Wugax8DWX39BPhfJ_lgDZQ`.
- Os 4 xlsx/docx foram copiados também para o Drive, com o md5 igual ao local: `18 - Statutory Reports/*_v1.x.xlsx` e `19 - Statutory Integrations/LT-SIR-001-v1.1.docx`.
- **Os gids das abas mudaram com o Replace.** Os gids do `PASSE-DE-BASTAO.md` estão obsoletos.
- **Conferido em 30/10:** CSV exportado de cada aba das 3 planilhas no Drive e comparado linha a linha (hash do conteúdo de cada linha) com o xlsx local.
  - SAM: 9 abas, 0 diferenças.
  - GPM313: 9 abas, 0 diferenças.
  - GPM312: 9 abas, 0 diferenças.
  - Nenhum `#ERROR!`/`#REF!` (o GPM312 tinha 5 na v1.1).

## Finais
| Arquivo | md5 | Base |
|---|---|---|
| `LT-SODRA-003-SAM-Spec_v1.1.xlsx` | 1447d6b08e180eaab035f3f16b286ae1 | v1.0 (export do `.gsheet`) |
| `LT-VMI-001-GPM313-Spec_v1.2.xlsx` | 61285401c648581bdcf48df88b6edfcc | v1.1 (igual ao Drive) |
| `LT-VMI-002-GPM312-Spec_v1.2.xlsx` | 243500940fe0a3469e0ea7abc0b22075 | v1.1 |
| `SIR/LT-SIR-001-v1.1.docx` | bbeb8f25125693ec53335e8a54380686 | v1.0 (igual ao Drive, pasta 19) |

Detalhe célula a célula, com fonte, em `CHANGELOG-SAM-v1.1.md`, `CHANGELOG-GPM-v1.2.md` e `SIR/CHANGELOG-SIR-v1.1.md`. As alterações estão destacadas em `FFDDEBF7` (no docx, `DDEBF7`).

## Conferência
| Artefato | Construtor | Revalidação independente (verificador próprio) | Depois dos ajustes |
|---|---|---|---|
| SAM v1.1 | validate PASS; check_sam 106/0 | `REVAL-SAM-v1.1.md`: 0 BLOCKER, 0 MAJOR, 7 MINOR | Corrigidos; verificador independente rodado de novo em 29/10: **143 OK, 1 FAIL** (o FAIL é a divergência documentada da linha abaixo) |
| GPM313/312 v1.2 | validate PASS; check_gpm 0 erros | `REVAL-GPM-v1.2.md`: 1 MAJOR herdado da v1.1 (U7=U com 20 %) + 6 MINOR | Corrigidos; verificador independente rodado de novo em 29/10: **PASS, 0 erros, 10 avisos**; caixas 4–7 = soma das linhas |
| SIR v1.1 | docx/C29/lint limpos | `SIR/REVAL-SIR-v1.1.md`: 0 BLOCKER, 0 MAJOR, 7 MINOR | Corrigidos (R5 ficou de propósito) |

## Verificado pessoalmente (fonte primária)
- O pagador `302123442` passa no mod 11 (pesos 1–8, resto 2 = 9º dígito). O `302123456` falha (resto 1 ≠ 6).
- Não residente com renda de trabalho no exterior não é tributado: GPMI IX-1007 (redação consolidada de 2026-06-11), art. 2(16)(4), que exclui essa renda da renda de fonte lituana, e art. 5(4)(5).

## Pontos em aberto
- **V-243 da Sodra:** a SAM cita a redação V-683 (pontos 86.6–86.8, 88, 91.3.1, 92.4, 95.4, 250), herdada da v1.0, de um PDF que não está em disco. A e-TAR e a e-seimas responderam HTTP 403 em 29/10. Em disco só existe a redação de 2015. As células estão marcadas "fonte a arquivar" (Report Matrix!I2 e o changelog).
- **TaxRate do SAM3SDP:** o MXFD de 2018 dá tamanho 5 e a DSA dá 11. A spec ficou com 5 e registra a divergência em J69/M69.
- Se o Garantinis fondas, o ILDIF e os 3 % da pensão param no teto. Não há fonte lida.
- **Prazo GPM313 de 15/08/2026 (sábado):** falta a Lei de Administração Tributária.
- A SAM agora cita a V-243 de 2015, p. 111, para mover para o dia útil seguinte um prazo que cai em dia não útil (Population Rules!D13). O SIR v1.1 ainda trata o "dia útil seguinte" como lacuna G15. Alinhar o SIR para o caso da Sodra na próxima versão.
- Originais da Sodra não arquivados (G16). O teste real no EDAS/EDS é o critério 7 do método com o BAU.

## Frentes
| Data | Frente | O quê |
|---|---|---|
| 2026-10-29 | pipeline (Process Lithuania) | Correções, revalidação independente, ajustes da rodada 2 |
| 2026-10-29 | pipeline (Process Lithuania) | Drive: cópia dos 4 finais (md5 ok) e import Replace das 3 specs pelo Chrome |
| 2026-10-30 | pipeline (Process Lithuania) | Conferência Drive × local por CSV: 27 abas iguais, sem erros |

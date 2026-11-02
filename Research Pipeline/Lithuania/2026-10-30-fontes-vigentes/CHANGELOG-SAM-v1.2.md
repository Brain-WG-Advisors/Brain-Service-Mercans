# CHANGELOG: LT-SODRA-003 SAM Spec v1.1 → v1.2

> Hub [[Lituania]] · Lista de mudanças: [[Research Pipeline/Lithuania/2026-10-30-fontes-vigentes/MUDANCAS|MUDANCAS]] · Reconferência: [[Research Pipeline/Lithuania/2026-10-29-correcoes/V243-RECHECK-2026-10-30|V243-RECHECK]] · Anterior: [[Research Pipeline/Lithuania/2026-10-29-correcoes/CHANGELOG-SAM-v1.1|CHANGELOG-SAM-v1.1]]

- **Arquivo:** `Research Pipeline/Lithuania/2026-10-30-fontes-vigentes/LT-SODRA-003-SAM-Spec_v1.2.xlsx`, md5 `87bed94be9abc24397bb48a7d776f6f2` (2ª rodada de 30/10; a 1ª era `feb69ec491f9b6ef67643e02bc971eb8`). Só local: nada foi para Drive, ticket ou e-mail.
- **Base:** `2026-10-29-correcoes/LT-SODRA-003-SAM-Spec_v1.1.xlsx` (md5 `1447d6b08e180eaab035f3f16b286ae1`, sem alteração).
- **Data:** 2026-10-30 (frente Pipeline).
- **Edição:** `build_specs_v12.py` (nesta pasta). Cirurgia XML no zip, sem `openpyxl.save`: só `sheet1/2/4/7.xml` mudaram; as outras 31 partes (9 desenhos, `persons`, `styles.xml`, `sharedStrings.xml` etc.) foram copiadas sem alteração, na mesma ordem. Cada célula alterada foi gravada como `inlineStr` com o estilo azul `FFDDEBF7` já existente (xf 13; T46 xf 14). Nenhum estilo novo.
- **Destaque:** o azul da v1.1 foi mantido. Como a v1.1 não foi para o Drive, o azul marca o que difere da v1.0 que está no Drive. As células da v1.2 são as 16 da tabela abaixo. M13, T13, M29 (antes azul de categoria `FFBDD7EE`) e Population Rules C4, D4 (antes sem preenchimento) passaram a azul.

## Fontes (arquivadas em `raw/docs/oficiais/LT/`, lidas em 30/10)
| Chave | Ato | Arquivo (.txt, md5) |
|---|---|---|
| V-243 | Ordem da Sodra V-243, redação consolidada em vigor desde 2026-10-03 (e-TAR TAR.34A6775CE75B) | `2026-10-30-V-243-suvestine-2026-10-03.txt`, `bdd6a96fa8e663d12634d2c5f2c20b49` |
| XII-2604 | Lei do Fundo de Garantia e do ILDIF, em vigor desde 2026-01-01 | `2026-10-30-XII-2604-GF-ILDIF-suvestine-2026-01-01.txt`, `4a97f50d6123e0e945b41b43d4c8e59a` |
| IX-1691 | Lei da acumulação de pensão, 2026-01-01 a 2026-12-31 | `2026-10-30-IX-1691-pensiju-kaupimo-suvestine-2026-01-01.txt`, `161bc4e3b26eb7c624aab040028793bf` |
| I-1336 art. 10(9) | Lei do seguro social, extrato de 27/10 | `2026-10-27-I-1336-art10-9_e_XV-632-art3_extrato.md` |

## Alterações célula a célula
Nos textos longos aparece só o trecho que mudou.

| Aba!Célula | Antes (v1.1) | Depois (v1.2) | Fonte |
|---|---|---|---|
| Report Matrix!G2 | "(EDAS) (points 8 and 249)"; "(point 250) and must be signed with a qualified electronic signature ('saugiu…'" | "(EDAS) (point 8)"; "(point 8; annex 'SAM aprašas v07' to V-243) and must be signed with a qualified electronic signature (point 8; 'saugiu…'" | V-243 p. 8 ("SD pranešimai teikiami siunčiant elektroninį dokumentą per EDAS … FFData … pasirašyti saugiu elektroniniu parašu … kvalifikuotu sertifikatu"); o texto termina no p. 127 (249 e 250 não existem); anexo "SAM aprašas v07" |
| Report Matrix!I2 | "consolidated redaction in force from 2026-01-01 - SOURCE NOT ARCHIVED … HTTP 403 … point references … (… 249, 250) remain as in v1.0 pending archiving. Archived locally: the 2015-09-17 wording …, whose numbering differs (… 103.6-103.7; late filing = 104.2; non-working-day deadline = 111); " | "consolidated redaction in force from 2026-10-03 (e-TAR TAR.34A6775CE75B), archived by Mercans Global Compliance on 2026-10-30 (file 2026-10-30-V-243-suvestine-2026-10-03). The Rules end at point 127; every point cited in this spec was re-checked against that text on 2026-10-30. Renumbering from the 2015-09-17 wording (lrs494520): PT-SAM3SD / PT-SAM3SD-M / PT-SAM3SDP annexes = points 86.6-86.8 (were 103.6-103.7); late filing = point 52 with 91.3.1 (was 104.2); non-working-day deadline = point 125 (was 111); " | V-243 cabeçalho "Suvestinė redakcija nuo 2026-10-03"; p. 86.6-86.8, 52, 91.3.1, 125, 127 |
| Population Rules!C4 | "…stated in the annex (point 92.4) and only the affected insured persons listed (points 95.4 and 96.4)." | "…stated in the annex (point 92.4). P35 belongs to the written (paper) correction route (points 93-97): the employer files a written request together with a new SAM marked 'x' in P35 (points 93-94), P14T and P17T give the corrected year and month (points 95.1-95.2), and the annexes list only the insured persons whose data change (points 95.3-95.4; points 96.3-96.4 for quarters up to 2009-12-31)." | V-243 seção "Duomenų tikslinimas rašytiniu būdu", p. 93, 94 ("teikia naują SAM pranešimą (laukelyje P35 pažymima „x“)"), 95 ("nuo 2010 m. sausio 1 d."), 95.1-95.4, 96 ("iki 2009 m. gruodžio 31 d."), 96.3-96.4 |
| Population Rules!D4 | "correction affecting one employee only, where points 95.4 and 96.4 require a partial annex;" | "correction affecting one employee only, where on the written route with P35 the annexes list only the insured persons whose data change (points 95.3-95.4; 96.3-96.4 for quarters up to 2009-12-31);" | V-243 p. 94, 95.3-95.4, 96.3-96.4 |
| Population Rules!C13 | "Points 8 and 249: …"; "Point 250 and the SAM v07 data structure description (DSA, V-243 in the V-624 wording)"; "signed with a qualified electronic signature by the manager"; "Point 84.1 notes the employer is informed of acceptance through EDAS." | "Point 8: …"; "Point 8 and the SAM v07 data structure description (DSA, annex 'SAM aprašas v07' to V-243, in the V-624 wording)"; "…signature (point 8) by the manager"; "Point 84.1: the employer is informed through EDAS of the territorial branch decision on data correction or on not recording the submitted data (within 3 working days, point 84); acceptance of the SAM file itself is shown by the DataService status (getDocumentStatus)." | V-243 p. 8; p. 84 ("sprendimą dėl apdraustųjų duomenų tikslinimo ar sprendimą neįrašyti … per 3 darbo dienas"); p. 84.1 ("Draudėjas informuojamas EDAS priemonėmis"); getDocumentStatus: extrato DataService já citado na v1.1 |
| Population Rules!D13 | "(the archived 2015 wording, point 111, moves the deadline to the next working day; the numbering in force is not archived)" | "(point 125 moves the end of the deadline to the next working day for SD notifications, which include SAM under point 4.7)" | V-243 p. 125 ("Jeigu paskutinė termino diena tenka ne darbo dienai (šeštadienis ir sekmadienis) ar oficialios šventės dienai, SD pranešimo pateikimo termino pabaigos data laikoma po jos einanti darbo diena"); p. 4.7 (Forma SAM é SD pranešimas) |
| Population Rules!D7 | "whether the Guarantee Fund, the Long-term Employment Benefit Fund and the 3 % pension accumulation also stop at the ceiling is an open item (no source read);" | "position, to confirm with Sodra/BAU how the SAM reports the month the ceiling is crossed (P3, A11, A12): the Guarantee Fund 0,16 % (Law XII-2604 art. 5(3)), the Long-term Employment Benefit Fund 0,16 % (art. 14(3)) and, for participants, the 3 % pension accumulation contribution (Law IX-1691 art. 8(1)) are charged on the income on which social insurance contributions are calculated, at rates set by those laws and not by the budget-indicators law, so they continue above the ceiling together with PSD 6,98 %;" | I-1336 art. 10(9) (0 % acima de 60 VDU só para as contribuições com taxa da lei anual de indicadores; PSD excluído); XII-2604 art. 5(3) ("0,16 procento … nuo … pajamų, nuo kurių skaičiuojamos valstybinio socialinio draudimo įmokos"), art. 14(3) (idem, ILDIF); IX-1691 art. 8(1) ("3 procentai dalyvio pajamų, nuo kurių skaičiuojamos valstybinio socialinio draudimo įmokos") |
| SAM Spec!M13 | "Points 95.4 and 96.4 add that in a correction the SAM3SDP annex lists ONLY the insured whose information changes, not the whole population." | "P35 itself belongs to the written correction route (points 93-97): a new SAM marked 'x' in P35 is filed with a written request (points 93-94), and its SAM3SDP annex then lists ONLY the insured persons whose data change, not the whole population (point 95.4; point 96.4 for quarters up to 2009-12-31)." | V-243 p. 93, 94, 95.4, 96, 96.4 |
| SAM Spec!T13 | "since points 86 and 91-96 describe PT as the correction mechanism." | "since points 86-92 describe PT as the electronic correction mechanism and points 93-97 the written route with P35." | V-243 seções "Duomenų tikslinimas elektroniniu būdu" (p. 86-92) e "…rašytiniu būdu" (p. 93-97) |
| SAM Spec!M29 | "which point 88 and the signing provision require." | "which point 8 requires (point 88 sets the same requirement for PT requests)." | V-243 p. 8 (SD pranešimai) e p. 88 ("PT elektroninis prašymas … turi būti pasirašytas saugiu elektroniniu parašu") |
| SAM Spec!T46 | "Residual only: confirm whether the 3 % … is included in P3, and the legal basis of the Guarantee Fund and Long-term Employment Benefit Fund rates (read on the Sodra tariff page only)." | "Residual only: (a) whether the 3 % … (Law IX-1691 art. 8(1)) is included in P3; (b) how the SAM reports the month in which the 60 VDU ceiling is crossed (P3, A11, A12) - to confirm with Sodra/BAU. Legal basis now read: Guarantee Fund 0,16 % (Law XII-2604 art. 5(3)) and Long-term Employment Benefit Fund 0,16 % (art. 14(3)) … Position on the ceiling: I-1336 art. 10(9) applies the 0 % rate above 60 VDU only to contributions at rates approved by the annual budget-indicators law and excludes PSD; … PSD 6,98 %, Guarantee Fund 0,16 %, Long-term Employment Benefit Fund 0,16 % and, for participants, 3 % continue above the ceiling." (a frase final sobre "employer plus employee" não mudou) | I-1336 art. 10(9); XII-2604 art. 5(3), 14(3); IX-1691 art. 8(1) |
| Version Control!A4:E4 (linha nova) | (não existia) | `LT-SODRA-003` · `1.2` · `2026-10-30` · `Mercans Global Compliance` · "V-243 point references re-checked against the consolidated text in force from 2026-10-03: points 249/250 replaced by point 8; non-working-day rule = point 125; scope of points 84.1, 88, 95.4/96.4 corrected. 60 VDU ceiling: Guarantee Fund, Long-term Employment Benefit Fund and 3 % read as continuing (XII-2604 art. 5(3), 14(3); IX-1691 art. 8(1)); SAM reporting of the crossing month to confirm with Sodra/BAU." | este changelog |

**Não alterado (de propósito):** Version Control!E2 (linha histórica da v1.0, cita "redaction in force from 2026-01-01"); Field Options!E33 e demais linhas OK do recheck (correções "opcionais"); Population Rules!C7 (continua dizendo que o preenchimento de A11/P3/A12 no teto não está na instrução, o que segue verdadeiro).

## Achado 4 (teto de 60 VDU): como ficou escrito
Escrito como **posição** com base legal, não como prática da Sodra. A célula diz "to confirm with Sodra/BAU how the SAM reports the month the ceiling is crossed". Confiança 85%: nenhum texto oficial da Sodra afirma isso para o Fundo de Garantia e o ILDIF (item B11 da lista do BAU).

## Conferência
- `validate_workbook.py --artifact RSPEC`: **PASS** (blocker 0, major 0, minor 0; inclui o lint C29).
- `check_sam.py` (da pasta 2026-10-29, aceita caminho) contra o FFData oficial: **106 OK, 0 FAIL** (igual à v1.1).
- Diff openpyxl (somente leitura) de todas as células, v1.1 × v1.2: **16 diferenças de valor**, exatamente as da tabela; 0 diferenças só de estilo; todas as 16 com `FFDDEBF7`. Fonte, borda e alinhamento iguais ao original em todas. Nenhuma célula de texto começa com "=".
- Partes do zip: 4 alteradas (sheet1, 2, 4, 7), mesma ordem de entradas.

## Frentes
| Data | Frente | O quê |
|---|---|---|
| 2026-10-30 | pipeline | v1.2 gerada a partir da V-243 vigente e do achado 4; só local |

## 2ª rodada (30/10, tarde): etapa 1, itens nossos
A v1.2 ainda não tinha saído do computador, então foi regerada com o mesmo número (`build_specs_v12.py`, a partir da v1.1). Agora são 30 células alteradas contra a v1.1, todas em `FFDDEBF7`.

| Célula | O que mudou | Fonte |
|---|---|---|
| Population Rules!C7 | Caso (i), teto: A11, P3 e A12 seguem os pontos 55.1, 55.5 e 55.2 (A12 = A11 × P3). A Sodra recalcula o mês sozinha e avisa a nova tarifa, que vira o P3 do mês seguinte. Caso (ii), piso do salário mínimo: continua aberto | Sodra, "Įdarbinimas, pranešimai, įmokos ir tarifai" (2026-05-19); V-243 p. 55.1, 55.2, 55.5 |
| Population Rules!D7 | Mesma regra no caso de borda; mantida a posição sobre o que continua acima do teto | idem; XII-2604 art. 5(3), 14(3); IX-1691 art. 8(1) |
| SAM Spec!T46 | Resíduos (a) 3 % no P3 e (b) mês do teto: fechados | tabela de tarifas da Sodra ("Bendras su 3 % kaupimu", 24,27); página acima |
| SAM Spec!M47 | Teto deixa de ser "regra aberta"; o piso do salário mínimo continua aberto | idem |
| SAM Spec!J69, M69 | Divergência 5 × 11 resolvida: o formulário em vigor (`SAM-v07.mxfd` de 2025-12-31) tem 5 casas e só aceita tarifa de 0,01 a 99,99 | `raw/docs/oficiais/LT/2026-10-30-Sodra-SAM-originais/x_zip/SAM-v07.mxfd`, função `ValidateRow3SD` |
| Field Options!E53–E60 | "inclusion in P3 is NOT VERIFIED" → confirmado | tabela de tarifas da Sodra |
| Report Matrix!F2 | Regra do dia útil seguinte (ponto 125) | V-243 p. 125 |
| Report Matrix!J2 | Itens abertos (1) e (2) reduzidos: sobram o piso do salário mínimo e o P3 dos códigos 06, 09 e 10 | — |
| Version Control!E4 | Resumo da 2ª rodada | — |

Testes: validate RSPEC **PASS (0/0/0)**; `check_sam.py` contra o FFData oficial **106 OK / 0 FAIL**; diff × v1.1: 30 células, todas destacadas; lint C29 limpo.

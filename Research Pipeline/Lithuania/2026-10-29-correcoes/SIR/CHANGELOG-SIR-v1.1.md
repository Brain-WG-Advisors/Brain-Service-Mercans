# LT-SIR-001 v1.1: changelog (29/10/2026)

Hub: [[Lituania]] · Base: [[Research Pipeline/Lithuania/2026-10-27-SIR/CONFERENCIA]] (v1.0) · Achados: [[Research Pipeline/Lithuania/2026-10-28-validacao/VAL-SIR|VAL-SIR]] (F01–F20) · Passe de bastão: [[Research Pipeline/Lithuania/2026-10-28-validacao/PASSE-DE-BASTAO]]

Só local. Nada foi para Drive, ticket ou e-mail. A pasta `2026-10-27-SIR/` e `raw/` não foram alterados.

## Arquivos
| Arquivo | O quê |
|---|---|
| `LT-SIR-001-v1.1.docx` | Entrega. md5 `bbeb8f25125693ec53335e8a54380686` (após a revalidação; antes `762761884127db9ce32349c82a744714`). 22 páginas, 24 tabelas, 201 trechos com sombreamento `DDEBF7` (exatamente o que mudou) |
| `sections/s00–s08.md` | Fonte do texto (sem marcadores desde a correção R4) |
| `build_sir_docx_lt.py` | Gerador (cópia do v1.0 com: sombreamento `w:shd fill="DDEBF7"` calculado contra a v1.0 — todo parágrafo/célula cujo texto não existe na v1.0, renderizada com o gerador da v1.0 em modo só leitura, sem gravar bytecode na pasta da v1.0; código dentro de negrito sem crase (F08); rodapé com campo PAGE; `w:updateFields`; core properties) |
| `update_toc_word.ps1` | Word (COM) atualiza o sumário e salva |
| `finalize_sir_docx.py` | Recoloca `w:updateFields` e as core properties (o Word tira o primeiro e grava o usuário em lastModifiedBy) |
| `build_lt_sir.py` | Gerador antigo, só histórico (copiado sem alteração) |

Ordem para regerar: `python build_sir_docx_lt.py` → `powershell -File update_toc_word.ps1` → `python finalize_sir_docx.py`.

## Tabela de alterações
| Achado | Seção | Antes (v1.0) | Depois (v1.1) | Fonte (arquivo + §/página) |
|---|---|---|---|---|
| F01 (MAJOR) | 1 intro; 1.1 IN-01; 1.2 IN-01; 2 intro; 2.1 OUT-02; 3.3; 8.2 G5 | IN-01 = resposta de OUT-01 **e** OUT-02 | IN-01 é retorno do OUT-02 **só se** o DataService aceitar o NP-SD2 (G5); senão não há retorno de máquina e o status é lido no EDAS. G5 diz que, até confirmar, IN-01 não é o retorno do OUT-02 | Extrato DataService (`raw/docs/oficiais/LT/2026-10-27-Sodra-SAM/2026-10-27-sodra-EDAS-DataService_extrato.md`, op. 1, 3, 5: docUID só de `uploadEdasDraft`/`sendSignedDocument`; `getPossibleDocuments`); s02 v1.0 2.2 OUT-02 |
| F02 (MAJOR) | 0.1 Scope; 2.4; 8.2 G13 | 9-SD listado entre "outside the report set" | Linha própria em 2.4: "Open scope decision (G13)", integração de licenças no escopo desde 27/10, decidida junto com a integração de licenças (data retirada na correção R2); G13 nova (Mercans Compliance; cliente). Scope cita a decisão em aberto | Hub `paises/Lituania.md` Pendências (SteerCo 27/10: "Leave reporting integration has been added to scope"; "pesquisar o 9-SD… acrescentar ao SIR"; "BO-35 vence 11/11"; "o 9-SD pode entrar na integração de licenças"); S2 (extrato: 9-SD pelo mesmo canal) |
| F03 (MAJOR) | 1.1/1.2 IN-04 (nova); 3.2 linha nova; 3.3; 5.2; 6.2 | "VMI notifies electronically" | Upload e web service: erros chegam **depois do processamento** aos contatos cadastrados no EDS do pagador representado, em "NUSTATYMAI → Atstovavimas → Atstovaujamas asmuo → Atstovaujamo mokesčių mokėtojo ryšio priemonės"; sem contato válido, a VMI usa contatos de outros sistemas. Recomendação de caixa monitorada. On-line: erro na hora | VA-72 LT `EDS_taisykles_VA72_LT.docx` §26 (*"21.2 ir 21.3 … informuojamas EDS nurodytais kontaktais po pateiktų duomenų apdorojimo"*), §13, §14 (contatos usados para status, erros e prazos de correção); EN `EDS_rules_VA72_EN.docx` §26; `EDS_HelpItem_Email_pranesimai.html` |
| F04 (MAJOR) | 5.1 (2 linhas novas); 6.3; 8.1 G10, G14 | Só WSDATA e ERR | (a) Validação de conteúdo do SAM: série **C23xx**, exemplos C2330/C2336/C2338/C2347/C2344 como citados pela spec (A1); catálogo não arquivado → **G14**. (b) Correção do SAM: a DSA v07 tem P35 *"Patikslintas pranešimas"* + P14T/P17T; o texto de 2015 das regras SD (ponto 76: corrigir sem demora; 103.6–103.7: PT-SAM3SD, PT-SAM3SDP); A1 registra PT e código 01 para atraso; o texto vigente das regras não está em disco → G10 reescrita | DSA SAM v07, PDF `C:\Users\instituto\Documents\youtrack_tickets\drive\2026-10-10-Lithuania\Lithuania\12- Country Report Codes\SODRA - Social Security\SAM specifications - Lithuanian.pdf` (md5 `1db02c71a74cc0bed1b5c5f2cd01d53b`; V-243 na redação V-624 de 2018-12-07), p. 1 (UTF-8, XML 1.0) e p. 10 (P35, P14T, P17T); `raw/…/2026-10-27-Sodra-SAM/2026-10-27_LRS_V-243_2010-06-04_redakcija-2015-09-17_lrs494520.html` pontos 76, 103.6, 103.7; spec SAM v1.0 `SAM Spec!M9, M17, M19, M47`, `Payroll Scope Summary!B22`, `Report Matrix!F2` |
| F05 (MAJOR) | Document Control (novo) | Sem bloco | Tabela 10×2 (Document ID, Version, Country, Jurisdictions, Tax year, Currency, Prepared by, Status, Related deliverables) + "Version history", no modelo do BE | `~/mercans-pipeline/BE-compliance/03-statutory-integrations/BE-SIR-001-v1.0.docx` (md5 `835d476f…`), tabela 1 e heading "Version history". Obs.: a cópia de Downloads/Drive do BE (md5 `ee9b71b5…`) não tem o bloco |
| F06 (MAJOR) | Appendix A intro; S1–S4 coluna versão; 0.5; 8.2 G16 | "Copies and extracts are kept under raw/…" | S1–S4: "extract only"; os originais não estão arquivados (sodra.lt recusa download por script); a DSA oficial do SAM (S11) está no Drive do país, *12- Country Report Codes / SODRA - Social Security*. G16 nova: salvar PDF DataService, `sam-v07.mxfd`, páginas S2/S4 | `raw/…/2026-10-27-Sodra-SAM/` (só extratos `.md`; o DataService "lido com pdf.js… não salvo em disco"; MXFD "lido em memória… não salvo"); pasta local do Drive acima |
| F07 | 3.2 EDS portal | "(not needed with a Lithuanian residence permit)" ligado ao certificado | O parêntese dispensa o **pedido** dos meios da VMI, não o certificado | `EDS_HelpItem_Uzsienio_pilietis.html` (*"…prašymo nurodyto pirmame punkte, pildyti nereikia"*) |
| F08 | 4.2 | `Web service \`EDSWebServiceUploadFile\`` com crases | Gerador trata código dentro de negrito; 0 crases no docx | Teste mecânico (abaixo) |
| F09 | 1.1 IN-02 | Sem actuality | `DeclarationActualityStateCode`: 10 current, 11 current by correction, 20 not current | Especificação `raw/…/2026-10-27-VMI-reports/EDSUplaodFileViaWebService-v2-2010_08_19.doc` (DeclarationDataResult; tabela *"Deklaracijos būsenų aktualumo kodai"*: 10 Aktuali, 11 Aktuali dėl tikslinimo, 20 Neaktuali); `EDSWebServiceUploadFile_WSDL_live.xml` l. 74–75 |
| F10 | 2.1 OUT-02 | "sickness and maternity benefit" | "sickness benefit (the instruction also covers care of a family member, S4 points 60-66) and maternity benefit" | Extrato NP-SD2 p. 60–66 (B3–B4 "só cuidado de familiar"). Só extrato (G16) |
| F11 | 2.2 OUT-01 | "EDAS account (on-line form or FFData file)" | "EDAS account (FFData file, e.g. prepared with the free ABBYY eFormFiller program)" | Extrato S2 (*"Programa gratuita de preenchimento: ABBYY eFormFiller 2.5 v6"*) |
| F12 | 3.2 EDS portal, Source/Who | Source "S9" | Who: "Representatives with EDS representation rights for the payer"; Source "S9; S6 §7; S8" | VA-72 LT §7 (*"EDS naudotojas, norėdamas atlikti veiksmus EDS, turi turėti EDS atstovavimo teises"*; numeração reconstruída pela numeração automática do docx, conferida com §21/§24/§26/§27); S8 `EDS_Ziniatinklio_paslauga.html`. Obs.: o VAL sugeriu "§18 ss."; pela contagem, a regra de representação é o §7 (o §18 trata do Mano VMI) |
| F13 | 7.2 S3 | "with WSDL and XSD" | "with WSDL" | Extrato DataService (só "Endpoint (WSDL, p. 15)") |
| F14 | 7.3 S9 | "2026-08-27" | "News 2026-08-27; help page undated (read 2026-10-27)" | `EDS_Naujienos.html` (*"2026-08-27 / Dėl prisijungimo prie EDS"*); ajuda sem data |
| F15 | 7.3 S6; 8.1 G4; 1.1 IN-04 | §27 ausente; G4 sem âncora | S6 lista §7, §13, §14, §21, §24, §26, §27; G4 aponta IN-04 (S6 §26, §27; informacinis pranešimas); IN-04 registra "NOT LOCATED as a machine channel" | VA-72 §27 (FR1025, ordem VA-135); IN GPM313 `nuo_2026` §19.1, §20; IN GPM312 §64.1, §66 |
| F16 | 2.2 OUT-03/04; 6.1 (2 linhas novas + nota); 8.1 G15 | Só "15th"/"15 February" | Prazos de período parcial (30 dias de falência/reestruturação; antes do fim da atividade em liquidação/reorganização). Dia útil seguinte **não** afirmado: nenhuma fonte primária em disco → lacuna G15 | IN GPM313 `x_IN_GPM313_PDF/IN_GPM313_nuo_2026.pdf` §16, §17; `IN_GPM312.pdf` §61, §62; busca por "darbo dien/poilsio/švenčių" nas duas IN: 0 ocorrências |
| F17 | 5.2 (linha nova + correção); 6.3 | Só refile | Acoplamento GPM312→GPM313 (§65); prazo do informacinis pranešimas (§20/§66); anulação só no portal ("Deklaravimas → Pateikti dokumentai ir formos → Pateiktos formos" → "Anuliuoti", às vezes com aprovação de servidor); web service só tem `SubmitFile` e `CheckFileState` | `IN_GPM312.pdf` §63–§66; IN GPM313 §18–§20; `EDS_HelpItem_Formu_statusai.html`; WSDL ao vivo |
| F18 | 0.1 Scope | "named for the Accenture Lithuania implementation" | "the two integrations in scope are…"; 0 ocorrências do nome do cliente | — |
| F19 | Docx | TOC "Right-click…"; sem updateFields; rodapé sem página; author python-docx, datas 2013, título vazio | TOC preenchido pelo Word (40 entradas) + `w:updateFields`; rodapé "… \| Page N" (campo PAGE); author/lastModifiedBy "Mercans Compliance", título "Lithuania Statutory Integration Register (LT-SIR-001 v1.1)", created/modified 2026-10-29 | Teste mecânico (abaixo) |
| F20 | Estrutura | Sem numeração 0.x, sem 3.4/6.3/8.4, sem "Appendix" | "0. Purpose, Scope and Audit Compliance" com 0.1–0.5; **0.4** completude vs Payroll Regulation Guide 2026 (P377–P402; 1-SD P206); **3.3** per-integration authentication lookup; **6.3** correction windows; **Appendix A. Sources** / **Appendix B. Open Gaps** com 8.1/8.2/8.3 ("What this register does not claim"); versões "v1.0"/"v1.1" | BE-SIR-001 (headings); `2026-10-27-atualizacao-2026/ccg2026.txt` P206, P377–P402; A4 nova em 7.1 |
| Referências | Capa; Document Control; 2.3; 7.1 | SAM v1.0; GPM313/GPM312 v1.1 | SAM v1.1 (LT-SODRA-003); GPM313 v1.2 (LT-VMI-001); GPM312 v1.2 (LT-VMI-002) | Pedido da tarefa (correções de 29/10) |
| Version history | Document Control | — | Linha v1.1, 29-Oct-2026, curta, só o confirmado | — |

Também (consequência dos achados, sem número no VAL): 3.1 "Who" do DataService passou de "Any EDAS user who has enabled the service" para "An EDAS user who has enabled the service in the EDAS user settings" (afirmação 38 NOT FOUND); 4.1 `sendSignedDocument` deixou de dizer "starts registration" (afirmação 40 NOT FOUND); 4.1 cita a DSA (S11) para XML 1.0/UTF-8. Fontes novas: S10 (ajuda do EDS: contatos e anulação), S11 (DSA SAM v07), S12 (regras SD V-243, texto consolidado de 2015, só histórico), A4 (Payroll Regulation Guide 2026). Lacunas novas: G13, G14, G15, G16.

## O que ficou sem corrigir (e por quê)
- **Originais da Sodra (F06):** sodra.lt responde 403 a download por script; os originais S1–S4 continuam só como extratos. O documento agora diz isso e a G16 registra como fechar. As afirmações de S1–S4 (incluindo F10 e F11) dependem do extrato.
- **Catálogo C23xx (F04a):** o `SAM-erros.pdf` não está em disco. Os códigos foram citados como estão na spec SAM **v1.0** (`SAM Spec!M9/M17/M19/M47`), e conferidos depois pela revalidação contra a SAM v1.1: iguais (M17 C2330, M9 C2336, M19 C2338/C2347, C2344).
- **Rota atual de correção do SAM (F04b/G10):** o texto vigente da V-243 não está em disco (só 2010 e 2015). O SIR traz o que a DSA v07 prova e marca o resto como aberto.
- **Dia útil seguinte (F16):** sem fonte primária (Lei de Administração Tributária e regras gerais SD TAR.34A6775CE75B não estão em disco) → G15, não afirmado. A spec GPM312 v1.1 cita 2026-02-16, mas não foi usada como fonte.
- **Referências SAM v1.1 / GPM313 v1.2 / GPM312 v1.2:** os arquivos existem em `2026-10-29-correcoes/` com esses números (conferido pela revalidação).
- **F19 no gerador da Bélgica:** fora do escopo (só LT). O `build_sir_docx.py` do BE continua com os mesmos defeitos.
- **F20 parcial:** não foi criado "0.2 Build order" nem "6.4 time-boxed items" do BE; não se aplicam aqui (o SIR LT foi feito depois das specs; não há item com prazo além da G13, que já tem data).
- **9-SD (F02):** a entrada da integração de licenças no escopo vem do hub (ata do SteerCo), não de fonte externa; a decisão é do usuário com o cliente. O SIR não cita data (11/11 é o vencimento do BO-35, a confirmar no hub).

## Testes
- Abre com python-docx: 163 parágrafos, 23 tabelas, 1 seção; `inspect_docx.py` (mercans-artifact-toolkit): 40 headings (11 H1, 29 H2), **C29 residual-marker scan: clean**.
- Lint próprio com `\b` (TODO, TBD, FIXME, XXX, placeholder, to be confirmed/verified, VERIFY, `[[`): 0. Crases: 0. "Accenture": 0. Marcadores `{+`: 0.
- Markdown × docx: 491 trechos das seções s00–s08 encontrados no docx; 0 faltando.
- Chaves: A1–A4, S1–S12 e G1–G16 usadas no texto existem nos registros (Appendix A/B), e toda chave do registro é usada.
- `settings.xml` com `w:updateFields val=true`; campo PAGE no rodapé; core properties: author "Mercans Compliance", lastModifiedBy "Mercans Compliance", título correto, created/modified 2026-10-29.
- Sombreamento (após R4): 201 ocorrências de `w:fill="DDEBF7"`. Diff independente v1.0 docx × v1.1 docx em 580 parágrafos/células (sem o sumário): 0 alterados sem destaque, 0 com destaque sem alteração. Os 5 trechos do R4 (0.4 "or a notice", 2.4 1-SD/P206, intro da seção 3, 4.2 web service, bullets do 8.3) estão com destaque. A 1ª rodada foi conferida visualmente no PDF do Word (páginas 3 e 6).
- md5 `LT-SIR-001-v1.1.docx` = `bbeb8f25125693ec53335e8a54380686` (1ª rodada: `762761884127db9ce32349c82a744714`).
- Reteste após R1–R7: abre com python-docx (169 parágrafos, 24 tabelas); `inspect_docx.py` C29 clean; lint `\b` 0; crases 0; "Accenture" 0; "11 November" 0; "29-Oct" 0; markdown × docx 506/506; `updateFields` presente; core properties como antes; Version history só em ISO (2026-10-27, 2026-10-29).

## Revalidação (REVAL-SIR-v1.1.md: 0 BLOCKER, 0 MAJOR, 7 MINOR) e correções
| Achado | Seção | Antes | Depois | Fonte |
|---|---|---|---|---|
| R1 | 5.1, G10, 8.3 | Texto vigente da V-243 "not available"; numeração de 2015 | **Sem mudança no SIR.** A SAM v1.1 cita a V-243 na redação V-683 (consolidada, vigente desde 2026-01-01), mas não há fonte primária em disco: a origem é o `SAM-V243-consolidado.pdf` citado na Version Control da SAM v1.0, que não existe em disco (busca em `C:\Users\instituto` por V243/V-243/V-683: só as redações de 2010 e 2015 em `raw/`). Células da SAM v1.1 que citam sem fonte em disco: `Report Matrix!I2` (V-683), `Report Matrix!F2` (91.3.1), `Report Matrix!G2` (250), `Payroll Scope Summary!B22` (86.6–86.8), `SAM Spec!M13` (86.6–86.8), `SAM Spec!T13` (86), `SAM Spec!M29` (88), `Field Options!E29, A32, A33, A34` (86.6–86.8), `Field Options!E33` (86.7), `Field Options!A31` (91.3.1), `Population Rules!C4` (86.6–86.8, 92.4, 95.4), `Population Rules!D4` (95.4) — repassado à coordenação | busca em disco; SAM v1.1 |
| R2 | 2.4, G13 | "target date 11 November 2026" | "still to be decided as part of that integration" / "decided together with that integration"; sem data | `paises/Lituania.md` l. 83 ("confirmar … o prazo (BO-35 vence 11/11)") |
| R3 | Version history | v1.1 "29-Oct-2026" | "2026-10-29" (ISO, como o BE-SIR-001) | BE-SIR-001 Version history |
| R4 | Todo o docx | 192 destaques por marcador manual (5 alterações sem destaque, ~12 células sem mudança com destaque) | Destaque calculado contra a v1.0: 201, exato (ver Testes) | diff v1.0 × v1.1 |
| R5 | Document Control, Status | "Issued" | Sem mudança, por instrução (modelo BE para versão emitida; Drive só com ok) | — |
| R6 | 0.6 (antes 0.5) | Só "read on 27 October 2026" | + "S11 and S12 were read on 29 October 2026." | Appendix A |
| R7 (F20) | 0.2 nova; 5.3 nova | Sem "Build order" e sem "Summary" | 0.2 Build order (Stage 6 depois das specs; 2.3 nomeia as versões; NP-SD2 sem spec, G5; v1.1 após revisão independente). 5.3 Summary — onde há e onde não há modelo de erro, só com o que já está em 5.1/5.2 e nas lacunas. 0.x renumerado (0.3 Source discipline … 0.6 Currency); A4 aponta para a Section 0.5 | O próprio documento (2.3, 5.1, 5.2, G1, G4, G5, G10, G14) |

## Próximo (com ok do usuário)
1. Revalidação independente da v1.1 (outra instância).
2. Drive 19 - Statutory Integrations: subir como v1.1 (não sobrescrever a v1.0); link na SR-479 e no monday; regra 9 (país ativo).
3. Decidir G13 (9-SD) junto com a integração de licenças (BO-35 vence 11/11, a confirmar).

## Frentes que mexeram
| Data | Frente | O quê |
|---|---|---|
| 2026-10-29 | lituania (subagente) | v1.1 local: F01–F20 conforme a tabela; nada no Drive/tickets/e-mail |
| 2026-10-29 | lituania (subagente) | Correções da revalidação R1–R7 (R1 e R5 sem mudança, justificados); docx regerado, md5 bbeb8f25… |

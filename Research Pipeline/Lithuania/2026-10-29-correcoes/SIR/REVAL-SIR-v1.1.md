# REVAL-SIR: revalidação independente do LT-SIR-001 v1.1 (29/10/2026)

Hub: [[Lituania]] · Achados de origem: [[Research Pipeline/Lithuania/2026-10-28-validacao/VAL-SIR|VAL-SIR]] (F01–F20) · Changelog do construtor: [[Research Pipeline/Lithuania/2026-10-29-correcoes/SIR/CHANGELOG-SIR-v1.1|CHANGELOG-SIR-v1.1]] · Base: [[Research Pipeline/Lithuania/2026-10-27-SIR/CONFERENCIA]]

- **Revisor:** auditor independente (não construiu a v1.1). Só leitura: nenhum arquivo existente foi alterado. Este relatório é o único arquivo novo.
- **Artefato:** `LT-SIR-001-v1.1.docx`, md5 `762761884127db9ce32349c82a744714`, igual ao md5 declarado no changelog.
- **Base:** `2026-10-27-SIR/LT-SIR-001-v1.0.docx`.
- **Specs irmãs conferidas** (existem em `2026-10-29-correcoes/`):

| Spec | md5 | Version Control |
|---|---|---|
| `LT-SODRA-003-SAM-Spec_v1.1.xlsx` | `f3ce3b9d…` | linha 1.1, 29-Oct-26 |
| `LT-VMI-001-GPM313-Spec_v1.2.xlsx` | `4fc13b96…` | linha 1.2, 29-Oct-26 |
| `LT-VMI-002-GPM312-Spec_v1.2.xlsx` | `81148366…` | linha 1.2, 29-Oct-26 |

## Veredito
**Aprovado com ressalvas menores (pode seguir para o ok do usuário). 0 BLOCKER · 0 MAJOR · 7 MINOR.**
- Os 6 MAJOR da VAL (F01–F06) estão fechados. F06 está fechado como "declarado". Os originais da Sodra continuam fora do disco e isso está registrado na G16.
- Das 14 MINOR (F07–F20), 13 estão fechadas e 1 está parcial (F20).
- Reabri na fonte primária as afirmações novas ou alteradas que eram verificáveis. Nenhuma está errada.
- Os pontos abaixo são de redação, coerência com a spec SAM v1.1 e forma (sombreamento e data).

## 1. Achados desta revalidação

| # | Seção | Problema | Fonte | Sev. |
|---|---|---|---|---|
| R1 | 5.1 "Correction of filed SAM data"; G10; 8.3 | O SIR diz *"The text of the SD rules in force today was not available"*. A spec irmã A1 (SAM v1.1) diz o contrário: cita o texto vigente da V-243 (*"in the wording of order No. V-683 of 2016-12-23 … consolidated redaction in force from 2026-01-01"*) e os pontos 86.6–86.8 (PT-SAM3SD, PT-SAM3SD-M, PT-SAM3SDP) e 91.3.1 (código 01). O SIR usa a numeração de 2015 (103.6/103.7) e não liga uma numeração à outra. Não há afirmação falsa (o SIR deixa a rota em aberto, e a A1 também pede confirmação à Sodra, `Population Rules!C4`), mas o leitor vê duas numerações para os mesmos anexos | A1 `Report Matrix!I2`, `Payroll Scope Summary!B22`, `SAM Spec!M13`, `Field Options!A32–A34`, `Population Rules!C4`; `raw/…/Sodra-SAM/…redakcija-2015-09-17_lrs494520.html` pontos 76, 103.6, 103.7 | MINOR |
| R2 | 2.4 9-SD; G13 | *"target date 11 November 2026"*: o hub não traz essa data como prazo da decisão sobre o 9-SD. Diz *"confirmar com o Wallisson o prazo (BO-35 vence 11/11)"*: é o vencimento de um item interno, e o próprio hub pede que o prazo seja confirmado | `paises/Lituania.md` l. 83 | MINOR |
| R3 | Version history | Datas em dois formatos na mesma tabela: v1.0 "2026-10-27" e v1.1 "29-Oct-2026". O modelo BE-SIR-001 usa ISO (2026-08-14) | BE-SIR-001 v1.0 (md5 `835d476f…`), tabela Version history | MINOR |
| R4 | Sombreamento DDEBF7 | Texto alterado **sem** destaque: 0.3 *"…a status response or a notice…"* ("or a notice" é novo); 2.4, célula de descrição dos "Other Sodra SD notices" (frase nova sobre o 1-SD/P206; só a 1ª célula tem destaque); intro da seção 3 ("Section 7" → "Appendix A"); 4.2, parágrafo do web service (sem crases, F08); os 4 bullets do 8.3 (novos, só o título tem destaque). Há também células **com** destaque e sem mudança: "OUT-03", "OUT-04", "A1", "S8", "S4 point 76", "Scope", "Deadline", "Sodra", a linha v1.0 do Version history e outras. Total: 192 `w:fill="DDEBF7"`, conferido | diff célula a célula v1.0 × v1.1 (python-docx) | MINOR |
| R5 | Document Control, Status | "Issued", mas a v1.1 é só local (não está no Drive nem na SR-479; o changelog diz "Próximo: revalidação, Drive"). Aceitável se a intenção é emitir assim, mas hoje não é verdade | `CHANGELOG-SIR-v1.1.md` "Próximo" | MINOR |
| R6 | 0.5 / Appendix A | 0.5 diz *"read on 27 October 2026"*; o Appendix A corrige isso (*"S11 and S12 were added on 29 October 2026"*). O 0.5 ficou incompleto. No `s00_control.md` o marcador `{+}` está no meio do parágrafo, e o parágrafo inteiro sai com destaque | `sections/s00_control.md` l. 56 | MINOR |
| R7 | F20 (estrutura) | Continuam faltando o 0.2 "Build order" e o 5.6 "Summary" do BE. A justificativa do changelog para o 0.2 é razoável. Sem impacto de conteúdo | BE-SIR-001, headings | MINOR |

Sem achado em: números, prazos, códigos, endpoints, versões, crases, TODO/TBD/placeholder, nome de cliente e dados pessoais.

## 2. Status F01–F20

| ID | Status | Onde na v1.1 | Observação |
|---|---|---|---|
| F01 | Fechado | Intro 1, 1.1 e 1.2 IN-01, intro 2, 2.1 OUT-02, 3.3, G5 | IN-01 só vale para o NP-SD2 se a G5 confirmar. Coerente em todos os pontos |
| F02 | Fechado (R2) | 0.1 Scope, 2.4, G13 | 9-SD como decisão aberta. A data 11/11 é fraca (R2) |
| F03 | Fechado | IN-04 (novo), 3.2, 3.3, 5.2, 6.2 | Conferido na VA-72 §13, §14 e §26 e no `EDS_HelpItem_Email_pranesimai.html` |
| F04 | Fechado | 5.1 (2 linhas), 6.3, G10, G14 | Os códigos C23xx batem com a spec SAM **v1.1** (M17 C2330; M9 C2336; M19 C2347/C2338; C2344 A12 = A11 × taxa). Coerência em R1 |
| F05 | Fechado (R3) | Document Control + Version history | 9 campos iguais ao BE |
| F06 | Fechado como declarado | 0.5, Appendix A intro, S1–S4 "extract only", G16 | Os originais continuam fora do disco (registrado) |
| F07 | Fechado | 3.2 | O parêntese agora dispensa o **pedido**, como diz a ajuda "Užsienio pilietis" |
| F08 | Fechado | 4.2 | 0 crases no docx (sem destaque: R4) |
| F09 | Fechado | 1.1 IN-02 | 10/11/20 conferidos na spec v2.01 (*"Aktuali / Aktuali dėl tikslinimo / Neaktuali"*) e no WSDL l. 75 |
| F10 | Fechado (extrato) | 2.1 OUT-02 | Extrato NP-SD2, p. 60–66 |
| F11 | Fechado (extrato) | 2.2 OUT-01 | Extrato S2 (ABBYY eFormFiller) |
| F12 | Fechado | 3.2 | §7 está correto: pela minha reconstrução da numeração, o §7 trata das *"EDS atstovavimo teisės"* e o §18 do Mano VMI. O construtor acertou ao trocar a sugestão "§18" da VAL |
| F13 | Fechado | 7.2 S3 | "with WSDL" |
| F14 | Fechado | 7.3 S9 | |
| F15 | Fechado | 7.3 S6 (§27), G4 → IN-04 | |
| F16 | Fechado | 2.2, 6.1 (2 linhas + nota), G15 | §16/§17 e §61/§62 conferidos. O dia útil seguinte não é afirmado (G15), coerente com as specs v1.2 |
| F17 | Fechado | 5.2 (linha nova + correção), 6.3 | §63–§66 e §18–§20 conferidos; anulação conferida no S10 |
| F18 | Fechado | 0.1 | "Accenture": 0 no docx, nos XML do pacote e nos `sections/` |
| F19 | Fechado | TOC, rodapé, propriedades | TOC preenchido (40 entradas); `updateFields=true`; campo PAGE; core: título, autor e lastModifiedBy "Mercans Compliance", datas 2026-10-29 |
| F20 | Parcial (R7) | 0.x numerado, 0.4, 3.3, 6.3, Appendix A/B, 8.3 | Faltam o 0.2 Build order e o 5.6 Summary do BE |

## 3. Afirmações novas ou alteradas, reabertas na fonte primária

(L) = fonte primária local lida por mim; (X) = só o extrato do builder.

| Afirmação v1.1 | Fonte reaberta | Resultado |
|---|---|---|
| Erros de upload/web service avisados **depois do processamento** aos contatos do EDS; on-line, na hora (5.2, IN-04) | VA-72 LT §26: *"21.2 ir 21.3 … EDS nurodytais kontaktais po pateiktų duomenų apdorojimo"*; EN §26 igual | CONFIRMED (L) |
| Sem contato válido, a VMI pode usar contatos de outros sistemas (3.2) | VA-72 §26, última frase (EN: *"contact details … specified in other information systems and/or registers of the STI"*); §16 diz o mesmo para e-mail | CONFIRMED (L) |
| Contatos usados para status, erros e prazos de correção (S6 §13, §14) | §13.2 *"kontaktiniai duomenys keičiami EDS"*; §14 *"…jų statusus, klaidas ir jų ištaisymo terminus"* | CONFIRMED (L) |
| Caminho "NUSTATYMAI → Atstovavimas → Atstovaujamas asmuo → Atstovaujamo mokesčių mokėtojo ryšio priemonės"; e-mail e telefone (3.2, S10) | `EDS_HelpItem_Email_pranesimai.html`: *"…gali nurodyti el. paštą ir tel. nr."* | CONFIRMED (L) |
| Direito de representação (S6 §7) | VA-72 §7 *"turi turėti EDS atstovavimo teises"* | CONFIRMED (L) |
| FR1025 diz como e até quando corrigir (5.2) | VA-72 §27 (EN: *"shall specify the manner in which and the time limit…"*) | CONFIRMED (L) |
| Anulação só no portal, às vezes com aprovação de servidor da VMI (5.2) | `EDS_HelpItem_Formu_statusai.html`: *"…„Anuliuoti“"*, *"reikalingas VMI darbuotojo patvirtinimas ar ne"* | CONFIRMED (L) |
| O web service só tem SubmitFile e CheckFileState | WSDL ao vivo l. 100–141 | CONFIRMED (L) |
| GPM313: §12 dia 15; §14 só eletrônico; §16 30 dias de falência/reestruturação; §17 antes do fim da atividade; §18 nova declaração completa; §19.1 informacinis pranešimas; §20 prazo do aviso, e por iniciativa própria os prazos da Lei de Administração Tributária | `IN_GPM313_nuo_2026.pdf` pontos 12, 14, 16–20 | CONFIRMED (L) |
| GPM312: §57 15/02; §59 só eletrônico; §61 e §62 período parcial; §63; §64.1; §65 GPM312 → corrigir o GPM313; §66 | `IN_GPM312.pdf` (VA-9 na redação VA-24) pontos 57–66 | CONFIRMED (L) |
| Nas IN da VMI, prazo em dia corrido e sem regra de dia útil seguinte (6.1 nota, G15) | Texto das duas IN, sem regra de dia útil | CONFIRMED (L) |
| Na instrução do SAM, prazo em dia corrido (6.1 nota) | Extrato S1, ponto 52 | CONFIRMED (X) |
| S11: DSA SAM v07, V-243 na redação V-624 de 2018-12-07; XML 1.0 e UTF-8 na p. 1; P35 "Patikslintas pranešimas", P14T e P17T na p. 10 | `SAM specifications - Lithuanian.pdf` (md5 `1db02c71…`, igual ao do changelog): cabeçalho, §1 *"W3C XML 1.0 … UTF-8"* (página 1), tabela com P14T RevisedCycleYear, P17T RevisedCycleMonth, P35 RevisedDocument (página 10). O mesmo PDF está no Drive `G:\…\Lithuania\12- Country Report Codes\SODRA - Social Security\` | CONFIRMED (L) |
| S12: V-243, texto de 2015: ponto 76 (corrigir *"nedelsdamas"*); 103.6 PT-SAM3SD; 103.7 PT-SAM3SDP | `…redakcija-2015-09-17_lrs494520.html` | CONFIRMED (L) |
| S12 "superseded" | A1 `Report Matrix!I2` cita a redação V-683, vigente desde 2026-01-01 | CONFIRMED (L, pela A1); ver R1 |
| A1 registra os anexos PT e o código 01 para SAM em atraso | A1 `Report Matrix!F2` (*"reason code 01 (late data) under point 91.3.1"*), `Payroll Scope Summary!B22` | CONFIRMED (L) |
| 0.4: o CCG 2026 lista GPM313 e SAM como mensais e GPM312 como anual (P377–P402), com os mesmos prazos; 1-SD no P206 | `2026-10-27-atualizacao-2026/ccg2026.txt` P377–P402, P206 | CONFIRMED (L) |
| Integração de licenças no escopo desde 27/10 (0.1, 2.4) | Hub l. 83 (SteerCo 27/10) | CONFIRMED (L) |
| Prazo-alvo do 9-SD 11/11/2026 | Hub l. 83: só "BO-35 vence 11/11", prazo a confirmar | FRACO → R2 |
| DataService: "An EDAS user who has enabled the service in the EDAS user settings" | Extrato DataService p. 4 | CONFIRMED (X) |
| NP-SD2 também cobre cuidado de familiar (p. 60–66); ABBYY eFormFiller | Extratos NP-SD2 e S2 | CONFIRMED (X), dependente da G16 |

Placar: 21 afirmações reabertas. 18 CONFIRMED em fonte local; 3 só no extrato da Sodra (sem original, G16), das quais 1 conta também como local na linha "Na instrução do SAM"; 1 fraca (R2). **Nenhuma errada.**

## 4. Regressões e coerência
- **Diff v1.0 → v1.1** (comparação de cada parágrafo e célula):
  - Nada útil sumiu. Os trechos removidos foram trocados pela redação corrigida (F01, F07, F10, F11, F13, F14, F18, a rota de correção do SAM e o "starts registration").
  - Os prazos, códigos, endpoints, versões e datas de MXFD da v1.0 continuam idênticos.
- **Markdown × docx:** 491 trechos de `sections/` conferidos. Os 491 estão no docx. O único "faltante" do script vinha de um `{+}` no meio da linha (R6) e o texto está lá.
- **Chaves:** A1–A4, S1–S12 e G1–G16 usadas no texto existem nos registros; nenhuma chave órfã. G2, G3, G8, G9, G11 e G12 aparecem só no registro, como na v1.0 (já aceito pela VAL).
- **Specs irmãs:**
  - Os arquivos existem e têm os números citados no SIR: SAM v1.1, GPM313 v1.2, GPM312 v1.2. A ressalva do changelog (*"os arquivos ainda não estão em disco"*) caducou.
  - Os prazos do 6.1 e do 2.2 batem com o `Report Matrix!F2` das três specs, inclusive o período parcial §16/§17 e §61/§62.
  - O canal da VMI bate com o `Report Matrix!H2` (*"…EDS rules VA-72 §21; see LT-SIR-001"*).
  - Dia útil seguinte: as três specs deixam o ponto em aberto, igual à G15. GPM313 `Example Analysis!D5` (15/08/2026 cai num sábado, em aberto); SAM `Population Rules!D13`. O "2026-02-16" do GPM312 v1.1 saiu da v1.2.
  - U12 e U15 condicionais (GPM312 v1.2): o SIR não desce a campo, então não há conflito.
  - Única incoerência: R1 (texto vigente da V-243).
- **Ressalvas do changelog:**
  - "Códigos C23xx citados da v1.0": conferi contra a v1.1 e continuam iguais.
  - "Referências a confirmar": confirmadas.

## 5. Forma
- **Document Control:** tabela 10×2 no modelo BE-SIR-001, com os mesmos campos e "Version history" em seguida. Ressalvas: R3 (data) e R5 (Status).
- **Crases:** 0. **TODO/TBD/FIXME/XXX/placeholder/VERIFY/to be confirmed**, com `\b`: 0. `[[` e `{+`: 0.
- **Cliente:** "Accenture" aparece 0 vezes no texto, no `document.xml`, no `core.xml`, no `app.xml` e nos `sections/`.
- **Propriedades:**
  - título "Lithuania Statutory Integration Register (LT-SIR-001 v1.1)";
  - subject "Statutory Integration Register, Lithuania, tax year 2026";
  - creator e lastModifiedBy "Mercans Compliance";
  - created e modified 2026-10-29;
  - Company vazio.
- **Sumário:** campo TOC preenchido com 40 entradas, com as páginas; `w:updateFields val="true"`.
- **Rodapé:** "LT-SIR-001 v1.1 | Mercans Compliance Regulations Team | 2026 | Page N" (campo PAGE).
- **Destaque DDEBF7:** 192 ocorrências, cobre quase toda a mudança, com as lacunas e excessos do R4.

## 6. Dados pessoais
Nenhum:
- 0 nomes de pessoas no docx (procurei Yojana, Wallisson, Kevin, Manju, Marko, Gomes);
- 0 e-mails;
- 0 sequências de 11 dígitos (código pessoal LT).

O G13 cita só "Mercans Compliance; client", sem nome.

## 7. Recomendações (para a v1.1 antes do Drive, ou para a v1.2)
1. **R1:** trocar em 5.1, G10 e 8.3 por: "A1 cites the current consolidated SD rules (V-683 wording, in force from 2026-01-01; points 86.6–86.8, 91.3.1); that text is not archived with this register and was not re-checked; S12 (2015) numbered the same annexes 103.6–103.7."
2. **R2:** tirar a data ou escrever "internal target to be confirmed".
3. **R3:** v1.1 com data "2026-10-29".
4. **R4:** pôr destaque nas 5 alterações sem destaque e tirar das células que não mudaram.
5. **R5:** "Issued" só quando subir ao Drive. Até lá, "Draft for review".
6. **R6:** no 0.5, acrescentar "S11 and S12 were read on 29 October 2026".
7. País em Live/BAU: a publicação segue a regra 9 (ticket ao Development) e precisa do ok do usuário.

## 8. Bloco de prova
- **Pedido → resposta:**
  1. Status F01–F20: §2.
  2. Afirmações reabertas: §3.
  3. Regressões e coerência com as specs: §4.
  4. Forma: §5.
  5. Dados pessoais: §6.
- **Fontes lidas por mim:**
  - VA-72 LT/EN (`.docx`, numeração reconstruída);
  - `EDS_HelpItem_Email_pranesimai.html` e `EDS_HelpItem_Formu_statusai.html`;
  - WSDL ao vivo e especificação v2.01 `.doc`;
  - IN GPM313 `nuo_2026` e IN GPM312;
  - V-243 redação 2015 (`lrs494520`);
  - DSA SAM v07 PDF (md5 conferido);
  - as três specs `.xlsx` e `ccg2026.txt`;
  - hub `paises/Lituania.md`;
  - BE-SIR-001.
- **Teste:**
  - md5 do docx e das specs;
  - extração python-docx (texto, destaque por célula, core props, rodapé);
  - diff v1.0 × v1.1 por item;
  - lint regex com `\b`;
  - busca de chaves A/S/G;
  - 491 trechos markdown × docx;
  - XML do pacote (`settings`, `footer`, `core`, `app`).
- **Confiança: 90 %.**
  - Os 10 % que faltam são os originais da Sodra S1–S4 (só extratos, G16): as afirmações F10, F11 e a do DataService "who" dependem deles.
  - Também não conferi o PDF visual (o destaque foi medido no XML, não visto na tela).
  - Os achados R1–R7 têm confiança de 100 %.

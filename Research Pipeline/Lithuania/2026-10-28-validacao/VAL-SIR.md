# VAL-SIR — validação independente do LT-SIR-001 v1.0 (28/10/2026)

Hub: [[Lituania]] · Artefato: [[Research Pipeline/Lithuania/2026-10-27-SIR/CONFERENCIA]] · Modelo: `~/mercans-pipeline/BE-compliance/03-statutory-integrations/BE-SIR-001-v1.0.docx`

- **Revisor:** compliance-qa-auditor (instância independente, não construiu o SIR). Leitura apenas: nenhum artefato foi alterado.
- **Artefato:** `Research Pipeline/Lithuania/2026-10-27-SIR/LT-SIR-001-v1.0.docx`, md5 `1261f5473586f036baf665bfc4146cf7`. É idêntico à cópia do Drive `19 - Statutory Integrations/LT-SIR-001-v1.0.docx` (md5 conferido). O `.gdoc` não pôde ser conferido.
- **Situação de entrega:** a `CONFERENCIA.md` registra que o SIR já foi entregue em 28/10 (SR-479 e e-mail à Configuração). O país está em **Live/BAU** ([[Lituania]] linha 8). Por isso as correções abaixo pedem versão nova e ticket ao Development (regra 9).

## Método (medido, não declarado)
1. Extração do docx com python-docx (parágrafos, tabelas, rodapé, campos, core properties) e comparação célula a célula com `sections/s00–s08.md`: 412 trechos conferidos.
2. Lint de resíduos (C29) e de português no texto em inglês.
3. Cada afirmação foi rastreada até a fonte local:
   - VMI: HTML do EDS → texto; VA-72 LT/EN → texto com a numeração automática reconstruída; especificação v2.01 `.doc` → antiword; WSDL ao vivo; MXFD GPM313/GPM312; IN GPM313 `nuo_2026` e IN GPM312 (VA-24) com a numeração dos pontos.
   - Sodra: só os extratos do builder (ver NC-1).
4. WebFetch da instrução DataService (PDF) e da instrução NP-SD2 na sodra.lt: **HTTP 403** nas duas. As fontes Sodra não puderam ser verificadas de forma independente.
5. Coerência com `2026-10-27-reports/LT-VMI-001-GPM313-Spec_v1.1.xlsx`, `LT-VMI-002-GPM312-Spec_v1.1.xlsx` e `specs-drive/LT-SODRA-003-SAM-Spec.xlsx` (v1.0), além do CCG 2026 (`ccg2026.txt`) e do hub.
6. Estrutura comparada com o BE-SIR-001 (lista de headings e tabelas extraída das duas versões).

## 1. Achados

| ID | Seção / local | O SIR diz | A fonte diz (local exato) | Deve ser | Sev. |
|---|---|---|---|---|---|
| F01 | 2.1 OUT-02 "return leg IN-01"; 1.1 IN-01 "response to OUT-01, OUT-02" | O status do NP-SD2 volta pelo DataService (`getDocumentStatus(docUID)`) | O próprio SIR, 2.2 OUT-02: canal = conta EDAS; *"Whether DataService accepts NP-SD2 is shown only by getPossibleDocuments (Section 8)"* (G5). S3: o `docUID` só é devolvido por `uploadEdasDraft`/`sendSignedDocument` (extrato DataService, op. 1 e 3) | IN-01 só vale como retorno do OUT-02 **se** o G5 se confirmar. Marcar OUT-02 "return leg: IN-01 conditional on G5; otherwise none (status read in EDAS)" e espelhar o mesmo em 1.1 | MAJOR |
| F02 | s00 Scope; 2.4 (9-SD "outside the report set") | Integração de licenças = só NP-SD2; o 9-SD fica fora sem decisão registrada | Hub [[Lituania]], pendência (SteerCo 27/10): *"pesquisar o 9-SD (licença para cuidar de filho) e o recebimento automático dos dados de atestado… acrescentar ao SIR"*, e *"o 9-SD pode entrar na integração de licenças; decidir com o Wallisson"* | 2.4 não pode apresentar o 9-SD como já excluído enquanto a decisão está aberta. Criar a lacuna G13 "9-SD in the leave integration: scope decision pending (Mercans / client)" e citá-la em 2.4 e no Scope (padrão F15) | MAJOR |
| F03 | 5.2 "Declaration technically not accepted … VMI notifies electronically" | Notificação genérica, "electronically" | VA-72 §26 (LT, ponto 26): *"Jei dokumentas teikiamas … 21.2 ir 21.3 papunkčiuose … informuojamas EDS nurodytais kontaktais po pateiktų duomenų apdorojimo"*. A ajuda do EDS (`EDS_HelpItem_Email_pranesimai.html`) diz onde ficam os contatos: *"NUSTATYMAI → Atstovavimas → Atstovaujamas asmuo → Atstovaujamo mokesčių mokėtojo ryšio priemonės"* | Para upload e web service, os erros chegam **depois do processamento**, pelos contatos (e-mail/telefone) cadastrados no EDS para o pagador representado. A Configuração precisa cadastrar uma caixa monitorada. Acrescentar a linha em 5.2 e em 3.2 | MAJOR |
| F04 | 5.1 Sodra (só WSDATA-0..9 e ERR); G10 | Não há modelo de erro de conteúdo do SAM nem rota de correção do SAM em 5.1 | SAM spec LT-SODRA-003 v1.0: `SAM Spec!M9`/`M17`/`M19`/`M12` citam o catálogo de validação C23xx (C2326, C2327, C2330, C2336, C2338, C2347, C2352; SAM-erros.pdf). `Payroll Scope Summary!B22`: correção por PT-SAM3SD, PT-SAM3SD-M, PT-SAM3SDP (pontos 86.6–86.8). `Report Matrix!F2`: entrega fora do prazo exige PT com código 01 | 5.1 precisa de duas linhas: (a) "SAM content validation: C23xx codes, catalogue SAM-erros.pdf (A1)"; (b) "Correction of accepted SAM data: PT annexes per A1; not re-checked against source (G10)". A lacuna do catálogo C23xx não aparece em s08 | MAJOR |
| F05 | Estrutura, início do documento | Não há bloco **Document Control** | BE-SIR-001: tabela 10×2 depois do TOC (Document ID, Version, Country, Jurisdictions, Tax year, Currency, Prepared by, Status, Related deliverables) | Acrescentar a mesma tabela: LT-SIR-001 / v1.0 / Lithuania (LT) / Sodra, VMI / 2026 / EUR / Mercans Compliance Regulations Team / Issued / A1–A3 + Payroll Regulation Guide 2026, WTC, DD | MAJOR |
| F06 | s07 S1–S4 (fontes Sodra); s07 intro *"Copies and extracts are kept under raw/docs/oficiais/LT/"* | As fontes Sodra parecem arquivadas | `raw/…/2026-10-27-Sodra-SAM/`: só extratos em português escritos pelo builder. O DataService PDF consta como *"lido com pdf.js no navegador, não salvo em disco"* e o `sam-v07.mxfd` como *"lido em memória … não salvo em disco"*. As páginas S2 e S4 não estão salvas. WebFetch em 28/10: 403 | Salvar o PDF DataService v1.0, o `sam-v07.mxfd` e as páginas S2/S4 (PDF ou HTML pelo navegador), com md5 num `_FONTES.md`. Até lá, o s07 deve dizer "extracts only; originals not archived". As citações de página do S3 (pp. 4, 5, 8, 9, 10, 15, 19–20) não são verificáveis por terceiros | MAJOR |
| F07 | 3.2 EDS portal | *"…declare a qualified electronic-signature certificate issued in Lithuania (not needed with a Lithuanian residence permit)"* | `EDS_HelpItem_Uzsienio_pilietis.html`: *"Jei užsienio valstybės pilietis turi leidimą gyventi Lietuvoje, tai prašymo nurodyto pirmame punkte, pildyti nereikia"*: dispensa o **pedido do ponto 1** (meios de acesso da VMI), não o certificado | "…can request VMI access means (the request is not needed with a Lithuanian residence permit) or declare a qualified e-signature certificate issued in Lithuania" | MINOR (WRONG) |
| F08 | 4.2, 3º parágrafo (docx) | `Web service \`EDSWebServiceUploadFile\` (S7)`: crases literais no Word | `s04_tech.md` l.21: `**Web service `EDSWebServiceUploadFile`** (S7)`. O builder não trata código dentro de negrito | Texto sem crases. Único trecho dos 412 que não bate com o markdown | MINOR |
| F09 | 1.1 IN-02 | `CheckFileState` devolve o estado de confirmação e o da declaração | Especificação v2.01, `DeclarationDataResult`: há também `DeclarationActualityStateCode` *"Galimo reikšmės 10, 11, 20"* (Aktuali / Aktuali dėl tikslinimo / Neaktuali). Também no WSDL ao vivo, `DeclarationDataResult` | Acrescentar "Actuality: 10 current, 11 current by correction, 20 not current". Esse é o sinal que mostra que uma declaração foi substituída por correção | MINOR |
| F10 | 2.1 OUT-02 Description | *"NP-SD2: data for sickness and maternity benefit"* | Extrato NP-SD2, p. 60–66: *"B3–B4 férias pagas sobrepostas (só cuidado de familiar)"*: o NP-SD2 também cobre o caso de cuidado de familiar | "sickness (including care of a family member) and maternity benefit". Ou limitar expressamente o escopo a doença e maternidade | MINOR |
| F11 | 2.2 OUT-01 *"EDAS account (on-line form or FFData file)"* | Formulário on-line no EDAS | Extrato S2: só *"ABBYY eFormFiller 2.5 v6"* (programa de preenchimento) e envio de ffdata. Não fala de formulário on-line | "EDAS account (FFData file, e.g. prepared with ABBYY eFormFiller)", ou citar a fonte do formulário on-line | MINOR (NOT FOUND) |
| F12 | 3.2 EDS portal, coluna Source = S9 para "Who: Representatives with filing rights for the payer" | S9 sustenta "Who" | S9 (notícia + ajuda a estrangeiros) não trata de direitos de representação. Isso está em VA-72 §18 ss. (S6) e em S8 (*"bet kuris išorinis vartotojas, turintis teisę teikti tvirtinamą deklaraciją"*) | Fonte "S9; S6 §18; S8" | MINOR |
| F13 | s07 S3 *"with WSDL and XSD"* | O S3 traz XSD | Extrato DataService: só *"Endpoint (WSDL, p. 15)"*. Nenhum XSD é mencionado | "with WSDL", ou apontar a página do XSD | MINOR (NOT FOUND) |
| F14 | s07 S9 Version/date "2026-08-27" | A data vale para a notícia e para a ajuda | A notícia tem data 2026-08-27 (lista `EDS_Naujienos.html`: *"2026-08-27 / Dėl prisijungimo prie EDS"*). A página de ajuda não tem data | "News 2026-08-27; help page undated (read 2026-10-27)" | MINOR |
| F15 | s08 G4 | FR1025 / informacinis pranešimas sem citação | VA-72 §27 (*"Form FR1025 … approved by Order No VA-135"*), mas o S6 lista só §21, §24 e §26 | Acrescentar "S6 §27" em G4 e "§27" em S6. G3, G4, G9 e G10 não têm âncora no corpo; aceitável, mas G4 deveria ter uma linha em 1.1 ("VMI notices — NOT LOCATED as machine channel") | MINOR |
| F16 | 2.2 / 6.1 OUT-01, OUT-03, OUT-04 | Prazos fixos "15th" / "15 February" | GPM312 spec v1.1 `GPM312 Spec!T37`: *"the 2025 return deadline of 2026-02-16"*: há o deslocamento para o dia útil seguinte, que o SIR omite (só o NP-SD2 o traz). GPM313 `Report Matrix!F2` e GPM312 `Report Matrix!F2`: prazos de período parcial (regras 16–17 / 61–62) | Acrescentar "next working day if the 15th is not a working day (source to cite)" e uma linha "part-period returns: bankruptcy/restructuring 30 days; liquidation before end of activity (GPM313 rules §16–17; GPM312 rules §61–62)" | MINOR |
| F17 | 5.2 "Correction of a filed return" | Só o refile do mesmo período | IN GPM312 §65 (spec `GPM312 Spec!M7`): corrigir no GPM312 valores já dados no GPM313 exige corrigir também o GPM313. `research/VMI-integracao.md` l.114: *"Não há operação de anulação no web service"* | Acrescentar o acoplamento GPM312→GPM313 e "annulment only in the EDS portal; no web-service operation" | MINOR |
| F18 | s00 Scope | *"…named for the Accenture Lithuania implementation"* | O BE-SIR-001 não cita cliente. O SIR fica na pasta do país, que serve a todos os clientes | "the two integrations in scope: statutory filing … and leave …" e o nome do cliente no ticket SR-479 | MINOR |
| F19 | Docx: TOC, rodapé, propriedades | O TOC fica como *"Right-click and select 'Update Field'"*; `settings.xml` sem `updateFields`; rodapé sem número de página; core properties com author "python-docx", created/modified 2013-12-23 e título vazio | Herdado do BE (mesmo builder; o BE tem os mesmos defeitos) | Atualizar o TOC antes de publicar (ou `w:updateFields`), pôr título/autor/data nas propriedades e numerar as páginas. Corrigir no `build_sir_docx.py` (BE e LT) | MINOR |
| F20 | Estrutura vs BE | Sem 0.4 (completude vs CCG), 3.4 (autenticação por integração), 6.3 (janelas de correção), 8.4 (o que o SIR não afirma); s00 sem numeração "0."; 7/8 sem "Appendix A/B"; versão "1.0" × "v1.0" | Headings do BE-SIR-001 (ver seção 3) | Acrescentar 0.x numerado, 3.4 e 6.3 (as janelas existem: 3 dias do web service, PT imediato do NP-SD2, refile da VMI). Para o 0.4, o CCG 2026 lista GPM313, SAM, GPM312 (P377–P402) e o 1-SD (P206): os três estão no SIR e o 1-SD está em 2.4. Uma linha basta para mostrar que a completude foi conferida | MINOR |

**Contagem:** 0 BLOCKER · 6 MAJOR (F01–F06) · 14 MINOR (F07–F20).

## 2. Afirmações rastreadas (CONFIRMED / WRONG / NOT FOUND)

Fonte: (L) = fonte primária local lida por mim; (X) = só o extrato do builder (sem original; ver F06).

| # | Seção | Afirmação | Resultado | Evidência (citação curta e local) |
|---|---|---|---|---|
| 1 | 3, 4.2, 6.2 | Confirmação no EDS em 3 dias; sem confirmação o arquivo é apagado e a entrega não conta | CONFIRMED (L) | S8 `EDS_Ziniatinklio_paslauga.html`: *"Per 3 dienas nuo deklaracijos persiuntimo… Jei per 3 dienas … nebus patvirtinta, ji bus ištrinta iš sistemos ir deklaracijos pateikimas nebus įskaitytas"* |
| 2 | 4.2 | Caminho "Deklaravimas → Patvirtinti užpildytą formą" | CONFIRMED (L) | mesma página, mesma frase |
| 3 | 3.2 | Usuário/senha próprios em "Nustatymai → Mano duomenys"; só representantes de pessoa jurídica | CONFIRMED (L) | S8: *"„Nustatymai“ → „Mano duomenys“ … (galimybė yra tik juridinio mokesčių mokėtojo atstovams)"* |
| 4 | 3.2 | O usuário precisa ter direito de declarar pelo PersonCode | CONFIRMED (L) | S7: *"302_BAD_PERSON_LEGAL_CODE … Vartotojas neturi teisės teikti duomenų už nurodytą asmenį"* |
| 5 | 5.2, 6.2 | Não aceitação técnica notificada de imediato, no máximo em 5 dias úteis | CONFIRMED (L), com ressalva F03 | VA-72 p. 26: *"nedelsdamas, bet ne vėliau kaip per 5 darbo dienas, informuojamas"*. EN: *"immediately, but not later than within 5 working days"* |
| 6 | 4.2 | VA-72 §21: três modos (on-line, "Persiųsti failą", web service) | CONFIRMED (L) | VA-72 LT p. 21.1–21.3: *"„Persiųsti failą“"*; *"patvirtinant perduotus … naudojantis žiniatinklio paslauga"* |
| 7 | 6.2 nota | §24: a data de entrega é definida pelo software do EDS | CONFIRMED (L) | VA-72 p. 24: *"jo pateikimo data nustatoma EDS programinėmis priemonėmis"* |
| 8 | s07 S6 | VA-72 de 2021, alterada em 2022 | CONFIRMED (L) | *"2021 m. spalio 26 d. įsakymu Nr. VA-72 (… 2022 m. spalio 29 d. įsakymo Nr. VA-88 redakcija)"* |
| 9 | 4.2 | SubmitFile: .ffdata ou .zip em Base64, com AppName, UserName, Password, PersonCode | CONFIRMED (L) | Especificação v2.01, tabela de entrada: *"*.ffdata formatu arba suarchyvuotas *.ffdata failas *.zip … Base64"*; WSDL ao vivo `SubmitFile` |
| 10 | 4.2, 5.2 | Código 900 com data-limite de confirmação | CONFIRMED (L) | *"900_SUCCESS … Failas turi būti patvirtintas EDS portale iki {data}"* |
| 11 | 5.2 | Erros SubmitFile 000–501; CheckFileState 600–613; sucesso 901 | CONFIRMED (L) | Tabelas de códigos: 000_ERROR … 501_NO_APP_NAME; 600_ERROR … 613_NO_APP_NAME; *"901_SUCCESS_CHECK_FILE_STATE"* |
| 12 | 1.1 IN-02 | Confirmação 10/20/30/40; declaração 10, 21, 22, 101, 102, 103, 100 + outros | CONFIRMED (L), com omissão F09 | *"10 Patvirtintas / 20 Nepatvirtintas / 30 Pašalintas / 40 Nebetvirtinamas"*; *"9, 10, 21, 22, 41, 100, 101, 102, 103, 115"* |
| 13 | 4.3 | SOAP 1.1 na especificação de 2010; o WSDL ao vivo oferece também SOAP 1.2 | CONFIRMED (L) | Exemplos da especificação com `schemas.xmlsoap.org/soap/envelope/`, sem soap12. WSDL ao vivo l.130–131 `EDSWebServiceUploadFileSoap12` |
| 14 | 4.3, G8 | Endpoint https na especificação; http no `soap:address` do WSDL | CONFIRMED (L) | Especificação: *"https://deklaravimas.vmi.lt/EDSWebServiceUploadFile/EDSWebServiceUploadFile.asmx"*; WSDL l.153/156 `http://deklaravimas.vmi.lt/…` |
| 15 | G8 | 200 arquivos/dia; bloqueio de 30 min após 5 senhas erradas; configurável | CONFIRMED (L) | *"maksimaliai 200 failų (… „MaxRequests“)"*; *"5 kartus (… „BadPwdCount“) … užblokuotas 30 minučių"* |
| 16 | 4.2, s07 S7 | Especificação v2.01, 2010; é a oferecida hoje; md5 igual | CONFIRMED (L) | *"Versija 2.01"*; `_FONTES.md`: md5 `aae02f12…` = arquivo em VMI-reports (recalculado) |
| 17 | 3.2, S9 | A partir de 1º/09/2026, login só pelos meios do e-government gateway | CONFIRMED (L) | Notícia 2026-08-27: *"nuo rugsėjo 1 d. … tik „Elektroninių valdžios vartų“ portalo siūlomi prisijungimo būdai"* |
| 18 | 3.2 | Estrangeiro: pedir meios da VMI ou declarar certificado LT | CONFIRMED (L) / parêntese WRONG (F07) | Ajuda "Užsienio pilietis", pontos 1 e 2 e "Svarbu!" |
| 19 | 4.2 | Entrega e correção só eletrônicas pelo EDS (GPM313 §14; GPM312 §59) | CONFIRMED (L) | IN GPM313 `nuo_2026` p. 14 / IN GPM312 p. 59: *"teikiamos ir tikslinamos tik elektroniniu būdu"* |
| 20 | 6.1 | GPM313 até o dia 15 do mês seguinte (§12) | CONFIRMED (L) | p. 12: *"iki kito mėnesio 15 dienos"* |
| 21 | 6.1 | GPM312 até 15 de fevereiro (§57) | CONFIRMED (L), com ressalva F16 | p. 57: *"iki kito mokestinio laikotarpio vasario 15 d."* |
| 22 | 5.2 | Correção = nova declaração completa do período (GPM313 §18; GPM312 §63) | CONFIRMED (L) | p. 18 / p. 63: *"naujai užpildytą Deklaraciją … to mokestinio laikotarpio"* |
| 23 | s07 S5 | VA-121 alterada pela VA-105; VA-9 na redação VA-24 | CONFIRMED (L) | Cabeçalhos: *"(Paskutiniai pakeitimai 2025 11 20 įsakymu Nr. VA-105)"*; *"(2026 m. kovo 26 d. įsakymo Nr. VA-24 redakcija)"* |
| 24 | 4.3 | GPM313.mxfd criado em 2025-11-04, versão EDS 2025-12-31; GPM312.mxfd 2026-05-11 / 2026-06-12 | CONFIRMED (L) | MXFD `CreatedOn="2025-11-04"`, `"2026-05-11"`; lista de formulários do EDS: *"Versija 2025-12-31"*, *"Versija 2026-06-12"* |
| 25 | G9 | Endpoints só nos atributos do MXFD (MdocUploadService.svc, PublicServiceREST; AuthServiceWS) | CONFIRMED (L: VMI; X: Sodra) | MXFD: `Server="https://deklaravimas.vmi.lt/EDSMdocUploadService/MdocUploadService.svc"`, `URLUpdateForm="http://deklaravimas.vmi.lt/PublicServiceREST"`; extrato SAM: *"FFDataCollectServer draudejai.sodra.lt/AuthServiceWS"* |
| 26 | 6.1 | SAM até o dia 15 do mês seguinte (p. 52) | CONFIRMED (X) | Extrato SAM p. 52: *"iki kito kalendorinio mėnesio 15 dienos"*; página: *"iki kito mėnesio 15 d."* |
| 27 | 2.1 | SAM + SAM3SD + SAM3SDP (p. 48) | CONFIRMED (X) | p. 48.1/48.2 |
| 28 | 4.1 | sam-v07.mxfd, FormVersion 07 | CONFIRMED (X) | *"FormCode "SAM", FormVersion "07""* |
| 29 | 6.1 | NP-SD2 doença: fim da incapacidade ou a cada ≥14 dias; ≥2×/mês, até o dia 15 e o último dia; dia útil seguinte | CONFIRMED (X) | p. 57: *"ne rečiau kaip 2 kartus per mėnesį – ne vėliau kaip kalendorinio mėnesio 15 ir paskutinę dieną"* |
| 30 | 6.1 | NP-SD2 maternidade: 5 dias úteis | CONFIRMED (X) | p. 59: *"ne vėliau kaip per 5 darbo dienas nuo asmens kreipimosi dienos"* |
| 31 | 1.1 IN-03 | Instrução cita "elektroniniai pažymėjimai ar Pranešimai draudėjui" | CONFIRMED (X) | p. 68 |
| 32 | 5.1 | Erro no NP-SD2 corrigido de imediato por PT com anexo PT-NP-SD2 | CONFIRMED (X) | p. 76 |
| 33 | 3.1, 4.1 | EDAS: assinatura qualificada em toda notificação; só o diretor ou pessoa autorizada assina | CONFIRMED (X) | S2: *"būtina pasirašyti saugiu kvalifikuotu elektroniniu parašu"*; *"Tik įmonės vadovas arba jo įgaliotas asmuo"* |
| 34 | 2.2, 2.4 | S2 lista NP-SD2 e 1-SD, 2-SD, 9-SD, 12-SD, 13-SD como entregas obrigatórias pela conta | CONFIRMED (X) | *"1-SD, 2-SD, 9-SD, 12-SD, 13-SD, NP-SD2, SAM privalu teikti per asmeninę paskyrą"* |
| 35 | 3.1 | Login EDAS via draudejai.sodra.lt, e-banking, epaslaugos.lt | CONFIRMED (X) | extrato S2 |
| 36 | 4.1 | Arquivos conforme a descrição de estrutura da Sodra; transmissão pelo web service público | CONFIRMED (X) | *"duomenų struktūros aprašas"*; *"per viešąją tinklinę sąsają"* |
| 37 | 3.1 | UsernameToken; senha 10–14 caracteres, ≥1 especial e ≥1 dígito; 5 falhas bloqueiam (p. 4) | CONFIRMED (X) | extrato DataService p. 4 |
| 38 | 3.1 | "Any EDAS user who has enabled the service" | NOT FOUND (X): o extrato descreve a ativação, não quem pode | extrato p. 4 |
| 39 | 4.1, 4.3 | 5 operações; UTF-8 sem BOM; base64/MTOM; endpoint; SOAP 1.2 document/literal | CONFIRMED (X) | extrato pp. 5–10, p. 8, p. 15 |
| 40 | 4.1 | `sendSignedDocument` "starts registration" | NOT FOUND (X) | o extrato diz só *"FFDATA assinado → docUID"* |
| 41 | 1.1 IN-01 | Status NST/FNS/PRC/ARC/ERR/DRF (pp. 9, 19–20) | CONFIRMED (X); p. 9 não verificável | extrato pp. 19–20 |
| 42 | 5.1 | WSDATA-0..9 com as 10 descrições | CONFIRMED (X) | extrato p. 20 (as 10 descrições batem na ordem) |
| 43 | 1.1 IN-03 | O DataService não tem operação que devolva dados de atestado | CONFIRMED (X) | só 5 operações, nenhuma de entrada de dados |
| 44 | 2.2 | OUT-01 "on-line form" no EDAS | NOT FOUND (X) → F11 | |
| 45 | s00, s07 | Datas das fontes: DataService v1.0 de 2016-01-19 | CONFIRMED (X) | *"Sukūrimo data: 2016-01-19", "Dokumento versija: 1.0"* |

Placar: 45 afirmações. 41 CONFIRMED (25 em fonte primária local, 16 só no extrato), 1 WRONG (F07, parêntese), 3 NOT FOUND (38, 40 e 44; 44 é o F11). Nenhum número, prazo ou código do SIR contradiz a fonte.

## 3. Checagens aprovadas, com evidência
- **docx = markdown:** 412 trechos de `s00–s08` encontrados no docx; 1 divergência (F08). Tabelas: 16 no docx (2+1 s00, 2 s01, 4 s02, 2 s03, 1 s04, 2 s05, 2 s06, 3 s07, 1 s08), mesmas linhas do markdown. Travessões (—), setas (→) e diacríticos lituanos (ė, ų, š, „ “) chegaram intactos.
- **Título e rodapé:** capa *"Lithuania Statutory Integration Register — LT-SIR-001 v1.0"*; rodapé *"LT-SIR-001 v1.0 | Mercans Compliance Regulations Team | 2026"*. TOC presente como campo `TOC \o "1-3" \h \z \u` (não populado, F19).
- **IDs:** IN-01..03 e OUT-01..04 iguais em 1.1, 1.2, 2.1, 2.2, 2.3, 3, 4, 5, 6.1, 6.2 e s08. Nenhum ID órfão ou duplicado.
- **Citações:** todas as chaves usadas (S1–S9, A1–A3) existem em s07. Nenhuma linha de registro ficou sem fonte. Ressalvas de alvo errado ou incompleto: F12, F13, F15.
- **NOT LOCATED ↔ s08:** IN-03 (1.1 e 1.2) → G1; 6.2 OUT-01/02 → G12; "not stated" 3.2 → G7; 2.2 getPossibleDocuments → G5; nota 6.2 → G6; "no XSD" 4.2 → G2; http×https 4.3 → G8; versões 2016/2010 em s00 → G11. Ida e volta completa. G3, G4, G9 e G10 não têm âncora no corpo (F15).
- **Coerência com as specs:**
  - versões A1 = SAM v1.0 (`Version Control` 1.0, 2026-08-21), A2/A3 = v1.1 (2026-10-27): CONFIRMED;
  - prazos iguais (`Report Matrix!F2` das três specs);
  - canal VMI igual ao `Report Matrix!H2` das duas v1.1 (*"EDS on-line form, FFData file upload, or EDS web service EDSWebServiceUploadFile (EDS rules VA-72 §21; see LT-SIR-001)"*);
  - datas do MXFD iguais a `File Structure!B8`/`B10`;
  - SAM FFData / form 07 igual a `Report Matrix!H2`.
- **CCG 2026:** os três relatórios do CCG (P377–P402) estão no SIR, com os mesmos prazos.
- **Lint C29:** 0 ocorrências (TODO, TBD, FIXME, XXX, placeholder, to be confirmed/verified, VERIFY, `[[`). Português vazado: 0 (o único acerto, "do the confirmation", é inglês). O lituano aparece só como termo citado em itálico/aspas.
- **Drive:** md5 do docx local = md5 do docx no Drive 19.

### Estrutura vs BE-SIR-001
| BE-SIR-001 | LT-SIR-001 | Situação |
|---|---|---|
| Capa + TOC | Capa + TOC | OK |
| Document Control (tabela 10×2) | — | **Falta (F05)** |
| Version history | Version control (dentro de s00) | OK (formato "1.0" × "v1.0") |
| 0. Purpose, Scope & Audit Compliance, 0.1–0.6 | Document Control and How to Read… (sem número): Purpose, Scope, Version control, Source discipline, Product Mapping, Currency | OK no conteúdo; faltam 0.2 build order e 0.4 completude vs CCG (F20) |
| 1. Inbound 1.1/1.2 | 1. Inbound 1.1/1.2 | OK |
| 2. Outbound 2.1–2.4 | 2. Outbound 2.1–2.4 | OK |
| 3. Authentication 3.1–3.4 | 3.1–3.2 | Falta 3.4 lookup (F20) |
| 4. Technical | 4.1–4.3 | OK (proporcional) |
| 5. Error Handling, incl. 5.6 summary | 5.1–5.2 | OK; conteúdo F03/F04 |
| 6. SLA 6.1–6.4 | 6.1–6.2 | Falta 6.3 correction windows (F20) |
| Appendix A. Sources (7.1–7.4) | 7. Source Register (7.1–7.3) | OK (título diferente) |
| Appendix B. Open Gaps (8.1–8.4) | 8. Open Gaps (tabela única) | OK; sem 8.4 (o "nothing tested live" está em s00) |
| Rodapé, propriedades, TOC | idem | mesmos defeitos herdados (F19) |

## 4. Não verificável nesta rodada
1. **Originais Sodra S1–S4:** só há extratos do builder; a sodra.lt devolveu 403 ao WebFetch. As 16 afirmações (X) dependem da fidelidade do extrato (F06). As páginas 9 e 10 do S3 não estão confirmadas nem no extrato.
2. Se o DataService aceita o NP-SD2 (G5), se há ambientes de teste (G3) e o comportamento real dos endpoints: nenhum serviço foi chamado, por desenho.
3. O conteúdo do Google Doc (`.gdoc` do Drive, link da SR-479): só o `.docx` foi conferido.
4. A regra de deslocamento para o dia útil seguinte nos prazos da VMI/Sodra: a Lei de Administração Tributária e as regras gerais SD (TAR.34A6775CE75B) não estão em disco (F16).
5. O texto vigente da V-243 (pontos 86 e 91 sobre PT do SAM): em disco só existem as redações de 2010 e de 2015 (G10 continua honesto).

## 5. Veredito
**Não está pronto como está: precisa de revisão (v1.0 → v1.1). Nenhum BLOCKER, 6 MAJOR e 14 MINOR.**
- O conteúdo técnico e estatutário está correto onde foi possível medir: nenhum prazo, código, endpoint ou versão contradiz a fonte primária.
- Os MAJOR são de outro tipo:
  - lógica do registro: retorno IN-01 do NP-SD2 dado como certo;
  - escopo: 9-SD excluído sem decisão;
  - operação: canal de aviso de erro da VMI e modelo de erro/correção do SAM ausentes;
  - estrutura: falta o Document Control;
  - rastreabilidade: originais Sodra não arquivados.
- O SIR já foi entregue (SR-479) e o país está em Live/BAU. Corrigir exige v1.1 e comentário/ticket ao Development (regra 9). Nada foi alterado nesta validação.

**Confiança nesta validação: 85 %.**
- Os 15 % que faltam são as fontes Sodra, conferidas só contra o extrato do próprio builder (403 no acesso direto), e o Google Doc não conferido.
- Para fechar: salvar os originais Sodra (PDF DataService, `sam-v07.mxfd`, páginas S2/S4) e reconferir as afirmações 26–45.

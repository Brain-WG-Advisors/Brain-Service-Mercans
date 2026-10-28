# Sodra — envio eletrônico dos SD (EDAS) e web service DataService (lidos em 2026-10-27 pelo navegador)

## Página "Elektroninių pranešimų teikimas internetu" (sodra.lt/darbo-procesai/elektroniniu-pranesimu-teikimas-internetu)
- "Socialinio draudimo pranešimus 1-SD, 2-SD, 9-SD, 12-SD, 13-SD, NP-SD2, SAM privalu teikti per asmeninę paskyrą draudėjui / darbdaviui."
- "Pranešimus būtina pasirašyti saugiu kvalifikuotu elektroniniu parašu."
- Acesso à conta: https://draudejai.sodra.lt/, banco eletrônico, epaslaugos.lt. Quem assina: "Tik įmonės vadovas arba jo įgaliotas asmuo."
- Programa gratuita de preenchimento: ABBYY eFormFiller 2.5 v6.
- "Informacija verslo valdymo sistemų kūrimo ir integravimo įmonėms": sistemas do empregador, adaptadas aos requisitos da Sodra, "gali elektroninius pranešimus rengti bei pateikti „Sodrai“ automatiniu būdu". Funções: assinar e enviar documentos ffdata; enviar documentos já assinados; assinar com assinatura qualificada e guardar localmente; carregar rascunhos não assinados; consultar status (aceito/rejeitado, com erros).
- Requisitos: arquivos conforme "duomenų struktūros aprašas" da Sodra; assinatura conforme requisitos do diretor; transmissão "per viešąją tinklinę sąsają (angl. web service)".
- Atos: V-665 de 2007-12-20 (regras de uso do EDAS, e-tar TAR.5B98B417E564); V-666 de 2007-12-20 (assinatura/selo eletrônico qualificado, e-tar TAR.A0B319F14560). Não lidos.

## Instrução "„Sodros“ paskyros draudėjui (DataService) — Naudojimosi instrukcija" (PDF, sodra.lt/wp-content/uploads/2025/07/EDAS-DataService-public-versionpdf.pdf; "Sukūrimo data: 2016-01-19", "Dokumento versija: 1.0"; 21 p.; lido com pdf.js no navegador, não salvo em disco)
- Protocolo: SOAP sobre HTTPS, MTOM; segurança WS-Security UsernameToken: "turi būti perduodamas EDAS naudotojo vardas ir slaptažodis" (p. 4).
- Ativação: no EDAS, "Naudotojo nustatymai" → marcar "Naudoti pranešimų teikimo naudojant tinklinę sąsają paslaugą", definir senha (10–14 caracteres, ≥1 especial, ≥1 número); 5 falhas seguidas bloqueiam o serviço (p. 4).
- Operações (p. 5–10): 1 `uploadEdasDraft` (fileName opc., document base64/MTOM, FFDATA não assinado, UTF-8 sem BOM → signingURL, docUID); 2 `getDocumentLink` (docUID → documentURL); 3 `sendSignedDocument` (FFDATA assinado → docUID; p. 8: "Dokumentai turi būti perduodami UTF-8 without BOM koduote"); 4 `getDocumentStatus` (docUID → docStatus NST/FNS/PRC/ARC/ERR/DRF + descrição); 5 `getPossibleDocuments` (→ lista code/version dos formulários aceitos).
- Endpoint (WSDL, p. 15): `https://draudejai.sodra.lt/edas-external/services/DataService`; namespace `http://data.external.ws.edas.sodra.epr.lt`; SOAP 1.2, document/literal.
- Status (p. 19–20): NST Nepateiktas; FNS Įvykdytas/priimtas; ERR Atmestas dėl klaidų; PRC Vykdomas/Apdorojamas; ARC Padėtas į archyvą; DRF Ruošinys.
- Erros WSDATA-0…9 (p. 20): 0 sistema; 1 usuário não encontrado; 2 credenciais; 3 serviço bloqueado; 4 sem documento; 5 falha ao salvar rascunho; 6 assinatura inválida; 7 falha ao salvar documento; 8 documento não encontrado; 9 ação não permitida no status.

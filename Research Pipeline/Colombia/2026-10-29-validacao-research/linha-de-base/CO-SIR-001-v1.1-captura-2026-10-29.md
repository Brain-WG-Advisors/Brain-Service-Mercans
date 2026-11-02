# CO-SIR-001 v1.1: captura de texto para a linha de base

> Capturado em 2026-10-29 pelo Claude in Chrome (conta wgomes@mercans.com), Google Doc `CO-SIR-001-v1.1` do Drive `Country Folders/Colombia/19 - Staturory Integration/`, visão `mobilebasic` (só leitura, sem download). Texto integral: 19.875 caracteres, 2.702 palavras. Esta nota guarda a estrutura e todas as afirmações verificáveis (item de teste do SIR); tabelas achatadas com " | ". Plano: [[PLANO-DE-ACAO]] · [[CONFERENCIA]]

## Controle do documento
Document ID CO-SIR-001 | Version v1.1 | Country Colombia (CO) | Jurisdictions: National — DIAN (tax), Ministerio de Salud y Protección Social via licensed operadores de información (PILA), Fondos de Cesantías via operador | Tax year 2026 | Currency COP | Status Issued
Related deliverables: "CO-CCG-001 v1.1 (Module 10); scope_manifest.json; six Report Specs in 04-reports-spec; CO-DD-001 v1.0; DIAN-NE Configuration Runbook (P1–P7)"
Histórico: v1.0 2026-09-04 Initial issue · v1.1 2026-10-21 "Citations of Res. DIAN 000013 de 2021 updated to Res. DIAN 000227 de 2025."

## 0. Propósito e escopo
- Discovery verdict HAS_INTEGRATIONS; 4 autoridades; 1 canal system-to-system; "Of the six in-scope filings, one is carried system-to-system and five are manual."
- Inventário (scope_manifest.integrations): CO-OUT-NE-001 DIAN Servicio de Validación NE OUTBOUND Yes | CO-IN-NE-APPRESPONSE DIAN ApplicationResponse/GetStatus INBOUND Yes | CO-OUT-MUISCA-001 DIAN Muisca (Form 350) OUTBOUND No | CO-OUT-PILA-001 PILA via operador OUTBOUND Yes (file generation only) | CO-IN-PILA-001 PILA settlement return INBOUND No | CO-OUT-CESANTIAS-001 Fondos de Cesantías via operador OUTBOUND Yes (file generation only) | CO-IN-CESANTIAS-CONFIRMATION INBOUND No.
- 0.3 Fontes DIAN-NE: Res. DIAN 000227/2025 (compila a 000013/2021), Anexo Técnico DSPNE v1.0 (269 pp.), XSD v1.0.6, WSDL obtido em 2026-09-04; onde Anexo e WSDL divergem, vale o WSDL.

## 1. Inbound
- NE como instrumento de dedutibilidade: Res. 227/2025 art. 1.5.3.2.3; ApplicationResponse deve ser guardado.
- Registro inbound: CO-IN-NE-APPRESPONSE (SendNominaSync + GetStatus por CUNE; Mandatory) | CO-IN-PILA-001 (Operational) | CO-IN-CESANTIAS-CONFIRMATION (registros E10, E11, E90, E91, E93; Operational).

## 2. Outbound
- CO-OUT-NE-001 → CO-DIAN-001, mensal, SOAP 1.2, base64 ZIP com exatamente 1 XML assinado, UTF-8, 500 KB.
- CO-OUT-MUISCA-001 → CO-DIAN-002, mensal, portal, sem arquivo.
- CO-OUT-PILA-001 → CO-PILA-003, mensal, TXT de largura fixa (Archivo Tipo 1 + Archivo Tipo 2).
- CO-OUT-CESANTIAS-001 → CO-CESANTIAS-006, anual, TXT fixo ou XLS 97-2003 ou CSV, conforme o operador.
- 2.2 Conteúdo por canal: NE (por empregado: salário, horas extras, auxílios, bônus, cesantías e juros, férias; saúde, pensão, FSP, retención, embargos, pagamentos a terceiros) | Form 350 (retención agregada por conceito) | PILA (IBC por subsistema, dias, novedades, saúde, pensão, FSP, ARL, CCF, SENA, ICBF) | Cesantías (liquidação anual em 31/12, fundo, contato, data de início) | Form 220 "not filed with DIAN" | Format 2276 (renda e retención por beneficiário no ano).

## 3. Autenticação
- 3.1 NE: Anexo §9.3/§9.4 (mTLS) × WSDL `sp:HttpsToken RequireClientCertificate="false"` → TLS 1.2 só servidor; WS-Security 1.0, X.509 Token Profile 1.1, Basic256Sha256Rsa15, timestamp; WS-Addressing (To assinado); XAdES-EPES, SHA-1 rejeitado; certificado ONAC; habilitação (SoftwareID, PIN, set de pruebas; regra global 92); terceiro transmissor: Res. 227/2025 art. 1.5.3.8.1 (habilitado, RUT, mandato).
- 3.2 Muisca: sessão com IFE, sem credencial M2M.
- 3.3 PILA: credencial do operador (Aportes en Línea, Enlace Operativo, MiPlanilla, Asopagos, SOI…), sem autenticação publicada pelo governo.
- 3.4 Cesantías: login do operador; "APIS PILA" da ARUS/Enlace Operativo só casca em 2026-09-04, não usado.

## 4. Especificações técnicas
- NE: SOAP 1.2 document/literal; SendNominaSync e GetStatus; produção vpfe.dian.gov.co, habilitação vpfe-hab.dian.gov.co (`/WcfDianCustomerServices.svc`); XSD v1.0.6; **433 regras: 406 R + 27 N**; 500 KB; sem lote (1 por beneficiário); 15 operações, 2 no escopo.
- Muisca: portal. PILA: dois TXT fixos; layout do governo + pré-validação do operador. Cesantías: TXT "20 fields in 258 positions" ou XLS (16 colunas A–P) ou CSV; sem esquema do governo.

## 5. Erros
- 7 classes: Container, Signature, Schema, Business (R), Business (N), Global rule 90 (número reutilizado), Global rule 92 (emissor não habilitado).
- Sem retry idempotente; consultar GetStatus por CUNE antes de reenviar; correção por nota de ajuste; ApplicationResponse 02 validado, 04 rejeitado.
- Penalidades: NE (não dedutível; Res. 227/2025 art. 1.5.3.2.3; ET 616-1 e 651) | Form 350 (ET 641, 634) | PILA (juros de mora e UGPP; Ley 100/1993) | Cesantías (um dia de salário por dia de atraso, sem teto; Ley 50/1990 art. 99 num. 3).

## 6. Prazos
- NE: 10 primeiros dias do mês seguinte ao pagamento; 1 documento por empregado por mês (Res. 227/2025 arts. 1.5.3.2.2 e 1.5.3.4.1.1).
- Form 350: 7º a 16º dia útil, pelo último dígito do NIT (DUR 1625/2016 art. 1.6.1.13.2.33).
- PILA: 2º a 16º dia útil, pelos dois últimos dígitos (Decreto 780/2016 art. 3.2.2.1).
- Cesantías: antes de 15 de fevereiro (Ley 50/1990 art. 99 num. 3).
- Formato 2276: maio a junho do ano seguinte, pelo NIT (Res. 227/2025 art. 1.3.9.1.3).
- Form 220: até o último dia útil de março; não é enviado à DIAN (DUR 1625/2016 art. 1.6.1.13.2.40).
- Juros das cesantías ao empregado até 31 de janeiro (Ley 52/1975 art. 1).
- SendNominaSync síncrono; sem SLA publicado; contingência: emitir fora e transmitir em até 48 h após o retorno do serviço.

## Apêndice A (fontes citadas pelo SIR)
scope_manifest.json; CCG Module 10 (CO-CCG-001 v1.1); 6 Report Specs (sem a CO-PILA-007); Runbook P1–P7; Res. DIAN 227/2025 arts. 1.5.3.1.1 a 1.5.3.9.8; Anexo DSPNE v1.0; XSD v1.0.6; WSDL; "PILA — Resolución 2388 de 2016 and Anexo Técnico 2"; manual da Simple S.A. (cesantías); portal ARUS; integration-landscape.json (2026-09-04).

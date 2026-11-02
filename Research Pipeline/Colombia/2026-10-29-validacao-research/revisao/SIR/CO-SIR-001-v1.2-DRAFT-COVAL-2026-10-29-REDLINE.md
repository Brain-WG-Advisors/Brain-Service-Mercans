# CO-SIR-001 v1.2 DRAFT (COVAL, 2026-10-29): redline para colar no Google Doc

Base: `linha-de-base/CO-SIR-001-v1.1-captura-2026-10-29.md` (md5 27e3807ed33a9d8f72c200a70f18474a). Não há docx local: o SIR existe só como Google Doc. Este arquivo lista, por mudança confirmada, a seção, o texto atual (verbatim da captura), o texto novo em inglês pronto para colar e a fonte. Nada foi gravado no Google. Research CO não está em produção: nova versão, sem ticket ao Development. Ver [[CHANGELOG]] · [[PLANO-DE-ACAO]] · [[mudancas-SIR]].

Aviso: a captura é um resumo do texto do Doc (frases em português, termos em inglês entre aspas). Ao colar, localizar o trecho equivalente no Doc pelas âncoras indicadas (códigos de artigo, "48 h" etc.) e substituir a frase inteira em inglês do Doc; o texto novo abaixo está no padrão em inglês do artefato.

## D8: referências desatualizadas (Controle do documento, linha "Related deliverables"; Apêndice A)

### D8a. Controle do documento, "Related deliverables"
- Atual: `CO-CCG-001 v1.1 (Module 10); scope_manifest.json; six Report Specs in 04-reports-spec; CO-DD-001 v1.0; DIAN-NE Configuration Runbook (P1–P7)`
- Novo: `CO-CCG-001 v1.5 (Module 10); scope_manifest.json; seven Report Specs v1.1 in 04-reports-spec (including CO-PILA-007, the pensioners PILA flow); CO-DD-001 v1.4; CO Payslip Generator v1.2; DIAN-NE Configuration Runbook (P1–P7)`
- Fonte: versões geradas na rodada COVAL de 2026-10-29 (CCG v1.5, DD v1.4, 7 specs v1.1, Payslip v1.2; todas DRAFT, a emitir juntas; se o SIR for emitido antes, usar a versão vigente de cada uma). Versões vigentes antes da rodada em `paises/Colombia.md` (CCG v1.4, DD v1.3, 7 specs v1.0) e COMPARATIVO-FINAL-CO-v1.0.xlsx, D8; Res. MSPS 1529/2026 p.1.

### D8b. Apêndice A (fontes citadas pelo SIR), três entradas
1. Atual: `CCG Module 10 (CO-CCG-001 v1.1)` → Novo: `CCG Module 10 (CO-CCG-001 v1.5)`
2. Atual: `6 Report Specs (sem a CO-PILA-007)` → Novo: `7 Report Specs v1.1 (including CO-PILA-007, pensioners PILA flow)`
3. Atual: `"PILA — Resolución 2388 de 2016 and Anexo Técnico 2"` → Novo: `PILA — Resolución 2388 de 2016, Anexo Técnico 2 (v30) and Anexo Técnico 3 (v15), as amended by Resolución MSPS 1529 de 2026`
- Fonte: Res. MSPS 1529/2026 p.1: "Por medio de la cual se modifican los Anexos Técnicos 2 y 3 de la Resolución 2388 de 2016". Versões v30 (AT2) e v15 (AT3) conforme a base PILA confirmada no comparativo (mudancas-PILA).

## S-02: citação da NE como instrumento de dedutibilidade

### S-02a. Seção 1 (Inbound)
- Atual: `NE como instrumento de dedutibilidade: Res. 227/2025 art. 1.5.3.2.3; ApplicationResponse deve ser guardado.`
- Novo: `The NE is the supporting document for costs and deductions: Res. DIAN 000227/2025 art. 1.5.3.2.1 (formerly art. 2 of Res. DIAN 000013/2021), ET art. 771-2 inc. 3, ET art. 616-1 par. 6 and DUR art. 1.6.1.4.27; the ApplicationResponse must be retained.`

### S-02b. Seção 5 (Erros), linha Penalidades, item NE
- Atual: `NE (não dedutível; Res. 227/2025 art. 1.5.3.2.3; ET 616-1 e 651)`
- Novo: `NE (not deductible; Res. 227/2025 art. 1.5.3.2.1; ET 771-2, ET 616-1 and 651)`
- Fonte (ambas): Res. 13/2021 art. 2 (normograma local, compilado como art. 1.5.3.2.1): "constituye el soporte de los costos y deducciones"; o art. 1.5.3.2.3 só define os sujeitos ("SUJETOS OBLIGADOS ..."). Não há outra ocorrência do art. 1.5.3.2.3 na captura.

## S-01: Formato 2276, calendário dos grandes contribuyentes

- Seção 6 (Prazos). Atual: `Formato 2276: maio a junho do ano seguinte, pelo NIT (Res. 227/2025 art. 1.3.9.1.3).`
- Novo: `Format 2276: May to June of the following year, by NIT (Res. 227/2025 art. 1.3.9.1.3): by the last digit of the NIT for large taxpayers (grandes contribuyentes) and by the last two digits for legal entities (personas jurídicas); exact dates are set in the annual DIAN due-date resolution.`
- Fonte: Res. 227 art. 1.3.9.1.3: "último dígito del NIT ... gran contribuyente o los dos últimos dígitos ... persona jurídica". A remissão às "resoluções anuais de datas" não leva número de resolução (nenhum foi lido).

## S-06: contingência da NE

- Seção 6 (Prazos), última linha. Atual: `SendNominaSync síncrono; sem SLA publicado; contingência: emitir fora e transmitir em até 48 h após o retorno do serviço.`
- Novo: `SendNominaSync is synchronous; no published SLA; contingency: transmit within 48 hours counted from the day after the service is restored (Res. 227/2025 art. 1.5.3.5.1.5); keep the supporting documents (soportes) of the payroll document.`
- Fonte: Res. 227 art. 1.5.3.5.1.5: "plazo máximo de cuarenta y ocho (48) horas contadas a partir del día siguiente al que se restablezca el servicio". "Emitir fora" retirado conforme o comparativo. A frase sobre guardar os soportes segue o comparativo ("guardar os soportes (caso do sujeito)"), sem artigo próprio citado: confirmar a redação com o usuário.

## Histórico de versão e controle do documento (regra 8)

- Linha nova em Version history: `v1.2 DRAFT | 2026-10-29 | Validation corrections (COVAL): D8, S-02, S-01, S-06; round 4 (2026-10-30): S-03, S-04, S-05, S-07 (provisional)`
- Campo "Version" do Controle do documento: `v1.1` → `v1.2 DRAFT` (decorrência da regra de nome; Status "Issued" não alterado aqui).

## Rodada 4 (2026-10-30, pesquisa oficial de 30/10: `pesquisa-2026-10-30/PENDENTES-SPECS-DD.md`)

### S-03. Seção 5 (Erros), linha Penalidades, item PILA
- Atual: `PILA (juros de mora e UGPP; Ley 100/1993)`
- Novo: `PILA (late-payment interest at the income-tax default rate, Ley 100/1993 art. 23; UGPP penalties for omission, late filing and inaccuracy, Ley 1607/2012 art. 179 as modified by Ley 1819/2016 art. 314, num. 3 as modified by Ley 2010/2019 art. 121)`
- Fonte: Ley 100 art. 23 ("generarán un interés moratorio a cargo del empleador, igual al que rige para el impuesto sobre la renta y complementarios"); Ley 1607 art. 179 (texto da Ley 1819 art. 314: "La UGPP será la entidad competente para imponer las sanciones..."). Confiança 92%.

### S-04. Seção 6 (Prazos), linhas PILA e juros das cesantías
1. Atual: `PILA: 2º a 16º dia útil, pelos dois últimos dígitos (Decreto 780/2016 art. 3.2.2.1).` → Novo: `PILA: from the 2nd to the 16th business day, by the last two digits of the NIT / identity document (00–07 = 2nd … 94–99 = 16th), Decreto 780/2016 art. 3.2.2.1 (as substituted by Decreto 1990/2016 art. 2).`
2. Atual: `Juros das cesantías ao empregado até 31 de janeiro (Ley 52/1975 art. 1).` → Novo: `Interest on severance savings (12% a year): paid to the employee in January, or on termination / within the month after a partial severance settlement (Ley 52/1975 art. 1; Decreto 1072/2015 art. 2.2.1.3.4).`
- Fonte: Decreto 1990/2016 art. 2 (tabela "Día hábil | 2o 00 al 07 | … | 16o 94 al 99"); Decreto 1072 art. 2.2.1.3.4 ("deberán pagarse en el mes de enero del año siguiente … o en la fecha de retiro del trabajador o dentro del mes siguiente a la liquidación parcial de cesantía"). Confiança 93%.

### S-05. Seção 4 (Especificações técnicas), linha Cesantías
- Atual: `Cesantías: TXT "20 fields in 258 positions" ou XLS (16 colunas A–P) ou CSV; sem esquema do governo.`
- Novo: `Severance funds: the file format (TXT 258 positions / XLS / CSV) is each severance fund's own rule; no government schema is published. The annual deposit does not go through the PILA (AT2 v30 has no severance record); Ley 2466/2025 art. 64 par. 1 tasks the Ministry of Health with a PILA rule only for the optional monthly advance deposit, not yet reflected in AT2 v30.`
- Fonte: AT2 v30 (busca "cesant": só "Mecanismo de Protección al Cesante"); Ley 2466/2025 art. 64 par. 1. Confiança 85%.

### S-07. Seção 4 (Especificações técnicas), linha NE — continua aberto; posição provisória
- Atual: `433 regras: 406 R + 27 N`
- Novo: `more than 430 validation rules (R = rejection, N = notification), Anexo Técnico NE v1.0 §6`
- Fonte: Anexo NE §6 (contagem por texto ruidosa; não reproduz 433/406/27 por nenhum recorte). Position — confidence 80%; fecha com a planilha de regras da caixa de ferramentas DIAN ou leitura da tabela do PDF.

## Observação fora do pedido

A seção 0 e a seção 2 ainda dizem "six in-scope filings, one system-to-system and five manual" e não descrevem o fluxo de pensionados (CO-PILA-007). D8 só confirma Related deliverables e Apêndice A; acrescentar o fluxo ao inventário exigiria conteúdo novo sem mudança confirmada. Fica como pendência para decisão do usuário.

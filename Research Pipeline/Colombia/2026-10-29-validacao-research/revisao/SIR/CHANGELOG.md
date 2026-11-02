# CHANGELOG: CO-SIR-001 v1.1 → v1.2 DRAFT (COVAL, 2026-10-29)

Formato: redline em Markdown ([[CO-SIR-001-v1.2-DRAFT-COVAL-2026-10-29-REDLINE]]); o SIR é só Google Doc e nada foi gravado no Google. Base md5 27e3807ed33a9d8f72c200a70f18474a. "APLICADA" = redline pronto para colar.

| ID | Onde | Antes (verbatim da captura) | Depois | Fonte | Status |
|---|---|---|---|---|---|
| D8a | Controle do documento, Related deliverables | `CO-CCG-001 v1.1 (Module 10); scope_manifest.json; six Report Specs in 04-reports-spec; CO-DD-001 v1.0; DIAN-NE Configuration Runbook (P1–P7)` | `CO-CCG-001 v1.5 (Module 10); scope_manifest.json; seven Report Specs v1.1 in 04-reports-spec (including CO-PILA-007, the pensioners PILA flow); CO-DD-001 v1.4; CO Payslip Generator v1.2; DIAN-NE Configuration Runbook (P1–P7)` | Res. MSPS 1529/2026 p.1; versoes geradas na rodada COVAL (CCG v1.5, DD v1.4, specs v1.1, Payslip v1.2) | APLICADA (redline) |
| D8b | Apêndice A | `CCG Module 10 (CO-CCG-001 v1.1)`; `6 Report Specs (sem a CO-PILA-007)`; `"PILA — Resolución 2388 de 2016 and Anexo Técnico 2"` | `CO-CCG-001 v1.5`; `7 Report Specs v1.1 (including CO-PILA-007, pensioners PILA flow)`; `PILA — Resolución 2388 de 2016, Anexo Técnico 2 (v30) and Anexo Técnico 3 (v15), as amended by Resolución MSPS 1529 de 2026` | Res. MSPS 1529/2026 p.1 | APLICADA (redline) |
| S-02a | Seção 1 Inbound | `NE como instrumento de dedutibilidade: Res. 227/2025 art. 1.5.3.2.3; ApplicationResponse deve ser guardado.` | `The NE is the supporting document for costs and deductions: Res. DIAN 000227/2025 art. 1.5.3.2.1 (formerly art. 2 of Res. DIAN 000013/2021), ET art. 771-2 inc. 3, ET art. 616-1 par. 6 and DUR art. 1.6.1.4.27; the ApplicationResponse must be retained.` | Res. 13/2021 art. 2 = 227 art. 1.5.3.2.1 | APLICADA (redline) |
| S-02b | Seção 5 Penalidades, NE | `NE (não dedutível; Res. 227/2025 art. 1.5.3.2.3; ET 616-1 e 651)` | `NE (not deductible; Res. 227/2025 art. 1.5.3.2.1; ET 771-2, ET 616-1 and 651)` | idem | APLICADA (redline) |
| S-01 | Seção 6, Formato 2276 | `Formato 2276: maio a junho do ano seguinte, pelo NIT (Res. 227/2025 art. 1.3.9.1.3).` | `Format 2276: May to June of the following year, by NIT (Res. 227/2025 art. 1.3.9.1.3): by the last digit of the NIT for large taxpayers (grandes contribuyentes) and by the last two digits for legal entities (personas jurídicas); exact dates are set in the annual DIAN due-date resolution.` | Res. 227 art. 1.3.9.1.3 | APLICADA (redline) |
| S-06 | Seção 6, última linha | `SendNominaSync síncrono; sem SLA publicado; contingência: emitir fora e transmitir em até 48 h após o retorno do serviço.` | `SendNominaSync is synchronous; no published SLA; contingency: transmit within 48 hours counted from the day after the service is restored (Res. 227/2025 art. 1.5.3.5.1.5); keep the supporting documents (soportes) of the payroll document.` | Res. 227 art. 1.5.3.5.1.5 | APLICADA (redline) |
| VC | Version history + campo Version | `v1.1 2026-10-21 ...`; `Version v1.1` | linha nova `v1.2 DRAFT | 2026-10-29 | Validation corrections (COVAL): D8, S-02, S-01, S-06`; `Version v1.2 DRAFT` | regra 8 | APLICADA (redline) |
| S-03 | Seção 5, PILA | `PILA (juros de mora e UGPP; Ley 100/1993)` | sem mudança | norma da sanção UGPP não lida | NÃO APLICADA: SEM FONTE |
| S-04 | Seção 6, PILA e juros das cesantías | `PILA: 2º a 16º dia útil...`; `Juros das cesantías ... até 31 de janeiro (Ley 52/1975 art. 1)` | sem mudança | coluna de dias perdida na cópia local | NÃO APLICADA: SEM FONTE |
| S-05 | Seção 4, Cesantías | `TXT "20 fields in 258 positions" ou XLS (16 colunas A–P) ou CSV; sem esquema do governo.` | sem mudança | sem esquema oficial | NÃO APLICADA: SEM FONTE |
| S-07 | Seção 4, NE | `433 regras: 406 R + 27 N` | sem mudança | contagem não reproduzida | NÃO APLICADA: SEM FONTE |

## Prova
Ver a linha "Prova" abaixo (preenchida após a verificação mecânica de que cada "Antes" ocorre uma única vez na base).

Verificação (python -I): os 8 textos "Antes" (verbatim) ocorrem exatamente 1 vez cada na base; nenhum outro trecho é tocado. md5 base: 27e3807ed33a9d8f72c200a70f18474a. md5 do REDLINE no momento da verificação: fcc2c2b31c131d5259ac1921354ba857. Contagem: 4 IDs confirmados aplicados (D8, S-02, S-01, S-06; 7 linhas de edição) e 4 não aplicados (S-03, S-04, S-05, S-07, SEM FONTE).

## Rodada 2 (2026-10-29, DECISOES-RODADA2 item 13)
Redline md5 da rodada 2: `8f186e65279ae9a06b61ed40fdd0a4b6` (rodada 1: `fcc2c2b31c131d5259ac1921354ba857`). Base da captura inalterada (md5 27e3807ed33a9d8f72c200a70f18474a).

| ID | Onde | Antes (redline rodada 1) | Depois | Fonte | Status |
|---|---|---|---|---|---|
| D8a | Related deliverables | `CO-CCG-001 v1.4 ...; seven Report Specs ...; CO-DD-001 v1.3; ...` | `CO-CCG-001 v1.5 ...; seven Report Specs v1.1 ...; CO-DD-001 v1.4; CO Payslip Generator v1.2; ...` | versoes geradas na rodada COVAL (todas DRAFT, a emitir juntas; se o SIR sair antes, usar a versao vigente de cada uma) | APLICADA (redline) |
| D8b | Apendice A, item 1 e 2 | `CO-CCG-001 v1.4`; `7 Report Specs (including ...)` | `CO-CCG-001 v1.5`; `7 Report Specs v1.1 (including ...)` | idem | APLICADA (redline) |
| S-02a | Secao 1, Inbound | `ET art. 771-2 par. 3` | `ET art. 771-2 inc. 3` | mudancas-SIR S-02 ("ET 771-2 inc. 3") | APLICADA (redline) |
| Nao aplicado | Payslip v1.2 em outro ponto do SIR | n/a | n/a | a captura nao cita o Payslip em nenhum outro lugar; so entrou em Related deliverables | n/a |

Prova (python -I): a base x redline v2 difere da rodada 1 exatamente nas 4 linhas acima (D8a Novo e Fonte, D8b itens 1 e 2, S-02a Novo); os 8 "Antes" continuam ocorrendo 1 vez na captura; nenhum "v1.4", "v1.3" ou "par. 3" resta nas linhas "Novo".

## Rodada 4 (2026-10-30, pesquisa oficial de 30/10; redline markdown, seção "Rodada 4")

Decisões: `pesquisa-2026-10-30/TABELA-CONSOLIDADA.md` (+ DECISOES-TEST4, PENDENTES-CCG-WTC, PENDENTES-SPECS-DD). Registro completo: `../mudancas-RODADA4.md`; conferência: `../CONFERENCIA-DRAFTS-R4.md`. Status de todas as linhas abaixo: APLICADA.

- `CO-SIR-001-v1.2-DRAFT-COVAL-2026-10-29-REDLINE.md`: md5 antes da rodada 4 `8f186e65279ae9a06b61ed40fdd0a4b6` → depois `cf1cdc95e07ccf6683fbb9e7870eeeed`.

| ID | Onde | Antes (verbatim) | Depois (verbatim) |
|---|---|---|---|
| S-03, S-04, S-05, S-07 (provisória) | REDLINE, seção "Rodada 4" | ver REDLINE | ver REDLINE e ../mudancas-RODADA4.md |

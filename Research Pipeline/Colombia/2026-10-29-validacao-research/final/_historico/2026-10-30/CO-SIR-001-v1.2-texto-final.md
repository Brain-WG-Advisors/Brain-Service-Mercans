# CO-SIR-001 v1.2: texto final para colar no Google Doc

Emissão 2026-10-30. O SIR existe só como Google Doc (`Country Folders/Colombia/19 - Staturory Integration/CO-SIR-001-v1.1`), então a versão final é este texto, para colar à mão. Cada bloco abaixo substitui a frase inteira do Doc no ponto indicado (a âncora é o trecho em inglês que já está no Doc). Só o conteúdo dentro dos blocos de código vai para o Doc. A trilha de revisão (texto anterior, fonte de cada mudança) fica em `changelogs/CO-SIR-001-v1.2-CHANGELOG.md` e no redline `revisao/SIR/CO-SIR-001-v1.2-DRAFT-COVAL-2026-10-29-REDLINE.md`. Ligado a [[CONFERENCIA]] e [[RELEASE-CROSSCHECK]].

## 1. Document control

Campo **Version** (hoje `v1.1`):
```
v1.2
```

Campo **Status**: manter `Issued`.

Linha **Related deliverables** (hoje começa por `CO-CCG-001 v1.1 (Module 10)`):
```
CO-CCG-001 v1.5 (Module 10); the seven Report Specs v1.1 (including CO-PILA-007, the pensioners PILA flow); CO-DD-001 v1.4; CO Payslip Generator v1.2; DIAN-NE Configuration Runbook (P1–P7)
```

**Version history**: acrescentar a linha, depois da v1.1:
```
v1.2 | 2026-10-30 | Statutory validation against the primary sources: related deliverables and Appendix A updated (CO-CCG-001 v1.5, the seven Report Specs v1.1 including CO-PILA-007, CO-DD-001 v1.4, Payslip Generator v1.2; PILA Technical Annexes 2 v30 and 3 v15 as amended by Resolución MSPS 1529 de 2026); the electronic payroll document as the support for costs and deductions (Res. DIAN 000227 de 2025 art. 1.5.3.2.1); Format 2276 calendar; NE contingency (48 hours from the day after the service is restored); PILA penalties and deadlines; interest on severance savings; severance-fund file formats; NE validation-rule count.
```

## 2. Section 1 (Inbound)

Frase sobre a NE como suporte de dedutibilidade (âncora: `art. 1.5.3.2.3` e `ApplicationResponse`):
```
The NE is the supporting document for costs and deductions: Res. DIAN 000227/2025 art. 1.5.3.2.1 (formerly art. 2 of Res. DIAN 000013/2021), ET art. 771-2 inc. 3, ET art. 616-1 par. 6 and DUR art. 1.6.1.4.27; the ApplicationResponse must be retained.
```

## 3. Section 4 (Technical specifications)

Linha NE, contagem de regras (âncora: `433` / `406` / `27`):
```
more than 430 validation rules (R = rejection, N = notification), Anexo Técnico NE v1.0 §6
```

Linha Cesantías (âncora: `258 positions`):
```
Severance funds: the file format (TXT 258 positions / XLS / CSV) is each severance fund's own rule; no government schema is published. The annual deposit does not go through the PILA (AT2 v30 has no severance record); Ley 2466/2025 art. 64 par. 1 tasks the Ministry of Health with a PILA rule only for the optional monthly advance deposit, not yet reflected in AT2 v30.
```

## 4. Section 5 (Errors), linha Penalties

Item NE (âncora: `ET 616-1` e `651`):
```
NE (not deductible; Res. 227/2025 art. 1.5.3.2.1; ET 771-2, ET 616-1 and 651)
```

Item PILA (âncora: `UGPP` e `Ley 100/1993`):
```
PILA (late-payment interest at the income-tax default rate, Ley 100/1993 art. 23; UGPP penalties for omission, late filing and inaccuracy, Ley 1607/2012 art. 179 as modified by Ley 1819/2016 art. 314, num. 3 as modified by Ley 2010/2019 art. 121)
```

## 5. Section 6 (Deadlines)

Linha PILA (âncora: `Decreto 780/2016 art. 3.2.2.1`):
```
PILA: from the 2nd to the 16th business day, by the last two digits of the NIT / identity document (00–07 = 2nd … 94–99 = 16th), Decreto 780/2016 art. 3.2.2.1 (as substituted by Decreto 1990/2016 art. 2).
```

Linha Formato 2276 (âncora: `art. 1.3.9.1.3`):
```
Format 2276: May to June of the following year, by NIT (Res. 227/2025 art. 1.3.9.1.3): by the last digit of the NIT for large taxpayers (grandes contribuyentes) and by the last two digits for legal entities (personas jurídicas); exact dates are set in the annual DIAN due-date resolution.
```

Linha juros das cesantías (âncora: `Ley 52/1975 art. 1`):
```
Interest on severance savings (12% a year): paid to the employee in January, or on termination / within the month after a partial severance settlement (Ley 52/1975 art. 1; Decreto 1072/2015 art. 2.2.1.3.4).
```

Última linha, NE síncrona e contingência (âncora: `SendNominaSync` e `48`):
```
SendNominaSync is synchronous; no published SLA; contingency: transmit within 48 hours counted from the day after the service is restored (Res. 227/2025 art. 1.5.3.5.1.5); keep the supporting documents (soportes) of the payroll document.
```

## 6. Appendix A (sources cited by the SIR)

Três entradas:

Entrada do CCG (hoje `CO-CCG-001 v1.1`):
```
CCG Module 10 (CO-CCG-001 v1.5)
```

Entrada das specs (hoje fala em seis specs, sem a CO-PILA-007):
```
7 Report Specs v1.1 (including CO-PILA-007, pensioners PILA flow)
```

Entrada da PILA (âncora: `Resolución 2388 de 2016`):
```
PILA — Resolución 2388 de 2016, Anexo Técnico 2 (v30) and Anexo Técnico 3 (v15), as amended by Resolución MSPS 1529 de 2026
```

## Depois de colar

- Conferir no Doc: Version `v1.2`, a linha nova do Version history e os 15 blocos acima.
- Pendências que ficam no Doc e não estão neste texto (não havia mudança aprovada nem o texto integral local): a seção 0 e a seção 2 ainda falam em "six in-scope filings" e não descrevem o fluxo de pensionados (CO-PILA-007); a seção 0 e o Apêndice A ainda citam `scope_manifest.json` e `integration-landscape.json`, que são arquivos de trabalho internos.

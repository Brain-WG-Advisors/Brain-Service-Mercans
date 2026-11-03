# CO-SIR-001 v1.4: texto final para colar no Google Doc

Emissão 2026-11-02, rodada 6 (substitui, onde indicado, o texto da v1.3 de `CO-SIR-001-v1.3-texto-final.md`, que continua valendo para os demais blocos). Origem: [[SIR-R6-secoes-0-2]], aprovado pelo usuário em 02/11 ("Pode aplicar os ajustes de texto e o SIR v1.4"). Ligado a [[CONFERENCIA]] e [[SIR-DOC-CONFERENCIA]].

Fonte das linhas novas: spec CO-PILA-007 v1.1, Report Matrix B9–B15 e A29–A37 (relida em 02/11). Contagem 6 → 7: `scope_manifest.json` (authority_filings.in_scope = 6) + CO-PILA-007 (spec v1.0 de 21/10).

## 1. Version
`v1.3` → `v1.4`

## 2. Related deliverables (célula inteira)
```
CO-CCG-001 v1.7 (Module 10); the seven Report Specs (CO-DIAN-004 at v1.3; CO-DIAN-001, CO-DIAN-005, CO-PILA-003 and CO-CESANTIAS-006 at v1.2; CO-DIAN-002 and CO-PILA-007, the pensioners PILA flow, at v1.1); CO-DD-001 v1.6; CO Payslip Generator v1.3; DIAN-NE Configuration Runbook (P1–P7)
```

## 3. Version history, linha nova depois da v1.3
```
v1.4 | 2026-11-02 | Mercans Compliance Regulations Team | Pensioners' PILA (CO-PILA-007) added to the integration inventory (0.1), outbound register (2.1) and data disaggregation (2.2); in-scope filings corrected from six to seven; internal working-file names removed from section 0 and Appendix A; related deliverables and Appendix A updated (CO-CCG-001 v1.7, CO-DIAN-004 v1.3, CO-DD-001 v1.6).
```

## 4. Seção 0, última frase do parágrafo de abertura
Âncora: `Of the six in-scope filings, one is carried system-to-system and five are manual.`
```
Of the seven in-scope filings, one is carried system-to-system and six are manual or operator-mediated; one of them, the pensioners' PILA (CO-PILA-007, Anexo Técnico 3), applies only where the employer pays pensions directly as pension payer.
```

## 5. Título 0.1
`0.1 Canonical integration inventory (scope_manifest.integrations)` → `0.1 Canonical integration inventory`

## 6. Tabela 0.1, linha nova depois de CO-OUT-PILA-001 (4 células)
```
CO-OUT-PILA-002 | PILA (pensioners) via operador de información | OUTBOUND | Yes — file generation only
```

## 7. Tabela 2.1, linha nova depois de CO-OUT-PILA-001 (8 células)
```
CO-OUT-PILA-002 | PILA via licensed operador de información, pension payer | OUT | Yes | Contributions withheld from pensions the employer pays directly (pension payer type 01): health, solidarity fund and, where they apply, pension and CCF; one detail record per pensioner and pension type | CO-PILA-007 | Monthly | Fixed-width TXT (Archivo Tipo 1 + Archivo Tipo 2, Anexo Técnico 3) uploaded to the operator portal
```

## 8. Tabela 2.2, linha nova depois da linha PILA (3 células)
```
Pensioners' contributions, per pensioner | PILA pensioners (operator) | Pension type, mesada, contribution days, health, solidarity fund and, where they apply, pension and CCF; no occupational risk, SENA or ICBF
```

## 9. Apêndice A
- Primeira entrada (`scope_manifest.json (.integrations, .authority_filings) — AUTHORITATIVE canonical integration and filing list (4 authorities; 6 in-scope filings, 7 descoped).`) →
```
Scope decision of 3 September 2026 (internal scope record): 4 authorities; 7 in-scope filings (the six original filings plus the pensioners' PILA, CO-PILA-007, added on 21 October 2026), 7 descoped.
```
- `CCG Module 10 (CO-CCG-001 v1.6)` → `CCG Module 10 (CO-CCG-001 v1.7)`
- `7 Report Specs (v1.2; CO-DIAN-002 and CO-PILA-007 v1.1; including CO-PILA-007, pensioners PILA flow)` → `7 Report Specs (CO-DIAN-004 v1.3; CO-DIAN-002 and CO-PILA-007 v1.1; the others v1.2; including CO-PILA-007, pensioners PILA flow)`
- Fim da lista de arquivos das specs: `CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx.` → `CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx, CO-PILA-007-AportesPensionados-Spec.xlsx.`
- Última entrada (`integration-landscape.json (schema integration-landscape/1.0), generated 2026-09-04 — the discovery record behind this register.`) →
```
Integration discovery record of 4 September 2026 (internal working file behind this register).
```

## 10. Rodapé e título
- Rodapé `CO-SIR-001 v1.3 |` → `CO-SIR-001 v1.4 |`
- Nome do Doc `CO-SIR-001-v1.3` → `CO-SIR-001-v1.4`

## Lista de verificação (no export depois de recarregar)
- Version `v1.4`; linha v1.4 no Version history.
- Zero ocorrências de: `six in-scope`, `scope_manifest`, `integration-landscape.json`, `CO-CCG-001 v1.6`, `CO-DD-001 v1.5`, `CO-SIR-001 v1.3`.
- `CO-OUT-PILA-002` presente 2 vezes (0.1 e 2.1); `Pensioners' contributions, per pensioner` 1 vez; `CO-PILA-007-AportesPensionados-Spec.xlsx` 1 vez.

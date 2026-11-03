# CO-SIR-001: texto das seções 0, 2 e do Apêndice A para incluir o fluxo de pensionistas (item 15 do PLANO-92)

Rascunho de 2026-11-02, ainda não colado no Doc. Colar no Google Doc depende do ok do usuário (Drive). Ligado a [[PLANO-92]] e [[CONFERENCIA]].

## Base

- O escopo de 03/09 (`Research Pipeline/Colombia/CO-compliance/scope_manifest.json`, scope_version 1.0) tem 6 declarações no escopo (NE, Form 350, PILA, Form 220, Formato 2276, Cesantías) e 7 fora do escopo. O fluxo de pensionistas não está em nenhuma das duas listas. A cópia em `~/mercans-pipeline` tem outro md5, mas as mesmas listas.
- A spec CO-PILA-007 v1.1 (`final/specs/`, Report Matrix) define o fluxo assim:
  - empregador como pagador de pensão tipo 01;
  - planilla tipo P (R, L e V para retroativos);
  - Arquivo Tipo 1 + Arquivo Tipo 2, conforme o AT3 v15;
  - envio por operador de informação licenciado;
  - aportes de saúde e FSP, e pensão/CCF quando se aplicam;
  - sem ARL, SENA e ICBF;
  - prazo do Decreto 780 art. 3.2.2.1.
- Com a PILA de pensionistas, ficam 7 declarações no escopo: 1 de sistema a sistema (NE) e 6 manuais ou por operador. As fora do escopo continuam 7.

## Seção 0, parágrafo de abertura

Âncora: `Of the six in-scope filings`. Substituir a última frase do parágrafo por:
```
Of the seven in-scope filings, one is carried system-to-system and six are manual or operator-mediated; the seventh, the pensioners' PILA (CO-PILA-007, Anexo Técnico 3), applies only where the employer pays pensions directly as pension payer.
```

## 0.1, título

Hoje: `0.1 Canonical integration inventory (scope_manifest.integrations)`. Fica:
```
0.1 Canonical integration inventory
```

## 0.1, linha nova na tabela, depois de CO-OUT-PILA-001

```
CO-OUT-PILA-002 | PILA (pensioners) via operador de información | OUTBOUND | Yes — file generation only
```

## 2.1 Outbound integration register, linha nova depois de CO-OUT-PILA-001

```
CO-OUT-PILA-002 | PILA via licensed operador de información, pension payer | OUT | Yes | Contributions withheld from pensions the employer pays directly (pension payer type 01): health, Fondo de Solidaridad Pensional and, where they apply, pension and family compensation fund; one detail record per pensioner and pension type | CO-PILA-007 | Monthly (planilla P; R, L, V for retroactive amounts) | Fixed-width TXT (Archivo Tipo 1 + Archivo Tipo 2, Anexo Técnico 3 v15) uploaded to the operator portal
```

## 2.2 Data disaggregation, linha nova depois da PILA

```
Pensioners' contributions, per pensioner | PILA pensioners (operator) | Pension type, pensioner type, mesada, contribution days, IBC, health, solidarity fund and, where they apply, pension and CCF; no occupational risk, SENA or ICBF
```

## Apêndice A

Trocar a primeira entrada (`scope_manifest.json (.integrations, .authority_filings) — AUTHORITATIVE ...`) por:
```
Scope decision of 3 September 2026 (internal scope record): 4 authorities; 7 in-scope filings (the six original filings plus the pensioners' PILA, CO-PILA-007, added on 21 October 2026), 7 descoped.
```

Na entrada das specs, acrescentar o arquivo que falta no fim da lista:
```
, CO-PILA-007-AportesPensionados-Spec.xlsx
```

Trocar a última entrada (`integration-landscape.json (schema integration-landscape/1.0), generated 2026-09-04 — ...`) por:
```
Integration discovery record of 4 September 2026 (internal working file behind this register).
```

## Controle de versão

- Version: `v1.4`.
- Linha nova no histórico:
```
v1.4 | 2026-11-02 | Pensioners' PILA (CO-PILA-007) added to the integration inventory (0.1), outbound register (2.1) and data disaggregation (2.2); in-scope filings corrected from six to seven; internal working-file names removed from section 0 and Appendix A.
```
- O nome do Doc passa a `CO-SIR-001-v1.4`. Depois, trocar o rótulo no monday (Statutory Integration) e na SR-470.

## Prova

- **Seis → sete:** contei `authority_filings.in_scope` = 6 e `out_of_scope` = 7 no scope_manifest e acrescentei a 007. A spec 007 v1.0 é de 21/10 (Version Control).
- **Texto das linhas novas:** sai da Report Matrix da spec CO-PILA-007 v1.1, campos Authority, Report Type, Tax Type, Relationship, Frequency e File Format, mais as notas de escopo e de aportes. Não foi relido no AT3 nesta passada; o AT3 foi conferido na rodada de 29/10 (`achados/PILA.md`).
- **Confiança:** 93%. O que falta é você confirmar que a PILA de pensionistas está no escopo. A spec 007 diz "escopo YES", e o DD v1.5 já tem os campos.

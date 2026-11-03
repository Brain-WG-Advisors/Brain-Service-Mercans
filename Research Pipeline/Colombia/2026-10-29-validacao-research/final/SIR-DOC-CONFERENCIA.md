# CO-SIR-001: Google Doc v1.1 → v1.3 (conferência da subida)

Data: 2026-11-02. Frente Validação CO, pelo Claude in Chrome, com ok do usuário para esta subida ao Drive. Doc: `https://docs.google.com/document/d/1QEQ3v7qTFQevjM9xKWeISPwYw8rpa26MepVOaYfTSh4/edit` (o mesmo Doc, sem criar outro). Título renomeado de `CO-SIR-001-v1.1` para `CO-SIR-001-v1.3`.

Textos aplicados: [[CO-SIR-001-v1.3-texto-final]] (vale onde substitui a mesma frase) sobre o texto v1.2 de `_historico/2026-10-30/CO-SIR-001-v1.2-texto-final.md` e o redline `revisao/SIR/CO-SIR-001-v1.2-DRAFT-COVAL-2026-10-29-REDLINE.md`. Ligado a [[CONFERENCIA]].

Método: Editar > Localizar e substituir (regex + diferenciar maiúsculas), uma ocorrência única por busca, conferida antes no export txt; Version e Version history editados direto na célula (Tab cria a linha nova). Export final: `CO-SIR-001-v1.3-export-2026-11-02.txt` (após a rodada 2: SHA-256 `2cd6efa07d162b27e70c6e0b5c86d53830ac5373c86a2f8945ad908d29541cc7`, idêntico ao texto lido no Doc após recarregar; md5 `9c36e5777fd3ef5f1911a63f9fc52626`; rodada 1 era SHA-256 `09c849d3…`).

## Blocos

| # | Bloco | Âncora no Doc (texto v1.1 substituído) | Aplicado? | Conferido no export |
|---|---|---|---|---|
| 1 | Version | célula `v1.1` | sim → `v1.3` | sim |
| 2 | Related deliverables (v1.3) | célula inteira `CO-CCG-001 v1.1 (Module 10); scope_manifest.json; six Report Specs ...; CO-DD-001 v1.0; DIAN-NE Configuration Runbook (P1–P7) in 03-statutory-integrations/DIAN-NE/` | sim | sim |
| 3 | Version history v1.2 | linha nova após v1.1 (autor: Mercans Compliance Regulations Team) | sim | sim |
| 4 | Version history v1.3 | linha nova após v1.2 | sim | sim |
| 5 | Seção 1.1, NE suporte de custos e deduções | frase `The Documento Soporte de Pago de Nómina Electrónica is a deductibility instrument: under Res. DIAN 000227 de 2025 art. 1.5.3.2.3 ... costs and deductions.` | sim | sim |
| 6 | Seção 4, contagem de regras NE (v1.3: 519) | `433 validation rules: 406 rejecting (R) and 27 notifying (N).` (célula Schema/validation) | sim | sim |
| 7 | Seção 4, Cesantías | célula `Fixed-width TXT (20 fields in 258 positions), or XLS 97-2003 (16 columns A–P), or CSV` | sim | sim |
| 8 | Seção 5.4, item NE | célula Basis `Res. DIAN 000227 de 2025 art. 1.5.3.2.3; ET arts. 616-1 and 651` | sim | sim |
| 9 | Seção 5.4, item PILA | célula Basis `Ley 100 de 1993; UGPP enforcement regime` | sim | sim |
| 10 | Seção 6.1, PILA | célula Deadline `2nd to 16th business day of the month following the period, by the last two digits of the employer ID.` | sim | sim |
| 11 | Seção 6.1, Formato 2276 | célula Deadline `May to June of the following year, staggered by NIT.` | sim | sim |
| 12 | Seção 6.2, juros das cesantías | célula Note `Paid directly to the employee, not to the fund (Ley 52 de 1975 art. 1)` | sim | sim |
| 13 | Seção 6.3, contingência NE | frase `A statutory contingency applies when the service is unavailable: ... within 48 hours of the service being restored.` | sim | sim |
| 14 | Apêndice A, CCG (v1.3) | `CCG Module 10 (CO-CCG-001 v1.1)` (resto da linha mantido) | sim → v1.6 | sim |
| 15 | Apêndice A, specs (v1.3) | `Report Specs (04-reports-spec/)` (lista de arquivos mantida) | sim | sim |
| 16 | Apêndice A, PILA | `PILA — Resolución 2388 de 2016 and Anexo Técnico 2` (resto da linha mantido) | sim | sim |
| 17 | Apêndice A, Anexo NE (fora dos blocos; exigência da lista de verificação) | `web service, 433 validation rules` → `web service, 519 validation rules` | sim | sim |
| 19 | Seção 5.1, contagem (rodada 2, S-07) | `DIAN applies 433 rules ...: 406 are rejecting (R) and 27 are notifying (N).` → `DIAN applies 437 rules ...: 408 are rejecting (R) and 29 are notifying (N).` | sim | sim |
| 20 | Seção 5.1, tabela de classes (rodada 2) | `DIAN, 406 rules` → `DIAN, 408 rules (payroll documents)`; `DIAN, 27 rules` → `DIAN, 29 rules (payroll documents)` | sim | sim |
| 21 | Seção 6.3, repetição (rodada 2) | 1º parágrafo `SendNominaSync is synchronous: the DianResponse carrying` → `The DianResponse carrying` (fica só a frase da v1.3) | sim | sim (1 ocorrência) |
| 18 | Rodapé (fora dos blocos) | `CO-SIR-001 v1.1 | ...` → `CO-SIR-001 v1.3 | ...` | sim | sim (o export inclui o rodapé) |

Lista de verificação final (após recarregar a página; refeita na rodada 2 com zero ocorrências de `433`, `406` e `27 rules`, e 1 só `SendNominaSync is synchronous`): os 15 blocos da v1.3 (que contêm os da v1.2 onde não foram substituídos) presentes literalmente; Version `v1.3`; linhas v1.2 e v1.3 no Version history; zero ocorrências de `433 validation rules`, `CO-CCG-001 v1.1 (Module 10)` e `CO-CCG-001 v1.1`; nenhum texto antigo substituído restante. Resultado: OK.

## Decisões de encaixe (o texto final foi escrito sobre a captura-resumo, e o Doc é em tabelas)
- Blocos 8 e 9 entraram na coluna Basis da tabela 5.4 (a coluna Charge ficou como estava), por isso o texto da célula começa por "NE (" e "PILA (".
- Blocos 10 e 11 entraram na coluna Deadline; a coluna Basis (Decreto 780 de 2016 art. 3.2.2.1; Res. DIAN 000227 de 2025 art. 1.3.9.1.3) ficou como estava.
- Bloco 12 entrou na coluna Note; a coluna Date continua `By 31 January`.
- Bloco 5 substituiu só a frase com o art. 1.5.3.2.3; as duas frases seguintes da 1.1 ficaram.
- Bloco 13: a frase anterior da 6.3 e a seguinte (engine guarda e reenvia) ficaram; a repetição de "SendNominaSync is synchronous" foi tirada na rodada 2.
- Related deliverables: a v1.2/v1.3 tiram `scope_manifest.json` e `in 03-statutory-integrations/DIAN-NE/` desta linha.

## Pendências (ficam no Doc; sem texto aprovado)
- Seção 0 e seção 2 ainda falam em "six in-scope filings" e não descrevem o fluxo de pensionados (CO-PILA-007); a lista de arquivos do Apêndice A não tem a spec CO-PILA-007.
- Seção 0 e Apêndice A ainda citam `scope_manifest.json` e `integration-landscape.json`.
- Fonte do Version history (rodada 2, conferido na tela): a 1ª coluna inteira da tabela já era Calibri 11 negrito (v1.0 e v1.1 também); as células v1.2 e v1.3 estão iguais a elas, e as demais colunas estão em Arial. Não alterei: passar só a v1.2 para Arial a deixaria diferente das outras linhas.

## Linhas por frente
| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | Validação CO | Doc v1.1 → v1.3 no Drive (blocos v1.2 + v1.3, Version, Version history, rodapé, título); export salvo e conferido por SHA-256. |
| 2026-11-02 | Validação CO | Rodada 2 (S-07): 5.1 com 437 = 408 R + 29 N; tabela de classes 408/29 (payroll documents); repetição da 6.3 tirada; fonte do Version history conferida (sem mudança); export regravado (SHA-256 2cd6efa0…). |
| 2026-11-02 | Validação CO | **v1.3 → v1.4** ([[CO-SIR-001-v1.4-texto-final]], ok do usuário): seção 0 (sete declarações, PILA de pensionistas), título 0.1 sem `scope_manifest`, linhas CO-OUT-PILA-002 em 0.1 e 2.1, linha de pensionistas em 2.2, Related deliverables (CCG v1.7, DIAN-004 v1.3, DD v1.6), Apêndice A (registro de escopo, CCG v1.7, specs, CO-PILA-007 na lista, registro de descoberta), Version v1.4, linha v1.4 no Version history, rodapé, título `CO-SIR-001-v1.4`. Conferência: export do Doc (sem BOM) SHA-256 `2e509b52…` = texto esperado montado de v1.3 + as mudanças, byte a byte (`CO-SIR-001-v1.4-export-2026-11-02.txt`). Antes de editar: Doc = export v1.3 (SHA-256 `2cd6efa0…`). Apóstrofos curvos que o Docs pôs nas 2 linhas digitadas na página trocados por retos (padrão do Doc). |

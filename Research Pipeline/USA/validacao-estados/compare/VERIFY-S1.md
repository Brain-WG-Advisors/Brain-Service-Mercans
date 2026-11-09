# EUA — Conferência adversarial dos 4 S1 (V-01..V-04) e de V-05
Data 2026-11-06. Revisor independente (compliance-qa-auditor), sem participação no build nem na comparação. Liga: [[FINDINGS]]. Nada foi alterado em artefatos ou facts.

## Resumo
| Id | Veredito | Severidade nova |
|---|---|---|
| V-01 NYS Method II | DOWNGRADED | S2 |
| V-02 NYC Method II | DOWNGRADED | S2 |
| V-03 Yonkers Method II | DOWNGRADED | S2 |
| V-04 GA jan–10/mai | CONFIRMED | S1 |
| V-05 OH SUI 2,85 | CONFIRMED (defeito do juiz) | — |

## V-01, V-02, V-03 — NY Method II (NYS, NYC, Yonkers): DOWNGRADED para S2
**O que confere:** as faixas não estão em nenhum facts.
- Busca em todos os `_research/*facts.json`: as únicas chaves NY de retenção são `ny.wh.method` / `ny.sit.method` (texto), `ny.sit.deduction_allowance.{single,married}.annual` (7.400 / 7.950), `ny.sit.exemption.annual`, `ny.pit.top_income.threshold.annual` e as taxas suplementares.
- Não há `bracket`, `floor`, `base` nem allowance por período para NYS, NYC ou Yonkers. A taxa da sobretaxa de residente de Yonkers não aparece nem como valor.
- Também não estão em WTC nem em DD. WTC `Wage Type Catalogue` US-104 só cita "NYS-50-T-NYS (1/26): Method I tables, Method II exact …".
- O CA carrega `ca.pit.bracket.*`, então o pacote não segue um padrão único.

**Por que não é S1:** a remissão às tabelas da publicação foi uma escolha de desenho declarada. Nenhum valor está errado.
- `01-ccg/annexes/annex_NY.md` L54: "the build uses the publication's tables and formula, never the statutory brackets of Tax Law 601. The WTC references NYS-50-T-NYS only."
- A fonte é A.2 (US-NY-001) e tem cópia local (`ccg-sources/NY/nys50t-nys-1-26.txt`). L58 registra que os exemplos 1, 3 e 4 do Method II "reproduce" (foram reproduzidos).
- Um engenheiro consegue calcular, mas só abrindo a publicação. Pelo pacote sozinho, não consegue.

**Por que continua sendo achado:**
- A escolha não está em L-1..L-10 (`07-qa-crosscheck/QA-REPORT.md` L87-96), nem no MANDATE, nem em `gaps.json`. A única lacuna NY de Method II é o arredondamento (RQ-263/RQ-547).
- O juiz e a suíte (C37/C69) não conseguem testar o que não está nos facts.

**Correção mínima:** escolher uma das duas.
- **(a)** Carregar as faixas, como foi feito no CA:
  - `ny.wh.method2.{single,married}.bracket.N.{floor,rate,base}`;
  - as allowances por período;
  - as constantes do Method III;
  - o equivalente para NYC (NYS-50-T-NYC) e para Yonkers (sobretaxa de residente e não residente, NYS-50-T-Y).
  - Todas com o register US-NY-001 / US-NYB5-301 / -302.
- **(b)** Registrar no QA-REPORT uma limitação nomeada (L-11, "NY por remissão à publicação"), com o que a fecha, e tirar NY do % do juiz até que (a) seja feito.

Para as linhas NY, o veredito passa de "REPROVADO" para "LIMITAÇÃO NÃO DECLARADA".

## V-04 — GA, 2026-01-01..2026-05-10: CONFIRMED S1
**Guia de jun/2026** (`oracle/_src_live/GA_2026-employers-tax-guide-june_wayback-20260913.txt`):
- L76-80: "effective upon signature of HB 463, but retroactive to taxable years beginning on or after January 1, 2026".
- Na mesma passagem: "Employers must continue to withhold at the rate of 5.19% before the effective date of the change".
- L41: o guia se baseia em "tax laws signed into effect on May 11, 2026".
- **Leitura:** a retroatividade vale para o ano-base, ou seja, para a apuração anual. O próprio guia separa a retenção e mantém a regra anterior até a assinatura.

**Guia de dez/2025, em vigor até 10/05** (`GA_2026-employers-tax-guide_wayback-20260116.txt`), Table E, L3873-3896:
- "Annual 24,000.00 12,000.00 12,000.00 4,000.00";
- exemplo: "Less Standard Deduction $1000.00 per Table E (1)" (mensal = 12.000/12).

Antes de 11/05 não havia tabela de retenção com 30.000/15.000/5.000 nem instrumento que mandasse aplicá-la na retenção. Os valores novos só aparecem no guia de junho, Table E L4026-4047: "Annual 30,000.00 15,000.00 15,000.00 5,000.00".

**Nossa research mistura os dois regimes (combinação que nenhum guia publicou):**
- `ga.wh.rate` = 5,19 de 2026-01-01 a 2026-05-10, correto;
- `ga.wh.std_deduction.mfj` = 30.000, `.single` = 15.000 e `ga.wh.dependent_allowance` = 5.000, todos com vigência desde 2026-01-01.
- O mesmo aparece em `annex_GA.md`:
  - L6, sem corte de data na dedução;
  - L33-35.
- E na linha "Flat rate" do `m06` (L42), que só faz o corte de data na taxa.
- Resultado: a retenção dos pagamentos de 01/01 a 10/05 sai menor que a do guia em vigor. É o caso GA-01, (320 − 230,77) × 5,19% = 4,63.

O impacto hoje é retroativo (re-run, ajuste, testes), mas o valor do período está errado. Por isso S1 se mantém.

**Correção mínima:**
- Dividir as 3 chaves por período:
  - de 2026-01-01 a 2026-05-10: 24.000 / 12.000 / 4.000, com register da Table E do guia de dez/2025 (registrar se ainda não houver linha);
  - de 2026-05-11 em diante: 30.000 / 15.000 / 5.000 (US-GAS5-001).
- Ajustar `ga.wh.method` (4,99% fixo no texto), a L6 do `annex_GA` e a linha "Flat rate" do `m06` §6.1.
- Linha no PROPAGATION-LEDGER: CCG annex GA, m06, WTC (US-1xx GA), suíte de validação.

## V-05 — OH SUI 2,85 = 2,7 + 0,15: CONFIRMED (defeito do juiz)
`00-official-sources/precheck-copies/US-OHP7-003.pdf`:
- linha "42 NB Rate 2.7% 0.15% 2.85%";
- legenda: "H Columns E + F + G" e "G Flat surcharge rate per 4141.251".

Nossa research (2,85) está certa. Ressalva menor: o FINDINGS cita "linha 41"; o rótulo no PDF é a linha 42 (NB Rate).

**Correção mínima:** no juiz, somar a sobretaxa de 0,15% (4141.251) à taxa de novo empregador. Corrigir a referência para a linha 42.

## Prova
- **Teste:**
  - varredura de chaves em todos os `_research/*facts.json`;
  - leitura com openpyxl de WTC e DD, procurando NY + bracket/table/NYS-50;
  - grep nos dois guias GA;
  - extração com pypdf do US-OHP7-003.
- **Confiança:**
  - V-04 e V-05: 95%;
  - V-01..V-03: 90%. O rebaixamento depende de aceitar a remissão declarada em L54 como escolha de desenho; se o critério da validação exigir pacote autossuficiente, voltam a S1.

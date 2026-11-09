# EUA — Validação por estado, passo 3b: nossa research × juiz (oracle)
Data 2026-11-06, frente EUA. Liga: [[../PLANO-VALIDACAO|plano da validação]], `../oracle/README.md`. Texto gerado pelo agente de comparação e gravado pela janela EUA, porque a escrita do relatório pelo subagente foi recusada.

## Como foi feito
- `ours.py` usa só estas fontes:
  - `_research/CCG-annex_{FED,CA,NY,IL,PA,OH,NC,MI,GA,TX,FL}-facts.json`;
  - `WTC-country_specific-facts.json`, só para 2 chaves que faltam no CCG: `ny.sui.new_employer.total.rate` e `ny.sit.deduction_allowance.single.annual`;
  - as regras de m03/m05/m06 e dos anexos.
- Cada valor é lido por chave (função `F`). O trace de cada linha está em `compare.json` e marca "RESEARCH-SILENT" quando a research não tem a regra.
- Não foram abertos `oracle.py`, `params_2026.json` nem `params_sources.md`.
- A linha `futa_credit_reduction_er_pending` (15 linhas de CA) ficou fora do %, ver V-08.
- Total: 1.534 de 1.580 linhas = 97,09%. Federal: 1.200 de 1.200.

## Achados
| Id | Estado | Linha | Casos | Classe | Sev. | Evidência | Correção |
|---|---|---|---|---|---|---|---|
| V-01 | NY | sit_NY | NY-01..15 | RESEARCH-DEFECT | S1 | "Method II Exact Calculation Method New York State Single NYS-50-T-NYS (1/26) Page 17 of 23" (ccg-sources/NY/nys50t-nys-1-26.txt l.1035). A research só cita a publicação. | Criar `ny.wh.method2.{single,married}.{freq}.bracket.N.{floor,rate,base}`, as allowances por período e as constantes do Method III; ligar no NY.2 e no m06 §6.2. |
| V-02 | NY | sit_NYC | NY-03, 09, 12 | RESEARCH-DEFECT | S1 | NYS-50-T-NYC índice: "Method II — Exact calculation method and dollar to dollar tables" (l.45). Só a taxa suplementar está nos facts. | `ny.local.nyc.method2.*` + allowances; NY.2. |
| V-03 | NY | sit_YONKERS | NY-11, 13 | RESEARCH-DEFECT | S1 | "A. Yonkers resident tax surcharge … Method II — Exact calculation method" (NYS-50-T-Y l.16-24). Só 1,95975% suplementar nos facts. | `ny.local.yonkers.resident.surcharge.*`; NY.2. |
| V-04 | GA | sit_GA | GA-01..06, 09, 10, 11, 14 | RESEARCH-DEFECT | S1 | Guia jun/2026 p.3: "Employers must continue to withhold at the rate of 5.19% before the effective date of the change". Guia dez/2025, Table E p.46: "Annual 24,000.00 12,000.00 12,000.00 … 4,000.00" (oracle/_src_live/GA_2026-employers-tax-guide_wayback-20260116.txt). | `ga.wh.std_deduction.mfj`/`.single` e `ga.wh.dependent_allowance`: linhas 2026-01-01..2026-05-10 = 24.000/12.000/4.000; as atuais passam a valer de 2026-05-11. Corrigir GA.2 e a linha "Flat rate" do m06 §6.1. |
| V-05 | OH | sui_er | OH-01, 03, 06, 09, 12 | ORACLE-DEFECT | — | ODJFS 2026 Rate Details, linha 41: "Rate 2.7% … 0.15% 2.85%"; coluna H = "Columns E + F + G", G = "Flat surcharge rate per 4141.251" (precheck-copies/US-OHP7-003.pdf). | Research certa (2,85). O juiz deve somar a TCSF de 0,15%. |
| V-06 | PA | sit_PA | PA-11, 13 | AMBIGUOUS | — | REV-415 p.4 só trata acordo voluntário de H-2A: "an H-2A worker may request that a payor withhold … If the payor agrees to withhold". O juiz soma +5; nós não somamos (PA.2: "no PA W-4"). | Decide: posição do PA DOR ou 61 Pa. Code 113 sobre retenção adicional voluntária. Registrar no PA.2. |
| V-07 | CA | sit_CA | CA-03..09, 13, 15 (0,02 a 0,06) | AMBIGUOUS | — | DE 44 Rev. 52 p.45: "Employers may determine the amount of income tax to be withheld for an annual payroll period and prorate the tax back to the payroll period." | Escolha do Design: anual × tabelas por período. CA.2 deve citar essa nota. Se o Design quiser por período, carregar as Tables 1-4 e 8-28. |
| V-08 | CA | futa_credit_reduction_er_pending | 15 (fora do %) | AMBIGUOUS | — | `fed.futa.credit_reduction.ca` em aberto (GAP RQ-402: "becomes final only if the Title XII advance is outstanding on 2026-11-10"). | Decide: página do DOL OUI depois de 10/11 ou Schedule A 2026. |
| V-09 | FED | fit (W-4 antigo) | 16 casos *-10/*-15 (bateram) | RESEARCH-SILENT | S3 | Pub. 15-T 2026 WS 1A Step 2: "marital status (line 3 of Form W-4 from 2019 or earlier) … Don't use the Head of Household table". | m06 §6.1.1 e FED.2: casado → MFJ, solteiro → Single, sem HoH; o extra da linha 6 entra por período. |
| V-10 | NY | dbl_NY | 15 (bateram) | AMBIGUOUS | — | WCL 209(3)(a): "not in excess of sixty cents per week". O m05 diz "convert these per pay period" sem regra; usamos 0,60 × 52/períodos. | Decide: orientação WCB/DFS para folha não semanal. Registrar no NY.3 e no m05. |
| V-11 | MI | sit_MI | 15 (bateram); MI-14 diário | AMBIGUOUS | — | `mi.wh.method`: "Per-period exemption weekly 113.46, biweekly 226.92 … (derived). No rounding rule." Nada para folha diária. | Decide: tabela por período do Form 446 ou a calculadora do Treasury. MI.2. |
| V-12 | NY | sit_NY (arredondamento) | não testável | AMBIGUOUS | — | GAP RQ-263: o exemplo 2 imprime 258,51 e a conta half-up dá 258,50. | Decide: convenção do DTF; testar depois de V-01. |
| V-13 | NY | pfl_NY | NY-14 (bateu) | RESEARCH-SILENT | S3 | O NY.3 traz taxa e teto 411,91, mas não como acumular o que já foi retido. | NY.3: acumulador anual da PFL retida. |

## Veredito (≥95% + 0 S1 + AMBIGUOUS nomeados)
| Estado | % | S1 | Veredito |
|---|---|---|---|
| FED | 100 | 0 | APROVADO COM RESSALVA (V-09) |
| CA | 95,00 | 0 | APROVADO COM RESSALVA (V-07, V-08) |
| NY | 89,19 | 3 | REPROVADO |
| IL | 100 | 0 | APROVADO |
| PA | 98,79 | 0 | APROVADO COM RESSALVA (V-06) |
| OH | 96,67 | 0 | APROVADO (V-05 é do juiz) |
| NC | 100 | 0 | APROVADO |
| MI | 100 | 0 | APROVADO COM RESSALVA (V-11) |
| GA | 93,33 | 1 | REPROVADO |
| TX | 100 | 0 | APROVADO |
| FL | 100 | 0 | APROVADO |

## Prova
- **Teste:** `python compare.py` refaz a comparação (Decimal, half-up). GA-01 foi conferido à mão: (320 − 230,77) × 5,19% = 4,63, igual ao juiz.
- **Fontes lidas:** DE 44 p.45/50, Pub. 15-T WS 1A, NYS-50-T-NYS/NYC/Y, guias GA dez/2025 e jun/2026, ODJFS 2026 Rate Details, REV-415, ORC 4141.25.
- **Confiança:** 95%.
  - V-04 depende de ler "effective upon signature" como valendo também para a dedução padrão na retenção, e não só para a taxa.
  - V-06, V-08, V-10 e V-11 esperam decisão externa.
- **Pendente:** conferência independente dos 4 S1 pelo revisor, antes de corrigir.

## Rodada 2 (2026-11-06, depois da versão 1.1 dos facts)
- O que mudou:
  - Facts GA e NY corrigidos (V11);
  - juiz de OH corrigido (V-05: 2,7% + 0,15% da sobretaxa ORC 4141.251 = 2,85%, em `oracle/params_2026.json`; backups `*.r1.json`);
  - `ours.py` calcula NY Method II/III, NYC e Yonkers pelas chaves novas (backup `ours.r1.py`).
- Total: 1.568 de 1.580 = 99,24%. Federal segue 1.200/1.200.
- **V-01..V-04: fechados.** NY: 184 de 185 linhas batem, 0 divergência. GA: 150/150.
- Novo achado **V-14** (NY, RESEARCH-SILENT, S3):
  - Falta o valor semanal de `ny.local.nyc.method2.single.deduction_allowance` (o NY-09 sit_NYC ficou sem conta).
  - As tabelas por período do NYS-50-T não estão em chaves; o nosso lado as deriva da tabela anual (nota do próprio fact), o que pode divergir perto do limite de faixa.
  - Correção: chavear as tabelas por período e as allowances de todas as frequências.

| Estado | % | S1 | Veredito (rodada 2) |
|---|---|---|---|
| FED | 100 | 0 | APROVADO COM RESSALVA (V-09) |
| CA | 95,00 | 0 | APROVADO COM RESSALVA (V-07, V-08) |
| NY | 99,46 | 0 | APROVADO COM RESSALVA (V-10, V-12, V-14) |
| IL | 100 | 0 | APROVADO |
| PA | 98,79 | 0 | APROVADO COM RESSALVA (V-06) |
| OH | 100 | 0 | APROVADO |
| NC | 100 | 0 | APROVADO |
| MI | 100 | 0 | APROVADO COM RESSALVA (V-11) |
| GA | 100 | 0 | APROVADO |
| TX | 100 | 0 | APROVADO |
| FL | 100 | 0 | APROVADO |

- **Teste:** `python compare.py` (tabela acima); `python ../oracle/reference_tests.py` = 35/38 (os 3 que não batem: diferença de 1 centavo nos exemplos impressos de NY, V-12).

## Rodada 3 (2026-11-06): chaves por período de NY
- 550 chaves novas de NY por período (NYS-50-T-NYS/NYC; `US-compliance/_research/validation/V11-facts-fix.md` item 5); `ours.py` lê essas chaves primeiro (backup `ours.r2.py`).
- NY: 185 de 185 = 100%, nenhuma linha usou a derivação anual. **V-14 fechado.** NY: APROVADO COM RESSALVA (V-10, V-12).

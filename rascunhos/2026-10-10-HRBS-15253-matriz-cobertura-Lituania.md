# HRBS-15253: Accenture Lithuania, matriz de cobertura (visão de Compliance)

- **Data:** 2026-10-10
- **Ticket:** HRBS-15253 (Kevin Gunawan, REF-LE-04-359, Live/BAU)
- **Natureza:** **visão de Compliance**, ou seja, se a regra está documentada nos nossos artefatos. **A coluna de sistema (S/C/M/N) é de Configuration/Product** e não foi preenchida aqui.
- **Status usados:** **Coberto** (regra documentada) · **Parcial** · **Lacuna** (Compliance não documentou) · **Fora de Compliance** (Config/Product/HR/Integração)
- **Rascunho:** nada foi enviado ao ticket. O hub [[Lituania]] está desatualizado (diz "nenhum artefato citado") e precisa ser atualizado, com aprovação, a partir desta nota.

## O que foi lido (pasta Drive exportada em 2026-10-10)

| Pasta / arquivo | Versão / data | Observação |
|---|---|---|
| `05 - Payroll Regulation Guide/2026 Regulation guide/Lithuania Payroll Regulation Guide_2026.docx` (= **CCG 2026**) | sem controle de versão nem aprovação | Base principal de regras. Tem inconsistências internas (ver NPD) |
| `09 - Alerts/2026/Lithuania_Changes in Tax Rates & social security Rates - 1st January 2026.docx` (= **Alerta 2026**) | vigência 2026-01-01 | Faixas GPM, NPD único, MMA, teto e limite de €350 para seguro saúde |
| `03 - WTC/Lithuania  WTC V3.0.xlsx` | V3.0, 2025-06-30, Approved | Estrutura de 2025. Não tem nada de 2026 |
| `02 - DD/Lithuania Data Dictionary V3.0.xlsx` | V3.0, 2025-07-08, Approved | Campos de 2025 |
| `02 - DD/LT - All report fields.xlsx` | sem versão | Mapeamento antigo de SAM, GPM313 e GPM312 |
| `06 - Payroll Implementation Guide/Payroll LT Implementation Guide.docx` (= **IG**) | change history 2025-06-12 | Lógica G2N de 2025 (MMA 1.038, 20%/32%) |
| `07 - Design/Annual Tax Brackets.xlsx`, `LT Draft Regulations.xlsx` (CT-3213) | 2025 | Faixas 20%/32% com €126.532,80 e lista das tax rules |
| `04 - Tax Calculator/*`, `11 - Simulations/*` (inclui `Tax flow.xlsx` e `Research/Copy of Average salary calculation rules.xlsx`) | 2025 (MMA 1.038) e 2022 | Notas de design, perguntas da época e regra de salário médio |
| `18 - Statutory Reports/LT-SODRA-003-SAM-Spec.xlsx` | v1.0, 2026-08-21 | SAM v07 com SAM3SD e SAM3SDP (V-243 consolidado em 2026-01-01) |
| `18 - Statutory Reports/LT-VMI-001-GPM313-Spec.xlsx` | v1.0, 2026-08-21 | VA-121 na redação do VA-105 (2025-11-20) |
| `18 - Statutory Reports/LT-VMI-002-GPM312-Spec.xlsx` | v1.0, 2026-08-21 | VA-9 na redação do VA-24 (2026-03-26) |
| `12- Country Report Codes/**` | 2018 a 2025 | Instruções de SAM, 1-SD, 2-SD e NP-SD; .mxfd de SAM v07, 1-SD v10, 2-SD v09, NP-SD2 v01, GPM312 (2025-01) e GPM313 (2023-01); IN_GPM313 2022; IN_GPM312; listas de filings (2022 e contratual); G2N; payslip spec |
| `17 - Payslip/LT_Compliance_Payslip_Generator.xlsx` | sem versão | Abas "Lithuania (EN)" e "Lithuania (LT)" |
| `15 - Release Note/LT Release Note.pdf` | LT-253649, deploy 2025-07-16 | Release original: 20% ou 32%, sem 25% |

Não abri `10 - ICE Support` (instrução). Também não li dados de empregados (QC 2025 e SAM de cliente).

---

## Matriz (Partes 1 a 4, ordem original)

### PART 1 — CALCULATION

#### A. Bases and element treatment

| Item | Visão de Compliance | Onde está | Regra / valor 2026 (fonte, vigência) | Observação |
|---|---|---|---|---|
| Separate GPM (taxable income) base and Sodra (contribution) base, independently derivable | **Coberto** | CCG 2026 › Income Tax › Taxable Base e Social Security › Social security Base; IG › "Period Gross Earnings Taxability Matrix" (58008) × "Social Security Taxability Matrix" (58550) | GPM: pago menos não tributável menos NPD (CCG, art. 16 GPMI). Sodra: bruto menos as exclusões listadas, entre elas o auxílio-doença (CCG) | O SAM exclui ainda direitos autorais, atividade esportiva e artística e tantièmes (SAM spec › Population Rules, A11, ponto 55.1). Por isso a base do SAM não é igual à base tributável do GPM313 |
| Element-level flags per wage type — taxable yes/no, contributory yes/no, set independently | **Coberto** | WTC V3.0 › colunas "Subject to Tax", "Table Tax", "Special Tax", "Subject to Social Insurance", "Subject to Pension" | Flags independentes por WT. Ex.: 79408 Sick leave = Tax Yes, Special Tax "15%", SI No | O IG aplica os flags por **série** (padrões 621%%, 6257% etc.), não WT a WT. Configuration precisa confirmar se o sistema segue o WTC ou a série |
| Benefits in kind — valuation and inclusion in both bases | **Parcial** | WTC 65400–65859 (car, phone, meal, housing, health insurance); GPM312 spec › L6/U6 (A = carro, N = outros em espécie) | Inclusão em ambas as bases está no WTC. **Regras de valoração (carro, moradia etc.) não estão no CCG** | Divergência: o Alerta 2026 cria limite de **€350/ano** isento para seguro saúde voluntário pago pelo empregador (a partir de 2026-01-01). O CCG 2026 (Non-Taxable Pay) e o WTC (23610 e 65810) ainda usam a regra antiga de 25% da renda anual. O WTC 65630 Health Insurance Benefit está 100% tributável |
| Allowances — including any treated as non-taxable, with the exemption basis held against the element | **Parcial** | CCG › Non-Taxable Pay (art. 17 GPMI); WTC coluna "Formula" (65805 "Non taxable up to 200 Euro per year", 23610 "25%"); WTC 62570/62830 Daily/Business Trip (code 05, não tributável) | Não tributáveis segundo o CCG: auxílio por morte de familiar, diárias e despesas de viagem comprovadas, presentes até €200/ano, transporte público, stock options (3 anos) e seguros/pensão até 25% (este último superado pelo Alerta para seguro saúde) | O fundamento da isenção só está no elemento em poucos WTs. As séries 62860 (Meal), 62866 (Birth) e 62868 (Gift) estão sem tributação e sem base legal anotada. Há dois Prize/Gift: 65805 não tributável e 65835 tributável |
| Bonuses and one-time payments | **Coberto** | CCG › Taxable Pay (bonuses); WTC 62200–62229 (tributável + SI); SAM spec › Payroll Scope (ponto 51.6) | GPM no mês do pagamento. No SAM, no mês em que foi calculado (51.6) | Para o salário médio, há regra de rateio de bônus trimestral (1/4) e anual (1/12) em `Average salary calculation rules` (material de pesquisa de 2022) |
| Retro and backdated payments — which period's parameter set is applied | **Coberto** | CCG › Taxable Pay (Ex. 1 e 2) e Social security Base (Ex. 1 a 3 + notas) | **GPM: mês do pagamento**, sem reenviar declarações. **Sodra: mês de competência**, com reenvio da declaração do mês original (juros e multas; limite de 5 anos). Prática local: pagar como bônus no mês corrente | Consequência: retro de Sodra usa os parâmetros do mês de origem, mesmo de ano anterior. Ver item G "Concurrent parameter sets" |

#### B. Employee contributions (Sodra)

| Item | Visão de Compliance | Onde está | Regra / valor 2026 | Observação |
|---|---|---|---|---|
| Pension insurance | **Coberto** | CCG › Social security rates; IG › Social Security (58150) | **8,72%** (CCG 2026) | Mesma taxa no IG de 2025 |
| Sickness insurance | **Coberto** | CCG; IG 58151 | **1,99%** (CCG 2026, "Diseases") | |
| Maternity insurance | **Coberto** | CCG; IG 58152 | **1,81%** (CCG 2026) | |
| Health insurance (PSD) | **Coberto** | CCG › Health insurance; IG 58163 | **6,98%**, sem piso nem teto. Só empregado (CCG 2026) | Divergência: o CCG isenta "estrangeiros sem autorização de residência" (e diz que, desde 2024-07-01, na prática todos contribuem). O IG corta o PSD quando **Residential Status = non-resident** (58218 = 1). Residência fiscal não é critério de PSD no CCG |
| Pillar II pension accumulation — driven by a participation flag on the employee master | **Coberto** | CCG (nota "additional 3%"); DD › Country Fields "Additional Pension Eligibility"; WTC 58202 / 21650 / 58153 | **+3%** sobre a base Sodra (CCG 2026). Janela de retirada entre 2026-01-01 e 2027-12-31 (CCG) | O flag existe no DD |
| Combined employee rate correct with and without Pillar II | **Coberto** | CCG ("Total contributions 12,52%") | VSD **12,52%**; com Pillar II **15,52%**. Somando PSD 6,98%: **19,50%** / **22,50%** (soma feita por nós a partir do CCG) | O SAM P3 pede **taxa total (empregado + empregador)** por pessoa (SAM spec; All report fields). O CCG traz um aviso de que "ICE confirmed no need to split" |

#### C. Employer contributions (Sodra)

| Item | Visão de Compliance | Onde está | Regra / valor 2026 | Observação |
|---|---|---|---|---|
| Unemployment insurance | **Coberto** | CCG › Employer contributions; IG 58157 | **1,31%** contrato por prazo indeterminado; **2,03%** prazo determinado (CCG 2026) | |
| Guarantee Fund | **Coberto** | CCG; WTC 52550 / 58159 | **0,16%**. Isentos: Banco da Lituânia, instituições orçamentárias, partidos, sindicatos e comunidades religiosas (CCG) | A isenção não tem flag no DD |
| Long-Term Employment Benefit Fund | **Coberto** | CCG; WTC 52565 / 58160 | **0,16%**. Isentos: Banco da Lituânia e instituições orçamentárias (CCG) | A isenção não tem flag no DD |
| Accidents at work — rate configurable per legal entity by assigned Sodra risk group | **Coberto** | CCG; DD › Legal Entity "Type of Employer" (Group 1–4); IG 58158 | Grupo I **0,14%**, II **0,43%**, III **0,70%**, IV **1,40%** (CCG 2026) | |
| Contract-type driven rate switch — open-ended versus fixed-term | **Coberto** | CCG (nota + Exemplo 5); DD "Employment Type" | Na troca no meio do mês: dois registros na Sodra, cada parte com a sua taxa (CCG) | Pelo `Tax flow.xlsx`, dois contratos no mesmo mês = "product feature" (não é regra de Compliance). O Tax Calculator mostra 58215 com 3 opções no design e 2 na entidade |

#### D. Income tax (GPM)

| Item | Visão de Compliance | Onde está | Regra / valor 2026 | Observação |
|---|---|---|---|---|
| Base rate withholding | **Coberto** | CCG › Tax Rates / Tax Calculation Process | **20%** fixo na folha. Auxílio-doença: **15%** (CCG 2026, art. 6 GPMI) | GPM313 spec, regra 9.4: 15% fixo também para maternidade, paternidade, cuidado infantil e tempo de serviço (benefícios pagos pela Sodra) |
| Higher bands — including the band structure change effective 1 January 2026 | **Parcial** | CCG › Tax Rates; Alerta 2026; GPM313 spec (regras 9.5.1–9.5.3) | **20%** até €82.962; **25%** de €82.962 a €138.270; **32%** acima de €138.270 (anual, CCG 2026 e Alerta 2026). Em VDU: 36 e 60 VDU (GPM313 spec / VA-105) | Divergências: (1) a tabela do Alerta 2026 diz "Below 82 962 = **0%**", erro de digitação (CCG e spec dizem 20%); (2) **DD, IG, WTC, Release Note e `07 - Design/Annual Tax Brackets` ainda estão em 20%/32%** (a 32% sobre a base inteira, flag "consent to be taxed at 32%"). Nenhum artefato de design tem a faixa de 25% |
| Cumulative in-year tracking to drive band progression, or the agreed alternative mechanic | **Lacuna** | CCG ("monthly calculation method"; progressiva só a pedido do empregado, normalmente na declaração anual); GPM313 spec, regra 9.6 | CCG: método mensal, sem ajuste no fim do ano. GPM313 spec (regra 9.6): a pedido, a taxa progressiva é aplicada com base nos pagamentos **acumulados e previstos no ano** | Não há regra documentada para acumular no ano nem uma alternativa acordada para 2026. O design de 2025 dividia a faixa anual por 12 (€10.544,40/mês) |
| Standard NPD, year-specific formula, tapering with income | **Parcial** | CCG › Pre-Tax Deductions (TEAI/NPD); Alerta 2026; IG › Pre-Tax Deductions | **Alerta 2026:** NPD = 747 − 0,49 × (renda mensal − 1.153); €747 até €1.153; **zero acima de €2.677,49** | **Divergência material:** o CCG 2026 mantém a estrutura de 2025 com duas fórmulas (corte em €2.387,29 e "400 − 0,18 × (renda − 642)"), mas o Exemplo 3 do próprio CCG já usa a fórmula única. O IG ainda usa MMA €1.038 (2025). Vale o Alerta, que é coerente: 1.153 + 747/0,49 = 2.677,49 |
| Fixed NPD for reduced capacity for work — non-tapering, both capacity brackets | **Coberto** | CCG; Alerta 2026; DD "Incapacity Level"; IG 58100 | **€1.127** (0–25%) e **€1.057** (30–55%), sem redução por renda e iguais a 2025 (Alerta 2026) | Faixas inconsistentes entre documentos: DD "0–25% / 30–40% / 45–55%"; CCG "0–25% / 30–55%"; IG "40–55%"; Tax flow "20–55%". O Alerta fala em "capacity for work" e o DD/CCG em "incapacity". Precisa confirmar a semântica |
| NPD waiver flag on the employee master | **Coberto** | CCG (consentimento por escrito); DD "Tax Exemption Eligibility"; IG 58204 | O NPD só é aplicado na folha **com consentimento por escrito** do empregado (CCG) | No nosso modelo é opt-in, não renúncia. Default no DD: "0-Yes" |
| NPD capped at taxable income so it can never exceed the base it reduces | **Lacuna** | CCG ("negative TEAI = 0", sem transporte para o mês seguinte); IG 58552 = 58008 + 58100 + 58101 | Documentado: NPD ≥ 0 e não acumula para o mês seguinte | **Não há regra que limite o NPD à base tributável.** A fórmula do IG não tem MAX(0) na base |
| Non-resident treatment | **Parcial** | CCG › Residency / NPD; DD "Residential Status"; GPM312 spec (anexo U, U12–U15, marcador U do VA-24) | Não residente é tributado só sobre renda de fonte lituana. **Sem NPD na folha** (só na declaração anual) (CCG) | Falta no CCG: tratado ou crédito, alíquota específica e PSD de estrangeiro (ver item PSD). O critério de residência fiscal (183/280 dias) está no CCG |

#### E. Ceilings and floors

| Item | Visão de Compliance | Onde está | Regra / valor 2026 | Observação |
|---|---|---|---|---|
| Sodra annual ceiling — tracked cumulatively, pension/sickness/maternity stop, health continues uncapped | **Parcial** | CCG › Social security rates + Calculation Process (S50); Alerta 2026; `Tax flow.xlsx` linha 141 | **€138.270/ano** em 2026 (era €126.532,80 em 2025) (CCG e Alerta). PSD sem teto (CCG) | Mecanismo documentado: **a Sodra avisa** o empregador (extrato S50) e o empregado deixa de contribuir. Pela nota de design, calcula no mês do aviso e para no mês seguinte. **Não há regra de acumulado no sistema** (IG só tem override/refund manuais: 52517, 58164, 62641, 23641). Falta dizer se o Pillar II também para no teto |
| Minimum contribution base (MMA floor) — contributions calculated on at least the minimum wage | **Parcial** | CCG › Social Security Calculation Process (Note 1 + Ex. 1 e 2); Alerta 2026 | MMA **€1.153/mês** a partir de 2026-01-01 (CCG e Alerta). Contribuição do empregador sobre pelo menos o MMA; diferença apurada pela Sodra (S50) | O piso **não está no WTC, DD nem IG**: a base do empregador é o 58550 real. **A verificar:** o CCG aplica o piso só às taxas do empregador. Não está documentado se a diferença inclui a parte do empregado custeada pelo empregador |
| Floor exemption categories held per employee and applied automatically | **Lacuna** | CCG lista as exceções: ≤ 24 anos, mais de um empregador, aposentado | Exceções existem no CCG | **O DD não tem nenhum campo** (idade vem da data de nascimento; faltam "outro empregador" e "aposentado") |
| Floor behaviour for partial months — joiners, leavers, unpaid leave | **Parcial** | CCG (licença não remunerada com 12-SD) | Licença não remunerada informada no 12-SD: MMA ÷ dias úteis oficiais do mês × dias efetivamente trabalhados (CCG) | Admissão e desligamento no meio do mês: não documentado |

#### F. Absence and statutory pay

| Item | Visão de Compliance | Onde está | Regra / valor 2026 | Observação |
|---|---|---|---|---|
| Employer-funded first days of sick pay, then handover to Sodra | **Parcial** | WTC 79408 ("First two days paid by employer, after two days paid by the government", tax code 03, 15%, sem SI); GPM312 spec (código 03, regra 27); GPM313 spec (box 5); `Average salary calculation rules` | 2 primeiros dias pelo empregador, depois Sodra. Tributado a 15% e fora da base Sodra | **% do salário médio pago pelo empregador não documentado.** Notificação NP-SD só com material de 2018/2025 (ver Parte 3) |
| Maternity, paternity and childcare leave handling | **Parcial** | WTC 65700–65712 (Maternity Allowance), 79420 Parental leave ("mamadienis"), 79406/79407; Statutory filings (9-SD); GPM313 spec, regra 9.4 (15%) | Benefícios pagos pela Sodra; empregador informa via 9-SD | O CCG não tem seção de licenças. Falta: dia extra para pais (mamadienis/tėvadienis), relação com SAM3SDP e PA-DP |
| Annual leave accrual and leave pay on the statutory average-earnings basis | **Parcial** | `11 - Simulations/Research/Copy of Average salary calculation rules.xlsx`; WTC 62300–62305, 79450 | Salário médio = 3 meses anteriores, sem o mês da licença; inclui elementos ligados ao trabalho; bônus trimestral 1/4 e anual 1/12; usado em férias, doença, licença parental, férias não gozadas e indenização | É material de pesquisa de 2022 ("Copy of"), não está no CCG e não tem fonte legal. **Acúmulo de férias (dias de direito) não documentado.** No SAM, férias que atravessam o mês são divididas por mês (SAM spec, ponto 51.4) |
| Labour Code premiums — overtime, night work, public holiday, rest-day | **Parcial** | WTC 62110–62153 (Overtime, Night work, Day Off, Bank Holiday) | WTs existem, tributáveis e com SI | **Multiplicadores do Código do Trabalho não documentados** no CCG |
| Severance on termination | **Parcial** | WTC 62180–62182 (Severance Pay, tributável + SI); CCG › Taxable Pay; 2-SD instruction (A33, meses de indenização média) | Indenização é tributável (CCG) | **Valores e meses por tempo de casa não documentados** |
| Final settlement on termination | **Parcial** | WTC 79450 Unused Holiday compensation, 62880 Post-Termination; 2-SD (ref. 2025) | Elementos existem | Falta regra de acerto final no CCG. Quem tem 2-SD no mês sai do SAM3SD (SAM spec, ponto 51.1) |

#### G. Cross-cutting

| Item | Visão de Compliance | Onde está | Regra / valor 2026 | Observação |
|---|---|---|---|---|
| Rounding convention — component level, and the register total equals the sum of the components | **Coberto** | CCG › "Rounding off provisions" (GPM, Sodra e PSD); SAM spec (erro C2344); GPM313 spec (HALF_UP 2 casas) | Não estabelecido em lei; usa-se arredondamento matemático com 2 casas (CCG) | **Risco:** a Sodra valida **A12 = A11 × P3** (taxa total) linha a linha, ao centavo (C2344). A soma de componentes arredondados um a um pode errar por 1 centavo |
| Mid-month joiner and leaver proration | **Parcial** | WTC (Pro Rata nos recorrentes); IG teste LT12 "pass"; `Average salary calculation rules` (dias úteis oficiais) | Não há regra legal de proporcionalidade no CCG | Método de proporcionalidade é de Config. Compliance só tem os exemplos de 2022 em dias úteis |
| One person holding more than one contract or appearing in more than one entity | **Parcial** | CCG (troca de contrato = dois registros; exceção de MMA para "mais de um empregador") | Regras pontuais documentadas | Multi-entidade e dois contratos no mesmo mês ficaram como "product feature" no design de 2025 |
| Concurrent parameter sets — prior year and current year held simultaneously for retro processing | **Fora de Compliance** | CCG (Sodra pelo mês de competência; GPM pelo mês de pagamento) | Exigência de Compliance: retro de Sodra usa parâmetros do mês de origem; GPM usa os do mês de pagamento | Manter dois conjuntos de parâmetros é capacidade do sistema (Product) |
| EU coordination cases and A1 certificate populations | **Lacuna** | só no lado fiscal: GPM312 spec (L12/L13 imposto estrangeiro, U7 marcador "U") | — | Nada sobre A1, legislação aplicável (Reg. 883/2004) ou LDU além de uma linha no template de filings de 2022 |

### PART 2 — REPORTING, MONTHLY

| Item | Visão de Compliance | Onde está | Regra / valor 2026 | Observação |
|---|---|---|---|---|
| SAM, with the SAM3SD appendix (per-employee income and contributions) | **Coberto** | `18 - Statutory Reports/LT-SODRA-003-SAM-Spec.xlsx` v1.0 (2026-08-21) | Mensal, até o **dia 15 do mês seguinte** (ponto 52). SAM3SD: todos os segurados exceto quem teve 2-SD no mês (51.1); A11 / P3 (taxa no início do mês) / A12 | Base: V-243 consolidado em 2026-01-01; formulário SAM **v07** (MXFD de 2021) |
| SAM3SDP appendix for exception populations | **Coberto** | SAM spec › SAM Spec, Field Options e Population Rules R9–R11 | Códigos de motivo **01–10** (sem 99); 04 só para períodos até 2021-12-31; A21/A22 dentro do mês | A spec corrige o mapeamento antigo (`All report fields`), que só tem descrição genérica |
| Generated as a .ffdata file to Sodra's published data structure | **Parcial** | SAM spec › File Structure / Population Rules R13; `SAM-v07.mxfd`; `SAM-V07 SAMPLE.ffdata` | FFData XML conforme a descrição publicada no site da Sodra (ponto 250) | **A descrição oficial da estrutura FFData não está na pasta**. A spec chama isso de "the single largest open item". Envelope reconstruído pelo MXFD; "data structure v03" não confirmada |
| Submitted by upload to EDAS, or machine-to-machine via the EDAS data service | **Fora de Compliance** | SAM spec › Report Matrix (pontos 8, 249, 250, 88) | Canal: EDAS, com assinatura eletrônica qualificada. Aceite pelo EDAS (ponto 84.1) | Upload ou M2M é integração. Compliance documentou só o canal legal |
| GPM313 — monthly declaration of A-class payments and tax withheld, as totals | **Coberto** | `18 - Statutory Reports/LT-VMI-001-GPM313-Spec.xlsx` v1.0 (2026-08-21) | Até o **dia 15 do mês seguinte** (regra 12; art. 24(2) GPMI). 12 campos; declaração zerada obrigatória se houve empregados no mês (regra 4) | Base: VA-121 na redação do VA-105 (2025-11-20) |
| Generated as a .ffdata file to the VMI structure, submitted via EDS | **Parcial** | GPM313 spec › File Structure (nível 3: "No file-level container"); `GPM313.zip` (.mxfd de 2023-01) | Só eletrônico, via EDS (regras 6 e 14) | Divergência: a spec diz que a ordem **não prescreve FFData** (formulário online ou upload EDS). A pasta tem um GPM313.mxfd de **2023**, anterior ao VA-105. Falta o esquema de upload EDS vigente |
| Tax payment date derived from the actual pay date, not the declaration deadline | **Parcial** | GPM313 spec (campos 6 e 7, regras 9.2 e 9.3, art. 23 GPMI); CCG › GPM 313; IN_GPM313 2022 | Campo 6 = GPM de pagamentos **até o dia 15 (inclusive)**; campo 7 = **depois do dia 15 até o fim do mês**. A divisão é pela data de pagamento | Os documentos dizem que a divisão gera "prazos de recolhimento diferentes (art. 23)", mas **não trazem os prazos** ("até 15 do mesmo mês" / "último dia do mês"). A regra do Kevin não está confirmada nos nossos documentos |
| Payslip — confirm available language options | **Coberto** | `17 - Payslip/LT_Compliance_Payslip_Generator.xlsx` (abas "Lithuania (EN)" e "Lithuania (LT)"); `LT Payslip Specification.xlsx` | **EN e LT** | Payslip personalizado é Config (IG › Payslips) |
| Bank payment file in the format the client's bank accepts | **Fora de Compliance** | IG › Bank Files (tabela vazia) | — | Config / Implementation |
| GL posting file, including the employer contribution liability | **Fora de Compliance** | `LT Country Specific Gross to Net.xlsx` ("Employer Liability = Net Pay + Employer Contributions") | — | Config / Product |
| Reconciliation report tying the register to SAM and to GPM313 before submission | **Fora de Compliance** | — | Insumo de Compliance: **SAM e GPM313 não fecham por definição.** A base do SAM é por competência e exclui direitos autorais, tantièmes etc.; o GPM313 é por data de pagamento e antes do NPD (SAM spec R7; GPM313 spec R5) | Relatório é de Product. Compliance pode fornecer as regras de conciliação |

### PART 3 — REPORTING, EVENT-DRIVEN

> Se é gerado pelo sistema ou digitado, e se fica com payroll ou com HR: **não é de Compliance** (Delivery/Config). Para referência, a lista contratual `List of Statutory Filings Lithuania.xlsx` diz que o vendor prepara e envia 1-SD, 2-SD, 9-SD, 12-SD, notificação de doença e de estrangeiro (base fee), e childbirth/childcare como ad-hoc cobrado.

| Item | Visão de Compliance | Onde está | Regra / valor 2026 | Observação |
|---|---|---|---|---|
| 1-SD — start of insurance, due before the first working day | **Lacuna** | Só referência: `Archieved/.../1-SD instruction.docx`, `1-SD_v10.mxfd` (2019), PDF; `Statutory filings template 2022` | Prazo: **1 dia antes** do início (template 2022; CCG, nota em Social security Base) | Sem spec Mercans e sem versão vigente do formulário confirmada |
| 2-SD — end of insurance | **Lacuna** | Só referência: `2-SD instruction.docx`, `2-SD-v09.mxfd` (2018), `2-SD-SAMPLE.FFDATA` (2024) | Prazo: até o último dia de trabalho (template 2022) | Interage com o SAM (quem teve 2-SD sai do SAM3SD) |
| 9-SD — childcare leave granted or revoked | **Lacuna** | Só citado: template 2022 e lista contratual | Até o dia seguinte ao início da licença (template 2022) | Condição para dispensar o SAM (ponto 49) |
| 12-SD — non-insured periods, including unpaid leave | **Lacuna** | Citado no CCG (proporção do MMA) e no template 2022 | Até o dia seguinte ao início da licença (template 2022) | Afeta o piso MMA |
| 13-SD — copyright, sports and performer agreements | **Lacuna** | Só citado na SAM spec (File Structure R9) | — | Ligado às exclusões da base do SAM |
| NP-SD — benefit application support | **Lacuna** | Só referência: `NPSD instruction.docx`, `NP-SD2-v01.mxfd` (2018), PDF de exemplo | No último dia da licença médica (template 2022) | Inclui B7 (auxílio pago pelo empregador) e B8 (motivos) |
| PT — correction of previously submitted insured-person data | **Parcial** | SAM spec › Population Rules R4 e Report Matrix (pontos 52, 86.6–86.8, 91.3.1, 92.4) | Correção por PT com anexos PT-SAM3SD, PT-SAM3SD-M e PT-SAM3SDP; **SAM entregue com atraso exige PT com motivo 01** | O formulário PT não tem spec. Está em aberto qual rota usar (P35 no SAM ou PT) e a spec manda confirmar com a Sodra |

### PART 4 — REPORTING, ANNUAL

| Item | Visão de Compliance | Onde está | Regra / valor 2026 | Observação |
|---|---|---|---|---|
| GPM312 — annual declaration, due 15 February | **Coberto** | `18 - Statutory Reports/LT-VMI-002-GPM312-Spec.xlsx` v1.0 (2026-08-21); CCG › GPM 312 | Até **15 de fevereiro** do ano seguinte (regra 57). Campos 4–7 calculados a partir dos anexos | Base: VA-9 na redação do **VA-24 (2026-03-26)** |
| GPM312L appendix — per-recipient detail for residents | **Coberto** | GPM312 spec (L1–L13) | Uma linha por pessoa × classe × código × alíquota × espécie/dinheiro; código 03 para os 2 primeiros dias de doença | |
| GPM312U appendix — per-recipient detail for non-residents | **Coberto** | GPM312 spec (U1–U15) | U12 data de nascimento obrigatória; novo marcador **"U"** (VA-24) para trabalho feito no exterior | |
| Generated as .ffdata to the VMI structure, at full-year by full-headcount volume | **Parcial** | GPM312 spec › File Structure ("No file-level container"); `Taxes/GPM312 - Annual/GPM312 (1).zip` (.mxfd de 2025-01) | Só eletrônico via EDS (regras 11 e 59) | Mesma divergência do GPM313: o MXFD da pasta é **anterior ao VA-24**. Volume e desempenho são de Product |
| Annual leave provision and accrual roll-forward | **Fora de Compliance** | — | — | Provisão é contábil (Config/Finance). O direito legal de férias também não está no CCG (ver Parte 1, F) |
| Year-end parameter changeover — new rates and thresholds available before the January run | **Parcial** | Alerta 2026; CCG 2026 | Compliance publicou o Alerta de 2026-01-01 | **WTC, DD e IG continuam em 2025** e a pasta não tem release note de 2026. Compliance precisa dizer se a mudança de 2026 foi passada para Product. A carga no sistema é de Product |

---

## Parte 5: respostas de Compliance

1. **Quem mantém as estruturas .ffdata e como recebemos mudança de versão?**
   - Compliance mantém as **specs** com a versão do formulário oficial em que se baseiam: SAM **v07** (V-243 consolidado em 2026-01-01), GPM313 pelo **VA-105** (2025-11-20) e GPM312 pelo **VA-24** (2026-03-26).
   - O **gerador do arquivo** é de Product/Integração.
   - Lacunas: a descrição oficial da estrutura FFData da Sodra não está na pasta. Os MXFD de GPM313 (2023) e GPM312 (2025-01) são anteriores às ordens vigentes. As specs da VMI dizem que as ordens não prescrevem FFData.
   - Também não há processo documentado de monitoramento de versão. Hoje só existe o alerta anual.
2. **Existe teste ou dry-run de upload?** Compliance não tem nada sobre ambiente de teste da Sodra ou da VMI. É assunto de Integração. A SAM spec só registra que o aceite vem pelo EDAS.
3. **Como funcionam as correções?**
   - **SAM:** pela solicitação **PT** (anexos PT-SAM3SD, PT-SAM3SD-M e PT-SAM3SDP; pontos 86.6–86.8). SAM com atraso exige PT motivo 01. Ainda falta confirmar com a Sodra a rota P35/P14T/P17T.
   - **CCG:** Sodra corrige no mês de competência (limite de 5 anos); GPM no mês do pagamento, sem reenvio.
   - **GPM313:** nova declaração completa do mês (regra 18). A regra 19.2 proíbe corrigir, depois de encerrado o período, GPM retido a maior e erro de NPD de residente.
   - **GPM312:** nova declaração completa (regra 63). **Regra 65: se o valor alterado no GPM312 entrou agregado num GPM313, esse GPM313 também precisa ser corrigido.** Isso **corrige a nossa resposta de 2026-09-28**, que dizia não haver documentação: a regra está na GPM312 spec.
4. **Existe parameter sheet de 2026 aprovada?** Não.
   - O mais próximo é o CCG 2026, sem controle de versão nem aprovação e com o NPD desatualizado, junto com o Alerta 2026.
   - WTC e DD V3.0 estão aprovados, mas são de 2025.
   - O dono é Compliance. Proposta: emitir uma planilha de parâmetros 2026 aprovada (ver Lacunas).
5. **A Mercans já entregou a Lituânia?** Sim, a regulação está em produção: Release Note LT-253649 com deploy em 2025-07-16, entidade de aceite REF-LE-03-418 e QC e G2N de 2025 (CT-3410, CT-3568). Só que ela foi construída com regras de 2025. Indicar cliente de referência é com Implementation.

## Lacunas de Compliance (o que precisa ser feito)

1. **Atualizar a lógica de GPM 2026 no design (WTC, DD, IG):** faixa de 25%, flag de escolha com 3 opções (20, 25, 32) e mecanismo de progressão (acumulado no ano pela regra 9.6 do GPM313 ou alternativa acordada). Hoje está 20%/32% sobre a base inteira.
2. **Corrigir o NPD no CCG 2026 e no IG:** fórmula única 747 − 0,49 × (renda − 1.153), zero acima de €2.677,49 (Alerta 2026), e limitar o NPD à base tributável.
3. **Dar versão e aprovação ao CCG 2026** e emitir a **planilha de parâmetros 2026** (MMA, teto, taxas, NPD, faixas), com fonte e vigência.
4. **Piso MMA no design:** campos no DD para as exceções (≤ 24 anos, outro empregador, aposentado), regra para meses incompletos (admissão e desligamento) e confirmação de quanto do déficit cabe ao empregador.
5. **Teto anual da Sodra:** documentar o mecanismo (aviso S50 ou acumulado), o que acontece no mês do aviso e se o Pillar II também para.
6. **Limite de €350/ano do seguro saúde voluntário (2026):** atualizar o CCG (Non-Taxable Pay) e os WTs 23610, 65630 e 65810.
7. **Specs dos formulários de evento da Sodra:** 1-SD, 2-SD, 9-SD, 12-SD, 13-SD, NP-SD2 e PT, com a versão vigente de cada formulário.
8. **Estrutura de arquivo:** obter a descrição FFData publicada pela Sodra e o esquema de upload EDS vigente da VMI para GPM313 e GPM312. Os MXFD da pasta são anteriores ao VA-105 e ao VA-24.
9. **PSD × residência:** alinhar o IG (corta PSD de não residente fiscal) com o CCG (isenção só para estrangeiro sem autorização de residência).
10. **Ausências e verbas do Código do Trabalho:** % do auxílio-doença pago pelo empregador, licenças parentais, regra de salário médio com fonte legal, direito a férias, adicionais de hora extra, noturno e feriado, e indenização por tempo de casa.
11. **Coordenação UE / A1:** sem nenhuma regra documentada.
12. **Prazos de recolhimento do GPM** (art. 23 GPMI) em função da data de pagamento: falta registrar com fonte.
13. Pequenos ajustes: faixas de incapacidade divergentes (DD, CCG e IG); erro "0%" na tabela do Alerta 2026; isenções de Guarantee Fund e LTEBF sem flag.

## Pontos para a call com o Kevin

- A regulação LT está em produção desde 2025-07-16 (LT-253649), mas o **design ainda é de 2025**. Precisamos que Product confirme o que foi carregado para 2026 (faixa de 25%, NPD, MMA €1.153, teto €138.270).
- O nosso baseline é: CCG 2026, Alerta 2026, WTC e DD V3.0 e as specs SAM, GPM313 e GPM312 v1.0 de 2026-08-21. Não existe parameter sheet aprovada; Compliance vai emitir uma.
- GPM: na folha a retenção é de 20% fixo, e 25%/32% só a pedido do empregado. Precisamos combinar com ele a mecânica da progressão para a Accenture.
- Piso MMA e teto da Sodra: hoje dependem de aviso da Sodra (S50) e de ajustes manuais. Perguntar se Config quer automatizar e quais dados de empregado precisam ser coletados.
- Correções: SAM via PT; GPM313 e GPM312 por declaração completa, e mudança no GPM312 obriga corrigir o GPM313 (regra 65). Retificar o que respondemos em 2026-09-28.
- .ffdata: a Sodra usa FFData com estrutura publicada no site, que ainda não temos. Para a VMI, as specs não confirmam FFData. Perguntar quem é o dono do gerador e se há caminho de teste.
- Formulários de evento (1-SD … PT): pelo contrato o vendor prepara, mas Compliance não tem spec. Definir se são gerados pelo sistema ou digitados, e se ficam com payroll ou HR.
- SAM e GPM313 não fecham por definição (competência × pagamento, base Sodra × base GPM). Combinar as regras de conciliação.
- Banco, GL, relatório de conciliação, provisão de férias e multi-entidade são de Config/Product. Pedir a marcação S/C/M/N dessas linhas.
- Dados que precisamos da Accenture: grupo de risco Sodra da entidade, tipos de contrato, adesão ao Pillar II, consentimentos de NPD, não residentes e A1.

## Conhecimento a absorver (regras LT confirmadas nos documentos)

- Ano fiscal = ano civil; GPM pelo método mensal, sem ajuste anual pelo empregador (CCG 2026).
- **GPM no mês do pagamento; Sodra no mês de competência**, com reenvio do SAM do mês original (CCG 2026).
- GPM 2026: 20% / 25% / 32% com cortes em €82.962 e €138.270 por ano (36 e 60 VDU). Na folha, 20% fixo, e as faixas maiores só a pedido do empregado (CCG 2026; GPM313 spec regras 9.5 e 9.6; VA-105).
- 15% fixo sobre auxílio-doença; pela regra 9.4 do GPM313, também sobre maternidade, paternidade, cuidado infantil e tempo de serviço.
- NPD 2026: €747 até MMA €1.153; 747 − 0,49 × (renda − 1.153); zero acima de €2.677,49. Capacidade reduzida: €1.127 / €1.057 fixos. Só para residentes e só com consentimento escrito (Alerta 2026; CCG 2026).
- Sodra empregado: pensão 8,72% + doença 1,99% + maternidade 1,81% = 12,52%; Pillar II +3%; PSD 6,98% sem teto (CCG 2026).
- Sodra empregador: desemprego 1,31% (prazo indeterminado) / 2,03% (prazo determinado); acidentes 0,14 / 0,43 / 0,70 / 1,40% por grupo; Guarantee Fund 0,16%; LTEBF 0,16% (CCG 2026).
- Teto anual Sodra 2026: €138.270 (era €126.532,80 em 2025), não aplicável ao PSD (Alerta 2026; CCG 2026).
- Piso MMA €1.153 para o empregador, com exceções (≤ 24 anos, mais de um empregador, aposentado); proporcional na licença não remunerada informada no 12-SD (CCG 2026).
- SAM: até o dia 15 do mês seguinte; formulário v07; SAM3SDP com motivos 01–10, sem 99; P3 = taxa no início do mês; A12 = A11 × P3 validado ao centavo; correção via PT; SAM atrasado exige PT motivo 01 (SAM spec).
- GPM313: até o dia 15; campos 6 e 7 divididos pela data de pagamento (até o dia 15 inclusive / depois do dia 15); declaração zerada obrigatória se houve empregado; correção por declaração completa (GPM313 spec).
- GPM312: até 15 de fevereiro; anexos L e U; VA-24 criou o marcador "U"; corrigir o GPM312 obriga corrigir o GPM313 (regra 65) (GPM312 spec).
- Seguro saúde voluntário pago pelo empregador: isento até €350/ano a partir de 2026-01-01 (Alerta 2026).
- Contratual: o vendor prepara SAM, GPM313, GPM312, 1-SD, 2-SD, 9-SD, 12-SD e notificações de doença e de estrangeiro; childbirth e childcare são ad-hoc cobrados (`List of Statutory Filings Lithuania.xlsx`).

## Contagem

| Status | Itens |
|---|---|
| Coberto | 26 |
| Parcial | 22 |
| Lacuna | 10 |
| Fora de Compliance | 6 |
| **Total** | **64** |

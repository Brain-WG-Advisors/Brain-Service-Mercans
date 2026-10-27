# Teste de exatidão

> Arquivo: `testes/exatidao.md`. Roda **no claude.ai**, onde o time trabalha. Ver [[PLANO]] §7 e [prompts/fase-1-linha-de-base.md](../prompts/fase-1-linha-de-base.md).
> **Conjunto A** = 30 perguntas de [[correcoes]] (Fase 1). **Conjunto B** = correções novas da coleta (Fase 3). **Conjunto C** = ~20 perguntas **cegas**, de tickets resolvidos depois da data do MVP, em quarentena (não ingeridos até a medição final).
> Cada pergunta roda **2 vezes** (`T-xxx-r1.md`, `T-xxx-r2.md` em `testes/rodadas/AAAA-MM-DD/`). Duas ✅ = ✅; divergência = ⚠️ instável (não conta como acerto). Um ❌ vira ação com dono; não basta anotar.
> **Este arquivo nunca sobe para o Projeto do claude.ai** (o gabarito vazaria).
> Perguntas prontas para colar: [rodadas/2026-10-27-perguntas.txt](rodadas/2026-10-27-perguntas.txt).

## Critério da seleção (Conjunto A, gerado em 2026-10-27)
- **Base:** `correcoes.md` como estava em 2026-10-27 (linhas 9–135). A "linha" no gabarito é a linha do arquivo nessa data.
- **Fora:** as entradas marcadas "validação humana pendente" (F6 de 2026-10-27, linhas 127–135); entradas com [INCERTO] (linha 23; e o item (g) da linha 21, que não foi usado); entradas sem fonte nível A/B (linhas 34, 43, 47, 60, 64, 65, 109, 20 "spec/BA sem fonte legal") e correções de processo interno que o claude.ai não teria como responder (linhas 93, 112–114, 119).
- **Por país:** pisos/tetos do prompt como guia, ajustados porque `correcoes.md` cresceu: Ucrânia 6, Espanha 6, Colômbia 2 (passou a ter ~10 entradas elegíveis) e 1 de cada um dos demais países com correção elegível (França, Chile, Chade, Irlanda, Holanda, Costa do Marfim, Reino Unido, Hungria, Gabão, Congo, Canadá, Bulgária, Lituânia, Egito, Bélgica, Turquia). Para caber em 30 com os 4 países novos (Lituânia, Egito, Bélgica, Turquia), França, Chile e Chade ficaram com 1 em vez de 2.
- **Por tipo:** V 10 · M 8 · R 8 · P 4 (mínimos do prompt: 8/8/6/4).
- **Erro nosso em resposta de ticket:** 12 (T-001, T-002, T-003, T-006, T-007, T-008, T-009, T-010, T-019, T-021, T-027, T-030).
- **Redação:** em inglês (os casos originais são de ticket/BA em inglês), autocontidas, sem citar a correção nem o ticket, sem nomes de clientes nem dados pessoais.

| País | V | M | R | P | Total |
|---|---|---|---|---|---|
| Espanha | 1 | 4 | 0 | 1 | 6 |
| Ucrânia | 1 | 2 | 2 | 1 | 6 |
| Colômbia | 1 | 0 | 1 | 0 | 2 |
| França | 0 | 0 | 0 | 1 | 1 |
| Chile | 0 | 0 | 1 | 0 | 1 |
| Chade | 1 | 0 | 0 | 0 | 1 |
| Irlanda | 0 | 0 | 1 | 0 | 1 |
| Holanda | 1 | 0 | 0 | 0 | 1 |
| Costa do Marfim | 1 | 0 | 0 | 0 | 1 |
| Reino Unido | 1 | 0 | 0 | 0 | 1 |
| Hungria | 0 | 0 | 1 | 0 | 1 |
| Gabão | 0 | 1 | 0 | 0 | 1 |
| Congo | 1 | 0 | 0 | 0 | 1 |
| Canadá | 0 | 0 | 1 | 0 | 1 |
| Bulgária | 0 | 1 | 0 | 0 | 1 |
| Lituânia | 0 | 0 | 0 | 1 | 1 |
| Egito | 1 | 0 | 0 | 0 | 1 |
| Bélgica | 1 | 0 | 0 | 0 | 1 |
| Turquia | 0 | 0 | 1 | 0 | 1 |
| **Total** | **10** | **8** | **8** | **4** | **30** |

## Perguntas (colar só a coluna Pergunta)
| # | Conj. | País | Tipo (V/M/R/P) | Pergunta |
|---|---|---|---|---|
| T-001 | A | [[Espanha]] | M | Spain, TGSS CRA report (ES-CRA-001, Conceptos Retributivos Abonados): in the month an employee's contract is terminated, which Mercans wage types must be reported in the CRA file for the end-of-contract amounts, and with which CRA concept code and type (I/E)? |
| T-002 | A | [[Espanha]] | M | Spain, TGSS AFI report spec ES-AFI-001 (TrabajadoresTramos): what does the field TRL stand for, and what does it represent? |
| T-003 | A | [[Espanha]] | M | Spain, Modelo 190 (annual withholding summary): which perception key (clave and subclave) should be used for WT 79432 Parental Leave Payout, WT 79429 Breastfeeding Risk Payout and WT 79430 Pregnancy Risk Payout? |
| T-004 | A | [[Espanha]] | M | Spain, SEPE Certific@ (CERTIFICA) XML report: the Data Dictionary stores the employee's occupation as the 4-digit CNO code (table T90), e.g. 3123. How must the field CodProfesion be populated in the XML? |
| T-005 | A | [[Espanha]] | V | Spain 2026, Social Security General Regime: what are the minimum contribution bases for contribution groups 1, 2, 3 and 4–7 (monthly) and for groups 8–11 (daily), effective 1 January 2026, and what is the legal source? |
| T-006 | A | [[Espanha]] | P | Spain WTC: should WT 65815 be mapped to Modelo 296? What is its current classification in the Spain Wage Type Catalogue? |
| T-007 | A | [[Ucrania]] | V | Ukraine 2026: what percentages of average salary are paid as temporary incapacity (sick leave) benefit depending on the employee's insurance record (stazh)? |
| T-008 | A | [[Ucrania]] | R | Ukraine: when calculating the temporary incapacity (sick leave) benefit, what reference period is used to compute the employee's average daily salary? |
| T-009 | A | [[Ucrania]] | R | Ukraine: is an employer-paid life insurance premium for an employee subject to the single social contribution (ESV/USC)? |
| T-010 | A | [[Ucrania]] | M | Ukraine, 4DF (Annex 4 of the Unified Report): for payments to a civil contractor registered as an individual entrepreneur (FOP) who provides the required supporting documents, which 4DF income code and which Mercans wage type apply, and are PIT, Military levy and ESV due? |
| T-011 | A | [[Ucrania]] | M | Ukraine, Unified ESV/PIT Report (J05 package, D1 annex), XML header (DECLARHEAD): how should the fields C_REG, C_RAJ and C_STI_ORIG be populated? |
| T-012 | A | [[Ucrania]] | P | Ukraine: which form code and version of Annex D6 of the Unified Report (J05 package) is in force for 2026 reporting periods, and since when? |
| T-013 | A | [[Colombia]] | R | Colombia 2026, withholding tax (retención en la fuente): are payments for temporary incapacity (common illness from day 3, work-related/ARL incapacity) and maternity/paternity/parental leave exempt income under Estatuto Tributario art. 206, or taxable? |
| T-014 | A | [[Colombia]] | V | Colombia, Nómina Electrónica (DIAN): for an employee who is already a pensioner and keeps working (worker subtype 01), what health (Salud) percentage is deducted from the employee, and is a pension (FondoPension) deduction due? |
| T-015 | A | [[Franca]] | P | France: when payroll software transmits the DPAE (déclaration préalable à l'embauche) electronically, which host receives it and in which file formats can it be sent? |
| T-016 | A | [[Chile]] | R | Chile: in the Mercans regulation design, how should the Impuesto Único de Segunda Categoría (IUSC) and its reliquidation be structured (calculation steps and accumulators)? |
| T-017 | A | [[Chade]] | V | Chad: what is the income tax (IRPP) and CNPS treatment of a transport allowance paid to employees? |
| T-018 | A | [[Irlanda]] | R | Ireland, Mercans payroll engine regulation design: what reg structure should be used to compute progressive income tax (PAYE bands at 20%/40%)? |
| T-019 | A | [[Costa-do-Marfim]] | V | Côte d'Ivoire 2026: what is the monthly CNPS contribution ceiling for the family benefits, maternity and work-injury (AT/MP) branches, and what is the ceiling for the retirement branch? |
| T-020 | A | [[Holanda]] | V | Netherlands 2026: what is the total Whk premium (WGA + ZW-flex) for a small employer in sector 42, according to the Handboek Loonheffingen 2026? |
| T-021 | A | [[Congo]] | V | Republic of Congo: is there an occupancy tax (TOL) that the employer must withhold from employees' salaries? If so, what amount and on what legal basis? |
| T-022 | A | [[Gabao]] | M | Gabon WTC: which Global WTC code ranges must the Gabon Wage Type Catalogue contain for employee deductions and for employer contributions? |
| T-023 | A | [[Reino-Unido]] | V | UK workplace pension auto-enrolment: in the GB Country Data Dictionary, what default employee and employer contribution percentages should be set? |
| T-024 | A | [[Hungria]] | R | Hungary, under-25 PIT exemption in the regulation design: on which date should the employee's age be evaluated (period begin date or end date), and which variable should provide the date of birth? |
| T-025 | A | [[Canada]] | R | Canada payroll and payslip: how should annual maximums (e.g. CPP and EI maximum contributions) be applied in each pay period? |
| T-026 | A | [[Bulgaria]] | M | Bulgaria regulation design: which Mercans wage type code holds the TZPB (Labour Accident and Occupational Disease Fund) contribution rate? |
| T-027 | A | [[Lituania]] | P | Lithuania: when an annual GPM312 declaration has to be corrected after submission, what are the consequences for the monthly GPM313 declarations already filed, and how is the GPM312 correction submitted? |
| T-028 | A | [[Egito]] | V | Egypt: does the Martyrs' Fund contribution (0.05%) apply to private-sector employees' payroll? If so, on what base and who bears it? |
| T-029 | A | [[Belgica]] | V | Belgium 2026: what is the basic employer social security contribution rate (ONSS) for private-sector worker categories 1 and 3, and what is the approximate total rate including the wage moderation contribution? |
| T-030 | A | Turquia | R | Turkey 2025: how is the payroll income tax deduction for an employee's private life insurance premium limited? Which limits apply, and which of them are cumulative over the year? |

## Gabarito (não colar no claude.ai)
| # | Resposta correta | Fonte (nível) | ✅ se... | ⚠️ se... | ❌ se... / erro conhecido | Origem |
|---|---|---|---|---|---|---|
| T-001 | 58184, 58186 e 58188, todos CRA 0054/E. 58197/58198 são WTs só do BASES (prorrata L03); 58198 não entra em nenhum relatório | Spec ES-CRA-001 (B) | Lista 58184, 58186, 58188 com 0054/E e não inclui 58197/58198 | Códigos certos sem o 0054/E, ou com tipo I; ou lista incompleta (2 dos 3) sem código errado | Qualquer outro WT. **Erro conhecido:** CRA reporta 58197 (0054/I) e 58198 (0054/E) no mês do desligamento | [[correcoes]] linha 13 (~2026-05), SR-81 |
| T-002 | TRL = Tipo de Relación Laboral | Schema TGSS AFI (A) | "Tipo de Relación Laboral" (tipo de relação laboral) | Sentido certo com descrição vaga ou sem a expansão da sigla | Qualquer outro significado. **Erro conhecido:** "Work Risk Type", que determina taxa AT/EP (escala 000/500/800) | [[correcoes]] linha 14 (~2026-05), SR-80 |
| T-003 | 79432 = clave L, subclave 27 (prestações públicas de maternidade/paternidade isentas); 79429 e 79430 = clave B, subclave 03 | AEAT Diseños Lógicos 190 / FAQ AEAT (A) | L.27 para 79432 e B.03 para 79429 e 79430 | Dois dos três certos e o terceiro omitido, ou certo sem citar a AEAT | Qualquer outra chave. **Erro conhecido:** 79432 = B/B.01; 79429/79430 = B.01 (B.01 é só pensões/haberes pasivos) | [[correcoes]] linha 16 (2026-08-10), SR-83 |
| T-004 | Completar à direita com zeros até 7 dígitos (3123 → 3123000); o DD continua com 4 dígitos (T90 CNO) | Tabela T90 CNO (seg-social.es) (A) | Padding à direita com zeros até 7 dígitos | Diz que precisa de 7 dígitos sem dizer como completar, ou sem exemplo | Enviar 4 dígitos, zeros à esquerda ou outro comprimento. **Erro conhecido:** CodProfesion com 4 dígitos sem padding (rejeitado) | [[correcoes]] linha 22 (~2026-09-01), HRBS-13757 |
| T-005 | G1 1.989,30 · G2 1.649,70 · G3 1.435,20 · G4–7 1.424,40 €/mês · G8–11 47,48 €/dia, a partir de 2026-01-01 | Orden PJC/297/2026 arts. 2–3 (A) | Os 5 valores exatos e a Orden PJC/297/2026 | Valores certos sem a fonte ou sem a vigência; ou 4 de 5 certos sem valor errado | Qualquer valor diferente. **Erro conhecido:** G1 1.929,00 / G2 1.599,60 / G3 1.391,70 / G4–7 1.424,50 | [[correcoes]] linha 76 (2026-10-08) |
| T-006 | Não: desde a mudança da V3.4 (07/05/2026), 65815 = Flexible Remuneration – Non-Taxable SS Subject, sem mapeamento 296 (WTC V3.5 em diante). Conferir na versão vigente (maior número) antes de afirmar | WTC V3.5 (B) | Diz que não vai ao 296 e dá a classificação "Non-Taxable, SS Subject" (com base na versão mais recente do WTC) | "Não vai ao 296" sem a classificação, ou classificação certa sem dizer de qual versão | Diz que 65815 deve ir ao 296. **Erro conhecido:** contestar a remoção com base em cópia de referência antiga (WTC v3.3 de 30/04) | [[correcoes]] linha 19 (~2026-06), SR-85 |
| T-007 | 50% (< 3 anos) · 60% (3–5) · 70% (5–8) · 100% (> 8 anos) | Lei 1105-XIV art. 17 (A) | As 4 faixas e percentuais exatos | Percentuais certos sem a fonte, ou com limites de faixa imprecisos (ex.: "até 3/3 a 5") sem valor errado | Qualquer outra escala. **Erro conhecido:** 60% (< 5 anos) / 80% (5–8) / 100% (8+) | [[correcoes]] linha 78 (~2026-08), HRBS-13389 |
| T-008 | 12 meses calendário anteriores ao mês do início da incapacidade | Postanova KMU 1266 (A); Lei 1105-XIV art. 19 só para o teto quando o stazh nos 12 meses é < 6 meses | "12 calendar months preceding the month of incapacity" | 12 meses sem dizer "anteriores ao mês da incapacidade", ou com a ressalva do art. 19 descrita de forma confusa | 6 meses ou outro período. **Erro conhecido:** período-base = 6 meses ("Postanova 1266, п. 4") | [[correcoes]] linha 77 (~2026-09-09 → 2026-09-21), HRBS-14331 |
| T-009 | Sim, ESV devido: só seguro médico e seguro de previdência (pensão) estão na lista de isenção; seguro de vida não | Resolution/Poryadok CMU 1170, p. 2, rozd. II (Perelik) (A) | "Yes, subject to ESV" com a razão (vida não está na lista de exclusões da Resolução 1170) | "Sim" sem fonte, ou com fonte errada | "Não" ou "depende" sem chegar a Sim. **Erro conhecido:** USC (ESV) = Não para seguro de vida | [[correcoes]] linha 28 (~2026-09-09), HRBS-14331 / HRBS-12181 |
| T-010 | 4DF 157, WT 62942, PIT/Military/ESV = Não/Não/Não; "Payment to Individual Entrepreneur", fora do fundo de salário | PKU p. 177.8 (A) | 157 + 62942 + Não/Não/Não | 157 e Não/Não/Não sem o WT (ou WT certo sem citar 177.8) | Outro código ou qualquer "Sim". **Erro conhecido:** 157 "não é de empregado, sem WT"; ou Sim/Sim/Sim | [[correcoes]] linhas 79 e 31 (2026-08-03 → 2026-09), HRBS-12181, 14331 |
| T-011 | Não são fixos: código da oblast, do distrito e do órgão da ДПС ao qual cada entidade entrega (diretório SPR_STI.XML; C_STI = C_REG × 100 + C_RAJ). 26/50/2650 é só o órgão de Kyiv do template de teste | наказ Міндоходів № 729/2013, Додаток 1 (DECLARHEAD); SPR_STI.XML de 06.03.2026 (A) | Diz que variam por entidade conforme o órgão da ДПС (SPR_STI) | Diz que variam, sem explicar a origem (SPR_STI / órgão fiscal) | Valores fixos. **Erro conhecido:** "fixed 26 / 50 / 2650" | [[correcoes]] linha 89 (2026-10-13), SR-160/SR-162 |
| T-012 | J0510611 (versão 11), em vigor desde 2026-07-17 | DPS (A) | J0510611 / v11 e a data 2026-07-17 | Código/versão certos sem a data | Outro código. **Erro conhecido:** formulário superado J0510610 (v10) | [[correcoes]] linha 49 (2026-10-01), SR-163 |
| T-013 | Tributáveis, não isentas: o ET 206 nums. 1–2 isenta só indenizações, e incapacidades e licenças não são indenizações; a retenção se aplica | DIAN Oficio 27408 de 01/11/2019, itens 7.1–7.4 (A) | Tributáveis + a razão (206 só indenizações) + Oficio DIAN 27408 | Tributáveis sem a razão ou sem a fonte | Isentas, total ou parcialmente. **Erro conhecido:** "exempt within the statutory minimum (ET art. 206 nums. 1-2 and par. 1)" | [[correcoes]] linha 91 (2026-10-13) |
| T-014 | Salud continua: 4% do empregado sobre o salário; só a pensão é 0 | Decreto 780/2016 art. 2.2.1.1.2.1 e par.; Ley 100 arts. 157, 204 (A) | Salud 4% e pensão 0 | 4% certo com fonte errada ou ausente | Salud 0% ou outro percentual. **Erro conhecido:** Salud e FondoPension com Porcentaje 0,00 e Deduccion 0,00 | [[correcoes]] linha 111 (2026-10-22) |
| T-015 | Host da URSSAF (não "via net-entreprises"); TXT (layout de 120 posições) ou XML | 03-sir.md do pipeline França (B) | URSSAF + TXT 120 e XML | Host certo e só um dos formatos (sem afirmar exclusividade) | Só net-entreprises ou só XML. **Erro conhecido:** DPAE "via net-entreprises", só XML | [[correcoes]] linha 70 (2026-08-28) |
| T-016 | IUSC em 3 passos e 1 step YTM (design v1.1) | CL_Regulation_Design_v1.0; KB_Chile_Design_Decisions (B) | 3 passos + 1 step YTM | Estrutura enxuta parecida (poucos passos + acumulado YTD) sem o número exato | **Erro conhecido:** 8 regs (uma por faixa) e reliquidação com 12 acumuladores (v1.0) | [[correcoes]] linha 62 (2026-06) |
| T-017 | Isento até 30% da base; o excesso é tributável no IRPP e sujeito a CNPS | CGI arts. 3 e 45 (A) | Limite de 30% e excesso tributável e sujeito a CNPS | 30% certo sem dizer que o excesso vai à CNPS, ou sem fonte | Isenção total ou outro limite. **Erro conhecido:** transporte com isenção total (WTC v1.1) | [[correcoes]] linha 58 (2026-07-07) |
| T-018 | Uma reg `Differential`; a decomposição Threshold/Base/Amount era específica do RPN | DevKB (B) | Reg única `Differential` | Reg única por faixas sem nomear `Differential` | **Erro conhecido:** decompor o imposto progressivo em Threshold / Base / Amount | [[correcoes]] linha 67 (2026-07-02) |
| T-019 | 75.000 XOF/mês desde 2023-01-01 (igual ao piso de todos os ramos); aposentadoria 3.375.000 XOF/mês | Communiqué CNPS (jan/2023); Décret 2022-986 de 21/12/2022 (A) | 75.000 e 3.375.000 | 75.000 certo sem o teto da aposentadoria, ou sem vigência/fonte | Qualquer outro valor. **Erro conhecido:** 70.000 XOF/mês; "75.000 é o SMIG (piso), não o teto" | [[correcoes]] linha 96 (2026-10-15), HRBS-14996 |
| T-020 | 1,45% (WGA 0,91% + ZW-flex 0,54%) | Handboek Loonheffingen 2026, Bijlage 1 Tabel 10, pp. 518–519 (A) | 1,45% (com ou sem a decomposição) | Total certo com decomposição errada | Qualquer outro total. **Erro conhecido:** 1,25% (WGA 0,71% + ZW-flex 0,54%, lido na linha de outro setor) | [[correcoes]] linha 103 (2026-10-16) |
| T-021 | Sim: TOL de habitação do assalariado, 1.000 FCFA/mês retidos na fonte pelo empregador, como adiantamento | Loi 34-2013 art. 14, redação da Loi 48-2014 (LF 2015) art. 8 (A) | 1.000 FCFA/mês retidos pelo empregador + a base legal | Sim e 1.000 FCFA sem a base legal | "Não é desconto de folha" ou outro valor. **Erro conhecido:** só a TOL Prof, imposto anual da empresa sobre imóvel comercial | [[correcoes]] linha 90 (2026-09-02), HRBS-14055 |
| T-022 | Bloco Global de deduções 21100–21900 e de contribuições patronais 23640–23673 (59 códigos ao todo) | Global WTC v1.0 (B) | As duas faixas | Uma faixa certa e a outra omitida | Faixas erradas. **Erro conhecido:** WTC sem esses blocos (v3.0) | [[correcoes]] linha 55 (2026-09-23), HRBS-14978 |
| T-023 | EE 5% / ER 3% | GB_Country_Data_Dictionary (B) | EE 5% e ER 3% | Total 8% certo sem a divisão | **Erro conhecido:** EE 3 / ER 5 (invertido) | [[correcoes]] linha 73 (2026-05-27) |
| T-024 | Idade na `end_date`; data de nascimento em `$person.birth_date` (nacionalidade e residência numa flag única `$58218`) | T-2026-05-27/29; KB_Mercans_Knowledgebase_Formulas (B) | end_date e `$person.birth_date` | Um dos dois certo e o outro omitido | begin_date, ou `$employee.years_worked`. **Erro conhecido:** idade no begin_date; `$employee.years_worked` como idade | [[correcoes]] linha 72 (2026-05-27) |
| T-025 | "Lesser-of" por período: a contribuição do período é limitada ao saldo do máximo anual (máximo − acumulado do ano), não ao máximo anual ÷ 12 | CRA (A) | Saldo do máximo anual (lesser-of) por período | Diz que é cumulativo sem descrever o lesser-of | **Erro conhecido:** máximo anual ÷ 12 por período | [[correcoes]] linha 74 (⚠️ data?) |
| T-026 | 52560 | KB_Bulgaria_Design (B) | 52560 | n/a | Qualquer outro código. **Erro conhecido:** 52980 | [[correcoes]] linha 75 (⚠️ data?) |
| T-027 | Os GPM313 mensais afetados também precisam ser corrigidos (uma correção do GPM312 pode gerar até 12 correções de GPM313; regra 65). Correção do GPM312 = declaração completa nova, sem formulário delta (regra 63); a regra 64.2 impede corrigir GPM retido a mais e erros de NPD em renda de residente | LT-VMI-002-GPM312-Spec v1.0, Population Rules, regras 63–66 (B) | Corrigir os GPM313 afetados + GPM312 refeito completo | Só uma das duas partes | **Erro conhecido:** "não há documentação" / GPM313 não é afetado | [[correcoes]] linha 86 (2026-09-28), HRBS-15253 |
| T-028 | Sim: 0,05% do salário mensal total, descontado dos empregados de pessoas jurídicas privadas sob a Lei do Trabalho (exceto irregulares/diaristas), custeado pelo empregado | Lei 4/2021 art. 1 (novo art. 8 da Lei 16/2018), Gazette nº 8 bis (هـ) de 03/03/2021 (A) | Sim + base salário mensal total + custeado pelo empregado | Sim sem a base ou sem quem custeia | **Erro conhecido:** "NOT a private-sector payroll item" (só desembolsos do governo/setor público) | [[correcoes]] linha 115 (2026-10-22) |
| T-029 | 19,88% (categorias 1 e 3, desde o 1º tri/2018, tax shift) + moderação salarial até 5,12% [(19,88 × 0,0427) + 4,27] ≈ 25,00% | Instruções administrativas ONSS, "Le pourcentage de cotisation globalisé" e "La cotisation de modération salariale" (A) | 19,88% e ≈ 25% com moderação | 19,88% sem o total com moderação | Qualquer outra taxa básica. **Erro conhecido:** 24,92% (taxa básica de 2015) | [[correcoes]] linha 110 (2026-10-13 → 2026-10-21) |
| T-030 | Mínimo de: (1) prêmio elegível do mês (50% vida com poupança / 100% só risco); (2) 15% do bruto do mês (teste mensal); (3) saldo do teto anual = salário mínimo bruto anual (312.066 TRY em 2025). Só o teto anual é cumulativo | Folheto GİB 2025 (A) | Os três limites como "o menor de" e só o anual cumulativo | Os três limites certos sem dizer qual é cumulativo, ou sem o valor de 2025 | **Erro conhecido:** os três limites aplicados como cumulativos | [[correcoes]] linha 84 (2025-09-15 → 2025-09-18), CT-3945 |

## Rodadas
| Data | Rodada | Configuração (projeto/skills ativos) | Conj. | ✅ | ⚠️ (instável) | ❌ | Nota | Repetiu erro conhecido |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 (planejada) | 1: linha de base | claude.ai como o time usa hoje, skills Mercans ativas, fora de projeto, sem pacote do brain | A | | | | /30 | |

## Resultado por pergunta
| # | Rodada 1 | Rodada 2 | Causa do ❌/⚠️ (falta no brain / falta na skill / erro do modelo / gabarito) | Ação · dono · data |
|---|---|---|---|---|
| T-001 | | | | |
| T-002 | | | | |
| T-003 | | | | |
| T-004 | | | | |
| T-005 | | | | |
| T-006 | | | | |
| T-007 | | | | |
| T-008 | | | | |
| T-009 | | | | |
| T-010 | | | | |
| T-011 | | | | |
| T-012 | | | | |
| T-013 | | | | |
| T-014 | | | | |
| T-015 | | | | |
| T-016 | | | | |
| T-017 | | | | |
| T-018 | | | | |
| T-019 | | | | |
| T-020 | | | | |
| T-021 | | | | |
| T-022 | | | | |
| T-023 | | | | |
| T-024 | | | | |
| T-025 | | | | |
| T-026 | | | | |
| T-027 | | | | |
| T-028 | | | | |
| T-029 | | | | |
| T-030 | | | | |

## Quarentena do Conjunto C (data de corte = data do MVP: AAAA-MM-DD)
| # | Ticket | Resolvido em | País | Pergunta derivada | Ingerir depois de |
|---|---|---|---|---|---|
| C-001 | | | | | medição final |

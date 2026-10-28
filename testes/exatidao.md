# Teste de exatidão

> Arquivo: `testes/exatidao.md`. Roda **no claude.ai**, onde o time trabalha. Ver [[PLANO]] §7 e [prompts/fase-1-linha-de-base.md](../prompts/fase-1-linha-de-base.md).
> **Conjunto A** = 30 perguntas de [[correcoes]] (Fase 1). **Conjunto B** = correções novas da coleta (Fase 3). **Conjunto C** = ~20 perguntas **cegas**, de tickets resolvidos depois da data do MVP, em quarentena (não ingeridos até a medição final).
> Cada pergunta roda **2 vezes** (`T-xxx-r1.md`, `T-xxx-r2.md` em `testes/rodadas/AAAA-MM-DD/`). Duas ✅ = ✅; divergência = ⚠️ instável (não conta como acerto). Um ❌ vira ação com dono; não basta anotar.
> **Este arquivo nunca sobe para o Projeto do claude.ai** (o gabarito vazaria).
> Eficiência (idas e vindas por semana): [[testes/eficiencia]].
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
| T-001 | 58184, 58186 e 58188, todos CRA 0054/E. 58197/58198 são WTs só do BASES (prorrata L03); 58198 não entra em nenhum relatório | Spec ES-CRA-001 (B) | Lista 58184, 58186, 58188 com 0054/E e não inclui 58197/58198 | Códigos certos sem o 0054/E, ou com tipo I; ou lista incompleta (2 dos 3) sem código errado | Qualquer outro WT. **Erro conhecido:** CRA reporta 58197 (0054/I) e 58198 (0054/E) no mês do desligamento | [[correcoes]] linha 13 (~2026-05), SR-81 · **[REVISADO 2026-10-27: ver "Revisão do gabarito"]** |
| T-002 | TRL = Tipo de Relación Laboral | Schema TGSS AFI (A) | "Tipo de Relación Laboral" (tipo de relação laboral) | Sentido certo com descrição vaga ou sem a expansão da sigla | Qualquer outro significado. **Erro conhecido:** "Work Risk Type", que determina taxa AT/EP (escala 000/500/800) | [[correcoes]] linha 14 (~2026-05), SR-80 |
| T-003 | 79432 = clave L, subclave 27 (prestações públicas de maternidade/paternidade isentas); 79429 e 79430 = clave B, subclave 03 | AEAT Diseños Lógicos 190 / FAQ AEAT (A) | L.27 para 79432 e B.03 para 79429 e 79430 | Dois dos três certos e o terceiro omitido, ou certo sem citar a AEAT | Qualquer outra chave. **Erro conhecido:** 79432 = B/B.01; 79429/79430 = B.01 (B.01 é só pensões/haberes pasivos) | [[correcoes]] linha 16 (2026-08-10), SR-83 · **[REVISADO 2026-10-27: ver "Revisão do gabarito"]** |
| T-004 | Completar à direita com zeros até 7 dígitos (3123 → 3123000); o DD continua com 4 dígitos (T90 CNO) | Tabela T90 CNO (seg-social.es) (A) | Padding à direita com zeros até 7 dígitos | Diz que precisa de 7 dígitos sem dizer como completar, ou sem exemplo | Enviar 4 dígitos, zeros à esquerda ou outro comprimento. **Erro conhecido:** CodProfesion com 4 dígitos sem padding (rejeitado) | [[correcoes]] linha 22 (~2026-09-01), HRBS-13757 |
| T-005 | G1 1.989,30 · G2 1.649,70 · G3 1.435,20 · G4–7 1.424,40 €/mês · G8–11 47,48 €/dia, a partir de 2026-01-01 | Orden PJC/297/2026 arts. 2–3 (A) | Os 5 valores exatos e a Orden PJC/297/2026 | Valores certos sem a fonte ou sem a vigência; ou 4 de 5 certos sem valor errado | Qualquer valor diferente. **Erro conhecido:** G1 1.929,00 / G2 1.599,60 / G3 1.391,70 / G4–7 1.424,50 | [[correcoes]] linha 76 (2026-10-08) |
| T-006 | Não: desde a mudança da V3.4 (07/05/2026), 65815 = Flexible Remuneration – Non-Taxable SS Subject, sem mapeamento 296 (WTC V3.5 em diante). Conferir na versão vigente (maior número) antes de afirmar | WTC V3.5 (B) | Diz que não vai ao 296 e dá a classificação "Non-Taxable, SS Subject" (com base na versão mais recente do WTC) | "Não vai ao 296" sem a classificação, ou classificação certa sem dizer de qual versão | Diz que 65815 deve ir ao 296. **Erro conhecido:** contestar a remoção com base em cópia de referência antiga (WTC v3.3 de 30/04) | [[correcoes]] linha 19 (~2026-06), SR-85 |
| T-007 | 50% (< 3 anos) · 60% (3–5) · 70% (5–8) · 100% (> 8 anos) | Lei 1105-XIV art. 17 (A) | As 4 faixas e percentuais exatos | Percentuais certos sem a fonte, ou com limites de faixa imprecisos (ex.: "até 3/3 a 5") sem valor errado | Qualquer outra escala. **Erro conhecido:** 60% (< 5 anos) / 80% (5–8) / 100% (8+) | [[correcoes]] linha 78 (~2026-08), HRBS-13389 |
| T-008 | 12 meses calendário anteriores ao mês do início da incapacidade | Postanova KMU 1266 (A); Lei 1105-XIV art. 19 só para o teto quando o stazh nos 12 meses é < 6 meses | "12 calendar months preceding the month of incapacity" | 12 meses sem dizer "anteriores ao mês da incapacidade", ou com a ressalva do art. 19 descrita de forma confusa | 6 meses ou outro período. **Erro conhecido:** período-base = 6 meses ("Postanova 1266, п. 4") | [[correcoes]] linha 77 (~2026-09-09 → 2026-09-21), HRBS-14331 |
| T-009 | Sim, ESV devido: só seguro médico e seguro de previdência (pensão) estão na lista de isenção; seguro de vida não | Resolution/Poryadok CMU 1170, p. 2, rozd. II (Perelik) (A) | "Yes, subject to ESV" com a razão (vida não está na lista de exclusões da Resolução 1170) | "Sim" sem fonte, ou com fonte errada | "Não" ou "depende" sem chegar a Sim. **Erro conhecido:** USC (ESV) = Não para seguro de vida | [[correcoes]] linha 28 (~2026-09-09), HRBS-14331 / HRBS-12181 |
| T-010 | 4DF 157, WT 62942, PIT/Military/ESV = Não/Não/Não; "Payment to Individual Entrepreneur", fora do fundo de salário | PKU p. 177.8 (A) | 157 + 62942 + Não/Não/Não | 157 e Não/Não/Não sem o WT (ou WT certo sem citar 177.8) | Outro código ou qualquer "Sim". **Erro conhecido:** 157 "não é de empregado, sem WT"; ou Sim/Sim/Sim | [[correcoes]] linhas 79 e 31 (2026-08-03 → 2026-09), HRBS-12181, 14331 |
| T-011 | Não são fixos: código da oblast, do distrito e do órgão da ДПС ao qual cada entidade entrega (diretório SPR_STI.XML; C_STI = C_REG × 100 + C_RAJ). 26/50/2650 é só o órgão de Kyiv do template de teste | наказ Міндоходів № 729/2013, Додаток 1 (DECLARHEAD); SPR_STI.XML de 06.03.2026 (A) | Diz que variam por entidade conforme o órgão da ДПС (SPR_STI) | Diz que variam, sem explicar a origem (SPR_STI / órgão fiscal) | Valores fixos. **Erro conhecido:** "fixed 26 / 50 / 2650" | [[correcoes]] linha 89 (2026-10-13), SR-160/SR-162 |
| T-012 | J0510611 (versão 11), em vigor desde 2026-07-17 | DPS (A) | J0510611 / v11 e a data 2026-07-17 | Código/versão certos sem a data | Outro código. **Erro conhecido:** formulário superado J0510610 (v10) | [[correcoes]] linha 49 (2026-10-01), SR-163 |
| T-013 | Tributáveis, não isentas: o ET 206 nums. 1–2 isenta só indenizações, e incapacidades e licenças não são indenizações; a retenção se aplica | DIAN Oficio 27408 de 01/11/2019, itens 7.1–7.4 (A) | Tributáveis + a razão (206 só indenizações) + Oficio DIAN 27408 | Tributáveis sem a razão ou sem a fonte | Isentas, total ou parcialmente. **Erro conhecido:** "exempt within the statutory minimum (ET art. 206 nums. 1-2 and par. 1)"; ARL isenta pelo Oficio DIAN 036846/2015 (29/12/2015), doutrina anterior que o 27408/2019 (item 7.1, "accidentes de trabajo") supera | [[correcoes]] linha 94 (2026-10-13) · **[CONFERIDO 2026-10-27: gabarito mantido; conflito 036846/2015 registrado]** |
| T-014 | Salud continua: 4% do empregado sobre o salário; só a pensão é 0 | Decreto 780/2016 art. 2.2.1.1.2.1 e par.; Ley 100 arts. 157, 204 (A) | Salud 4% e pensão 0 | 4% certo com fonte errada ou ausente | Salud 0% ou outro percentual. **Erro conhecido:** Salud e FondoPension com Porcentaje 0,00 e Deduccion 0,00 | [[correcoes]] linha 111 (2026-10-22) |
| T-015 | Host da URSSAF (não "via net-entreprises"); TXT (layout de 120 posições) ou XML | 03-sir.md do pipeline França (B) | URSSAF + TXT 120 e XML | Host certo e só um dos formatos (sem afirmar exclusividade) | Só net-entreprises ou só XML. **Erro conhecido:** DPAE "via net-entreprises", só XML | [[correcoes]] linha 70 (2026-08-28) |
| T-016 | IUSC em 3 passos e 1 step YTM (design v1.1) | CL_Regulation_Design_v1.0; KB_Chile_Design_Decisions (B) | 3 passos + 1 step YTM | Estrutura enxuta parecida (poucos passos + acumulado YTD) sem o número exato | **Erro conhecido:** 8 regs (uma por faixa) e reliquidação com 12 acumuladores (v1.0) | [[correcoes]] linha 62 (2026-06) |
| T-017 | Isento até 30% da base; o excesso é tributável no IRPP e sujeito a CNPS | CGI arts. 3 e 45 (A) | Limite de 30% e excesso tributável e sujeito a CNPS | 30% certo sem dizer que o excesso vai à CNPS, ou sem fonte | Isenção total ou outro limite. **Erro conhecido:** transporte com isenção total (WTC v1.1) | [[correcoes]] linha 58 (2026-07-07) |
| T-018 | Irlanda: decomposição Threshold / Base / Amount (triplet), com taxas e cut-off vindos da Revenue via RPN (padrão IE de produção). A regra geral, para país sem RPN, é uma reg `Differential` com faixas | chat design-dev-kb, 06-24 e 07-02, Mohit (B); DevKB oficial não conferido | Triplet via RPN para a Irlanda | Triplet sem ligar ao RPN, ou a regra geral `Differential` dizendo que a Irlanda (RPN) é a exceção | `Differential` única para a Irlanda. **Erro conhecido (revisto):** aplicar o triplet como regra geral a país sem RPN | [[correcoes]] linha 67 (2026-07-02) · **[REVISADO 2026-10-27: o gabarito antigo era "uma reg Differential"]** |
| T-019 | 75.000 XOF/mês desde 2023-01-01 (igual ao piso de todos os ramos); aposentadoria 3.375.000 XOF/mês | Communiqué CNPS (jan/2023); Décret 2022-986 de 21/12/2022 (A) | 75.000 e 3.375.000 | 75.000 certo sem o teto da aposentadoria, ou sem vigência/fonte | Qualquer outro valor. **Erro conhecido:** 70.000 XOF/mês; "75.000 é o SMIG (piso), não o teto" | [[correcoes]] linha 96 (2026-10-15), HRBS-14996 |
| T-020 | 1,45% (WGA 0,91% + ZW-flex 0,54%) | Handboek Loonheffingen 2026, Bijlage 1 Tabel 10, pp. 518–519 (A) | 1,45% (com ou sem a decomposição) | Total certo com decomposição errada | Qualquer outro total. **Erro conhecido:** 1,25% (WGA 0,71% + ZW-flex 0,54%, lido na linha de outro setor) | [[correcoes]] linha 103 (2026-10-16) |
| T-021 | Sim: TOL de habitação do assalariado, 1.000 FCFA/mês retidos na fonte pelo empregador, como adiantamento | Loi 34-2013 art. 14, redação da Loi 48-2014 (LF 2015) art. 8 (A) | 1.000 FCFA/mês retidos pelo empregador + a base legal | Sim e 1.000 FCFA sem a base legal | "Não é desconto de folha" ou outro valor. **Erro conhecido:** só a TOL Prof, imposto anual da empresa sobre imóvel comercial | [[correcoes]] linha 90 (2026-09-02), HRBS-14055 |
| T-022 | Bloco Global de deduções 21100–21900 e de contribuições patronais 23640–23673 (59 códigos ao todo) | Global WTC v1.0 (B) | As duas faixas | Uma faixa certa e a outra omitida | Faixas erradas. **Erro conhecido:** WTC sem esses blocos (v3.0) | [[correcoes]] linha 55 (2026-09-23), HRBS-14978 |
| T-023 | EE 5% / ER 3% | GB_Country_Data_Dictionary (B) | EE 5% e ER 3% | Total 8% certo sem a divisão | **Erro conhecido:** EE 3 / ER 5 (invertido) | [[correcoes]] linha 73 (2026-05-27) |
| T-024 | Idade na `end_date`; data de nascimento em `$person.birth_date` (nacionalidade e residência numa flag única `$58218`) | T-2026-05-27/29; KB_Mercans_Knowledgebase_Formulas (B) | end_date e `$person.birth_date` | Um dos dois certo e o outro omitido | begin_date, ou `$employee.years_worked`. **Erro conhecido:** idade no begin_date; `$employee.years_worked` como idade | [[correcoes]] linha 72 (2026-05-27) · **[REVISADO 2026-10-27: ver "Revisão do gabarito"]** |
| T-025 | "Lesser-of" por período: a contribuição do período é limitada ao saldo do máximo anual (máximo − acumulado do ano), não ao máximo anual ÷ 12 | CRA (A) | Saldo do máximo anual (lesser-of) por período | Diz que é cumulativo sem descrever o lesser-of | **Erro conhecido:** máximo anual ÷ 12 por período | [[correcoes]] linha 74 (⚠️ data?) |
| T-026 | 52560 | KB_Bulgaria_Design (B) | 52560 | n/a | Qualquer outro código. **Erro conhecido:** 52980 | [[correcoes]] linha 75 (⚠️ data?) |
| T-027 | Os GPM313 mensais afetados também precisam ser corrigidos (uma correção do GPM312 pode gerar até 12 correções de GPM313; regra 65). Correção do GPM312 = declaração completa nova, sem formulário delta (regra 63); a regra 64.2 impede corrigir GPM retido a mais e erros de NPD em renda de residente | LT-VMI-002-GPM312-Spec v1.0, Population Rules, regras 63–66 (B) | Corrigir os GPM313 afetados + GPM312 refeito completo | Só uma das duas partes | **Erro conhecido:** "não há documentação" / GPM313 não é afetado | [[correcoes]] linha 86 (2026-09-28), HRBS-15253 |
| T-028 | Sim: 0,05%, descontado dos empregados de pessoas jurídicas privadas sob a Lei do Trabalho (exceto irregulares/diaristas), custeado pelo empregado. Base: salário mensal total pela Circular MoF 14/2021; o sistema da ETA calcula só sobre as verbas básicas (FAQ v4 Q110): seguir o ETA e informar a divergência | Lei 4/2021 art. 1 (novo art. 8 da Lei 16/2018), Gazette nº 8 bis (هـ) de 03/03/2021 (A); FAQ ETA v4 Q110, citada na skill `payroll-compliance-egypt` v2 `01-ccg.md` §8.2 (B, PDF não localizado) | Sim + empregado + base com a divergência (total pela circular × básico no sistema ETA) | Sim + empregado + uma base só, sem a divergência | **Erro conhecido:** "NOT a private-sector payroll item" (só desembolsos do governo/setor público) | [[correcoes]] linha 118 (2026-10-22) · **[REVISADO 2026-10-27: o gabarito antigo exigia só "salário mensal total"]** |
| T-029 | 19,88% (categorias 1 e 3, desde o 1º tri/2018, tax shift) + moderação salarial até 5,12% [(19,88 × 0,0427) + 4,27] ≈ 25,00% | Instruções administrativas ONSS, "Le pourcentage de cotisation globalisé" e "La cotisation de modération salariale" (A) | 19,88% e ≈ 25% com moderação | 19,88% sem o total com moderação | Qualquer outra taxa básica. **Erro conhecido:** 24,92% (taxa básica de 2015) | [[correcoes]] linha 110 (2026-10-13 → 2026-10-21) |
| T-030 | Mínimo de: (1) prêmio elegível do mês (50% vida com poupança / 100% só risco); (2) 15% do bruto do mês (teste mensal); (3) saldo do teto anual = salário mínimo bruto anual (312.066 TRY em 2025). Só o teto anual é cumulativo | Folheto GİB 2025 (A) | Os três limites como "o menor de" e só o anual cumulativo | Os três limites certos sem dizer qual é cumulativo, ou sem o valor de 2025 | **Erro conhecido:** os três limites aplicados como cumulativos | [[correcoes]] linha 84 (2025-09-15 → 2025-09-18), CT-3945 |

## Rodadas
| Data | Rodada | Configuração (projeto/skills ativos) | Conj. | ✅ | ⚠️ (instável) | ❌ | Nota | Repetiu erro conhecido |
|---|---|---|---|---|---|---|---|---|
| 2026-10-27 | 1: linha de base | claude.ai fora de projeto, conectores desligados no chat, skills Mercans + busca web + memória + pesquisa em conversas anteriores ativas | A | 20 | 5 (1 instável: T-003) | 5 | **20/30** (→ 19/28 depois das anulações e da revisão de 27/10: T-028 instável) | 3 perguntas (T-001, T-003, T-024; 4 respostas) + 1 parcial (T-017, só CNPS) |
| 2026-10-27 | 2: Claude Code + cérebro (livro aberto) | Claude Code (Opus 5.5), 1 resposta por pergunta, 3 agentes; `contexto_pais.py` + hub + correcoes + arquivos locais/Drive; sem web (1 consulta secundária na T-010); skills de país não carregadas; gabarito bloqueado | A | 28 | 0 | 0 | **28/28** (T-001 e T-003 anuladas como na rodada 1; as duas respostas seguem a revisão do gabarito) → **26/28** depois da revisão de 27/10 (T-018 ❌, T-028 ⚠️) | T-018 (gabarito revisto) |
| 2026-10-27 | 3: claude.ai + skill brain-service | claude.ai org Mercans, Opus 5.5 Alto, 1 passada; skill brain-service v2 (pessoal) + skills Mercans; pesquisa de conectores desligada; memória e pesquisa em conversas anteriores ativas | A | 24 | 2 (T-016, T-028) | 2 (T-013, T-018) | **24/28** (T-001/T-003 anuladas) → **26/28** depois da revisão do gabarito (T-018 e T-028 ✅) | T-013 em parte (ARL) |

- T-001 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-001-r1|r1]] · [[testes/rodadas/2026-10-27/T-001-r2|r2]]
- T-002 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-002-r1|r1]] · [[testes/rodadas/2026-10-27/T-002-r2|r2]]
- T-003 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-003-r1|r1]] · [[testes/rodadas/2026-10-27/T-003-r2|r2]]
- T-004 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-004-r1|r1]] · [[testes/rodadas/2026-10-27/T-004-r2|r2]]
- T-005 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-005-r1|r1]] · [[testes/rodadas/2026-10-27/T-005-r2|r2]]
- T-006 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-006-r1|r1]] · [[testes/rodadas/2026-10-27/T-006-r2|r2]]
- T-007 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-007-r1|r1]] · [[testes/rodadas/2026-10-27/T-007-r2|r2]]
- T-008 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-008-r1|r1]] · [[testes/rodadas/2026-10-27/T-008-r2|r2]]
- T-009 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-009-r1|r1]] · [[testes/rodadas/2026-10-27/T-009-r2|r2]]
- T-010 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-010-r1|r1]] · [[testes/rodadas/2026-10-27/T-010-r2|r2]]
- T-011 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-011-r1|r1]] · [[testes/rodadas/2026-10-27/T-011-r2|r2]]
- T-012 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-012-r1|r1]] · [[testes/rodadas/2026-10-27/T-012-r2|r2]]
- T-013 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-013-r1|r1]] · [[testes/rodadas/2026-10-27/T-013-r2|r2]]
- T-014 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-014-r1|r1]] · [[testes/rodadas/2026-10-27/T-014-r2|r2]]
- T-015 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-015-r1|r1]] · [[testes/rodadas/2026-10-27/T-015-r2|r2]]
- T-016 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-016-r1|r1]] · [[testes/rodadas/2026-10-27/T-016-r2|r2]]
- T-017 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-017-r1|r1]] · [[testes/rodadas/2026-10-27/T-017-r2|r2]]
- T-018 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-018-r1|r1]] · [[testes/rodadas/2026-10-27/T-018-r2|r2]]
- T-019 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-019-r1|r1]] · [[testes/rodadas/2026-10-27/T-019-r2|r2]]
- T-020 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-020-r1|r1]] · [[testes/rodadas/2026-10-27/T-020-r2|r2]]
- T-021 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-021-r1|r1]] · [[testes/rodadas/2026-10-27/T-021-r2|r2]]
- T-022 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-022-r1|r1]] · [[testes/rodadas/2026-10-27/T-022-r2|r2]]
- T-023 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-023-r1|r1]] · [[testes/rodadas/2026-10-27/T-023-r2|r2]]
- T-024 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-024-r1|r1]] · [[testes/rodadas/2026-10-27/T-024-r2|r2]]
- T-025 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-025-r1|r1]] · [[testes/rodadas/2026-10-27/T-025-r2|r2]]
- T-026 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-026-r1|r1]] · [[testes/rodadas/2026-10-27/T-026-r2|r2]]
- T-027 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-027-r1|r1]] · [[testes/rodadas/2026-10-27/T-027-r2|r2]]
- T-028 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-028-r1|r1]] · [[testes/rodadas/2026-10-27/T-028-r2|r2]]
- T-029 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-029-r1|r1]] · [[testes/rodadas/2026-10-27/T-029-r2|r2]]
- T-030 (rodada 1, 2026-10-27): [[testes/rodadas/2026-10-27/T-030-r1|r1]] · [[testes/rodadas/2026-10-27/T-030-r2|r2]]

## Resultado por pergunta
| # | Rodada 1 | Rodada 2 | Causa do ❌/⚠️ (falta no brain / falta na skill / erro do modelo / gabarito) | Ação · dono · data |
|---|---|---|---|---|
| T-001 | ❌ | ❌ | Resultado ❌. falta no brain/skill (erro conhecido reproduzido nas 2; as duas citam o Manual CRA de 01/07/2026, ver Gabarito a revisar) | Levar a correção SR-81 à skill do ES; revisar gabarito · usuário |
| T-002 | ✅ | ✅ |  |  |
| T-003 | ❌ | ✅ | Resultado ⚠️. instável (r1 reproduz o erro conhecido; r1 cita Orden HAC/1431/2025, ver Gabarito a revisar) | Corrigir na skill ES; revisar gabarito · usuário |
| T-004 | ✅ | ✅ |  |  |
| T-005 | ✅ | ✅ |  |  |
| T-006 | ❌ | ❌ | Resultado ❌. falta no brain (WTC fora do alcance do claude.ai sem Drive; critério não prevê "não sabe", ver Gabarito a revisar) | Pacote do brain com a linha 65815 / WTC vigente · usuário |
| T-007 | ✅ | ✅ |  |  |
| T-008 | ✅ | ✅ |  |  |
| T-009 | ✅ | ✅ |  |  |
| T-010 | ⚠️ | ⚠️ | Resultado ⚠️. falta no brain/skill (WT 62942 interno; as duas dizem que não sabem) | Pacote do brain com o WT 62942 · usuário |
| T-011 | ✅ | ✅ |  |  |
| T-012 | ✅ | ✅ |  |  |
| T-013 | ✅ | ✅ |  |  |
| T-014 | ✅ | ✅ |  |  |
| T-015 | ✅ | ✅ |  |  |
| T-016 | ⚠️ | ⚠️ | Resultado ⚠️. falta no brain (design v1.1 interno; respondem pela lei, não pelo design) | Pacote do brain com CL_Regulation_Design · usuário |
| T-017 | ⚠️ | ⚠️ | Resultado ⚠️. falta no brain/skill (excesso na CNPS afirmado ao contrário; ver Gabarito a revisar) | Incluir CGI 45-13 + base CNPS na skill do Chade · usuário |
| T-018 | ⚠️ | ⚠️ | Resultado ⚠️. falta no brain (DevKB interno) | Pacote do brain com a regra DevKB do Differential · usuário |
| T-019 | ✅ | ✅ |  |  |
| T-020 | ✅ | ✅ |  |  |
| T-021 | ✅ | ✅ |  |  |
| T-022 | ❌ | ❌ | Resultado ❌. falta no brain (Global WTC é interno; critério não prevê "não sabe") | Pacote do brain com o Global WTC v1.0 · usuário |
| T-023 | ✅ | ✅ |  |  |
| T-024 | ❌ | ❌ | Resultado ❌. gabarito/falta no brain (respondem pela lei 29/F § (3); sem a variável do DD; ver Gabarito a revisar) | Decidir o gabarito antes de agir · usuário |
| T-025 | ✅ | ✅ |  |  |
| T-026 | ❌ | ❌ | Resultado ❌. falta no brain (KB_Bulgaria_Design interno; critério não prevê "não sabe") | Pacote do brain com o código 52560 · usuário |
| T-027 | ✅ | ✅ |  |  |
| T-028 | ✅ | ✅ |  |  |
| T-029 | ✅ | ✅ |  |  |
| T-030 | ✅ | ✅ |  |  |


### Correção detalhada, rodada 1 (2026-10-27)

Critério escrito do gabarito, sem reinterpretar. Resposta sem o dado pedido ("não tenho o arquivo") não está em nenhuma coluna do critério: contada como ❌ (ver Gabarito a revisar). Regra do resultado: ✅✅ → ✅; r1 ≠ r2 → ⚠️ instável (não acerto); ❌❌ → ❌; ⚠️⚠️ → ⚠️.

| # | Resp. | Nota | Justificativa (trecho da resposta) | Repetiu o erro conhecido? |
|---|---|---|---|---|
| T-001 | r1 | ❌ | lista 58198 → "0054/E" e 58197 → "0054/I" e diz que 58184/86/88 "would double count" | sim |
| T-001 | r2 | ❌ | "58197/58198 are the correct CRA lines"; diz que 58188 não pode ser E | sim |
| T-002 | r1 | ✅ | "TRL = Tipo de Relación Laboral" (nó InformacionAfiliacion, 3 dígitos) | não |
| T-002 | r2 | ✅ | "TRL = Tipo de Relación Laboral" (tabela T-52) | não |
| T-003 | r1 | ❌ | 79429/79430 → "Clave B, subclave 01" (79432 = L.27 certo) | sim |
| T-003 | r2 | ✅ | 79432 = L.27; 79430 e 79429 = "Clave B, Subclave 03", fonte AEAT FAQ | não |
| T-004 | r1 | ✅ | "3123 → 3123000" | não |
| T-004 | r2 | ✅ | "<CodProfesion>3123000</CodProfesion>"; "Do not left-pad" | não |
| T-005 | r1 | ✅ | 5 valores exatos (1.989,30 … 47,48) + Orden PJC/297/2026 art. 3 | não |
| T-005 | r2 | ✅ | 5 valores exatos + Orden PJC/297/2026, desde 01/01/2026 | não |
| T-006 | r1 | ❌ | "I can't answer either part yet: the Spain WTC isn't attached" | não |
| T-006 | r2 | ❌ | "I can't answer either part yet because the Spain WTC isn't in this chat" | não |
| T-007 | r1 | ✅ | tabela 50% / 60% / 70% / 100%, Lei 1105-XIV art. 17 | não |
| T-007 | r2 | ✅ | mesma tabela, art. 17(1) | não |
| T-008 | r1 | ✅ | "12 calendar months … preceding the month in which the incapacity began", Postanova 1266 p. 25 | não |
| T-008 | r2 | ✅ | "12 calendar months … that precede the month in which the insured event occurs", p. 25 | não |
| T-009 | r1 | ✅ | "Yes, it's subject to ESV"; Res. 1170 sec. II p. 2 "Life insurance is not on that list" | não |
| T-009 | r2 | ✅ | "subject to ESV"; Res. 1170 "Life insurance is not on the List" | não |
| T-010 | r1 | ⚠️ | "code 157", PIT/militar/ESV não devidos (art. 177.8), mas "I can't confirm the wage type" | não |
| T-010 | r2 | ⚠️ | "157", PIT/ML/ESV "not withheld/due", mas "I can't confirm the element number" | não |
| T-011 | r1 | ✅ | "come from the DPS directory of territorial bodies (SPR_STI.XML)"; C_STI_ORIG = C_REG*100+C_RAJ | não |
| T-011 | r2 | ✅ | "taken from the DPS tax-office directory (SPR_STI.XML)"; varia pelo órgão de registro | não |
| T-012 | r1 | ✅ | "J0510611 (version 11)"; "entered into force on 17 July 2026" | não |
| T-012 | r2 | ✅ | "J0510611 (version 11)"; "entered into force on 17.07.2026" | não |
| T-013 | r1 | ✅ | "all of them are taxable"; Oficio 027408/2019 itens 7.1–7.4; art. 206 só indenizações | não |
| T-013 | r2 | ✅ | "Taxable"; Oficio 027408/2019 itens 7.1–7.4 | não |
| T-014 | r1 | ✅ | "Salud: 4%"; "FondoPension: not due" | não |
| T-014 | r2 | ✅ | "Salud: 4% deducted from the employee"; "FondoPension: no deduction due" | não |
| T-015 | r1 | ✅ | host "depot.dpae-edi.urssaf.fr"; "DPAE XML and flat-file … format 120" | não |
| T-015 | r2 | ✅ | host "depot.dpae-edi.urssaf.fr"; "Both formats are accepted" | não |
| T-016 | r1 | ⚠️ | 3 blocos (A mensal, B Art. 46, C reporte) e acumuladores por mês de competência; sem "1 step YTM" nem "3 passos" do design; admite não ter a skill | não |
| T-016 | r2 | ⚠️ | passos A/B/C e ~9 acumuladores por mês; "proposed design, not the current artifact" | não |
| T-017 | r1 | ⚠️ | "up to 30% of each employee's monthly base salary"; mas CNPS "no percentage cap applies" | sim (parcial, só CNPS) |
| T-017 | r2 | ⚠️ | "capped at 30%"; CNPS "Excluded from the contribution base, with no cap" | sim (parcial, só CNPS) |
| T-018 | r1 | ⚠️ | "Don't model … as a fixed progressive bracket table … two-rate formula"; não nomeia `Differential` | não |
| T-018 | r2 | ⚠️ | "two-band calculation … cumulative"; não nomeia `Differential` | não |
| T-019 | r1 | ✅ | "75,000 FCFA/month. Retirement: 3,375,000 FCFA/month"; communiqué CNPS jan/2023 | não |
| T-019 | r2 | ✅ | "75,000 FCFA per month … 3,375,000"; communiqué CNPS | não |
| T-020 | r1 | ✅ | "1.45%, made up of WGA 0.91% and ZW-flex 0.54%" | não |
| T-020 | r2 | ✅ | "1.45% … 0.91% … 0.54%" | não |
| T-021 | r1 | ✅ | "Yes … 1,000 FCFA per month"; Loi 34-2013 art. 14 / Loi 48-2014 art. 8 | não |
| T-021 | r2 | ✅ | "Yes … XAF 1,000 per employee per month"; Art. 14 Loi 34-2013 reescrito pela Loi 48-2014 | não |
| T-022 | r1 | ❌ | "I can't give you those ranges reliably … don't have the baseline file" | não |
| T-022 | r2 | ❌ | "I can't give you those ranges with confidence" | não |
| T-023 | r1 | ✅ | "Employer … 3% … Employee … 5%" | não |
| T-023 | r2 | ✅ | "Employer 3%, Employee 5%, Total 8%" | não |
| T-024 | r1 | ❌ | "Neither date as a simple age test … YYYYMM(DOB + 25 years) ≥ YYYYMM(payroll period)"; diz que "Period end date is wrong" | não |
| T-024 | r2 | ❌ | "Eligible if 25th birthday ≥ period begin date" (usa begin); "Period end date" errado; sem $person.birth_date | sim (begin_date) |
| T-025 | r1 | ✅ | "you deduct only the remaining balance … After that, the deduction is zero" | não |
| T-025 | r2 | ✅ | "When YTD reaches the annual maximum, the final period takes only the remaining balance" | não |
| T-026 | r1 | ❌ | "I can't confirm the code"; sugere 2566 sem afirmar | não |
| T-026 | r2 | ❌ | "I can't pin the TZPB code" | não |
| T-027 | r1 | ✅ | GPM313 "must also be corrected"; GPM312 "newly completed declaration … complete replacement" | não |
| T-027 | r2 | ✅ | "they must be corrected too"; "newly completed declaration"; cita a exclusão do NPD | não |
| T-028 | r1 | ✅ | "Yes … 5/10,000 of the salary"; "The employee bears it"; Lei 4/2021 | não |
| T-028 | r2 | ✅ | "Yes … 0.05% … monthly salary … the employee bears it" | não |
| T-029 | r1 | ✅ | "19.88%"; "Approximate total: 25.00%" | não |
| T-029 | r2 | ✅ | "19.88%"; "about 25.00% of gross pay" | não |
| T-030 | r1 | ✅ | "2 caps" + parcela elegível 50%/100%; 15% mensal "No" cumulativo; anual 312,066 TL "Yes" | não |
| T-030 | r2 | ✅ | 15% mensal "not cumulative"; anual 312,066 "cumulative"; 50%/100% | não |

### Totais da rodada 1

- **Nota: 20/30 ✅** · 5 ⚠️ (4 consistentes: T-010, T-016, T-017, T-018; 1 instável: T-003) · 5 ❌ (T-001, T-006, T-022, T-024, T-026). Por resposta: r1 20 ✅ / 4 ⚠️ / 6 ❌; r2 21 ✅ / 4 ⚠️ / 5 ❌.
- **Erro conhecido repetido:** T-001 (r1 e r2), T-003 (r1), T-024 (r2: teste no begin_date); parcial em T-017 (r1 e r2: CNPS sem teto).
- **Causa:** T-006, T-022, T-026, T-010, T-016 e T-018 dependem de material interno que o claude.ai não alcança sem o brain/Drive (WTC, Global WTC, design, DevKB, KB Bulgária). T-001, T-003 e T-017 são erros de conteúdo.

| País | ✅ / total |
|---|---|
| Espanha | 3/6 (T-001 ❌, T-003 ⚠️ instável, T-006 ❌) |
| Ucrânia | 5/6 (T-010 ⚠️) |
| Colômbia | 2/2 |
| França | 1/1 |
| Chile | 0/1 (⚠️) |
| Chade | 0/1 (⚠️) |
| Irlanda | 0/1 (⚠️) |
| Costa do Marfim | 1/1 |
| Holanda | 1/1 |
| Congo | 1/1 |
| Reino Unido | 1/1 |
| Hungria | 0/1 (❌) |
| Gabão | 0/1 (❌) |
| Canadá | 1/1 |
| Bulgária | 0/1 (❌) |
| Lituânia | 1/1 |
| Egito | 1/1 |
| Bélgica | 1/1 |
| Turquia | 1/1 |
| **Total** | **20/30** |

| Tipo | ✅ / total | Observação |
|---|---|---|
| V (valor) | 9/10 | só T-017 ⚠️ |
| M (mapeamento) | 3/8 | T-001 ❌, T-022 ❌, T-026 ❌, T-010 ⚠️, T-003 ⚠️ instável |
| R (regra/design) | 5/8 | T-024 ❌, T-016 ⚠️, T-018 ⚠️ |
| P (processo/procedimento) | 3/4 | T-006 ❌ |
| **Total** | **20/30** | |

### Revisão do gabarito (2026-10-27, depois da fonte primária)
Conferido pela janela geral na fonte primária (detalhe em `revisoes/2026-10-27-gabarito-T001-T003-T024.md`; entradas novas em [[correcoes]] de 2026-10-27):
- **T-003 — anulada na rodada 1.** Desde o exercício 2025, B.03 = mutualidades de funcionários (Orden HAC/1431/2025, BOE-A-2025-25390); "79429/79430 = B.03" ficou desatualizado e a chave nova não está na norma. Novo gabarito só depois da confirmação da AEAT. 79432 = L.27 continua.
- **T-001 — anulada na rodada 1.** O Manual CRA da TGSS de 2026-07-01 (§2, CRA 0051–0054) manda prorratear E/I nos 12 meses anteriores e põe o excesso sobre a indenização obrigatória na base (I). O gabarito (todos 0054/E no mês do desligamento) fica em revisão até a decisão de design sobre qual WT leva o 0054.
- **T-024 — gabarito reescrito e recorrigido.** ✅: isenção por **mês**, até o mês do 25º aniversário inclusive (mês do período ≤ mês do 25º aniversário; Szja tv. 29/F (3); NAV nº 73 de 2026-03-19) **e** `$person.birth_date`. ⚠️: regra do mês certa sem a variável, ou `begin_date` com a variável. ❌: `end_date` (tira o mês do aniversário) ou `$employee.years_worked`. Recorreção: r1 ⚠️ (regra YYYYMM certa, sem variável); r2 ⚠️ (25º aniversário ≥ início do período, que inclui o mês; sem variável) → **⚠️**.
- **Nota ajustada da rodada 1: 20/28 ✅** (T-001 e T-003 anuladas) · 5 ⚠️ (T-010, T-016, T-017, T-018, T-024) · 3 ❌ (T-006, T-022, T-026). A nota original de 20/30 fica acima como registro.

### Gabarito a revisar (decisão do usuário)

O gabarito não foi alterado. Pontos para decidir:

1. **T-001:** as duas respostas citam o Manual CRA da TGSS de 01/07/2026 (seg-social.es/descarga/es/188863, §2 "CRA 0051 a 0054"): 0054 com E e I, prorrateado nos 12 meses anteriores, e os WTs 58197/58198 como as linhas do CRA. Contradiz o gabarito (58184/58186/58188 em 0054/E e 58197/58198 fora do CRA). Conferir o manual vigente contra a SR-81 antes de manter o gabarito.
2. **T-003:** a r1 cita a Orden HAC/1431/2025, art. 2, Tres (a partir do exercício 2025), que teria redefinido a subclave B.03 e criado o campo de tipo de prestação em B.01, e diz que a FAQ da AEAT está desatualizada. O gabarito dá B.03. Verificar se a FAQ ainda é a fonte vigente.
3. **T-024:** as duas respostas citam Szja tv. 29/F § (3) (o mês em que o jovem faz 25 anos ainda dá direito) e rejeitam o end_date como teste de idade; o gabarito diz end_date. Também não há como acertar `$person.birth_date` sem a lista de variáveis do DD. Confirmar o gabarito com a fonte (T-2026-05-27/29).
4. **T-006, T-022, T-026 (e T-010 em parte):** respostas "não tenho o arquivo" não cabem em ✅/⚠️/❌ como escritos. Contei ❌. Decidir se vira categoria própria ("recusa honesta"); essas perguntas dependem de arquivo interno (WTC, Global WTC, KB Bulgária) e não são respondíveis no claude.ai sem o brain.
5. **T-017:** o critério ⚠️ diz "30% certo sem dizer que o excesso vai à CNPS", mas as duas respostas afirmam o contrário (CNPS sem teto, fora da base). Contei ⚠️ pelo texto; o ❌ ("isenção total") também poderia valer para a parte CNPS.
6. **T-016 e T-018:** o gabarito ("3 passos + 1 step YTM"; reg `Differential`) depende do design interno; as respostas dão uma estrutura legal razoável sem esses nomes. Contei ⚠️ ("estrutura parecida"). Confirmar se o critério quer o termo exato.
7. **T-006:** o gabarito pede conferir a versão vigente do WTC (maior número); no claude.ai sem Drive isso é inalcançável (mesmo ponto do item 4).

### Observações de método

- A pesquisa em conversas anteriores estava ativa nesta rodada, então a r2 pode ter lido a r1 (ex.: T-012 r2 respondeu em menos de 30 s). As duas rodadas podem não ser independentes; a instabilidade medida (só T-003) pode estar subestimada.
- A T-001 r1 foi refeita: a 1ª tentativa (chat 0d30b93d) chamou o Google Drive e travou em "Vincular"; a refeita rodou com conectores desligados.
- Algumas respostas citam conversas anteriores do projeto Mercans (T-001 r1/r2: resposta SR-81 de abril; T-026: revisão do BG WTC V2.0) e a página DSR da Mercans (T-019): a memória/histórico da conta traz contexto interno e enviesa a medição.

### Rodada 2: Claude Code + cérebro (2026-10-27)
- **Nota: 28/28 ✅** (rodada 1 no claude.ai: 20/28). As 5 ⚠️ e 3 ❌ da rodada 1 (T-006, T-010, T-016, T-017, T-018, T-022, T-024, T-026) viraram ✅: eram "falta no brain" para o claude.ai (WTC, Global WTC, design, DevKB), e no Claude Code o cérebro e o Drive estão ao alcance.
- **Passos:** 2 a 6 chamadas de ferramenta por pergunta (T-001: ~10). `contexto_pais` bastou para o veredito em 21 de 30; nas outras, o corte de linha longa das correções obrigou a abrir `correcoes.md` (5 casos) ou o arquivo-fonte.
- **Ressalvas:** livro aberto (o Conjunto A vem de [[correcoes]], que o agente pode ler), então mede achar rápido e com fonte, não conhecimento às cegas; o Conjunto C (cego) continua sendo a medida final. Skills `payroll-compliance-<país>` não carregaram nos agentes.
- **Achados fora do pedido** (registrados nos hubs): spec AFI v2.0-FINAL B55/L55 ainda "Tipo de Riesgo Laboral" ([[Espanha]]); spec 4DF v3.3 B72 rotula 157 como renda de não residente e WTC UA V4.3 com justificativa genérica nas linhas 65808 e 62942 ([[Ucrania]]); CCG UA V1.6 no Drive (hub corrigido). A leitura de versões do Drive não pegava "V1_6": corrigidos Ucrânia CCG, Egito CCG v1.4, Hungria WTC v1.0, Romênia WTC v3.2.
- **Ações:** `contexto_pais` mostrar a correção inteira quando houver poucas (≤ 10); Conjunto C.
- Respostas: [[testes/rodadas/2026-10-27-claude-code/T-001|T-001]] · [[testes/rodadas/2026-10-27-claude-code/T-002|T-002]] · [[testes/rodadas/2026-10-27-claude-code/T-003|T-003]] · [[testes/rodadas/2026-10-27-claude-code/T-004|T-004]] · [[testes/rodadas/2026-10-27-claude-code/T-005|T-005]] · [[testes/rodadas/2026-10-27-claude-code/T-006|T-006]] · [[testes/rodadas/2026-10-27-claude-code/T-007|T-007]] · [[testes/rodadas/2026-10-27-claude-code/T-008|T-008]] · [[testes/rodadas/2026-10-27-claude-code/T-009|T-009]] · [[testes/rodadas/2026-10-27-claude-code/T-010|T-010]] · [[testes/rodadas/2026-10-27-claude-code/T-011|T-011]] · [[testes/rodadas/2026-10-27-claude-code/T-012|T-012]] · [[testes/rodadas/2026-10-27-claude-code/T-013|T-013]] · [[testes/rodadas/2026-10-27-claude-code/T-014|T-014]] · [[testes/rodadas/2026-10-27-claude-code/T-015|T-015]] · [[testes/rodadas/2026-10-27-claude-code/T-016|T-016]] · [[testes/rodadas/2026-10-27-claude-code/T-017|T-017]] · [[testes/rodadas/2026-10-27-claude-code/T-018|T-018]] · [[testes/rodadas/2026-10-27-claude-code/T-019|T-019]] · [[testes/rodadas/2026-10-27-claude-code/T-020|T-020]] · [[testes/rodadas/2026-10-27-claude-code/T-021|T-021]] · [[testes/rodadas/2026-10-27-claude-code/T-022|T-022]] · [[testes/rodadas/2026-10-27-claude-code/T-023|T-023]] · [[testes/rodadas/2026-10-27-claude-code/T-024|T-024]] · [[testes/rodadas/2026-10-27-claude-code/T-025|T-025]] · [[testes/rodadas/2026-10-27-claude-code/T-026|T-026]] · [[testes/rodadas/2026-10-27-claude-code/T-027|T-027]] · [[testes/rodadas/2026-10-27-claude-code/T-028|T-028]] · [[testes/rodadas/2026-10-27-claude-code/T-029|T-029]] · [[testes/rodadas/2026-10-27-claude-code/T-030|T-030]]

### Rodada 3: claude.ai + skill brain-service (2026-10-27)
- **Nota: 24/28 ✅**: rodada 1 no claude.ai, 20/28; rodada 2 no Claude Code, 28/28. Correção em [[testes/rodadas/2026-10-27-claudeai-skill/CORRECAO|CORRECAO]].
- **Viraram ✅:** T-006, T-022 e T-026 (antes ❌) e T-010, T-017 e T-024 (antes ⚠️). O material interno agora vem na skill.
- **Pioraram:**
  - T-013 ❌: na ARL, preferiu ofícios DIAN achados na web à correção do Oficio 27408.
  - T-018 ❌: triplet Threshold/Base/Amount. O hub [[Irlanda]] é ambíguo ("Differential" × "padrão IE: triplet").
  - T-028 ⚠️: base pela FAQ ETA de mar/2026, que não está no pacote.
- **T-016 ⚠️:** conhece o design v1.1, mas propõe outra estrutura.
- **Repetição com a skill v3** (T-013, T-016, T-018, T-028): a nota não mudou, mas T-013 (Oficio 036846/2015, ARL), T-018 (leitura "específica do RPN" = Irlanda) e T-028 (FAQ ETA v4 2026) indicam **gabarito a revisar** na fonte primária. Detalhe em CORRECAO.
- **Ações:**
  - SKILL.md: a correção do cérebro vence a busca web, e o design registrado vem antes de propor outro.
  - Desambiguar o hub da Irlanda (conferir no DevKB).
  - Conferir a FAQ ETA (T-028).
  - Levar a correção 27408 à skill da Colômbia.

### Revisão do gabarito: T-013, T-018, T-028 (2026-10-27)
Conferido na fonte primária depois da repetição com a skill v3. Detalhe em [[testes/rodadas/2026-10-27-claudeai-skill/CORRECAO|CORRECAO]].
- **T-013, mantido.** O Oficio DIAN 036846/2015 (29/12/2015, [normograma](https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_36846_2015.htm)) tratava o subsídio de incapacidade ARL (Ley 776 art. 3) como isento pelo ET 206 num. 1. O Oficio 27408/2019, item 7.1 (cópia em `raw/docs/oficiais/CO/`), é posterior e diz que as incapacidades "por enfermedad general y accidentes de trabajo" não são rendas isentas. Vale 2019. Conflito registrado em [[correcoes]] e no hub [[Colombia]].
- **T-018, revisto.** No chat design-dev-kb, o Learning #2 (triplet) foi revogado em 02/07 **como regra geral** por ser "específico do RPN", e o padrão IE de produção tem o triplet. Para a Irlanda a resposta certa é o triplet via RPN; `Differential` é a regra dos países sem RPN. Fonte B; falta conferir no DevKB oficial.
- **T-028, revisto.** A skill `payroll-compliance-egypt` v2 (22/10, `01-ccg.md` §8.2) já citava a FAQ ETA v4 Q110 (base = só verbas básicas, exceto diaristas egípcios) e manda seguir o ETA e informar a divergência com a Circular 14/2021 (total mensal). O gabarito antigo só aceitava "total".
- **Recontagem:** rodada 1: 19/28 (T-028 r1 ✅, cita a leitura restrita da Fatwa 244/2023; r2 ⚠️, só "gross"; T-018 segue ⚠️). Rodada 2: 26/28 (T-018 ❌, recomendou `Differential` para a Irlanda; T-028 ⚠️, só "total"). Rodada 3: 26/28 (T-018 e T-028 ✅).

## Quarentena do Conjunto C (data de corte = data do MVP: AAAA-MM-DD)
| # | Ticket | Resolvido em | País | Pergunta derivada | Ingerir depois de |
|---|---|---|---|---|---|
| C-001 | | | | | medição final |

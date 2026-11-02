# Checkpoint do Step 4 — Research EUA (mandato)

> Gerado em 2026-10-30, atualizado na tentativa 4 de selo (rodada 3 do agente 2) e depois nas tentativas 5 (30/10) e 6 (01–02/11, mandato selado), para exposição ao usuário no fim da rodada (modo contínuo autorizado em 29/10; a parada do Step 4 foi dispensada). Plano: [[Research Pipeline/USA/PLANO-EXECUCAO|PLANO-EXECUCAO]]. Estado da frente: [[frentes/eua/estado|estado]]. Fontes: `MANDATE.md` (seção Seal assessment, tentativa 4), `_pipeline/build-manifest.json`, `SKELETON-MANIFEST.md`, `SOURCE-REGISTER.md` (902 linhas), `BLOQUEIOS-CHROME.md` (todos em `Research Pipeline/USA/US-compliance/`, exceto o registro em `00-official-sources/`).

## Tentativa 6 (01–02/11) — mandato SELADO

> Esta seção é a mais recente. A seção "Tentativa 5" e as seguintes ficam como histórico.

- **Mandato SELADO em 02/11/2026.** 65 de 65 perguntas respondidas. `mandate_status: sealed` no `MANDATE.md` e no `_pipeline/build-manifest.json` (`mandate_sealed_on` 2026-11-02). Os três critérios do selo passam: (1) nenhuma pergunta aberta (`grep -c pending_research` no MANDATE dá 0; a lista do manifest tem 0 `open`); (2) conferência mecânica: todo `register_id` citado nas 65 respostas resolve para uma linha `active` do `legal-basis-register.csv` (1.303 linhas, 1.006 ativas, ids únicos), contando as linhas do usuário US-OWN-*; (3) status virou `sealed` nos dois arquivos.
- **Passo 1 (01/11):** US-MQ-03 (idioma) respondida na decisão US-OWN-006 e US-MQ-05 parte (c) (encargos de transporte e de formação) na US-OWN-007, ambas tomadas pelo líder do build com a delegação do usuário de 01/11 (`PLANO-ATE-O-FIM.md`, regra 1). O merge P9 tirou do status ativo 26 linhas citadas; as referências foram reapontadas, mas três partes ficaram sem sucessora ativa e foram reabertas com o mesmo id: **US-MQ-26 CT parte 5**, **US-MQ-45 MS parte 2** e **US-MQ-57 OR parte 5** (ficou 62 de 65).
- **Passo 2 (02/11):** as três partes fecharam em linhas novas, com o arquivo oficial guardado no build e relido antes de citar:
  - **CT (US-CTP10-001):** Circular CT IP 2026(1), `00-official-sources/pdfs/CT/CT_IP-2026-1_2026-11-02.pdf` (md5 a64b2bbb…). Residente: retém sobre todo o salário; se outro estado exige retenção, o imposto de CT é rateado e só a diferença vai à DRS (Exemplo 4). Não residente: salário por serviço prestado em CT, alocado no CT-W4NA; regra dos 15 dias (PS 2015(6)): até 15 dias no ano não retém; passou de 15, retém sobre tudo, inclusive os 15 primeiros. Nenhum acordo de reciprocidade na publicação.
  - **MS (US-MSP10-001):** menu de tributos empresariais do site do MDOR, `pdfs/MS/MS_DOR-home_2026-11-02.html` (md5 942d0f24…). O único item sobre salário é a retenção estadual (Withholding Tax); não há imposto municipal, de condado ou de distrito escolar sobre salário. É prova por ausência na lista oficial (registrado assim; confiança média-alta).
  - **OR (US-ORP10-001):** DOR 150-206-692, edição em vigor Rev. 02-08-22 (é a que o site oficial serve em 02/11), `ccg-sources/OR/OR_150-206-692_2026-11-02.pdf` (md5 bec23f2e…), substitui US-OR-P5-1-001. Não residente: retém sobre o salário por serviço em OR, salvo se o ganho em OR no ano ficar abaixo da dedução padrão (2026: 2.910 solteiro, de US-OR-P5-1-002). Empregador de fora com residente de OR trabalhando em OR: retém tudo (inclusive teletrabalho), com dispensa possível até US$ 300 por empregado no ano. Sem acordo de reciprocidade.
- **Tier:** sem mudança. Geral **T4**; censo **9 T1 / 31 T3 / 11 T4 / 0 sem classe**. As três partes reabertas e fechadas não mexem em tier (CT T3, MS T3, OR T4). O texto do veredito (só o parêntese inicial mudou) foi repetido igual no MANDATE, no SKELETON-MANIFEST e no build-manifest, e atualizado na seção 1 abaixo.
- **Artefatos:** todos continuam `scaffolded`. Pelo contrato 1.4.0, o scaffolder só grava `scaffolded`; quem avança é o orquestrador. Com o selo, a trava do mandato saiu: o próximo passo é o estágio 1 (CCG).
- **build-manifest.json:** lista de perguntas sincronizada com o MANDATE (65 respondidas, com `_answer_register_ids_all`); `answer_register_id` preenchido em 21 das 24 que estavam nulas; US-MQ-24 CA, 46 MT e 49 NE ficam nulas com nota, porque todos os ids que citam têm mais segmentos do que o padrão do schema aceita (todos ativos). `languages` atualizado (holerite e declarações em inglês, regras separadas; documento bilíngue permitido). O id fora do padrão US-UT-P5-1-001-dup1 foi trocado por **US-UT-P5-1-006** na lista de defeitos. Partição medida: estágio 1 `ccg-sources` 3.933.039 bytes (9 arquivos), estágios 3 a 7 vazios, tudo abaixo de 32 MB; `pdfs/` (214.620.192 bytes) não é lida por nenhum estágio.
- **Higiene, não trava o selo (para o agente 2, antes do estágio 1 usar os números):**
  - Cerca de 60 vínculos `supersedes` que apontam para linhas que não estão `superseded`, e 24 valores de `supersedes` em texto livre que não são ids (P9-MERGE.md, seção 7 "Found, not fixed"). Corrigir linha a linha; troca em lote derrubaria linhas A.1 ativas.
  - 91 linhas antigas `superseded` sem `effective_to`.
  - Linhas MANUAL que ainda esperam a decisão sobre PDF salvo via WebFetch: US-VT-PIT-002, US-VT-P5-1-003, US-VA-PIT-005, US-WV-PIT-004. US-NDL-001 (idioma de ND) não é citada em nenhuma linha `register_id`.
  - Existe `_prompts/chrome-rehunt.md` (29/10) numa pasta que a regra do esqueleto mantém vazia; é o prompt de reexecução manual do orquestrador, preservado.
- **Validador:** `validate_contract.py build-manifest _pipeline/build-manifest.json` deu **PASS** (jsonschema 4.26.0).

## Tentativa 5 (30/10)

> Histórico (substituída pela tentativa 6). As seções seguintes descrevem a tentativa 4 e também ficam como histórico.

- **Mandato NÃO selado.** 63 de 65 perguntas respondidas (eram 52). Todas as 51 jurisdições estão respondidas. Ficam abertas só US-MQ-03 (idioma) e US-MQ-05 (encargos de transporte e de formação profissional, parte c). Os critérios do selo: (1) FALHA, porque há 2 abertas; (2) PASSA, porque todos os ids das 63 respostas resolvem para linha `active`; (3) a flag não foi virada. Nenhum artefato saiu de `scaffolded`.
- **Fechadas nesta tentativa (11):** US-MQ-12 (decisão do usuário, US-OWN-005: todas as populações IN), IN, LA, ME, MN, NH, NJ, NM, UT, VA, VT. As fontes vêm de P6, P8 e das duas linhas da sessão principal: US-VTP9-001 (regra 24-090-003 no Code of Vermont Rules oficial) e US-NHP9-001 (NHES 0041 R-8/16 listado como atual).
- **Tier:** o geral continua T4. NJ passou de T3 provisório para **T4** (Jersey City e Newark cobram imposto de folha do empregador com declaração trimestral à cidade: US-NJP6-001/-002). O censo agora é **9 T1 / 31 T3 / 11 T4**. O domínio `employer_payroll_levies` passou de T3 para **T4-shaped** (imposto de folha da cidade com declaração própria). WA fica T1, com Seattle declarada como elemento T4-shaped. As citações do veredito foram trocadas pelas sucessoras ativas (ex.: US-OH-003 → US-OH-P5-2-003, US-MD-PIT-001 → US-MD-P5-1-001).
- **O que trava US-MQ-03:**
  - GA só tem linha tier B/MANUAL (US-GAL-001).
  - MS está `partial` (US-MSL-001).
  - Em MD, o aviso da Healthy Working Families Act não foi lido.
  - As páginas de cartazes obrigatórios não foram lidas em nenhum estado, nem as leis estaduais de idioma oficial.

  Fecha com uma de duas saídas: o agente 2 lê essas três fontes e o usuário decide que cartazes ficam fora do escopo de folha; ou o usuário aceita a resposta de escopo do bloco (linha `US-OWN-006`). O desenho de idioma (G-LANG) já está decidido: `en` primeiro e `es` em 2º. O eixo de participação no emprego deixou de travar.
- **O que trava US-MQ-05 (c):** a ausência de encargo de transporte ou de formação profissional fora da lista P7 não está provada em 22 estados (AK, AR, AZ, CT, GA, HI, IA, KS, KY, LA, MA, MD, MI, MO, MT, NC, ND, NH, OK, RI, UT, VA). Nesses estados a lista oficial de tributos não foi lida, estava ilegível ou foi lida só por resumo, e a própria P7 achou encargos que o censo tinha perdido. Fecha com uma de duas saídas: o agente 2 lê a lista oficial completa (A.2) desses estados; ou o usuário aceita "transporte só em OR e NY; formação/administrativos conforme a P7; nos demais, nenhum localizado" (linha `US-OWN-006`/`-007`). As partes (a) IWO e (b) PFML do Maine ficaram respondidas.
- **Linhas do registro que parecem erradas (para o agente 2; nenhuma resposta depende delas):**
  - US-NYP7-002: a nota "DFS page 403" está velha; citar US-NYP8-001 (0,432% / 411,91).
  - US-WVP7-001: a taxa de automação está `active`, mas o próprio texto diz que os 7% são ambíguos (pontos percentuais ou relativo).
  - Tier "A" fora da lista de valores em US-VTP9-001 (deveria ser A.1) e US-NHP9-001 (deveria ser A.3).
  - Linhas tier B com status `active` (ex.: US-MEL-002, que carrega CSSF/UPAF).
  - US-UT-P5-1-001 está como tier B, mas a mesma página do DOL é A.2 em outras três linhas.
  - Falta o `supersedes` em US-NJ-P5-2-001 e US-NHR3-001.
  - O id US-UT-P5-1-001-dup1 está fora do padrão.
  - A decisão sobre PDFs salvos via WebFetch (VT GB-1210, VA, WV), que estão MANUAL, continua pendente.
- **Validador:** `validate_contract.py build-manifest` deu PASS (jsonschema 4.26.0).

## Resumo em 5 linhas

1. **Mandato NÃO selado** (`mandate_status: pending_research`, tentativa 4 de 30/10): 52 de 65 perguntas respondidas (eram 34), 13 abertas (3 federais, 10 estaduais: IN, LA, ME, MN, NH, NJ, NM, UT, VA, VT). Nenhum artefato saiu de `scaffolded`.
2. **Tier geral T4** mantido; censo dos 51 agora **9 T1, 32 T3, 10 T4, 0 sem classificar** (WV passou de T3 provisório para T4 verificado; NJ segue T3 provisório, candidato a T4 em Newark/Jersey City, linha MANUAL/gated).
3. **Selo falha em 2 de 3 critérios:** (1) 13 perguntas abertas; (2) ids não resolvem para CT (US-MQ-26) e KS (US-MQ-36) porque o rebuild do registro (902 linhas) perdeu 12 linhas do shard `mandate-P5-W3A-r2.csv`, e US-MQ-01/02/04/09 citam linhas hoje `superseded` por vínculo errado (as respostas se sustentam em outras linhas ativas).
4. **Travas das 13:** 8 estados só de acesso (IN, MN, NH, NJ, NM, UT, VA, VT), 2 de acesso mais defeito de registro (LA, ME); federal: US-MQ-03 pesquisa faltante + acesso, US-MQ-05 acesso + pesquisa faltante, US-MQ-12 decisão do usuário. Confiança fraca persiste: US-MQ-01 88%, US-MQ-10 80%, 29 estaduais em Medium-High sem número.
5. **Decisão pendente do usuário:** rota (a) baixar as URLs de acesso para `00-official-sources/pdfs/<UF>/`; (c) assinar a matriz US-MQ-12; (d) decidir o corte de escopo de US-MQ-03 e a parte (c) de US-MQ-05 (a rota de aceitar as listas federais de TDI/PFML não foi aceita); mais aceitar ou refazer as leituras por script anteriores a 29/10. A rota (b), corrigir o registro, é do agente 2.

## 1. Veredito de tier

### Geral (palavras do compliance-scaffolder, repetir igual no CCG m01, no scope_manifest.json e no relatório de QA)

(Texto atualizado na tentativa 6, 02/11/2026; idêntico ao do MANDATE.md, SKELETON-MANIFEST.md e build-manifest.json.)

> Overall T4 (discriminator confirmed 2026-10-29 on source-read evidence; per-jurisdiction census completed at seal attempt 3 and re-checked at seal attempts 4, 5 and 6, 2026-10-30 to 2026-11-02; mandate sealed 2026-11-02 with all 65 questions answered; the limbs reopened and closed at seal attempt 6 (US-MQ-26 CT, US-MQ-45 MS, US-MQ-57 OR) bear on no tier). Employer-operation test: T4 requires a second independent calculation AND a separate remittance/return to a second authority. Federal: 26 U.S.C. 3402(a)(1) obliges every employer to withhold federal income tax under IRS tables and covers federal tax only [US-FED-012]; FICA and FUTA go on federal returns 941/944/940 [US-FED-005, US-FED-007, US-FED-015]. State: a wage-taxing state imposes its own withholding computed on its own basis (e.g. Va. Code 58.1-461 [US-VA-PIT-002]) remitted to the state revenue authority on its own returns (Virginia Tax VA-5/VA-6 [US-VA-PIT-003]); state UI is a separate state tax base and agency (Fla. Stat. 443.1216 [US-MULTI-001]; SC Code ch. 41-31 [US-SC-002]). Nothing is absorbed into the federal deduction (contrast Switzerland, StHG Art. 36a Abs. 1, where one deduction discharges all levels). FUTA is federal but its credit depends on state UI paid and on the state's Title XII loan status (26 U.S.C. 3302(c)(2) [US-FED-014]): a cross-layer dependency, so futa is T3. Inside a state, a local layer is T4 where a locality receives a separate return (City of Portland Metro SHS / Multnomah PFA [US-OR-003]; Ohio municipal income tax, ORC 718.03 [US-OH-P5-2-003]; Pennsylvania Act 32 EIT/LST to the local collector [US-PA-004]; Jersey City and Newark employer payroll taxes on quarterly city returns [US-NJP6-001, US-NJP6-002]) and T3 where it is piggybacked on the state return (Maryland county tax on MW506 [US-MD-P5-1-001]; NYC and Yonkers on NYS-45/NYS-1 [US-NY-008]). Consequence: the federal core and each jurisdiction are declared and scoped as parallel layers, and the multistate domain routes each employee to one or more of them. Jurisdiction annexes (re-checked 2026-10-30, seal attempt 5): 9 T1 (no state wage tax; SUI and levies only: AK, FL, NH, NV, SD, TN, TX, WA, WY; WA declares the Seattle payroll expense tax, a threshold-conditional employer tax on a city return [US-WA-P5-1-001], as a T4-shaped element), 31 T3 (state withholding, local layer absent or piggybacked on the state return), 11 T4 (local layer remitted to the locality on its own return: AL occupational taxes [US-AL-P5-1-001], CO Denver OPT [US-CO-P5-2-001], DE Wilmington [US-DE-P5-2-001], KY occupational taxes [US-KY-P5-2-002], MI 23 self-administering cities [US-MI-P5-2-002], MO St. Louis/Kansas City [US-MO-P5-2-006], NJ Jersey City/Newark employer payroll taxes filed with the city [US-NJP6-001, US-NJP6-002], OH [US-OH-P5-2-003], OR [US-OR-003], PA [US-PA-004], WV municipal service fees withheld and remitted to the city, W. Va. Code 8-13-13 [US-WVR3-001], Charleston [US-WVR3-002]); 0 unclassified; no classification rests on MANUAL/gated evidence.

Por que T4 e não T2/T3: o teste é "segundo cálculo independente E remessa/declaração separada a uma segunda autoridade". O federal fica no IRS; cada estado que tributa salário calcula na sua base e remete na sua autoridade; SUI é base e agência estaduais separadas. Nada é absorvido pela retenção federal (contraste com a Suíça). Camada local é T4 quando a cidade recebe declaração própria (OR, OH, PA, AL, CO, DE, KY, MI, MO e, desde a tentativa 4, WV com taxas municipais por empregado, W. Va. Code 8-13-13) e T3 quando vai na declaração do estado (MD, NY/NYC/Yonkers, IN).

### Por domínio

| Domínio | Tier | Raciocínio (scaffolder) |
|---|---|---|
| federal_income_tax | T2 | Confirmed: one authority (IRS), 26 U.S.C. 3402 federal-only withholding [US-FED-012], Pub. 15-T tables [US-FED-001]; NRA and supplemental inside one calculation. |
| fica_social_security_medicare | T2 | Federal, uniform rates, one authority; wage base indexed (US-MQ-06). |
| futa | T3 | Confirmed: federal return, but the credit depends on state UI paid and credit-reduction status, 26 U.S.C. 3302(a)(1), (c)(1), (c)(2) [US-FED-014]. |
| state_income_tax | T4 | Confirmed: separate state calculation and separate state return (Va. Code 58.1-461 [US-VA-PIT-002]; VA-5/VA-6 [US-VA-PIT-003]); verified in 21 wage-tax states, see the per-jurisdiction table. T1 annex in the 9 no-wage-tax states. |
| local_income_tax | T4 | Re-checked 2026-10-30 (attempt 3): T4 where a locality receives a separate return, verified in 9 jurisdictions: OR [US-OR-003], OH [US-OH-003], PA [US-PA-004, US-PA-006], DE Wilmington [US-DE-P5-2-001], AL occupational [US-AL-P5-1-001], KY occupational [US-KY-P5-2-002], MI 23 self-administering cities (Detroit via Treasury) [US-MI-P5-2-002], MO St. Louis / Kansas City [US-MO-P5-2-006/-007], CO Denver OPT [US-CO-P5-2-001]. T3 where piggybacked: MD county on MW506 [US-MD-P5-1-001], NYC/Yonkers on NYS-45/NYS-1 [US-NY-008], IN county rates [US-IN-P5-1-001]; IA school-district/EMS surtaxes are settled on the individual return, not withheld [US-IA-P5-1-005]. Open local limbs: NJ Newark (gated), WV municipal service fees (partial). |
| state_unemployment_insurance | T4 | Confirmed: separate state tax base, agency and quarterly report (Fla. Stat. 443.1216 [US-MULTI-001]; MD [US-MD-SUI-001]; SC ch. 41-31 [US-SC-002]). Employee UI contributions exist in exactly three states, AK, NJ, PA (DOL Comparison of State UI Laws, law as of 2023-01-01 [US-FED-P5-2-006]; 2026 rates AK 0.50% [US-AK-P5-1-002], PA 0.07% [US-PA-003]); employer-only elsewhere. |
| sdi_tdi_pfml | T4-shaped | Re-checked attempt 3: TDI programmes exactly CA, HI, NJ, NY, RI (+PR, out of scope) [US-FED-P5-2-007]. T3 where filed with the state wage return (CA SDI 1.3% [US-CA-EDD-004]; OR Paid Leave on the Combined Payroll Report [US-OR-002]); separate agency/report (WA PFML and WA Cares [US-WA-PFML-001, US-WA-LTC-001]; CT Paid Leave [US-CT-PL-001]; CO FAMLI [US-CO-FAMLI-001]; DE Paid Leave 0.8% [US-DE-P5-1-001]; ME PFML [US-ME-P5-1-002]; MD FAMLI from 2027-01-01 [US-MD-P5-1-003]); data-problem where insurer-funded (NY DBL/PFL [US-NY-005, US-NY-010], HI TDI [US-HI-003]). |
| workers_compensation | data-problem | Unchanged: mostly insurer premiums outside payroll. Payroll deduction in a state-fund state now verified: WA employer deducts half the medical-aid premium per class, RCW 51.16.140 [US-WA-LTC-002]. Variability axis is the insurer/state fund, not a statutory rate table (US-MQ-05). |
| multistate | T4 | Routing layer that selects which T4 jurisdictions apply per employee (work state, residence state, reciprocity, convenience rule, SUI localization), US-MQ-10. |
| labour_code | T3 | Federal floor (FLSA) plus state wage-payment rules; one calculation, state-keyed fields. |
| payslip_statute | T3 | Confirmed: no federal pay-statement mandate (29 CFR 516.2(a) is recordkeeping only [US-FED-010]); state content statutes verified in MD, MN, SC, VA, WA; none in ND, SD chapters read. |
| statutory_reporting | T4 | Federal 941/940/W-2 plus per-state withholding, reconciliation, UI and local returns; submitted via third-party provider (US-MQ-09). |
| leave | T3 | State and local paid-sick-leave rules, state/locality-keyed. |
| termination | T3 | State final-pay deadlines, state-keyed. |
| benefits_in_kind | T2 | Federal fringe rules; state conformity is data. |
| deductions_garnishments | T3 | Federal CCPA limits plus state variations. |
| collective_agreements | T1 | Confirmed (US-MQ-07 answered): CBAs bind the certified unit only, 29 U.S.C. 159(a) [US-FED-018]; Davis-Bacon is a contract overlay [US-FED-019]. |
| indexation | T3 | Re-cited (US-MQ-06 answered): C-CPI-U, 26 U.S.C. 1(f)(3) [US-FED-026]; Rev. Proc. 2025-32 [US-FED-002]; OASDI base 184,500 re-derived [US-FED-003], 2027 = 192,300 [US-FED-022]; state wage bases indexed per state. |
| payroll_data_protection | T2 | SSN handling rules, mostly uniform. |
| live_legal_change | T3 | 53 parameter sets change yearly AND mid-year 2026 changes already seen: GA rate 2026-05-11 [US-GA-001], UT 2026-06-01 [US-UT-PIT-002, M], OH tables 2026-08-01 [US-OH-002, M], ID 2026-07-23 [US-ID-001, M]; WA 2028 high-earner tax watch [US-WA-PIT-001]. |
| employer_payroll_levies | T3 | Re-checked attempt 3: employer-only payroll levies, one calculation per employer, jurisdiction-keyed: OR TriMet/Lane [US-OR-002]; NY MCTMT on its own return to DTF [US-NY-003]; NV MBT 1.17% general business [US-NV-P5-1-002]; Seattle payroll expense tax (local business tax, own return) [US-WA-P5-1-001]; Denver OPT employer 4.00/month [US-CO-P5-2-001]; WV unemployment automation fee from 2026-07-01 [US-WV-P5-2-001]; Newark payroll tax gated [US-NJ-P5-1-005]. |

## 2. Os 51 (50 estados + DC): tier, partes 1 a 6, fonte principal

Partes: 1 retenção/imposto de renda estadual; 2 camada local; 3 SUI; 4 SDI/PFML/outros encargos; 5 multi-estado (reciprocidade); 6 holerite + aviso de idioma + prevailing wage + procuração (POA) + oráculo.
Legenda: ✅ respondida com linha ativa do registro; ⚠️ parcial (inferida, só resumo/fonte secundária, ou ausência local "não verificada" por fonte oficial); ❌ ausente (não localizada, ilegível, MANUAL ou sem prova). "(cópia Wayback)" = alguma fonte citada na base do tier é cópia Wayback. Tier da camada do anexo do estado (T1 sem imposto salarial; T3 retenção estadual sem camada local separada; T4 camada local remetida à cidade). A classificação das partes é leitura nossa da lista "partes faltantes" do mandato (tentativa 3), não campo do contrato. Tentativa 4: nas 18 jurisdições recém-respondidas todas as partes foram dadas por fechadas pelo agente 2 e conferidas contra linha `active`; ficam ⚠️ só AK parte 2 (ausência local só por índice) e DC parte 1 (alíquota suplementar 'NOT LOCATED' na linha do mandato). Nas 10 abertas, ❌ é só a parte que o mandato lista como faltante; as demais viraram ✅ por leitura nossa (o mandato não as lista como faltantes). `respondida*` = respondida, mas com id sem resolução no registro (CT, KS).

| UF | Tier | Pergunta | P1 | P2 | P3 | P4 | P5 | P6 | Fonte principal (ID do registro e instrumento) |
|---|---|---|---|---|---|---|---|---|---|
| AK | T1 | respondida | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | US-AK-WT-001 Alaska Dept of Revenue Tax Division: Alaska Dept of Revenue Tax Division page (no wage tax statement) |
| AL | T4 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-AL-WH-001 Alabama Department of Revenue: Alabama Withholding Tax Tables and Instructions 2026 (whbooklet_0126) |
| AR | T3 | respondida | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | US-AR-WH-001 Arkansas DFA Revenue Division: Arkansas Withholding Tax Formula Method effective 01/01/2026 |
| AZ | T3 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-AZ-WH-001 Arizona Department of Revenue: Arizona Form A-4 2026 and employer instructions (cópia Wayback) |
| CA | T3 | respondida | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | US-CA-EDD-001 California Employment Development Department: California EDD 2026 contribution rates, withholding schedules |
| CO | T4 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-CO-P5-1-001 Colorado Department of Revenue: DR 1098 2026 Colorado Withholding Worksheet for Employers (10/21/25) |
| CT | T3 | respondida* | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | US-CT-WH-001 Connecticut Department of Revenue Services: Connecticut TPG-211 2026 Withholding Calculation Rules |
| DC | T3 | respondida | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | US-DC-P5-1-001 Council of the District of Columbia: D.C. Code 47-1812.08 Withholding of tax (read in full) (cópia Wayback) |
| DE | T4 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-DE-WH-001 Delaware Division of Revenue: Delaware Division of Revenue withholding FAQ (cópia Wayback) |
| FL | T1 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-FL-001 Florida Senate: Florida Constitution Art. VII s.5(a) - no income tax on natural person |
| GA | T3 | respondida | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | US-GA-001 Georgia Department of Revenue: Georgia Employer Withholding Tax Guide 2026 (rev. Sept 2026) |
| HI | T3 | respondida | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | US-HI-001 Hawaii Department of Taxation: HRS ch. 235 ss.61-69 withholding; DoTax withholding page |
| IA | T3 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-IA-001 Iowa Department of Revenue: Iowa Individual Income Tax Withholding Formula effective 2026-01-01 |
| ID | T3 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-ID-001 Idaho State Tax Commission: Idaho State Tax Commission withholding computing / 2026 tables (cópia Wayback) |
| IL | T3 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-IL-001 Illinois Department of Revenue: IL-700-T 2026 Illinois Withholding Tax Tables (cópia Wayback) |
| IN | T3 | aberta | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | US-IN-001 Indiana Department of Revenue: Indiana DOR Departmental Notice 1 (county tax rates for withholding) (cópia Wayback) |
| KS | T3 | respondida* | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | US-KS-001 Kansas Department of Revenue: KW-100 Kansas Withholding Tax Guide (cópia Wayback) |
| KY | T4 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-KY-P5-2-001 Kentucky Department of Revenue: 2026 Kentucky Withholding Tax Formula 42A003 (TCF)(10-2025) |
| LA | T3 | aberta | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | US-LA-PIT-001 Louisiana Department of Revenue: Louisiana Withholding Tables and Formulas R-1306 (1/26) |
| MA | T3 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-MA-P5-1-001 Massachusetts Department of Revenue: Massachusetts DOR Withholding Tax Guide (posted August 2026) |
| MD | T3 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-MD-PIT-001 Comptroller of Maryland: Maryland Employer Withholding Guide, effective January 2026 |
| ME | T3 | aberta | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | US-ME-P5-2-001 Maine Revenue Services: 2026 Withholding Tables for Individual Income Tax (revised Dec 2025) w (cópia Wayback) |
| MI | T4 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-MI-P5-2-001 Michigan Legislature: MCL 206.703 Income Tax Act of 1967, Sec. 703 (tax withholding) (cópia Wayback) |
| MN | T3 | aberta | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | US-MN-PIT-001 Minnesota Department of Revenue: Minnesota Income Tax Withholding Instruction Booklet and Tax Tables (s |
| MO | T4 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-MO-PIT-001 Missouri Department of Revenue: Missouri Employer Tax Guide 4282 (Revised 03-2026) (cópia Wayback) |
| MS | T3 | respondida | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | US-MS-PIT-001 Mississippi Department of Revenue: Mississippi Pub 89-700-25-1 Withholding Income Tax Tables and Employer |
| MT | T3 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-MT-P5-1-001 Montana Department of Revenue: Montana Employer and Information Agent Guide with Withholding Tax Tabl (cópia Wayback) |
| NC | T3 | respondida | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | US-NC-001 NC Department of Revenue: NC-30 2026 Income Tax Withholding Tables and Instructions for Employer |
| ND | T3 | respondida | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | US-ND-001 ND Office of State Tax Commissioner: ND Income Tax Withholding Rates and Instructions, wages paid in 2026 |
| NE | T3 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-NE-P5-1-001 Nebraska Department of Revenue: 2026 Nebraska Circular EN (Rev. 11-2025) - Wayback copy (cópia Wayback) |
| NH | T1 | aberta | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | US-NH-006 NH Department of Revenue Administration: NH DRA Taxes at a Glance (list of administered taxes) |
| NJ | T3 prov. | aberta | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | US-NJ-001 NJ Division of Taxation: NJ-WT New Jersey Income Tax Withholding Instructions (Sept 2025 editio |
| NM | T3 | aberta | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | US-NM-P5-2-001 New Mexico Taxation and Revenue Department: NM TRD FYI-104 New Mexico Withholding Tax (Rev. 11/2025), effective 20 |
| NV | T1 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-NV-001 NV Department of Taxation: NV Department of Taxation: Income Tax in Nevada |
| NY | T3 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-NY-001 NY Department of Taxation and Finance: NYS-50-T-NYS (1/26) New York State Withholding Tax Tables and Methods |
| OH | T4 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-OH-003 Ohio General Assembly (codes.ohio.gov): Ohio Revised Code Chapter 718 municipal income tax (withholding ORC 71 (cópia Wayback) |
| OK | T3 | respondida | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | US-OK-001 Oklahoma Tax Commission: Packet OW-2 2026 Oklahoma Income Tax Withholding Tables (Rev. 11-2025) |
| OR | T4 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-OR-001 Oregon Department of Revenue: 150-206-436 Oregon Withholding Tax Formulas (Rev. 12-31-25) |
| PA | T4 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-PA-002 Pennsylvania Department of Revenue: PA Department of Revenue employer withholding page |
| RI | T3 | respondida | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | US-RI-005 RI Division of Taxation: RI Division of Taxation Withholding Tax page |
| SC | T3 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-SC-001 South Carolina Department of Revenue: SCDOR employer withholding page (2026 SC W-4, tables, formula WH1603F) |
| SD | T1 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-SD-001 South Dakota Department of Revenue: SD Department of Revenue - individual taxes |
| TN | T1 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-TN-001 Tennessee Department of Revenue: TN Dept of Revenue: Hall Income Tax repealed 1 Jan 2021 |
| TX | T1 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-TX-P5-2-001 Texas Comptroller of Public Accounts: Texas Comptroller of Public Accounts - list of taxes and fees administ |
| UT | T3 | aberta | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | US-UT-PIT-002 Utah State Tax Commission: Utah Tax Commission Pub 14 Withholding Tax Guide (cópia Wayback) |
| VA | T3 | aberta | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | US-VA-PIT-002 Virginia General Assembly (LIS): Code of Virginia 58.1-461 Requirement of withholding |
| VT | T3 | aberta | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | US-VT-PIT-001 Vermont Department of Taxes: Vermont Department of Taxes - Withholding (employers) |
| WA | T1 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-WA-PIT-001 Washington Department of Revenue: Washington DOR - Income tax page (new tax from 1 Jan 2028) |
| WI | T3 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-WI-PIT-001 Wisconsin Department of Revenue: Wisconsin Publication W-166 Withholding Tax Guide (1/26) |
| WV | T4 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-WV-PIT-001 West Virginia Legislature: West Virginia Code 11-21-71 Requirement of withholding tax from wages (cópia Wayback) |
| WY | T1 | respondida | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | US-WY-P5-1-001 Wyoming Legislature: W.S. 39-12-101 Preemption by state (Title 39 chapter 12 Income Tax) |

Federal e transversais (Step 4):

| Pergunta | Tema | Status | Confiança | Registro |
|---|---|---|---|---|
| US-MQ-01 | Tax year | answered | 88% | US-FED-013 |
| US-MQ-02 | Currency, minor units and rounding | answered | 90% | US-FED-001 |
| US-MQ-03 | Official languages and what fixes document language (G-LANG) | open | - | - |
| US-MQ-04 | Sub-national wrinkle: confirm the T4 discriminator | answered | 90% | US-FED-012 |
| US-MQ-05 | Devolved payroll-adjacent domains (federal list) | open | - | - |
| US-MQ-06 | Indexation (federal) | answered | 90% | US-FED-026 |
| US-MQ-07 | Collective agreements | answered | 90% | US-FED-018 |
| US-MQ-08 | Oracle for Stage 9b | answered | 90% | US-FED-027 |
| US-MQ-09 | Third-party filing provider (SIR) | answered | 90% federal; owner limb by owner decision | US-FED-008 |
| US-MQ-10 | Multi-state domain | answered | 80% | US-MULTI-001 |
| US-MQ-11 | Validation exemptions (owner) | answered | n/a | - |
| US-MQ-12 | Employee population in scope | open | - | - |
| US-MQ-13 | Jurisdiction priority (owner) | answered | n/a | - |
| US-MQ-14 | Package shape (owner) | answered | n/a | - |

## 3. Respostas seladas e as fracas

**Respondidas (52, eram 34):** federais US-MQ-01, 02, 04, 06, 07, 08, 09, 10 (pesquisa) e US-MQ-11, 13, 14 (decisão do usuário, agora com linhas `US-OWN-001..003` no registro); estaduais (41): AK, AL, AR, AZ, CA, CO, CT, DC, DE, FL, GA, HI, IA, ID, IL, KS, KY, MA, MD, MI, MO, MS, MT, NC, ND, NE, NV, NY, OH, OK, OR, PA, RI, SC, SD, TN, TX, WA, WI, WV, WY. Novas na tentativa 4: AK, AL, AZ, DC, ID, IL, KY, MA, MI, MO, NV, OH, SC, TN, TX, WI, WV, WY. "Respondida" aqui não é selada; o mandato como um todo continua aberto. Critério mecânico: toda parte tem pelo menos uma linha `active` no registro; isso reabriu MN parte 6, NJ parte 6 e ME parte 4, que o agente 2 tinha dado como fechadas.

**Critérios de selo (tentativa 4):** (1) zero `pending_research`: FALHA (13 abertas); (2) todo `register_id` resolve no registro: PARCIAL (US-MQ-11/13/14 agora resolvem; FALHA em CT e KS); (3) `mandate_status` = sealed: não alterado.

**Fracas (confiança < 90% ou frágil):**
- **US-MQ-10 (multi-estado), 80%:** a mais fraca; vale como mapa de roteamento, não como regra fechada por estado.
- **US-MQ-01 (ano fiscal), 88%:** ano civil comprovado no federal; o lado estadual é inferência. Cita US-FED-005, hoje `superseded` por vínculo errado (US-FEDR3-006); a resposta se sustenta em US-FED-013/015/016 ativas.
- **US-MQ-02, 04, 06, 07, 08, 09 (federal), 90%:** no limite; US-MQ-09 vale para o federal, a escolha do provedor é decisão de negócio (Marko). US-MQ-02/04/09 citam US-FED-005/029, também `superseded` por vínculo errado.
- **Estaduais sem número:** 29 em Medium-High (AK, AR, CO, CT, DE, FL, GA, HI, IA, KS, MA, MO, MS, MT, NC, ND, NE, NV, NY, OH, OK, OR, PA, RI, SC, SD, TN, WA, WV). Fora disso: AL Medium; AZ Medium; CA High (part 6 Medium-High); DC Medium; ID High (part 6: 90%); IL High (92%); KY High (90%); MD High; MI High (rates of the 23 self-administering cities: annex data); TX High (statutes); Medium (C-42 content); WI Medium-High (part 2 Medium); WY High. Nenhum tem percentual: tratar como abaixo de 90% até o auditor revalidar.
- **CT e KS:** respondidas, mas o rebuild do registro perdeu as 12 linhas do shard `mandate-P5-W3A-r2.csv` (US-CT-P5-2-001/002, US-KS-P5-2-001..004, US-LA-P5-2-001..005, US-NV-P5-2-001); sem reinclusão o critério 2 falha.
- **Apoiadas em cópia Wayback na base do tier:** DE, KS, MT, NE entre as respondidas. KS: edição 06/21 do KW-100, tabelas 2026 ainda abertas. RI: só o lado estadual verificado; RI-006 é MANUAL.
- **Ausência local "não verificada"** (parte 2): quase todos os T3 — a camada local não foi localizada, mas não há frase oficial de ausência.

## 4. Perguntas ainda abertas e URLs bloqueadas

Tipos de trava: **ACESSO** = a fonte está identificada e só um host bloqueado/geo/antirrobô/inalcançável impede (download manual ou cópia alcançável fecha); **PESQUISA** = fonte ainda não identificada ou censo incompleto; **REGISTRO** = defeito de merge/supersedes do agente 2; **DECISÃO** = decisão do usuário. **Só ACESSO: IN, MN, NH, NJ, NM, UT, VA, VT.**

**Federais (3):**

| Pergunta | O que falta | Trava | URL |
|---|---|---|---|
| US-MQ-03 | Censo de avisos em idioma primário nos 45 estados restantes (6 de 51 lidos: CA, NY, MN, DC, NJ, IL); eixo de participação no emprego (G-LANG); texto estatutário da CA | PESQUISA (45 estados e G-LANG) + ACESSO (CA) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=2810.5 (gated) |
| US-MQ-05 | Data de renovação do IWO OMB 0970-0154 (cabeçalho vence 2026-08-31; renovação ICR 202607-0970-002 pedida, resultado não confirmado); taxa PFML 2026 de ME; ausência de levies de transporte/workforce fora de NY/OR | ACESSO (a, b) + PESQUISA (c) | https://www.reginfo.gov/public/do/PRAViewICR?ref_nbr=202607-0970-002 ; https://acf.gov/sites/default/files/documents/ocse/omb_0970_0154.pdf ; https://www.maine.gov/paidleave/docs/2026/employers/faq/employerFAQenglish.pdf (geo-block) |
| US-MQ-12 | Assinatura do usuário na matriz de populações especiais L10 (pesquisa concluída: Pub. 15-A, Pub. 15, Pub. 54 lida inteira) | DECISÃO (nem acesso nem pesquisa) | nenhuma |

**Estaduais (10):**

| UF | Pergunta | Parte | O que falta | Trava | URLs |
|---|---|---|---|---|---|
| IN | US-MQ-35 | 6 | Lei de demonstrativo de pagamento IC 22-2-2-8 (só cópia tier C, US-INR3-007 provisória) | ACESSO | https://iga.in.gov/laws/2025/ic/titles/22 ; https://iga.in.gov/ic/2026/Title_22/Article_2.pdf?download=1 |
| LA | US-MQ-38 | 6 | Lei de prevailing wage R.S. 38:2301 (revogação de 1988) não lida; linha de POA do UI US-LA-P5-2-005 ausente do registro reconstruído | ACESSO + REGISTRO (shard não mesclado) | https://law.justia.com/codes/louisiana/2011/rs/title38/rs38-2301/ (US-LAR3-003, gated); legis.la.gov Law.aspx 38:2301 (host não resolve) |
| ME | US-MQ-41 | 4 | Parte 4 sem linha ativa: US-FEDR3-011 (gated) substitui a ativa US-ME-P5-1-002; taxa PFML 2026 não lida | REGISTRO + ACESSO | https://www.maine.gov/paidleave/docs/2026/employers/faq/employerFAQenglish.pdf (geo-block) |
| MN | US-MQ-43 | 6 | Pay statement 181.032, prevailing wage 177.42 e rota de agente do UI só em linhas MANUAL (US-MNR3-003/-004/-005) | ACESSO (leitura literal; muro antirrobô no uimn) | https://www.revisor.mn.gov/statutes/cite/181.032 ; https://www.revisor.mn.gov/statutes/cite/177.42 ; https://mn.gov/uimn/employers/info-agents/agent-self-service/ |
| NH | US-MQ-50 | 6 | POA do UI nhes0041; ausência de prevailing wage só MANUAL; índice do Título XXIII gated | ACESSO | https://mm.nh.gov/files/uploads/nhes/documents/nhes0041.pdf ; https://gc.nh.gov/rsa/html/XXIII/XXIII-mrg.htm |
| NJ | US-MQ-51 | 2, 6 | 2: imposto de folha de Jersey City (N.J.S.A. 40:48C-14) e Newark só em linha MANUAL; 6: pay statement US-NJ-P5-2-001 e calculadora US-NJR3-006 MANUAL | ACESSO | https://jerseycity.hosted.civiclive.com/payrolltax ; https://pub.njleg.gov/Bills/2016/AL17/35_.HTM ; https://nj-newark.civicplus.com/647/Payroll-Tax ; https://www.nj.gov/treasury/taxation/businesses/payroll/index.shtml |
| NM | US-MQ-52 | 6 | NMSA 50-4-2 (só secundária), POA do UI, texto do Public Works Minimum Wage Act | ACESSO | https://www.dws.nm.gov/portals/0/dm/business/power_of_attorney.pdf ; https://www.dws.nm.gov/Portals/0/DM/LaborRelations/Public_Works_Minimum_Wage_Act_Policy_Manual_Active.pdf ; nmlegis.gov (WAF) |
| UT | US-MQ-64 | 6 | Pay statement 34-28-3, TC-737, POA do DWS | ACESSO | https://le.utah.gov/xcode/Title34/Chapter28/34-28-S3.html ; https://tax.utah.gov/forms/current/tc-737.pdf ; https://jobs.utah.gov/ui/employer/Public/Forms/POA.pdf |
| VA | US-MQ-65 | 6 | Formulário/processo de agente do VEC | ACESSO | https://www.vec.virginia.gov/employer-self-service |
| VT | US-MQ-66 | 6 | Texto oficial do SOS da regra 24-090-003 Sec. VI; linha de tabelas US-VT-P5-1-003 MANUAL | ACESSO | https://law.cornell.edu/regulations/vermont/24-003-Code-Vt-R-24-090-003-X (espelho MANUAL); URL oficial sos.vermont.gov não registrada |

Padrão: das 13, **8 só de acesso** (IN, MN, NH, NJ, NM, UT, VA, VT), 2 de acesso + defeito de registro (LA, ME), 2 federais com pesquisa faltante (US-MQ-03, US-MQ-05 parte c) e 1 de decisão do usuário (US-MQ-12). Nenhum veredito de tier depende de parte aberta, exceto a ponta local de NJ (T3 provisório, candidato a T4).

**Defeitos de registro do agente 2 (nenhuma resposta sela em cima deles):** (1) remesclar `_register-shards/mandate-P5-W3A-r2.csv` (12 linhas perdidas; trava CT, KS e LA parte 6); (2) vínculos `supersedes` errados: US-FEDR3-005 -> US-FED-030, US-FEDR3-006 -> US-FED-005, US-FEDR3-007 -> US-FED-029 (instrumentos diferentes) e US-FEDR3-011 (gated) -> US-ME-P5-1-002 (estatuto ativo); (3) linhas MANUAL que substituem ativas: US-MNR3-004 -> US-MN-P5-1-004, US-MNR3-005 -> US-MN-PAY-001, US-NJR3-001 -> US-NJ-P5-1-005.

**Bloqueios do Chrome (`BLOQUEIOS-CHROME.md`, 29/10):**
- Tipo 1, permissão da extensão: mass.gov, michigan.gov, maine.gov, dor.mo.gov, laworks.net, marylandcomptroller.gov, revenue.state.mn.us, revenue.ky.gov, dol.georgia.gov, tax.hawaii.gov, flsenate.gov. No teste da sessão principal, mass.gov, michigan.gov, revenue.ky.gov, marylandcomptroller.gov, revenue.state.mn.us, dor.ms.gov, tax.hawaii.gov, dol.georgia.gov e tax.illinois.gov abriram e foram lidos (o "Permission denied" foi só nas abas dos agentes).
- Tipo 2, bloqueio por país/antirrobô (não contornar): dew.sc.gov e twc.texas.gov (CloudFront geo-block), maine.gov (geo), dor.mo.gov (Incapsula), louisiana.gov (Cloudflare), azdor.gov, ncleg.gov, leg.state.nv.us, detr.nv.gov, vec.virginia.gov, gc.nh.gov, jobs.utah.gov, dwd.wisconsin.gov, floridarevenue.com. Saída: VPN com saída nos EUA (decisão do usuário; a Pritunl #13036 é interna e não serve, a princípio) ou colega nos EUA baixar.
- Tipo 3, não carregam nesta rede: in.gov, tax.idaho.gov, ksrevenue.gov, revenue.nebraska.gov, mtrevenue.gov e legislaturas (WV, WI, VT, UT, RI, OR, OK, OH).
- PDFs que o Chrome não lê: NYS-50-T-NYC, ND UI 2026, OH WHT 2026, PA llc-2, NM FYI-104, UT Pub 14, DE PFL, EDD.

**Rotas para selar (do mandato, tentativa 4):** (a) o usuário abre as URLs de ACESSO num navegador normal e salva as páginas em `00-official-sources/pdfs/<UF>/`; o agente 2 regradeia; (b) o agente 2 corrige os defeitos de registro acima (o `supersedes` do NV já foi corrigido em US-NVR3-001); (c) o usuário assina a matriz US-MQ-12; (d) o usuário decide o corte de escopo de US-MQ-03 (aceitar a resposta proposta em R3-FED ou mandar o censo dos 45 estados) e a parte (c) de US-MQ-05 (aceitar "nenhum localizado" para levies de transporte/workforce ou mandar o censo). A rota antiga de aceitar as listas federais de TDI/PFML como prova de ausência **não foi aceita**; o agente 2 já levantou provas de ausência da parte 4 por estado para AL, AZ, KY, MO, TX, WI e WV.

## 5. Notas de método

- **Wayback:** onde o site oficial não carrega, a cópia Wayback da edição mais próxima de 2026 é tratada como primária *para a edição mostrada* (passada 3 de 29/10). O registro (800 linhas na contagem de 29/10; não recontado nas 902 atuais) tinha 225 linhas ligadas a Wayback/cópia; a data da cópia vai na linha e uma fonte vigente de 2026 mais nova prevalece. Linhas `superseded` por cópia velha (ex.: US-KS-001, US-ID-001/002, US-IL-001, US-MT-PIT-001) não são citáveis.
- **Leituras com script antes da proibição (29/10):** G1, G4, G5 e G6 usaram `javascript_tool` antes do aviso; G1 e G6 alteraram texto para passar pelo filtro "[BLOCKED: Cookie/query string data]". Só G6 marcou as linhas. Regra vigente: viram pista, o auditor revalida 100% dos números (F44), as alteradas viram MANUAL. No registro: US-TX-PIT-001, US-TX-SUI-002, US-TX-SUI-003 (uma saída alterada para passar pelo filtro, texto igual), US-TX-LAB-001, US-VA-SUI-002, mais US-CA-EDD-002/003 (pdf.js). **Pendente do usuário:** aceitar essas leituras ou refazer com `get_page_text`.
- **Linhas rebaixadas na conferência:** o registro tem 902 linhas (tentativa 4): 712 ativas, 114 superseded, 46 MANUAL, 22 gated, 4 partial, 2 provisional, 2 historical. A conferência mecânica da tentativa 4 reabriu MN parte 6 e NJ parte 6 (apoiadas só em MANUAL) e ME parte 4 (a ativa foi substituída por uma gated). De tentativas anteriores: US-IL-P5-1-002 (verificador divergente), US-PA-P5-2-001 (3,07% não está na página citada), US-ME-P5-2-008 (formulário é UC-28 rev. 09/2013, não 2018), US-KY-P5-1-001 (figuras 3.360/117,60/104,65 fora do arquivo citado), US-WV-P5-1-004 (lista de formulários fora do texto).
- **Fontes secundárias:** linhas de fornecedor (US-FIL-004, 022 a 027), resumos de busca e espelhos (Cornell, employmentlawhandbook) não sustentam número; não entram como fonte.
- **Revisão:** nada vai ao Marko. As revisões usam a ferramenta de cross-check do Research Pipeline. Nada foi enviado a Drive, monday, ticket ou e-mail.
- **Pasta:** BASE em `Research Pipeline/USA/US-compliance/` (não `~/mercans-pipeline/US-compliance`); os `_shared-appends/` ficam como proposta para a frente Pipeline.

## 6. O que mudou desde 29/10

| Marco | Respondidas | Abertas | Censo T1 / T3 / T4 / sem classe |
|---|---|---|---|
| Esqueleto (29/10) | 0 | 65 | T4 provisório |
| Tentativa 1 (29/10) | 3 (MQ-01, 04, 07) | 62 | 9 / 32 / 5 / 5 |
| Tentativa 2 (29/10, passadas 2 Chrome e 3 Wayback) | 7 (+MQ-06, 08, 13, 14) | 58 | 9 / 34 / 5 / 3 |
| Tentativa 3 (30/10, passadas 4 e 5, registro de 800 linhas) | 34 | 31 | 9 / 33 / 9 / 0 |
| Tentativa 4 (30/10, rodada 3 do agente 2, registro de 902 linhas) | 52 | 13 | 9 / 32 / 10 / 0 |
| Tentativa 5 (30/10, P6, P7, P8, registro de 1.161 linhas) | 63 | 2 | 9 / 31 / 11 / 0 |
| Tentativa 6, passo 1 (01/11, P9-MERGE, US-OWN-006/007) | 62 | 3 (CT, MS, OR reabertas) | 9 / 31 / 11 / 0 |
| Tentativa 6, passo 2 (02/11, US-CTP10/ORP10/MSP10, registro de 1.303 linhas) — **SELADO** | 65 | 0 | 9 / 31 / 11 / 0 |

- Tentativa 4: +18 jurisdições respondidas (AK, AL, AZ, DC, ID, IL, KY, MA, MI, MO, NV, OH, SC, TN, TX, WI, WV, WY); WV T3 provisório -> T4 verificado (W. Va. Code 8-13-13 [US-WVR3-001], Charleston [US-WVR3-002]); tiers por domínio inalterados; NJ segue T3 provisório.
- Linhas `US-OWN-001..004` registram as decisões do usuário; US-MQ-11, 13 e 14 passam a resolver no registro. Correção do NV (`supersedes`) feita em US-NVR3-001. Defeitos novos: shard P5-W3A-r2 perdido no rebuild e vínculos `supersedes` errados (seção 4).
- Tier geral passou de "provisório" para **T4 confirmado** (cita US-FED-012, US-VA-PIT-002/003, US-FED-014); novo domínio `employer_payroll_levies` (T3), ambos desde a tentativa 3.
- Decisões do usuário de 29/10 registradas: 51 jurisdições, perguntas não reduzidas; MQ-13 em ondas 1/2/3; MQ-14 pacote único dos EUA; MQ-11 nenhum estado fora da validação; provedor de filing fora do build. Inalteradas na tentativa 4 (rota d não aceita, MQ-12 não assinada).
- Teste na sessão principal: 9 domínios do tipo 1 abrem e leem; mass.gov (Withholding Tax Guide, Aug 2026) lido; maine.gov e twc.texas.gov confirmados como geo-bloqueio.
- Pasta `skills-build/` irmã não criada (escrita restrita à BASE); pastas de estágio 01 a 09 intactas.

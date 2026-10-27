# Matriz de cobertura: erros da validação FR × pipeline v2.11

**Data:** 2026-10-17 · **Frente:** Pipeline · **Pedido:** janela geral (brain-service-49), a pedido do usuário.
**Pergunta:** o pipeline atual impede que os erros encontrados na validação da França se repitam num país novo?

## Como foi feito
- **Erros:** `fr-research-validation/fr-research-validation/docs/defect-drafts/INDEX.md` (D-01..D-19), revisões em `docs/review/` (CCG F-01..F-29, WTC/DD/Payslip/SIR, Specs A/B, triagem DSN-Val SD-01..SD-05, Teste 0), `TEST-DESIGN-CORRECTIONS.md` e o catálogo `revisoes/2026-10-15-licoes-aprendidas/detalhado/licoes-fr-research-validation.md` §2.
- **Pipeline (lido no disco em 2026-10-17):** `~/mercans-pipeline/mercans_pipeline_v2_9.sh` (cabeçalho v2.11, 4.289 linhas), `shared/*/` (código dos checks), `shared/PRESUBMISSION_AUDIT.md`, `shared/country_failure_log.md` (F40–F47), `IMPROVEMENT_LOG.md`.
- **"Coberto" só com prova no código.** Cada F/C citado foi lido no arquivo e na linha indicados. Nome de check não conta como prova.
- **Testes negativos rodados hoje** (todos sobre cópias temporárias; nada no pipeline foi alterado):

| Teste | Comando (resumo) | Resultado em 2026-10-17 |
|---|---|---|
| C34/C35/C36 | `spec-builder/tests/test_mutations.py` sobre FR-DSN-002 + `neodes_ct2026.json` | ALL EXPECTATIONS MET (corte para 2.500 → C34 FAIL TRUNCATED; SIREN alterado → C36 FAIL e C35 FAIL CSL-11) |
| C37 | `validation-suite-template/tests/test_mutation.py FR-compliance/_validation` | ALL EXPECTATIONS MET (CSG 6,80 → 6,70 %: 275 resíduos inexplicados, 275 regressões, FAIL nas bases raw e law) |
| C38/C39 | `validation-suite-template/tests/test_c38_c39.py <cópia de FR-CCG-001-v1.0.docx>` | ALL EXPECTATIONS MET. **Na CCG FR emitida (v1.0), o C38 reprova já na linha de base: 3 divergências** (ver "Achados fora do pedido") |
| C40/C41 | `research-checks/tests/test_research_checks.py` | 8/8 ok |
| C42–C46 | `consistency-checks/tests/test_consistency_checks.py` | 7/7 ok |
| C47 | — | **Não há teste negativo no repositório** (`shared/release/` não tem `tests/`). Há só a medição registrada em `IMPROVEMENT_LOG.md:437-441` |

## Regras de leitura da matriz
- **Executável:** o check roda como código **e bloqueia** (`exit 1`). Os checks C34–C47 bloqueiam (`mercans_pipeline_v2_9.sh:3833-3836`, `:3847-3850`, `:3984-3986`, `:4184-4186`, `:4226-4229`). **C1–C33 não bloqueiam:** `:3862` "Don't halt on BLOCKED — let user decide" (decisão D2 de 2026-10-07: "até o piloto").
- **Teste 0 (C39) e o auditor adversarial são uma rede amostral** (40 afirmações; o auditor só existe no caminho de agentes). Eles podem pegar qualquer erro, mas não garantem nenhum erro específico. Por isso **não contam como cobertura** de um erro; aparecem só como "rede".
- **Total:** existe um mecanismo executável e bloqueante que reprova essa classe de erro qualquer que seja o conteúdo, e um teste negativo prova isso. **Parcial:** o mecanismo existe, mas depende de o conteúdo cair nele (um caso de teste, uma linha da matriz, um validador do país), ou cobre só parte da classe. **Nenhuma:** nada executável que reprove.
- **Pensando num país novo (ex.: Portugal):** hoje só a França tem plugin (`shared/spec-builder/mercans_spec/countries/fr.py` é o único arquivo da pasta), norma legível (`FR-compliance/04-reports-spec/_data/neodes_ct2026.json`) e motor (`FR-compliance/_validation/`). Sem eles, C34 e C35 dão **SKIP**, e SKIP não reprova (`spec_checks.py:118-120`, `:284`; o checklist do Stage 3 aceita SKIP, `mercans_pipeline_v2_9.sh:1387`).

## Lacunas estruturais citadas várias vezes (base das linhas abaixo)
- **L-A. C46 aprova sem nenhuma etiqueta.** `consistency_checks.py:446-472`: com o arquivo de fatos presente e 0 etiquetas `[[FACT:]]`, o status é PASS, só com uma nota. O C32 faz o mesmo (`mercans_pipeline_v2_9.sh:3459-3460`). Na FR, 0 etiquetas e C46 PASS (`IMPROVEMENT_LOG.md:525`). **A coerência de valores entre artefatos não é verificada na prática.**
- **L-B. C40 confere a forma, não o conteúdo.** `research_checks.py:101-152` exige as 13 linhas (`:41-55`), tratamento com 40 ou mais caracteres, os 3 efeitos não vazios ("none: <razão>" passa), fonte com `register_id` e URL, e `ccg_location` existente. Não confere se o tratamento está certo. Não há linha para regimes locais (Alsace-Moselle/DOM), porte ou tipo de empregador, nem mudança de taxa no meio do ano.
- **L-C. Os casos do C37 não estão ligados à matriz C40 nem aos exemplos do CCG.** `run_suite.py:155-234` mede só os casos que existem em `tc.json`. O "inclua cada exemplo resolvido do CCG" está só no README (`validation-suite-template/README.md:71`). O caminho `official_examples` (país sem motor) nunca rodou num país real (`IMPROVEMENT_LOG.md:295`).
- **L-D. C38 só lê o Módulo 12 e só refaz a aritmética.** O módulo padrão é `("Module 12",)` (`worked_examples_check.py:202`, `:216`), e o Stage 9 não passa `--module` (`mercans_pipeline_v2_9.sh:3633-3634`). Um operando errado com conta certa passa. Exemplos das specs não são lidos.
- **L-E. Nenhuma checagem cruzada de código de rubrica, flag de tributação ou lado (EE/ER) entre WTC, DD, CCG, specs e Payslip.** O C27 é o mais próximo: compara a coluna L da spec com os termos do DD, é MANUAL e não bloqueia, e lê um DD de nome fixo `{CODE}-DD-001-v1.0.xlsx` (`mercans_pipeline_v2_9.sh:2928-2932`).
- **L-F. O Payslip não tem check de conteúdo.** C21/C26 conferem só as abas. O conteúdo obrigatório está só no prompt (`mercans_pipeline_v2_9.sh:2206`). O Teste 0 não amostra o Payslip: `T0_ARTS` é `CCG,WTC,DD[,RSPEC]` (`:3975-3976`).

---

## Matriz

Abreviações: Est. = estágio que falhou (1 Pesquisa/escopo; 1c CCG; 3 Specs; 4 DD; 5 WTC; 6 SIR; 7 Payslip; Design; Entrega/Release); SA = `shared/`; SH = `mercans_pipeline_v2_9.sh`.

### A. Defeitos D-* da research (nossos)

| ID | Erro | Est. | F/C que cobre (arquivo:linha) | Executável? | Teste negativo? | Cobertura | O que falta | v2.12 (17/10) |
|---|---|---|---|---|---|---|---|---|
| D-01 | Apec até 8 PMSS (certo: 4 PSS), igual em CCG, WTC, skill e params | 1 | F41/**C37** (`SA/validation-suite-template/run_suite.py:155-234`); F44/C41 (`SA/research-checks/research_checks.py:173-249`, só data e frescor do registro); F45/C46 (L-A) | C37 sim; C46 aprova sem etiqueta | C37 sim (mutação de taxa → FAIL) | **Parcial** | Só é pego se houver motor independente **e** um caso acima de 4 PMSS (L-C). Sem motor, um erro consistente passa em C32/C46 (L-A). Falta C46 reprovar valor sem etiqueta e cada teto do registro ter caso por banda (F51/C51) | **Parcial** — C46+ faz uma correção chegar a todos os artefatos, mas o valor errado no fato continua coerente; detectar ainda exige motor + caso acima do teto (F51/C51 não aprovado) |
| D-03 | Net social com a doutrina de 2023 (patronal L911-1 somada); 2027 não distinguido | 1 | C37 (pegou na FR); C41 `effective_from`/`effective_to` (`research_checks.py:190-194`) | Sim | C37 sim; C41 sim (linha sem `effective_from`) | **Parcial** | C41 olha só a linha do registro, não se a regra no texto é a da versão em vigor. A varredura começa em 1º de janeiro do ano da build (`:234`) e não pega doutrina antiga. Regra com troca de data (2026/2027) sem constante datada (F novo) | **Parcial** — C40 `mid_year_rate_change` + C41+ (data da troca escrita) forçam a regra datada; a doutrina antiga só cai no C37 |
| D-07 | Prorrateio do teto no tempo parcial como automático; renúncia e heures complémentaires ausentes | 1 | F43/C40 linha `part_time` (`research_checks.py:45`); C37 (TC23/TC24) | Sim | C40 sim (linha vazia → FAIL) | **Parcial** | L-B: C40 obriga a pergunta, não a resposta certa. L-C: sem caso de tempo parcial, C37 não mede | **Parcial** — C69 obriga ao menos 1 caso de tempo parcial na suíte; a opção de renúncia continua dependendo do caso |
| D-08 | FNAL citando CSS L834-1 revogado (4×) | 1 | C41 (status da linha é declarado por quem escreve, `:186`); C30 (só agregadores, não bloqueia) | C41 sim, mas não vê revogação | Não para revogação | **Nenhuma** | Check novo: cada citação do registro com URL da versão consolidada e estado "em vigor" lido na build; varrer o texto dos artefatos atrás de artigos fora do registro (G-22; sem F48–F66 correspondente → F novo) | **Parcial** — C70: citação fora do registro ou de linha marcada revogada reprova (testado); revogação não registrada passa |
| D-11 | CPF-CDD 1 % ausente; CDD→CDI não isento desde 2022 | 1 | C40 linha `fixed_term_contract` (`:44`); C37 (TC46a/b) | Sim | C40 sim | **Parcial** | L-B e L-C: falta exigir ao menos 1 caso do C37 para cada linha "answered" do C40 | **Parcial** — C69 obriga caso para a linha `fixed_term_contract`; o caso pode não exercer o CPF-CDD |
| D-12 (research) | AT/MP: divisor da doença 3/91,25 no lugar de 1/30,42; teto do ganho líquido do dia 29 ignorado | 1 | C40 linha `work_accident_occupational_disease` (`:49`); C37 (TC45c) | Sim | C40 sim | **Parcial** | Igual a D-11 | **Parcial** — C69 obriga caso para AT/MP |
| D-17 | Não residente fiscal coberto pela seguridade: CSG/CRDS em vez de COTAM 5,50 % | 1 | C40 linha `non_resident_employee` "(tax and social security)" (`:43`, efeitos `:56`, `:129-131`); C31 (`SH:3285-3309`, só IR, MANUAL, não bloqueia) | C40 sim; C31 não | C40 sim | **Parcial** | `effects.social_security = "none: ..."` passa. Falta exigir fonte específica de seguridade para não residente e caso no C37 (L-B, L-C). O C31 continua só no IR | **Parcial** — C40+ exige fonte que cubra seguridade do não residente (testado) + C69 caso + C31 (MANUAL) |
| D-19 | Presidente de SAS sem Apec/CDS (inconclusivo) | 1 | C40 linha `officers_without_employment_contract` (`:46`) | Sim | C40 sim | **Parcial** | Defeito ainda inconclusivo; a linha existe, mas aceita qualquer tratamento com fonte | **Parcial** — C69 caso para dirigentes; defeito inconclusivo |

### B. Revisão do CCG (F-xx) e achados do Teste 0

| ID | Erro | Est. | F/C que cobre (arquivo:linha) | Executável? | Teste negativo? | Cobertura | O que falta | v2.12 (17/10) |
|---|---|---|---|---|---|---|---|---|
| CCG F-04 / WTC F-06 | Prévoyance patronal somada ao líquido tributável; o Mod. 3 Step 5 dizia o contrário (mesma regra, duas versões) | 1c | F45/C32 e C46 (L-A); verificador semântico só reporta (`SH:3316-3317`) | Aprova sem etiqueta | C46 sim (etiqueta ≠ fato), mas não sem etiqueta | **Nenhuma** | L-A + L-E: coerência de regra/flag entre módulos e artefatos (F50/C50 base legal por flag) | **Parcial** — C50 (flag de tributação do WTC = crosswalk, com base legal) + C46+; a versão em prosa do CCG não é comparada |
| CCG F-02 / WTC F-04 | CDS 0,016 % também no lado do empregado (boilerplate em dezenas de células) — S1 | 1c/5 | Nenhum check de lado EE/ER; C46 (L-A) | Não | Não | **Nenhuma** | Boilerplate do WTC gerado do arquivo de fatos (C46 obrigatório) + check de lado EE/ER × tabela do CCG (L-E) | **Parcial** — C50 reprova item ER descrito "each side / employee and employer" no WTC (testado); a tabela do CCG não |
| WTC F-05 | CDS dentro do perímetro da RGDU | 5 | Nenhum | Não | Não | **Nenhuma** | Igual a F-02 (perímetro de redução como fato com etiqueta) | **Parcial** — C50 se o perímetro de redução for flag do crosswalk |
| CCG F-05 | Exemplo da RGDU em tempo parcial com o SMIC de tempo integral (C 0,3981 × 0,3751) | 1c | F42/C38 (`worked_examples_check.py:114-211`) | Sim | Sim (mutação R/T) | **Parcial** | L-D: conta certa sobre operando errado passa. Falta operandos etiquetados `[[FACT:]]` + o exemplo virar caso do C37 (L-C) | **Parcial** — C38 kind F só testa taxas; o SMIC de tempo integral como operando passa; C69 obriga o exemplo a ser caso do oráculo |
| CCG F-11 | Mod. 9.1: líquido tributável sem os 485,00 (PAS subestimado em 48,02) | 1c | C38 só no Módulo 12 (`:202`, `:216`; `SH:3633-3634`) | Não para o Mod. 9 | Não | **Nenhuma** | C38 sobre todos os módulos com tabela de cálculo (L-D) | **Nenhuma** — exemplo em prosa no Mod. 9.1: C38 `--module all` não o lê (conferido nas cópias arquivadas); C69 só mapeia exemplos do Mod. 12 |
| CCG F-13 | Base da CSG sem a prévoyance de 1,50 % (Mod. 6.3 Ex. 1/3; Mod. 12 Ex. 5) | 1c | C38 (só a parte do Mod. 12, e só se a base for expressão) | Parcial | Sim | **Parcial** | L-D | **Parcial** — C38 em todos os módulos |
| CCG Ex. 3 (Mod. 6.3) | Teto de dezembro 4.005 × 4.060 com regularização progressiva | 1c | C38 não lê o Mod. 6 | Não | Não | **Nenhuma** | L-D | **Nenhuma** — exemplo em prosa (como F-11) |
| CCG F-12/F-14/F-10 (F-20 retirado) | Média de 3 meses com bônus fora da janela; divisor 151,67 arredondado; teto 3.203,84 × 3.203,85 | 1c | C38 tipo E com tolerância de 1 unidade (`:17-19` do docstring) | Sim | Sim | **Parcial** | Convenção de arredondamento/divisor não declarada por contribuição (F64/C64) | **Parcial** — sem mudança (F64 não aprovado) |
| CCG F-29 | Exemplo da Moselle fecha só com taxa de aprendizagem 0,68 % (certo: 0,44 %) | 1c | C38 (conta consistente com taxa errada passa); C46 (L-A) | Não para a taxa | Não | **Nenhuma** | Operando como etiqueta `[[FACT:]]` (L-A, L-D) | **Total** — C38 kind F: taxa de exemplo que não é fato reprova (testado com 0,68 % × 0,44 %) |
| CCG F-16 | Assiette minimale (seção do BOSS de 24/07/2026) ausente | 1 | F44/C41 varredura final (`research_checks.py:217-246`) | Sim | Sim (varredura ausente ou com mais de 14 dias → FAIL) | **Parcial** | A varredura é obrigatória, mas não se exige uma por autoridade do registro (BOSS, URSSAF, BOFiP...). Falta "1 varredura por autoridade presente no registro" | **Parcial** — C41+: uma varredura por autoridade do registro (testado); a qualidade da busca segue com o agente |
| CCG taxe sur les salaires | Só as taxas; faltavam os limites de 2026 (9.229 / 18.423) | 1 | Nenhum | Não | Não | **Nenhuma** | Fato do tipo "faixa" no `facts.schema.json` exigindo os limites, com vigência | **Nenhuma** — sem mudança |
| CCG F-21 / Teste 0 TEST0-F2 | "Três anos de salário" (certo: 3 × PASS) — CCG corrigido, WTC/DD não | 1/5/4 | C46 (L-A); rede: C39 pegou | Aprova sem etiqueta | — | **Nenhuma** | L-A: o mesmo fato com etiqueta nos 3 artefatos | **Nenhuma** — regra em prosa ("three years' pay") sem número: o C46+ não a vê |
| Teste 0 TEST0-F1 | WTC 62876: IJ de AT "totalmente tributável" (certo: 50 %, CGI 81 8°); CCG certo | 5 | C46 (L-A); rede: C39 pegou | Aprova sem etiqueta | — | **Nenhuma** | L-E: flag de tributação WTC × regra do CCG (F50/C50) | **Total** — C50: "fully taxable" contra flag parcial reprova (testado) |
| CCG F-23 / WTC F-14 | Minimum garanti 4,22 (2025); certo 4,25 a partir de 01/01/2026 e 4,35 a partir de 01/06/2026 (arrêté) | 1 | C41 (`effective_to` vencido com linha ativa → FAIL, `:193-194`; `verified_on` ≤ 120 dias) | Sim | Sim | **Parcial** | Pega se o valor estiver no registro; o número no artefato não está ligado ao registro (L-A) | **Parcial** — C46+ pega o valor etiquetado ≠ fato; um 4,22 escrito sem etiqueta não é valor de fato e passa |
| CCG F-24 | Mínimo protegido 651,69 sem "a partir de 01/04/2026" | 1 | C41 exige `effective_from` no registro, não no texto | Sim (registro) | Sim | **Parcial** | Constante datada no texto e no design para regra que muda no ano (net social, grade PAS 01/05, SMIC 01/06) — F novo | **Total** — C41+: fato com início no meio do ano exige a data no CCG / design (testado) |
| CCG F-25/F-26, F-06, F-28 | Conteúdo atribuído à lei errada (Loi 2026-492/534); decreto incompleto da RGDU; limite em espécie citado no CT em vez do Décret 85-1073 | 1 | Nenhum (C30 só agregadores) | Não | Não | **Nenhuma** | Igual a D-08 (citação lida e em vigor) | **Parcial** — C70: artigo citado fora do registro reprova; se o próprio registro estiver errado, passa |
| CCG F-17/F-18 | Tolerância do BOSS não citada; norma DSN 2027 (CT2027.1.2) não antecipada | 1 | C41 varredura (só o ano da build, `:234`) | Sim | Sim | **Parcial** | A varredura não pede "norma do ano seguinte publicada?" | **Parcial** — C41+ `next_year` obrigatório (F-18, testado); F-17 não |
| CCG F-19 | "Versão 1.3" dentro de v1.0; 4 "Released" sem mudar o nome | Entrega | F45/**C43** (`consistency_checks.py:257-295`) | Sim | Sim ("cover says Version 1.3" → FAIL) | **Total** | — | **Total** — C43 (sem mudança) |

### C. Revisão do WTC / DD / Payslip / SIR

| ID | Erro | Est. | F/C que cobre (arquivo:linha) | Executável? | Teste negativo? | Cobertura | O que falta | v2.12 (17/10) |
|---|---|---|---|---|---|---|---|---|
| WTC F-02/F-03 | Agirc-Arrco com código 105 (só regularização anterior a 2025); certo 131/132 | 5 | C35 só valida o Sample File das specs, não o WTC (`spec_checks.py:118-154`) | Não para o WTC | — | **Nenhuma** | Check novo: todo código de declaração no WTC/DD existe na tabela de códigos da autoridade, válido no período (F48/C48, F49/C49) | **Total** — C48: código fora da tabela da autoridade ou vencido no ano reprova (testado) |
| WTC F-07 | Contribuição patronal Agirc-Arrco marcada como sujeita à CSG; FR-046 diz que não | 5 | Nenhum | Não | Não | **Nenhuma** | F50/C50: base legal por flag + flag × texto da mesma linha | **Parcial** — C50 compara com o crosswalk e exige base legal; erro no próprio crosswalk passa |
| WTC F-08, F-09, F-21/F-22, F-11/F-12/F-13/F-23 | Rubricas DSN por analogia (MNS em 50.004 — S1; horas extras em 50.011; IJSS como benefício em espécie; statut catégoriel, APET, INSEE, BOETH trocados); o DD estava certo | 5 | C27 (`SH:2928-2932`, MANUAL, não bloqueia, DD de nome fixo v1.0) | Não | Não | **Nenhuma** | L-E: cruzamento de rubrica WTC × DD × spec (F49/C49, F56/C56); C27 com glob de versão e bloqueante | **Parcial** — C48 valida campo=código; o mapeamento semântico (MNS em 50.004) não é verificável sem a norma |
| WTC F-10 | PAS arredondado ao euro (certo: ao centavo); `params.json` já anotava "unsourced" | 5 | C41 só para fatos com `register_id` (`:203-216`) | Não para convenção | — | **Nenhuma** | F64/C64: sinal, arredondamento e unidade declarados por contribuição, com fonte | **Nenhuma** — F64 não aprovado |
| WTC F-16 | Sobretaxas de contrato curto abolidas apresentadas como vigentes; bonus-malus ausente | 5 | C41 (se a linha estiver no registro com `effective_to`) | Sim | Sim | **Parcial** | Igual a F-23 (texto não ligado ao registro, L-A) | **Parcial** — C41 + C40 `mid_year_rate_change` |
| WTC F-24 | Teto de 7.500 escrito de 3 formas (WTC × DD × CCG) | 5/4/1c | C46 (L-A) | Aprova sem etiqueta | — | **Nenhuma** | L-A + F51/C51 (período e acumulador declarados) | **Parcial** — C46+ amarra o 7.500; a diferença de regra (anual × mensal) em prosa não |
| WTC F-20 / DD F-34/F-36 | Drive com conteúdo v1.3 e log "1.0"; DD do Drive desatualizado; DD dizendo que a grade PAS 2025 "não deve mais ser usada" | Entrega | C43 (rótulos internos); nenhuma conferência Drive × pipeline | C43 sim | Sim (C43) | **Parcial** | Conferência MD5 Drive × pipeline na promoção (`promote_to_pipeline.py` está só no repositório FR, não em `SA/release/`) | **Parcial** — C73 com `DRIVE_DIR` compara o Drive (testado); sem `DRIVE_DIR` não roda |
| DD F-35 / SD-02 (DD) | Sem campo do bonus-malus; sem "Urssaf SIRET (collecting body)" — dado mestre tratado como "produzido pelo cálculo" | 4 | `SA/spec-builder/mercans_spec/guards.py:48` `missing_sources`: **não é chamado** por `spec_checks.py` nem pelo script; só reporta, sem calibração (`IMPROVEMENT_LOG.md:227`) | Não | Não | **Nenhuma** | Ligar e calibrar o guard; F56/C56: todo campo-fonte de spec existe no DD ou nos dados mestres | **Parcial** — C56 reprova campo obrigatório "produced by the payroll calculation" (testado); campo inexistente no DD (bonus-malus) não |
| Payslip F-25/F-26/F-28 | Ajuste visual apagou 8 linhas estatutárias e deslocou fórmulas; líquido superestimado (~400; refeição 115,50 nunca deduzida) — S1 | 7 | C21/C26 só abas (`PRESUBMISSION_AUDIT.md:40,45`) | Não para conteúdo | Não | **Nenhuma** | L-F: contar as linhas estatutárias antes × depois de cada mudança de layout + recalcular o líquido (G-14/G-16; F57/C57) | **Total** — C57: linha estatutária ausente, líquido que não fecha e benefício em espécie não deduzido reprovam (testado) |
| Payslip F-27 | Itens obrigatórios do R3243-1 ausentes (net antes do imposto, MNS, PAS, convenção...) — S1 | 7 | Só prompt (`SH:2206`) | Não | Não | **Nenhuma** | F57/C57: checklist de campos legais por país, executável; Payslip no Teste 0 | **Parcial** — C57 confere os itens contra o payslip; a lista de itens vem da pesquisa; PSL entrou no Teste 0 |
| Payslip F-29/F-30/F-32/F-33 | Códigos que não batem com o WTC; taxa reduzida de família 3,45 % abolida; 151,67; "read from FR-DD-001-v1.0" com o DD em v1.1 | 7 | C43 pega a versão citada (`consistency_checks.py:276-285`); o resto não | Parcial | Sim (C43 "cites XX-DD-001 v1.1") | **Parcial** | Códigos Payslip × WTC (F49/C49); taxa com etiqueta (L-A) | **Parcial** — C49 (códigos) Total; taxa abolida 3,45 % não |
| SIR-01..09 | Prazos simplificados; FR-URSSAF-002 como outbound (é inbound CRM); "DSN Substitution" como ferramenta do declarante; CRM 124 omitido; ID "FR-SIR-001" num arquivo FR-SIR-INDEX-001 | 6 | C10 inbound/outbound só no prompt (`PRESUBMISSION_AUDIT.md:29`) | Não | Não | **Nenhuma** | F53/C53: tabela única arquivo × direção × spec × amostra; ID = nome do arquivo | **Parcial** — C53: ID e direção (testado; FR reprova em 11 pontos); prazos não |

### D. Specs e triagem DSN-Val

| ID | Erro | Est. | F/C que cobre (arquivo:linha) | Executável? | Teste negativo? | Cobertura | O que falta | v2.12 (17/10) |
|---|---|---|---|---|---|---|---|---|
| SD-03 / SA-01 / SB-09 | Conditional Reason cortada em 2.500 caracteres (71 controles perdidos na DSN-001) | 3 | F40: a biblioteca não corta (`SA/spec-builder/mercans_spec/workbook.py:249-256`, `rules.py:9`); **C34** (`spec_checks.py:82-116`) | Sim | Sim (corte → C34 FAIL TRUNCATED) | **Parcial** | Total na FR. Num país novo, C34 dá SKIP sem norma legível, e o uso da biblioteca é só prompt (`SH:1341`). Falta: SKIP do C34 exigir decisão registrada no manifesto; check "spec gerada pela biblioteca" | **Total** — biblioteca sem corte + C34, ou isenção registrada pelo dono (F68) + C71 garante que a spec veio do script |
| SD-01 / SA-02..04 / SB-10 | Árvore genérica da DSN mensal em todas as specs; blocos em ordem de identificador | 3 | F40: interface de árvore por natureza (`mercans_spec/trees.py`), com dados só da FR; C35 DSN-Val (só FR) | FR sim | Sim (C35) | **Parcial** | País novo sem dados de árvore e sem validador: nada. Falta "ordem da spec = ordem do arquivo oficial" contra o leiaute/XSD (F48/C48) | **Parcial** — país sem validador: só com isenção registrada; a ordem não é verificada |
| SD-02 / SA-05 | Identificador OPS "produzido pelo cálculo", sem fonte; exemplos inválidos | 3 | `guards.missing_sources` não ligado (ver DD F-35) | Não | Não | **Nenhuma** | Igual a DD F-35 (F56/C56) | **Total** — C56 (testado) |
| SD-04 / SA-07 / SB-11 (+44 anomalias do balde 1) | SIREN/SIRET sem Luhn; NIR incoerente; código de risco inexistente; S90 com contagem errada | 3 | F40/**C36** (`spec_checks.py:161-240`; registro genérico só IBAN e ISO 11649, `mercans_spec/ids.py:65-66`; o resto vem do plugin FR); C35 (FR) | Sim | Sim (SIREN alterado → C36 FAIL) | **Parcial** | País novo precisa de plugin com os seus identificadores (PT: NIF, NISS). Sem plugin, só IBAN/RF. Falta: identificador sem validador registrado → FAIL, não silêncio | **Parcial** — C36 sem plugin agora reprova, salvo isenção; o plugin do país (ex.: NIF/NISS) é do piloto |
| SD-05 / SA-06 / SB-34 | Regeneração apagou o Version Control (ID em branco, histórico colapsado, REMARKS perdido) | 3/Entrega | F47: uma linha de VC + histórico em `_audit/` (`SA/release/release.py`); C43 confere a última linha | Sim | C43 sim; C47 sem teste | **Parcial** | Nenhum check de "REMARKS/Document ID presentes"; C47 sem teste negativo no repositório | **Parcial** — sem mudança (C43 + C47, este agora com teste) |
| Patches pós-build (inclui SB-19) | Correções feitas à mão no .xlsx, desfeitas a cada regeneração; uma delas introduziu um S1 | 3 | `SA/spec-builder/compare_specs.py` existe, mas **não é chamado** pelo script (grep sem resultado em `SH`) | Não | Não | **Nenhuma** | Stage 9: "regerar = emitido" com `compare_specs.py`, bloqueante (G-15) | **Total** — C71 regera e compara célula a célula (testado; no FR reprova) |
| SB-19 | DGFIP-003: 8,50 %/13,60 % somados sobre os 4,25 % (imposto ~31–33 % maior); exemplo oficial alterado | 3 | C38 não lê specs | Não | Não | **Nenhuma** | C38 sobre "Example Analysis" das specs; exemplo oficial da autoridade como caso do C37 | **Total** — C71 (o defeito veio de patch manual) + C38 nos exemplos das specs |
| SB-01/SB-02/SB-03 | DGFIP-001: campo proibido no grupo de correção; controle sobre o campo errado; gatilho do 182 A pelo campo errado | 3 | C34 + C35 (FR) | FR sim | Sim | **Parcial** | Total na FR (norma + validador). País novo: só se houver validador; senão nenhuma | **Parcial** — sem mudança (FR com validador) |
| SB-05/SB-14/SB-15 | CRM PAS: regra de aplicação, validade e quantidade de CRM erradas; fonte dada como "não recuperável" | 3 | Nenhum | Não | Não | **Nenhuma** | Check novo: "fonte não obtida" cruzada com o registro, o SIR e os runbooks da mesma build (G-23) | **Parcial** — C70 reprova "not retrievable" sem lacuna registrada (no FR: 67 frases); as regras erradas não |
| SB-06/SB-07 | Sample com taxa 3,50 % (certo 2,9 %); grades e datas de troca ausentes | 3 | C46 (L-A) | Aprova sem etiqueta | — | **Nenhuma** | L-A (taxa do sample com etiqueta) | **Nenhuma** — 3,50 % não é fato; o C38 só testa taxa em linha Base × Rate |
| SA-08/SA-19/SIR-01 | Prazo da FCTU errado (também no CCG e no SIR) | 3/1c/6 | Nenhum | Não | Não | **Nenhuma** | Prazo como fato com etiqueta (L-A); C46 entre spec, CCG e SIR | **Nenhuma** — prazo em dias não é valor distintivo para o C46+ |
| SA-09/SA-10/SA-18 | Norma por natureza: FCTU antes da folha final; último dia em 62.008; TPT nas naturezas 04/05 | 3 | C34/C35 (FR) | FR sim | Sim | **Parcial** | Igual a SB-01 | **Parcial** — sem mudança |
| SA-25/SA-26 | DPAE "guia não obtido" (o runbook do SIR já tinha); campo SPST ausente | 3 | Nenhum | Não | Não | **Nenhuma** | Igual a SB-05 (G-23) | **Parcial** — C70 reprova lacuna já respondida pelo SIR (testado); campo SPST ausente não |
| SA-40..SA-43 | Solde TA: linha CTP 995 ausente; CSA em abril (certo: março); aplicado à Alsace-Moselle; sem fins lucrativos omitidos | 3/1 | C40 não tem linha de regime local nem de tipo de empregador (`research_checks.py:41-55`) | Não | Não | **Nenhuma** | Linhas novas no C40: `local_regimes`, `employer_type_and_size` | **Parcial** — C40 `local_regimes` e `employer_type_and_size` obrigam a pergunta |
| SB-25 | Taxa AT/MP indexada só pelo SIRET (certo: SIRET + código de risco + taxa "B") | 3 | Nenhum | Não | Não | **Nenhuma** | Rede: C39. Sem check específico; entra em `employer_type_and_size`/chave de taxa no C40 | **Parcial** — C40 `employer_type_and_size` |

### E. Entrega, vazamento e processo

| ID | Erro | Est. | F/C que cobre (arquivo:linha) | Executável? | Teste negativo? | Cobertura | O que falta | v2.12 (17/10) |
|---|---|---|---|---|---|---|---|---|
| Sobras de outros países | REFERENCE_Payslip_Tunisia, "delivered Belgium catalogue", BE-NSSO-002/004, FR-NSSO/FR-FIN | Entrega | F45/**C42** (`consistency_checks.py:155-187`) + C47 | Sim | Sim (XX-NSSO → FAIL) | **Total** | Frase sobre "outra jurisdição" sem nome nem código depende do C47 (sem teste) | **Total** — sem mudança |
| Jargão interno | "v2.7 STEP 3.5", "C25 audit failure", caminhos do pipeline nas specs | Entrega | F47/**C47** (`SA/release/release_crosscheck.py:46-174`) | Sim | **Não** (só a medição 2.544 → 0, `IMPROVEMENT_LOG.md:437-438`) | **Parcial** | Teste negativo do C47 no repositório | **Total** — C47 agora tem teste negativo (9 casos) |
| Versões internas | Report Matrix "1.4–1.6"; CCG v1.0 com "1.3" | Entrega | **C43** (`consistency_checks.py:226-231`) | Sim | Sim | **Total** | — | **Total** — sem mudança |
| "NO DD COUNTERPART" (264) | Anotação falsa de "sem contraparte no DD" nas specs | 3 | C27 (MANUAL, não bloqueia, DD de nome fixo); índice DD só no builder FR | Não | Não | **Nenhuma** | F56/C56; C27 com glob de versão e bloqueante | **Total** — C56 + C27 lendo a versão vigente do DD |
| Design: condições mortas | `LESS($58209;1)` em flag 1/2 | Design | F46/**C45** (`consistency_checks.py:411-428`; Stage 12 `SH:4181-4186`) | Sim | Sim | **Total** | — | **Total** — sem mudança |
| Design: semântica | Referência para frente; fórmula de 58110 contra o texto; 0,49 em vez de 0,0049 | Design | C45 só alcançabilidade | Não | Não | **Nenhuma** | Teste de expressões do design: unidade de taxa, ordem de cálculo, fórmula × texto | **Parcial** — C45+: unidade de taxa e referência para frente (testado); fórmula × texto (R-44) não |
| Skill desatualizada | Hash das referências nunca conferido; contagens fixas no código | Stage 11 | Nenhum (F28 existe só como texto) | Não | Não | **Nenhuma** | Stage 11: hash por referência × final do pacote (G-21) | **Total** — C73: proveniência SHA-256 de cada referência (testado; FR 52/52 iguais) |
| Desvio pós-promoção | Finais alterados depois de promovidos; 49 inconsistências | Entrega | Nenhum no pipeline | Não | Não | **Nenhuma** | Promoção com log MD5 e conferência byte a byte em `SA/release/` (G-21) | **Total** — `promote.py` com MD5 + C73 (testado; FR reprova em 21 arquivos) |
| Autoverificação baixa | QA aprovou 87/100 com Teste 0 de 77,5 % | 10 | F41/**C39** (`SA/validation-suite-template/test0_check.py:46-95`; Stage 10 `SH:3973-3986`) | Sim | Sim (3 FAIL = 92,5 % → FAIL; agregador → FAIL) | **Total** | O Payslip e o SIR ficam fora da amostra (L-F) | **Total** — C39 + PSL na amostra |
| Sem oráculo independente | Research nunca medida contra cálculo externo | 9b | F41/**C37** (`SH:3640-3643`, `:3845-3850`) | Sim | Sim | **Parcial** | L-C: o caminho `official_examples` nunca foi exercitado; nenhum mínimo de casos por linha do C40 | **Parcial** — C69 + caminho `official_examples` testado em suíte sintética; suíte real de país sem motor é do piloto |

### F. Defeitos do motor modele-social (não são nossos)

| IDs | Situação no pipeline |
|---|---|
| D-02, D-04, D-05, D-05b, D-06, D-13, D-14, D-15, D-16, D-18 (e a parte do motor do D-12) | **Não é nosso.** Ficam como resíduos explicados do C37 da FR (59/59; `run_suite.py:86-93`, `:170-185`). Ponto de atenção para um país novo: a classe "engine" é declarada em `defects.json` por quem corrige (o fixer do Stage 9, `SH`, entrada 8 do prompt); o código exige só "confirmed" + fonte não vazia. Um erro de research rotulado como do motor passaria |

### G. Erros do próprio validador (`TEST-DESIGN-CORRECTIONS.md`)
Não são erros da research. São lições de desenho de suíte: tolerância de 0,01 esconde erro de coeficiente (comparar com 4 casas), caso na fronteira de arredondamento (TC27), citação errada nas notas da suíte. O template `run_suite.py` não impõe tolerância por tipo de linha: fica como nota para o piloto.

---

## Contagem

| | Total | Parcial | Nenhuma | Linhas |
|---|---|---|---|---|
| A. D-* research | 0 | 7 | 1 | 8 |
| B. CCG + Teste 0 | 1 | 7 | 10 | 18 |
| C. WTC/DD/Payslip/SIR | 0 | 3 | 9 | 12 |
| D. Specs + DSN-Val | 0 | 6 | 9 | 15 |
| E. Entrega/processo | 4 | 2 | 4 | 10 |
| **Total** | **5** | **25** | **33** | **63** |

Linhas que agrupam IDs da mesma causa e cobertura contam como uma. Os defeitos do motor (seção F) e as notas do validador (seção G) ficam fora da contagem.

**Leitura:** o v2.11 fechou bem o que é **forma e embalagem**: versão única (C43), sobras de outros países (C42), condição morta no design (C45), truncamento e identificadores na FR (C34/C36), Teste 0 bloqueante (C39), e todos esses têm teste negativo. Ficou aberto o que é **conteúdo**: valor coerente entre artefatos (C46 aprova sem etiqueta), código de rubrica e flag cruzados, Payslip, exemplos fora do Módulo 12, e tudo o que depende de plugin, norma ou motor do país. Para um país novo, vários "Parcial" viram "Nenhuma", porque C34/C35 dão SKIP e o C36 só tem IBAN/RF.

---

## Lacunas priorizadas e correção proposta

Numeração: F48–F66 já estão propostos (catálogo de tickets, não aprovados). As correções que não casam com nenhum deles ficam como **F67+ (a numerar)**.

| Prio | Lacuna | Linhas afetadas | Correção proposta | Ligação | Piloto PT prova? |
|---|---|---|---|---|---|
| **P0-1** | C46/C32 aprovam com 0 etiquetas: a coerência de valores entre artefatos não existe na prática (L-A) | D-01, F-04, F-02, F-29, F-21/TEST0-F2, WTC F-24, SB-06, SA-08 (≈ 12 linhas) | C46: FAIL quando um número de taxa, teto ou prazo nas tabelas do CCG/WTC/DD/specs/Payslip não tem etiqueta (cobertura mínima de etiquetas por artefato) e quando o mesmo fato tem dois valores | F45 (reforço) + F52 | **Sim:** a etiquetagem nunca rodou numa build real (FR: 0 etiquetas) |
| **P0-2** | Nenhuma checagem cruzada de código de rubrica, flag de tributação e lado EE/ER (L-E) | WTC F-02/03, F-07, F-08/09/11/13/21/22/23, TEST0-F1, Payslip F-29, CDS lado, "NO DD COUNTERPART" | C novo bloqueante: mesmo código de rubrica, mesma flag e mesmo lado em WTC × DD × spec × Payslip × CCG; código existe na tabela da autoridade no período; C27 com glob de versão e bloqueante | F49/C49, F50/C50, F56/C56, F48/C48 | Parcial: a regra testa-se por mutação; o piloto mede o ruído |
| **P0-3** | Payslip sem check de conteúdo, sem recálculo e fora do Teste 0 (L-F) | Payslip F-25..F-28 (3 S1) | C novo: lista de itens legais do país (do registro) × Payslip; contagem de linhas estatutárias antes × depois de qualquer mudança de layout; líquido recalculado; `PSL` em `T0_ARTS` | F57/C57 | Sim (lista de itens de PT) |
| **P0-4** | Num país novo, C34/C35 dão SKIP e C36 vira só IBAN/RF; o C37 `official_examples` nunca rodou; os casos do C37 não estão ligados ao C40 (L-C) | SD-03, SD-01, SD-04, SB-01, SA-09, D-11, D-12, D-17, D-07 | SKIP só com decisão registrada no manifesto ("sem validador oficial: motivo + fonte"); identificador sem validador registrado → FAIL; ao menos 1 caso do C37 por linha "answered" do C40 e por exemplo do CCG | F43/F41 (reforço) + F67+ | **Sim, só o piloto prova** |
| P1-5 | C40 confere forma, não conteúdo; faltam linhas (L-B) | D-17, D-11, D-07, SA-40..43, SB-25 | Linhas novas: `local_regimes`, `employer_type_and_size`, `mid_year_rate_change`, ciclos especiais, competência × pagamento; seguridade do não residente com fonte própria; o caso do C37 (P0-4) prova o conteúdo | F58, F65, F43 | Sim |
| P1-6 | C38 só no Módulo 12, só aritmética, sem specs (L-D) | F-11, Ex. 3, F-13, F-05, F-29, SB-19 | Stage 9 com `--module` de todos os módulos com tabela + abas "Example Analysis" das specs; operandos com etiqueta `[[FACT:]]` | F42 (reforço) | Não: mutação basta |
| P1-7 | Citação não lida ou revogada; "fonte não obtida" falsa | D-08, F-06, F-25/26/28, SB-05, SA-25 | C novo: citação do registro com URL consolidada e estado "em vigor" lido na build; artigos citados no texto ⊂ registro; "not obtained/not retrievable" no texto × registro/SIR/runbooks | F63 (parcial) + F67+ | Não: mutação basta |
| P1-8 | Correção manual no binário; guard de campo sem fonte desligado | Patches pós-build/SB-19, SD-02, DD F-35 | Ligar `compare_specs.py` ("regerar = emitido") e `guards.missing_sources` (calibrado) no Stage 9, bloqueantes | F56 + F67+ | Não |
| P1-9 | Regra com troca de data no ano e valor sem data no texto | D-03, F-24, F-23, WTC F-16, F-17/18 | Constante datada no facts/design (vigência no texto); varredura também da norma do ano seguinte e 1 por autoridade do registro | F44 (reforço) + F51 | Sim (PT tem mudanças no meio do ano?) — a verificar |
| P2-10 | Promoção sem MD5, desvio Drive × pipeline, skill sem hash | WTC F-20, desvio pós-promoção, skill | Levar `promote_to_pipeline.py` (log MD5) para `SA/release/`; Stage 11 confere hash por referência | F59 | Não |
| P2-11 | C1–C33 não bloqueiam (`SH:3862`) | C31 (D-17), C27, C10 | Decidir após o piloto (decisão D2) quais passam a bloquear; C31 incluir seguridade | — | Sim (D2 dizia "até o piloto") |
| P2-12 | C47 sem teste negativo; semântica do design | Jargão interno, Design R-35/42/44 | `SA/release/tests/` com mutações; teste de expressões do design (unidade de taxa, ordem) | F47/F46 (reforço) | Não |
| P2-13 | Rubrica de SIR: direção e ID | SIR-01..09 | Tabela única arquivo × direção × spec × amostra | F53/C53 | Não |

### O piloto em Portugal é necessário?
**Sim, mas não para tudo.** Os mecanismos de C34–C47 já estão provados por mutação (5 conjuntos de teste, rodados hoje). Só o piloto prova:
1. o caminho de **país sem motor** (`official_examples`) e de **país sem plugin, norma ou validador** (P0-4). É exatamente o caso de PT, e hoje ele daria SKIP em silêncio;
2. a **etiquetagem `[[FACT:]]` numa build real** (P0-1). Sem ela, o C46 continua aprovando vazio;
3. o **Teste 0 escrito pelo agente do Stage 10** (o da FR foi feito numa sessão à parte, `IMPROVEMENT_LOG.md:541-583`);
4. a matriz C40 preenchida por um agente num país real.

Recomendação: corrigir antes P0-1 e a regra de SKIP do P0-4 (mudanças pequenas e testáveis por mutação) e só depois rodar o piloto, para que ele meça o pipeline corrigido e não a lacuna já conhecida.

---

## v2.12 (17/10/2026): o que mudou na cobertura

Correções P0–P2 implementadas no pipeline (aprovadas pelo usuário em 17/10, pela janela geral). Detalhe, arquivos e testes: `~/mercans-pipeline/IMPROVEMENT_LOG.md` (entrada de 2026-10-17); padrões no `shared/country_failure_log.md` (F48, F49, F50, F53, F56, F57 e F67–F74); checks no `shared/PRESUBMISSION_AUDIT.md` (seção v2.12). A coluna "v2.12" de cada tabela usa a mesma régua (Total / Parcial / Nenhuma) e só conta como coberto o que tem código bloqueante **e** teste negativo.

| | Total | Parcial | Nenhuma |
|---|---|---|---|
| v2.11 (matriz original) | 5 | 25 | 33 |
| **v2.12** | **18** | **38** | **7** |

| Seção | v2.11 T / P / N | v2.12 T / P / N |
|---|---|---|
| A. D-* research | 0 / 7 / 1 | 0 / 8 / 0 |
| B. CCG + Teste 0 | 1 / 7 / 10 | 4 / 10 / 4 |
| C. WTC / DD / Payslip / SIR | 0 / 3 / 9 | 2 / 9 / 1 |
| D. Specs + DSN-Val | 0 / 6 / 9 | 4 / 9 / 2 |
| E. Entrega / processo | 4 / 2 / 4 | 8 / 2 / 0 |

**Lacunas P0–P2 → check:**

| Lacuna | Correção (executável, com teste) |
|---|---|
| P0-1 C46 aprova sem etiqueta | C46+: 0 etiquetas ou valor de fato sem etiqueta = FAIL (F67); C32 idem |
| P0-2 rubrica / flag / lado | C48 códigos na tabela da autoridade; C49 códigos citados existem no WTC; C50 flags e lado = crosswalk, com base legal (F48–F50) |
| P0-3 Payslip | C57 itens legais, linhas estatutárias, líquido conciliado, benefício em espécie deduzido; PSL no Teste 0 (F57) |
| P0-4 SKIP silencioso / suíte sem ligação | SKIP por falta de suporte do país = FAIL salvo `validation_exemptions` registrada pelo dono (F68); C69 caso da suíte por linha da matriz e por exemplo do CCG; caminho `official_examples` testado (F69) |
| P1-5 C40 só forma | +5 linhas (F58, F65), fonte de seguridade para não residente; o conteúdo é cobrado pelo C69 |
| P1-6 C38 limitado | todas as tabelas do CCG, taxa = fato, exemplos das specs; SKIP sai com 1 |
| P1-7 citação / lacuna falsa | C70 (F70) |
| P1-8 binário corrigido à mão / campo sem fonte | C71 regerar = emitido (F71); C56 (F56) |
| P1-9 troca de data no ano | C41+: varredura por autoridade, `next_year`, data da troca no CCG / design (F72) |
| P2-10 promoção / Drive / skill | `promote.py` com MD5 + C73 (F73) |
| P2-11 C1–C33 | C27 lê a versão vigente do DD; C31 pede a seguridade do não residente; C32 0 etiquetas = FAIL. Bloquear C1–C33: decisão para depois do piloto (D2) |
| P2-12 C47 sem teste / design | teste negativo do C47 (9 casos); C45+ unidade de taxa e referência para frente (F74) |
| P2-13 SIR | C53 ID e direção (F53) |

**Ainda Nenhuma (7):** exemplos em prosa (CCG F-11 Mod. 9.1, Ex. 3 Mod. 6.3), limites da taxe sur les salaires, regra em prosa sem número (F-21 "three years' pay"), arredondamento do PAS (F64 não aprovado), taxa de sample que não é fato (SB-06), prazo em dias (SA-08). Nenhuma delas vira check genérico sem dado de país ou sem as propostas F51 / F64.

**Fica para o piloto (Portugal), porque precisa do dado do país:** suíte real `official_examples`; etiquetagem `[[FACT:]]` numa build real (calibrar o limiar de 100 %); plugins e tabelas do país (NIF/NISS, norma legível, validador, tabelas de códigos) ou as isenções do dono; Teste 0 escrito pelo agente do Stage 10; decidir se C1–C33 passam a bloquear.

**Regressão v2.12 no FR-compliance (só leitura):** C34–C37, C42–C45, C49, C56 PASS; FAIL esperados e explicados em C38 (os 3 números do Ex. 1 + 3 taxas de exemplo que não são fatos), C40/C41/C46/C48/C50/C57/C69 (o FR é anterior a esses insumos), C53 (11), C70 (56 + 67), C71 (builder FR ≠ specs emitidas), C73 (21 arquivos fora do MD5 do log de 09/10). Nenhum falso positivo novo sem explicação (dois achados no desenvolvimento, C45 e C49, foram corrigidos antes da rodada). Saídas em `~/mercans-pipeline/shared/_test-runs/2026-10-17-v2.12/`.

## Achados fora do pedido (não alterados)
1. **C38 reprova a CCG FR emitida** [[frentes/pipeline/mercans-pipeline/FR-compliance/01-ccg/FR-CCG-001-v1.0.docx|FR-CCG-001-v1.0.docx]]: 3 divergências na linha de base (rodado hoje). São os mesmos 3 números digitados do Exemplo 1 (`IMPROVEMENT_LOG.md:289-293`), que ficaram no pacote v1.0. Um novo Stage 9 da FR pararia no C38. O quadro final do log (`:579-583`) não lista o C38. → Pendência para o hub [[Franca]] (artefato entregue; regra 2: não corrigir sem pedido).
2. **C27 lê um DD de nome fixo `{CODE}-DD-001-v1.0.xlsx`** (`SH:2932`). Com o DD em v1.1 ou maior, o check dá SKIP sem aviso.
3. **`C21` no inventário diz "5-Sheet"** (`PRESUBMISSION_AUDIT.md:40`), e o código pede 8 abas (já anotado em `IMPROVEMENT_LOG.md:42`; o título da tabela continua o antigo).

## Registro das frentes
| Data | Frente | O quê |
|---|---|---|
| 2026-10-17 | Pipeline | Matriz criada (só leitura do pipeline, das skills e da fr-research-validation; testes de mutação rodados sobre cópias temporárias) |
| 2026-10-17 | Pipeline | Coluna "v2.12" e seção v2.12 acrescentadas depois da implementação das correções P0–P2 no pipeline (cobertura 5/25/33 → 18/38/7) |

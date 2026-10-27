# Lições consolidadas para o próximo Research Pipeline

Consolidado em 2026-10-15 a partir de três frentes de trabalho:

| Frente | O que é | Período | Relatório detalhado |
|---|---|---|---|
| **brain-service** | Wiki do serviço: 90 correções nossas, 137 tickets analisados, 49 hubs de país, 40 fronteiras de escopo | 2026-10-01 a 15 (os tickets cobrem 2024-05 a 2026-10) | [detalhado/licoes-brain-service.md](detalhado/licoes-brain-service.md) |
| **fr-research-validation** | Validação da research da França contra o motor oficial (modele-social) e o DSN-Val, com redlines e promoção | 2026-10-01 a 13 | [detalhado/licoes-fr-research-validation.md](detalhado/licoes-fr-research-validation.md) |
| **internal-certification** | Validação de 11 pacotes reais de folha (NO, DK, NL, SE, KZ, UA, UK) contra a fonte oficial, usando as skills como mapa | 2026-10-07 a 14 | [detalhado/licoes-internal-certification.md](detalhado/licoes-internal-certification.md) |

Os relatórios detalhados trazem cada defeito com o caminho da evidência. Este documento reúne o que converge entre as três frentes e o que falta fazer.

Referência do pipeline atual:
- Agentes em `~/.claude/agents/` (scaffolder, source-hunter, artifact-builder, qa-auditor) e skill `country-build`, todos revisados em 2026-10-07.
- Script `~/mercans-pipeline/mercans_pipeline_v2_9.sh`, cabeçalho v2.11.
- Failure log `~/mercans-pipeline/shared/country_failure_log.md`, com F1–F47.
- Checks C1–C47.

---

## 1. Resumo executivo

1. **O pipeline já absorveu parte das lições, mas só as da França.** As entradas F40–F47 e os checks C34–C47 (v2.11, 07/10) saíram da validação FR. São eles: gerador de specs, oráculo, exemplos calculados, matriz de populações, reverificação de 100 % dos números, fatos únicos e release limpo. O **piloto num país novo (Fase 6, recomendado Portugal) nunca rodou**, então nada disso foi provado fora da França.
2. **O brain-service propôs 19 padrões novos (F48–F66) que ainda aguardam aprovação.** Eles cobrem spec contra XSD, WT renomeado, flag sem base legal, acumuladores, resposta de ticket como fonte de erro, matriz de cobertura de relatórios, ciclos, sinal e arredondamento, entre outros. Nada foi aplicado ao failure log.
3. **A internal-certification revelou uma classe de lição que o pipeline não tem: a validação contra a folha real.** Na maioria dos países a skill estava certa e a configuração errada (NO, SE, UK, NL). Mesmo assim apareceram erros dos artefatos:
   - DK com 46 marcadores `[VERIFY]` publicados; um deles virou um achado High;
   - NL sem a regra AantVerlU;
   - CCG UA desatualizado e contraditório;
   - UA sem a spec J0500111;
   - KZ sem base, com o código tributário substituído em 2026.

   Também faltam no pipeline um validador e um registro de controles por país.
4. **As três frentes chegam às mesmas causas-raiz** (§3), com destaque para:
   - fonte secundária ou desatualizada;
   - valor sem vigência;
   - flag decidida por analogia;
   - spec não testada no validador oficial;
   - exemplo digitado;
   - correção não propagada;
   - cobertura de populações, relatórios e ciclos;
   - QA autodeclarado e checks que nunca reprovam.

Números que dimensionam o problema:

| Indicador | Valor | Fonte |
|---|---|---|
| Teste 0 do pacote FR, antes e depois | 77,5 % → 98,0 % | FR |
| DSN-Val na DSN Mensuelle, antes e depois | 51 anomalias (49 bloqueantes) → 0 | FR |
| Controles da norma cortados pelo gerador (truncamento em 2.500 caracteres) | 71 na FR-DSN-001 | FR |
| QA autodeclarado contra real | 86,5 % contra 73,2 % (FR); QA 87/100 aprovou pacote com Teste 0 de 77,5 % | brain / FR |
| Erros nossos registrados | 90 linhas em `correcoes.md`; 69 defeitos catalogados (WTC 18, Specs 17, CCG 11, design 8, tickets 8) | brain |
| Padrão mais frequente nos tickets novos | F54 (cobertura não publicada): 20 de 79 | brain |
| Achados abertos da certificação | 79 (10 High, 23 Medium, 30 Low, 16 Observation) | IC |
| Falsos positivos do validador automático NL | ~40 % das exceções | IC |
| Divergências do simulador oficial que eram erro do motor | 59 de 59 restantes (11 defeitos do motor) | FR |

---

## 2. O que já está no pipeline v2.11 e o que não está

| Lição | Situação | Onde |
|---|---|---|
| Gerador de specs sem truncamento, com árvore por natureza e identificadores válidos | **Absorvido** (F40; C34–C36) | `shared/spec-builder/` |
| Validador oficial de formato no sample da spec | **Só França** (C35 = DSN-Val). Ucrânia (J05 inválido no XSD) e Espanha (M190, rejeição 21902B) ficaram fora | `shared/validators/dsnval_batch.py` |
| Oráculo independente e suíte externa | **Absorvido** (F41; C37) | `shared/validation-suite-template/` |
| Exemplos resolvidos calculados | **Absorvido** (F42; C38) | idem |
| Matriz de populações especiais | **Absorvido** com 13 linhas (F43; C40) | `research-checks/` |
| Reverificação de 100 % dos números e varredura final de boletins | **Absorvido** (F44; C39, C41) | qa-auditor §6 |
| Consistência cruzada, fatos únicos e versão de pacote | **Absorvido** (F45; C42–C46) | `consistency-checks/` |
| Design derivado da research | **Absorvido** (F46) | `design-template/` |
| Release sem histórico de revisão no entregável | **Absorvido** (F47; C47) | `release/release.py` |
| F48–F66 (brain-service) | **Proposto, não aplicado** | `brain-service/revisoes/2026-10-0{8,9}-catalogo-erros-tickets*.md` |
| Certificação contra folha real, registro de controles e validador por país | **Novo** (internal-certification) | — |
| Vigência (`valid_from/valid_to`) por fato e rotina de virada de ano | **Novo** (as três frentes) | — |
| Distribuição de skills com manifesto e hash | **Novo** (IC) | — |
| Piloto do v2.11 num país novo | **Não executado** | `~/mercans-pipeline/IMPROVEMENT_LOG.md` |

---

## 3. Temas transversais

Cada tema traz a evidência das três frentes, a situação no pipeline e o gate proposto.

### T1. Fonte secundária, valor desatualizado e valor sem vigência

Este é o padrão mais frequente: 14 casos no brain-service, além de França e certificação.

**Evidência**
- CI: teto CNPS de 70.000 XOF, quando o correto é 75.000 desde 2023 (CLEISS e página da CNPS desatualizados). Chegou à skill e ao CT-A-620.
- LT: VDU de €2.304,50 sem fonte; o correto é €2.312,15, o que dá €83.237,40 / €138.729. Os artefatos em produção seguem com as regras de 2025.
- FR:
  - PASS 50.122 em vez de 50.112;
  - teto da Apec em 8 PSS em vez de 4;
  - minimum garanti de 2025;
  - net social pela regra de 2023;
  - sobretaxas de contrato curto abolidas em 2017/2019 apresentadas como vigentes.
- IE, BW, BE e NA: valores do ano anterior.
- UA: lei marcial dada como vigente "até 04/05/2026" (está prorrogada até 31/10); C_DOC_VER 10 → 11 em julho/2026.
- NL: teto SS de 5.509 contra 6.617,41.
- KZ: o Código Tributário de 2017 foi **substituído por inteiro** em 01/01/2026.

**Situação.** O F44/C39 cobre a reverificação. **Faltam:**
- data de vigência por fato;
- separação primária/secundária com bloqueio;
- recálculo de valores derivados;
- verificação de substituição do diploma;
- rotina de virada de ano e de meio de ano.

**Gates**
- **G-T1a:** todo fato no `facts.json` e no `legal-basis-register` com instrumento, artigo, `valid_from`/`valid_to`, URL aberta na build e data de leitura. Fato sem vigência = FAIL.
- **G-T1b:** tier por fonte. Número vindo só de fonte secundária (CLEISS, PwC, blog, tabela-resumo) não entra em artefato.
- **G-T1c:** todo valor derivado (36 × VDU, 12 × mensal, 4 × PSS) carrega a conta e o insumo citado, e um script recalcula.
- **G-T1d:** o scaffolder pergunta se o diploma principal foi substituído no ano, como no caso KZ.
- **G-T1e:** calendário de revisão por fonte (hash da página ou do arquivo oficial). Mudança de hash abre uma rodada de atualização. Inclui a tarefa de parâmetros do ano seguinte no manifest.
- Quando portal e lei divergem, registrar uma pergunta (F63); a notícia datada e o texto normativo prevalecem sobre a tabela-resumo.

### T2. Flag de wage type e mapeamento decididos por analogia

**Evidência**
- brain-service, 13 casos:
  - UA: seguro de vida tratado "como médico";
  - CO: incapacidade tratada "como indenização", contra o DIAN Oficio 27408/2019; ARL = Yes nas férias;
  - ES: clave B "pago directo".
- FR: mapeamento DSN sem o cahier aberto (MNS em 50.004, horas extras em 50.011, IJSS como benefício em espécie, Agirc-Arrco com código 105).
- IC: DK-4020 (seguro-saúde) publicado com o AM em `[VERIFY]` virou High num cliente real.

**Situação.** F7 e F20 existem. F50/C50 estão propostos.

**Gate G-T2.** Esquema de WTC com uma coluna "base legal" (artigo) por flag. Flag sem base = bloqueio. Colunas obrigatórias por elemento:
- método de retenção (tabela, engångsbelopp ou percentual);
- base de imposto e base de cada contribuição;
- campo(s) do report com a regra de população;
- inclusão em férias;
- rótulo local obrigatório (o GL NL saiu com "EOBI" e "EIS");
- conta GL.

WT de ajuste herda as flags do WT principal (C60). Todo mapeamento DSN ou de formulário cita o cahier ou a instrução de preenchimento.

### T3. Spec de arquivo oficial nunca testada no XSD ou validador oficial

**Evidência**
- brain-service, 10 casos:
  - ES: M190 (rejeição 21902B), M111, BASES e CERTIFICA;
  - UA: J05 D1/D5/D6. A amostra D5 do Dev era inválida no XSD; o teste do Dev era circular porque reproduzia a nossa spec.
- FR: 51 anomalias no DSN-Val; 44 vieram de um sample "ilustrativo".
- IC UK: o FPS live trazia comentários do sample do HMRC e Timestamp de teste.

**Situação.** C35 está ligado só à França. F48 e F55 estão propostos.

**Gate G-T3.** Toda spec de arquivo oficial:
- nasce do XSD ou do Diseño Lógico, com diff mecânico de tags, posições, comprimentos, padding, enums, ordem, `xs:choice` e nillable;
- traz uma amostra validada no validador ou XSD oficial dentro da própria spec;
- conta os controles da norma contra a spec.

Quando não houver validador, a SKIP precisa dizer o motivo. O título da spec é o nome oficial mais a direção (C53). Campos que dependem da entidade vão para o DD, nunca como constante de template (caso Kyiv 26/50/2650).

### T4. Exemplos digitados e contradições internas

**Evidência**
- FR:
  - RGDU de tempo parcial com o SMIC de tempo integral;
  - net taxable sem 485,00;
  - taxe sur les salaires superestimada ~31 % por um patch manual.
- UA:
  - teto do ЄСВ dito "15×" e "20×" no mesmo CCG;
  - gross-up de BIK por 0,77 contra 0,82;
  - exemplo com base de PIT de 2.360.
- CO: "non-salary" na mesma linha que "in levy base".
- LT: duas fórmulas de NPD.

**Situação.** F42/C38 cobrem os exemplos do CCG. Falta o lint de valor único por parâmetro em todo o dossiê (inclusive skill e specs).

**Gate G-T4.** Um parâmetro tem um único valor em todo o dossiê. Os exemplos de todos os artefatos (CCG, specs, WTC e skill) são recalculados por script a partir dos fatos; diferença maior que 0,01 = FAIL. Detectar classificações conflitantes do mesmo WT ou conceito.

### T5. Correção não propagada e resposta de ticket como fonte de erro

**Evidência**
- CG: CCG certo e WTC errado (SS patronal).
- FR: prévoyance no net taxable escrita de três formas; IJ AT corrigida no CCG e não no WTC.
- UA: piso do ЄСВ corrigido num lugar e não nos exemplos; "6 meses" de sick leave dito em resposta e nunca retirado por escrito.
- Código de WT renomeado sem varredura (57176 → 58176 → 58552).
- As correções do brain-service (CG, CI, LT, CO, UA) estão só no `correcoes.md`, não nas skills.

**Situação.** F27, F45 e C46 existem. F49 e F52 estão propostos. Lição da FR: "uma regra, um lugar". O boilerplate repetido multiplica o erro.

**Gate G-T5.** Toda correção, inclusive a feita via ticket, gera um ledger de propagação CCG ↔ WTC ↔ DD ↔ Specs ↔ Payslip ↔ Skill, com reverse lookup de códigos renomeados ou retirados (C49), **antes** de responder "done". A resposta de ticket cita a versão vigente do artefato, e um fato novo entra no artefato antes da resposta. Decidir o OD-13: o ticket HRBS edita o artefato ou escala para CT?

### T6. Cobertura: populações, ciclos, tributos locais, regimes especiais, relatórios e regra de preenchimento de campo

**Evidência**
- Populações e regimes:
  - FR: COTAM do não residente (a C31 só olhava o imposto de renda, não a seguridade social), CPF-CDD, AT/MP, maternidade acima do teto;
  - CO: retención contingente, licença por perda gestacional, incapacidade acima de 180 dias;
  - CG: TOL (tributo local);
  - CI: regime petrolífero, aprendiz.
- Relatórios sem spec:
  - LT: 1-SD, 2-SD e outros (matriz com 64 itens);
  - UA: J0500111.
- Regras ausentes na skill:
  - DK: Store bededag e felt 0026;
  - NL: AantVerlU = média de 173 para mensalista (Medium recorrente em 2 clientes);
  - DK: 0069 bruto antes da isenção.

**Situação.** F43/C40 cobrem uma matriz de 13 linhas. F54, F58 e F65 estão propostos.

**Gates**
- **G-T6a:** matriz de cobertura publicada por país (o modelo é a matriz LT de 64 itens), com cada relatório, população, ciclo e tributo marcado como Coberto, Parcial, Lacuna ou Fora, e com dono.
- **G-T6b:** eixos obrigatórios na matriz:
  - populações, incluindo residência para imposto **e** para seguridade;
  - ciclos (off-cycle, adiantamento, retroativo, licença entre meses, ordem de runs);
  - competência × pagamento;
  - tributos locais e regionais;
  - regimes especiais;
  - pagamentos não-emprego.
- **G-T6c:** todo campo de Report Spec com a regra de população dos casos de borda: valor bruto contra isento, campo adicional obrigatório, média contra efetivo, categoria por natureza.

### T7. Limites, acumuladores, sinal e arredondamento

**Evidência**
- Limites e acumuladores:
  - CO: 1.340 UVT ÷ 12 sem acumulador;
  - CI: defeito de 12×; CT-A-620 com 840.000 em vez de 900.000;
  - CG: limiar anualizado;
  - CA: máximo anual ÷ 12.
- Arredondamento:
  - FR: PAS arredondado ao euro em vez de ao centavo;
  - UK: meio pêni de NIC;
  - SE: FK487 com öre descartado;
  - NL: tabela contra fórmula;
  - KZ: regra NOT LOCATED;
  - UA: kopeck no 126 e no Д1.

**Situação.** F51 e F64 estão propostos.

**Gate G-T7.** Todo limite declara período, acumulador, status (calculado ou pago), sinal, unidade e arredondamento (direção, momento e nível: linha, pessoa ou total), diz se a tabela é normativa e traz um teste por banda, inclusive acima do teto.

### T8. Resíduos, marcadores e jargão interno no entregável

**Evidência**
- FR: Bélgica, Tunísia e Holanda dentro dos artefatos franceses, e textos internos como "v2.7 STEP 3.5".
- TD: "Czechia Report" no DD.
- CG: matriz do cliente com conteúdo do Senegal.
- DK: **46 `[VERIFY]` numa skill distribuída**.
- UA: "approximately — verify exact amount" no CCG.

**Situação.** C29 e C42 existem, mas chegaram skills com `[VERIFY]` à operação.

**Gate G-T8.** O lint C29/C42 também cobre `references/` da skill compilada e os artefatos do Drive. Além disso:
- marcadores bloqueados: `TBC`, `Check WTC`, `[provisional]`, `approximately`, `verify exact`, `RESEARCH-GAP`;
- prefixos de outro país;
- o lint tem **teste negativo** (plantar um marcador e provar que reprova).

### T9. QA autodeclarado e checks que nunca reprovam, ou sempre reprovam

**Evidência**
- FR: QA de 86,5 % declarado contra 73,2 % real; QA 87/100 sobre um Teste 0 de 77,5 %. O próprio CCG declarava ter reverificado só 11 % das perguntas.
- C20 dá FAIL como falso positivo em todos os países; C8 casava "todo" em ES e PT.
- NL: ~40 % de falsos positivos no validador automático.
- "Simulador oficial não é gabarito": havia 11 defeitos no próprio motor.

**Situação.** C37 e C39 existem. A calibração e o teste negativo não existem.

**Gates**
- **G-T9a:** todo gate tem um teste de mutação ou negativo que prova que ele reprova (modelos: `sch_negative_test.py` do UK e `mutation_test.py` da FR).
- **G-T9b:** o score do QA é recalculado por script, nunca autodeclarado.
- **G-T9c:** calibrar C20 e C8.
- **G-T9d:** divergência com oráculo ou simulador é classificada (research, motor, limitação ou inconclusivo) e decidida pela fonte primária.
- **G-T9e:** auditor independente que re-deriva sem importar o código do construtor.

### T10. Versão, linhagem e distribuição

**Evidência**
- CO: a v1.2 foi montada sobre o `~/mercans-pipeline` defasado, quando a vigente era a linhagem do Drive.
- FR: Drive desatualizado em relação ao pipeline; finais alterados depois da promoção (49 inconsistências).
- CL: versão da spec LRE apagada enquanto a BA trabalhava nela.
- UA: v3.5 entregue com nome V3.4; WTC V4.2 só como `.gsheet`, ilegível offline.
- IC: **skills na `.trash` no dia da validação**.

**Situação.** C47 e a promoção com MD5 da FR existem. Faltam a linhagem e a distribuição.

**Gate G-T10.** O builder compara com a maior versão publicada (Drive) antes de começar e recusa partir de uma base mais antiga. Além disso:
- nome = Version Control = conteúdo, e nunca se apaga uma versão em uso (C59);
- todo artefato é exportado em `.xlsx`/`.docx` (nada só em `.gsheet`);
- as skills são distribuídas com manifesto e hash, com checagem de presença antes do uso;
- o link é atualizado no Monday na promoção.

### T11. Corrupção por ferramenta e edição de binário

**Evidência**
- Excel transformou posições em datas (58 células ES).
- Um ajuste visual do Payslip FR apagou 8 linhas estatutárias: líquido ~EUR 400 acima e R3243-1 não atendido.
- Patches manuais no `.xlsx` eram desfeitos a cada regeneração, e um deles introduziu um erro S1.
- `delete_rows` do openpyxl; python-docx não lê `w:ins`.
- pdftotext e o parser NL perderam linhas de tabela.

**Gate G-T11.**
- Correção só no gerador ou num overlay versionado; o diff "regerar = emitido" tem de ser idêntico.
- Detector de perda (tamanho máximo de célula, linhas de Version Control, linhas estatutárias antes × depois).
- Edição de xlsx com comentários ou desenhos só por cirurgia de XML.
- O extrator de PDF é testado por tipo de documento, com contagem de linhas.
- Depois de qualquer mudança de layout do Payslip, conferir a lista legal do país.

### T12. Validação contra a realidade: o elo que falta

**Evidência**
- IC:
  - a skill certa não chega à configuração (NO sindicato, SE engångsbelopp, UK NIC e Gateway, NL AOW);
  - clientes do mesmo país divergem entre si (DK Sherwin × KGS);
  - defeitos de Payslip em todos os 7 países (YTD de imposto = período, totais, indicadores contraditórios).
- FR: só o cálculo independente pegou o erro da Apec, que estava "consistente" em todos os artefatos e por isso invisível ao QA de consistência.

**Gates (novos)**
- **G-T12a, Estágio de certificação contra folha real** entre o QA e a promoção. Usa um pacote HRBLIZZ real e recente (report, recibo, G2N, contracheques, GL, banco e master) ou um sintético oficial. Achado com origem SKILL bloqueia a promoção; achado CFG vira ticket para implementation.
- **G-T12b:** o pipeline emite `control-register.md` + `validate.py` por país, no modelo do `nl-payroll-validator`: uma linha de controle por regra do CCG, flag do WTC, campo de spec e invariante do Payslip, com "every run produces every row".
- **G-T12c:** diff WTC × configuração real do cliente.
- **G-T12d:** Payslip com invariantes testáveis:
  - roll-forward do YTD;
  - YTD de imposto ≥ período;
  - Σ linhas = total;
  - campos iguais ao report;
  - benefício in natura visível.
- **G-T12e:** o SIR define, por país, o que prova o aceite (GODKJENT, Afstemning, Digipoort, Kvittens, HMRC ack, квитанція №2) e exige a redação de credenciais.
- **G-T12f:** cada achado SKILL vira caso de regressão permanente da skill.

---

## 4. Backlog priorizado

**P0: bloqueia o próximo país**

| # | Ação | Tema |
|---|---|---|
| 1 | Aprovar e ingerir F48–F66 no `country_failure_log.md` (v2.12), com os checks C48–C66 | T2–T7, T10 |
| 2 | Vigência por fato (`valid_from/valid_to`) e tier primária/secundária com bloqueio no `facts.json` e no register | T1 |
| 3 | Estender o C35 a todo país com XSD ou validador (no mínimo XSD + lxml), com a amostra validada dentro da spec | T3 |
| 4 | Lint de residual (C29/C42) cobrindo `references/` das skills, com teste negativo | T8, T9 |
| 5 | Teste negativo ou de mutação para cada gate bloqueante; calibrar C20 e C8 | T9 |
| 6 | Builder parte da maior versão publicada (Drive); nada só em `.gsheet` | T10 |
| 7 | **Rodar o piloto da Fase 6** num país novo (recomendado: Portugal), medindo os indicadores do plano | — |

O piloto mede: linhas iguais ao simulador ≥ 98 %, Teste 0 ≥ 95 %, 0 anomalias no validador, 0 controles cortados, 0 inconsistências entre artefatos e menos de 10 mudanças por artefato depois da entrega.

**P1: entra no v2.12**

| # | Ação | Tema |
|---|---|---|
| 8 | Esquema de WTC com flags testáveis, base legal por flag, rótulo local e método de retenção | T2 |
| 9 | Matriz de cobertura ampliada (relatórios, ciclos, competência, tributos locais, regimes) publicada com dono | T6 |
| 10 | Regra de população de campo de borda e regra de arredondamento por valor em todo Report Spec | T6, T7 |
| 11 | Lint de valor único por parâmetro no dossiê e recálculo dos exemplos de todos os artefatos | T4 |
| 12 | Ledger de propagação obrigatório, inclusive para correções via ticket | T5 |
| 13 | Payslip: invariantes testáveis e lista legal do país conferida depois de qualquer mudança de layout | T11, T12 |
| 14 | Calendário de revisão por fonte (hash) e tarefa de virada de ano no manifest | T1 |

**P2: estágio novo**

| # | Ação | Tema |
|---|---|---|
| 15 | Estágio de certificação contra folha real antes da promoção | T12 |
| 16 | `control-register.md` + `validate.py` por país como artefato do pipeline; parsers HRBLIZZ como biblioteca comum (`validators/common/`) | T12 |
| 17 | SIR com prova de aceite por país e higiene de template de produção | T12 |
| 18 | Distribuição de skills com manifesto, hash e checagem de presença | T10 |

**Propostas de 2026-10-19 (F75–F81 / C75–C81): status "proposta — não aceita"**

Origem: as correções de 19/10 (BE e ES) e a call de 16/10. Pedido do usuário via janela geral: só registrar agora. Não implementar e não mexer no script, nos checks, no `country_failure_log.md` nem nas skills. Nada entra em vigor sem o ok do usuário.

| Proposto | Título | Evidência | Check / regra proposta | Status |
|---|---|---|---|---|
| F75 / C75 | **Report Spec com texto do glossário da autoridade fora do inglês.** As colunas G Conditional Reason, J Format, M Field Explanation, O Option Values e T Query to RA saíram em FR em 5 specs BE (cerca de 3.100 células). | `rascunhos/2026-10-16-BE-auditoria-idioma.md`; `rascunhos/2026-10-19-BE-specs-idioma-verificacao.md`; correção de G e M em `Research Pipeline/Belgium/2026-10-19-specs-idioma-M-G/` | C75: reprovar texto não-inglês (palavras funcionais, ignorando parênteses e aspas) em toda coluna que o cabeçalho não declare local ("(FR)", "(NL)", "Local"…); códigos e máscaras ficam literais. Reforça C33 (só CCG hoje). | proposta — não aceita |
| F76 / C76 | **Versão citada entre artefatos que não existe.** As 9 specs BE citam "BE-DD-001-v1.4" (791×), mas o DD vigente no Drive é o v1.0 e não existe v1.4. | `rascunhos/2026-10-19-BE-specs-idioma-verificacao.md` §3 | C76 (propagação): toda citação `<CC>-<TYPE>-<SEQ>-vX.Y` é validada contra a versão vigente do artefato citado (maior versão não-DRAFT; linhagem do Drive). | proposta — não aceita |
| F77 / C77 | **Formulário oficial do empregado × DD.** Campos que entram no cálculo e não estavam no DD: 8 do Modelo 145 ES, como pensão compensatória, anualidades por alimentos, préstamo vivienda, art. 18.2, ano de adoção, convivência do ascendente, data da mobilidade e 5º descendente em diante. | `Research Pipeline/Spain/2026-10-19-modelo145-x-DD/` (matriz + CONFERENCIA) | C77: na pesquisa e no DD, cruzar as entradas do algoritmo oficial (ex.: XSD AEAT) e o desenho do report (ex.: Modelo 190) com o DD. Campo só entra quando a fonte oficial o prova necessário (não espelhar o formulário). | proposta — não aceita |
| F78 / C78 | **Slots fixos menores que o limite oficial.** O DD tinha Child 1-4, mas a lei não tem limite (LIRPF art. 58.1) e o serviço da AEAT aceita 16 (XSD maxOccurs=16). | idem F77; DD ES V5.0 (Child 5-16) | C78: grupo repetido no DD é dimensionado pelo limite oficial documentado (XSD, desenho de registro ou lei), com a fonte do número. | proposta — não aceita |
| F79 / C79 | **Edição de DD que renumera ou destaca de forma ambígua.** A 1ª V5.0 ES renumerou 15 ordinais existentes, e o azul FFDDEBF7 se confundia com FFD9E1F2/FFCFE2F3 do arquivo. | `Research Pipeline/Spain/2026-10-19-modelo145-x-DD/CONFERENCIA.md` (opção A; amarelo FFFFF2CC) | Regra/C79: só acrescentar, sem renumerar os ordinais existentes. Destacar com cor que o arquivo não use (fazer o inventário de fills antes; FFFFF2CC já existia em 7 células). Conferir célula a célula com 0 diferenças nas células antigas. | proposta — não aceita |
| F80 / C80 | **Design × Global WTC.** Flag com código fora do designado: 58201 (Advance Reconciliation) no lugar de 58218 (tax residency). Base fora das dedicadas: 58550/58552 no lugar de 58106/58130/58131 ("do not use"). Par EE/ER incoerente (2551 EE / 2550 ER). | `raw/chats/2026-10-16-cross-training-design-creation.txt`:<br>• 12:06–13:53: 58218 × 58201;<br>• 21:38–23:34: 58131 × "we use 58550 and 58552";<br>• 27:07 e 40:58: "2551 for employee. 2550 has to be for employer";<br>• 42:12: 58106/58130/58131 "aren't used", que o ASR transcreve como "581 06" e "five eight one thirty".<br>`Downloads\Global Wage Type Catalogue 1.1.xlsx`, aba All Codes:<br>• 58106/58130/58131 = "Regulation base (do not use)";<br>• 58201 = "Advance Reconciliation Enabled (regulation base)";<br>• 58218 = "Tax residency (regulation base)";<br>• 58550 = "Period Taxable SSI Base (ER) (notional)";<br>• 58552 = "Period Taxable Tax Base 1 (EE) (notional)";<br>• 2550 = "Social Security (employer)";<br>• 2551 = "Social Security (employee)". | C80: todo código usado no Design existe no Global WTC com a designação compatível. Flags e bases só com o código designado; códigos "do not use" reprovam; pares EE/ER coerentes. | proposta — não aceita |
| F81 / C81 | **Design fechado antes de estudar os reports.** Ler os reports depois do design causa mudança grande de design em alguns países. | `raw/chats/2026-10-16-cross-training-design-creation.txt` (Mohit, 45:03–46:01) | Regra de ordem: as Report Specs são estudadas campo a campo antes de fechar o Design; o gate do Design exige a matriz report × campo × WT. | proposta — não aceita |

---

## 5. Correções de conteúdo que ainda precisam ir para as skills e os artefatos

Já foram identificadas e verificadas em fonte primária, mas ainda não foram aplicadas.

| País | Pendência | Origem |
|---|---|---|
| CI | Teto CNPS 75.000 desde 2023 (skill §2.1, CT-A-620: 840.000 → 900.000/ano) | brain |
| CG | CAMU paga direto à CAMU em 5 dias; DAS em janeiro (CGI art. 176); DAS3 art. 116 I; solidarité pela LFR 2021 art. 42; TOL de habitação 1.000 FCFA/mês | brain |
| LT | VDU €2.312,15 → €83.237,40 / €138.729; NPD 2026; os artefatos em produção ainda estão em 2025 (faixa de 25 %); faltam specs 1-SD/2-SD/9-SD/12-SD/13-SD/NP-SD | brain |
| CO | Incapacidades e licenças tributáveis (DIAN 27408/2019); ARL = No; dias 1–2 fora dos parafiscales; CO-GAP-15; 1.340 UVT ÷ 12 | brain |
| UA | Pacote de 25 correções para a skill. Itens:<br>• CCG V1.6: lei marcial até 31/10, teto ЄСВ 20×, gross-up 0,82, piso ЄСВ nos exemplos<br>• spec J0500111 e C_DOC_VER 11<br>• WTC V4.2 exportado para `.xlsx`<br>• "6 meses" de sick leave retirado por escrito | brain + IC |
| ES | KB CT-A-485 e fórmulas 52982–52984 com as bases mínimas antigas (correto: G1 1.989,30 / G2 1.649,70 / G3 1.435,20 / G4-7 1.424,40) | brain |
| BE | 24,92 % × (19,88 % + 5,12 %); 697,61 × 697,42; box 360 | brain |
| DK | 46 `[VERIFY]`; DK-4020 seguro-saúde → 0013 + 0026 com AM; 0069 bruto; Store bededag; base do ferietillæg | IC |
| NL | AantVerlU média de 173; teto SS 2026 de 6.617,41 (PE 52990/52999); validador NL v1.5 | IC + brain |
| KZ | Construir a base sobre o Código 214-VIII (reaproveitar `internal-certification/references/Kazakhstan/2026/facts.md`) | IC |
| FR | D-19 inconclusivo; net social de 2027 depende do decreto; 4 notas sem fonte; reenviar a skill ao Claude.ai; push ao GitHub | FR |
| IE, BW, GB, NA | Valores de 2026 (PRSI 4,35 % desde 01/10, A1 > 552, 6ª faixa PAYE BW, AE GB, data do teto SSC NA) | brain |

---

## 6. Decisões e itens de processo em aberto

- Aprovar F48–F66 (P0 #1).
- Aprovar ou rejeitar F75–F81 / C75–C81 (propostas de 19/10, seção 4).
- Escolher o país do piloto (P0 #7).
- OD-13: o ticket HRBS edita o artefato ou escala para CT?
- Erro de parsing Stage 1 → 2 (v2.8) sem correção registrada.
- **Segurança:**
  - chave da Anthropic exposta, que precisa ser rotacionada (`brain-service/servicos/research-pipeline.md`);
  - credencial do Government Gateway da McDermott em texto claro arquivada em `internal-certification` (UK-F01).
- Orquestrador Hermes parado à espera de 3 arquivos de referência.
- Reinstalar e versionar as skills que estavam na `.trash`.
- Git do brain-service sem commit desde 08/10; commits locais da FR não enviados.

---

## 7. Regras de trabalho que valem para qualquer estágio

Extraídas das memórias e dos `CLAUDE.md` das três pastas.

- A fonte primária decide. Simulador, blog, fornecedor e outro artefato só servem para achar a fonte. O que não se confirma sai do texto ou fica marcado como não confirmado.
- "Tem certeza?" significa reverificar do zero.
- Lente de fornecedor de software de folha, não de consultor fiscal. Mapear WT do cliente não é Compliance. Bug fix tem escopo restrito.
- Antes da web, procurar nos arquivos locais e no Drive.
- Edição de xlsx:
  - mexer só no que foi pedido;
  - destacar as células alteradas em `FFDDEBF7`;
  - conferir célula a célula;
  - nunca sobrescrever o `.gsheet`.
- Correção vai como DRAFT ou redline, e nada é enviado sem aprovação explícita.
- Trilha de auditoria fora do entregável (`_audit/`). O entregável diz só a regra vigente.
- Separar papéis: quem roda não interpreta, quem pesquisa propõe, o auditor tenta derrubar e o humano decide nos portões.
- Gravar o progresso por etapa (`.done/<stage>`, `HANDOFF.md`) para retomar sessões longas.

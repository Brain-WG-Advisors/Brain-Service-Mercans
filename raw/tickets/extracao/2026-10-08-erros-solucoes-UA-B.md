# Erros e soluções — Ucrânia, specs SR e payslip (grupo UA-B)

- **Grupo:** UA-B (Ucrânia: Report Specs D1, 4DF, D5, D6, 1-PV mensal, 1-PV trimestral e Payslip)
- **Data:** 2026-10-08
- **Nota:** Análise de erros e soluções; complementa a extração factual de 2026-10-02.
- **Arquivos lidos** (`raw/tickets/txt-utf8/`):
  - SR-160: `27`, `84`, `96`
  - SR-161: `98`
  - SR-162: `28`, `97`
  - SR-163: `29`, `95`
  - SR-340: `03` (txt com 1 byte, ou seja, imagem; o PDF original não pôde ser renderizado neste ambiente, sem `pdftoppm`/`pdfimages`; o conteúdo do 03 foi tomado da extração de 2026-10-02, **não conferido contra a imagem**) e `11`
  - SR-414: `82`, `100`
  - SR-415: `83`, `101`
- **Também consultados:** `extracao/2026-10-02-tickets-UA.md`, `correcoes.md`, `mercans-pipeline/shared/country_failure_log.md` (F1–F47).
- **Limites gerais de leitura:**
  - Nos tickets, as planilhas (Google Sheets) e as imagens/tabelas coladas não vêm no texto. Quase todo "achado" de revisão (coluna V da spec) está **na planilha**, não no ticket; só aparece aqui o que o texto do ticket diz ("queries reverted", "Done" etc.).
  - Datas "aprox." são derivadas de "X days/months ago" relativo à data de exportação do snapshot.
  - Equipe: Lily Li = BA (revisora); Michael Mukosi John = Dev; Wallisson = Research Analyst/autor das specs.

---

## SR-160 — Spec D1 (Contribuição Social Unificada / ESV): revisão BA/Dev
- **País / Cliente / Tipo / Prioridade:** Ucrânia / n/a (país) / Statutory Reports, Report Spec (fase "Final Review Phase - Business Analyst") / Major
- **Snapshots lidos:** 27 (2026-08-20), 84 (2026-09-25), 96 (2026-09-28)
- **Estado no último snapshot (96):** In Review; assignee Wallisson (no 84 estava com Michael); Dev Michael. Em aberto: pedido da Lily de "true XML sample" (o atual é schema).
- **Linha do tempo:**
  - ~2026-03/04 (aprox.): Lily converte a spec para Google Sheets, pede para atualizar o link na descrição e checar queries da coluna V. Pergunta onde a coluna "D1 Insured Category (КЗО)" do WTC é usada no relatório D1.
  - ~2026-04/05: Wallisson responde: a coluna КЗО do WTC não mapeia para nenhum campo do XML do D1; o Graf 8 (T1RXXXXG8) vem do HR (`$hr.esv_category_code`). A coluna foi renomeada para "Insured Person Type for ESV Engine" (filtro de motor; 20 = contrato de trabalho, 21 = contrato civil/ЦПД). "Queries reverted".
  - ~2026-05: Lily: duas queries pendentes; volta a perguntar se a coluna КЗО pode ser removida do WTC.
  - ~2026-05/06: Wallisson: queries da linha 27 resolvidas. **WTC V3.2**: WT 62964 (Top-up to minimum wage), célula R388, coluna "D1 Accrual Type Code (КТН)" de vazio para **13** (base: MFU Порядок №4 §IV). **DD V3.3**: novo campo Part-Time Indicator (`part_time_indicator`, **CM**, Integer 0/1), linha 20, ordinal 15.1; Graf 22 = 1 se indicador = 1; default 1 se `employment_contract_type = 3`.
  - Lily: o campo deve ser **M**, não CM, pois não pode virar 1 automaticamente; todos os campos devem ser configurados manualmente. Wallisson: "agreed". Lily: "Done".
  - ~2026-07: Lily pergunta em que idioma o dev deve desenvolver os relatórios ucranianos (D1, D5, D6, 4DF). Michael pergunta onde estão na spec os campos "Sum Graf 16/17/18/19/20 (all rows)" (print que não vem no texto).
  - ~2026-07/08: Wallisson responde: relatórios em **ucraniano** (requisito estatutário); os totais **estão** na spec (rodapé, seção D, linhas 37-41, posições 031-035, XML R01G16-R01G20), mas o BA Mapping dizia "Total of [field]" em vez de SUM; foi reescrito como SUM explícito (G16 = SUM Graf 16 / PE 58133; G17 = Graf 17 / PE 58130; G18 = Graf 18, 0 se não houver top-up; G19 = 0,00; G20 = Graf 20 / PE 2550, conciliar com o ESV pago à DPS). Base: MFU Порядок (estrutura do D1); Law 2464-VI; Law 77-VIII (ESV do empregado abolido em 2016-01-01); XSD da DPS.
  - ~2026-07/08: Michael configura o relatório em acceptance (`ua-unified-social-contribution`, entidade REF-02-370) e anexa template XML e amostra.
  - ~2026-08-20: Lily pergunta como preencher HZ/HZN/HZU e C_DOC_STAN a partir de `document_type_flag_d1` (ex.: 011) e aponta que HBOS e HBUH não existem na spec, pedindo verificar se há outros elementos faltando.
  - ~2026-08/09: Wallisson responde: mesmo padrão do D6/4DF (anexos do mesmo formulário J05). 011 → HZ=1/C_DOC_STAN=1; 012 → HZN=1/C_DOC_STAN=2; 013 → HZU=1/C_DOC_STAN=3 (os outros ficam 0). Só HBOS (nome do diretor) e HBUH (nome do contador) faltavam; adicionados (par igual a HKBOS/HKBUH). 57 tags conferidas. "Updated spec attached."
  - ~2026-09-24: Lily manda o Dev aplicar: BA mapping das linhas 4 e 27 atualizado; campos novos nas linhas 46 e 47. Pede a Wallisson que inclua `$legal_entity_hr.chief_accountant_name` no DD.
  - ~2026-09-25: Wallisson adiciona `chief_accountant_name` (Country Fields linha 77, ordinal 9.5; mesma estrutura de Director/Authorized Person), alimenta a tag HBUH.
  - ~2026-09-28: Lily pede um "true XML sample" (o atual é schema).
- **Problema relatado:** revisão da spec D1 pela BA/Dev: uso de coluna do WTC que não alimenta o relatório; ausência de indicador de tempo parcial; totais de rodapé "não encontrados"; tags de cabeçalho não explicadas e faltando; campo de contador-chefe ausente no DD; XML de amostra que é só schema.
- **Erro identificado (achados de revisão e correção):**
  1. **Coluna КЗО do WTC sem uso no D1 e com rótulo enganoso.** Artefato: WTC (versão anterior à V3.2). Erro nosso (rótulo/propósito da coluna). Correção: renomeada para "Insured Person Type for ESV Engine" e documentado que é filtro de motor. Pergunta se podia ser removida: sem resposta registrada [ficou aberto].
  2. **WT 62964 sem código D1 Accrual Type (КТН).** Artefato: WTC antes da V3.2. Erro nosso (campo vazio). Correção: = 13, WTC V3.2.
  3. **DD sem Part-Time Indicator.** O Graf 22 do D1 não tinha de onde sair (tipo de contrato não identifica tempo parcial em contratos fixos/indeterminados). Artefato: DD antes da V3.3. Erro nosso. Correção: campo criado na DD V3.3.
  4. **Obrigatoriedade do Part-Time Indicator CM com default automático.** Artefato: DD V3.3. Erro nosso, apontado pela Lily. Correção: M, sem default.
  5. **BA Mapping do rodapé como "Total of [field]".** Artefato: Report Spec D1. Erro nosso de redação/ambiguidade (o conteúdo existia). Correção: SUM explícito com PE e XML.
  6. **Idioma do relatório não definido na spec.** Artefato: Report Spec D1 (e D5/D6/4DF). Lacuna nossa. Correção: esclarecido por comentário (ucraniano); não consta que tenha sido escrito na spec.
  7. **Tags HBOS e HBUH ausentes** (de um XSD de 57 tags). Artefato: Report Spec D1. Erro nosso. Correção: tags adicionadas.
  8. **Regra HZ/HZN/HZU/C_DOC_STAN não documentada.** Artefato: Report Spec D1 (linha 4, Document Type Flag). Erro nosso (regra de população ausente). Correção: regra explicada por comentário; a Lily atualizou o BA Mapping da linha 4.
  9. **DD sem `chief_accountant_name`.** Artefato: DD. Erro nosso (HBUH sem fonte de dado). Correção: campo criado, ordinal 9.5.
  10. **XML "de amostra" é o schema.** Artefato: anexo da spec/ticket. Não consta de quem é o anexo (a Lily o pede a Wallisson). [INCERTO: se o arquivo em questão é o template do Dev ou um anexo nosso].
  11. Linhas 4 e 27 do BA Mapping e linhas 46-47 novas (09-24): conteúdo das mudanças não consta no texto.
- **Causa raiz:**
  - Itens 1-3, 9: construção do artefato. WTC/DD/Report Specs foram feitos em sequência, sem checagem de que cada campo/tag do relatório tinha origem no DD/WTC (sincronização entre artefatos, etapa de design). [INCERTO quanto ao processo exato; inferido do padrão].
  - Item 4: decisão de design (default automático) sem considerar que a obrigatoriedade CM exige regra manual; correção da BA.
  - Itens 5, 8: a spec descrevia o que o campo é, não a regra de construção (população).
  - Item 7: a spec foi montada a partir do que parecia necessário, não da lista completa de tags do XSD (conferência contra o schema só ocorreu após a revisão). [INCERTO]
- **Solução aplicada:** ver itens acima: WTC V3.2, DD V3.3, `chief_accountant_name`, spec atualizada com HBOS/HBUH e SUM explícito, dados por Wallisson entre ~2026-04 e 2026-09-25. Base legal: MFU Порядок №4 §IV (КТН 13); Law 2464-VI; Law 77-VIII; XSD DPS R01G16-R01G20.
- **O que não aconteceu / ficou aberto:**
  - True XML sample (pedido em 09-28).
  - Remoção da coluna КЗО: sem resposta registrada.
  - Idioma ucraniano: não consta registro na spec.
  - O ticket continua "In Review" (Due Date 2026-03-31 já vencida há ~6 meses).
  - Conferência de 2 queries do ciclo 1 ("Two queries pending") só indireta.
- **Tipo de erro:** T3, T4, T5, T8, T12 (T12 para: base legal do КТН 13 só dada depois, por comentário).
- **Lição para o pipeline:** F25 (naming drift Specs × DD) e F45 (cross-artifact) cobrem a falta de origem dos campos; escapou porque a spec foi revisada pela BA contra o sistema, não contra o DD. F9 (thin spec schema) e F5 (population rules thin) cobrem a regra de HZ/HZN/HZU e o rodapé. F40 (defeito de builder copiado em todas as specs) descreve exatamente o que ocorreu em D1/4DF/D5/D6: **as 4 specs vieram sem HBOS/HBUH**. NOVO: **Cobertura de tags do XSD** — um check automático "toda tag do XSD da DPS aparece como linha da spec" teria pegado HBOS/HBUH e, no D5/D6, TIN/C_DOC*/etc.

---

## SR-161 — Spec 4DF (Imposto de Renda Pessoal): revisão BA e QC do XML
- **País / Cliente / Tipo / Prioridade:** Ucrânia / n/a / Statutory Reports, Report Spec ("Final Review Phase") / Major
- **Snapshots lidos:** 98 (2026-09-28)
- **Estado no último snapshot:** In Review; assignee Wallisson. Em aberto: pedido de true XML sample e lista de defeitos de QC no XML do Dev.
- **Linha do tempo:**
  - ~2026-04: Lily converte a spec para Google Sheets e pede para checar queries da coluna V; pede o mesmo para as outras specs ucranianas.
  - ~2026-04: Wallisson: "queries reverted and DD updated" (o que mudou no DD não consta).
  - ~2026-05: Lily: "All queries resolved"; link atualizado.
  - ~2026-06: Michael configura `ua-personal-tax` em acceptance, anexa template e amostra (REF-02-370).
  - ~2026-08-20: Lily repete as perguntas do D1 sobre HZ/HZN/HZU/C_DOC_STAN (`document_type_flag_4df`) e HBOS/HBUH. Wallisson: mesmo padrão do D6, anexos do J05; mesmo mapeamento 011/012/013; HBOS/HBUH adicionados; 54 tags conferidas.
  - ~2026-09-24: Lily manda o Dev atualizar o BA mapping da linha 4 e criar campos para as linhas 60 e 61. ~09-25: Michael atualiza o template.
  - ~2026-09-28: Lily testa na entidade REF-04-125 (Ukraine QC Entity) e lista defeitos (abaixo); pede true XML sample a Wallisson.
- **Problema relatado:** XML gerado diferente da spec; tags de cabeçalho faltando na spec.
- **Erro identificado:**
  1. HBOS/HBUH ausentes na spec 4DF (54 tags). Erro nosso. Corrigido.
  2. Regra HZ/HZN/HZU/C_DOC_STAN não documentada. Erro nosso. Corrigido por comentário; linha 4 atualizada pela Lily.
  3. QC da Lily (09-28), **todos do Dev/configuração, não da spec**, exceto onde indicado:
     - U4 mapeado para `document_type_flag_d1` em vez de `_4df` (config. do Dev, copiado do D1).
     - U21/U22: mapeamento de 58120 para 58582; "não encontrei onde 58552 e 58582 são usados na configuração" (Dev). Também as abas Gross Income, Income Code 101 e 102 tiveram códigos de PE atualizados (tabelas não constam no texto) [INCERTO: se a causa foram códigos 4DF novos do WTC V3.x; ver SR-415 item 1].
     - U17-U23: teste com renda 101 + 126 gerou só 101; código de renda não pode ter default 101 (Dev).
     - T1RXXXXG06D sai com traços (05-01-2026), deve ser 05012026; formato DDMMAAAA (Dev; a spec define o formato).
     - R02G03I vazio; "deveria ser 1 conforme o mapeamento da spec?" (pergunta da Lily; sem resposta).
     - T1RXXXXG09 = 0 deve ser omitido (Dev, U27).
     - Separador de milhar em G03A/G03/G04A/G04/G5A/G5 e totais R01G* (21,600.00); a spec manda sem separador (Dev).
- **Causa raiz:** HBOS/HBUH: spec incompleta frente ao XSD (ver SR-160). Defeitos de QC: implementação do Dev (copiar configuração do D1, ignorar formatos de data/números da spec). O padrão "U4 aponta para D1" se repete no D5 (SR-162), indicando que o Dev clonou a config do D1 [INCERTO: inferência a partir dos dois tickets].
- **Solução aplicada:** spec corrigida (tags); QC repassado ao Dev. Não consta correção do Dev no snapshot.
- **O que não aconteceu / ficou aberto:** todos os defeitos de QC (Dev); resposta sobre R02G03I; true XML sample (conosco); origem dos PEs 58552/58582 na configuração.
- **Tipo de erro:** T5, T10 (defeitos de implementação sem erro da spec), T3 (PEs 58582/58120 [INCERTO]).
- **Lição para o pipeline:** F40 (defeito compartilhado em todas as specs) para HBOS/HBUH; F4 (formato) e F5 (população) para formato de data e omissão de G09=0, que **estavam na spec mas o Dev não seguiu**. Escapou porque não há validação do XML gerado contra a spec: NOVO: **Teste do XML gerado contra o XSD e as regras de formato da spec (data DDMMAAAA, sem separador de milhar, omissão de zero)** — análogo ao C35 (validação por validador da autoridade) já previsto no F40.

---

## SR-162 — Spec D5 (Registro de relações de trabalho): campos HR, gatilho e QC
- **País / Cliente / Tipo / Prioridade:** Ucrânia / n/a / Statutory Reports, Report Spec / Major
- **Snapshots lidos:** 28 (2026-08-20), 97 (2026-09-28)
- **Estado no último snapshot:** In Review; assignee Wallisson. Em aberto: true XML sample; HDDGV/HNDGV; defeitos de QC no Dev.
- **Linha do tempo:**
  - ~2026-04/05: Lily converte para Sheets; queries da coluna V; Wallisson "queries reverted".
  - ~2026-05/06: "One query pending" (roxo); Wallisson reverte; Lily "Done".
  - ~2026-07/08: Michael lista 23 campos "a criar pela compliance" (ex.: `ukrainian_citizenship_flag::key`, `labour_registry_person_category::key`, `special_seniority_code`, `document_type_flag_d5`, RNOCPP etc.) e diz que alguns já foram criados por support ticket, mas muitos faltam. ~07-22 (29 dias antes do 08-20, aprox.): Lily responde que **todos já estão no DD** (coluna U, BA Mapping); pede configuração em acceptance; já estão configurados.
  - ~2026-07/08: Michael configura `ua-labour-relations-register` (REF-02-370).
  - ~2026-08-20 (09-28 no snapshot 97): Lily pergunta (1) gatilho = `labour_event_period_start_date` no período?; (2) HZ/HZN/HZU/C_DOC_STAN; (3) HBOS/HBUH.
  - ~2026-08/09: Wallisson responde: gatilho **orientado a eventos** (Порядок §5 p.34, Report Matrix), 7 tipos de evento (início/fim de contrato, novo posto, transferência, serviço militar, licença-maternidade/cuidado), conferido contra o XML de teste; HZ... igual ao D1; HBOS/HBUH faltavam, adicionados; também adicionados TIN, C_DOC, C_DOC_SUB, C_DOC_VER, C_DOC_TYPE, C_DOC_CNT, C_REG, C_RAJ, C_STI_ORIG, LINKED_DOCS, SOFTWARE, PERIOD_TYPE; PERIOD_MONTH, PERIOD_YEAR, D_FILL provavelmente duplicam as linhas 6, 5 e 33 (adicionados, a confirmar). "Spec v3."
  - ~2026-09-24: Lily formaliza o gatilho (início de evento no período OU fim por categoria: 1/2/9 = `last_working_date`; 3 = `contract_end_date`; 4-8 = `labour_event_period_end_date`; se nenhum empregado cumpre, D5 não é gerado), atualiza BA Mapping da linha 4 e manda desenvolver as linhas 36-54. ~09-25: Michael atualiza o template.
  - ~2026-09-28: QC da Lily (abaixo) e pedido de true XML sample a Wallisson.
- **Problema relatado:** gatilho ambíguo; 23 campos "faltando" (na verdade existiam); tags do cabeçalho não explicadas ou ausentes; XML gerado com defeitos.
- **Erro identificado:**
  1. **Gatilho da Lily interpretado como "só data de início"** (erro de entendimento da BA/Dev, não nosso): a spec era orientada a eventos. Mas a spec não deixava isso explícito o bastante para a BA, que precisou de uma regra formal por categoria (T5). Corrigido: a regra completa saiu da Lily, derivada da nossa resposta.
  2. **Campos "ausentes" do DD** (Michael): campos existiam no DD V3.x e na coluna U da spec; falha de comunicação/ configuração (campos criados no DD mas não no sistema acceptance). Erro: nenhum nosso (T10).
  3. **Tags ausentes:** HBOS, HBUH, TIN, C_DOC, C_DOC_SUB, C_DOC_VER, C_DOC_TYPE, C_DOC_CNT, C_REG, C_RAJ, C_STI_ORIG, LINKED_DOCS, SOFTWARE, PERIOD_TYPE (12+ tags) e possivelmente duplicatas PERIOD_MONTH/YEAR/D_FILL. Erro nosso. Corrigido na spec v3; duplicatas pendentes.
  4. **HDDGV/HNDGV**: em schema (nillable), não na spec. Erro nosso potencial, [INCERTO] pois ainda sem resposta.
  5. **QC (Dev), 09-28:** U4 mapeado para `document_type_flag_d1` (devia ser `_d5`); **C_DOC_SUB gerado 106, devia ser 105**: a Lily manda atualizar U39 para 105 (a spec/mapa dela define 105; o valor 106 pode ter vindo de erro do Dev [INCERTO]); C_DOC_STAN vazio; espaço antes do 1 em `<HZ> 1</HZ>`; HFILL "28-09-2026" (formato errado); T1RXXXXG12 vazio; campos `::key` sem valor default.
- **Causa raiz:** spec montada com subconjunto de tags (mesma causa do SR-160, etapa de construção do artefato); gatilho descrito por categoria no Report Matrix mas não no nível de campo (comunicação); Dev clonou a config do D1.
- **Solução aplicada:** spec v3 (Wallisson, ~2026-08/09): tags adicionadas, gatilho confirmado com base no Порядок §5 p.34; Lily e Michael ajustaram o template em 09-25. QC do Dev sem retorno no snapshot.
- **O que não aconteceu / ficou aberto:** true XML sample; HDDGV/HNDGV; confirmação das duplicatas PERIOD_*/D_FILL; correções de QC pelo Dev; resposta sobre o valor 105 vs. 106 (quem estava certo é só a Lily, sem confirmação nossa no ticket).
- **Tipo de erro:** T5, T4 (campos/tags), T10, T6 (nenhum; gatilho não é escopo).
- **Lição para o pipeline:** F10 (sub-formulários ausentes) e F40 (lacunas copiadas em todas as specs) pela cobertura de tags; F5 (population rules thin) pelo gatilho; F43 (populações especiais) pelas 7 categorias de evento/pessoa. Escapou porque o gatilho estava no Report Matrix e não por campo. NOVO: **Gatilho de geração escrito por extenso na própria spec** e **checagem de tags do XSD** (ver SR-160).

---

## SR-163 — Spec D6 (Tempo de serviço especial): campos, gatilho e option mapper
- **País / Cliente / Tipo / Prioridade:** Ucrânia / n/a / Statutory Reports, Report Spec / Major
- **Snapshots lidos:** 29 (2026-08-20), 95 (2026-09-28)
- **Estado no último snapshot:** In Review; assignee Wallisson. Em aberto: true XML sample.
- **Linha do tempo:**
  - ~2026-04/05: Lily converte para Sheets, queries na coluna V; Wallisson reverte.
  - ~2026-05/06: Lily: ainda há queries (roxo); pede criar `$legal_entity_hr.d6_duration_unit` no DD UA. Wallisson: feito. Lily: **o option mapper "D6 Duration Unit" não foi criado** na aba Country Option Mappers. Wallisson: feito (~2026-06/07).
  - ~2026-07: Michael lista 9 campos "a criar pela compliance"; Lily: todos já estão no DD (coluna U); configurados em acceptance. Michael configura `ua-special-seniority` (~07-23/27).
  - ~2026-08-20: Lily: (1) gatilho = `special_seniority_code` não nulo?; (2) HZ/HZN/HZU/C_DOC_STAN; (3) HBOS/HBUH. Pede que as mudanças sejam feitas **na mesma spec da descrição da tarefa, sem criar documento separado, destacando em outra cor**.
  - ~2026-08/09: Wallisson: gatilho em **duas camadas** (empregador com posto de trabalho qualificado, Порядок §6; por linha, `special_seniority_code` não nulo). HBOS/HBUH adicionados (vazios no XML, preenchidos pela assinatura digital); mais TIN, C_DOC..., PERIOD_TYPE etc.; PERIOD_MONTH/YEAR/D_FILL prováveis duplicatas das linhas 6/5/30 (a confirmar). "Spec v3."
  - ~2026-09-24: Lily ao Dev: gatilho = `special_seniority_code` não nulo; BA Mapping da linha 4; linhas 33-51 novas.
  - ~2026-09-28: Lily pede true XML sample.
- **Problema relatado:** campos D6 no DD; option mapper faltando; gatilho; tags de cabeçalho.
- **Erro identificado:**
  1. **Campo `d6_duration_unit` ausente no DD** (apontado pela Lily). Artefato: DD UA. Erro nosso. Corrigido.
  2. **Option mapper "D6 Duration Unit" ausente.** Artefato: DD UA, Country Option Mappers. Erro nosso. Corrigido.
  3. **HBOS/HBUH + 12 tags de cabeçalho ausentes** (spec v2 → v3). Erro nosso. Corrigido.
  4. **Gatilho só em uma camada na leitura da BA** (a spec tinha duas camadas, mas a Lily só leu a segunda). Mal-entendido de comunicação; sem erro nosso, mas a regra não estava clara por campo [INCERTO].
  5. **Pedido do Dev:** "Chief Accountant RNOCPP" mapeado para `director_signatory_rnocpp` na lista do Dev (item 9). Possível erro de mapeamento do Dev ou da spec; não tratado no ticket [INCERTO]. O mesmo texto aparece na lista do SR-162 com `chief_accountant_rnocpp` correto, o que sugere erro de cópia do Dev no SR-163.
  6. Lily pediu **alterar a spec original** (não criar documento separado, destacar alteração): sugere que houve ou risco de versões paralelas da spec [INCERTO].
- **Causa raiz:** construção do artefato (DD e option mapper criados depois da spec; etapa de design/sincronização); tags de cabeçalho: ver SR-160.
- **Solução aplicada:** d6_duration_unit + option mapper (Wallisson, ~2026-06/07); spec v3 (~2026-08/09); fonte do gatilho: Порядок §6.
- **O que não aconteceu / ficou aberto:** true XML sample; confirmação das duplicatas PERIOD_*/D_FILL; mapeamento RNOCPP do contador-chefe (item 5); conteúdo das linhas 33-51 não consta.
- **Tipo de erro:** T3 (código/rótulo), T4, T8, T5, T10.
- **Lição para o pipeline:** F1 (option mapper mismatch DD × Specs) e F25 (DD criado depois da spec, nomes/campos fora de sincronia) cobrem diretamente; escaparam porque o check C2 não cobre campo `legal_entity_hr` novo criado na revisão. NOVO: **Todo campo `$legal_entity_hr.*::key` citado em spec tem option mapper na aba Country Option Mappers** (check automático spec × DD).

---

## SR-340 — Payslip UA: inconsistência template × Payslip Spec 1
- **País / Cliente / Tipo / Prioridade:** Ucrânia / n/a / Statutory Reports, Payslip / Normal
- **Snapshots lidos:** 03 (~2026-08-04, imagem; **não conferido**, conteúdo vem da extração anterior), 11 (2026-08-10)
- **Estado no último snapshot:** In Progress, fase de desenvolvimento, Dev Michael, assignee Wallisson. Due Date 2026-08-31.
- **Linha do tempo:**
  - ~2026-07-10: ticket criado por Wallisson (1 mês antes de 08-10).
  - ~2026-07-23 (17 dias antes de 08-10): Lily deixa uma query (um print): "Employer Address / EDRPOU" [conforme extração anterior: o EDRPOU está em `company_tax_identification_number`; perguntou se aparece junto do endereço, e formato; nota da spec "ESV payer number normally = EDRPOU post-2016 [VERIFY WITH RA]"]. [Não conferido no 03.]
  - ~2026-08-05: Wallisson: "queries reverted".
  - ~2026-08-10: Michael pede o mapeamento HRB de "ESV Payer Number" (dados do empregador) e "division" (dados bancários). Lily: esses campos não estão na "Payslip Spec 1". Michael: estão nos templates "Ukraine (EN)" e "Ukraine (UK)". Lily a Wallisson: os campos do template são inconsistentes com os da spec.
- **Problema relatado:** campos do template do payslip (EN e UK) que não existem na Payslip Spec 1.
- **Erro identificado:** **inconsistência entre template do payslip (EN/UK) e Payslip Spec 1** (ESV Payer Number no empregador; division nos dados bancários). Artefato: Payslip (template × spec). De quem: nosso artefato (inconsistência interna) [INCERTO qual dos dois está certo; o template pode ter vindo do modelo Mercans/base e não ser nosso]. Também EDRPOU/endereço sem formato definido e marcado "[VERIFY WITH RA]" no próprio texto da spec, o que indica pergunta ao RA deixada no artefato entregue (conforme extração anterior).
- **Causa raiz:** [INCERTO] os templates foram construídos a partir do modelo (tipo Espanha) e a spec foi reduzida/alterada sem sincronizar; `ESV payer number` possivelmente considerado igual ao EDRPOU, sem decidir; o marcador [VERIFY WITH RA] mostra pesquisa não fechada.
- **Solução aplicada:** não resolvido no último snapshot (queries 1 revertidas em ~08-05; a inconsistência segue aberta).
- **O que não aconteceu / ficou aberto:** decisão sobre ESV Payer Number e division (incluir ou remover do template); confirmação do [VERIFY WITH RA]; formato do EDRPOU; resposta à inconsistência.
- **Tipo de erro:** T9, T8, T12 (ESV payer number = EDRPOU sem fonte no ticket).
- **Lição para o pipeline:** F45 (consistência entre artefatos) e F6 (open queries unanswered; C8 proíbe "to be verified" em entregáveis) cobrem; escapou porque o check C8 só olha marcadores textuais e não compara os campos do template com os da Payslip Spec 1. NOVO: **Check "cada campo do template do payslip existe na Payslip Spec 1 e vice-versa"**.

---

## SR-414 — Spec Form 1-PV mensal (estatística de trabalho): fonte de "staff" e fórmulas
- **País / Cliente / Tipo / Prioridade:** Ucrânia / n/a / Statutory Reports, Report Spec (fase "Product Mapping Phase - Business Analyst") / Major. Origem: HRBS-12548 (Ukraine Statistic reports).
- **Snapshots lidos:** 82 (2026-09-24), 100 (2026-09-29)
- **Estado no último snapshot:** Open; assignee Wallisson; sem developer; Due Date 2026-09-30.
- **Linha do tempo:**
  - ~2026-09-23/24: Lily pede para checar a coluna V da spec UA-1PV-001 e especificar o formato do arquivo, que falta na Report Matrix.
  - ~2026-09-24: Wallisson: "DD checked": o campo certo para "staff" não é Employment Contract Type e sim **Labour Registry Person Category (D5)**: categorias 1-2 = quadro (escopo r.1070); categoria 3 (CPC) = contrato civil, excluída.
  - ~2026-09-29: Lily responde com novas perguntas: (a) qual categoria é "external part-time"?; (b) formato do arquivo ainda ausente na matriz; (c) campo "No-data indicator": o comentário do RA "worth a direct check if the 2024 text surfaces" é confuso; se precisa de novo campo HR, criar "No-Data Indicator" no DD com option mapper; (d) "Average FTE headcount": o que é "calendar-day average"? Pede fórmula exata e exemplo; (e) confirmar exclusões da população "staff": maternidade (`labour_registry_person_category` = 5), licença-cuidado (4 ou 6), mobilizado/serviço militar (7 ou 8), contrato suspenso/evacuado/paradeiro desconhecido (qual campo HR ou PE?), licença não remunerada ilimitada sob lei marcial (Art. 26(1) da Lei "On Vacations"): não existe no DD/WTC, pode usar 79410 Unpaid Leave Payout?; (f) campos de "deviation flag" de headcount (≥25%) e de salário médio (≥10%): criar campo HR para o texto do motivo? A coluna O cita option mapper na aba Field Options que não existe.
- **Problema relatado:** spec de 1-PV com campos não mapeáveis ao DD/WTC, fórmulas vagas, formato de arquivo omitido, option mapper citado e inexistente.
- **Erro identificado:**
  1. **Fonte de "staff" errada na versão original** (Employment Contract Type). Artefato: Report Spec UA-1PV-001. Erro nosso. Corrigido por Wallisson (comentário; spec: não consta a versão).
  2. **Formato do arquivo ausente na Report Matrix.** Artefato: Report Spec. Erro nosso (T5). Aberto no 09-29.
  3. **Option mapper citado na coluna O sem existir** na aba Field Options. Artefato: Report Spec/DD. Erro nosso. Aberto.
  4. **"external part-time" sem categoria no DD.** Lacuna de modelo (DD não distingue). Aberto.
  5. **"Average FTE headcount / calendar-day average" sem fórmula nem exemplo.** Erro nosso (T7). Aberto.
  6. **Exclusões de "staff" sem campo no DD/WTC** (suspenso/evacuado, licença ilimitada de lei marcial). Erro nosso de escopo de DD (T4, T6). Aberto.
  7. **Limiares 25% e 10% de desvio sem fonte no ticket** (T12) e **comentário do RA confuso/ambíguo** ("worth a direct check if the 2024 text surfaces"): texto interno do RA vazou para o artefato. Aberto.
  8. Campo de motivo do desvio sem campo HR. Aberto.
- **Causa raiz:** (1) construção da spec antes de olhar o DD (F25-like), sem passagem de verificação; (2-3) campos de matriz/lista deixados para depois; (4-6) o DD foi desenhado para os relatórios D1/D5/4DF e não para estatística; (7) pesquisa não fechada transferida para o artefato [INCERTO].
- **Solução aplicada:** apenas a correção do item 1 (Labour Registry Person Category). Nada mais no último snapshot.
- **O que não aconteceu / ficou aberto:** todas as perguntas (a)-(f) de 09-29; o prazo 2026-09-30 estava a 1 dia.
- **Tipo de erro:** T4, T5, T6, T7, T12.
- **Lição para o pipeline:** F4 (formato de arquivo) e F5 (population rules thin); F43 (populações especiais: licenças, mobilizados); F42 (exemplos digitados, não computados) pela falta de fórmula com exemplo; F6 (consultas abertas/"worth a direct check"). Escaparam porque a spec foi entregue com marcadores de pesquisa e sem validação contra o DD. NOVO: **Cada população especial/exclusão da spec precisa apontar um campo HR/PE existente ou virar item de DD** (check de rastreabilidade spec → DD).

---

## SR-415 — Spec Form 1-PV trimestral (estatística de trabalho): formato e WTC × Wage Fund Classification
- **País / Cliente / Tipo / Prioridade:** Ucrânia / n/a / Statutory Reports, Report Spec (fase "Product Mapping Phase - Business Analyst") / Major. Origem: HRBS-12548.
- **Snapshots lidos:** 83 (2026-09-24), 101 (2026-09-29)
- **Estado no último snapshot:** Open; assignee Wallisson; Due Date 2026-09-30.
- **Linha do tempo:**
  - ~2026-09-23/24: Lily pede para checar a coluna V da UA-1PV-002 e especificar o formato do arquivo.
  - ~2026-09-24: Wallisson: coluna V respondida na coluna W; **formato adicionado à Report Matrix (linha 16): XML, template Derzhstat S0301121, assinado com KEP, envio exclusivamente eletrônico via Кабінет респондента (Law 2524-IX, art. 10(4))**.
  - ~2026-09-29: Lily: (1) alteramos códigos 4DF de alguns PEs no WTC; ela os atualizou na aba **Wage Fund Classification** e pergunta se as colunas E e F dessa aba também mudam; (2) coluna V marcada em vermelho para checar.
- **Problema relatado:** formato do arquivo ausente na matriz; spec dependente de códigos 4DF do WTC.
- **Erro identificado:**
  1. **Formato de arquivo ausente na Report Matrix.** Artefato: Report Spec UA-1PV-002. Erro nosso. Corrigido (linha 16).
  2. **Desalinhamento entre WTC (códigos 4DF alterados) e aba Wage Fund Classification da spec.** Artefato: Report Spec × WTC. Erro de sincronização, nosso (a mudança no WTC não foi propagada; a BA corrigiu os códigos). A pergunta sobre colunas E/F está sem resposta.
- **Causa raiz:** propagação (WTC mudou depois de a spec ser construída: WTC v3.x com mudanças de 4DF nos PEs, HRBS-12181/14331 [INCERTO a qual versão se refere]); formato omitido por esquecimento (mesma lacuna do SR-414).
- **Solução aplicada:** formato (Wallisson, ~2026-09-24; base Law 2524-IX art. 10(4)); coluna V respondida na coluna W (conteúdo na planilha). A BA atualizou os códigos 4DF.
- **O que não aconteceu / ficou aberto:** resposta sobre colunas E/F; nova coluna V em vermelho; confirmar se a Wage Fund Classification precisa de revisão completa após a mudança do WTC.
- **Tipo de erro:** T5, T8.
- **Lição para o pipeline:** F27 (artefato posterior não ressincronizado após correção) e F45 (consistência entre artefatos e versões) cobrem; F4 pelo formato. Escaparam porque a mudança de códigos 4DF no WTC não disparou revisão das specs que os citam. NOVO (ou extensão do F27): **tabela de dependências WTC → specs** (todo PE com código 4DF citado em spec dispara revisão quando o código muda).

---

## Tabela-resumo

| ID | País | Tipo(s) | Artefato | Resolvido? | F-xx / NOVO |
|---|---|---|---|---|---|
| SR-160 | UA | T3, T4, T5, T8, T12 | Report Spec D1; WTC V3.2; DD V3.3 | Parcial (spec e DD corrigidos; falta true XML sample; ticket In Review) | F25, F45, F9, F5, F40; NOVO: cobertura de tags do XSD |
| SR-161 | UA | T5, T10, T3 [INCERTO] | Report Spec 4DF; config. do Dev | Parcial (spec corrigida; QC do Dev aberto) | F40, F4, F5; NOVO: teste do XML gerado contra a spec/XSD |
| SR-162 | UA | T5, T4, T10 | Report Spec D5 v3; DD | Parcial (spec v3; QC do Dev e HDDGV/HNDGV abertos) | F10, F40, F5, F43; NOVO: gatilho por extenso na spec |
| SR-163 | UA | T3, T4, T8, T5, T10 | Report Spec D6 v3; DD (d6_duration_unit + option mapper) | Parcial (spec v3; falta true XML sample) | F1, F25; NOVO: option mapper para todo campo `::key` |
| SR-340 | UA | T9, T8, T12 | Payslip (templates EN/UK × Payslip Spec 1) | Não resolvido | F45, F6; NOVO: check template × Payslip Spec |
| SR-414 | UA | T4, T5, T6, T7, T12 | Report Spec UA-1PV-001 | Não (só a fonte de "staff" corrigida; 6 perguntas abertas) | F4, F5, F43, F42, F6; NOVO: rastreabilidade spec → DD |
| SR-415 | UA | T5, T8 | Report Spec UA-1PV-002 (Wage Fund Classification) | Parcial (formato adicionado; colunas E/F e coluna V abertas) | F27, F45, F4; NOVO: dependência WTC → specs |

## Padrões recorrentes no grupo

- **Tags/campos do XSD ausentes na spec:** HBOS e HBUH faltaram nas 4 specs do formulário J05 (D1, 4DF, D5, D6), e D5/D6 ainda perderam 12 tags de cabeçalho. A mesma lacuna em specs-irmãs é o padrão do F40 (defeito de builder copiado em cada spec). Só foi descoberta na revisão da BA.
- **Campo ou option mapper criado depois da spec e fora de sincronia com o DD:** `d6_duration_unit` e seu option mapper (SR-163), `part_time_indicator` (SR-160), `chief_accountant_name` (SR-160), option mapper citado e inexistente na 1-PV (SR-414), campos "ausentes" que na verdade existiam no DD mas não no sistema (SR-162/163). Padrão F1/F25/F45.
- **Regra de população/gatilho implícita:** D5 (7 tipos de evento, regra por categoria), D6 (duas camadas), mapeamento 011/012/013 → HZ/HZN/HZU, "calendar-day average" do 1-PV. Em todos, a BA precisou perguntar e a resposta veio por comentário, não escrita na spec (F5, F43, F42).
- **Defeitos de implementação do Dev aparecendo como "erro da spec":** U4 apontando para `document_type_flag_d1` em 4DF e D5, formatos de data/número ignorados (05012026, sem separador de milhar), valores zero omitidos, defaults para `::key`. Sem validação do XML gerado contra a spec/XSD estes erros só aparecem no QC manual da Lily; o ciclo "true XML sample" (pedido nos 4 tickets em 09-28) mostra que também falta amostra de saída real do nosso lado.
- **Marcadores de pesquisa aberta no artefato entregue:** "[VERIFY WITH RA]" no payslip (ESV payer number = EDRPOU), comentário do RA "worth a direct check if the 2024 text surfaces" no 1-PV, limiares 25%/10% sem fonte no ticket (F6/C8, T12).
- **Mudança no WTC não propagada às specs:** códigos 4DF alterados no WTC e a aba Wage Fund Classification do 1-PV trimestral (SR-415); PEs 58582/58120 e abas de renda da 4DF atualizadas pela Lily (SR-161) [INCERTO se mesma causa]. Padrão F27/F45.
- **Formato de arquivo omitido na Report Matrix:** SR-414 e SR-415 (duas specs 1-PV pela mesma mão), análogo ao F4. Corrigido primeiro no SR-415.
- **Prazos vencidos / tickets parados em "In Review" ou "Open":** D1, 4DF, D5, D6 com Due Date 2026-03-31 ainda em revisão em 2026-09-28; 1-PV com Due Date 2026-09-30 e perguntas abertas em 09-29.

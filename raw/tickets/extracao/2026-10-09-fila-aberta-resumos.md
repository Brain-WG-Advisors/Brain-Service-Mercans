# Fila aberta atribuída a nós: resumos (2026-10-09)

> Tickets abertos atribuídos a nós no YouTrack (consulta `for: me #Unresolved`, API, 2026-10-09). PDF com resumo + ticket completo em `Documents\youtrack_tickets\105–109`. Foco: conhecimento a absorver.

## SR-414 — UA Form 1-PV Monthly (Labour Statistics Report) - SPEC
PDF: `youtrack_tickets\105 - Ticket - SR-414 - UA Form 1-PV Monthly (Labour Statistics Report) - SPEC.pdf`

**País / tipo:** Ucrânia · Spec de relatório estatístico (Derzhstat) · Prioridade Major · Estado: **Open** · Fase: Product Mapping (BA) · Due date: 2026-09-30 (vencido)
**Quem pede:** Lily Li (BA) · **Responsável:** Wallisson (Research Analyst)

### O que está sendo pedido
Fechar a spec **UA-1PV-001** (formulário 1-PV mensal, estatística do trabalho) para a BA mapear e o Dev construir.

### Histórico
- **09-23 (Lily):** responder a coluna V e informar o formato do arquivo na Report Matrix.
- **09-24 (nós):** o campo certo não é o Employment Contract Type, e sim **Labour Registry Person Category (D5)**. As categorias 1 e 2 são "staff"; a categoria 3 (contrato civil, CPC) fica fora.
- **09-29 (Lily):** perguntou como identificar o "external part-time", qual é o "no-data indicator", qual é a fórmula do FTE médio, como mapear as exclusões da população staff e se as flags de desvio (25% e 10%) precisam de campo.
- **09-29 (nós):**
  - **External part-time:** categoria D5 = 2 com a flag "Simultaneous Main + Concurrent" = 0.
  - **Formato:** XML no template Derzhstat **S0301016**, assinado com KEP.
  - **Sem dados no período:** campo novo "1-PV No-Data Reason" no DD.
  - **Fórmula do FTE:** na célula W12.
  - **Maternidade (5/7) e childcare (4/6):** o mapeamento da Lily está correto.
  - **Mobilizados:** identificados pelo **WT 79417** (não pelas categorias 7 e 8).
  - **Contrato suspenso:** hoje não há campo para isso.
  - **WT 79410:** não serve, porque cobre todas as licenças não remuneradas.
  - **Justificativas de desvio:** texto livre, sem campo novo.

### O que falta (último pedido, 10-09)
1. A aba "XML Sample File" não está em XML e a spec não lista os elementos XML. É preciso entregar uma **amostra XML real** e os **elementos** correspondentes.
2. Revisar a coluna V nas linhas marcadas em vermelho.

### Conhecimento a absorver
- **1-PV mensal:** XML no template Derzhstat S0301016, assinado com KEP.
- **População "staff":** categorias D5 1 e 2. A categoria 3 (CPC) fica fora; o external part-time é a categoria 2 com a flag de vínculo simultâneo = 0.
- **Ficam fora do staff:** licença-maternidade, childcare e mobilizados (WT 79417). Contrato suspenso ainda não tem campo no DD (lacuna).
- **Lição:** a spec saiu com "XML" no formato, mas sem amostra XML nem elementos. É o mesmo erro do SR-415, feito pela mesma mão.

## SR-415 — UA Form 1-PV Quarterly (Labour Statistics Report) - SPEC
PDF: `youtrack_tickets\106 - Ticket - SR-415 - UA Form 1-PV Quarterly (Labour Statistics Report) - SPEC.pdf`

**País / tipo:** Ucrânia · Spec de relatório estatístico (Derzhstat) · Prioridade Major · Estado: **Open** · Fase: Development (Dev) · Due date: 2026-09-30 (vencido)
**Quem pede:** Lily Li (BA) · **Responsável:** Wallisson (Research Analyst)

### O que está sendo pedido
Fechar a spec **UA-1PV-002** (1-PV trimestral) para o desenvolvimento.

### Histórico
- **09-23 (Lily):** responder a coluna V e informar o formato do arquivo.
- **09-24 (nós):** formato XML no template Derzhstat **S0301121**, assinado com KEP, entregue **só eletronicamente pelo Кабінет респондента** (Lei 2524-IX art. 10(4)).
- **09-29 (Lily):** depois da nossa mudança de códigos 4DF no WTC, perguntou se as colunas E e F da aba Wage Fund Classification também mudam.
- **09-29 (nós):** as colunas E e F dependem da **natureza do pagamento**, não do código 4DF.
  - 62180, 62181 e 79406 continuam EXCLUDED (Instrução nº 5, p. 3.8 e 3.2).
  - **62942** passa a EXCLUDED: pagamento a FOP não é salário, e FOP fica fora da linha 7040.
  - **65808** (seguro de vida, BIK) passa a SOCIAL_IND / 5080 (p. 2.3.4).
- **10-09 (Lily):** "Mapping done".

### O que falta (10-09)
1. Entregar a **amostra XML real** e os **elementos XML** na spec. A aba de amostra hoje não está em XML.
2. Confirmar se as **linhas 6 a 16 valem só para staff**.

### Conhecimento a absorver
- **1-PV trimestral:** XML no template Derzhstat S0301121, assinado com KEP, entregue só pelo Кабінет респондента (Lei 2524-IX art. 10(4)).
- **Classificação do fundo de salário** (Instrução nº 5): depende da natureza do pagamento, não do código 4DF.
  - Severance (62180/62181) e 79406: EXCLUDED.
  - Pagamento a FOP (62942): EXCLUDED.
  - Seguro de vida BIK (65808): SOCIAL_IND / 5080.
- **Lição:** quando muda um código no WTC, as specs que dependem dele precisam ser revistas (padrão F27/F45).

## SR-162 — UA D5-001 LabourRelations
PDF: `youtrack_tickets\107 - Ticket - SR-162 - UA D5-001 LabourRelations.pdf`

**País / tipo:** Ucrânia · Spec do relatório D5 (Registro unificado de relações de trabalho, formulário J05) · Prioridade Major · Estado: **In Review** · Fase: Final Review (BA) · Due date: 2026-03-31 (vencido)
**Quem pede:** Lily Li (BA) · **Dev:** Michael Mukosi John · **Responsável:** Wallisson

### O que está sendo pedido
Concluir a revisão final da spec **UA-D5-001** e o teste do relatório já configurado em acceptance.

### Histórico
- **abr–mai:** a spec foi convertida para Google Sheets, e as perguntas da coluna V foram respondidas.
- **07-17 a 07-24:** o Dev listou 23 campos HR e de Legal Entity. A Lily mostrou que já existiam no DD. Relatório configurado em acceptance com o código **`ua-labour-relations-register`** (entidade REF-02-370).
- **08-20 (Lily):** perguntou sobre o gatilho do relatório, o mapeamento HZ/HZN/HZU/C_DOC_STAN e as tags HBOS/HBUH, que faltavam.
- **08-24 (nós):**
  - **Gatilho:** o D5 é disparado por evento, em 7 tipos (Порядок §5 p.34).
  - **HZ/HZN/HZU/C_DOC_STAN:** mesmo mecanismo do D1.
  - **Spec v3:** com HBOS/HBUH e mais 12 tags de cabeçalho.
- **09-24 (Lily):** regra final do gatilho:
  - o D5 é gerado se `labour_event_period_start_date` cai no período **ou** se a data de fim cai no período, conforme a categoria:
    - categorias 1, 2 e 9: `last_working_date`;
    - categoria 3: `contract_end_date`;
    - categorias 4 a 8: `labour_event_period_end_date`.
- **09-28 (Lily, QC do Dev):**
  - U4 deve apontar para `document_type_flag_d5`;
  - C_DOC_SUB = 105;
  - C_DOC_STAN está vazio;
  - há um espaço em `<HZ> 1`;
  - o formato de data do HFILL está errado;
  - todo campo `::key` precisa de valor padrão.
- **09-28 (nós):** amostra XML real no lugar do schema; HDDGV e HNDGV acrescentados nas linhas 55–56.

### O que falta (10-09, Lily → nós)
1. Linhas 55–56 (HDDGV/HNDGV): o tamanho do segundo campo está em branco. Confirmar se **não precisam de mapeamento e podem ficar em branco**.
2. Linhas 37–51: estão marcadas "Blank" no mapeamento, com tamanho 0, mas a amostra XML traz valores (ex.: `<C_REG>26</C_REG>`). Confirmar se o "Blank" está certo.
3. Do lado do Dev: corrigir os defeitos do QC de 09-28.

### Conhecimento a absorver
- **Código do relatório:** `ua-labour-relations-register`.
- **Gatilho do D5:** disparado por evento, com a data de fim definida pela categoria (regra acima).
- **Mapeamento HZ/HZN/HZU/C_DOC_STAN:** o mesmo do D1; por exemplo, 011 → HZ=1 / C_DOC_STAN=1.
- **Lição:** a spec saiu sem tags do XSD (HBOS/HBUH) e com uma amostra que não batia com o próprio mapeamento (linhas 37–51). Um check "toda tag do XSD tem linha na spec e a amostra bate com o mapeamento" teria pegado isso.

## HRBS-12110 — Please review this report matrix for Congo
PDF: `youtrack_tickets\108 - Ticket - HRBS-12110 - Please review this report matrix for Congo.pdf`

**País / tipo:** Congo (Brazzaville) · Service Request · Cliente: Baker Hughes Congo (Implementation) · Prioridade Medium · Estado: **In Progress**
**Quem pede:** Daniel Kelvin Balogun · **Suporte:** Pradeep Duraisamy · **Responsável:** Wallisson

### O que está sendo pedido
Revisar a **Reporting Matrix do Congo** (anexo `Reporting Matrix - Congo.xlsx`) e dizer se ela pode ir para o cliente.

### Histórico
- **07-21:** pedido aberto.
- **08-13 (nós):** **não está pronta para o cliente.**
  - A aba "note" descreve relatórios do **Senegal** (État 1024, TRIMF, CFCE, IPRES).
  - As abas CG-CNSS e CG-DAS-001 estão vazias.
  - A CG-DGID-001 diz que a entrega é por XML/télédéclaration, mas a declaração DGID do Congo é **feita no portal**. Não existe XML/XSD para nenhuma declaração do Congo.
  - O total de ITS da CG-DGID-001 (279.300 XAF) está cerca de **10 vezes abaixo**: bate com o valor anual de um único empregado, não com o total mensal de 120 empregados (≈ 2.793.000).
- **10-06 e 10-07 (Pradeep):** avisou que o ticket seria fechado por falta de resposta.
- **10-07 (Daniel):** "still need".

### O que falta
Daniel diz que ainda precisa de ajuda, mas **não disse o quê**, e não anexou uma matriz corrigida. O próximo passo é entender o que ele espera: revisar uma nova versão ou receber os pontos para corrigir.

### Conhecimento a absorver
- **Relatórios do Congo:** ITS + TUS para a DGID e PVID/PF/AT-MP para a CNSS. A entrega é **pelo portal**; não há XML/XSD.
- **Lição:** a matriz do cliente foi montada a partir de um modelo de outro país (Senegal). Ao revisar a matriz de um cliente, conferir resíduos de outro país (padrão do check C42) e conferir os totais por ordem de grandeza.

## HRBS-15253 — ACCENTURE LITHUANIA - Compliance (Calculation & Reporting) Check
PDF: `youtrack_tickets\109 - Ticket - HRBS-15253 - ACCENTURE LITHUANIA - Compliance (Calculation & Reporting) Check.pdf`

**País / tipo:** Lituânia · Question / Inquiry · Cliente: Accenture Lithuania (Live/BAU, cliente novo) · Prioridade Medium · Estado: **Open** · Resolution Time: 2026-10-01 (vencido)
**Quem pede:** Kevin Gunawan (escopo de configuração) · **Responsável:** Wallisson

### O que está sendo pedido
O Kevin vai configurar a Lituânia e quer saber **o que o sistema cobre hoje**. Pede que cada linha de uma lista de cerca de 70 itens seja marcada como **S** (suportado e configurado), **C** (suportado, precisa de configuração), **M** (manual) ou **N** (não suportado). A lista tem 5 partes:
1. **Cálculo:** bases GPM × Sodra, contribuições do empregado e do empregador, GPM com faixas de 2026 e NPD, teto anual da Sodra e piso MMA, ausências, e casos como arredondamento, proração e A1.
2. **Relatórios mensais:** SAM com SAM3SD/SAM3SDP (.ffdata, EDAS), GPM313 (.ffdata, EDS), payslip, arquivo bancário, GL e conciliação.
3. **Relatórios por evento:** 1-SD, 2-SD, 9-SD, 12-SD, 13-SD, NP-SD e PT.
4. **Relatórios anuais:** GPM312 com GPM312L e GPM312U, e a virada de parâmetros no fim do ano.
5. **Perguntas gerais:** quem mantém as estruturas .ffdata, se existe ambiente de teste, como funcionam as correções, se há uma planilha de parâmetros aprovada e se já existe cliente de referência.

### Histórico
- **09-28 (nós):**
  - **Baseline de Compliance** (Drive › Country Folders › Lithuania): CCG 2026, WTC V3.0 e DD V3.0 (aprovados em jun/jul de 2025); specs de SAM (com SAM3SD e SAM3SDP), GPM313 e GPM312 (com L e U); payslip em EN e LT. **O CCG 2026 não tem registro de versão nem aprovação formal.**
  - **Versões dos formulários:** SAM v07; GPM313 conforme VA-105, de 2025-11-20; GPM312 conforme VA-24, de 2026-03-26.
  - **Não especificados por Compliance:** os formulários de evento da Sodra (1-SD, 2-SD, 9-SD, 12-SD, 13-SD, NP-SD e PT; só existe material de referência de 2025 para 1-SD, 2-SD e NP-SD) e a integração (geração .ffdata, canais EDAS/EDS e envio de teste).
  - **Não são de Compliance:** a marcação S/C/M/N e os arquivos de banco, GL e conciliação ficam com Configuration e Product.
  - **Correções, segundo o CCG:** a Sodra é reenviada no mês de referência; o GPM é tributado no mês do pagamento, sem reenvio; SAM entregue com atraso exige o formulário PT, código 01. Não há documentação para corrigir o GPM313 depois de uma mudança no GPM312.
  - **Referências de 2025:** QC e mapeamento G2N da folha de 2025 (CT-3410, CT-3568).
- **10-02 (Kevin):** pediu uma call; diz que será urgente quando o cliente começar.

### O que falta
1. **Marcar a call** com o Kevin.
2. Configuration e Product devolverem a matriz S/C/M/N.
3. **Lacunas de Compliance:**
   - specs dos formulários de evento da Sodra;
   - registro de versão e aprovação do CCG 2026;
   - regra de correção do GPM313 depois de mudança no GPM312.

### Conhecimento a absorver
- **Baseline da Lituânia:** CCG 2026, WTC/DD V3.0, specs de SAM, GPM313 e GPM312 e payslip EN/LT.
- **Versões dos formulários:** SAM v07; GPM313 VA-105 (2025-11-20); GPM312 VA-24 (2026-03-26).
- **Regras de correção:** Sodra é reenviada no mês de referência; o GPM é tributado no mês do pagamento; SAM atrasado exige PT com código 01.
- **Lacunas registradas:** formulários de evento da Sodra (1/2/9/12/13-SD, NP-SD, PT) e integração .ffdata/EDAS/EDS.
- **Lição:** um cliente novo pediu uma matriz de cobertura que deveria existir antes do pedido (padrão F54, saída do scaffolder).

# Ucrânia (UA-A): erros e soluções nos tickets HRBS

- **Grupo:** UA-A (Ucrânia, tickets HRBS): 11 tickets.
- **Data da análise:** 2026-10-08.
- **Nota:** Análise de erros e soluções; complementa a extração factual de 2026-10-02 (`raw/tickets/extracao/2026-10-02-tickets-UA.md`).
- **Arquivos lidos (`raw/tickets/txt-utf8/`):**
  - HRBS-12181: 05, 14, 36
  - HRBS-12368: 15, 19, 22
  - HRBS-12548: 08
  - HRBS-12631: 04, 25, 46, 93
  - HRBS-13389: 23
  - HRBS-13392: 24
  - HRBS-13499: 31
  - HRBS-14255: 47, 62
  - HRBS-14324: 48, 49, 51
  - HRBS-14331: 50, 53, 58, 63, 76, 81
  - HRBS-15216: 89
- **Outras fontes conferidas:** `correcoes.md` e `mercans-pipeline/shared/country_failure_log.md` (F1 a F47).
- **Convenções:**
  - Datas "~" são derivadas de "X days ago" e têm margem de ±1 dia.
  - O YouTrack imprime "Updated/Commented ... ago" relativo à data de exportação.
  - Cada snapshot é um subconjunto cumulativo do anterior. Conferi linha a linha que nenhum comentário aparece só num snapshot intermediário; as diferenças entre eles são só de cabeçalho/estado.
  - [INCERTO] marca inferência.
  - Cliente de todos os tickets, salvo indicação: Altium Ukraine. Quem abre quase todos os tickets é Nataliia Hahan (especialista local de payroll UA do lado Mercans [INCERTO: papel exato não declarado]).
  - Papéis, conforme os tickets: Wallisson dos Santos Gomes = Compliance (nós). Lily Li = BA. Vaishnavi Mane = configuração/leave module. Mohit Jain = Head of Compliance Product. Abarna Khaliq = Sr. Specialist-Configurations. Archit Naik = L2 Support.
  - Nenhum dado pessoal de empregados consta nos tickets lidos.

---

## HRBS-12181 — Atualização do WTC: BIK "só PIT" e gross-up com coeficiente 1.219512
- **País / Cliente / Tipo / Prioridade:** UA / Altium (REF-04-254) / Service Request, Tier 3, Support Group Compliance Support / Medium. Fase Live/BAU. SLA status "Breached".
- **Snapshots lidos:** 05 (2026-08-05), 14 (2026-08-12), 36 (2026-09-01).
- **Estado no último snapshot:** Resolved, assignee Lily Li (snapshot 36). Última atualização de Lily ~2026-08-18. Nataliia disse em ~2026-08-17: "if we done with the WTC, you can close that ticket". O WTC final (com a matriz de tributação de benefícios) foi publicado pela Lily em ~08-13.
- **Linha do tempo:**
  - ~2026-07-21: Nataliia abre o pedido. Quer uma série nova de WTs BIK com PIT=Sim e Military Tax e USC=Não (8 códigos: 65816, 65805, 65806, 65810, 65808, 65812, 65720, 62224) e gross-up com 1.219512 para benefícios não monetários.
  - ~07-22 a 08-02: Vaishnavi pede a série e lista códigos 4DF que não achou no WTC de compliance: 103, 109, 124, 157, 169 (linhas rosa). Pede também "Mobilization (without pay)" e confirmação sobre 160/126 (gifts; "25% threshold"). Lily repassa a Wallisson duas vezes.
  - ~08-03 (WTC v3.5, Wallisson): não construir a série "PIT only, no Military Tax", sem base legal. Códigos 62610-619, 65630, 58113, 65801, 65804 já estão PIT/Military=Sim e USC=Não. 103/109/157 "não são códigos de payroll de empregado". 124: usar 125. 169: confirmar com o cliente. Mobilization criado como 79417. Aponta que os números de código da Lily não batem com os do ticket.
  - ~08-03: Nataliia concorda: o coeficiente vale só para a base do PIT; não precisa de WT separado, é fórmula.
  - ~08-05: Nataliia dá um exemplo (benefício 2000, base PIT 2360, PIT 439,03). Lily avisa que o v3.5 chegou com nome V3.4 e sem controle de versão.
  - ~08-06 (WTC v3.7, Wallisson): "Gross-up confirmed and built into the WTC: 65816 now has the formula". Corrige o exemplo (base 2.439,02; PIT 439,02; Military 100 sobre 2.000). Nomeia 65805/65806/65808/65810/65812 e confere 65720/62224. Pergunta ao cliente sobre o Art. 170.9 PKU (despesas de representação documentadas e publicitárias isentas de PIT). Nataliia pergunta sobre indexação (CPI mensal e base month por empregado).
  - ~08-10: Lily observa que o gross-up hoje entra nas duas bases e que só 2 PEs foram renomeados no v3.7, que estava em Excel. Converte para Google Sheets.
  - ~08-10/11 (Wallisson): base legal Art. 164.5 PKU só para PIT; a base do Military (p. 16-1, pidrozd. 10, rozd. XX) não incorpora o coeficiente. Confessa que a coluna Formula de 65816, 65801 e 65804 está em branco. Conclui que a diferenciação PIT/Military é regra de motor e a sinaliza ao "Drew".
  - ~08-11: Lily pergunta se são só 6 benefícios. Wallisson: não, o gross-up é por categoria (109 WTs com 4DF=126; 51 são placeholders "Benefit Earning" não renomeáveis). Nataliia corrige: o coeficiente vale só para renda não monetária (pp. 164.2.17), e dinheiro ligado à remuneração é 101, não BIK (pp. 14.1.47/14.1.48). Lily informa o limite de 20 PEs de gross-up (Mohit).
  - ~08-12 (WTC v3.8, verde): Wallisson define os 20 PEs (35 códigos), renomeia 65805/65810/65812/65816 e retira a citação do coeficiente de 65806/65808.
  - ~08-13: Lily publica o WTC finalizado e assume o desenvolvimento do gross-up.
- **Problema relatado:** o WTC não tinha série BIK com PIT=Sim e Military/USC=Não, nem mecanismo de gross-up com coeficiente. Vaishnavi não encontrava vários códigos 4DF.
- **Erro identificado:** vários erros nossos, todos no WTC e em respostas:
  - **WTC v3.5:** entregue com nome de arquivo V3.4 e sem controle de versão.
  - **WTC v3.7:**
    - Só 2 PEs renomeados.
    - O changelog dizia que 65801/65804 já tinham o coeficiente na fórmula, mas a coluna estava em branco.
    - A resposta de ~08-06 afirmou "65816 now has the formula", e na resposta seguinte admitiu-se que a fórmula não existia.
  - **Escopo do gross-up:** a resposta de ~08-11 dizia "todos os 109 códigos 4DF=126", e a correção da Nataliia reduziu para os não monetários (20 PEs).
  - **Resposta de ~08-03:**
    - Disse que os códigos de seguro médico/vida (62610-619, 65630 etc.) estavam corretos com USC=Não. O HRBS-14331 mostrou que seguro de vida tem USC=Sim (Poryadok 1170, p. 2, rozd. II). Erro nosso, já registrado em `correcoes.md`.
    - Disse que 157 "não é código de empregado". Em ~09-09 (HRBS-14331) ele foi confirmado e configurado no WT 62942 para civil contractors.
  - **Exemplo do cliente:** a base 2360 estava errada (2.439,02); erro do cliente, corrigido por nós.
  - **Nomes de códigos:** os números de código do ticket (cliente) não batem com o master (apontado por nós e pela Lily). No HRBS-14331 a Nataliia chama 65808 de "Life Insurance (BIK)", enquanto aqui 65808 era "Representation expenses (financial)" [INCERTO: numeração do catálogo do cliente versus master].
- **Causa raiz:**
  - **Controle de versão e renomeação:** processo de entrega (construção do artefato/sincronização). Arquivo novo salvo sobre o nome antigo, changelog redigido sem conferir a célula.
  - **Gross-up:** a resposta inicial assumiu escopo "por categoria" sem testar a condição legal (forma monetária ou não monetária). Foi a segunda leitura da Nataliia contra o PKU que fechou o escopo. Origem em research/design: o WTC global tem flags de incidência, não de base de cálculo, e o desenho PIT/Military ficou sem dono (motor). [INCERTO sobre o desenho final.]
  - **USC do seguro de vida:** a incidência de ESV foi inferida por analogia ao seguro médico, sem ler a norma que isenta só médico e previdenciário (research).
  - **157:** classificado como "fora do payroll" por heurística, sem checar o caso do civil contractor (research/escopo).
- **Solução aplicada:**
  - **Série "PIT only":** rejeitada, com base na lei. Aceita pela Nataliia.
  - **Gross-up:** coeficiente 1.219512 só na base do PIT (Art. 164.5 PKU), Military na base bruta (p. 16-1, pidrozd. 10, rozd. XX PKU). Limitado a 20 PEs (35 códigos Mercans) e só para renda não monetária.
  - **WTC v3.8:** renomeações. Mobilization = 79417. Lily publicou o WTC final.
  - **Implementação:** o desenvolvimento do gross-up (PIT sim, Military não) ficou com Lily/Dev.
- **O que não aconteceu / ficou aberto:**
  - Confirmação da Altium se 65806/65808 são despesas documentadas com finalidade publicitária (Art. 170.9 PKU), o que as tornaria PIT=Não. A pergunta nunca foi respondida no ticket.
  - Pergunta da Nataliia sobre indexação (CPI mensal e base month): sem resposta aqui. O HRBS-13392 responde em parte, via campo "Effective Date of Current Salary".
  - Confirmação de uso do 4DF 169 com o cliente.
  - A regra de motor para PIT/Military não tem confirmação do Dev neste ticket.
  - A explicação pedida pela Vaishnavi sobre 160/126 (gift) não foi respondida de forma direta.
  - O ticket foi fechado com Lily como assignee, mas o desenvolvimento do gross-up estava em andamento.
  - Os 51 placeholders "Benefit Earning" continuam sem nome.
- **Tipo de erro:** T2, T3, T8, T1 (USC do seguro de vida), T6 (157), T12.
- **Lição para o pipeline:**
  - F7 (WTC wage type tax codes wrong) e F20 (WTC gaps and invalid tax codes): cobrem códigos de tributação errados. Escaparam porque a verificação C9 olha a tabela de incidência, não a base de cálculo, e porque seguro de vida foi tratado por analogia.
  - F45 (cross-artifact consistency on facts and versions): v3.5 com nome V3.4 e changelog sem conferir a célula.
  - F27 (downstream artifact not re-synced): changelog e planilha divergentes.
  - NOVO: "base de cálculo por imposto (flags não expressam bases diferentes)". Um check automático teria cobrado, para toda linha de Category=Benefit, a base de cada imposto (PIT, Military, USC) declarada numa coluna/regra de motor, e rejeitado um changelog que cite fórmula inexistente (conferir a célula citada).

---

## HRBS-12368 — Data Dictionary e Master Data de empregados (Ucrânia)
- **País / Cliente / Tipo / Prioridade:** UA / Altium / Service Request, Tier 3, Compliance Support / Medium. Fase Live/BAU.
- **Snapshots lidos:** 15 (2026-08-12), 19 (2026-08-13), 22 (2026-08-17).
- **Estado no último snapshot:** Paused, SLA Exempt, assignee Wallisson (2026-08-17). Pendente nosso: pedido da Nataliia de apagar o option mapper de Region.
- **Linha do tempo:**
  - ~2026-07-27: Nataliia abre o ticket com uma lista de ~30 colunas do Master Data a revisar contra o DD (laranja = revisar).
  - ~07-29 a 08-04: Abarna Khaliq pede acesso à planilha e ao DD para avaliar se os campos são de nível país ou cliente. Nataliia dá acesso e links (~07-29/30).
  - ~08-06: Nataliia cobra andamento.
  - ~08-12: Nataliia reorganiza o pedido ("15 campos faltantes no Country Fields: Ukraine do DD V3.4", 6 com decisão pendente) e anexa o master data de empregados. Lily repassa a Wallisson.
  - ~08-13 (Wallisson, DD V3.5): adiciona em Country Fields 1C Personnel Number, Name (Ukrainian), Email, Suburb, Division (1C Department), Cost Centre (Department), Monthly Salary (UAH) Gross official, Effective Date of Current Salary, FTE (Rate), ESV Rate Effective Date, Disability Certificate, Bank 1 Account Holder. Em ID Information: Passport Issued By e Passport Issue Date. Não adiciona Monthly Salary (USD), por ser lógica de WTC (pediu confirmação).
  - ~08-17: Nataliia pede para apagar o campo de option mapper de Region.
- **Problema relatado:** o DD V3.4 não tinha campos usados na operação de payroll/HR da Ucrânia (número pessoal 1C, nome em ucraniano, dados do passaporte, salário oficial UAH, data de vigência da taxa de ESV, certificado de deficiência, titular da conta). Também pediu ajustes de option mapper (nomes curtos de tipo de contrato "Постійний/Строковий/ЦПХ", Disability Group III, Part-Time Indicator) e Region sem option mapper.
- **Erro identificado:** DD V3.4 incompleto para a operação local (campos faltantes, T4) e option mappers inadequados (Region com mapper de oblasts, T4). Erro do nosso artefato (DD), do ponto de vista do cliente. Não consta erro declarado pela equipe. Duas lacunas na nossa V3.5, vistas no texto:
  - **Insurance Record:** a lista da Nataliia incluía Insurance Record (para sick pay), e a resposta da V3.5 não cita o campo nem explica a não inclusão. Gerou o HRBS-13389 no dia seguinte.
  - **Option mappers:** os itens de option mapper (contract type, Disability Group III, Part-Time Indicator), Job Title (ENG/UKR) e "Street and Building Number" separados não são citados na resposta. Também "Email" foi adicionado sem constar na lista do pedido [INCERTO: pode ter vindo de outra coluna da planilha].
- **Causa raiz:** [INCERTO] o DD V3.4 foi construído a partir da legislação e dos relatórios estatutários, sem reconciliar com o formulário de admissão/Master Data que o payroll local usa. A DD ficou sem os campos operacionais locais e sem tradução e mapeamentos locais. Etapa: design/construção do DD. A ausência de resposta item a item é falha de comunicação.
- **Solução aplicada:** DD V3.5 (~2026-08-13) com 14 campos adicionados. Salário em USD tratado como lógica de WTC (conforme F26).
- **O que não aconteceu / ficou aberto:**
  - Nenhuma resposta sobre Insurance Record (foi parar no HRBS-13389).
  - Nenhuma resposta sobre os option mappers pedidos.
  - Não consta confirmação da Nataliia de que o salário em USD fica no WTC.
  - Pedido de apagar o option mapper de Region (08-17) sem resposta.
  - Decisões de configuração (Division e conta contábil; Cost Centre para o GTN) não detalhadas.
  - A taxa de ESV em si (22%/8.41%) não ganhou campo, só a data de vigência; o HRBS-15216 (~09-25) pede o campo "SSC Rate".
- **Tipo de erro:** T4, T11, T8 (parcial).
- **Lição para o pipeline:**
  - F1 (Option mapper mismatch DD e Specs) cobre mapper, mas só contra os Specs, não contra o master data do cliente.
  - F26 (Calculated/transactional value misclassified into the DD): aplicada corretamente para o salário em USD.
  - NOVO: "DD sem reconciliação com o Master Data/formulário local de payroll". Teria pegado um check que compare as colunas do template de Master Data do país (ou do cliente piloto) com os campos do DD e liste os faltantes antes da entrega.
  - F6 (Open queries unanswered): a resposta deixou itens do pedido sem retorno explícito.

---

## HRBS-12548 — Relatórios estatísticos da Ucrânia (1-PV mensal/trimestral, Pension Fund, relatórios internos)
- **País / Cliente / Tipo / Prioridade:** UA / Altium / Service Request, Tier 3, Compliance Support / Medium.
- **Snapshots lidos:** 08 (2026-08-07).
- **Estado no último snapshot:** Paused, SLA Exempt, assignee Wallisson. Sem resposta nossa no snapshot.
- **Linha do tempo:**
  - ~2026-07-30: Nataliia pede inclusão dos relatórios estatutários 1-PV (mensal e trimestral) e relatórios internos para cruzamento. Anexa os templates (S0301016 e S0301121 e planilhas internas).
  - ~07-30: pede também o relatório do Pension Fund de licença médica (a "Tab. 2" é a mais importante).
  - ~07-31: Lily repassa a Wallisson.
  - ~08-02: Nataliia pede o relatório interno de salário médio (licença médica, férias e viagens).
- **Problema relatado:** os relatórios 1-PV não estavam no escopo de reports; faltavam também relatórios internos e o relatório do Pension Fund.
- **Erro identificado:** erro de escopo do nosso pipeline: relatórios estatutários de estatística do trabalho (1-PV) e o relatório de licença médica do Pension Fund ficaram fora do conjunto de Report Specs (T6). Os relatórios internos e o de salário médio são pedidos de novas specs.
- **Causa raiz:** [INCERTO] o mapeamento de obrigações de reporte da Ucrânia (scope manifest/Report Matrix) cobriu declarações tributárias e de seguro (D1, 4DF, D5, D6), mas não relatórios estatísticos do Derzhstat. Etapa: research/escopo.
- **Solução aplicada:** nenhuma neste snapshot. A extração de 2026-10-02 indica que o ticket originou as specs SR-414 (1-PV mensal) e SR-415 (1-PV trimestral). O snapshot 08 não mostra esse vínculo; ele vem de outros arquivos do grupo (SR-414 e SR-415 existem em txt-utf8, fora deste grupo).
- **O que não aconteceu / ficou aberto:** relatório do Pension Fund (Tab. 2), relatórios internos de cruzamento e relatório de salário médio: sem registro de tratamento nestes snapshots. Quem constrói relatórios internos (Compliance, Config ou Dev) não consta.
- **Tipo de erro:** T6, T5 (pedido de specs novas), T11.
- **Lição para o pipeline:**
  - NOVO: "relatórios estatísticos/obrigações não tributárias fora do scope_manifest". Teria pegado um check de completude do scope_manifest contra uma lista de obrigações por autoridade (tributária, previdenciária, estatística, trabalhista).
  - F2 (Out-of-scope codes leaked) e F19 (HR-scope report included in payroll handover) cobrem o excesso de escopo, não a falta.
  - F24 (Stale scope/mandate document): relacionado.
  - O erro posterior no SR-414 (Staff mapeado por Employment Contract Type em vez de Labour Registry Person Category, registrado em `correcoes.md`) vem do mesmo problema de mapeamento em specs novas. Está fora deste grupo de arquivos.

---

## HRBS-12631 — Relatório de reserva de férias, salário médio e revisão do CCG
- **País / Cliente / Tipo / Prioridade:** UA / Altium / Service Request, Tier 3, Compliance Support / Medium.
- **Snapshots lidos:** 04 (2026-08-05), 25 (2026-08-19), 46 (2026-09-07), 93 (2026-09-28).
- **Estado no último snapshot:** Pending on reporter, assignee Lily Li (2026-09-28). Pendências abertas: "como criar o relatório de reserva de férias no HRBlizz".
- **Linha do tempo:**
  - ~2026-08-03: Nataliia pede cálculo automático de reserva de férias por empregado (dias de direito, usados e restantes; 24 dias/ano da admissão) e relatório exportável.
  - ~08-03: Lily responde que dias e saldo podem virar PE 79xxx no WTC mas não são calculados no payroll, pois são do leave module. Aciona Vaishnavi.
  - ~08-05: Nataliia pede ao Wallisson as regras de salário médio (12 meses para férias, licenças e donor; 2 meses para viagens).
  - ~08-05 (Wallisson, WTC v3.6, CCG Module 8 v1.1): férias = 12 meses (§7). Donor leave = 2 meses (§8; LC Art. 124; WT 79414). Business trip = 2 meses (WT 79415; maior entre a média de 2 meses e a diária do mês, LC Art. 121 §4). Sick leave = 12 meses, mas pela Postanova 1266. Seção de salário média do CCG dividida em 12 e 2 meses. Código de tipo de acréscimo do D1 para 79414/79415 marcado TBC.
  - ~08-06: Nataliia pergunta se o ticket pode ser fechado.
  - ~08-10/11: Nataliia aponta 3 erros do CCG (prazo de PDFO/ML, seção da semana 53, frequência do 4DF), depois mais 3 (proração, base mínima do ESV na admissão/desligamento, citação do Art. 115) e depois ESV de deficiência, contrato civil e pseudo-código sem is_disabled. Lily repassa.
  - ~08-11 (Wallisson, CCG v1.2): aceita 5 pontos e corrige. Mantém o caveat "(if main place of work)" do contrato civil (discorda da Nataliia). Oferece o rótulo "theoretical" para a seção da semana 53.
  - ~08-18: Nataliia pergunta como criar o relatório de reserva de férias no HRBlizz.
  - 09-07 e 09-28: sem novidades.
- **Problema relatado:** (a) cálculo automático e relatório de reserva de férias; (b) regras de salário médio por tipo de licença; (c) erros no CCG detectados pela Nataliia.
- **Erro identificado:** erros em CCG v1.0/1.1 (nosso artefato), tipo de conteúdo estatutário:
  1. Prazo de PDFO/ML tratado como "3 dias bancários" universal.
  2. Base mínima de ESV proporcional (8.647 x 21/31) no mês de admissão/desligamento, que não se aplica.
  3. Pseudo-código e nota de dev que completavam a base mínima de empregado com deficiência (8.41%).
  4. Proração por dias corridos com citação indevida do Art. 115 (que rege prazo de pagamento).
  5. 4DF tratada como trimestral; para pessoa jurídica é mensal desde 2026-01-01.
  6. Salário médio descrito como fórmula única de 12 meses, sem distinguir 2 meses (donor, viagem) e a regra de sick leave.
  - Pedido de reserva de férias: nenhum erro (pedido de funcionalidade/leave module).
- **Causa raiz:**
  - **Erros 1, 2, 3, 5:** research com regras gerais aplicadas sem testar populações especiais (mês de admissão, deficiência, contrato civil, pessoa jurídica) e sem varredura de mudança legal de 2026 (Law 4536-IX). Etapa: research/CCG.
  - **Erro 4:** citação de artigo que não sustenta a regra. Etapa: fonte/base legal.
  - **Exemplo 8.647 x 21/31:** número digitado, sem recomputar (F42), e a lógica "proporcional" foi inventada pela inferência, e o exemplo só deu certo porque o salário já excedia o mínimo.
  - **Fórmula única de 12 meses:** [INCERTO] simplificação do CCG v1.0.
- **Solução aplicada:** CCG v1.2 (~2026-08-11), com os itens corrigidos nos Modules 1.2, 4.4, 5.1.1, 6.6 e 10.3, e WTC v3.6 (79414, 79415). Bases: TCU Art. 168.1 (confirmado pela DPS); Instruction 449 s.III; DPS 04.02.2026 nº 676/ІПК; cartas 27.05.2019 nº 4340 e 15.04.2019 nº 553; Law 4536-IX e MinFin Orders 4/243/284 (fontes citadas no comentário, não verificadas aqui).
- **O que não aconteceu / ficou aberto:**
  - Relatório e saldo de férias: o leave module (Vaishnavi) não respondeu no ticket. Pergunta de 08-18 sem resposta há 40 dias.
  - Código do D1 para 79414/79415 em TBC.
  - Discordância sobre o caveat de contrato civil (CPC) sem tréplica da Nataliia.
  - Rótulo "theoretical" da semana 53 oferecido e não confirmado.
  - O estado é "Pending on reporter", mas a última pergunta ainda é para nós e a Lily [INCERTO: dono].
  - O sick leave "12 meses" dito aqui contradiz a resposta de ~09-09 no HRBS-14331 (6 meses). Ver aquele ticket.
- **Tipo de erro:** T1, T7, T12, T5 (D1 TBC), T11, T8.
- **Lição para o pipeline:**
  - F43 (Special populations not covered systematically): admissão/desligamento no mês, deficiência e contrato civil estão na matriz de 13 linhas dessa lição.
  - F42 (Worked examples typed instead of computed): exemplo 8.647 x 21/31.
  - F21 (Filing mechanics misunderstood monthly/quarterly): 4DF.
  - F18 (Stale law references in CCG): mudança de 2026.
  - F6 (Open queries unanswered): "TBC" do D1 permaneceu depois da entrega.
  - NOVO: "citação de artigo que rege outro assunto (Art. 115 para proração)". Um check de fidelidade de fonte que leia o trecho citado e confirme que ele sustenta a regra teria pegado. A pipeline tem a passada P2 do QA, mas o texto do artigo não foi lido contra a afirmação.

---

## HRBS-13389 — Campo "Insurance Record" (страховий стаж) ausente do DD
- **País / Cliente / Tipo / Prioridade:** UA / Altium / Service Request, Tier 3, Compliance Support / Medium. Fase Live/BAU.
- **Snapshots lidos:** 23 (2026-08-18).
- **Estado no último snapshot:** Open, assignee Wallisson (atualizado por Archit Naik). Sem resposta nossa.
- **Linha do tempo:**
  - 2026-08-18: Nataliia abre o ticket e pede que Wallisson ajude.
- **Problema relatado:** o Insurance Record (tempo acumulado de seguro social) existe só no template de Master Data ("Insurance Record (for sick pay)") e não no DD V3.4. Define o percentual do auxílio-doença. Pede: incluir no DD, definir o tipo (anos/meses/dias ou data), dizer se é estático ou acumulativo e se se liga à fórmula do sick pay no WTC.
- **Erro identificado:** campo obrigatório do sick pay ausente do DD (T4, nosso artefato). Já fora pedido no HRBS-12368 (item "Insurance Record (for sick pay)"), e a DD V3.5 foi entregue sem ele e sem explicação.
- **Causa raiz:** omissão silenciosa na resposta do HRBS-12368 (comunicação/DD). [INCERTO] possível dúvida sobre se o valor é do DD ou de cálculo.
- **Solução aplicada:** não resolvido no último snapshot.
- **O que não aconteceu / ficou aberto:**
  - Todo o pedido.
  - Contradição entre os dados do ticket: aqui o campo é "cumulativo, informado na admissão, não calculável com os dados do empregador", e no HRBS-12368 ela dizia que "deve ser calculado automaticamente no HRBlizz".
  - Faixas informadas aqui (<5 anos 60%, 5 a 8 anos 80%, 8+ anos 100%) diferem das que ela deu depois no HRBS-14331 (<3 anos 50%, 3 a 5 anos 60%, 5 a 8 anos 70%, >8 anos 100%). Sem fonte nos dois. Precisa de validação contra a lei antes de entrar no CCG/WTC [INCERTO: qual é a correta]. A resposta ao 14331 diz que "faixas foram adicionadas ao CCG", sem conferir a divergência.
  - Relacionado: HRBS-13499 (Insurance Record Type em ano/mês/dia, importante para todos os clientes).
- **Tipo de erro:** T4, T11, T1 (faixas), T12 (sem fonte).
- **Lição para o pipeline:**
  - F6 (Open queries unanswered).
  - F26 (Calculated/transactional value misclassified into the DD): aqui o campo é um dado de entrada legítimo (histórico anterior), não um valor calculado. A regra de F26 não o impede.
  - F5 (Population Rules thin): sem definição de tipo/carga.
  - NOVO: "campo de entrada necessário a fórmula de WTC sem campo correspondente no DD". Um check de rastreabilidade WTC para DD (toda variável de fórmula tem campo de entrada ou é calculada) teria pegado.

---

## HRBS-13392 — 12 meses de histórico de payroll (média salarial no go-live)
- **País / Cliente / Tipo / Prioridade:** UA / Altium / Service Request, Tier 3, Support Group L2 Support / Medium. Fase Live/BAU.
- **Snapshots lidos:** 24 (2026-08-20).
- **Estado no último snapshot:** Open, assignee Archit Naik (L2 Support).
- **Linha do tempo:**
  - ~2026-08-19: Nataliia abre o ticket: precisa de 12 meses de histórico de rendimentos por mês e por empregado para o go-live; pergunta onde e como carregar, se os dias também precisam vir e como fica a carga em lote.
  - ~08-19 (Wallisson): define 3 elementos e os adiciona ao DD num grupo "Historical Payroll Data (Pre-Go-Live Migration)": (1) 12 meses de rendimentos sujeitos a ESV (1266 e 100 ramo 12 meses); (2) 12 meses de dias corridos trabalhados/justificados (denominador do sick pay 1266); (3) 2 meses de dias úteis trabalhados (denominador de viagem, Poryadok 100 ramo 2 meses). Indexação só precisa do base month ("Effective Date of Current Salary").
  - ~08-19 (réplica da Nataliia): (1) no ramo de 2 meses, o denominador são dias úteis do horário da empresa, não dias efetivamente trabalhados; (2) as listas de exclusão do 1266 p.4 e do 100 p.4 não são iguais; o sistema usará dois conjuntos de regras?
- **Problema relatado:** sem 12 meses de histórico, as médias de sick pay, férias e viagens saem erradas no primeiro ano. Precisa saber como carregar.
- **Erro identificado:** na resposta e no DD:
  - Rótulo do 3º elemento: "dias úteis trabalhados" gera denominador errado (deve ser dias úteis do horário). Erro nosso, de definição de campo.
  - Versão: o texto diz "Data Dictionary (v3.7)" e o arquivo anexado é "V3.8"; a Nataliia fala em "before we finalize v3.8" [INCERTO qual é a versão vigente].
  - Elemento 2 (12 meses de dias corridos): o denominador do sick pay segundo a Nataliia no HRBS-14331 é "dias em que o empregado foi segurado, feriados sempre excluídos", e não "dias corridos". [INCERTO] os dois textos podem estar descrevendo a mesma coisa de formas diferentes; a definição do campo precisa ser alinhada.
  - Pergunta técnica central (modelo de carga, template ou backend) não foi respondida; o ticket está em L2 Support.
- **Causa raiz:** o DD foi estendido para suportar a carga sem o critério exato de cada denominador (design/DD). A lista de exclusões ficou sem dono (WTC ou template de carga).
- **Solução aplicada:** grupo "Historical Payroll Data (Pre-Go-Live Migration)" no DD (v3.7/V3.8), com 3 elementos. Base: Procedure 1266 (12 meses antes do mês do evento), Procedure 100 (2 meses para viagens, 12 meses para férias), Procedure 1078 (indexação), conforme o texto do ticket.
- **O que não aconteceu / ficou aberto:** respostas às 2 perguntas da Nataliia; lista completa de WTs excluídos por norma; mecanismo de carga e template; definição final do rótulo do denominador; atualização para V3.8. O ticket seguiu Open com Archit Naik.
- **Tipo de erro:** T4, T7, T11, T8.
- **Lição para o pipeline:**
  - F26 (Calculated/transactional value misclassified into the DD): o histórico de rendimentos por mês é dado transacional; F26 manda tratar acumuladores no WTC (flags de inclusão e YTD-Load). Aqui o DD foi usado para a carga única. É uma exceção justificável de migração [INCERTO], mas a decisão e o trade-off não foram registrados.
  - F45 (cross-artifact consistency on facts and versions): v3.7 versus V3.8.
  - F6 (Open queries unanswered).
  - NOVO: "dois conjuntos de exclusão para a mesma base". Um check que liste, por tipo de cálculo de média, o conjunto de WTs incluídos/excluídos teria exposto a necessidade (as colunas J/K/L do HRBS-14331 tentaram resolver, ver lá).

---

## HRBS-13499 — Data Dictionary GSK Ukraine (campos extras do Master Data)
- **País / Cliente / Tipo / Prioridade:** UA / GSK (GSK Ukraine REF-LE-04-222) / Service Request, Tier 1, Compliance Support / Medium. Fase Implementation.
- **Snapshots lidos:** 31 (2026-08-24).
- **Estado no último snapshot:** Open, assignee Wallisson. Sem resposta nossa. Resolution time estimado "20h", First Reply "-3d" (atraso).
- **Linha do tempo:**
  - ~2026-08-19: Nataliia abre o ticket com 4 campos do Master Data da GSK: Insurance Record Type (for Sick Leave) (ano, mês, dia), Grade 2, City of Work, Manager. Os 3 últimos são específicos do cliente. O primeiro vale para toda a Ucrânia e tem ticket próprio (HRBS-13389).
  - ~08-20: pede nossa orientação.
  - ~08-24: Pradeep Duraisamy atualiza o ticket [INCERTO: sem texto visível].
- **Problema relatado:** campos do Master Data da GSK que faltam no DD.
- **Erro identificado:** nenhum (pedido de informação/escopo do DD). A pergunta é se campos específicos de cliente entram no DD de país ou na configuração do cliente.
- **Causa raiz:** não se aplica. O pedido reflete a ausência de critério declarado para campos de cliente versus país [INCERTO].
- **Solução aplicada:** não resolvido no último snapshot.
- **O que não aconteceu / ficou aberto:** orientação nossa; decisão sobre Grade 2, City of Work e Manager; definição do tipo do Insurance Record (ano, mês, dia), que é o mesmo ponto do HRBS-13389.
- **Tipo de erro:** T11, T6, T4 (Insurance Record).
- **Lição para o pipeline:** não há F-xx diretamente. F2 (Out-of-scope codes leaked) cobre excesso de escopo, e aqui a dúvida é sobre o limite entre DD do país e configuração do cliente. NOVO: "regra escrita de quando um campo é do DD de país e quando é do cliente". Um critério na MANDATE do scaffolder evitaria a pergunta.

---

## HRBS-14255 — Setup de Advance Payroll no nível país (Ucrânia)
- **País / Cliente / Tipo / Prioridade:** UA / Altium Ukraine, GSK Ukraine e SDL Ukraine (campo Client: GSK) / Service Request, Tier 1, Compliance Support / Medium. Fase Implementation.
- **Snapshots lidos:** 47 (2026-09-08), 62 (2026-09-11).
- **Estado no último snapshot:** Pending on reporter, assignee Lily Li.
- **Linha do tempo:**
  - ~2026-09-07: Nataliia pede o setup de Advance Payroll no nível país.
  - ~09-08: Mohit Jain: "No Requirements?".
  - ~09-08 (Wallisson): requisitos estão no CCG (`Ukraine_Country_Configuration_Guide_FY2026_V1_3`): piso de cálculo no Module 4 §4.2 (adiantamento = dias trabalhados x oklad puro, sem bônus; Law 108/95-VR Art. 24); regra de data fixa única no Module 1 §1.2 e Module 13; LC Art. 115 como gatilho de prazo.
  - ~09-11: Mohit: "not enough. Someone needs to share what exactly we need to develop". Lily pede à Nataliia requisitos detalhados e cenários reais.
  - ~09-11: Nataliia explica: dois pagamentos por mês (adiantamento = 1ª metade, pelos dias trabalhados; saldo = fechamento). Qualquer provento pode cair em qualquer metade. Alguns empregadores pagam fixo (ex. 53% do bruto). Licença médica e férias devem ser pagas com impostos junto com a 1ª ou 2ª parte. No HRBlizz: 1º run = adiantamento; 2º run = tudo, com coluna do adiantamento líquido já pago. Saldos de abertura e fechamento por mês.
- **Problema relatado:** configurar o Advance Payroll no nível país.
- **Erro identificado:** nenhum erro estatutário no texto. Falha de adequação: a resposta apontou o CCG (regras legais), mas o time de produto precisava de requisito funcional (dois runs, coluna do adiantamento líquido, saldos). Do nosso lado: o CCG V1.3 não tem esse comportamento. Erro de comunicação/escopo do artefato (T6, T11).
- **Causa raiz:** a pesquisa descreveu o que a lei exige (piso, prazo), e não o que o motor precisa fazer (design). Etapa: design/comunicação.
- **Solução aplicada:** não resolvido no último snapshot. O CCG V1.3 foi indicado como fonte.
- **O que não aconteceu / ficou aberto:** especificação funcional de desenvolvimento (Lily/Mohit com a Nataliia); não está claro se Compliance deve entregar algo além do CCG [INCERTO]. O estado foi para "Pending on reporter" sem prazo.
- **Tipo de erro:** T11, T6.
- **Lição para o pipeline:** F46 (Technical design not derived from the research): o Stage 12 Design deve derivar o comportamento do motor do CCG. Aqui o comportamento (adiantamento, saldos, runs) ficou fora do CCG e do design. NOVO (se F46 não cobrir): "mecânica operacional de pagamento (adiantamento, saldos) sem requisito funcional". Teria ajudado um item na matriz de cobertura (F43) do tipo "múltiplos pagamentos por período".

---

## HRBS-14324 — Fórmulas de salário médio e de benefício adicional (Ucrânia)
- **País / Cliente / Tipo / Prioridade:** UA / sem cliente no campo (Company Name: Altium, GSK, SDL) / Service Request / Medium. Sem fase definida.
- **Snapshots lidos:** 48 (2026-09-08 10:34), 49 (2026-09-08 11:21), 51 (2026-09-08 21:28).
- **Estado no último snapshot:** Open, assignee Wallisson, Compliance Support (antes New, Unassigned, L2). Sem resposta nossa.
- **Linha do tempo:**
  - ~2026-09-08: Nataliia pede que Compliance prepare e documente as fórmulas com base legal: 1.1 férias (Order 100, 12 meses); 1.2 sick leave/maternidade (Order 1266); 1.3 donor leave (2 ou 12 meses?); 1.4 viagem (Order 100 + LC Art. 121, 2 meses); 1.5 indexação (Order 1078; não é média); 1.6 paralisação sem culpa do empregado (2/3, LC Art. 113, base = tarifa/salário); 2. presentes (25% do salário mínimo, p. 165.1.39); 3. gross-up (duas variantes); 4. feriado e dia não útil em dobro (LC Art. 107).
  - ~09-08 21:28: Vaishnavi (FYI) atualiza; ticket vai para Wallisson.
- **Problema relatado:** falta de documento de fórmulas com base legal para a configuração construir a lógica correta.
- **Erro identificado:** nenhum erro declarado (pedido de documentação). Mas várias perguntas já tinham resposta em outros tickets: donor leave = 2 meses (HRBS-12631, ~08-05), gross-up só na base do PIT (HRBS-12181). O repasse do pedido sugere que essas respostas não estavam consolidadas num lugar que a configuração use (T8, T11) [INCERTO].
- **Causa raiz:** [INCERTO] as fórmulas ficaram dispersas entre tickets, CCG e WTC, sem um documento de fórmulas por tipo de pagamento.
- **Solução aplicada:** não resolvido no último snapshot. Respostas parciais em outros tickets.
- **O que não aconteceu / ficou aberto:** tudo. Em particular: variante de gross-up padrão (variante 1 é a posição da autoridade e a que usamos; a decisão da empresa não foi tomada); base horária do Art. 107; tratamento do Art. 113; fórmula de presentes. A variante 2 (K = 100 / (100 - (PIT+Military))) sem fonte. PIT Diia City 5% sem fonte. A afirmação "Order 1266: calculada sobre meses efetivamente trabalhados" fica em tensão com os 6/12 meses divergentes do HRBS-14331.
- **Tipo de erro:** T11, T7, T12, T8.
- **Lição para o pipeline:**
  - F45 (cross-artifact consistency on facts and versions): fórmulas em lugares diferentes.
  - F42 (Worked examples typed instead of computed): fórmulas de média precisam de exemplo calculado.
  - NOVO: "catálogo único de fórmulas de média (período-base, denominador, exclusões) por tipo de pagamento". Teria evitado que o mesmo dado (12/6/2 meses) fosse redito em quatro tickets.

---

## HRBS-14331 — Checagem do catálogo de WTs do cliente (Altium) contra o master
- **País / Cliente / Tipo / Prioridade:** UA / Altium, GSK, SDL (sem cliente no campo) / Service Request, Compliance Support / Medium. SLA status "Breached".
- **Snapshots lidos:** 50 (2026-09-08), 53 (09-09), 58 (09-10), 63 (09-11), 76 (09-18), 81 (09-23).
- **Estado no último snapshot:** Resolved, assignee Wallisson (2026-09-23). A Nataliia fez ~09-22 novas perguntas depois do Resolved, sem resposta.
- **Linha do tempo:**
  - ~2026-09-08: Nataliia pede (1) colunas de inclusão na média para coletar 12 meses de histórico e (2) cross-check das WTs destacadas contra o master.
  - ~09-09 (Wallisson, catálogo do cliente `WTC_Altium_Ukraine_2026_2`): colunas J/K/L já existem para 114 WTs (férias 12 meses; sick leave 6 meses sobre renda sujeita a ESV, 1266 p.4; viagem/donor 2 meses). Linha 5 (presente de aniversário não tributável): PIT/Military de Sim/Sim para Não/Não (4DF 160, p. 165.1.39). Linhas 93 a 101: PIT=Sim e Military=Sim corretos. Linha 17 (Payment Civil Contractors): Sim/Sim/Sim não bate com o p. 177.8, sem código.
  - ~09-09: Nataliia: civil contractor FOP = 4DF 157; seguro de vida é base de ESV (SSC = Sim); lista de 14 itens grossed-up versus benefício; pede dias de feriado/fim de semana na proração de bônus (20 + 3 = 23).
  - ~09-09 (Wallisson, WTC V3_8): colunas W/X/Y para 114 WTs (102 no master); seguro de vida USC corrigido para Sim (Poryadok 1170 p.2 rozd. II); 157 confirmado, configurado no 62942, Não/Não/Não; 14 itens com código; feriado/fim de semana na proração conta +1 dia (Poryadok 100 p.3), regra distinta da média de férias (dias corridos com feriados excluídos).
  - ~09-10: Nataliia pede coluna de WTs faltantes no catálogo do cliente e um segundo código para "65808 Life Insurance (BIK)" com 126 e SSC=Sim. Wallisson: catálogo do cliente fora do escopo (só mantemos o master; encaminhar ao team lead); 65808 já tem 4DF 126 e ESV=Sim; a divisão PIT/Military "65808 base + 65894 grossed-up" existe porque as bases são distintas.
  - ~09-11: Nataliia pede códigos livres para 4 benefícios (representation expenses e English courses) e traz a nota sobre 79401/21142. Wallisson (master atualizado, verde): representação (65806/65807) PIT=Sim sem coeficiente (Art. 170.9); English courses (65720/65803) PIT=Sim com coeficiente (Art. 164.5); 79401 recalcula média nova de 12 meses (Poryadok 100 p.2, segundo parágrafo); 21142 usa a média original, exceções Art. 127 LC e Art. 22 da Lei 504/96. Em seguida diz que 21142 no master é "Unpaid leave deduction", logo o código não pode ser 21142.
  - ~09-14: Nataliia pede a Mohit códigos numéricos para 3 WTs do catálogo do cliente.
  - ~09-16: Lily nota os PEs que Wallisson adicionou, diz que o 65894 está incorreto, pergunta o significado de "Life insurance (no base for military tax of gross up part)". Nataliia atualiza o catálogo e pergunta sobre dedução de dias de férias a mais.
  - ~09-17: Lily: pergunta por que a fórmula de 65894 é 802536457 e lembra que "code assignment is within BA range, not RA". Nataliia pede correção do CCG 8.2 e regras de sick leave no Guide.
  - ~09-18: Nataliia: fórmula do 62209 (compensação de bônus mensal, 18% + 5%, "benefits/0.77"); 65817 (benefício monetário, sem coeficiente); colunas de GTN; WTs cinza.
  - ~09-21 (Wallisson, CCG V1.5 e WTC V3.9 em draft): 65894 não existe, changelog retirado; não criar. Aponta dois desenhos contraditórios para o mesmo mecanismo (regra de motor versus "BIK Gross Up" com PE agregado 58134 nunca construído). Linha de dedução de férias adiantadas com código em branco. 65817 sem coeficiente. CCG 8.2 corrigido. Regras de sick leave adicionadas ao CCG. GTN sem layout estatutário. WTs cinza são do catálogo do cliente. 62209: divisor 0.77 deve ser 0.82.
  - ~09-21: Lily: 65894 removido; daqui em diante PEs novos entram sem código; publica o WTC finalizado.
  - ~09-22: Nataliia, depois do Resolved: 128 só para maternidade 126 + 14 dias; 62180/62181 não devem ser base de ESV; per diem com teto; stock options (cenários A/B); código que "deveria ser 102"; código sem imposto (licença-cuidado?).
- **Problema relatado:** o catálogo do cliente precisava de colunas para a média e tinha WTs com tributação/códigos duvidosos em relação ao master.
- **Erro identificado:** erros em WTC e CCG, de vários donos:
  - **Nosso, WTC/respostas:**
    - Seguro de vida com USC=Não (ver HRBS-12181): corrigido para Sim.
    - Presente de aniversário não tributável Sim/Sim: corrigido para Não/Não [INCERTO: a correção foi no catálogo do cliente ou no master; o texto cita "Row 5" do arquivo do cliente].
    - Civil contractors Sim/Sim/Sim: corrigido para 157, 62942, Não/Não/Não.
    - Changelog afirmando criação do 65894, que não existia: retirado. Resposta anterior de ~09-10 usava "65808 base + 65894 grossed-up" como se existisse.
    - Citação do 79401 ("sub-para. 3") corrigida para p. 2, segundo parágrafo.
    - Divisor 0.77 do 62209: ver [INCERTO] abaixo.
  - **Nosso, CCG:**
    - CCG 8.2 aplicava a lista de exclusão do 1266 p.3 às férias (Poryadok 100).
    - Citava o Social Insurance Fund, fundido ao Pension Fund em 2023-01-01.
  - **Contradição interna não resolvida (nossa):** a média de sick leave aparece como 6 meses (resposta de ~09-09: "Sick leave (K): 6-month base ... Постанова №1266, п. 4"), e como 12 meses em HRBS-12631 (nossa resposta de ~08-05), HRBS-13392 (nossa resposta) e nas regras da Nataliia de ~09-17 ("Last 12 calendar months"). A resposta de ~09-09 ainda afirma que "a história de 12 meses mapeia só para a coluna J", o que quebraria a carga do HRBS-13392. Nenhum snapshot mostra correção.
  - **Escopo:** primeiro editamos o catálogo do cliente (colunas W/X/Y para 114 WTs, correções de linhas), depois dissemos que o catálogo do cliente está fora do escopo [INCERTO se isto mudou o rumo do ticket].
  - **Representação (Art. 170.9):** em 12181 a citação indicava possível isenção de PIT para despesa documentada e publicitária; em ~09-11 foi usada para confirmar PIT=Sim em 65806/65807 (mecanismo de adiantamento a prestar contas). Sem confirmação do cliente do uso real [INCERTO].
  - **Perguntas de ~09-22 (Nataliia, não resolvidas):**
    - Código 128 só para maternidade 126+14 dias, e nós havíamos escrito no CCG que maternidade vai em 128.
    - 62180/62181 (severance, redundancy) como base de ESV.
    - Per diem com PIT/ML=Sim fixo, sem teto (p. 170.9.1 PKU).
    - Stock options com 4DF 101 e ESV=Não, sem combinação válida.
- **Causa raiz:**
  - **Tributação de seguro de vida, presentes, contractors:** inferência por analogia e leitura incompleta de norma (research/WTC). Os checks da pipeline conferem a tabela de incidência contra a fonte oficial só por amostra (F44).
  - **65894 e changelog:** o texto de changelog foi escrito sem conferir o arquivo (construção/sincronização) e o conceito "linha grossed-up" foi herdado do desenho antigo (aba "BIK Gross Up", PE 58134) sem decisão final.
  - **Sick leave 6 versus 12 meses:** [INCERTO] resposta redigida a partir de leitura da Postanova 1266 sem reconciliar com o que o CCG e os outros tickets já diziam. Etapa: research/sincronização.
  - **CCG 8.2 e Social Insurance Fund:** texto CCG redigido por unir listas de normas diferentes e por fonte desatualizada (F18).
  - **Per diem, stock options, severance, 128:** WTC global/herdado do template sem revisão por população/caso (F43, F20).
- **Solução aplicada:**
  - **Correções:** nas linhas e no WTC V3_8/V3.9 e no CCG V1.5 (draft para revisão). Lily finalizou o WTC em ~09-21.
  - **Gross-up:** regra PIT x1.219512 (Art. 164.5), Military e USC sobre o bruto (p. 16-1 pidrozd. 10 rozd. XX).
  - **Novo procedimento:** PEs novos entram sem código; Lily atribui.
  - **Base legal do que foi corrigido:** p. 165.1.39 (presentes); p. 177.8 (FOP); Poryadok 1170 p. 2 rozd. II (USC do seguro de vida); Poryadok 100 p. 2 (79401) e p. 3 (proração e exclusões); Art. 127 KZpP e Art. 22 da Lei 504/96-VR (21142); p. 165.1.1 (maternidade).
- **O que não aconteceu / ficou aberto:**
  - Decisão Compliance/BA/Dev entre regra de motor ou PE agregado 58134 para o gross-up.
  - Divisor do 62209 sem validação (ver abaixo).
  - Sick leave 6 versus 12 meses.
  - As 4 perguntas pós-Resolved: código 128; 62180/62181 como base de ESV; per diem com teto (62570, 65570-65572, 65580-65582, 62965, com 63711, 63712, 75100, 75101); stock options (62890-62899 e 62990-62999: Cenário A com ESV=Sim e gross-up, ou Cenário B fora do payroll, dependendo de resposta do cliente/global team); código 102; item sem imposto.
  - Lista dos códigos Mercans dos "WTs cinza".
  - Códigos novos de dedução de férias.
  - 65817 e 65811/65812 seguem como placeholders sem renomear.
  - Pergunta sobre dias negativos versus código dedicado respondida (código dedicado), mas ainda sem código.
  - Ticket marcado Resolved com perguntas abertas.
- **[INCERTO] sobre o divisor 0.82 do 62209:** a justificativa dada ("o coeficiente vale só para a base do PIT e o Military roda sobre o valor sem gross-up") fala da base do benefício. O 62209 é uma compensação em dinheiro, que o próprio empregado pagaria com 18% + 5% = 23% de imposto (divisor 0.77). A fórmula pedida pela Nataliia ("18%+5% from the benefits/0.77") não está descrita completamente no texto, e a mudança para 0.82 pode estar certa ou errada conforme o objetivo da compensação. Recomendo revalidar antes de tratar a correção como fechada. Na variante 1 da própria Nataliia (HRBS-14324), K = 100/(100-18) = 1/0.82 = 1.219512 só rege a base do PIT do benefício.
- **Tipo de erro:** T1 (seguro de vida, faixas), T2 (USC, 128, ESV de severance, per diem, stock options), T3 (65894, 21142, códigos livres), T7 (62209, médias), T8 (changelog, 6 versus 12 meses), T6 (catálogo do cliente), T10 (códigos do cliente), T12 (citações, Social Insurance Fund).
- **Lição para o pipeline:**
  - F7 (WTC wage type tax codes wrong) e F20 (WTC gaps and invalid tax codes): flags de ESV/PIT erradas e combinações inválidas (101 com ESV=Não). Escaparam porque o WTC é verificado por amostra e por analogia, sem teste de combinações válidas por 4DF (F44).
  - F43 (Special populations): maternidade, civil contractor, per diem, stock options, severance.
  - F45 (cross-artifact consistency): sick leave 6 versus 12 meses; changelog do 65894.
  - F18 (Stale law references in CCG): Social Insurance Fund.
  - F27 (downstream not re-synced): CCG versus WTC versus DD.
  - F41 (research never tested against an independent oracle): as perguntas de ~09-22 mostram uma revisão externa (Nataliia) achando o que a pipeline não achou.
  - NOVO: "matriz 4DF x flags (PIT, ML, ESV, médias) com combinações inválidas rejeitadas". Teria pegado stock options 101+ESV=Não, 128 em linhas de benefício e per diem sem teto.
  - NOVO: "changelog verificado contra o arquivo". Teria pegado 65894.

---

## HRBS-15216 — Checagem do DD: obrigatoriedade, SSC Rate e traduções
- **País / Cliente / Tipo / Prioridade:** UA / Altium (campo Client vazio) / Service Request, L2 Support / Medium.
- **Snapshots lidos:** 89 (2026-09-25).
- **Estado no último snapshot:** New, Unassigned. Sem resposta nossa.
- **Linha do tempo:**
  - 2026-09-25: Nataliia abre o ticket para Wallisson (FYI Mohamed Nabil e Vaishnavi).
- **Problema relatado:** revisar o DD:
  - Não obrigatórios: Contract Start Date, Oblast (Region), Street and Building Number, Postal Code, Supporting Document Reference (D5), TSB Eligibility (pede explicação do que é).
  - Apagar 1C Personnel Number (não será usado por ora).
  - Renomear "ЄСВ Rate Effective Date" para "SSC Rate Effective Date" e criar o campo "SSC Rate" (22% ou 8.41%).
  - Explicar "ESV Category Code (Ознака категорії особи)".
  - Traduzir para o ucraniano os campos sem tradução.
- **Erro identificado:** obrigatoriedade (T4) e completude (T4):
  - Campos marcados como obrigatórios no DD que, para o cliente, não devem ser (6 campos).
  - Campo "SSC Rate" ausente: a V3.5 (HRBS-12368) adicionou só a data de vigência.
  - Campos sem tradução em ucraniano.
  - 1C Personnel Number adicionado por pedido dela em ~08-12 e agora tornado desnecessário (T10).
  - A obrigatoriedade de D5 Supporting Document Reference e TSB Eligibility pode vir dos Report Specs (D5/D1) [INCERTO]; tornar opcional exige conferir a regra de população das specs.
- **Causa raiz:** [INCERTO] obrigatoriedade herdada da regra do relatório estatutário (campo obrigatório no formulário) e aplicada ao campo master. Etapa: design do DD versus Report Spec. O "SSC Rate" nasceu de resposta parcial ao HRBS-12368.
- **Solução aplicada:** não resolvido no último snapshot.
- **O que não aconteceu / ficou aberto:** todo o pedido, incluindo as explicações de TSB Eligibility e ESV Category Code.
- **Tipo de erro:** T4, T11, T10.
- **Lição para o pipeline:**
  - F1 (Option mapper mismatch DD e Specs) e F25 (Report-Specs-built-before-DD naming drift): a relação entre obrigatoriedade no DD e nas Specs deve ser verificada nos dois sentidos.
  - F5 (Population Rules thin): condicional.
  - NOVO: "obrigatoriedade do DD derivada do formulário estatutário sem distinguir obrigatório no relatório e obrigatório no master". Um check que liste cada campo Mandatory=Y do DD e a regra de população da spec que o torna obrigatório teria exposto.
  - Idioma: o scaffolder define LANGUAGE do país, e a tradução ausente indica falta de um check de completude de tradução [INCERTO].

---

## Tabela-resumo

| ID | País | Tipo(s) | Artefato | Resolvido? | F-xx / NOVO |
|---|---|---|---|---|---|
| HRBS-12181 | UA | T1, T2, T3, T6, T8, T12 | WTC v3.4 a v3.8, respostas | Sim (Resolved; dev do gross-up em andamento; Art. 170.9 e indexação sem resposta) | F7, F20, F27, F45; NOVO: base de cálculo por imposto em Benefit |
| HRBS-12368 | UA | T4, T11, T8 | DD V3.4 para V3.5 | Parcial (Paused; Insurance Record, option mappers e Region sem resposta) | F1, F6, F26; NOVO: DD x Master Data local |
| HRBS-12548 | UA | T5, T6, T11 | Report Specs (1-PV, Pension Fund, internos) | Não neste snapshot (originou SR-414/415 segundo a extração anterior) | NOVO: relatórios estatísticos fora do scope_manifest; F24 |
| HRBS-12631 | UA | T1, T5, T7, T8, T11, T12 | CCG Module 8 v1.0 a v1.2, WTC v3.6 | Parcial (CCG corrigido; relatório de férias e D1 TBC abertos) | F18, F21, F42, F43, F6; NOVO: citação de artigo que rege outro assunto |
| HRBS-13389 | UA | T1, T4, T11, T12 | DD V3.4 | Não | F5, F6; NOVO: campo de WTC sem campo no DD |
| HRBS-13392 | UA | T4, T7, T8, T11 | DD V3.7/V3.8 (Historical Payroll Data) | Parcial (DD ampliado; carga e exclusões sem resposta) | F26, F45, F6; NOVO: conjuntos de exclusão por cálculo |
| HRBS-13499 | UA | T4, T6, T11 | DD (campos de cliente) | Não | NOVO: critério país versus cliente; F2 |
| HRBS-14255 | UA | T6, T11 | CCG V1.3 (advance payroll) | Não (Pending on reporter; falta requisito funcional) | F46; NOVO: mecânica de pagamento fracionado |
| HRBS-14324 | UA | T7, T8, T11, T12 | CCG/WTC (fórmulas de média e BIK) | Não | F45, F42; NOVO: catálogo único de fórmulas de média |
| HRBS-14331 | UA | T1, T2, T3, T6, T7, T8, T10, T12 | WTC V3.8 a V3.9, CCG V1.5, catálogo do cliente | Parcial (Resolved com 4+ perguntas abertas e 6 versus 12 meses) | F7, F18, F20, F27, F41, F43, F44, F45; NOVO: matriz 4DF x flags; changelog verificado |
| HRBS-15216 | UA | T4, T10, T11 | DD (obrigatoriedade, SSC Rate, traduções) | Não | F1, F5, F25; NOVO: obrigatoriedade DD x Spec |

## Padrões recorrentes no grupo

- **Respostas de ticket não consolidadas nos artefatos.** Os mesmos fatos (período-base de 12, 6 ou 2 meses; escopo do gross-up) foram redefinidos em HRBS-12631, 13392, 14324 e 14331 sem um ponto único de verdade. O pior caso é sick leave: 12 meses (nossas respostas de 08-05 e 08-19, e a regra da cliente de 09-17) versus 6 meses (nossa resposta de ~09-09). Cobre F45; falta um catálogo único de fórmulas de média.
- **Changelog e versão que não batem com o arquivo.** v3.5 com nome V3.4, v3.7 com "fórmula" inexistente em 65816/65801/65804, changelog do 65894 inexistente, DD "v3.7" anexado como "V3.8". Quatro ocorrências em dois meses (F45, F27).
- **CCG com regra geral aplicada sem testar populações especiais ou mudança de lei.** PDFO "3 dias bancários", ESV mínimo proporcional no mês de admissão, deficiência com complemento, 4DF trimestral para pessoa jurídica, Social Insurance Fund extinto (F43, F21, F18, F42). Todos descobertos pela Nataliia, não pela pipeline (F41).
- **Tributação de WTs por analogia.** Seguro de vida com USC=Não (analogia ao médico), presente de aniversário como Sim/Sim, civil contractor como Sim/Sim/Sim, stock options com 101+ESV=Não, per diem sem teto, 128 em benefícios (F7, F20). O WTC global não representa bases diferentes por imposto, então o gross-up PIT/Military ficou sem desenho acordado (regra de motor versus PE 58134).
- **DD incompleto ou desalinhado com a operação local.** Campos locais ausentes (HRBS-12368), Insurance Record ausente e não respondido, SSC Rate sem campo, obrigatoriedades herdadas do relatório, falta de tradução (HRBS-12368, 13389, 13499, 15216). Cobertura parcial por F1 e F26; falta reconciliar o DD com o Master Data do país.
- **Pedidos sem resposta ou sem dono.** HRBS-12548, 13389, 13499, 14324 e 15216 sem resposta nossa nos snapshots; perguntas da Nataliia sem retorno em 12181 (Art. 170.9, indexação), 12368 (Region) e 13392 (exclusões, carga); HRBS-14331 marcado Resolved com perguntas abertas (F6).
- **Fronteira de escopo oscilante.** Editamos o catálogo do cliente (W/X/Y, linhas corrigidas) e depois declaramos o catálogo do cliente fora de escopo. Também ficou pendente quem faz a atribuição de códigos (BA), o motor do gross-up (Dev) e o leave module (Vaishnavi). Sugere registrar a fronteira em `fronteiras.md`.
- **Divergências entre fontes da cliente sem arbitragem registrada.** Faixas do auxílio-doença (60/80/100 versus 50/60/70/100), cálculo automático versus entrada manual do Insurance Record, caveat do contrato civil. Falta o registro da fonte legal que decide cada divergência (T12).

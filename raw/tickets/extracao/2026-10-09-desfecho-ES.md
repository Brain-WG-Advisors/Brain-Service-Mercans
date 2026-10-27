# Desfecho dos tickets da Espanha (grupo ES): o que aconteceu depois do snapshot e solução final

- **Grupo:** ES (15 tickets: SR-79, SR-80, SR-432, SR-81, HRBS-12839, HRBS-14528, CT-4321, SR-83, SR-82, SR-85, SR-144, SR-342, SR-365, HRBS-13757, HRBS-10563)
- **Data:** 2026-10-09
- **Nota:** Atualiza `2026-10-08-erros-solucoes-ES-A` e `2026-10-08-erros-solucoes-ES-B` (e, para HRBS-10563, `2026-10-08-erros-solucoes-OUT`) com o desfecho obtido pela API.
- **Fonte:** `raw/tickets/api/2026-10-09/<ID>.md` (estado atual, todos os comentários com data UTC, anexos). Os 15 arquivos existem; nenhum "não baixado".
- **Convenções:** datas da API são UTC e exatas (substituem os "~" da análise anterior). Sem dados pessoais de empregados. Papéis (confirmados nos metadados): Lily Li = BA; Wallisson Gomes = RA (nós); "Drew Õispuu" e "Brenet Õispuu" são o mesmo Developer (nome de exibição diferente entre comentários e campo Developer). "Phase" do YouTrack está desatualizado em vários tickets (ex.: SR-85, SR-342, SR-365 constam "Ready for Production Deployment" mas há comentário de deploy em produção); vale o comentário.
- **Limite:** o que está só em planilhas Google, imagens e anexos não consta. Quando a resolução depende disso, marcado "não consta".

---

## SR-79 — Fichero de Bases (SLD): namespace do root, bônus L03 e limite do 509
- **Estado:** In Review / Phase "Deployed To Production" (10-08) → In Review / Phase "Deployed To Production" (API 10-09, atualizado 2026-10-09 07:44 UTC). Sem data de resolução. O que mudou foi o conteúdo: duas pendências do snapshot foram fechadas em acceptance.
- **O que aconteceu depois do snapshot:**
  - 10-08 15:49 (Wallisson): confirma o root `Bases` com `xmlns="http://www.seg-social.es/creta/esquemas/V130/Bases"`, `xmlns:xsi` e `xsi:schemaLocation="... Bases.xsd"`, com base no Manual de Usuario SLD v2.0.2 (mar/2024), onde todos os elementos pertencem a esse namespace.
  - 10-09 05:39 (Lily a Drew): manda aplicar o root acima. Troca o gatilho do bônus: **4212x é substituído por 68460, 68461, 68462, 68463, 68464**, porque "entrada manual de 4212x não é suportada no salary card" (já acrescentou 68460 para ESP03). Respostas às 2 perguntas de Drew de 10-01: (1) mostrar o valor integral do 6846x em cada mês de acréscimo, "porque o usuário digita o acréscimo mensal"; (2) pergunta a Drew se "sempre 500" é limitação do sistema.
  - 10-09 07:44 (Drew): feito e testado em acceptance (Spain Reports Testing, fev/2026): root com namespace e schemaLocation; gatilho 68460-68464; ESP03 com 68460 = 500,00 gera L03 com período 01/2026, FechaControl 02/2026, LiquidacionMes 01/2026, base 500 = 50000 (centavos), indicador 54; um bloco por mês de acréscimo entre data inicial e final da entrada (meses anteriores ao mês do relatório), cada um com o valor integral. 509: **é limitação do relatório** (lê só a folha corrente, não vê a situação de IT dos meses passados); precisaria de outro dataset ou campo de HR; por ora sempre 500.
  - Sem comentário de Lily ou Wallisson depois disso. Deploy em produção do namespace e do 68460-68464: não consta (só acceptance).
- **Solução final:** namespace do root: resolvido em acceptance (base: Manual SLD v2.0.2). Bônus plurianual: gatilho passa a 68460-68464, um L03 por mês de acréscimo, base 500 com valor integral. Continua aberto: produção, aceite do "sempre 500" (limitação) e itens abaixo.
- **Correções à análise de 10-08:**
  - Namespace do root `Bases`: era "sem resposta"; agora confirmado por Wallisson com fonte (manual v2.0.2) e implementado em acceptance.
  - 4212x: a divergência de WTC (V4.3 sem os elementos, V4.6 com) fica explicada: 4212x não era usável (não há entrada manual na salary card); o elemento certo é 68460-68464. O WTC que traz 68460-68464 e a versão: não consta.
  - A afirmação de Lily de que "Wallisson confirmou só 500/509" continua sem registro em comentário do ticket (só aparece repetida por Lily); a regra "509 só vale na condição de E30" agora tem a limitação técnica declarada por Drew.
  - Fórmula do 563: **não resolvida**. Wallisson (09-04) disse "58151 é o valor reportado, a SUM só abre o gate"; Lily (08-12) escreveu o mesmo; Wallisson (08-13) escreveu "Formula unchanged: SUM(79415, 79416)"; Drew (09-14) implementou 563 = SUM(79415;79416) "como em E145" e pediu confirmação; nenhuma resposta, L13 passou em 09-16 e foi a produção em 09-17. A célula E145 da nossa spec contradiz o texto do comentário de 09-04. Também sem confirmação: 501 e 602 lendo 58554.
  - Escopo: a decisão de 09-25 (só L00, L03, L13) continua só em comentário; nada no ticket mostra que a spec/DD foram atualizadas.
  - Papéis: o campo Developer é "Brenet Õispuu" (= Drew).
- **Conhecimento a absorver:**
  - Elemento raiz do XML do Fichero de Bases leva o namespace `http://www.seg-social.es/creta/esquemas/V130/Bases` e `schemaLocation` `Bases.xsd` (Manual SLD v2.0.2, mar/2024).
  - Acréscimo/bônus plurianual vai em L03, um bloco por mês de acréscimo (período, LiquidacionMes e FechaControl = mês do pagamento), base 500 com o valor integral digitado; 509 não é decidível porque o relatório não vê a IT de meses passados (limitação do relatório).
  - Pay elements 68460-68464 (não 4212x) são os de entrada de acréscimo na salary card.
  - Gatilho de relatório precisa citar campo-fonte que exista na folha corrente (falha recorrente: retro year, situação de IT passada).

## SR-80 — "AFI – Affiliation Message" que na verdade é TrabajadoresTramos (inbound)
- **Estado:** Open, Phase "Development Phase – Developer", assignee Lily (09-14) → **Done em 2026-09-28 10:55 UTC**, assignee Illya Virchenko, Developer Illya. Atualizado/resolvido 09-28.
- **O que aconteceu depois do snapshot:**
  - 09-14 17:08 (Wallisson): reconfirma por extenso que SR-80 é inbound e que "A26S0003.AFI matches TrabajadoresTramos" (comentário que já estava no snapshot).
  - **09-15 00:52 (Wallisson): fecha a questão inbound/outbound e reconhece o erro da amostra:** "wrong sample file replaced with the real TrabajadoresTramos.xml". Três artefatos tocados: **SR-80 v2.1** (amostra trocada), **ES-AFI-OUT-001 v1.0** (nova spec outbound, construída a partir do manual oficial da TGSS; é o SR-432) e **Data Dictionary v5.0** (4 campos que faltavam). Diz que SR-80 "is correct as-is".
  - 09-15 10:54 (Lily): confirma que o relatório é inbound e pede a Katrin atribuir ao desenvolvimento.
  - 09-15 15:14 (Katrin Rudi): após falar com Nabil e Gulnaaz, entende que já está desenvolvido por Liaqat como "AFI report response from Ciltra [sic, SILTRA]"; pede confirmação.
  - 09-28 10:55 (Illya): "developed and confirmed with Testing by Nabil". Ticket fechado.
- **Solução final:** SR-80 (TrabajadoresTramos, TGSS→usuário) já estava desenvolvido pelo time de Integration e testado por Mohamed Nabil; spec v2.1 e DD v5.0 corrigidos por nós; o outbound (Mensaje de Afiliación) foi tirado do SR-80 e virou SR-432. Fechado sem desenvolvimento novo.
- **Correções à análise de 10-08:**
  - **O [INCERTO] sobre A26S0003.AFI está resolvido:** a amostra é o arquivo de afiliação (outbound, Mensaje de Afiliación), não TrabajadoresTramos. A conferência "A26S0003.AFI casa com TrabajadoresTramos" (Wallisson, 09-09 e reconfirmada 09-14) estava **errada**; a validação do SR-432 (entidade de pensão em 43/43) é a que vale. A própria spec SR-80 trazia essa amostra errada, trocada em v2.1.
  - Alocação (Integration × report config): era "em discussão"; resolvida: Integration, já entregue.
  - MA/MB/MC/MG: o SR-432 cobre mensagens de afiliação (os comentários de Drew citam ações MA, MB, MC, ASA, MSA, ESA), então a pergunta "onde ficaram" tem resposta provável; classificação formal não consta [INCERTO residual].
  - O título do SR-80 no YouTrack continua "ES: AFI – Affiliation Message (Social Security) - SPEC", que é o nome do outbound: a causa da colisão de nomes não foi removida.
  - Versão do DD: "v5.0" (comentário de 09-15) × "Version Control 4.6" e "29-Set-26" (SR-432, 09-23 e 09-29). Não dá para saber se são numerações diferentes (arquivo × aba de controle); não consta.
  - Dúvida antiga sobre CNAE/TRL/ColectivoEspecial: nada novo; permanece "não consta".
- **Conhecimento a absorver:**
  - Mapa de arquivos TGSS: TrabajadoresTramos = inbound (resposta da TGSS), SolicitudTrabajadoresTramos = outbound (SR-370), Mensaje de Afiliación (.AFI, MA/MB/MC/MG...) = outbound (SR-432). A amostra `A26S0003.AFI` é do Mensaje de Afiliación.
  - Antes de afirmar que uma amostra "casa" com uma spec, conferir o cabeçalho/estrutura do arquivo (ETI de 70 caracteres = mensagem RED; XML de resposta = TrabajadoresTramos), não só o nome/extensão.

## SR-432 — AFI Outbound (Mensaje de Afiliación): premissas do Dev respondidas
- **Estado:** Open / Phase Developer (10-08) → **Open** / Phase "Development Phase – Developer" (API 10-09, atualizado 10-09 11:15 UTC). Assignee Lily; Developer Brenet (Drew). Criado 2026-09-15 01:09 UTC (não 09-14).
- **O que aconteceu depois do snapshot:**
  - 10-08 19:54 (Wallisson) responde às 4 premissas: (1) confirmado: DOM/LDD só em MA (segmentos opcionais), ODL em toda ação exceto MB, FCT em ASA/MSA/ESA e em MB com data de fim de férias; (2) **corrige a premissa de Drew**: DAM 2110 é zeros em toda ação, MA e MC inclusive; só é preenchido com Specific FIC = S (subrogações parciais, contratos temporários curtos sucessivos), que está hardcoded N; (3) FAB 1910 = zeros (fora de escopo; a amostra A3 mostra 000); **os 14 dígitos do DD estão corretos**: `$hr.collective_agreement_code` é o ODL 2410, outro campo, e o mapper T-61 não deve ser acrescentado; (4) o formato 'A' + data + 0 não serve com a data do fim do período: a TGSS exige nome único por submissão e o AFI pode sair várias vezes no período; o nome externo tem de coincidir com a referência ETI; sugere data de geração + sequência diária ('A' + yyMMdd + 0-9).
  - 10-09 05:18 (Lily): atualizou o mapeamento de FAB 1910 para zeros e pede a Drew aplicar.
  - 10-09 06:58 (Drew): DAM 2110 e FAB 1910 em zeros; condições DOM/LDD/ODL/FCT já estavam como confirmado. Nome do arquivo: a data de geração não está disponível no nome (volta vazia em acceptance); usa **'A' + id da folha (6 dígitos) + último dígito do payrun**, ex.: A1121661.AFI, e a referência de controle ETI/ETF recebe o mesmo valor; cada payroll/payrun gera nome novo, só regerar o mesmo payrun repete o nome. Pede confirmação.
  - 10-09 09:46 (Lily): aprova. 10-09 11:15 (Drew): nome já em acceptance.
- **Solução final:** continua aberto como ticket (Open, em desenvolvimento), mas as 4 premissas estão fechadas (regras de população acima e nome único por id de folha/payrun). Falta: criar/preencher os 10 campos de DD na entidade de teste e testar com eventos reais; não consta se foram criados.
- **Correções à análise de 10-08:**
  - A premissa 2 de Drew (DAM só em MA e MC) estava errada; a regra é "zeros sempre". O comentário de 09-23 da spec sobre DAM.2150-2170 (Special System 32) segue válido para outro campo.
  - A premissa 3 do Dev ("14 dígitos é erro de spec") e a dúvida da Lily ("14 dígitos do DD está errado") ficam resolvidas a favor do DD: dois campos distintos (FAB 1910, 3 dígitos, zeros; ODL 2410, collective agreement code).
  - Premissa 4: nossa orientação inicial (recomendar data) foi substituída pela solução do Dev (id de folha + payrun). A unicidade é por submissão, não por período.
  - A amostra `A26S0003.AFI` usada na validação de 09-25 está correta para o outbound (ver SR-80).
  - Os "7 resíduos de coluna U × DD" (linhas 145, 148, 158, 165, 166, 170, 176): sem menção nova; não consta resolução.
- **Conhecimento a absorver:**
  - Nome do arquivo AFI e referência ETI devem ser únicos por submissão (não por período); o motor não gera número sequencial, então se usa id da folha + último dígito do payrun.
  - DAM 2110 = zeros salvo Specific FIC = S; FAB 1910 = zeros; collective agreement code só no ODL 2410 (14 dígitos).
  - O DD pode listar o campo com um comprimento (14) e a posição do layout ter outro (3): são campos diferentes; conferir o código do segmento antes de acusar erro.

## SR-81 — CRA (Conceptos Retributivos Abonados): layout ETI errado na nossa spec
- **Estado:** In Review / Final Review (09-04) → **Done em 2026-09-14 03:05 UTC**, Phase "Ready for Production Deployment", assignee Lily.
- **O que aconteceu depois do snapshot:**
  - 09-04 16:05 (Wallisson): a amostra A3 `tc260704.cra` está correta e casa byte a byte com o layout ETI oficial (Instrucciones Técnicas: Mensaje CRA, seg-social.es/descarga/es/214731). **O arquivo gerado estava errado da posição 7 em diante porque a linha 8 da nossa spec ("Authorized User ID") não tinha 4 subcampos obrigatórios da TGSS**, deslocando todo o resto. Layout corrigido (spec v2.4): pos 1-3 ETI; 4-7 CRA1; 8: 2; 9-12 código do software registrado na TGSS ("WS56 na referência antiga, a confirmar"); 13: 2; 14-21 número de autorização RED (8 dígitos, movido de 7-14); 22-29 reservado; 30-37 data AAAAMMDD (estava em 27-34); 38-41 hora HHMM sem segundos (eram 6 dígitos); 42-49 nome externo do próprio arquivo, 8 caracteres; 50-52 CRA; 53-70 em branco.
  - 09-08 09:34-09:36 (Lily): pede criar no DD `$legal_entity_hr.software_vendor_code_registered_with_tgss` e `$legal_entity_hr.process_syntax_version_number` e atualizar linhas 6 a 20. 09-08 20:50 (Drew): ETI reconstruído conforme v2.4 e testado em acceptance. 09-10 07:09 (Lily): aceite passou.
  - 09-10 07:10 (Lily): cinco pay elements perdem o código CRA. 09-10 18:31 (Drew): 62874, 62875, 62877, 62878 e 62879 estavam mapeados ao CRA 0001 (indicador I) e seus valores negativos de salary sacrifice reduziam o registro CRE 0001. 09-11 12:52 (Drew): removidos do CRA; demais códigos do bloco 6286x-6288x inalterados. Lily (09-11) pedira deploy em produção; resposta de Drew é só "Done" (deploy em produção: **não consta** explicitamente).
- **Solução final:** spec ES-CRA-001 v2.4 (layout ETI corrigido, base: instrução técnica da TGSS e amostra A3), DD com 2 campos novos de LE, 5 pay elements de salary sacrifice fora do CRA, Remuneration Amount vem do resultado da folha (62100 + 79450 somados no 0001). Ticket fechado em 09-14.
- **Correções à análise de 10-08:**
  - "Posição/comprimento do ETI x A3: não verificado": agora verificado, e o erro era **nosso** (spec sem 4 subcampos), não do Dev.
  - External Reference: a análise tratava o campo como "em branco por design / sugerir `$payroll.reference_code`". Wallisson esclarece que as posições 42-49 são o **nome externo do próprio arquivo** (8 caracteres), não um texto livre; a decisão de usar `$payroll.reference_code` fica superada [a regra de preenchimento final desse campo não consta no ticket].
  - Os testes anteriores do Dev ("5 execuções limpas", exemplo `ETICRA28123456 20260610173047`, "Ready for compliance testing") passaram com um ETI estruturalmente errado: teste circular contra a spec.
  - O ponto "se 79450 deve ir ao 0001": sem discussão nova; permanece [INCERTO].
  - Código do software na TGSS ("WS56, a confirmar"): não consta confirmação.
- **Conhecimento a absorver:**
  - Layout ETI de 70 caracteres (mensagem CRA) conforme acima; o ETI é cabeçalho compartilhado por AFI/CRA/Bases.
  - Wage types de salary sacrifice (negativos) não devem alimentar o CRA 0001.
  - Remuneration Amount do CRA vem do resultado da folha, agrupado por código + indicador I/E.

## HRBS-12839 — "o AFI do cliente é o mesmo relatório da spec?"
- **Estado:** Open (10-08 snapshot de 08-08) → **Resolved em 2026-08-08 17:28 UTC** (SLA Met). Já estava resolvido no dia do snapshot; a análise tinha lido antes da resposta.
- **O que aconteceu depois do snapshot:** 08-08 17:28 (Wallisson): "Confirmed – yes, same report (SR-80). Closing this out." Sem outros comentários.
- **Solução final:** resposta nossa: "é o mesmo relatório (SR-80)". Fechado.
- **Correções à análise de 10-08:** a análise dizia "sem resposta registrada" e "figura como menção de entrada em SR-80". Havia resposta, e ela mapeou o `.AFI` do cliente (amostra `A26G0002`, "relatório AFI com a contribuição de pensão") para o SR-80. **Essa resposta ficou desatualizada/errada**: SR-80 é TrabajadoresTramos (inbound); o arquivo `.AFI` enviado via SILTRA é o Mensaje de Afiliación, coberto pelo SR-432 (ES-AFI-OUT-001). É inferência (o conteúdo de `A26G0002` não consta), baseada em que a amostra `A26S0003.AFI` do mesmo cliente é o outbound. Não há correção posterior a Gulnaaz no ticket.
- **Conhecimento a absorver:** ao responder "é o mesmo relatório?", citar nome oficial do arquivo TGSS e a direção (inbound/outbound), não só o ID da spec; o título do SR-80 ainda induz ao erro.

## HRBS-14528 — Notificações do SILTRA (.msj)
- **Estado:** Open, Compliance Support (09-28) → **Open**, Support Group voltou para **Configuration Support**, assignee Shyam Narayan Tripathi (API 10-09, atualizado 10-05 08:27 UTC; sem comentário visível nessa data).
- **O que aconteceu depois do snapshot:** 09-28 18:37 (Wallisson), a pesquisa pedida: os `.msj` são só aviso de que há uma notificação esperando a empresa na Sede Electrónica da Seguridad Social; a notificação não está no arquivo e só se lê abrindo-a na Sede; se ninguém abrir em **10 dias naturais** é considerada rejeitada, mas produz efeitos legais (Orden ISM/903/2020, art. 8.1). Nas duas amostras o assunto é `(NMTT1HAF10)`, que serve de filtro na pasta `Msjrec`. Cada arquivo traz só data/hora, NIF da empresa e link da Sede, sem dados de empregado ou folha. Devolveu o ticket para Configuration.
- **Solução final:** continua aberto: pesquisa de Compliance entregue; falta decisão e configuração por Configuration Support (Shyam; reporter Mohamed Nabil): o que o HRB pode fazer com um aviso sem conteúdo (ex.: detecção por assunto `NMTT1HAF10` e alerta, ou processo manual). Decisão: não consta.
- **Correções à análise de 10-08:** a lacuna "pesquisa não registrada" fechou; a lacuna "escopo nosso × Integration" ficou como configuração/produto, não pesquisa estatutária. O item sobre F8 (canal inbound não classificado) continua válido para o SIR.
- **Conhecimento a absorver:** notificação SILTRA `.msj` (assunto `NMTT1HAF10`) = aviso de notificação na Sede Electrónica; prazo de 10 dias naturais para acesso, depois considerada rejeitada com efeito legal (Orden ISM/903/2020, art. 8.1).

## CT-4321 — Handover Checklist da regulação Espanha
- **Estado:** Status "Ready for Design" → igual (API 10-09, atualizado 2026-06-15). Sem Resolvido.
- **O que aconteceu depois do snapshot:** nada. Último comentário de texto: 04-15 (Wallisson). O comentário de Lily de 04-28 não foi apagado: é um comentário só com imagem (`image.png`).
- **Solução final:** continua aberto sem ação: lista de handover não atualizada (sem Payslip, SEPE, SR-370, AFI outbound) e critérios de aceite marcados "confirmed" sem evidência. Dono: nós (Wallisson) com Lily.
- **Correções à análise de 10-08:**
  - "Comentário seguinte da Lily foi apagado": corrigido (era imagem).
  - Achado novo: os links de planilha do checklist para AFI, CRA, Modelos 111, 190 e 296 **apontam para arquivos diferentes** dos que as descrições de SR-80, SR-81, SR-82, SR-83 e SR-85 usam (só o Fichero de Bases coincide). Provável cópia antiga; o conteúdo dos arquivos não consta. Reforça o padrão de múltiplas versões paralelas.
  - Datas: início 2026-01-12, due 2025-12-31 (due anterior ao início, como na análise).
- **Conhecimento a absorver:** nenhum novo; a regra "handover cita versão vigente de cada artefato e link do arquivo de trabalho" fica reforçada.

## SR-83 — Modelo 190: fechado e em produção, com lacunas conhecidas
- **Estado:** In Review (09-16) → **Done em 2026-09-22 12:27 UTC**, Phase "Deployed To Production" (deploy 09-22 07:13).
- **O que aconteceu depois do snapshot:**
  - 09-17 00:07 e 03:41 (Wallisson): Descendants = contagens (223-228), não valor em euros; a AEAT deriva o mínimo. Removeu como duplicadas as linhas 38-44 (Children Under 3, Children 3-25 studying, Ascendants over 65/75, Disabled Ascendants), com posições que não batiam com o Diseño Lógico 190 (ejercicio 2025).
  - 09-17 13:46 (Lily): manda aplicar Contract Type, Family Situation e Descendants; define a lógica de Descendants com `child_N_birth_year` e `child_N_full_computation_flag` (N = 1 a 4), com exemplo (ex.: 110201). 09-17 16:12 (Drew): feito em acceptance (Contract Type pos 168, 1 dígito, só Clave A; Family Situation pos 157, claves A, B e C; Descendants 223 = menores de 3, 224 = desses, por inteiro, 225-226 = restantes, 227-228 = restantes por inteiro; idade em 31/12).
  - **09-18 13:35 (Lily): "Year of Birth" e os demais falhavam porque, em registros de outras claves, saíam em branco. Regra do portal: para claves fora de A, B (01/03/04/99) e C, mostrar 0000 / 0 / 0, não branco.** 09-18 15:34 (Drew): Birth Year = 0000, Family Situation = 0, Contract Type = 0 nos Type 2 de outras claves (ex.: L01); arquivo com 500 caracteres/linha sem linha final.
  - 09-21 13:52 (Lily) pede deploy; 09-22 07:13 (Drew): em produção. O arquivo de teste de 09-18 é `M190__2025` (ejercicio encerrado).
- **Solução final:** Spec ES-M190-001 corrigida (posições, domínios e escopo por clave com base no Diseño Lógico 190 ejercicio 2025 e Orden HAC/1431/2025), WTC V4.4 (79429/79430 = B/03; 79432 = L/27), implementação em produção 09-22. Não consta mensagem final do portal AEAT aceitando o arquivo; em HRBS-13757 (09-22 00:51) Lily diz "M190 ok now".
- **Correções à análise de 10-08:**
  - **Year of Birth "falha nos registros 2/4, causa desconhecida, 'não é defeito de spec'":** a causa era regra de preenchimento (zeros em claves não aplicáveis), que a nossa spec não trazia; foi achada por Lily. Portanto lacuna **da spec**, não só do Dev.
  - **B/03 e L/27 (contradição não resolvida):** continua. Drew (08-14) dizia que 79429/79430 produzem B/03 e 79432 produz L/27; em 09-10 diz que a aba "Income Type Clave and Subclave" não atribui WT a B/03/L/27 (apesar de Lily ter atualizado a aba em 08-12), e em 09-14 **removeu os dois grupos**. Resultado em produção: quem recebe esses payouts não gera registro B/03 nem L/27. Se isso é correto ou subnotifica 190 (risco/gravidez/lactação, parental isenta): **não consta decisão**.
  - **Accrual Year (linha 107):** sem nenhuma menção após 08-14; Drew dizia "bloqueado, `wage_type.accrual_period_year` não existe". O ticket foi fechado sem resposta: segue aberto de fato (campo fica 0000).
  - Linhas 55/56 sem códigos de WT Mercans: sem menção nova.
  - A "troca 57176/58176": a fórmula de Annual Withholdings de Lily (08-07) ainda usa 58176/58177 (`2552/58176*(58176-79414-79415-79416)`), códigos que em 09-04 (SR-342) foram declarados "antigos" e trocados por 58552/58572. Se SR-83 e SR-82 foram atualizados: não consta.
  - Não residentes no 190 (HRBS-13757): Lily (08-31) escreveu que não residentes **não aparecem** no arquivo que ela gerou. A análise dizia "não consta correção"; na prática não foi reproduzido.
  - O erro "Ejercicio = 2026" foi artefato de teste, com ejercicio em curso; o reteste foi feito com `M190__2025`.
- **Conhecimento a absorver:**
  - Modelo 190, Type 2: Birth Year/Family Situation/Contract Type só valem para claves A, B (01/03/04/99) e C; nas demais claves, zeros (0000/0/0), nunca branco.
  - Family Situation tem 3 códigos (não 6; o código 1 exige filho dependente); Contract Type tem 1 dígito, códigos 1-4, só Clave A; Descendants 223-228 composto de 4 partes, idade em 31/12; "por inteiro" × "por metade" pelo flag de guarda.
  - Posições de campos que a AEAT exige com zero não podem sair em branco; zona 395-500 em branco.
  - Registro por clave/subclave só se gera se existir WT mapeado; sem WT, remover o grupo (mas confirmar se não falta mapeamento).

## SR-82 — Modelo 111: fechado e em produção
- **Estado:** In Review / Final Review (09-03) → **Done, resolvido em 2026-09-04 13:11 UTC**; deploy em produção 09-08 21:09 (Phase "Deployed To Production").
- **O que aconteceu depois do snapshot:**
  - 09-03 20:01 (Wallisson): campos B-S conferidos no `dr111e16v18.xls`: [05]/[11]/[17] = "Valor percepciones en especie"; [23] Forestry = "Importe percepciones" (a redação da AEAT); [26] = "Contraprestaciones satisfechas"; Colegio Concertado; N(15,2). Campo novo no DD v3.10, linha 143 ("Reference number of the previous declaration (Form 111)"), `$legal_entity_hr.previous_m111_justificante_number`. O 538 não aceita outras chaves além de complementar: só existe declaração complementaria no modelo real (não há "substitutiva").
  - 09-04 05:35-13:10: Lily ajusta posições conforme a amostra A3 (linhas 15 a 65) e novos campos; Drew (11:11) avisa que o campo `previous_m111_justificante_number` ainda não existia no sistema; Lily (13:08) o cria; **aceite passou** (09-04 13:10) para mensal (`..._02.111`) e trimestral (`..._1T.111`).
  - 09-08 10:56 (Lily) / 21:09 (Drew): deploy em produção.
- **Solução final:** spec v4 (campo "Company Legal Name" desdobrado em dois campos AEAT, 60 + 20 caracteres, posições refeitas contra `dr111e16v18.xls` e A3), duas custom reports (mensal 1 período; trimestral 3 períodos, gerar do último mês do trimestre), DD v3.10; produção em 09-08. Aceite do portal AEAT: não consta.
- **Correções à análise de 10-08:**
  - "Campos B-S em branco, campo do DD ausente, remoção de opções do DD": todos resolvidos (resposta de 09-03, campo criado em 09-04).
  - **O erro do portal continua:** HRBS-13757 (09-10, depois do deploy de 09-08) mostra o 111 mensal e trimestral ainda rejeitado para a entidade de teste do cliente, com IBAN já cadastrado; Wallisson (09-11) disse que a spec está correta e pede olhar do Dev. Sem resolução em nenhum dos dois tickets.
  - Valor da chave do campo 538 inconsistente: em 09-02 "X" (Declaración Complementaria), em 09-03 fala de chave diferente de "C" [INCERTO qual vale; conferir `dr111e16v18.xls`].
  - Troca 57176/58176 (linhas 24 e 27): Lily pediu 57176 → 58176 em 07-20 e Drew "atualizou todas as linhas" (07-22); não houve mais menção, e 58176 virou "código antigo" em 09-04 (SR-342). Se o M111 foi atualizado para 58552/58572: não consta.
- **Conhecimento a absorver:**
  - Modelo 111: Denominación o Apellidos (60) + Nombre (20) são dois campos; fundir os dois desloca todas as posições seguintes.
  - Trimestral é lookback de 3 períodos a partir da folha de geração; gerar do último mês do trimestre. Mensal = só o período da folha.
  - Só existe declaração complementar no 111, sem substitutiva.

## SR-85 — Modelo 296: fechado e em produção, com pendências
- **Estado:** In Review (09-04) → **Done em 2026-09-15 06:31 UTC**; deploy em produção 09-15 11:58 (Phase mostra "Ready for Production Deployment").
- **O que aconteceu depois do snapshot:**
  - 09-04 18:05 (Wallisson): as 9 mudanças de Lily para zeros estão corretas e completas (DR296_2024); T2-038 Birth Date sem fallback de zeros, acrescentado na spec v2.4 (`$person.birth_date` se F/J = F; senão zeros); **Record ID (77-84) é alfanumérico na AEAT, alinhado à esquerda com brancos, não zero-padded: a A3 está certa**.
  - 09-08 20:50-21:17: Drew implementa Record ID ("1" + espaços), zeros em 134, 135, 148 e 171-226, Birth Date DDMMAAAA para pessoa física e 00000000 para jurídica (J). 09-10 06:50: aceite passou.
  - 09-10 18:18 (Drew): o 296 não lê chave/subchave do WTC; D (caixa) vem da base 58552, E (espécie) da base 58572, retenção de 2582, população por 58218 e 58205; 62874/62875/62877/62878/62879 não são referenciados no M296/M190/M111/M216. 09-11 12:45 (Lily): discorda (aparecerão sob chave 20/01?) e reporta novos erros do portal. 09-14 10:01 (Drew): para a chave 20/01 vêm dos campos HR `modelo296_clave/subclave`; a opção correta é tirar esses elementos da acumulação de 58552/58572 do lado da folha (mantém 111/190/296 consistentes) ou subtraí-los no relatório. **Bug do Dev**: Contact Person Phone/Name (AEAT 10703/10803) mapeados errado, corrigido. Tax Residence Country (24102): o relatório lê o campo HR "Country of tax residence"; vazio na entidade de teste, pediu preencher e recalcular o masterdata.
  - 09-14 12:42 (Lily): reporta registro fantasma (ex.: "Record 4"), Tax Residence Country aplicado a só 1 dos 3 registros do mesmo NIF; pergunta de Gulnaaz: ao escolher 2025, arquivo e nome saem com 2026. 09-15 06:31: "Acceptance testing passed" (sem comentário de correção de Drew sobre esses três pontos). 09-15 11:58: deploy.
- **Solução final:** M296 com zeros nos campos numéricos, Record ID alfanumérico à esquerda, birth date, contact person e residence country corrigidos; população não residente por 58218/58205; D/E por natureza. Em produção. Aceite do portal: não consta.
- **Correções à análise de 10-08:**
  - "Resposta de Wallisson sobre campos a zerar e Record ID não consta": agora consta (09-04 18:05): lista completa e Record ID alfanumérico.
  - Taxa de retenção 2400 × 1900: Drew corrigiu (4 de 5 pontos, 08-04); causa (spec/WTC × implementação) continua não dita.
  - "Troca 57176/58176" (linha 41): Lily pediu 57176 → 58176 (07-21). Drew, no mesmo comentário, escreveu "58176→57176" **ao descrever a edição**; foi só a redação dele: ele mesmo diz que o relatório soma 2582 direto e depois lê 58552/58572. Direção correta confirmada: **57176 (obsoleto) → 58176 (07/2026) → 58552 (caixa) e 58177 → 58572 (espécie) (09/2026)**.
  - Aberto de fato: registro fantasma, Tax Residence Country em 1 de 3 registros, ano 2025 vs 2026 no nome/conteúdo, decisão sobre exclusão de 62874-62879 da acumulação 58552/58572 (opção a ou b). O aceite de 09-15 não os cita.
- **Conhecimento a absorver:**
  - Modelo 296: campos numéricos que a AEAT exige sem branco levam zeros; Record ID 77-84 é alfanumérico à esquerda; D e E são registros Type 2 separados.
  - Códigos de valor de cada relatório: base 58552 (caixa) / 58572 (espécie), retenção 2582; o relatório não usa a chave 296 do WTC (usa campos HR).
  - Elementos de salary sacrifice (62874...) devem ser tratados na acumulação da folha (58552/58572), senão aparecem em todos os relatórios.

## SR-144 — SEPE Llamamiento: fechado
- **Estado:** Open / "Deployed To Production" (09-09) → **Done em 2026-09-10 02:46 UTC**, Phase "Deployed To Production".
- **O que aconteceu depois do snapshot:** 09-09 21:03 (Wallisson), 8 h depois da pergunta da Lily: o bloco `DATOS_USOLIBRE_EMPRESA` é **opcional**, nenhuma mudança de motor; o valor de referência da A3 (`E3|T079214|C389|F20250808`) é uma referência construída pela empresa (os segmentos T e F repetem o ID do trabalhador e a data do chamamento já presentes no arquivo); não é estrutura definida pelo SEPE, não há o que mapear. Explicação da spec atualizada (linhas 33-34, verde).
- **Solução final:** campo opcional, omitido, mantido assim; spec esclarecida. Deploy em produção já tinha ocorrido em 09-08.
- **Correções à análise de 10-08:** "bloco em aberto, possível causa de rejeição" estava incerto e agora é resposta fechada: opcional, sem mapeamento, sem fonte oficial (decisão nossa; fonte oficial do SEPE: não consta). O ponto "relatório não documenta o comportamento orientado a evento": Drew explicou (07-22) mas a atualização da spec de 09-09 só cobre `DATOS_USOLIBRE_EMPRESA`; documentação do comportamento por evento na spec: não consta.
- **Conhecimento a absorver:** Llamamiento só gera arquivo se houver `sepe_callback_start_date` no período (pasta vazia é esperado); `DATOS_USOLIBRE_EMPRESA` é referência da empresa, opcional, não mapear.

## SR-342 — Employee Tax Certificate: fechado
- **Estado:** In Review (09-11) → **Done em 2026-09-14 09:49 UTC**; deploy em produção 09-15 11:58 (Phase mostra "Ready for Production Deployment").
- **O que aconteceu depois do snapshot:** 09-11 14:21 (Wallisson): spec v2.1; **o texto de fechamento da caixa 15 estava sem a redação legal obrigatória e trazia uma cláusula condicional incorreta**; removeu "a petición del perceptor": a emissão é obrigatória (Art. 108.3 RIRPF) independentemente de pedido; texto correto na coluna M. "Ambos os arquivos (amostra A3 e PDF gerado) já casam com o resto da spec." 09-14 09:49 (Lily): sem mudança no mapeamento. 09-15: deploy.
- **Solução final:** diferença de formato resumida a **um defeito de texto** (caixa 15); spec v2.1; códigos 58552/58572 já aplicados (09-04). Em produção.
- **Correções à análise de 10-08:**
  - "Formato diferente A3 × AEAT × HRB, contradição não resolvida": resolvida; o leiaute do HRB casa com a A3 salvo o texto da caixa 15.
  - O "campo `wage_type.accrual_period_year` (mesma lacuna do SR-83)" **não aparece em nenhum comentário do SR-342**; só Drew o cita no SR-83. A análise de SR-342 não deve listá-lo como aberto neste ticket.
  - A resposta de Wallisson em HRBS-13757 (09-11 13:26, "formato confirmado correto, verificado contra 5 certificados da AEAT") foi seguida 55 minutos depois de uma correção da própria spec: a afirmação foi prematura.
- **Conhecimento a absorver:** o certificado de retenciones é de emissão obrigatória (Art. 108.3 RIRPF), sem cláusula "a petición del perceptor" no texto de fechamento. Comparar texto legal de rodapé/caixas finais com o modelo oficial, não só campos de dados.

## SR-365 — Finiquito: fechado; ramo de não residente não existe
- **Estado:** In Review (08-07) → **Done, resolvido em 2026-08-12 13:13 UTC**; deploy em produção 09-04 12:19 (Phase estagnada em "Ready for Production Deployment").
- **O que aconteceu depois do snapshot:** 08-10 21:48 (Wallisson) responde à pergunta residente × não residente: **só residentes**. O documento de finiquito (liquidação trabalhista) serve a qualquer desligado, mas a retenção da spec é só para residente. Não residente é tributado pelo IRNR (RDL 5/2004) com ramo diferente: taxa fixa 24% (19% para UE/EEE/Islândia/Noruega com certificado de residência), sem escala progressiva, sem mínimo pessoal e familiar, sem regularización/zero-floor do Art. 87; a isenção legal mínima da indenização continua (Art. 14 TRLIRNR remete ao Art. 7.e LIRPF); relatórios 216 (periódico) e 296 (anual) em vez de 111/190. Esse ramo "não existe na spec atual". 09-01 12:42 (Lily) pede deploy; 09-04 12:19 (Drew): em produção.
- **Solução final:** escopo = residentes; não residente: lacuna documentada, sem ramo construído.
- **Correções à análise de 10-08:** "pergunta final sem resposta" → respondida. A regra do zero-floor no desligamento (08-04) segue como explicação; a spec/CCG ainda não registra a nota sobre desligamento [não consta]. As taxas 24%/19% e artigos vêm do comentário (sem link oficial no ticket).
- **Conhecimento a absorver:**
  - Finiquito: retenção só para residentes; não residente exige ramo IRNR (taxa fixa 24%/19%, sem regularización, via 216/296), ainda a construir.
  - Desligamento é gatilho de regularización (Art. 87.2.3º RIRPF): o zero-floor compara com o acumulado real do ano; o piso de 2% do Art. 86.2 é só para contratos de duração inferior a um ano.

## HRBS-13757 — Feedback de testes dos relatórios espanhóis
- **Estado:** Paused / Pending on reporter (09-18) → **Pending on reporter**, assignee Lily, Compliance Support (API 10-09, atualizado 2026-09-22 23:23 UTC). Sem Resolvido.
- **O que aconteceu depois do snapshot:**
  - 09-19 01:56 (Wallisson): em M190, os quatro campos (Year of Birth 153-156, Family Situation 157, Contract 168, Dependents 223-228) estão corretos na versão atual (v3.6) e batem com o Diseño Lógico 190 (2025); pede regenerar e revalidar.
  - 09-22 00:51 (Lily): "M190 ok now."
  - 09-22 23:23 (Wallisson), payslip: contra a Orden ESS/2098/2014 (modelo oficial de recibo), **nenhum dos dois campos é exigência legal**. Antiguidade: a lei só exige que seja derivável (STS 29/10/1993), e o recibo já mostra data de admissão, anos completos e a linha do complemento de antiguidade. Código de contrato: não faz parte do cabeçalho obrigatório (Empresa/Domicílio/CIF/CCC + Trabajador/NIF/NAF/Grupo profesional/Grupo de Cotización). Nenhuma alteração; oferece o código de contrato como campo voluntário (art. 1.1 ¶2) se o cliente quiser.
- **Solução final:** por item: CERTIFICA CodProfesion com right-pad a 7 (v1.1, 09-04), Fichero de Bases L01/L02/L03 corrigidos (v2.5) e ver SR-79; payslip, taxa de IRPF corrigida (deploy 09-04) e campos "obrigatórios por lei" rejeitados com base legal; M190 ok (ver SR-83); Annual Tax Certificate: ver SR-342 (defeito só da caixa 15); Llamamiento: ver SR-144 (evento sem dado + bloco opcional). **M111 e M296:** sem resolução registrada (ver SR-82 e SR-85). Aguarda Gulnaaz/cliente aceitar a resposta do payslip.
- **Correções à análise de 10-08:**
  - Não residentes no 190: não é problema reproduzido (Lily, 08-31, não vê no arquivo dela); a análise dizia "sem correção".
  - Payslip sem contract code/seniority date: a análise dizia "aberto, nosso, campos legais não levantados". A resposta de 09-22 mostra que **não são obrigatórios**: o suposto erro nosso não procede; a pesquisa original estava certa.
  - "Responsável não determinado" no M111: continua não determinado (tem posições ajustadas e deploy; erro de portal persiste em 09-10). M296: o erro de ejercicio 2026 não explicava tudo (SR-85 achou bug de contact person e residência).
  - Rejeição por `Ejercicio = 2026` (M190/M296): erro de teste (ejercicio em curso), confirmado por Lily 08-31.
- **Conhecimento a absorver:**
  - Recibo de salário (Orden ESS/2098/2014): cabeçalho obrigatório = empresa, domicílio, CIF, CCC + trabalhador, NIF, NAF, grupo profissional, grupo de cotização. Código de contrato e antiguidade não são obrigatórios (antiguidade só derivável). 
  - Testes de portal AEAT devem usar ejercicio encerrado.

## HRBS-10563 — Wage types, matriz de tributação e licenças (Espanha)
- **Estado:** Open, SLA Breached (09-08) → **Open**, SLA status **Met** (API 10-09, atualizado 2026-09-10 18:31 UTC), assignee Lily.
- **O que aconteceu depois do snapshot:**
  - 09-08 23:43 (Wallisson), sobre a licença médica contínua (abril a maio): **é problema de desenvolvimento, não de pesquisa**; a lógica especificada (convenção de 30 dias para grupo mensal, base do mês anterior travada durante todo o episódio de IT, segmentação por dia em meses mistos) está correta. Defeitos de execução: (1) "Actual Worked Days" (63956) subtrai os dias de licença duas vezes (ex.: abril 30−2×16 = −2; maio 31−2×31 = −31); (2) "Sick Leave Base" (64552/64553) divide por dias do calendário e não por 30 (maio 31/30 × 5101,20 = 5271,24); (3) "Total BCCC Base" (58150) puxa a base/salário do período corrente em vez da base travada antes da licença. Não aparece no recibo em BASE C.C./A.T. porque ambos batem o teto de 5101,20, mas reportaria dias errados à TGSS/SILTRA e a base errada para quem está abaixo do teto.
  - 09-09 11:56 (Lily): "a base de licença 58151 está correta agora **após reinício do motor de produção**". Os pontos (1) e (2) de Wallisson: não consta se foram corrigidos; Lily cita 58151, Wallisson 58150 (códigos diferentes no texto).
  - 09-10 18:31 (Gulnaaz): novo problema, outra entidade: 58140 "Prorated Extras" não prorateia pela jornada (87,5% deveria reduzir o valor) nem zera quando o empregado está de licença o mês todo. Sem resposta registrada.
- **Solução final:** continua aberto: o pacote original (matriz 6296/6298, 62983 CRA 0054/E + L05, leaves 79022/79024/79028, payouts, lógica 79411/79412, bases por contingência) está no WTC V3.9 (mudanças de Wallisson em laranja) mas o ticket não foi fechado; licença contínua teria sido corrigida por reinício do motor (base 58151) mas há pontos de execução listados sem confirmação; 58140 sem tratamento.
- **Correções à análise de 10-08:**
  - "Ticket de sick leave contínua sem resposta nossa": respondido em 09-08 23:43.
  - **Colisão de numeração 79416 [INCERTO]:** esclarecida pelos outros tickets: 79416 = pagamento de licença médica 16-20 dias (SR-83, SR-79); os payouts de risco na gravidez, risco na lactação e licença parental, propostos nos slots 79416/79417/79418 em 06-15, aparecem no WTC V4.4 como **79430 (gravidez), 79429 (lactação) e 79432 (parental)**; 79417-79424 = aborto, menstruação incapacitante e interrupção da gravidez.
  - **Contradição nova:** em 06-18 (HRBS-10563) corrigimos os payouts 79417-79424 para pago **delegado** (clave A) — a razão dada foi que o empregador adianta o subsídio; em 08-10 (SR-79), Wallisson diz que o WTC traz "INSS pago directo" para cada um deles e usa 79418-79421, 79423 e 79424 como gatilho do 509 (pago directo). Os dois lados não podem estar certos para os mesmos payouts. Qual vale (e qual versão do WTC): não consta; verificar (relevante para Bases 500/509 e para 190/111).
  - A fórmula do dia 1 do aborto: Wallisson (06-18) mandou rotular 79428 "EMP 60%" como 100% salário íntegro do dia da baja (Art. 173.1 LGSS) e modelar como "Abortion First Day" + 2 payouts; no texto final de 06-18 21:58 usa-se 79417 como "Abortion day-1". Se o 79428 foi renomeado: não consta.
  - Ponto 3 (override de severance nos regulation steps) e ponto 6 (Extra Pay Month N, 15ª paga): sem mudança; permanecem de Lily/regulation.
- **Conhecimento a absorver:**
  - Base de cotização em licença: continuam as bases BCCC e BCCP (prior-month); nascimento/cuidado em M-2; base diária = prior ÷ 30 para grupo mensal, ÷ dias do mês para grupo diário; teto 2026 5.101,20/mês = 170,04/dia (Orden PJC/297/2026 arts. 6.1, 6.3, 6.4, 6.5; BOE-A-2026-7296). A Seção 5 do documento "BCCC/BCCP Base Logic" está errada.
  - Dia 1 de acidente (79411) e do aborto/interrupção = salário íntegro do empregador (Art. 173.1 LGSS); menstruação incapacitante é paga pela SS desde o dia 1.
  - 62983 = CRA 0054 E (TGSS) e AEAT/190 clave L, subclave L05 (isenta, Art. 7.e LIRPF), fora de 111/216: sistemas diferentes que coexistem.

---

## 1. Tabela de desfecho

| ID | Estado antes | Estado agora | Resolvido de verdade? | Solução em 1 linha |
|---|---|---|---|---|
| SR-79 | In Review, Deployed To Production | In Review, Deployed To Production (atualizado 10-09) | Parcial | Namespace do root e gatilho 68460-68464 prontos em acceptance (10-09); 563 e produção abertos |
| SR-80 | Open, Developer | Done 2026-09-28 | Sim | TrabajadoresTramos inbound já desenvolvido por Integration e testado; amostra errada trocada, spec v2.1 e DD v5.0 |
| SR-432 | Open, Developer | Open (10-09) | Parcial | Premissas do Dev fechadas e nome de arquivo único por folha; faltam campos de DD na entidade de teste e teste real |
| SR-81 | In Review, Final Review | Done 2026-09-14 | Parcial | Layout ETI corrigido (spec v2.4, 4 subcampos que faltavam), 5 elementos de salary sacrifice fora; deploy não consta |
| HRBS-12839 | Open | Resolved 2026-08-08 | Não (resposta ficou errada) | Respondido "mesmo relatório (SR-80)", mas o .AFI do cliente é o outbound (SR-432) |
| HRBS-14528 | Open, Compliance | Open, Configuration Support (Shyam) | Parcial | Pesquisa entregue (.msj só avisa; 10 dias, Orden ISM/903/2020); falta configuração |
| CT-4321 | Ready for Design | Ready for Design (sem mudança desde 06-15) | Não | Sem ação; checklist desatualizado e links divergentes |
| SR-83 | In Review | Done 2026-09-22, em produção | Parcial | Posições/domínios corrigidos, zeros em claves não aplicáveis; B/03-L/27 removidos e Accrual Year sem fonte |
| SR-82 | In Review, Final Review | Done 2026-09-04, em produção 09-08 | Parcial | Spec v4 (nome legal em 2 campos), mensal/trimestral; erro de portal persiste em HRBS-13757 |
| SR-85 | In Review | Done 2026-09-15, em produção | Parcial | Zeros, Record ID alfanumérico, contact e residência corrigidos; registro fantasma e ano 2025/2026 abertos |
| SR-144 | Open, Deployed | Done 2026-09-10 | Sim | DATOS_USOLIBRE_EMPRESA opcional, referência da empresa, sem mapeamento |
| SR-342 | In Review | Done 2026-09-14, em produção 09-15 | Sim | Só o texto da caixa 15 estava errado (Art. 108.3 RIRPF); códigos 58552/58572 já trocados |
| SR-365 | In Review | Done 2026-08-12, em produção 09-04 | Sim (com lacuna de escopo) | Finiquito só para residentes; ramo IRNR de não residente não construído |
| HRBS-13757 | Paused / Pending on reporter | Pending on reporter (09-22) | Parcial | CNO, L01-L03, M190 e payslip (campos não obrigatórios) resolvidos; M111/M296 sem fechamento |
| HRBS-10563 | Open, SLA Breached | Open, SLA Met (atualizado 09-10) | Não | Defeitos de execução da licença contínua identificados (Dev) e base 58151 ok após reinício do motor; 58140 novo |

## 2. Erros nossos do catálogo (seção 5) que este grupo resolve ou confirma

Item por item dos que tocam o grupo ES (os demais itens da seção 5, UA, CI, NA, não são deste grupo):

- **#6 — ES, SR-80 × SR-432, mesma amostra `A26S0003.AFI` validou inbound e outbound: CONFIRMADO e RESOLVIDO no ticket.** Wallisson (SR-80, 2026-09-15 00:52) reconhece que a amostra em SR-80 era errada e a troca pelo TrabajadoresTramos real (SR-80 v2.1, ES-AFI-OUT-001 v1.0, DD v5.0). A amostra é do Mensaje de Afiliación (outbound); a validação do SR-432 (43/43) vale; a de SR-80 (09-09/09-14) não. Falta só gravar em `correcoes.md` e renomear o título do SR-80. Efeito colateral: a resposta de HRBS-12839 (mesmo relatório = SR-80) ficou desatualizada.
- **#7 — ES, CT-A-485, pisos 1.424,50 / 1.929 / 1.599,60 / 1.391,70: NÃO TOCADO por este grupo** (CT-A-485 não está nos 15 IDs). Apenas o teto 5.101,20/mês e o diário de 170,04 (Orden PJC/297/2026) reaparecem coerentes em HRBS-10563; os pisos não são tratados.
- **#8 — ES, SR-79, root `Bases` sem namespace / 4212x / 563 com duas fórmulas: parcialmente resolvido.**
  - Root sem namespace: **resolvido em acceptance** (Wallisson confirmou 10-08; Drew implementou 10-09); produção: não consta.
  - 4212x: **superado**: Lily trocou para 68460-68464 (10-09) por não haver entrada de 4212x na salary card; Drew implementou em acceptance. As 2 perguntas finais do Dev foram respondidas (valor integral por mês; 509 é limitação, sempre 500).
  - 563 com duas fórmulas: **continua aberto e confirmado**: Wallisson/Lily dizem 58151 com gate; Drew implementou SUM(79415;79416) (E145 da nossa spec) e pediu confirmação sem resposta; já em produção.

Erros nossos novos que este grupo revelou (não estavam na seção 5; sugerir ao catálogo):
- SR-81: spec sem 4 subcampos do ETI (layout deslocado desde a posição 7); nosso, corrigido em v2.4.
- SR-83: regra "zeros nas claves não aplicáveis" ausente (Year of Birth/Family Situation/Contract Type); B/03 e L/27 removidos sem decisão sobre subnotificação; Accrual Year sem fonte.
- HRBS-12839: resposta "mesmo relatório (SR-80)" errada.
- HRBS-10563 × SR-79: payouts 79417-79424 como pago delegado (clave A) em um e pago directo (509) no outro.
- SR-342: texto da caixa 15 do certificado (cláusula condicional indevida) e afirmação "formato correto" 55 minutos antes de corrigi-la.
- SR-82/SR-83: se as fórmulas com 58176/58177 foram atualizadas para 58552/58572: não consta.

## 3. Ainda abertos de verdade (próximo passo e dono)

1. **SR-79:** (a) fórmula do 563: decidir entre "58151 com gate SUM(79415;79416)" e SUM; alinhar célula E145 e Drew. Dono: Wallisson (decisão), Drew (código). (b) Deploy em produção do namespace e do 68460-68464. Dono: Lily/Drew. (c) Lily aceitar "sempre 500" (509 impossível sem outro dataset). Dono: Lily/Wallisson. (d) Gaps H02-H06 e 537, `part_time_hours_per_week` ausente do DD, 604 "fantasma", 501/602 lendo 58554, escopo L00/L03/L13 registrado na spec/DD. Dono: Wallisson.
2. **SR-432:** criar e preencher os 10 campos de DD na entidade de teste, testar eventos reais (MA, MB, MC, ASA, MSA, ESA); confirmar os 7 resíduos coluna U × DD. Dono: Lily (campos/teste), Drew (execução), Wallisson (spec).
3. **HRBS-12839 e SR-80:** corrigir a resposta a Gulnaaz (o `.AFI` do cliente é o outbound, SR-432) e renomear o título do SR-80 para o nome do arquivo TrabajadoresTramos (inbound). Dono: Wallisson.
4. **HRBS-14528:** decidir o tratamento do aviso `.msj` (detecção por assunto `NMTT1HAF10`, alerta de 10 dias ou processo manual) e configurar. Dono: Configuration Support (Shyam) com Mohamed Nabil.
5. **SR-83 (M190):** decidir o destino de B/03 e L/27 (recriar grupos com 79429/79430/79432 ou confirmar que não se reportam) e fechar o Accrual Year (linha 107); confirmar atualização das fórmulas 58176/58177 para 58552/58572. Dono: Wallisson (decisão e spec), Drew (config).
6. **SR-82 (M111) / HRBS-13757:** o upload de M111 mensal/trimestral continua rejeitado para a entidade de teste do cliente; obter o texto exato do erro do portal e achar a causa. Dono: Lily (assignee) com Drew; Gulnaaz fornece o erro.
7. **SR-85 (M296):** registro fantasma, Tax Residence Country em 1 de 3 registros, arquivo de 2025 saindo como 2026, e decisão de tirar 62874-62879 da acumulação 58552/58572; confirmar aceite do portal. Dono: Drew (código), Lily (teste); Wallisson decide a regra de acumulação.
8. **SR-81:** confirmar deploy em produção do layout ETI v2.4 e da remoção dos 5 elementos; confirmar código do software na TGSS ("WS56, a confirmar"). Dono: Lily/Drew; Wallisson (código).
9. **SR-365:** decidir se o ramo de finiquito de não residente (IRNR, 24%/19%, 216/296) vira nova spec ou fica fora de escopo; registrar na spec/CCG a nota do zero-floor no desligamento. Dono: Wallisson e Lily.
10. **HRBS-13757:** cliente/Gulnaaz aceitar a resposta do payslip (contract code e antiguidade não são obrigatórios) ou pedir o campo como voluntário; M111/M296 acima. Dono: Gulnaaz, Lily.
11. **HRBS-10563:** confirmar correção dos defeitos de execução (63956, 64552/64553, 58150 × 58151), tratar 58140 (Prorated Extras: jornada parcial e licença do mês inteiro), resolver a contradição delegado × directo dos payouts 79417-79424 e fechar o pacote WTC V3.9/DD V3.7. Dono: Lily (regulation e dev), Wallisson (pesquisa/WTC), Gulnaaz (casos).
12. **CT-4321:** atualizar a lista de handover (Payslip, SEPE, SR-370, AFI outbound) com versão de cada artefato e links do arquivo de trabalho; evidenciar os critérios de aceite. Dono: Wallisson com Lily.

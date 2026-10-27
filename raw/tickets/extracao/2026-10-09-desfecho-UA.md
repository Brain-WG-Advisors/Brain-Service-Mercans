# Ucrânia (UA): desfecho dos tickets, versão completa pela API

- **Grupo:** UA (18 tickets: 11 HRBS + 7 SR)
- **Data:** 2026-10-09
- **Nota:** Atualiza `2026-10-08-erros-solucoes-UA-A` e `2026-10-08-erros-solucoes-UA-B` com o desfecho obtido pela API.
- **Fontes:** `raw/tickets/api/2026-10-09/<ID>.md` (estado atual, todos os comentários com data, anexos), comparados com as análises de 10-08 e com a seção 5 de `revisoes/2026-10-08-catalogo-erros-tickets.md`.
- **Convenções:** [INCERTO] marca inferência. "Não consta" = não está no texto do ticket. Planilhas, imagens e anexos não vêm no texto. Sem dados pessoais de empregados.
- **Equipe:** Wallisson = Compliance/Research Analyst (nós). Lily Li = BA. Michael Mukosi John = Dev dos relatórios. Vaishnavi Mane = Configuração/leave module. Mohit Jain = Head of Compliance Product. Nataliia Hahan = reporter, especialista local de payroll.
- **Resultado geral:** dos 18, 8 HRBS estão Resolved (12368, 13389, 13392, 13499, 14255 e 14324 passaram a Resolved depois do snapshot; 12181 e 14331 já estavam) e SR-340 ficou Done. Resolvido não significa pronto: 14324, 13392, 13389 e 14331 fecharam com desenvolvimento ou decisão pendente (ver cada ticket).

---

## HRBS-12181: WTC, BIK "só PIT" e gross-up 1.219512
- **Estado:** Resolved (snapshot 36) → Resolved (API). Resolvido em 2026-08-18 10:59 UTC por Lily Li.
- **O que aconteceu depois do snapshot:** nada. O último comentário é de Nataliia em 2026-08-18 ("if we done with the WTC, you can close that ticket"); Lily resolveu no mesmo dia. O snapshot 36 (09-01) já mostrava esse estado final.
- **Solução final:**
  - Série "PIT only, no Military Tax" **não criada** (sem base legal; Military segue a base do PIT; zero combinação assim no WTC de 1281 linhas). Aceito pela Nataliia em 08-04.
  - Gross-up: ×1.219512 só na base do PIT (Art. 164.5 PKU); Military e USC sobre o valor bruto (p. 16-1, pidrozd. 10, rozd. XX PKU). Vale só para renda em forma não monetária (pp. 164.2.17); dinheiro ligado à remuneração é 101, não BIK (pp. 14.1.47/14.1.48).
  - **20 PEs de gross-up (35 códigos Mercans)** definidos em 2026-08-12 (WTC v3.8, verde): moradia, utilidades, carro, combustível, telefone, refeição, vale-refeição, educação, presente in natura, academia, curso pago pelo empregador, parte tributável de serviços médicos, 65805 seguro médico, 65810 seguro de vida, 65812 seguro familiar, 65816 benefício adicional 1. Representação (65806/65808) fora, por ser dinheiro.
  - **A diferenciação PIT/Military não é fórmula de WTC**: é regra de motor para Category=Benefit (conclusão de Wallisson em 08-11, sinalizada ao "Drew"). Lily assumiu o desenvolvimento em 08-13. Estado do desenvolvimento: não consta no ticket.
  - WTC finalizado e publicado por Lily em 08-13 (links com mesmo ID de planilha do master, v3_8). Mobilização = 79417.
- **Correções à análise de 10-08:**
  - **65816 "now has the formula" (08-06) era falso e foi retirado por nós mesmos em 08-11**: colunas Formula de 65816, 65801 e 65804 em branco. A análise de 10-08 já registrava isso; o que muda é que o desfecho está claro: não existe fórmula no WTC, e o gross-up fica no motor. Item 2 do catálogo está resolvido do lado do WTC.
  - **Código 157:** a afirmação de 08-04 ("103/109/157 não são códigos de payroll de empregado") era literalmente verdadeira (157 é pagamento a contratado civil FOP), mas o código acabou configurado no WT 62942 (ver HRBS-14331). O erro foi tratar "não é de empregado" como "não precisa de WT".
  - **Art. 170.9 (representação):** nunca foi respondido pela Altium. Em 09-11 (HRBS-14331) nós mesmos decidimos PIT=Sim em 65806/65807 (mecanismo de adiantamento a prestar contas, sem coeficiente). Continua sem confirmação do uso real pelo cliente.
  - **Indexação (pergunta de 08-07 da Nataliia):** nunca respondida neste ticket. A resposta parcial está no HRBS-13392 (basta o base month, campo "Effective Date of Current Salary") e no HRBS-14255 (indexação só no mês cheio). A entrada mensal do índice CPI continua sem mecanismo definido.
  - A conclusão do 12181 de que "são 6 benefícios" estava descartada; o escopo final (20 PEs) é o de 08-12.
- **Conhecimento a absorver:**
  - Coeficiente 1.219512 vale só para renda não monetária e só na base do PIT.
  - Flags do WTC (PIT/Military/USC) registram incidência, não base de cálculo; a base distinta por imposto é regra de motor.
  - Limite de 20 PEs de gross-up imposto pelo produto (Mohit).
  - Códigos novos de PE entram no WTC sem código; quem atribui é a BA (regra de Lily, repetida em 09-17 e 09-21).

## HRBS-12368: Data Dictionary e Master Data (UA)
- **Estado:** Paused (snapshot 22, 08-17) → Resolved (API), 2026-08-18 11:03 UTC.
- **O que aconteceu depois do snapshot:**
  - 2026-08-17 15:34 (Wallisson): option mapper de Region removido, **DD V3.6**. Isso resolve o pedido que a análise de 10-08 dava como pendente.
  - 2026-08-18 04:27 (Nataliia): "we have all changes in DD file", pede para fechar.
- **Solução final:** DD V3.5 (08-13: 14 campos novos) + V3.6 (08-17: sem option mapper de Region). Salário em USD ficou como lógica de WTC; a confirmação pedida por Wallisson não consta, mas a Nataliia aceitou o conjunto.
- **Correções à análise de 10-08:**
  - Insurance Record: não foi omissão definitiva. Foi tratado no HRBS-13389 (DD V3.7), no dia seguinte.
  - Os option mappers pedidos (nomes curtos de tipo de contrato, Disability Group III, Part-Time Indicator) nunca foram respondidos item a item, mas a Nataliia fechou o ticket sem cobrá-los. Tratar como aceitos por silêncio, sem registro.
  - A taxa ESV (22%/8.41%) ganhou campo "SSC Rate" em 09-25 e **o campo foi retirado em 09-28** (ver HRBS-15216).
- **Conhecimento a absorver:** nenhum novo além do que está em HRBS-15216 (taxa de ESV é parâmetro de regulamento, não campo).

## HRBS-12548: relatórios estatísticos UA (1-PV, Pension Fund, internos)
- **Estado:** Paused / SLA Exempt, assignee Wallisson (snapshot 08, 08-07) → SLA Exempt, assignee Lily Li, sem resolução (API; última atualização 2026-08-10).
- **O que aconteceu depois do snapshot:** 2026-08-10 20:31 (Wallisson): 1-PV mensal e trimestral "confirmed, neither had an existing spec"; specs construídas do zero contra Наказ Держстату №117 e as declarações reais da Altium. Abertos **SR-414** (mensal) e **SR-415** (trimestral).
- **Solução final:** parcial. 1-PV coberto pelas specs SR-414/SR-415 (ainda abertas). **Continua aberto:** relatório do Pension Fund de licença médica (Tab. 2), relatórios internos de cruzamento e relatório interno de salário médio (licença, férias, viagens). Nenhuma resposta nos comentários. Dono: Lily (assignee) decide o roteamento; nós (Wallisson) decidimos se vira spec de relatório. [INCERTO: dono real].
- **Correções à análise de 10-08:** confirmado o erro de escopo (T6): as duas 1-PV não tinham spec. A análise de 10-08 já indicava a origem de SR-414/415 apenas pela extração antiga; agora há confirmação direta e data (08-10).
- **Conhecimento a absorver:** relatórios estatísticos do Derzhstat (1-PV) fazem parte do escopo de reports da UA; devem entrar na Report Matrix.

## HRBS-12631: reserva de férias, salário médio, revisão do CCG
- **Estado:** Pending on reporter, assignee Lily (snapshot 93, 09-28) → Pending on reporter, assignee Lily (API). Última atualização 2026-08-18.
- **O que aconteceu depois do snapshot:** nada. O ticket está parado desde 08-18; o 04/25/46/93 de 10-08 já continham todos os comentários.
- **Solução final:** parcial.
  - CCG V1.2 (08-11) corrigiu: PDFO/ML no dia da transferência bancária (TCU Art. 168.1, confirmado pela DPS); sem base mínima de ESV no mês de admissão/desligamento (Instrução 449 s.III); sem base mínima para quem está em 8,41% (DPS ІПК 04.02.2026 №676); proração por dias úteis, sem Art. 115 (cartas 27.05.2019 №4340 e 15.04.2019 №553); 4DF mensal para pessoa jurídica desde 2026-01-01 (Lei 4536-IX).
  - WTC v3.6 (08-05): 79414 (donor leave, 2 meses) e 79415 (viagem, 2 meses; vale o maior entre a média de 2 meses e a diária do mês, Art. 121 §4).
  - Caveat "(if main place of work)" do contrato civil **mantido** por nós; a Nataliia não replicou.
  - **Continua aberto:** o relatório e saldo de férias (leave module, Vaishnavi) nunca foram respondidos; pergunta de 08-18 sem resposta há 52 dias. Código de acréscimo do D1 para 79414/79415 em TBC sem registro de fechamento.
- **Correções à análise de 10-08:**
  - Sick leave "12 meses" (Postanova 1266) dito aqui em 08-05 está **alinhado com o desfecho final** (ver HRBS-14331). O erro era o "6 meses" de 09-09, não este.
  - Seção da semana 53: nosso rótulo "theoretical" foi oferecido e a Nataliia não respondeu.
- **Conhecimento a absorver:** regras de ESV em mês parcial, 8.41% e contrato civil (já em CCG V1.2); saldo de férias é do leave module, não do payroll.

## HRBS-13389: Insurance Record no DD
- **Estado:** Open, sem resposta nossa (snapshot 23, 08-18) → Resolved (API), 2026-08-23 04:06 UTC.
- **O que aconteceu depois do snapshot:**
  - 2026-08-18 21:49 (Wallisson): campo "Insurance Record (at Hire Date)" no **DD V3.7**: Integer (dias), condicionalmente obrigatório na admissão, capturado uma vez do livro de trabalho, acumula depois. Vínculo com o WTC: "not automatic, separate, not yet built".
  - Wallisson corrigiu as faixas do ticket: Art. 17 da Lei №1105-XIV = **50/60/70/100% em 3/5/8 anos**, não 60/80/100.
  - 2026-08-19 (Nataliia): o valor na admissão é o histórico total de todos os empregadores anteriores, nunca zero. 08-20 e 08-23 (Wallisson): confirmado; a descrição do DD já dizia "covering prior employment", sem mudança de arquivo.
  - 2026-08-23: Nataliia pede o fechamento.
- **Solução final:** DD V3.7, campo Integer em dias. **Pendente:** a fórmula do WTC para o percentual do sick pay não foi construída ("separate, not yet built"); sem dono nomeado.
- **Correções à análise de 10-08:**
  - A divergência de faixas ([INCERTO] em 10-08) está resolvida: valem **50/60/70/100%** (Lei 1105-XIV Art. 17), as da resposta ao 14331. As faixas do ticket (60/80/100) estavam erradas.
  - "Cumulativo informado na admissão" × "calculado automaticamente": resolvido como entrada na admissão + acúmulo automático depois.
  - Dúvida de tipo (anos/meses/dias): o DD usa **Integer em dias**. O HRBS-13499 (GSK) diz que a estrutura Anos/Meses/Dias "é correta" porque espelha o Registro do PFU: as duas respostas não foram reconciliadas [INCERTO].
- **Conhecimento a absorver:** Art. 17 (50/60/70/100% em 3/5/8 anos) e Art. 19 (teto pelo salário mínimo se o stazh nos 12 meses anteriores for menor que 6 meses), ambos da Lei 1105-XIV. O campo é dado de entrada legítimo, não valor calculado (F26 não se aplica).

## HRBS-13392: 12 meses de histórico de payroll
- **Estado:** Open, assignee Archit Naik / L2 (snapshot 24, 08-20) → Resolved (API), 2026-09-08 13:32 UTC, assignee Wallisson.
- **O que aconteceu depois do snapshot:**
  - 2026-08-20 15:21 (Wallisson): **DD V3.9** (resposta às duas perguntas da Nataliia).
  - 2026-09-08 12:38 (Wallisson): pede à Nataliia para fechar; resolvido uma hora depois.
- **Solução final:**
  - O elemento 3 (dias úteis dos 2 meses) **foi retirado da lista de migração**: o denominador é o calendário de trabalho da empresa, não dado por empregado.
  - Exclusões da base de 12 meses: **um único conjunto compartilhado** (não dois), ligado aos códigos do WTC na origem e não ao template de carga. Cinco WTs com ESV=Sim a excluir: 62180 (severance), 79401 (compensação de férias), 79415 (viagem), 79408 (sick leave parte do empregador), 79468 (sick leave parte PFU).
  - Indexação: só precisa do base month.
- **Correções à análise de 10-08:**
  - Versão: o texto de 08-18 dizia "DD v3.7" com anexo V3.8. O ajuste do mesmo dia foi V3.8; a versão final deste ticket é **V3.9** (08-20). Registrado como mais uma ocorrência de rótulo incorreto.
  - Rótulo "dias úteis trabalhados" estava errado (era o denominador do horário da empresa): corrigido.
  - Dos cinco WTs excluídos, **62180 deixou de ser ESV=Sim** (HRBS-14331, 09-23: ESV corrigido para Não). O conjunto efetivo de exclusão por ESV fica com os outros quatro; 62180 continua excluído por norma.
- **Continua aberto (nunca respondido no ticket):**
  - Mecanismo e template da carga (backend único ou arquivo): sem resposta de L2/Configuração.
  - Conferência linha a linha dos Porady 1266 e 100 para achar exclusões diferentes por tipo de cálculo ("still on us as a manual step"). Dono: Wallisson.
  - Denominador do sick pay: aqui "dias corridos trabalhados/justificados"; na regra da Nataliia no 14331 (09-17) são "dias em que foi segurado, feriados sempre excluídos". Não reconciliado.
- **Conhecimento a absorver:** o histórico de rendimentos tem 3 componentes ligados a cálculos diferentes; exclusões são propriedade do WT, não do template de carga.

## HRBS-13499: DD da GSK (campos extras)
- **Estado:** Open, sem resposta (snapshot 31, 08-24) → Resolved (API), 2026-08-27 11:48 UTC.
- **O que aconteceu depois do snapshot:**
  - 2026-08-24 14:14 (Wallisson): respondeu.
  - 2026-08-27: Nataliia pede o fechamento.
  - A resposta de Wallisson já existia no mesmo dia do snapshot (08-24), mas não aparecia nele.
- **Solução final:**
  - Insurance Record: **não é específico do cliente**, vale para toda a UA (Lei 1105-XIV Art. 17: 50/60/70/100%; Art. 19: teto se stazh < 6 meses nos 12 meses anteriores). Fonte oficial: Registro do PFU (Довідка ОК-5/ОК-7 ou e-cabinet).
  - Grade 2, City of Work e Manager: sem base na lei trabalhista ou tributária; campos organizacionais da GSK (configuração do cliente, não DD do país).
- **Correções à análise de 10-08:** "nenhum erro, sem critério" agora tem critério de fato: **campo com base legal entra no DD do país; campo só organizacional é do cliente**. A faixa de 13389 está confirmada aqui (50/60/70/100). Persiste a tensão Integer em dias × Anos/Meses/Dias (ver HRBS-13389).
- **Conhecimento a absorver:** critério país × cliente para campos do DD (base legal = país). Registrar em `servicos/design.md` ou na MANDATE.

## HRBS-14255: Advance Payroll no nível país
- **Estado:** Pending on reporter, assignee Lily (snapshot 62, 09-11) → Resolved (API), 2026-09-25 16:02 UTC, assignee Vaishnavi Mane, Support Group Configuration Support.
- **O que aconteceu depois do snapshot:**
  - 2026-09-11 19:13 (Wallisson): respondeu à Nataliia. O adiantamento é salário pelos dias trabalhados (Art. 24(3) Lei 108/95-VR + Art. 115(3) CLT ucraniana), sem relatório. Qualquer tipo de ganho pode cair em qualquer metade, **exceto indexação (Postanova 1078) e Tax Social Benefit, que só valem no mês cheio**. Adiantamento fixo (ex. 53%) é válido, mas tem de ficar acima do piso legal em todo mês; prática de mercado 55 a 60%+; reduzido proporcionalmente se o período não foi cheio. Sick leave segue a metade em que cai; **férias**: pagas antes do início (Art. 21 Lei 504/96-VR, alterada em 2022), independentes de adiantamento/saldo.
  - 2026-09-15 (Mohit): **solução de produto**: criar um *Custom Period Setup* mapeando 2 períodos de meio mês para 1 período mensal de reporte; "the regulations will work automatically".
- **Solução final:** configuração (Custom Period Setup), não desenvolvimento. Resolvido em 09-25 pela Configuração.
- **Correções à análise de 10-08:** a análise tratava como falha nossa o CCG V1.3 não ter o comportamento funcional (dois runs, coluna do adiantamento líquido, saldos). O desfecho mostra que o produto resolveu por configuração de período; **não era necessário requisito adicional do Compliance**. Fica só a lição de que nossa resposta inicial (apontar o CCG) foi lida como insuficiente. As exceções acima (indexação, TSB, férias) estão só no comentário; não consta que tenham entrado no CCG.
- **Conhecimento a absorver:** o adiantamento ucraniano é pagamento de meio mês em dois runs; no HRBlizz usa Custom Period Setup. Exceções de mês cheio: indexação e TSB.

## HRBS-14324: fórmulas de salário médio e benefício adicional
- **Estado:** Open, assignee Wallisson (snapshot 51, 09-08) → Resolved (API), 2026-09-22 00:48 UTC, assignee Lily.
- **O que aconteceu depois do snapshot:**
  - 2026-09-09 01:57 (Wallisson): respondeu os 4 blocos e atualizou o CCG.
  - 2026-09-22 00:48 (Lily): "Average pay formula will be created after requirements are finalized." Resolveu em seguida.
- **Solução final:** respostas no CCG (versão não nomeada no comentário).
  - Férias: Порядок 100, 12 meses. Sick/maternidade: Postanova 1266, regras separadas, não misturar com férias.
  - Donor leave e viagem: 2 meses (Порядок 100 §2, confirmado pela Derzhpratsi).
  - Indexação: Postanova 1078, mecanismo próprio de CPI, não é média.
  - Paralisação sem culpa: 2/3 da tarifa/oklad (CLT Art. 113), não é média; agora fórmula documentada no Module 4.
  - Presentes: isenção de 25% do salário mínimo confirmada (p. 165.1.39).
  - **Gross-up: a Variante 1 é o padrão** (coeficiente natural 1/0.82 só na base do PDFO; Military sobre o valor real; sem base legal para coeficiente combinado), incorporada no campo Grossing-Up das "6 categorias de BIK" do Module 7.
  - Feriado/dia não útil (Art. 107): **não é 2× fixo.** Horista e tarefa: 2×. Mensalista (oklad): 1× adicional dentro da norma mensal de horas e 2× só além dela. Valor-hora = oklad ÷ norma de horas daquele mês.
- **Continua aberto:** as fórmulas de média no HRBlizz **ainda não foram construídas** (Lily: depende de requisitos finalizados). Dono: BA/Config, com requisitos da Nataliia.
- **Correções à análise de 10-08:**
  - A variante de gross-up, que 10-08 dava como "decisão da empresa não tomada", foi **decidida por nós: Variante 1** (a da autoridade). Sem confirmação explícita da Nataliia.
  - Art. 113 e Art. 107, dados como sem tratamento, estão tratados e documentados.
  - A tensão "1266: meses efetivamente trabalhados" × 6/12 meses: o 6 foi um erro de 09-09 (ver HRBS-14331).
  - O CCG fala em "6 categorias de BIK" e o 12181 fechou em "20 PEs": não reconciliado [INCERTO].
- **Conhecimento a absorver:** o Art. 107 vale diferente para mensalista e horista. Donor leave = 2 meses. Gross-up: Variante 1.

## HRBS-14331: catálogo do cliente × master
- **Estado:** Resolved, assignee Wallisson (snapshot 81, 09-23) → Resolved (API), 2026-09-28 05:21 UTC, assignee Lily. SLA status passou a "Met" [INCERTO se foi re-resolvido; a data de resolução é 09-28].
- **O que aconteceu depois do snapshot (09-23 em diante):**
  - 2026-09-23 17:26 (Wallisson), WTC master: **62180/62181** ESV corrigido para Não (CMU 1170 Perelik, seção I item 4) e 4DF de 101 para **127** (MinFin Order 4, anexo 2; ДПС ЗІР 103.25). **65808**: 4DF de 126 para **125** (ДПС, julho 2026), ESV mantido Sim (Instrução 5 p. 2.3.4). 62940/62941 sem mudança. Stock options: sem consolidação dos dois blocos. "65894 existed, created 09-Sep and 15-Sep, removed"; o valor 802536457 era `65808*1.219512` avaliado.
  - 2026-09-23 17:52 (Wallisson): maternidade (65700-65712, 79406): pergunta quais são financiados pelo PFU. Stock options: pergunta se o custo é recarregado à entidade UA. **Per diem (62570, 65570-65572, 65580-65582): é correção da coluna Formula, para Dev**; teto UAH 864,70/dia (doméstico) e EUR 80/dia (exterior), 2026; Formula vazia nos 13 códigos relacionados; 62965 fica como está (tributável integral).
  - 2026-09-23 18:24 e 09-24 16:56 (Nataliia): **128 só para o benefício de maternidade pago pelo PFU** (126/140 dias; desde 2023-01-01 o PFU paga tudo desde o dia 1). Top-up do empregador: 101 (PIT, ML, ESV Sim). Benefício próprio do empregador: 126. Stock options: três cenários (recarga + remuneração = 101 com ESV Sim e gross-up; recarga + fora da folha = 126 com ESV Não; pai estrangeiro paga direto = fora do payroll da UA). Os "WTs cinza" do catálogo do cliente foram **deletados** pela Nataliia.
  - 2026-09-24 (Lily): per diem não tributável para 6557x/6558x **desenvolvido em regulations**.
  - 2026-09-25 05:30 (Wallisson), WTC master: 65700/65701/65702/65710/65711/65712 ESV de Não para Sim; **79406 reclassificado**, 4DF 128 para 101, PIT/ML/ESV Não para Sim.
  - 2026-09-28: Resolved.
- **Solução final (consolidando toda a thread):**
  - Colunas de média: J/K/L e depois W/X/Y para 114 WTs (102 com par direto no master).
  - Seguro de vida: USC/ESV Sim (Postanova 1170 p.2 rozd. II isenta só médico e previdenciário).
  - Presente de aniversário não tributável: PIT/ML Não/Não (4DF 160, p. 165.1.39).
  - Contratado civil FOP: 4DF 157, WT **62942**, PIT/ML/USC Não/Não/Não (p. 177.8 PKU).
  - 65894 removido; novos PEs entram sem código (BA atribui). 65817 sem coeficiente (monetário). Dedução de férias antecipadas: linha-spec nova, categoria Deduction, Não/Não/Não, código em branco para a Lily atribuir (21142 do master é "Unpaid leave deduction"). Rótulo de 62209: divisor 0.82.
  - CCG V1.5 / WTC V3.9 (draft em 09-21), WTC finalizado por Lily em 09-21. Seção 8.2 do Guia corrigida (exclusões de férias); regras de sick leave acrescentadas; "Social Insurance Fund" substituído por Pension Fund (fusão em 2023-01-01).
  - Código 128: só no benefício PFU. 62180/62181: 127, ESV Não. Maternidade: ESV Sim. Stock options: **aberto, depende do cenário do cliente**.
- **Correções à análise de 10-08:**
  - **Sick leave 6 × 12 meses:** o desfecho é **12 meses** (Postanova 1266). Evidências: as regras da Nataliia de 09-17 ("last 12 calendar months", renda sobre a qual o ESV foi pago), adotadas por nós em 09-21 (item 4, "Sick leave rules added to the Guide"); nossas respostas de 08-05 (12631) e 08-19/20 (13392); e a descrição da própria Nataliia no 13392 (12 meses). **O comentário de 09-09 ("6-month base") nunca foi retirado por escrito.** Pode ter confundido o 12 meses com a regra do Art. 19 da Lei 1105 (teto quando o stazh nos 12 meses é menor que 6 meses) [INCERTO: causa]. **Pendência:** conferir a coluna K do master WTC V3.9 e as colunas X/Y da planilha. Isto é o item 1 do catálogo.
  - **65894:** a análise de 10-08 dizia "afirmava criação de um PE que não existia". Em 09-23 Wallisson disse que o PE **existiu** (criado em 09-09 e 09-15) e foi removido; em 09-21 ele dissera que não existe no master finalizado. As duas coisas conciliam: existiu em versões intermediárias, não no master final. A resposta de 09-10 ("65808 base + 65894 grossed-up") usava o PE, então não era inventada, só efêmera.
  - **Catálogo do cliente × master (item 4):** os links das correções de 09-09, 09-11 e 09-21 e o "WTC finalizado" de Lily apontam para a **mesma planilha** (ID `1rhjGwFM…`), rotulada "Mercans" e, no 09-09, "WTC_Altium…". O catálogo do cliente é outra planilha (ID `1FV2VgiN…`, a da Nataliia). Logo, as correções foram feitas no **master**, e o nome "Altium" no rótulo é só nome [INCERTO por ser inferência a partir dos IDs]. Wallisson ainda declarou o catálogo do cliente fora de escopo em 09-10.
  - **65808:** a nomenclatura que 10-08 deixou [INCERTO] ("Representation expenses (financial)" × "Life Insurance (BIK)") ficou resolvida do lado do master: em 09-29 (SR-415) tratamos 65808 como "Life Insurance (BIK)".
  - **62209, divisor 0.82:** nenhuma resposta da Nataliia ou da Lily à correção de 0.77 para 0.82; a Lily finalizou o WTC. Continua [INCERTO] se a compensação em dinheiro (18%+5%) devia ser 0.77.
  - **Perguntas de 09-22:** 128, 62180/62181, per diem e maternidade foram respondidas e corrigidas. Código 102 e o item "sem imposto" (imagens) não têm resposta explícita [INCERTO: conteúdo das imagens]. Stock options aguardam o cliente/global team.
  - Ticket Resolved com pendências: isso se repete (F6), mas desta vez a maioria foi tratada em 09-23 a 09-25 antes da resolução.
- **Conhecimento a absorver:**
  - 128 só para o benefício PFU de maternidade; benefícios do empregador = 126, top-ups = 101.
  - Per diem: teto diário (UAH 864,70 = 0,1 do salário mínimo; EUR 80), excesso com gross-up, ESV Não; 4DF 118.
  - Severance e redundancy: ESV Não, 4DF 127.
  - ESV de seguro de vida: Sim. Vacation: exclusões de 1266 não se aplicam.
  - Feriado/fim de semana trabalhado soma 1 dia na proração de bônus (Порядок 100 p.3), mas não na média de férias, que usa dias corridos com feriados excluídos.
  - Códigos novos no WTC sempre sem número.

## HRBS-15216: checagem do DD (obrigatoriedade, SSC Rate, traduções)
- **Estado:** New, Unassigned (snapshot 89, 09-25) → Open, Unassigned (API; última atualização 2026-09-28).
- **O que aconteceu depois do snapshot:**
  - 2026-09-25 20:22 (Wallisson): Contract Start Date, Oblast, Street and Building Number e Postal Code agora Optional. 1C Personnel Number removido. "ЄСВ Rate Effective Date" renomeado para "SSC Rate Effective Date". Novo campo "SSC Rate" (22/8.41). Supporting Document Reference (D5): **Conditional Mandatory**, só quando houver evento D5 (admissão, transferência, desligamento, licença); alimenta a coluna 16 do D5. TSB Eligibility = Tax Social Benefit (art. 169 PKU), só mediante pedido escrito do empregado; agora Optional. ESV Category Code = código da pessoa segurada (КЗО) no D1: 1 = contrato de trabalho, 2 = deficiência, 26 = contratado civil. Rótulos ucranianos que faltavam, adicionados.
  - 2026-09-26 (Nataliia): pede a Sahmad e Vaishnavi para atualizar a entidade de teste REF-04-254.
  - **2026-09-28 11:31 (Wallisson): correção, o campo "SSC Rate" NÃO entra no DD.** A taxa (22%/8.41%) é parâmetro de regulamento, guiada pelo campo Disability Group existente (DD Version Control 4.0). Pediu para não configurar, ou remover se já criado.
- **Solução final:** DD atualizado (versão 4.0) para obrigatoriedade, 1C, rename, traduções. Não há campo SSC Rate. Pendências: ninguém assumiu o ticket (sem assignee, sem Resolved); a Nataliia não respondeu à retirada do SSC Rate que ela mesma pedira; a configuração da entidade de teste não consta como feita.
- **Correções à análise de 10-08:**
  - A obrigatoriedade de D5/TSB, tida como [INCERTO], resolveu: D5 vira condicional por evento; TSB, opcional.
  - O erro "SSC Rate ausente" da análise de 10-08 deixa de existir como erro: foi decisão de design (parâmetro de regulamento). Vale registrar que a resposta de 09-25 errou ao adicionar e a de 09-28 corrigiu; mais um caso de mudança de resposta em 3 dias.
  - **Dois conjuntos de código de categoria:** aqui o código de pessoa segurada (1/2/26) no HR master; no SR-160 o filtro de motor do WTC usa 20/21. São campos distintos (HR × WTC), mas os valores não são os mesmos para o mesmo conceito (contrato civil = 26 aqui, 21 lá) [INCERTO: confirmar na spec do D1].
- **Conhecimento a absorver:** taxa de ESV não é campo do DD (parâmetro de regulamento); campo obrigatório em relatório não é necessariamente obrigatório no master (D5 é condicional ao evento).

## SR-160: Spec D1 (ESV)
- **Estado:** In Review, assignee Michael (snapshots 27/84/96, 09-28) → In Review, assignee Michael, fase Final Review (Business Analyst), atualizado 2026-10-09 10:40 UTC. Due Date original 2026-03-31, vencida.
- **O que aconteceu depois do snapshot:**
  - **2026-09-28 16:14 (Wallisson): "true XML sample" entregue** (substituiu o schema no "XML Sample File"). O pedido de Lily de 09-28 12:14 está atendido.
  - 2026-10-09 10:40 (Lily): repete ao Michael a mesma lista de 09-24 (linhas 4 e 27, campos novos nas linhas 46-47). Sem conteúdo novo [INCERTO se foi reenviado por engano].
- **Solução final:** spec com SUM explícito no rodapé, HBOS/HBUH adicionados (57 tags conferidas), `chief_accountant_name` no DD (ordinal 9.5), WTC V3.2 (62964 com КТН 13), DD V3.3 (Part-Time Indicator, obrigatório M). Idioma dos relatórios: ucraniano (requisito estatutário). **Continua aberto:** implementação e QC do Dev; encerramento do ticket. A coluna КЗО do WTC não foi removida, apenas renomeada (a pergunta de remoção nunca teve resposta).
- **Correções à análise de 10-08:**
  - Datas reais: respostas de Wallisson em 04-30, 05-23, 07-08, 08-23 e 09-25, não "~abril a setembro".
  - O assignee atual é Michael (não Wallisson, como em 10-08).
  - O true XML sample, listado em aberto, está entregue.
  - O ticket permanece In Review; HBOS/HBUH: ver conclusão no fim (item 5 do catálogo).
- **Conhecimento a absorver:** todos os campos de relatório precisam de origem no DD; as tags HZ/HZN/HZU/C_DOC_STAN seguem 011 → HZ=1/C_DOC_STAN=1, 012 → HZN=1/C_DOC_STAN=2, 013 → HZU=1/C_DOC_STAN=3.

## SR-161: Spec 4DF
- **Estado:** In Review, assignee Wallisson (snapshot 98) → In Review, assignee Michael, atualizado 2026-10-09 09:54 UTC (sem comentário novo visível).
- **O que aconteceu depois do snapshot:** 2026-09-28 16:16 (Wallisson): **true XML sample entregue**. Nada além disso. Os defeitos do QC de Lily (09-28 10:00) seguem sem retorno do Dev no ticket: U4 apontando para `_d1`, PEs 58582/58552 sem uso na configuração, renda 101+126 gerando só 101, data com traços (05-01-2026 em vez de 05012026), `R02G03I` vazio, G09=0 não omitido, separador de milhar.
- **Solução final:** spec com HBOS/HBUH (54 tags conferidas) e regra HZ/HZN/HZU/C_DOC_STAN; linha 4 atualizada pela Lily; Michael atualizou o template em 09-25. **Continua aberto:** correções do Dev para a lista do QC (dono: Michael).
- **Correções à análise de 10-08:** o true XML sample deixou de ser pendência nossa. O assignee passou a Michael (Dev).
- **Conhecimento a absorver:** formatos da spec (data DDMMAAAA, sem separador de milhar, zero omitido) vêm da spec; defeito de implementação do Dev se corrige no Dev.

## SR-162: Spec D5 (relações de trabalho)
- **Estado:** In Review, assignee Wallisson (snapshot 97) → In Review, assignee Wallisson, atualizado 2026-10-09 10:11 UTC.
- **O que aconteceu depois do snapshot:**
  - **2026-09-28 16:15 (Wallisson):** true XML sample entregue; **HDDGV e HNDGV agora estão na spec (linhas 55-56)**.
  - 2026-10-09 10:00 (Lily ao Michael): feedback de testes. Observa que as linhas 55-56 estão em branco.
  - 2026-10-09 10:11 (Lily a Wallisson): (a) nas linhas 55-56, o comprimento do segundo campo está em branco e os campos não precisam de mapeamento: correto? (b) nas linhas 37-51, vários campos "Blank for mapping" aparecem com valor no XML de amostra (ex.: `<C_REG>26</C_REG>`) e com comprimento 0: o "Blank" está correto? **Pergunta aberta para nós.**
- **Solução final:** spec v3 com HBOS, HBUH, TIN, C_DOC, C_DOC_SUB, C_DOC_VER, C_DOC_TYPE, C_DOC_CNT, C_REG, C_RAJ, C_STI_ORIG, LINKED_DOCS, SOFTWARE, PERIOD_TYPE + HDDGV/HNDGV (09-28). Gatilho formalizado por Lily em 09-24 (evento no período OU fim por categoria). Continua aberto: duas perguntas de Lily de 10-09 (dono: Wallisson); QC do Dev (U4, C_DOC_SUB 106 → 105, C_DOC_STAN vazio, HFILL com formato errado, `::key` sem default); confirmação das linhas duplicadas PERIOD_MONTH/PERIOD_YEAR/D_FILL.
- **Correções à análise de 10-08:**
  - HDDGV/HNDGV, dados como [INCERTO], foram incorporados na spec.
  - **Achado novo:** as ~15 tags acrescentadas em 08-24 (linhas 37 a 51) foram marcadas "Blank for mapping" com comprimento 0, mas o XML de amostra as preenche com valores. Isto é uma lacuna nossa na spec (T5): as tags foram adicionadas sem conteúdo de mapeamento.
  - O assignee continua Wallisson.
- **Conhecimento a absorver:** tags adicionadas ao XSD precisam de regra de mapeamento e comprimento; marcar "Blank" é uma afirmação que o XML de amostra desmente.

## SR-163: Spec D6 (tempo de serviço especial)
- **Estado:** In Review, assignee Wallisson (snapshot 95) → In Review, assignee Michael, atualizado 2026-10-09 10:41 UTC.
- **O que aconteceu depois do snapshot:**
  - **2026-09-28 15:40 (Wallisson):** true XML sample entregue. **Correção: "HBOS can't be left empty, it's mandatory. Only HBUH is optional."** Isto retifica nossa resposta de 08-24 ("HBOS/HBUH vazios no XML, preenchidos pela assinatura digital").
- **Solução final:** spec v3; gatilho em duas camadas (posto de trabalho qualificado, Порядок §6, e `special_seniority_code` não nulo). Linhas 33-51 novas, a desenvolver (Lily, 09-24). Continua aberto: QC e implementação do Dev. Não consta se a correção do HBOS foi aplicada ao mapeamento.
- **Correções à análise de 10-08:**
  - Nossa resposta de 08-24 estava **errada** sobre HBOS (obrigatório, não vazio). Corrigido por nós em 09-28.
  - A afirmação equivalente para HBOS nas specs D1, 4DF e D5 ("same pairing as HKBOS/HKBUH") não foi revisitada; vale conferir se também precisa da correção.
  - O true XML sample está entregue; assignee passou a Michael.
  - O RNOCPP do contador-chefe mapeado para `director_signatory_rnocpp` (item da lista do Dev): continua sem tratamento [INCERTO].
- **Conhecimento a absorver:** HBOS é obrigatório nas specs J05.

## SR-340: Payslip UA
- **Estado:** In Progress (snapshot 11, 08-10) → Done (API), fase "Ready for Production Deployment", resolvido em 2026-09-28 05:02 UTC, assignee Lily.
- **O que aconteceu depois do snapshot:**
  - 2026-08-11 18:26 (Wallisson): **ESV Payer Number = código EDRPOU** (a UA não emite registro ESV separado para pessoa jurídica comum); **Division** (dados bancários) não corresponde a nenhum dado do sistema (o IBAN já contém o identificador do banco). Lily e Michael: ambos fora da spec; desenvolvimento segue.
  - 2026-08-18: Michael conclui `ua-payslip-en` e `ua-payslip-uk`. 08-20: Lily lista 10 itens (EN) e 9 (UK): coluna Rate sem taxas, coluna Unit sem base, capitalização, remover Banking Details/Bank Name/Tax Month, rótulos, Pay Period/Pay Date, labels locais dos PEs na versão UK. 08-21: Michael corrige (local name com fallback para o nome do PE).
  - 2026-09-24: retest da Lily (remover nomes ucranianos do EN; coluna Unit nas contribuições do empregador, EN e UK). 09-25: resolvido.
  - **2026-09-28 05:02 (Lily): acceptance testing passed.** Michael aguarda o aviso de Lily para fazer deploy.
- **Solução final:** o payslip passou no acceptance. Pendência: deploy em produção.
- **Correções à análise de 10-08:**
  - A "inconsistência template × Payslip Spec 1" ficou resolvida do **lado da spec**: ESV Payer Number e Division não são exigidos; o template foi alinhado à spec.
  - O marcador "[VERIFY WITH RA]" do ESV payer number = EDRPOU foi fechado por nós (08-11), sem fonte legal citada no ticket (T12 permanece). EDRPOU e endereço: o formato não foi definido no texto.
  - Os 19 itens do QC de Lily (08-20) eram defeitos de implementação do Dev, não da spec.
- **Conhecimento a absorver:** na UA, o "ESV payer number" é o EDRPOU; "Division" bancária não existe.

## SR-414: Spec 1-PV mensal
- **Estado:** Open, assignee Wallisson, sem Dev (snapshot 100) → Open, assignee Lily, fase "Product Mapping Phase - Business Analyst" (API, última atualização 2026-09-29 16:36). Due Date 2026-09-30 (original).
- **O que aconteceu depois do snapshot:** **2026-09-29 16:36 (Wallisson) respondeu todas as perguntas da Lily de 09-29:**
  - "External part-time" = categoria 2 do D5 (emprego concorrente) com "Simultaneous Main + Concurrent Employee Flag (D5)" = 0; categoria 1 = local principal de trabalho. Option mapper do DD corrigido.
  - Formato do arquivo adicionado à Report Matrix: XML, template Derzhstat S0301016, assinado com KEP.
  - No-Data indicator: criado o campo do empregador "1-PV No-Data Reason" no DD.
  - Fórmula e exemplo do FTE médio ("calendar-day average"): na coluna W, linha 12 (conteúdo não consta no ticket).
  - Exclusões da população "staff": maternidade (5 ou 7) e cuidado de filho (4 ou 6) confirmados; mobilizado é o WT 79417, não as categorias 7/8; contrato suspenso/evacuado: **nenhum campo mapeado hoje**; 79410 não pode ser usado (cobre toda licença não remunerada); motivo de desvio: texto livre, sem campo.
- **Solução final:** parcial, a revisão de Lily é a próxima. **Continua aberto:** exclusão de "contrato suspenso/evacuado/paradeiro desconhecido" sem campo no DD/WTC (lacuna de escopo); o limiar de 25%/10% de desvio e o comentário do RA "worth a direct check if the 2024 text surfaces" não foram tratados em comentário [INCERTO: se o RA limpou a coluna W].
- **Correções à análise de 10-08:**
  - A fonte de "staff" (Labour Registry Person Category, categorias 1-2) foi mantida; a análise de 10-08 listava 8 itens abertos, 5 deles agora respondidos (part-time externo, formato, No-Data, fórmula FTE, desvios).
  - Divergência a conferir: Lily mapeou maternidade = 5 e mobilizado = 7 ou 8; Wallisson respondeu maternidade "5 ou 7" e mobilizado via WT. O código 7 aparece nos dois lados. Verificar a lista de categorias do D5.
- **Conhecimento a absorver:** categorias do Labour Registry Person Category como definição de "staff"; mobilizados identificados por 79417.

## SR-415: Spec 1-PV trimestral
- **Estado:** Open, assignee Wallisson (snapshot 101) → Open, assignee Michael, fase "Development Phase - Developer" (API, 2026-10-09 12:02 UTC).
- **O que aconteceu depois do snapshot:**
  - 2026-09-29 17:07 (Wallisson): colunas E/F da aba Wage Fund Classification dependem da natureza do pagamento, não do código 4DF. 62180, 62181 e 79406 continuam EXCLUDED (Instrução 5, p. 3.8 e 3.2). 62942 ("Payment to Individual Entrepreneur") e 65808 ("Life Insurance (BIK)") mudaram: 62942 = EXCLUDED (FOP não é salário e está fora da linha 7040); 65808 = SOCIAL_IND / 5080 (p. 2.3.4). Coluna V respondida na W (linhas 8, 12 e 21).
  - 2026-10-09 09:51 (Lily): "Mapping done" (fase passa a Desenvolvimento).
  - **2026-10-09 12:02 (Lily): a aba de amostra não é XML e a spec não mostra elementos XML; pede amostra XML correta e os elementos correspondentes.** Pergunta aberta para nós.
- **Solução final:** formato e dependência do WTC resolvidos em 09-29; desenvolvimento em curso. **Continua aberto:** amostra XML e elementos XML da 1-PV trimestral. Dono: Wallisson.
- **Correções à análise de 10-08:** colunas E/F, que estavam sem resposta, foram respondidas; o formato (Law 2524-IX art. 10(4)) já estava. O achado novo (amostra e elementos XML ausentes) repete o padrão de "spec sem XSD/elementos".
- **Conhecimento a absorver:** a Wage Fund Classification depende da natureza do pagamento (Instrução 5), não do código 4DF; mudanças de 4DF no WTC exigem verificar a aba, sem que a mudança seja automática.

---

## Tabela final

| ID | Estado antes | Estado agora | Resolvido de verdade? | Solução em 1 linha |
|---|---|---|---|---|
| HRBS-12181 | Resolved | Resolved (2026-08-18) | Parcial: WTC sim, gross-up no motor sem confirmação do Dev | Sem série "só PIT"; coeficiente 1.219512 só na base do PIT, 20 PEs, regra de motor; WTC v3.8 |
| HRBS-12368 | Paused | Resolved (2026-08-18) | Sim | DD V3.5 (14 campos) e V3.6 (Region sem option mapper); Nataliia aceitou |
| HRBS-12548 | Paused, SLA Exempt | SLA Exempt, sem resolução | Parcial | 1-PV viraram SR-414/415; Pension Fund Tab. 2, relatórios internos e salário médio sem resposta |
| HRBS-12631 | Pending on reporter | Pending on reporter | Parcial | CCG V1.2 e WTC v3.6 corrigidos; relatório de saldo de férias (leave module) sem resposta |
| HRBS-13389 | Open | Resolved (2026-08-23) | Parcial | DD V3.7: Insurance Record Integer em dias, faixas 50/60/70/100; fórmula do WTC não construída |
| HRBS-13392 | Open (L2) | Resolved (2026-09-08) | Parcial | DD V3.9: histórico em 2 elementos de carga, exclusões ligadas ao WTC; mecanismo de carga sem resposta |
| HRBS-13499 | Open | Resolved (2026-08-27) | Sim | Insurance Record vale para toda a UA; Grade 2, City of Work e Manager são do cliente |
| HRBS-14255 | Pending on reporter | Resolved (2026-09-25) | Sim | Custom Period Setup (2 semimeses em 1 período mensal), pela Configuração |
| HRBS-14324 | Open | Resolved (2026-09-22) | Parcial | Fórmulas no CCG, gross-up Variante 1, Art. 107 corrigido; fórmula de média no HRBlizz ainda por construir |
| HRBS-14331 | Resolved (com perguntas abertas) | Resolved (2026-09-28) | Parcial | Correções no master (ESV, 4DF, 128, maternidade); sick leave 12 meses; stock options e 62209 pendentes |
| HRBS-15216 | New, Unassigned | Open, Unassigned | Não | Respondido em 09-25 e corrigido em 09-28 (sem SSC Rate); falta aceite da Nataliia e configuração da entidade |
| SR-160 | In Review | In Review | Não | Spec e DD corrigidos, true XML sample entregue; falta QC/implementação do Dev |
| SR-161 | In Review | In Review | Não | HBOS/HBUH e XML sample entregues; defeitos de QC do Dev sem retorno |
| SR-162 | In Review | In Review | Não | Spec v3 + HDDGV/HNDGV; duas perguntas novas de Lily (10-09) sobre linhas "Blank" |
| SR-163 | In Review | In Review | Não | Spec v3; HBOS passa a obrigatório; XML sample entregue; QC e desenvolvimento em curso |
| SR-340 | In Progress | Done (2026-09-28) | Sim, falta deploy | Template alinhado à spec (ESV Payer = EDRPOU, sem Division); acceptance passou |
| SR-414 | Open | Open | Parcial | 5 de 8 perguntas respondidas em 09-29; falta campo para contrato suspenso; revisão da Lily |
| SR-415 | Open | Open (Development) | Parcial | Formato e colunas E/F respondidos; Lily pede amostra e elementos XML |

## Erros nossos do catálogo (seção 5) que este grupo resolve ou confirma

1. **HRBS-14331, sick leave 6 × 12 meses: confirmado como erro nosso; desfecho 12 meses, falta correção escrita.** Postanova 1266 com 12 meses; adotado nas regras do Guia em 09-21. O "6" de 09-09 nunca foi retirado em comentário. Ação: conferir a coluna K do WTC V3.9 e as colunas W/X/Y da planilha, e registrar em `correcoes.md`. Possível origem do 6: confusão com o Art. 19 (stazh < 6 meses). Status: **confirmado, aberto só na conferência do artefato**.
2. **HRBS-12181, "65816 now has the formula": confirmado e resolvido.** Retirado por nós em 08-11: coluna Formula em branco; o gross-up é regra de motor. Status: **resolvido (WTC)**; implementação do motor sem confirmação do Dev.
3. **HRBS-12181/14331, código 157: resolvido.** 157 = pagamento a contratado civil FOP, configurado no WT 62942, PIT/ML/USC Não/Não/Não (p. 177.8); em 09-29 62942 aparece como "Payment to Individual Entrepreneur", EXCLUDED do fundo de salário. Decisão para `correcoes.md`: 157 pertence ao WTC (62942), não é "fora do payroll".
4. **HRBS-14331, correções no catálogo do cliente × master: resolvido por inferência.** Os links das correções apontam para a mesma planilha (ID `1rhjGwFM…`) que Lily chama de "Finalized WTC", e não para a planilha do cliente (`1FV2VgiN…`). Master atualizado em 09-09, 09-11, 09-21, 09-23 e 09-25. Falta só abrir as duas planilhas para confirmar. Status: **provavelmente resolvido, conferir**.
5. **SR-160 a 163, HBOS/HBUH e tags de cabeçalho: confirmado e corrigido nas specs (v3).** D1 (57 tags), 4DF (54 tags), D5 (+12 tags + HDDGV/HNDGV em 09-28), D6 (+12 tags). Ressalvas: (a) D6: HBOS é obrigatório, não vazio (correção de 09-28); conferir D1, 4DF e D5; (b) as linhas 37-51 do D5 estão marcadas "Blank" mas o XML as preenche (pergunta de Lily, 10-09); (c) PERIOD_MONTH/PERIOD_YEAR/D_FILL como possíveis duplicatas seguem sem confirmação. Status: **corrigido, com 3 ressalvas abertas**.

Itens novos deste grupo para acrescentar à seção 5 (se aprovado): (i) 62180/62181 estavam com ESV=Sim e 4DF 101 (corrigidos em 09-23); (ii) 65700-65712 com ESV=Não (corrigidos em 09-25) e 79406 com 128 (corrigido); (iii) 65808 com 4DF 126 (corrigido para 125); (iv) fórmula de per diem vazia nos 13 códigos (6557x/6558x desenvolvidos em regulations, 62570 não confirmado); (v) HBOS obrigatório no D6.

## Ainda abertos de verdade

| # | Ticket | O que falta | Próximo passo | Dono |
|---|---|---|---|---|
| 1 | HRBS-14331 | Coluna K (sick leave) do WTC com 6 meses em vez de 12; registro em `correcoes.md` | Abrir o master V3.9 e os W/X/Y, corrigir se necessário | Wallisson |
| 2 | HRBS-14331 | Stock options: cenário A, B ou 126 depende do cliente; sem resposta | Perguntar ao cliente/global team se o custo é recarregado à entidade UA | Wallisson via Lily |
| 3 | HRBS-14331 | Divisor do 62209 (0.82 × 0.77) e itens de código 102/"sem imposto" sem resposta | Pedir à Nataliia confirmação do divisor; ler as imagens do ticket | Wallisson / Nataliia |
| 4 | HRBS-14331 | Per diem: fórmula do 62570 e do teto (62570, 63711, 63712, 75100, 75101) | Confirmar com Lily que o desenvolvimento cobre 62570 | Lily / Dev |
| 5 | HRBS-12181 | Regra de motor do gross-up PIT/Military (e a escolha entre regra de motor e PE agregado 58134 "BIK Gross Up") | Decisão Compliance/BA/Dev; confirmar status do desenvolvimento | Lily, com Dev |
| 6 | HRBS-13389 | Fórmula do sick pay (percentual por stazh) no WTC; tipo do campo Integer em dias × Anos/Meses/Dias | Construir a fórmula; reconciliar a estrutura com o registro do PFU | Wallisson (WTC), Lily (config) |
| 7 | HRBS-13392 | Mecanismo/template de carga do histórico; conferência linha a linha dos Porady; denominador do sick pay (dias corridos × dias segurados) | Perguntar a Configuração/L2; Wallisson faz a conferência manual | Wallisson, L2/Config |
| 8 | HRBS-12631 | Relatório e saldo de férias no HRBlizz; código D1 de 79414/79415 em TBC | Cobrar Vaishnavi; fechar o código D1 | Vaishnavi; Wallisson |
| 9 | HRBS-12548 | Relatório do Pension Fund (Tab. 2), relatórios internos e de salário médio | Decidir se viram specs e responder à Nataliia | Lily (rotear), Wallisson |
| 10 | HRBS-14324 | Fórmulas de média no HRBlizz ainda não criadas; conflito "6 categorias" × 20 PEs no CCG | Nataliia fecha requisitos; Wallisson alinha o CCG com os 20 PEs | Lily / Nataliia; Wallisson |
| 11 | HRBS-15216 | Sem assignee; Nataliia não aceitou a retirada do SSC Rate; configuração da entidade REF-04-254 | Atribuir; confirmar com Nataliia; pedir a Sahmad/Vaishnavi que não configurem SSC Rate | Lily / Wallisson |
| 12 | SR-162 | Respostas às perguntas de Lily (10-09): linhas 55-56 e linhas 37-51 "Blank" com valor no XML | Responder e completar o mapeamento das tags | Wallisson |
| 13 | SR-415 | Amostra XML e elementos XML da 1-PV trimestral | Entregar amostra XML e linhas de elementos na spec | Wallisson |
| 14 | SR-414 | Contrato suspenso/evacuado sem campo; limiares 25%/10% sem fonte; categoria 7 em conflito | Criar campo ou documentar a exclusão; conferir a lista de categorias do D5 | Wallisson, Lily |
| 15 | SR-160/161/162/163 | QC e implementação do Dev (U4, C_DOC_SUB 105, formatos de data e número, `::key` com default, G09=0, 58552/58582); tickets In Review com prazo de 2026-03-31 vencido | Michael corrige; Lily retesta; Wallisson confere HBOS em D1/4DF/D5 | Michael, Lily |
| 16 | SR-340 | Deploy em produção | Lily avisa o Michael | Lily / Michael |

# Desfecho dos tickets: grupo AF + OUT (África e Outros)

- **Grupo:** AF (Namíbia, Congo, Côte d'Ivoire) + OUT (Colômbia, Chile, China, Holanda, Irlanda, Lituânia, Singapura). 25 tickets (a lista da tarefa diz 24; o ID HRBS-10563, Espanha, estava no OUT de 10-08 mas não está neste grupo).
- **Data:** 2026-10-09
- **Nota:** Atualiza `2026-10-08-erros-solucoes-AF` e `2026-10-08-erros-solucoes-OUT` com o desfecho obtido pela API.
- **Fonte:** `raw/tickets/api/2026-10-09/<ID>.md` (baixado em 2026-10-09 09:32 a 09:34). Todos os 25 IDs tinham arquivo. CT-A-620 (KB) não foi baixado e fica sem alteração.
- **Convenções:** datas em UTC, como no arquivo da API. Sem nomes, IDs ou salários de empregados dos clientes (vários tickets os trazem; foram omitidos). Funcionários Mercans aparecem pelo primeiro nome só quando o papel importa. "Não consta" = não está no ticket. [INCERTO] = inferência minha.
- **Aviso de higiene:** no HRBS-14714 o solicitante colou no comentário a senha de um pay register protegido. Não foi reproduzida aqui. Vale pedir a limpeza do comentário no YouTrack.
- **Padrão geral que a API revelou:** muito do "Resolved" é fechamento automático por falta de resposta do solicitante (12072, 12483, 14605, 13841), não confirmação do cliente. Nas cinco tickets da Colômbia o "Resolved" de 2026-09-30 12:00 é um fechamento em lote, feito por Mohit depois que Wallisson documentou a resposta no CCG/WTC v1.1.

---

# NAMÍBIA

## HRBS-12072: mais códigos de pay element (combinações Tax/SSNC/ECF/Pension)
- **Estado:** Open/SLA Exempt, assignee Wallisson (10-08) → **Resolved** (API 10-09), resolvido em 2026-08-10 05:26, assignee agora Pradeep, SLA "Met", motivo de violação "Reporter Non-Responsive".
- **O que aconteceu depois do snapshot:**
  - 2026-08-05 02:16, Wallisson: confirma a Mohit que **nenhum código** da WTC tem Tax=Yes/SSNC=Yes/Pension=No. Os 31 códigos SSNC=Yes (Basic Salary, Salary Addition, Annual Leave Pay etc.) são todos Pension=Yes, "padrão do catálogo, não regra legal". A combinação em si é legalmente válida: a base SSNC é fixada pelo Social Security Act e a pensão é inteiramente de fundo privado (o National Pension Fund nunca foi ativado), então nada liga as duas por lei.
  - 2026-08-05 05:06, Mohit: a configuração de pensão privada no nível do país é genérica; exigências do cliente não se configuram no país. Para o cliente, usar os pay elements 21640 (Private Pension Fund Contribution EE), 21641 (Private Provident Fund EE) e 21642 (Private Retirement Annuity Fund EE).
  - 2026-08-06/07, Pradeep: pergunta se precisa de algo e avisa que fecha por falta de resposta. Fechado 08-10.
- **Solução final:** nenhuma alteração na WTC de compliance. A combinação (b) SSNC=No/ECF=Yes/Pension=No já existe. Para a (a), o cliente configura a exclusão de pensão por pay elements próprios (21640/21641/21642). Versão da WTC: não consta.
- **Correções à análise de 10-08:**
  - Dizia "nenhuma resposta de Wallisson" e combinação (a) "sem veredito". Errado: houve veredito em 08-05.
  - A causa não é divergência de regra legal. É um default do nosso catálogo (Pension=Yes em todos os SSNC=Yes) sem base legal, o que o próprio Wallisson admite.
- **Conhecimento a absorver:**
  - Namíbia: pensão é 100% regida por fundo privado; flags Pension=Yes da nossa WTC são default de catálogo, não obrigação legal. Cliente com regra de fundo própria prevalece (ver 12483).
  - Regra de produto (Mohit): requisito específico de cliente não vira configuração de país; usar pay elements 21640/21641/21642.
  - Confirma o F50 (flag sem base legal): aqui a fonte do flag é "default".

## HRBS-12101: amostras dos relatórios estatutários da Namíbia
- **Estado:** Open, SLA estourado → **Resolved** em 2026-08-12 23:45 (SLA "Breached"), assignee Wallisson.
- **O que aconteceu depois do snapshot:** 2026-08-12 23:45, Wallisson responde item a item:
  - **ETX:** sample disponível. `NA_ETX_Mapping.xlsx` tem exemplo preenchido (`Sample_ETX_Template_Version_2`), igual ao "ETX Template Version 2" publicado pela NamRA (página de downloads do ITAS). Pronto para compartilhar.
  - **SSC Form 10:** não há arquivo para amostrar. Conferido no mySSC Guide v3 da própria SSC (ssc.org.na): o Form 10 é uma ação de revisar e clicar no portal sobre valores calculados pelo sistema; o empregador não digita nem edita nada. A Field-Level Spec MSD/ECF já cobre os campos reais, confirmados no mesmo guia.
  - **PAYE 5 certificate:** nada existe do nosso lado. O ITAS lista só o template ETX; o PAYE 5 não é fornecido pela NamRA, é gerado pelo empregador a partir dos mesmos dados do ETX mensal. Precisa ser escopado como entregável próprio, separado deste ticket.
- **Solução final:** ETX entregue com sample; Form 10 explicado (sem formulário a amostrar); PAYE 5 identificado como entregável **ainda inexistente**, a escopar. Resposta do solicitante: não consta.
- **Correções à análise de 10-08:**
  - "Resolvido: não; nenhuma resposta visível" estava errado.
  - A lacuna não era "pipeline gera spec e não sample": para o ETX o sample existia; o Form 10 não tem formulário; o PAYE 5 não tinha spec nenhuma. A hipótese de padrão "falta formulário oficial de referência" vale só para o ETX, que já tinha.
  - O descompasso de nomes (Form 10/PAYE 5/ETX versus PAYE Return/SSC Return da configuração) se explica: ver 14605.
- **Conhecimento a absorver:**
  - Namíbia: ETX = arquivo mensal do empregador à NamRA (template v2 oficial). PAYE 5 = certificado que o empregador emite, derivado do ETX (não é formulário NamRA). SSC Form 10 = ação no portal mySSC, não há arquivo.
  - Decisão pendente: escopar o PAYE 5 como Report Spec própria.

## HRBS-12111: revisão da report matrix da Namíbia
- **Estado:** Open, SLA -16d → **Resolved** em 2026-08-10 18:03 (SLA "Breached").
- **O que aconteceu depois do snapshot:** 2026-08-10 18:03, Wallisson revisou contra a WTC real v2.5 e devolveu arquivo corrigido (`Baker_Namibia__Report_Matrix_V2_for_review__3_.xlsx`). Achados:
  - relatório estatutário N-ETX (Employee Tax) faltava por completo: construído e incluído no índice;
  - SSC calculada errada (N$550; correto N$99 por GN 8461) e mapeada em códigos inexistentes (2556/2566): corrigido para 2551 (EE) e 2550 (ER);
  - PAYE não implementado: incluído com a tabela progressiva real, código 2552;
  - "Taxable Total" mapeado em 58998 (inexistente): corrigido para 58008;
  - "Employee payables previous" (26999) sem equivalente na WTC: marcado inválido;
  - moeda errada (TND em vez de NAD): corrigida.
- **Solução final:** matriz do cliente corrigida e devolvida; WTC v2.5 como referência.
- **Correções à análise de 10-08:** "Erro identificado: nenhum; conteúdo da matriz não consta" fica superado. A matriz do cliente tinha 6 defeitos, todos do lado do cliente (herdados de outro país/modelo, TND sugere cópia da Tunísia [INCERTO]). O potencial T6 se confirma: faltava o ETX.
- **Conhecimento a absorver:** SSC EE/ER = códigos 2551/2550; PAYE = 2552; Taxable Total = 58008. Valor SSC vigente na época: N$99 (GN 8461). Ver 14605 para o novo teto.

## HRBS-12483: flag de pensão divergente (WTC compliance × cliente)
- **Estado:** Open, Resolution Time -11h → **Resolved** em 2026-09-16 14:33, assignee Mohit (SLA "Breached").
- **O que aconteceu depois do snapshot:**
  - 2026-08-04 22:53, Wallisson: (1) 62961 **não** é "Yes" na nossa WTC; é "No (Typically)" nas três colunas de pensão, então provavelmente não há conflito. (2) Para 62100, 62146, 62147, 62148, 62149: sem edição na WTC. A Namíbia não tem definição nacional única de "pensionable salary"; ela é definida pelas regras de cada fundo do empregador (Pension Funds Act, legislação subsidiária e NAMFISA). A WTC marca Yes por padrão por ser o tratamento mais comum. Para a Baker Hughes existe a informação específica (a WTC dela), que prevalece: configurar No e deixar a WTC de compliance como está. Pergunta antes de fechar: confirmar que os valores da WTC do cliente vêm do administrador/regras reais do fundo, não de default copiado.
  - 2026-09-16 14:34, Mohit fecha: sem resposta há um mês.
- **Solução final:** nenhum erro nosso. Implementar conforme a WTC do cliente; a de compliance fica. Condição não respondida: origem dos valores do cliente.
- **Correções à análise de 10-08:** "não determinado, pode ser erro nosso" fica resolvido: não é erro. E 62961 não fazia parte do conflito (era No). A causa [INCERTO] "pensionável pode ser lido como SSC/ECF" é descartada: é indefinição legal intencional da Namíbia.
- **Conhecimento a absorver:** mesma regra do 12072: Pension=Yes é default de catálogo; vale a regra do fundo do cliente. Registrar na ficha Namíbia: "pensionável = por fundo".

## HRBS-13602: SSC do empregado (WT 2551) não reduz a base do PAYE
- **Estado:** Open, posição provisória "não é pré-imposto" → **Resolved** em 2026-08-24 17:37 (SLA "Met"), assignee Wallisson.
- **O que aconteceu depois do snapshot:**
  - 2026-08-24 17:36, Wallisson: sem correção; o cálculo está certo. Income Tax Act, s.17 limita a dedução pré-imposto a fundos de pensão/provident/retirement annuity e apólices educacionais; SSC/MSD não está nessa lista e não há outra previsão de dedução. Na WTC da própria Baker Hughes, WT 2551 (MSD EE) tem "Pre-tax Relief For PAYE Purposes: NA", enquanto WT 21640 (Private Pension Fund EE) tem "Yes". A fórmula citada pelo cliente ("SS Ee Pension Add") descreve a WT 21640, não a 2551. A diferença de 29,70/mês é o sistema funcionando.
  - 2026-08-24 17:52, solicitante pede call (link enviado por DM).
  - 2026-08-24 21:06, Wallisson reafirma e cita a fonte: NamRA, "Taxation of Individuals Who Earn a Salary", seção "Allowable Deductions" (brochura em PDF anexada ao ticket).
- **Solução final:** nenhuma mudança. CCG, WTC e cálculo estão corretos: WT 2551 é retida após o PAYE e não reduz a base da WT 2552.
- **Correções à análise de 10-08:** o "conflito entre artefatos" não existia. Era leitura errada do cliente: a fórmula do WTC dele se refere à WT 21640. A causa [INCERTO] "WTC/design descreve fórmula que não bate com o CCG" cai. Isto bate com `rascunhos/2026-10-08-pesquisa-NA-SSC-PAYE.md` (a lista fechada da s.17 e a brochura NamRA); a pesquisa pode ser promovida ao hub da Namíbia. Os dois tickets do cliente citados (anualização, constante de faixas desatualizada) continuam fora deste grupo.
- **Conhecimento a absorver:** Namíbia: apenas pensão/provident/RA e apólice de educação reduzem a base do PAYE (ITA s.17; teto conjunto, no rascunho de pesquisa, N$150.000/ano). SSC/MSD nunca reduz. Fonte NamRA brochure. Item 11 do catálogo (seção 5) fecha.

## HRBS-14605: confirmação de configuração dos relatórios estatutários da Namíbia
- **Estado:** Open, Resolution Time -7d → **Resolved** em 2026-10-08 05:19 (SLA "Breached"; motivo "Reporter Non-Responsive"), assignee Pradeep.
- **O que aconteceu depois do snapshot:**
  - 2026-09-28 14:53, Wallisson responde as quatro perguntas do cliente:
    1. **PAYE:** ano fiscal 1 mar a 28/29 fev. Faixas 2026/27 pela Income Tax Amendment Act 4 of 2024 (GG 8442): 0% até N$100.000; 18% de 100.001 a 150.000; N$9.000 + 25% de 150.001 a 350.000; N$59.000 + 28% de 350.001 a 550.000; N$115.000 + 30% de 550.001 a 850.000; N$205.000 + 32% de 850.001 a 1.550.000; N$429.000 + 37% acima.
    2. **SSC:** 0,9% empregado + 0,9% empregador sobre o "basic wage". Mínimo N$500, **máximo N$12.500** (máx. N$112,50 cada lado), legalmente em vigor em 1 mar 2026 (GN 236 de 2026, GG 8975). A SSC anunciou que aplica o novo máximo a partir de **1 set 2026**, sem retroatividade. Máximo sobe para N$14.000 em 1 mar 2027.
    3. **VET Levy:** 1% da folha anual, só empregador, quando a folha anual é de N$1.000.000 ou mais; pago à NTA até o dia 20 de cada mês (GN 67 de 2021, GG 7498).
    4. **IT12E / IT14E não são formulários da NamRA.** O empregador arquiva o ETX mensal e emite o PAYE5 a cada empregado; o ITAS valida a declaração do empregado contra os dados do ETX. 30 de junho é o prazo da declaração individual do empregado, não um arquivamento do empregador.
  - 2026-10-06/07, Pradeep: "ainda precisa de suporte?" e aviso de fechamento. Sem resposta; fechado em 10-08.
- **Solução final:** perguntas respondidas com fonte. Configuração dos relatórios (Monthly PAYE Return, Gross to Net, SSC Contribution Return, payslip) é do time de Configuração (previsão 25/set, depois revisão de Compliance); entrega efetiva: não consta.
- **Correções à análise de 10-08:**
  - IT12E/IT14E **não são lacuna de cobertura**: não existem como obrigação do empregador. A análise tratava como "relatórios que o cliente espera e não temos".
  - VET Levy existe como obrigação (limiar N$1.000.000 de folha), mas não temos relatório; Mohit disse em 09-18 que "só temos esses relatórios". Decisão de escopo (cobrir ou não) continua sem registro.
  - Taxa/teto SSC e ano fiscal, que a análise dava como "não respondidos", foram respondidos em 09-28.
  - Teto SSC: a análise lembrava "N$99 compatível com 0,9% × 11.000". Esse era o teto até 2026; o vigente passa a N$112,50. Ver "Conhecimento".
  - Descompasso de nomes (Form 10/PAYE 5/ETX versus PAYE Return/SSC Return): o "Monthly PAYE Return" da configuração é provavelmente o ETX [INCERTO, não dito no ticket].
- **Conhecimento a absorver:**
  - Valores com vigência e fonte para a hub da Namíbia: PAYE 2026/27 (acima); SSC 0,9%/0,9%, máx. N$12.500 (GN 236/2026, GG 8975), vigência legal 2026-03-01, aplicação pela SSC 2026-09-01 (anúncio da SSC, o ticket não cita o documento; o rascunho de pesquisa também não achou o Public Notice, então a data de aplicação continua sem fonte primária no cérebro); N$14.000 a partir de 2027-03-01; VET Levy 1% (GN 67/2021).
  - **Ponto de atenção:** em 2026-08 o WT 2551 ainda estava com teto N$99 (HRBS-13602). Conferir se WT 2551/2550 passaram a N$112,50 em 2026-09-01. Não consta no ticket.
  - Namíbia: o conjunto estatutário do empregador é ETX mensal + PAYE5 + SSC (portal) + VET Levy (NTA, se folha >= N$1 mi). Não existe IT12E/IT14E do empregador.

---

# CONGO E CÔTE D'IVOIRE (AF)

## HRBS-12110: revisão da report matrix do Congo
- **Estado:** Open, SLA -20d → **In Progress** (API 10-09), assignee Wallisson, atualizado 2026-10-08.
- **O que aconteceu depois do snapshot:**
  - 2026-08-13 16:54, Wallisson: matriz **não está pronta** para o cliente. Achados (lado estatutário): (1) aba "note" descreve os relatórios do **Senegal** (État 1024, TRIMF, CFCE, IPRES); o Congo usa ITS+TUS (DGID) e PVID/PF/AT-MP (CNSS); (2) aba CG-CNSS vazia; (3) aba CG-DAS-001 vazia; (4) CG-DGID-001 diz envio por XML/télédéclaration, mas a DGID do Congo é por portal e não existe XML/XSD para nenhuma declaração CG; (5) o total de ITS do CG-DGID-001 (279.300 XAF) está ~10x errado para 120 empregados: equivale ao valor anual de um empregado; o mensal agregado seria ~2.793.000.
  - 2026-10-06/07, Pradeep: "ainda precisa?" e aviso de fechamento. 2026-10-07, o solicitante: "ainda preciso".
- **Solução final:** **continua aberto.** Falta: o que exatamente o solicitante ainda precisa depois do parecer (matriz corrigida? nova versão?). Não consta no ticket. Dono: Wallisson (assignee), perguntar ao solicitante.
- **Correções à análise de 10-08:** "sem resposta nos snapshots" estava errado: o parecer go/no-go (não vai) saiu em 08-13, no mesmo dia do export de 08-13, depois do snapshot. Erro identificado: a matriz tinha conteúdo de outro país (Senegal) e valores ~10x errados; não era "nenhum".
- **Conhecimento a absorver:** Congo: ITS + TUS (DGID, portal), CNSS (PVID, PF, AT/MP); sem XML/XSD. Atenção: matrizes de cliente geradas por template copiam país errado.

## HRBS-12472: payslips Congo e Gabão (estado civil, filhos, partes)
- **Estado:** SLA Exempt, aberto no Congo → **Resolved** em 2026-08-12 06:23 (SLA "Breached"), assignee vazio.
- **O que aconteceu depois do snapshot:** 2026-08-11 17:59, Wallisson: igual ao Gabão, o payslip mostra estado civil e número de partes. O payslip já traz os dois no campo Situation Familiale/Quotient (exemplo dado: "Marié, 2 enfants, 3 parts"). Número de filhos não é exigido: é entrada do cálculo das partes (Art. 116 A-F, LF 2026), já refletido no quociente. Nada a acrescentar.
- **Solução final:** nenhuma mudança no payslip, em ambos os países. Versão do payslip: não consta.
- **Correções à análise de 10-08:** Congo "não resolvido" estava errado: resolvido em 08-11 com base legal (Art. 116 A-F, LF 2026). Nota: o exemplo "Marié, 2 enfants, 3 parts" já exibe a contagem de filhos dentro do texto do campo, o que mitiga a lacuna sem campo próprio.
- **Conhecimento a absorver:** Congo e Gabão: payslip mostra situação familiar + partes (quociente); nº de filhos não é campo obrigatório (Art. 116 A-F, LF 2026 no Congo). O CCG do Congo ainda precisa do 58204 "No Child" (0,5 parte), de `correcoes.md`.

## HRBS-13841: CAMU ausente na WTC do Congo
- **Estado:** Pending on reporter → **Resolved** em 2026-08-31 19:42 (SLA "Met"), assignee Wallisson.
- **O que aconteceu depois do snapshot:** nada depois de 08-31 12:54 (pergunta do solicitante se os 4,55%/2,27% são estatutários). O ticket foi resolvido às 19:42 sem comentário de fechamento. A resposta de Wallisson de 08-27 já dizia: dois fluxos separados na CAMU Congo (camu-congo.fr): 4,55% empregador / 2,27% empregado (6,82% combinados) e, à parte, 0,5% de "contribution de solidarité nationale" sobre a fração do salário acima de 500.000 XAF; a fórmula do cliente bate com a segunda.
- **Solução final:** esclarecimento de 08-27; o rótulo do cliente "CAMU Health Insurance (Employee)" é, na verdade, a solidarité de 0,5%. A pergunta de 08-31 foi fechada sem resposta explícita, embora a fonte citada já implique que 4,55%/2,27% são estatutários. Decisão de WT de solidarité na WTC de compliance: não consta.
- **Correções à análise de 10-08:** "Pending on reporter" → resolvido sem a última pergunta respondida. A relação com a correção do design CG de 2026-08-28 (limiar de solidariedade 6.000.000 anualizado para 500.000) continua [INCERTO]; o ticket não faz a ligação.
- **Conhecimento a absorver:** Congo, CAMU: 4,55% ER + 2,27% EE (fonte camu-congo.fr) e solidarité 0,5% sobre a parcela acima de 500.000 XAF/mês. Vigência: não consta.

## HRBS-14054: TUS subestimado (gross-up de car allowance)
- **Estado:** Open → **Resolved** em 2026-09-08 09:01 (SLA "Breached"), assignee Wallisson.
- **O que aconteceu depois do snapshot:** 2026-09-02 16:10, Wallisson: sim, o valor com gross-up entra na base do TUS. O TUS é 7,5% da remuneração bruta total (salário, primes, indemnités, avantages en nature), sem deduções, pela Loi n°42-2025 (LF 2026). O car allowance com gross-up é remuneração bruta paga ao empregado, não categoria à parte. O ticket foi resolvido em 09-08 sem comentário.
- **Solução final:** resposta T7 dada com fonte. O problema original (gross-up ausente para 2 empregados no g2n do cliente) segue sendo dado do cliente.
- **Correções à análise de 10-08:** "Taxa de 7,5% sem fonte" e "resposta não consta" resolvidos: Loi n°42-2025 (LF 2026). A análise já suspeitava corretamente que a resposta era "sim".
- **Conhecimento a absorver:** Congo TUS: 7,5% da remuneração bruta total, incluindo gross-up de benefícios com líquido garantido (Loi n°42-2025, LF 2026). Vigência: ano fiscal 2026.

## HRBS-14055: taxa de ocupação e taxa regional são regulatórias no Congo?
- **Estado:** Open → **continua Open** (atualizado 2026-10-07 12:20), assignee Wallisson, SLA "Breached".
- **O que aconteceu depois do snapshot:** 2026-09-02 16:09, Wallisson respondeu (a análise de 10-08 não tinha): nenhuma das duas é dedução estatutária por empregado no Congo. **Occupancy Tax:** existe imposto com esse nome (Taxe d'Occupation des Locaux à usage professionnel, TOL Prof), mas é anual, sobre imóveis comerciais, cobrado da empresa; a estrutura da WTC (XAF 1.000/mês descontados de cada empregado) não corresponde. **Region Tax:** nenhuma base legal encontrada, em referências completas e atuais de ITS, TUS, CNSS e CAMU; consistente com a nota da própria WTC que o marca como não confirmado. Sem resposta do solicitante registrada.
- **Solução final:** resposta de Compliance dada; ticket só aguarda fechamento/confirmação do solicitante. O que falta: o solicitante confirmar e remover as duas linhas da WTC dele. Dono: Daniel/Implementação; Wallisson pode pedir fechamento.
- **Correções à análise de 10-08:** "resposta de Wallisson não consta" estava errado; a resposta existe desde 09-02. A lacuna na WTC de compliance fica descartada: não há o que incluir.
- **Conhecimento a absorver:** Congo: Occupancy Tax (TOL Prof) é imposto anual da empresa, não desconto de folha; Region Tax não tem base legal. Não incluir no WTC de compliance.

## HRBS-14714: aplicabilidade do ITS e faixas/RICF (Côte d'Ivoire)
- **Estado:** Open (snapshot "1 of 6", possivelmente truncado) → **Resolved** em 2026-09-21 09:02, assignee Mohit, SLA "Met".
- **O que aconteceu depois do snapshot:**
  - 2026-09-17 00:21, Wallisson: **o ITS se aplica e deve ser retido.** Fontes: Ordonnance n°2023-719 (13 set 2023), nota de doutrina DGI N°00026/MFB/DGI/DLCD (3 jan 2024), CGI art. 119 bis, inalterados pela LF 2026. Faixas mensais aplicadas direto sobre a remuneração bruta, sem abatimento: 0-75.000 XOF 0%; 75.001-240.000 16%; 240.001-800.000 21%; 800.001-2.400.000 24%; 2.400.001-8.000.000 28%; acima de 8.000.000 32%. **RICF** (CGI art. 120): subtraído do ITS bruto, com piso 0: 5.500 XOF por 0,5 parte acima da primeira, máximo 5 partes. O pay register estava protegido por senha; foi pedida uma cópia aberta.
  - 2026-09-17 06:23, o solicitante informa a senha (não reproduzida).
  - 2026-09-17 15:36, Wallisson: a WTC CI-ITS está configurada corretamente pela posição estatutária confirmada.
- **Solução final:** faixas, RICF e fontes confirmados; WTC de ITS validada contra o pay register. Resolvido em 09-21.
- **Correções à análise de 10-08:**
  - Corrige o "aparente truncamento": havia 3 comentários de Wallisson (09-17), com a resposta completa. O snapshot estava realmente incompleto.
  - "Duplicação 14714 × 14996" é incorreta. A 14714 (aplicabilidade e faixas) foi respondida em 09-17; a 14996 (regime fiscal único, 09-22) é um desdobramento posterior com pergunta diferente. Não é duplicata.
  - "Import sur les Treatments et Salaries" no ticket é erro do solicitante; o nome correto é Impôt sur les Traitements et Salaires.
- **Conhecimento a absorver:** Côte d'Ivoire, ITS (vigência: a partir da Ordonnance 2023-719, inalterado na LF 2026): faixas e RICF acima. Cálculo de conferência de 14996: 1.940.670,66 → 417.760,96, menos RICF 11.000 (2 partes) = 406.760,96 (confere com as faixas).

## HRBS-14996: "Single Tax Regime" e isenção de ITS; tetos CNPS; defeitos do GTN
- **Estado:** Pending on reporter, cliente escalou "ao Marko" → **Resolved** em 2026-09-29 06:03, assignee Mohit, SLA "Met".
- **O que aconteceu depois do snapshot:**
  - 2026-09-28 14:48, Wallisson explica em inglês simples: a entidade é filial de empresa estrangeira (sede nas Bermudas, mãe nos Emirados) e, por isso e pela atividade de serviços petrolíferos, se enquadra no **regime fiscal dos prestadores de serviços petrolíferos estrangeiros**, no qual a empresa paga **6% fixos sobre o faturamento (IFPGAZ)**, o que cobre o que seria retido dos empregados. Confirmado por escrito pela DGI (carta de 19/08/2025, para 2025). A IFPGAZ é trimestral, devida até o fim do mês seguinte ao trimestre: T1/2026 até 30/abr, T2/2026 até 31/jul, T3 até 31/out. Pede ao cliente o T1 e o T2 de 2026. "Documentos todo ano" não é reaplicação do regime: o status se baseia em fatos estáveis (propriedade estrangeira, atividade); o que é contínuo é a declaração trimestral.
  - 2026-09-28 14:54/23:03, Govind pergunta e Wallisson confirma: a entrega de **qualquer um** dos retornos (T2 de preferência) confirma o regime em 2026; então o ITS para; **CNPS e CMU continuam descontados.**
  - 2026-09-29 06:03, Mohit: "Done. You may test tomorrow." Procedimento: **marcar "Stop Tax = Yes" em Employer Information, nos HR fields da Legal Entity.**
- **Solução final:** o "flag" pedido foi criado como atributo da **entidade** (Stop Tax = Yes), não por empregado. Base: regime des prestataires de services pétroliers (IFPGAZ), carta DGI n° 0984/MFB/DGI/DGE (19/08/2025), prova de nacionalidade estrangeira (Annexe fiscale 2019, art. 26). Não consta no ticket se o cliente entregou o retorno T1 ou T2 de 2026 antes de o flag ser ligado, nem como o "Marko" fechou a escalação.
- **Correções à análise de 10-08:**
  - A lacuna "consequência legal do regime petroleiro para o ITS não explicada [INCERTO]" fica explicada (IFPGAZ 6% substitui a retenção). O artigo legal específico que isenta o ITS sob esse regime ainda não é citado.
  - A "mudança de enquadramento entre as respostas 1 e 3" é coerente: primeiro afastou o impôt synthétique; depois o regime petroleiro, o correto.
  - **Banda apprentice / flag 58216 continua sem resolução.** Nenhum comentário posterior trata dos defeitos do GTN (pensão CNPS lançada e estornada; empregado acima do teto com valores da linha apprentice; rótulos de WT; sem linha CE; transporte/moradia nas bases). Wallisson disse que seriam tickets separados; nenhum ID aparece. Não há outro ticket da CI no lote baixado que os trate. O CT-A-620 (spec) ainda não foi relido.
  - Teto 70.000 (PF 5%, maternidade 0,75%, AT/MP 2-5%) × 75.000 (SMIG, piso da assiette) ficou como respondido, sem contestação.
- **Conhecimento a absorver:**
  - Côte d'Ivoire: nome de regime não é isenção; exigir instrumento. Impôt synthétique/micro-entreprise exclui o ITS por lei. Prestadores petrolíferos estrangeiros (IFPGAZ) ficam fora do ITS dos empregados com prova anual/trimestral; CNPS e CMU continuam.
  - Procedimento no sistema: HR field da Legal Entity, "Stop Tax".
  - Teto 70.000 XOF/mês (PF, maternidade, AT/MP); pensão teto 3.375.000 (45 × SMIG); 75.000 = SMIG (CLEISS CI, 2025-01-01).
  - Rótulos CNAMGS/FNH são de órgãos do Gabão, não CI.

---

# COLÔMBIA (PMI, transição para Instaroll)

Todos os cinco abaixo seguem a mesma linha do tempo posterior a 09-16: 2026-09-24 19:13/19:16 Wallisson posta "Colombia re-design is ready" cruzando a pesquisa nova com cada ticket (CO-CCG-001 v1.1, CO-WTC-001 v1.1, CO-DD-001 v1.0); 2026-09-25 04:20/04:21 Mohit: "se o ponto está no CCG, não precisa reatribuir; pode fechar"; 2026-09-30 12:00 os cinco são **Resolved**, assignee Mohit, SLA "Breached". O estado antes era Pending on reporter/Open. Em nenhum dos cinco há comentário do cliente depois da resposta.

## HRBS-12487: automação do vacation bonus offcycle (limite de 95 UVT)
- **O que aconteceu depois do snapshot:** 2026-09-18 17:38 o cliente reanexa a planilha. 2026-09-24 Wallisson responde: (1) **não existe limite de 95 UVT** para o bônus: 95 UVT é a primeira faixa da tabela geral (ET art. 383); (2) a tabela 8/9/10% do cliente não corresponde a nenhum mecanismo colombiano: as contribuições do empregado são planas sobre o IBC (4% saúde, 4% pensão, FSP a partir de 4 SMMLV; Ley 100 arts. 18, 20, 204); (3) com pacto escrito do art. 128, o bônus fica fora do IBC até 40% da remuneração total; o excesso volta (Ley 1393 art. 30); (4) retención: o bônus se soma aos demais rendimentos do mês (ET arts. 383, 388); (5) G2N: 62837 bruto, uma linha de retención; 62838 (becas) excluído. Referência: CO-CCG-001 v1.1 Módulo 13; CO-WTC-001 v1.1 CO-PRIMA-VACACIONES-EXTRALEGAL.
- **Solução final:** não é automação da regra do cliente; é o redesenho: a regra correta está no CCG/WTC v1.1. A implementação no sistema/Instaroll não consta.
- **Correções à análise de 10-08:** a hipótese [INCERTO] "95 UVT coincide com a primeira faixa do art. 383" está **confirmada** e vira argumento central: o limite do cliente não tem base legal. A "lacuna de design" se resolve no CCG v1.1, não por regra sobre 95 UVT. Aviso do próprio cliente: a planilha pede para netar o bônus no 62837; a solução manteve o bruto.
- **Conhecimento a absorver:** Colômbia: vacation bonus extralegal: sem limite 95 UVT; IBC conforme pacto art. 128 + 40% (Ley 1393 art. 30); retención junto ao rendimento mensal; 62837 bruto, 62838 sem SS nem retención.

## HRBS-12491: cálculo de embargos (garnishment)
- **O que aconteceu depois do snapshot:** 2026-09-24 Wallisson: (1) método: deduções legais primeiro, depois o SMMLV, depois 1/5; base é o salário líquido (DIAN Concepto 004032 int 368 de 16/03/2026; Corte Constitucional T-891 de 2013); (2) valor fixado pelo juiz é aplicado como ordenado (CST art. 155); o 1.548.190 está abaixo do teto; (3) ordens só sobre salário básico: mesma regra naquela base; (4) pensão alimentícia e dívidas cooperativas: 50% do salário todo, mesma base líquida (art. 156); (5) prestações sociais são inembargáveis, salvo esses dois casos, limitado a 50% (art. 344), alcançando o bônus de férias e a prima de serviços nesta base; (6) base igual ou abaixo de 1 SMMLV: zero, nunca negativo (art. 154); (7) SMMLV 2026: 1.750.905 (Decreto 1469 de 2025, restabelecido por auto do Consejo de Estado de 9/07/2026, rad. 11001-03-25-000-2026-00004-00). CO-CCG-001 v1.1 Módulo 4; CO-WTC-001 v1.1 CO-DED-EMBARGO, CO-DED-ALIMENTOS.
- **Solução final:** regra documentada com base legal; implementação no sistema: não consta.
- **Correções à análise de 10-08:** a divergência 2.072.641 × 1.548.190 está **explicada**: valor fixado em juízo, abaixo do teto de 1/5, aplicado como ordenado. O SMMLV 2026 e o 1/5 agora têm fonte (acima), então o item T12 da análise cai. O ponto do SMMLV hard-coded permanece como requisito de design (parâmetro anual).
- **Conhecimento a absorver:** SMMLV 2026 = 1.750.905 (vigência 2026; Decreto 1469/2025, restabelecido pelo Consejo de Estado em 2026-07-09). Embargo: líquido de deduções legais - 1 SMMLV, 1/5; piso zero; valor judicial prevalece.

## HRBS-12492: regras de seguridade social (empregado e empregador)
- **O que aconteceu depois do snapshot:** 2026-09-24 Wallisson: (1) confirmado: IBC de 1 a 25 SMMLV (Ley 100 art. 18); regra dos 40% (Ley 1393 art. 30); as taxas; a exoneração abaixo de 10 SMMLV (ET art. 114-1), nunca da CCF; (2) a exoneração se perde **exatamente em 10 SMMLV**: o art. 114-1 diz "menos de diez (10)"; (3) dias de férias: contribui sobre o último IBC anterior às férias, base legal **Decreto 780 de 2016 art. 3.2.5.1, não o Decreto 1072 art. 3**; (4) salário integral: IBC de 70%, logo 70% do mês anterior nos dias de férias. CO-CCG-001 v1.1 Módulos 4, 5 e 8; CO-WTC-001 v1.1 linhas 62300, 62302 e CO-VACACIONES.
- **Solução final:** regras confirmadas e documentadas; a hipótese do Support (IBC de férias sobre o bruto do mês) é o erro conhecido que o redesenho corrige. Implementação: não consta.
- **Correções à análise de 10-08:** o [INCERTO] sobre a norma de IBC em férias está resolvido: a citação do cliente (Decreto 1072/2015 art. 3) estava errada; vale Decreto 780/2016 art. 3.2.5.1. O cliente também escreveu "até 10 SMLMV" onde a lei diz "menos de 10". O percentual do Fundo de Solidariedade e a lista de conceitos não salariais não foram tratados no comentário [não consta].
- **Conhecimento a absorver:** exoneração (ICBF, SENA, saúde do empregador) só com salário < 10 SMMLV (ET art. 114-1); IBC em férias: Decreto 780/2016 art. 3.2.5.1; integral = 70%.

## HRBS-13627: cálculo da retención en la fuente
- **O que aconteceu depois do snapshot:** 2026-09-24 Wallisson: (1) UVT 52.374 (Res. DIAN 000238/2025), tabela do art. 383, limite de 40% (art. 388) e teto anual de 1.340 UVT (**ET art. 336 num. 3; Decreto 1625 art. 1.2.4.1.6 par. 3**): tudo correto; (2) a divisão por 1/12 é prática de mercado, não prescrita; a nota do arquivo sobre acumulação anual está certa; (3) a leitura separada da tabela para a prima vale só no Procedimento 1 (ET art. 385; DIAN Oficio 68292 de 2013); no Procedimento 2 ela entra na base do mês, como os bônus extralegais; (4) não residentes: 20% sobre o bruto (ET art. 408) até a residência aos 183 dias (ET art. 10); o art. 383 se aplica prospectivamente, sem true-up (DIAN Concepto 011108 de 2026); (5) os 20% valem só enquanto não residente; instrução escrita do cliente não desloca a responsabilidade por sub-retenção (ET art. 370). CO-CCG-001 v1.1 Módulo 6; CO-WTC-001 v1.1 CO-TX-08; CO-DD-001 v1.0 Tax Residence Status.
- **Solução final:** validador do cliente confirmado quanto aos limites; Expat/não residente tem base legal; campo de residência fiscal entra no DD. Acumulador anual do teto de 1.340 UVT: o motor segue com 1/12; a necessidade de acumulador não foi resolvida no comentário.
- **Correções à análise de 10-08:** (a) [INCERTO] "Art. 388 vs 336": o teto de 1.340 UVT é do **art. 336 num. 3**; o 40% é do art. 388. O ticket do cliente atribuía os dois ao 388. (b) Expat 20% "sem base legal" resolvido: ET art. 408 + art. 10. (c) A aritmética em COP da coluna de referência (3.446.732 e 5.847.117 contra 3.447.955 e 5.848.430) não foi comentada; a própria Wallisson usa 3.447.955 no HRBS-12487. Continua sendo só coluna de referência. (d) "Procedimento 2 recalculado só em junho e dezembro" está coerente com o art. 386 [não contestado].
- **Conhecimento a absorver:** Colômbia 2026: UVT 52.374; tabela art. 383; teto 40%/1.340 UVT (art. 388/336); não residente 20% (art. 408) até 183 dias (art. 10); prima no Procedimento 1 por tabela própria, no 2 junto à base.

## HRBS-13692: provisões de cesantías e juros
- **O que aconteceu depois do snapshot:** 2026-09-24 Wallisson: (1) uma remuneração mensal por ano de serviço (CST art. 249); variável usa a média do último ano (art. 253); (2) juros de 12% a.a. sobre o saldo (saldo × 12% × dias / 360), pagos até 31 de janeiro ou na rescisão (Ley 52 de 1975 art. 1); (3) o auxílio de transporte entra nas duas bases (Ley 1 de 1963 art. 7), mas fica fora das férias e das bases de SS e parafiscales; (4) Ley 2466 art. 64: o juro mensal de 1% é operável já, por acordo escrito; o depósito mensal de 8,33% não, porque passa pelo PILA e o decreto ainda é rascunho do MinTrabajo (julho/2026); o depósito anual é a única via hoje; (5) a base deve incluir o auxílio de transporte; o portal do operador calcula sobre o salário básico e fica curto em COP 249.095 no salário mínimo; depósito tardio custa um dia de salário por dia (Ley 50 de 1990 art. 99 num. 3); (6) **22110 e 22112 são códigos contábeis do cliente, não estatutários.** CO-CCG-001 v1.1 Módulo 9; CO-WTC-001 v1.1 CO-CESANTIAS, CO-PROV-CESANTIAS, CO-INTERESES-CESANTIAS; CO-DD-001 v1.0 Severance-Savings Deposit Arrangement.
- **Solução final:** cálculo e provisão modelados no CCG/WTC v1.1. **O relatório de consolidação (~16 colunas) não é mencionado** na resposta; não consta decisão sobre Report Spec.
- **Correções à análise de 10-08:** "T3 [INCERTO] conferir WTs 22110/22112" resolvido: são códigos do cliente; as WTs de compliance são CO-PROV-CESANTIAS e CO-INTERESES-CESANTIAS. O prazo de pagamento dos juros agora tem fonte (31 jan, Ley 52/1975). Fórmula 12% e /360 confirmadas.
- **Conhecimento a absorver:** cesantías: 1 salário/ano (art. 249); juros 12% a.a. (Ley 52/1975); base inclui auxílio de transporte; depósito mensal de 8,33% ainda não operável (julho/2026).

---

# CHILE E CHINA

## SR-221: Report Spec LRE (Chile)
- **Estado:** In Progress (10-08) → **In Progress** (10-09), assignee Ruchi Gupta, fase "Product Mapping Phase - Business Analyst", atualizado 2026-09-28 15:09. Due date 2026-07-31 (vencida).
- **O que aconteceu depois do snapshot:** 2026-09-28 15:08, Wallisson: coluna **AE** adicionada na WTC com o código LRE por wage type (**Version Control 1.4**); o campo Previred do SR-232 está na coluna AD; alguns itens estão marcados "Review" porque o código depende de como o cliente paga; pede o ok da BA para finalizar.
- **Solução final:** o pedido da coluna de Report Code está atendido na WTC CL v1.4. **Continua aberto:** a BA (Ruchi) precisa aprovar; itens "Review" dependem de decisão do cliente; versão apagada em maio não foi recuperada (não consta).
- **Correções à análise de 10-08:** as datas reais: ticket criado 2026-04-25; troca "apaguei a versão" em 2026-05-26/27 (a análise dizia 05-28/30). "Coluna no WTC não resolvida" estava defasada: foi feita 3 horas depois do snapshot.
- **Conhecimento a absorver:** WTC CL com uma coluna por relatório (AD Previred, AE LRE); versões 1.3 e 1.4 no mesmo dia. Regra de processo: não apagar versão revisada pela BA (F59).

## SR-232: Report Spec Previred (Chile)
- **Estado:** Open → **Open**, assignee Ruchi Gupta, atualizado 2026-09-28 12:22. Due date 2026-07-31 (vencida).
- **O que aconteceu depois do snapshot:** 2026-09-28 12:21, Wallisson: coluna **AD** na WTC com o campo Previred por wage type (**Version Control 1.3**); pergunta se a BA prefere o código LRE e promete finalizar.
- **Solução final:** coluna entregue; aguarda confirmação da BA. A pergunta "Previred ou LRE" foi respondida em seguida com a coluna AE (SR-221).
- **Correções à análise de 10-08:** "coluna no WTC pendente" resolvida em 09-28. Ticket criado em 2026-05-02.
- **Conhecimento a absorver:** nenhum além do SR-221.

## SR-316: CN Payslip (China)
- **Estado:** Open, assignee Wallisson → **Open**, assignee Michael Mukosi John, fase **"Development Phase - Developer"**, atualizado 2026-10-08 02:57.
- **O que aconteceu depois do snapshot:**
  - 2026-08-11, Enaakshi agradece a Wallisson e pede à Lily para conferir o payslip revisado (Wallisson revisou a spec).
  - 2026-08-17, Lily: aplicou na spec (em verde) título do payslip na coluna D, data de pagamento 发薪日期 (em vez de 发放日期), documento 证件号码 (em vez de 居民身份证号, porque nem todos têm 居民身份证号), seções de Earnings/Deductions/Employer Contribution com os campos padrão Compliance, e substituiu a seção "ITT Calculation Basis". Perguntas em amarelo: número de contrato é exigido? seção de leave balances é necessária? os campos da IIT Calculation Basis não são cumulativos, inconsistente com a retenção cumulativa de residentes; linhas 146-148 removidas.
  - 2026-08-21, Lily e Enaakshi confirmam as mudanças.
  - 2026-10-08 02:57, Lily encaminha ao Developer: "desenvolver conforme a spec do payslip; os samples diferem um pouco; não desenvolver pelo sample".
- **Solução final:** payslip convertido ao formato Compliance e aprovado em 2026-08-21; em desenvolvimento. Respostas às perguntas de contrato, leave balances e campos não cumulativos da IIT: não constam no ticket.
- **Correções à análise de 10-08:** "não resolvido; apenas pedido de ajuda" superado. A origem do v1.0 [INCERTO] continua sem esclarecimento; o ticket foi criado em 2026-06-28 (a análise dizia ~julho). O arquivo ainda se chama `CN_Compliance_Payslip_2026_V1.0` no ticket; a versão revisada não é nomeada.
- **Conhecimento a absorver:** China payslip: usar campos padrão Compliance; 发薪日期 e 证件号码; spec de payslip manda sobre o sample.

---

# HOLANDA, IRLANDA, LITUÂNIA, SINGAPURA

## HRBS-14675: percentuais de SSI desatualizados no relatório `netherland-ssc-pdf` (Holanda)
- **Estado:** Pending on reporter → **Pending on reporter**, assignee Shaik Jani Sharif (Configuration Support), atualizado 2026-10-08.
- **O que aconteceu depois do snapshot:**
  - 2026-09-21 16:22, Wallisson: **não é relatório estatutário de Compliance**, portanto sem spec ("nenhuma existe porque nenhuma deveria"). O Art. 7.2 URLB 2011 exige a loonstaat por empregado, com dados do empregado no cabeçalho; não existe formulário coletivo no artigo, e esta saída tem só dados do empregador. Contribuições do empregador são declaradas na aangifte loonheffingen, não em PDF-resumo. Custom Reports é a colocação correta.
  - 2026-09-22/24, Shaik pede ao solicitante uma spec; Suresh anexa a report matrix de NL e afirma que os dois relatórios (Collectieve premieloonstaat e Cumulatieve premieloonstaat) são padrão e obrigatórios no BPQ. 2026-09-24, Mohit: **não é relatório de Compliance; o consultor do projeto precisa revisar e aprovar.**
  - 2026-09-24 e 10-01: Suresh repete os percentuais, acrescenta UFO 0,68%, e diz que valem para todos os clientes. 2026-10-01, Romano: Compliance não confirma os percentuais; o requisito deve ser esclarecido antes e depois a Configuração entra.
  - 2026-10-01, Shaik: abriu o ticket **HRBS-14401** (campos do empregador não aparecem quando o relatório é agrupado por entidade). 2026-10-08, Suresh pergunta sobre ZW Flex e WGA.
- **Solução final:** **continua aberto.** Posição de Compliance firmada: não é estatutário, Compliance não valida percentuais. Falta: o consultor do projeto aprovar e a Configuração atualizar os percentuais e resolver o HRBS-14401 (ZW Flex/WGA vêm do campo "company details" do Legal Entity). Dono: Configuração (Shaik) com o consultor (Suresh).
- **Correções à análise de 10-08:** "ninguém definido como dono" fica definido: Configuração/Reports e consultor do projeto, fora do nosso escopo. "Pode não ser artefato do nosso serviço" confirmado. O relatório está "no BPQ e na report matrix" mas não no catálogo estatutário: a fronteira exige nota em `fronteiras.md`.
- **Conhecimento a absorver:** NL: loonstaat é por empregado (URLB 2011 Art. 7.2); a "premieloonstaat" coletiva/cumulativa é relatório de cliente, não estatutário. Compliance não valida taxas de relatório Custom. Percentuais da lista de Suresh: sem fonte oficial no ticket (⚠️ sem fonte).

## HRBS-13860: arquivo NAERSA falhando (Irlanda)
- **Estado:** In Progress, assignee Romano → **Resolved** em 2026-10-05 06:36, assignee Romano, prioridade High, SLA "Breached" ("It depended on some other team").
- **O que aconteceu depois do snapshot:**
  - 2026-08-27 15:01, Wallisson: causa-raiz: a validação da API rejeita `prsiClass` vazio (o schema PSR da Revenue exige `[A-Za-z][0-9A-Za-z ]?`). Dois empregados (um por entidade, Clavis e OMG) saíram com classe em branco e deveriam ser A1 e A0 pelo último payslip ativo. Eram lançamentos de fechamento de leaver (valor zero ou negativo, período final) que perderam a classe em vez de herdar da última linha ativa.
  - 2026-08-27 15:19, Romano informa que a NAERSA estava com **queda de serviço**, afetando as submissões, e que as retentativas seriam noturnas.
  - 2026-08-31 09:52, Romano documenta a análise de Wallisson: é um **defeito sistêmico do motor de cálculo**: para lançamentos de leaver/fechamento, a classe PRSI é derivada do bruto do período de fechamento em vez de herdar a classe da última linha ativa; com pagamento 0 ou negativo, cai no default **J0**. Em dois casos a classe saiu em branco (falha de validação); em outros, genuínos A1 foram enviados como J0 (passam no schema, sem alerta). Wallisson verificou **45 leavers adicionais** no arquivo de agosto, A1 reais (€4.583 a €11.126/mês), enviados como J0. Ação: corrigir a lógica para herdar do último período ativo ou do cadastro; investigar por que dois saíram em branco; corrigir manualmente no cartão do empregado para cumprir o prazo; RCA e correção permanente com prioridade; validar os 45.
  - 2026-08-31 10:07, Mohit: existe override **"PRSI Class Subclass"** no sistema para esses casos; estava oculto para a Omnicom.
  - 2026-09-10, Yojana (cliente/consultoria) lista novos defeitos de integração NAERSA: (1) AEPN com valor "0" (empregado isento) é recusado, e para isento com 0% AEPN não se deve enviar contribuição; (2) `payrollRunReference` deve ser único e hoje se repete; (3) falhas de dados aparecem como "Outbound API failed"; a 1ª submissão (27/ago) voltou `fileAcknowledged=true` com erros vazios; as seguintes devolveram MFFERR020 ("File has already been submitted with errors"); códigos MFFWAR046 e MFFERR038 não mapeados.
  - 2026-09-11, Illya (INT): a equipe de integração investiga a resposta da interface; demais perguntas vão para Compliance e Configuração de relatórios.
  - 2026-10-05: Resolved sem comentário de fechamento.
- **Solução final:** **correção manual das classes** (cartão do empregado/override) para entregar o arquivo; o ticket foi fechado sem registro da correção permanente do motor nem do tratamento dos 45 leavers, da unicidade do `payrollRunReference`, do 0% AEPN ou do mapeamento de erros. Dono da correção permanente: equipe de cálculo/regulation Irlanda e INT. Estado: não consta.
- **Correções à análise de 10-08:**
  - Causa raiz era "não consta [INCERTO] dado mestre ou DD": agora é **defeito do motor de cálculo/regulation de PRSI para leavers**, não do DD, nem do cliente, nem de enum de DD. T4 [INCERTO] cai; T10 cai.
  - A queda de serviço da NAERSA explica parte das falhas de 08-27, mas não a de classe vazia.
  - É um erro nosso novo, **não estava na seção 5 do catálogo**.
- **Conhecimento a absorver:** Irlanda: leaver/closing entry não pode recalcular a classe PRSI pelo bruto (vira J0); herdar da última linha ativa. Override "PRSI Class Subclass" disponível. NAERSA: AEPN 0% = isento, não enviar contribuição; `payrollRunReference` único; mapear MFFERR020/038 e MFFWAR046.

## HRBS-15253: verificação de cobertura de cálculo e reporting (Lituânia, Accenture)
- **Estado:** Open → **Open**, assignee Wallisson, atualizado 2026-10-02 18:02.
- **O que aconteceu depois do snapshot:**
  - 2026-09-28 20:17, Wallisson responde:
    1. **Baseline de Compliance existe** (pasta Drive Country Folders > Lithuania): CCG 2026, WTC V3.0 e DD V3.0 (ambos aprovados em jun/jul 2025); specs de SAM (com SAM3SD/SAM3SDP), GPM313 e GPM312 (com GPM312L/U); payslip generator (EN/LT). O CCG 2026 **não tem registro de versão nem sign-off formal.**
    2. Cada spec registra a versão do formulário oficial: SAM v07; GPM313 conforme VA-105 de 20/11/2025; GPM312 conforme VA-24 de 26/03/2026. **Não especificados:** formulários Sodra por evento (1-SD, 2-SD, 9-SD, 12-SD, 13-SD, NP-SD, PT; só há referências de 2025 para 1-SD, 2-SD e NP-SD) e o registro de integração (.ffdata, canais EDAS/EDS, caminho de teste).
    3. O status S/C/M/N de cada linha e as saídas de banco, GL e reconciliação são de Configuração/Produto.
    4. Correções segundo o CCG (não revalidadas): Sodra reenvia o mês de referência; o GPM é tributado no mês do pagamento, sem reenvio; SAM atrasado exige PT com código de motivo 01 (spec do SAM). **Não há documentação** sobre retificação do GPM313 após mudança no GPM312.
    5. Arquivos de QC e mapeamento G2N das folhas 2025 da Lituânia estão no Drive (CT-3410, CT-3568); a referência de cliente é do time de Implementação.
  - 2026-10-02 18:02, Kevin propõe uma call, com urgência para o início do cliente.
- **Solução final:** **continua aberto.** Falta: a call (Kevin/Wallisson), a matriz S/C/M/N (Configuração/Produto), a decisão sobre specs dos formulários por evento e integração .ffdata, e o sign-off do CCG 2026.
- **Correções à análise de 10-08:** "não consta se existe dossiê para a Lituânia" resolvido: existe (CCG 2026, WTC V3.0, DD V3.0, specs, payslip). Pergunta 4 (parameter sheet assinada): não existe sign-off formal do CCG 2026. Pergunta 5 (já entregou Lituânia): há folhas de 2025 com QC (CT-3410/3568).
- **Conhecimento a absorver:** Lituânia: baseline e lacunas (eventos Sodra, integração, retificação GPM313/GPM312, sign-off do CCG 2026). Versões de formulário: SAM v07; GPM313 VA-105 (2025-11-20); GPM312 VA-24 (2026-03-26).

## HRBS-15630: teto de AW do CPF com salário de outubro não pago (Singapura, GSK)
- **Estado:** In Progress, assignee Wallisson → **In Progress**, assignee agora **Shruti Sanjay Kamble** (Compliance Support), atualizado 2026-10-08 15:23, Resolution Time ~4d.
- **O que aconteceu depois do snapshot:** 2026-10-07 12:31, Wallisson responde: o overtime é Additional Wages (AW); o CPF sobre ele é limitado pelo teto de AW restante de 2026 (**S$102.000 menos o OW do ano sujeito a CPF**). O salário de outubro conta nesse OW **mesmo com o OT Run vindo antes**, porque o CPF é mensal e o teto usa o OW estimado do ano inteiro. Os três salários estão calculados no main run (REF-P202-857, segundo os screenshots). Empregado 1: sem teto de AW restante (S$6.000 de S$6.000 usados no relatório YTD), logo 0 está correto. Empregado 2: 0 é consistente com teto esgotado. Empregado 3: EE 316 / ER 268 é consistente com cerca de S$1.580 de teto restante. Os valores esperados pelo cliente tratam o OT como único salário do mês e não se aplicam. Para confirmar os empregados 2 e 3: enviar os relatórios YTD de OW e AW (58553/58554) como o do primeiro.
- **Solução final:** **posição de Compliance: comportamento correto, não é defeito.** Aguarda os relatórios YTD do cliente para confirmar dois dos três casos; sem sign-off do OT Run. Dono: cliente (Deepak/Kevin) entrega os YTD; Compliance (Shruti/Wallisson) fecha. Resposta do cliente: não consta.
- **Correções à análise de 10-08:**
  - A hipótese principal ("acumulador YTD usa valor calculado, não pago; falta regra de ordem de runs") foi **contrariada** pela resposta: o teto de AW é por regra, com OW estimado do ano, e inclui o main run calculado. Não é defeito; a análise tratava como defeito provável.
  - O "esperado" do cliente (OW de outubro = 0) fica sem base. O significado de "2553" da Crina continua obscuro; não explicado.
  - IDs de payroll continuam inconsistentes (936, 937, 857, 859). Wallisson usa REF-P202-857.
  - Taxas 20%/17% eram inferência; não confirmadas no ticket.
- **Conhecimento a absorver:** Singapura CPF: AW tem teto de S$102.000 menos o OW anual sujeito a CPF, com OW estimado do ano, mesmo em run off-cycle anterior ao main run. OW teto mensal S$6.000 em 2026. Sem fonte oficial citada no ticket (⚠️ conferir CPF Board).

---

# RESUMO

## (1) Tabela

| ID | Estado antes | Estado agora | Resolvido de verdade? | Solução em 1 linha |
|---|---|---|---|---|
| HRBS-12072 | Open (SLA Exempt) | Resolved 2026-08-10 | Sim (Compliance); fechado por falta de resposta | Combinação Tax=Y/SSNC=Y/Pension=N não existe: Pension=Yes é default; cliente usa pay elements 21640/21641/21642 |
| HRBS-12101 | Open | Resolved 2026-08-12 | Sim, com pendência (PAYE 5) | ETX com sample; Form 10 é ação de portal sem arquivo; PAYE 5 a escopar |
| HRBS-12111 | Open | Resolved 2026-08-10 | Sim | Matriz do cliente corrigida (6 defeitos) e devolvida |
| HRBS-12483 | Open | Resolved 2026-09-16 | Sim quanto à resposta; fechado por inatividade | Sem edição na WTC; pensionável é por fundo; seguir a WTC do cliente |
| HRBS-13602 | Open | Resolved 2026-08-24 | Sim | Sem mudança: SSC não é dedutível do PAYE (ITA s.17); fórmula do cliente era da WT 21640 |
| HRBS-14605 | Open | Resolved 2026-10-08 | Respostas sim; entrega de relatórios não confirmada | PAYE/SSC/VET respondidos; IT12E/IT14E não existem; teto SSC N$12.500 |
| HRBS-12110 | Open | In Progress | Não | Matriz tinha conteúdo do Senegal e total de ITS 10x errado; falta saber o que o solicitante ainda precisa |
| HRBS-12472 | Open (SLA Exempt) | Resolved 2026-08-12 | Sim | Payslip já mostra estado civil e partes; filhos não exigido (Art. 116 A-F) |
| HRBS-13841 | Pending on reporter | Resolved 2026-08-31 | Parcial (última pergunta sem resposta) | Rótulo do cliente era a solidarité 0,5%; 4,55%/2,27% são os fluxos principais |
| HRBS-14054 | Open | Resolved 2026-09-08 | Sim | Gross-up entra na base do TUS (7,5%; Loi 42-2025) |
| HRBS-14055 | Open | Open | Parcial (respondido, ticket aberto) | Nenhuma das duas é desconto estatutário de folha |
| HRBS-14714 | Open (truncado) | Resolved 2026-09-21 | Sim | ITS aplica; faixas e RICF confirmados; WTC CI-ITS correta |
| HRBS-14996 | Pending on reporter | Resolved 2026-09-29 | Sim para o flag; defeitos do GTN sem ticket | Stop Tax = Yes na entidade (regime petroleiro/IFPGAZ); CNPS e CMU continuam |
| HRBS-12487 | Pending on reporter | Resolved 2026-09-30 | Sim (Compliance); build não confirmado | Sem limite de 95 UVT; regra correta no CCG/WTC v1.1 |
| HRBS-12491 | Pending on reporter | Resolved 2026-09-30 | Sim (Compliance); build não confirmado | Embargo: líquido - SMMLV, 1/5; valor judicial prevalece; SMMLV 1.750.905 |
| HRBS-12492 | Pending on reporter | Resolved 2026-09-30 | Sim (Compliance); build não confirmado | IBC 1-25 SMMLV, 40%, exoneração < 10 SMMLV, férias pelo Decreto 780/2016 |
| HRBS-13627 | Open | Resolved 2026-09-30 | Sim (Compliance); acumulador anual aberto | Limites do validador corretos; teto 1.340 UVT é art. 336; expat 20% (art. 408) |
| HRBS-13692 | Open | Resolved 2026-09-30 | Parcial (relatório de consolidação não tratado) | Cesantías e juros no CCG/WTC v1.1; 22110/22112 são códigos do cliente |
| SR-221 | In Progress | In Progress | Não | Coluna LRE (AE) na WTC CL v1.4; aguarda BA |
| SR-232 | Open | Open | Não | Coluna Previred (AD) na WTC CL v1.3; aguarda BA |
| SR-316 | Open | Open (Development) | Parcial | Payslip convertido e aprovado 2026-08-21; em desenvolvimento |
| HRBS-14675 | Pending on reporter | Pending on reporter | Não | Não é estatutário; Configuração atualiza os percentuais |
| HRBS-13860 | In Progress | Resolved 2026-10-05 | Parcial (correção manual) | Classe PRSI de leavers vira J0/branco por defeito do motor; override manual; fix permanente não consta |
| HRBS-15253 | Open | Open | Não | Baseline existe (CCG 2026, WTC/DD V3.0, specs); falta call, S/C/M/N e specs por evento |
| HRBS-15630 | In Progress | In Progress | Não | Comportamento correto pelo teto de AW anual; aguarda YTD do cliente |

## (2) Erros nossos do catálogo (seção 5) que este grupo resolve ou confirma

- **Item 9, CI, HRBS-14996 (GTN acima do teto com valores "apprentice", flag 58216):** **NÃO resolvido, continua aberto.** A API não tem nenhum comentário posterior sobre a banda apprentice, 58216, nem sobre os demais defeitos do GTN (pensão lançada e estornada, rótulos de WT, CE ausente). Os tickets separados prometidos não aparecem. Agora é mais urgente: o flag Stop Tax foi ligado, então o GTN da CI muda de qualquer forma. Próximo passo: abrir ticket(s) dos defeitos do GTN e conferir o design CI v1.1 e o CT-A-620 quanto a 58216.
- **Item 10, NA, HRBS-14605 (lista de relatórios entregue ≠ esperada pelo cliente):** **Parcialmente resolvido.** IT12E/IT14E não existem como obrigação do empregador; PAYE/ETX, PAYE5 e SSC estão esclarecidos; VET Levy existe (folha >= N$1 mi) mas sem relatório nem decisão de escopo. Falta publicar "coberto / não coberto" (ETX, SSC, PAYE5 a escopar, VET Levy decidir).
- **Item 11, NA, HRBS-13602 (CCG × WTC sobre WT 2551 pré-imposto):** **Resolvido, e não era erro nosso.** O CCG está certo (ITA s.17; brochura NamRA); a fórmula citada era da WT 21640. Retirar da seção 5; o rascunho de pesquisa pode ser promovido.
- **Confirma/contradiz outros itens do catálogo fora da seção 5:**
  - F50 (flag sem base legal): 12072 e 12483 confirmam que Pension=Yes é default sem base; 13602 sai da lista (não era flag errado); 13841 sai (rótulo do cliente).
  - F51 (limite/acumulador): 13627 confirma que 1/12 do teto de 1.340 UVT é prática de mercado e o acumulador anual segue sem decisão; 15630 sai (não é defeito de acumulador); 14996/CT-A-620 seguem.
  - F54 (lista de relatórios): 12101, 12111 e 14605 confirmam a causa e mostram o resultado esperado de ter uma lista coberto/não coberto.
  - F57 (payslip): 12472 sem mudança; SR-316 converteu e aprovou.
  - F58 (ciclos especiais): 12487 resolvido por redesenho; 15630 enfraquece o item.
  - F59 (versão apagada): SR-221 confirma; a versão apagada em maio não foi recuperada.
  - Seção 3, item 6: "duplicado 14714 × 14996" é incorreto; "HRBS-14675 passou por 5 pessoas" agora tem dono definido (Configuração).
- **Itens novos a avaliar para a seção 5:** (a) Irlanda, HRBS-13860: defeito do motor para classe PRSI de leavers (45 leavers como J0), sem correção permanente registrada; (b) CI, defeitos do GTN sem ticket (ligado ao item 9); (c) Namíbia: conferir se WT 2551/2550 passaram a teto N$112,50 em 2026-09-01; (d) Colômbia: as cinco regras entraram no CCG/WTC v1.1, mas a implementação para o Instaroll não consta.

## (3) Ainda abertos de verdade

| ID | O que falta | Próximo passo | Dono |
|---|---|---|---|
| HRBS-12110 | Esclarecer o que o solicitante ainda precisa após o parecer "não está pronta" | Perguntar a Daniel; entregar matriz corrigida se for o caso | Wallisson |
| HRBS-14055 | Fechamento/confirmação do solicitante | Pedir confirmação e fechar; cliente remove as linhas da WTC dele | Wallisson / Daniel |
| HRBS-14996 (derivado) | Defeitos do GTN CI (banda apprentice/58216, pensão estornada, rótulos, CE, bases) sem ticket | Abrir ticket(s) de defeito; conferir design CI v1.1 e flag 58216; conferir se o cliente entregou IFPGAZ T1/T2 2026 | Wallisson / Mohit |
| HRBS-13860 (derivado) | Correção permanente do motor (PRSI leavers), validação dos 45 leavers, `payrollRunReference`, AEPN 0%, mapeamento de erros | Confirmar com Romano/INT o estado do fix | Romano / equipe de cálculo e INT |
| HRBS-14605 (derivado) | PAYE 5 a escopar; VET Levy sem decisão; teto SSC N$112,50 em 2026-09-01; configuração dos relatórios | Decidir escopo e registrar coberto/não coberto; conferir WT 2551/2550 | Mohit / Wallisson / Configuração |
| HRBS-13841 (derivado) | WT de solidarité na WTC do Congo (decisão) | Verificar se existe linha própria | Wallisson |
| Colômbia 12487/12491/12492/13627/13692 (derivado) | Implementação no sistema/Instaroll; relatório de consolidação das cesantías sem tratamento; acumulador anual 1.340 UVT | Confirmar com o time de desenvolvimento e acompanhar o PMI Instaroll Transition Tracker | Mohit / Manju |
| SR-221 e SR-232 | Aprovação da BA, itens "Review", due date vencida (2026-07-31) | Ruchi revisa as colunas AD/AE (v1.3/v1.4) | Ruchi Gupta / Wallisson |
| SR-316 | Desenvolvimento do payslip CN; perguntas de contrato, leave balances e IIT não cumulativo | Responder à Lily no ticket | Developer (Michael) / Enaakshi / Lily |
| HRBS-14675 | Consultor do projeto aprovar; Configuração atualizar percentuais; HRBS-14401 | Fora do nosso escopo; registrar em `fronteiras.md` | Configuração (Shaik) / Suresh |
| HRBS-15253 | Call, matriz S/C/M/N, specs por evento Sodra, integração .ffdata, sign-off do CCG 2026 | Marcar a call com Kevin; entregar o que for nosso | Wallisson (Compliance); Configuração/Produto (S/C/M/N) |
| HRBS-15630 | Relatórios YTD OW/AW (58553/58554) dos empregados 2 e 3 | Cliente envia; Compliance confirma e fecha | Cliente (Deepak/Kevin) / Shruti-Wallisson |

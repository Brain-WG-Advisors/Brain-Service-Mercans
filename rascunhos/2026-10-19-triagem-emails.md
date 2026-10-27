# Triagem de e-mails — 2026-10-19

> Janela Gmail. Período: desde 16/10 ~10h até 19/10 ~7h30. Lido pelo Claude in Chrome (só leitura; o conector Gmail pediu novo login). Tickets do YouTrack conferidos pela API (`youtrack_fetch.ps1`, cópia temporária fora de raw/).

## Agir
1. **Costa do Marfim — "Ceiling for Ivory coast"** (Govind, 19/10 03:17; cc Siva, Enaakshi, Yojana, Mohit). Depois da nossa resposta de 16/10 17:06 (teto 70.000 → 75.000 XOF/mês desde 01/01/2023, CT-A-620 reg. 4061, Mohit confirma), o Govind pergunta se algo muda no sistema e **até quando** será atualizado. O prazo é do Mohit (Design/Configuração): a resposta é "sim, muda o teto; prazo com o Mohit". Ticket HRBS-14996 é da Suporte.
2. **EUA — alerta da Usema** (Manju, 19/10 02:57): revisar em **2 dias úteis** (até ~21/10) o alerta "Social Security 2027 Wage Base Rises to $192,300 and COLA Set at 3.6%" e confirmar (o Wallisson é o responsável pelos EUA).
3. **Compliance Calendar** (Manju, 19/10 02:16; encaminha Manish Sharma de 17/10): o Produto entregou o acesso de **produção** (o que for publicado vale para todos os clientes do país). A Manju quer que cada um confirme acesso e teste antes de responder ao Manish. Enaakshi já confirmou (Índia ok); Shruti com erro de SSO (HRBS-16088). **Falta a confirmação do Wallisson.**
4. **Cazaquistão — Internal Certification** (Malika Iskakova, 19/10 04:06): enviou a declaração do 3º trimestre de 2026 (formulário 200) e o comprovante de envio; avisa que trabalham no 1C ZUP, sem lançamentos contábeis. → **frente Certificação**.
5. **Treinamento "AI Usage Awareness Q3 2026"**: o prazo final é **hoje, 19/10, fim do dia** (lembrete final de 16/10). Pessoal.

## Rascunhos criados no Gmail pelo Chrome (19/10 ~8h10, a pedido do usuário; nenhum enviado)
R1 Govind (responder a todos), R2 Manju/Usema (responder a todos: entram também o grupo Compliance Team e Mohsin Khan), R3 Compliance Calendar (com [CHOOSE ONE] para o usuário completar), R4 Malika/Cazaquistão (responder a todos: Malika e Sadaf), R5 Mammoet (só Manju, "Thanks, noted", opcional). Fora: PMI (último é nosso), avisos do YouTrack (Suporte), convites, notas, promoções.
- R4: "Dear Malika, Thank you, the 3Q 2026 declaration (form 200) and the submission receipt are received. Noted that the 1C ZUP database does not include accounting journal entries."
- Para a Certificação: o pacote KZ mistura períodos (G2N/holerites de out/26; declaração do 3º tri/26, jul–set). Falta GL (1C ZUP não tem lançamentos).
- O e-mail "Mercans compliance skills updated to v2.12" (rascunho da Pipeline, criado às 8:03) aparece como enviado às 8:08.

## Revisão do alerta EUA (19/10, depois do R2)
O título no e-mail da Usema era um **link** para a página do alerta: https://mercans.com/resources/statutory-alerts/usa-social-security-2027-wage-base-rises-to-192300-and-cola-set-at-3-6/. O R2 dizia que o e-mail tinha só o título, e isso estava **errado**. Conferência do texto completo:
- Teto OASDI de 2027: $192,300 (2026: $184,500). Aumento de $7,800 (≈4,2%). Vigência a partir de 2027-01-01. Fonte: SSA 2027 COLA Fact Sheet, "Maximum Taxable Earnings" ✅
- COLA 3,6%; benefício médio de aposentado $2,095 → $2,170 (+$75); limite de ganhos abaixo da FRA $24,480 → $25,560. Fonte: Fact Sheet ✅
- Comunicado de imprensa da SSA de 14/10/2026 (quarta-feira) ✅. Os números do teto e dos limites estão na Fact Sheet, não no texto do comunicado.
- Imposto OASDI máximo: 184.500 × 6,2% = 11.439,00 → 192.300 × 6,2% = 11.922,60 (cada parte), combinado 23.845,20, custo extra do empregador 7.800 × 6,2% = 483,60 ✅ (refeito)
- 6,2% OASDI e 1,45% Medicare para cada parte, Medicare sem teto: IRS Topic 751 ✅
- Additional Medicare 0,9%, só do empregado, retido sobre o salário acima de $200,000 no ano civil, sem considerar o estado civil: IRS Topic 560 ✅
- Ações de folha: coerentes com as fontes, nada errado.
Sugestão: em "Published", acrescentar a 2027 COLA Fact Sheet.
- **R2 substituído no Gmail em 19/10 (com ok do usuário):** texto novo = conferência completa acima + sugestão da Fact Sheet + "Approved from my side." O "AHi" e o pedido do texto completo saíram. "Draft saved", não enviado. O texto antigo abaixo fica só como histórico.
- **Reconferência campo a campo (19/10, a pedido do usuário):** alerta, Fact Sheet, press release, IRS 751 e 560 relidos pelo Chrome; contas refeitas. Tudo bate. Observações: a página do alerta já está pública no site (data 19/10/2026); o "Impact" diz "0.9% on wages exceeding $200,000" sem citar que a obrigação do empregado depende do estado civil ($250k casados em conjunto, $125k separados); a retenção pelo empregador começa em $200k em qualquer caso, então a ação de folha está certa.

## Textos dos rascunhos

### R1 — Govind, "Ceiling for Ivory coast" (responder a todos)
> Hi Govind,
>
> Yes. In the backend, the ceiling for Prestations Familiales, Assurance Maternité and AT/MP changes from XOF 70,000 to XOF 75,000/month (CT-A-620, reg. 4061: from XOF 840,000 to XOF 900,000 per year), effective 1 January 2023.
>
> The update is made by the Configuration team; Mohit can confirm the date.
>
> Kind regards,

Fonte: correcoes.md (2026-10-15, CI); nosso e-mail de 16/10 17:06; communiqué CNPS jan/2023 (raw/docs/oficiais/CI/).

### R2 — Manju, "AI-Generated Alerts Are Live – Content Review" (responder a Manju e Usema)
> Hi Manju, Usema,
>
> The figures in the USA alert title are correct: for 2027 the Social Security (OASDI) taxable maximum rises from $184,500 to $192,300, and the COLA is 3.6% (SSA, "2027 Cost-of-Living Adjustment (COLA) Fact Sheet", tables "Maximum Taxable Earnings" and COLA, ssa.gov/news/en/cola/factsheets/2027.html).
>
> Usema, could you share the full text of the alert? The email shows only the title, and I'd like to check the payroll implications before approval.
>
> Kind regards,

Conferido em 19/10 na fact sheet da SSA (lida pelo Chrome): OASDI 2026 $184,500 → 2027 $192,300; COLA 3,6%; alíquota do empregado 7,65% (6,2% OASDI + 1,45% HI) sem mudança.

### R3 — Manju, "Fwd: Compliance Calendar Testing" (responder a todos)
> Hi Manju,
>
> [Confirmed: I have access to the production Compliance Calendar and checked the events for my countries; no issues so far.] / [I don't have access yet: …]
>
> Kind regards,

Depende do teste do próprio Wallisson (não feito por esta janela).

## Esperando outros / já respondido
- **Colômbia — "PMI Review"**: a Heidy respondeu em 16/10 19:58 (lista das 15 rodadas de setembro; F350, resposta da DIAN, arquivo PILA e cesantías não existem do lado da Mercans; WT 21610–21612 = medicina prepagada) e compartilhou 9 planilhas pelo Drive (G2N set/out, Base of Withholding, Formato 2276, 2 liquidações). **O Wallisson já respondeu hoje 00:03** com 21 perguntas abertas e o ponto de escopo (PILA e cesantías são funcionalidade nova: entram no go-live de dezembro?) para Manju e Andy. Aguardando a Heidy/Cinthya e Manju/Andy (Andy volta hoje).
- **YouTrack (frente Suporte):**
  - SR-415 (1-PV trimestral, 19/10 07:44): **a Lily pergunta ao Wallisson** o mapeamento das linhas 38–46 (C_REG, C_RAJ, OBL, RAY, NOMER: campos existentes ou novos; NOMER fixo em 1?). **Pedido a nós.**
  - SR-160 (D1): Michael diz que tudo está resolvido e anexou o template novo (19/10 10:07). Nada para nós.
  - SR-161 (4DF): Michael reverteu R00G01I/R00G02I e decimais (19/10 10:31). Nada para nós.
  - SR-163 (D6): Lily — "testing ok in acceptance" (19/10). Nada para nós.
  - SR-414 (1-PV mensal): último comentário é nosso (v5.3, 16/10). Aguardando a Lily.
  - SR-432 (ES AFI): Drew colocou em acceptance (16/10). Nada para nós.
  - HRBS-14528 (SILTRA .msj): Shyam (16/10) diz que a integração já existe e pede uma call para entender o que apontamos. Decidir se marca a call.

## Só saber
- **Mammoet (Holanda) — auditoria forense** (Manju, FYI, 19/10 02:15): o Marko apontou que a maioria dos valores do XML P10 estava errada. Análise da Manju: FND-01 e FND-02 são a mesma causa — a loonaangifte de P10/P11 puxou valores dos registros de correção em vez do G2N finalizado, deslocando imposto entre P09 e P10; o total anual por empregado bate. Não foi pego porque faltou conciliar declaração × holerite por empregado. Lição útil para a Certificação NL.
- **Notas Gemini "Cross Training – Design Creation"** (16/10): próximos passos do Wallisson — ajustar o design do Chade com o feedback, mandar a descrição do design da Bélgica em inglês e enviar o design revisado para validação. Suman manda o link do formulário de legal entity de teste; prazo do Benjamin: dia 30.
- **Filipinas — PhilHealth** (Usema → Shruti, 16/10): alerta publicado. País da Shruti.
- **Convites**: GSK AU & SG Internal Steerco (atualizado, qua 21/10 07:30–08:00) e Accenture LT & LU Internal SteerCo (mensal, 4ª terça, 06:00–06:30).
- Transcrições Tactiq (Touchpoint, Meeting, Cross Training) e recibo da Anthropic.

## Não lidos — revisão de 19/10 ~13h30 (R2 EUA e Compliance Calendar já enviados pelo usuário)
- **Novo, agir:** Ruchi Gupta (comentário na Google Sheet "K2 Split into Regular and Bonus Income", 19/10 11:28, Canadá). Ela atribuiu um item ao Wallisson: pelo texto (CRA T4127, jan/2026, fórmula C, p. 29–30), um bônus pago sozinho, sem salário regular no mesmo pagamento, não tem a isenção básica de $3.500/P. Pergunta: "não há isenção se só o bônus for pago?". Responder depois de conferir na T4127; não respondido.
- **Convites de hoje:** Mammoet Defects (Yojana, 10:45–15:45) e STG: Spain – ESS Employee Tax Relief Declaration (Nihita, 11:30–12:30). Os dois sem resposta ao convite.
- **Só saber:** HR Blizz "What's New" (Mohsin, 10:42); Trello (vini Sam concluiu "Atualizar/Claude o pipeline"); AI Usage Awareness, lembrete final (Mayur/Neha, 12:09; prazo hoje).
- **YouTrack (API, 19/10):** SR-162 (D5) e HRBS-15216 (DD Ucrânia): nada pendente para nós; o último comentário é nosso ou "testing ok". SR-415 continua com a pergunta da Lily (19/10 07:44) → Suporte.
- O resto dos não lidos (planilhas da Heidy/Cinthya de 15–16/10, convites, promoções) já estava na triagem.

## Ignorar
ChatGPT, Ticketmaster, Apple, Tactiq (pesquisa), Google AI Studio.

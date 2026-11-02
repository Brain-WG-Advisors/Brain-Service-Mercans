# Mensagens ao BAU: fluxo das entregas (rascunho v0.3, 29/10/2026)

> **Não enviado. Quem envia é o usuário.** Substitui a [[mensagens_v0.2]].
> - **Regras (usuário, 29/10):**
>   - só o BAU, sem o Dev;
>   - sem call;
>   - uma mensagem nova por pessoa, sem a Manju e o Marko em cópia.
> - **Canal:** o mesmo que a pessoa usou para mandar os arquivos da certificação (`received.txt` de cada pacote). Gmail ou Chat, rascunho pela janela da frente correspondente.
> - **Contatos:** board BAU Master no monday, lido em 29/10 (`dados/monday_12paises.md`).
> - **Base:**
>   - weekly 27/10, 12:15: "That is what you can take from BAU team";
>   - call com o Vinícius, 27/10, 1:03:39–1:05:19: board BAU Master, perguntas simples e diretas.

## 1. Umesh Gaikwad: Noruega e Holanda
> Hi Umesh, we're mapping how each payroll filing reaches the authority today, so we can plan what still needs to be automated. Two quick questions:
>
> *(29/10: frase trocada a pedido do usuário. O e-mail leva o Marko e a Manju em Cc, então "for a plan Marko asked for" sai, e o mesmo vale para as outras 6 mensagens.)*
>
> 1. Norway: is the a-melding sent straight from HR Blizz, or exported as an XML file and uploaded on skatteetaten.no? Whose login is used? And who sends the inntektsmelding to NAV when an employee is on sick or parental leave?
> 2. Netherlands: is the loonaangifte sent from HR Blizz through Digipoort, or does someone upload or send it another way?
>
> Is there any other filing to a government body for these two countries that I haven't mentioned? A short answer is fine. Could you reply by Wednesday 4 November?
>
> Thanks!

## 2. Marju Martinson: Estônia e Finlândia
> Hi Marju, I'm mapping how each payroll filing reaches the authority today, for a plan Marko asked for.
>
> 1. Estonia: how is the TSD filed today? Since 1 October the annex 1 and 2 data has to go in the new data-based format, so I'd like to check the October TSD (due 10 November) is on track.
> 2. Finland: is the earnings payment report sent to the Incomes Register from HR Blizz, or uploaded by someone? And the employer's separate report?
>
> Is there any other filing to a government body for Estonia or Finland that I haven't mentioned? A short answer is fine. Could you reply by Monday 3 November, given the Estonian deadline?
>
> Thanks!

## 3. Deepak Prakash Pardeshi: Dinamarca
> Hi Deepak, I'm mapping how each payroll filing reaches the authority today, for a plan Marko asked for. For Denmark, is eIndkomst sent from HR Blizz system-to-system, or uploaded on skat.dk? Whose access is used?
>
> Is there any other filing to a government body for Denmark that I haven't mentioned? A short answer is fine. Could you reply by Wednesday 4 November?
>
> Thanks!

## 4. Athul S: Suécia
> Hi Athul, I'm mapping how each payroll filing reaches the authority today, for a plan Marko asked for. For Sweden, is the AGI loaded from HR Blizz through the Skatteverket API, or uploaded as a file? And who signs it on Mina sidor, the client or Mercans?
>
> Is there any other filing to a government body for Sweden that I haven't mentioned? A short answer is fine. Could you reply by Wednesday 4 November?
>
> Thanks!

## 5. Srikanth Kondam: Reino Unido
> Hi Srikanth, I'm mapping how each payroll filing reaches the authority today, for a plan Marko asked for. For the UK, are the FPS and EPS submitted directly from HR Blizz, or does someone upload them? Is Mercans set up as an agent with HMRC for any client, or is it always the employer's own Government Gateway?
>
> Is there any other filing to a government body for the UK that I haven't mentioned, such as P11D? A short answer is fine. Could you reply by Wednesday 4 November?
>
> Thanks!

## 6. Nataliia Hahan: Ucrânia
> Hi Nataliia, I'm mapping how each payroll filing reaches the authority today, for a plan Marko asked for. For Ukraine, who files the unified report (J0500111) and the 1-PV: the external payroll provider, the client or Mercans? Through which channel, and with whose digital signature?
>
> Is there any other filing to a government body for Ukraine that I haven't mentioned? A short answer is fine. Could you reply by Wednesday 4 November?
>
> Thanks!

## 7. Sadaf Nishat: Cazaquistão, Azerbaijão e Rússia
> Hi Sadaf, I'm mapping how each payroll filing reaches the authority today, for a plan Marko asked for. For Kazakhstan, Azerbaijan and Russia, who prepares and files the payroll returns: the external payroll provider, the client or Mercans? Through which portal or operator?
>
> Could you also list the filings for each country? I have form 200.00 for Kazakhstan, and 6-NDFL, RSV and EFS-1 for Russia, but nothing yet for Azerbaijan. A short answer is fine. Could you reply by Wednesday 4 November?
>
> Thanks!

## Irlanda: sem mensagem
Não há SBC no board. Os 5 clientes são SaaS, e o ticket HRBS-13860 mostra o HR Blizz enviando direto ao ROS. Fica registrado como "a confirmar" no documento do país.

## Bloco de prova
- **Destinatários:** monday 2072701698, lido em 29/10, Primary SBC com mais clientes ativos por país (`dados/monday_12paises.md`, tabela 1). A Dinamarca mudou de Rakshitha para Deepak.
- **Fatos citados nas perguntas:**
  - Estônia: e-MTA, "1. oktoobrist 2026 muutus TSD … andmepõhiseks" e prazo "järgneva kuu 10. kuupäevaks" (`raw/docs/oficiais/EE/2026-10-29-canal/`).
  - Noruega: o upload no portal existe (C7) e a inntektsmelding vai pelo portal da NAV (C8).
  - Reino Unido: a credencial do empregador aparece no envelope do FPS/EPS (UK F-01).
  - Ucrânia, Cazaquistão, Azerbaijão e Rússia: "External Supplier" no monday.
- **Tom:** a mesma abertura em todas, uma pergunta por país, sem códigos nem referências de fonte (orientação da call de 27/10, 1:05:04).
- **Confiança 95%:** falta só conferir o canal de cada pessoa (Chat ou e-mail) no `received.txt` antes do rascunho.

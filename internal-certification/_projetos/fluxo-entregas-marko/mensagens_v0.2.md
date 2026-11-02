# Mensagens: fluxo das entregas (rascunho v0.2, 29/10/2026)

> **Não enviado. Quem envia é o usuário.** Substitui a [[mensagens_BAU_v0.1]]. Linha de base: [[TAP_fluxo_entregas]] (WP4).
> **Contatos:** `dados/monday_12paises.md` (board BAU Master, lido em 29/10) e `dados/evidencia_hoje_e_dev.md` (Dev).
> **Regra:** perguntar só o que a fonte e a evidência não respondem. Cada pergunta já leva o que sabemos.

## 1. Dev: Illya Virchenko (Integration / Config Factory). **Enviar primeiro.**
Por que ele: o `fronteiras.md` o registra como dono das integrações; o HRBS-13860 mostra o "Irish Tax Payroll Submission" como Outbound Config com o passo `Submit_Report`.

> Hi Illya, quick question for a filing map Marko asked for.
>
> I can see HR Blizz submits Irish payroll directly through the "Irish Tax Payroll Submission" outbound config. Is there an equivalent outbound config that submits to the authority for Norway (a-melding), Estonia (TSD), the Netherlands (loonaangifte), the UK (FPS/EPS), Denmark (eIndkomst), Sweden (AGI) and Finland (Incomes Register)? Or does HR Blizz only produce the file in those countries?
>
> Two of them have deadlines coming up:
> - Norway: from 17 November the a-melding can no longer be sent with the old Altinn roles. Does our submission use a system user with the new access packages?
> - Estonia: since 1 October, TSD annex 1 and 2 can't be sent as XML any more (X-tee data or CSV only). The October TSD is due on 10 November. Is HR Blizz ready for it?
>
> Thanks!

## 2. BAU: uma mensagem por pessoa

Texto-base:

> Hi [name], we're mapping how each payroll filing reaches the authority today, for a plan Marko asked for. For [country], could you tell me:
> 1. [pergunta do país]
> 2. Is there any other filing to a government body for [country] that isn't listed here: [lista]?
>
> A short answer is enough. Could you reply by Wednesday 4 November?

| # | Para | País | Pergunta 1 (só o que falta) | [lista] |
|---|---|---|---|---|
| 1 | Umesh Gaikwad | NO, NL | **NO:** Is the a-melding sent straight from HR Blizz, or exported as XML and uploaded on skatteetaten.no? Under whose login? And who sends the inntektsmelding to NAV? **NL:** Is the loonaangifte sent from HR Blizz through Digipoort, or uploaded/sent by someone else? We have no Digipoort receipt for the September returns. | NO: a-melding, inntektsmelding (NAV). NL: aangifte loonheffingen |
| 2 | Marju Martinson | EE, FI | **EE (urgent):** How is the TSD filed today, and is the October one (due 10 Nov) ready in the new data format? **FI:** Is the earnings payment report sent to the Incomes Register from HR Blizz, or uploaded by someone? | EE: TSD, TÖR. FI: earnings payment report, employer's separate report |
| 3 | Deepak Prakash Pardeshi | DK | Is eIndkomst sent from HR Blizz (system-to-system) or uploaded on skat.dk? Under whose access? | eIndkomst |
| 4 | Athul S | SE | Is the AGI loaded from HR Blizz through the Skatteverket API, or uploaded as a file? Who signs it on Mina sidor (client or Mercans as ombud)? | Arbetsgivardeklaration (AGI) |
| 5 | Srikanth Kondam | UK | The FPS/EPS files carry the employer's Government Gateway credentials. Does HR Blizz submit them directly, or does someone upload them? Is Mercans set up as an agent for any client? | FPS, EPS, P11D |
| 6 | Nataliia Hahan | UA | Payroll runs with an external supplier. Who files the J0500111 and 1-PV, through which channel, and with whose КЕП? | J0500111, 1-PV |
| 7 | Sadaf Nishat | KZ, AZ, RU | For each country: who prepares and files the payroll returns (the external supplier, the client or Mercans), and through which portal or operator? | KZ: 200.00. RU: 6-НДФЛ, РСВ, ЕФС-1. AZ: (please list) |
| — | Irlanda | IE | Sem pergunta ao BAU: o monday não tem contato, os clientes são SaaS e o ticket mostra o HR Blizz transmitindo. A resposta do Illya fecha. | — |

## Bloco de prova
- **Contatos:** monday 2072701698, lido em 29/10 (`dados/monday_12paises.md`, tabela 1). A Dinamarca mudou de Rakshitha para Deepak.
- **Fatos usados nas perguntas:**
  - Irlanda: HRBS-13860 (Outbound Config "Irish Tax Payroll Submission", step `Submit_Report_ErrorBrake`).
  - Noruega: C6 "Fra 17. november…" (`raw/docs/oficiais/NO/2026-10-29-canal/nye_tilgangspakker_amelding.html`).
  - Estônia: "1. oktoobrist 2026 muutus TSD… andmepõhiseks" e "ei ole võimalik… XML-kujul" (`raw/docs/oficiais/EE/2026-10-29-canal/emta_tsd_*.txt`); prazo: "deklaratsioon tuleb esitada väljamaksetele või kulude tegemisele järgneva kuu 10. kuupäevaks", ou seja, até o dia 10 do mês seguinte ao pagamento; para outubro, 10/11 (conferido em 29/10).
  - Reino Unido: UK F-01 (credenciais no envelope).
  - Ucrânia, Cazaquistão, Azerbaijão e Rússia: "External Supplier" no monday.
- **Confiança 95%:** falta só a leitura dos SOPs por cliente (Google Docs), que pode mudar a pergunta 1 de algum país.

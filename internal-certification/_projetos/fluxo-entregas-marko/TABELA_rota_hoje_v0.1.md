# Tabela do relatório: como cada declaração chega hoje ao governo (v0.1, 03/11/2026)

> **Rascunho interno, não enviado.** É a tabela pedida pela Manju na weekly de 03/11 (10:24–11:43 e 15:40–18:26): uma linha por declaração e por país, mostrando se o envio é automático, se está conforme e por quê.
> - Insumos: certificação (pacotes de set/26 e Audit Reports), SOPs do Customer Success, respostas do BAU, tickets e o monday.
> - Respostas do BAU pendentes até 05/11 (Srikanth até 09/11). Ligada a [[TAP_fluxo_entregas]], [[PADRAO_email_SBC]] e [[paises/NO_fluxo_entregas]].
> - **Legenda:**
>   - "Automático?": **Sim** = o HR Blizz transmite sozinho à autoridade; **Não** = alguém sobe, digita ou corrige; **?** = sem prova ainda.
>   - "Conforme?": o que a certificação conseguiu provar do envio de set/26.

| País | Declaração | Como é hoje (com prova) | Automático? | Conforme? | Por quê / prova | O que falta |
|---|---|---|---|---|---|---|
| NO | a-melding (mensal) | O HR Blizz gera o XML. O Umesh: "We currently upload the XML file manually via the Altinn portal". O SOP do Customer Success (§5.5) diz o contrário: "exclusively via the HR Blizz outbound integration channel". | **Não** (conflito) | Sim (set/26) | O recibo de set/26 traz `kildesistema HR Blizz`, `mottatt`, sem desvios (pacote Henkel). Umesh, e-mail 30/10. SOP v0_1, 03/11. | Quem sobe e com qual login: risco de 17/11 (cortam os papéis antigos do Altinn). E-mail de 03/11. |
| NO | inntektsmelding à NAV (por evento) | Não visto no pacote. | ? | — | `NO_fluxo_entregas.md`, linha 30. | Quem envia: perguntado em 30/10 e 03/11. |
| DK | eIndkomst (mensal) | O arquivo do pacote **não é o que a SKAT recebeu**: a rescisão está no campo 0013 e não há campo 0069; a SKAT recebeu 0069 = 571.251. | **Não** (indício de alteração fora do sistema) | Parcial | `DK_SherwinWilliams_2026-09_Validation.xlsx`, Findings Register, F-02; Audit Report de 16/10, RF-01. | O arquivo que de fato foi enviado e quem enviou. E-mail ao Deepak, 03/11. |
| NL | loonaangifte (mensal, Digipoort) | O Umesh: tudo pelo HR Blizz. Mas o recibo do pacote Sherwin é de **outro número de folha** (868240503L01). O Suresh (Chat, 03/11) **não consegue** o recibo do Digipoort da Excerpta nem a declaração de agosto como enviada. | **?** (o BAU não tem o recibo) | **Não provado** | `NL_SherwinWilliams_2026-09_Audit_Report.docx`, RF-01 (F-01 High). Chat do Suresh, 03/11 9:55. Ticket HRBS-15179: XML rejeitado no portal, validação no VTS (`dados/evidencia_hoje_e_dev.md`, linha 12). | Quem transmite e onde fica o recibo: e-mails ao Umesh e ao Suresh. |
| NL | referência de pagamento | "Currently we are updating tax reference number manually" | **Não** | — | HRBS-9646, linha 34 (`evidencia_hoje_e_dev.md`, linha 13). | Automatizar no produto. |
| SE | arbetsgivardeklaration (mensal) | O SOP do Customer Success (§5.5): "done exclusively through this outbound integration — the declaration is not keyed in or file-uploaded manually"; API da Skatteverket (scope agd), status DONE_SUCCESS. O ICE revisa **depois** do envio (§5.6). A Manju, na weekly: o ICE completa o XML no portal e envia. | **Sim** pelo SOP; **?** pela weekly | Pass (One Identity set/26) | SOP SE V1, Doc 1Dww…Vfc8. Weekly 03/11, 16:32. | Qual dos dois vale: e-mail ao Athul, 03/11. |
| UK | FPS / EPS (RTI) | Os ACKs do HMRC de outubro chegaram (C-09). Ticket HRBS-16010: "whether the FPS has been submitted" (set e out). | Provável sim | Parcial (McDermott) | Certificação UK (C-09); `evidencia_hoje_e_dev.md`, linhas 15–18. | Login (Government Gateway do cliente ou Mercans como agente): e-mail ao Srikanth, prazo 09/11. |
| IE | PSR (ROS) e NAERSA | Conexão direta ao ROS com certificado digital; NAERSA com `softwareUsed=HRBlizz`, `fileAcknowledged=true`. O envio é acionado pelo suporte a pedido do cliente. | **Sim** | — (sem pacote) | CT-4078, linhas 65–74; HRBS-13860, linhas 56–57 e 184. | Sem SBC no board: confirmar o contato. |
| EE | TSD (mensal) | Desde 01/10 a TSD não aceita mais o XML antigo nos anexos 1 e 2 (XBRL GL; CSV até 2027). O vencimento é no dia 10. | ? | — (sem pacote) | e-MTA (`raw/docs/oficiais/EE/2026-10-29-canal/`). | A TSD de outubro (vence 10/11) está no formato novo? E-mail à Marju, que responde até 05/11. |
| FI | Incomes Register | HR Blizz (5 clientes, monday). | ? | — (sem pacote) | `dados/monday_12paises.md`, linha 17. | E-mail à Marju. |
| KZ | 200.00 (KGD) | A folha roda no 1C ZUP local, **fora do HR Blizz**; o 200.00 é entregue pelo portal da KGD. | **Não** | Parcial (Mastercard out/26) | Pacote KZ (`frentes/certificacao/estado.md`, linha 98). | Quem envia e com qual assinatura (ЭЦП): e-mail à Malika. |
| UA | relatórios mensais (Altium) | Fornecedor externo (6/6 clientes, "External Supplier"). | **Não** (terceiro) | Parcial (ago e set/26) | `dados/monday_12paises.md`, linha 16; Audit Reports UA. | Quem envia e com qual assinatura (KEP): e-mail à Nataliia. |
| AZ | relatórios mensais (Mastercard) | Fornecedor externo ("External Supplier"). | **Não** (terceiro) | Parcial (set/26, v1.1) | `dados/monday_12paises.md`, linha 21; validação AZ v1.1. | E-mail à Pari. Fora do tracker da Manju (61 países). |
| RU | relatórios mensais | Fornecedor externo; ICE Olga Fomicheva. | **Não** (terceiro) | — (sem pacote) | `dados/monday_12paises.md`, linha 22; e-mail da Sadaf, 03/11. | Falar com a Olga (pedido de 09/10 ficou em rascunho). Fora do tracker. |

## O que já dá para dizer (para a Manju e o Marko)
- **Passo manual com prova:** NO (upload no Altinn), DK (arquivo enviado ≠ arquivo do sistema), NL (referência de pagamento digitada) e KZ (folha fora do HR Blizz).
- **Terceiro no meio:** UA, AZ e RU (fornecedor externo ou ICE). São os casos que o Marko quer eliminar antes de janeiro.
- **Automático com prova:** IE (ROS e NAERSA direto do HR Blizz).
- **SOP × prática:** os SOPs de NO e SE dizem "só pela integração". As evidências da NO e a fala da Manju sobre a SE não confirmam.
- **O BAU não tem o recibo do envio na NL:** sinal de que o envio não está sob controle do BAU.

## Bloco de prova
- **Pedido → resposta:** a tabela da weekly de 03/11 (colunas: API sim/não, conforme sim/não, por quê). Uma linha por declaração principal dos 12 países. Mais declarações entram com as respostas de 05/11.
- **Fontes:** cada linha cita arquivo e linha, aba e item, ou mensagem com data. Os trechos entre aspas foram lidos nesta sessão: SOPs NO e SE pelo Chrome; Chat do Suresh; e-mail do Umesh (`log.md`, 30/10); Audit Reports NL e DK (`python-docx`, 02–03/11).
- **Teste:** nenhuma conta refeita; é tabela de evidência.
- **Confiança:** 90%.
  - UK "provável sim" depende do login (Srikanth).
  - FI e EE sem evidência de envio.
  - UA, AZ e RU "terceiro" vêm do monday ("External Supplier"), sem o detalhe de quem transmite.
  - Não apresentar como final antes das respostas de 05/11.

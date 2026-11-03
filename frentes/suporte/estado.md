# Estado — Frente 1: Suporte (YouTrack)

> Escrito **só pela janela "Suporte - Mercans"**. Atualizado em 2026-10-28 (fim do dia). Sessão: [[sessoes/2026-10-28-suporte]]. Textos: `rascunhos/2026-10-28-youtrack-drafts/`.

## Instruções vigentes
- 28/10: cada ticket fica com o seu dono. O que é nosso fica atribuído a wgomes; o que é de outra pessoa vai para ela (Holiday Pay DK → Enaakshi; tickets da Shruti → skamble).
- 28/10: antes de reatribuir, reler Assignee, Support Group e activity na API; depois, conferir que gravou.
- 28/10: os 10 da Shruti (SR-105 a 110, HRBS-3466, 15941, 16029, 15790) voltaram para skamble; o trabalho local fica em `rascunhos/2026-10-23-shruti/`, pronto para quando a Manju pedir.
- Ok de outra janela não vale para gravar aqui: pedir ao usuário nesta janela.
- Ao regravar rascunho que o usuário vai publicar: pedir para recarregar a página do ticket antes.
- 03/11: HRBS-16407 em espera até o transcript da reunião de hoje com a STG/cliente. Não trocar nem publicar o draft da v1.8 antes; texto corrigido pronto (excesso "above the amount exempt under LGSS art. 147.2.c", 12 meses antes do mês do desligamento). Com o transcript: ingerir (raw/reunioes/) e fechar a resposta.

## Tickets atribuídos (`for: me #Unresolved`, 28/10 19:30 UTC)
| Ticket | País | Estado | Próximo passo |
|---|---|---|---|
| HRBS-13704 | Reino Unido (STG, Implementation) | Pending on reporter. Publicado 19:21 + complemento 19:25 UTC (campos Seconded/EEA/EPM6 + código de imposto) | Aguardar o skondam |
| HRBS-16010 | Reino Unido (McDermott, Live) | Pending on Internal team. Publicado 18:04 UTC (PGL1 sem PlanType; regra do Mohit) | Aguardar o Josh; avisar a Manju em 1 linha |
| HRBS-16418 | Tunísia (Henkel) | In Progress, nosso. 02/11: asaber cobra resposta (10 dias). Pergunta: mínimo de 45% do Art. 12 bis Lei 89-114 se aplica? rfusana já mostrou que o design tn_2026 não aplica (Reg 259/260). 02/11: draft gravado com ok (806 car., IGUAL; `HRBS-16418.md`): regra vale p/ deduções "sous réserve" 12 bis (39-I-2, 39-VIII, 39 bis); fontes em raw/docs/oficiais/TN/ 02/11: publicado por mim com ordem do usuário ("Pode enviar!"), versão objetiva 573 car., IGUAL, id 4-205738. 03/11: Ahmed (chat) não entendeu como se aplica → draft passo a passo gravado com ok (534 car., IGUAL; `HRBS-16418-passo-a-passo.md`); publicado pelo usuário 12:00 UTC (4-206003, IGUAL) e chat ao Ahmed enviado | Aguardar Ahmed/Mohit |
| HRBS-16649 | Namíbia (Baker Hughes, UAT) | Open, nosso (Daniel). Confirmar método PAYE (anualização + true-up YTD), zero-pay, admissão no meio do ano, RSU, bônus. 02/11: draft trocado com ok pela versão curta (448 car., IGUAL; `HRBS-16649.md`): Q6 TIN = alíquota máxima (Sch.2 §12(2)); Q1–5 dependem das tabelas NamRA (§9(1)) → pede ao Daniel as tabelas que ele usou. Versão longa descartada (não respondia Q1–5) | Usuário publica; com as tabelas, responder Q1–5; testar namra.org.na a cada abertura |
| HRBS-15253 | Lituânia (Accenture) | Pending on Internal team. Publicado 03:20 UTC (retorno da call) | Aguardar o Kevin |

## Fora da fila, acompanhar
| Ticket | País | Situação |
|---|---|---|
| HRBS-16407 | Espanha (STG, Live; desde 02/11 assignee wgomes) | 02/11: publicado 14:36 UTC (518 car., IGUAL ao draft): limite do seguro p/ admitidos/desligados sem rateio (Lily) + 400,05 = provisão das extras (Nihita); Nihita confirmou 14:48. Antiguidade: Lily → 64556 na entidade (Vaishnavi incluiu a fórmula). Histórico: | 29/10: resposta aos 4 comentários publicada (3.054 car.). CCG v1.7 no Drive (Google Doc 1kkDXufX…) + monday; link da v1.7 + pergunta à Lily publicados 13:34 UTC (302 car.; usuário tirou "and who should it go to?"; "Developmen" corrigido para "Development", conferido na API, 303 car.). 30/10: draft com o resumo do chat (extras 58140/64993 só STG = Configuration; seguro 41,67 mensal = escolha da STG, anexar confirmação escrita) gravado com ok, 731 car., IGUAL, não publicado (`HRBS-16407-chat-30-10.md`). Aguardar a Lily → ticket ao Dev (rascunho `ticket-dev.md`); convenio da STG → WTC V4.8 só se incluir antiguidade. E-mails à Lily (509/701) enviados pelo usuário (janela Gmail, 29/10). Hub [[Espanha]] |
| HRBS-16487 | Holanda | Resolved pelo Mohit em 02/11 (feature exige research & development; informar o cliente) |
| HRBS-14394 | Holanda | Pedido ao Mohit em 27/10; aguardando |
| HRBS-16573 | Dinamarca | Com Asad Ansari (Configuration); não é nosso. Análise arquivada em `rascunhos/2026-10-28-tickets-novos/` |
| SR-414, SR-415, SR-160, HRBS-12110 | Ucrânia/Congo | Enviados em 16–20/10; aguardando Lily/Daniel |
| HRBS-14528, SR-163 | Espanha/Ucrânia | Rascunhos de 16/10 gravados, não enviados (usuário) |

# Lei × mercado (benchmark de prática de payroll)

> Ligada a: [[suporte]] · [[research-pipeline]] · [[correcoes]] · [[fronteiras]] · caso de origem: [[Espanha]] (HRBS-16407, STG)
> Criada em 2026-11-03 a partir das calls STG de 02/11 e 03/11.

## Por que existe
A lei fixa o **resultado** (limite, alíquota, prazo). Ela quase nunca fixa o **mecanismo** da folha (como aplicar mês a mês). O mercado de payroll (softwares, assessorias, convenios) escolhe um mecanismo, e quase sempre o **mais seguro para o empregador**. Responder só com a lei, quando a pergunta é de mecanismo, faz a resposta parecer "contra o mercado" e trava o cliente (caso STG: chamamos de "fora da lei" algo que provavelmente é aplicação conservadora dentro da lei).

## As 3 camadas (toda pergunta estatutária de cliente/BAU)
| Camada | Pergunta | Fonte | Nível |
|---|---|---|---|
| 1. Lei | Qual é o limite/obrigação e em que período ele se mede (mês, ano, por pagador, por pessoa)? | Lei, regulamento, consulta oficial (ex.: DGT) | A (primária) |
| 2. Mercado | Como os softwares e assessorias aplicam na folha? | Manual/blog de software de folha, assessoria, convenio, o próprio cliente | B/C — **sempre marcado como prática, nunca como lei** |
| 3. Teste | A prática pode dar resultado **além** da lei? | Conta com casos: ano cheio, admissão/saída no meio do ano, dois empregadores, valor alto | Conta refeita |

**Veredito pela camada 3:**
- **Dentro da lei (mais conservadora):** a prática nunca isenta mais / nunca recolhe menos do que a lei manda; o máximo que acontece é recolher antes ou a mais, recuperável no ajuste anual. → "Pode; é escolha de configuração. Efeito: …" (dizer quem paga a diferença e como recupera).
- **Além da lei:** a prática dá ao empregado mais do que a lei permite ou recolhe menos. → "Não pode" ou CR com aprovação do cliente ([[fronteiras]]; memória `pedido-fora-da-lei-cr`).
- **Sempre dizer o efeito no reporte anual** (ex.: Modelo 190), porque é onde a diferença aparece.

## Como redigir
"A lei fixa X (fonte). Na prática, as folhas aplicam Y. Y fica dentro da lei porque nunca passa de X; o efeito é Z para quem entra ou sai no meio do ano." Uma frase por camada; nunca apresentar prática de mercado como regra legal.

## Casos registrados
| Data | País / tema | Lei (camada 1) | Mercado (camada 2) | Teste (camada 3) | Situação |
|---|---|---|---|---|---|
| 2026-11-03 | [[Espanha]] / seguro-saúde (65630), STG, HRBS-16407 | €500/ano por pessoa coberta (€1.500 com deficiência), sem rateio para quem trabalha parte do ano (LIRPF art. 42.3.c; DGT V1967-17) | Limite dividido em 12 (41,67/mês isento), excesso tributado no mês, ajuste no fim do ano ("prorate at the end"); motivo: não depende de saber se o empregado usou a isenção noutro empregador (Gemma, STG, call 03/11 10:21–12:37; resumo de IA citando Seguros Zaragoza no chat 03/11; Cobee/PayFit na busca 03/11, não abertos) — nível B/C | Ano cheio: mesmo resultado. Admissão/saída no meio do ano: isenta menos na folha → empregado paga mais durante o ano e recupera na declaração (ou no ajuste de fim de ano, se o sistema fizer); nunca passa de €500 → **dentro da lei**. No Modelo 190 muda só a divisão entre isento (Clave L, subclave 24) e tributável (Clave A) (AEAT DR 190) | Respostas à Nihita enviadas em 03/11 (efeito em quem trabalha parte do ano; sem reporte extra). Abertos: (a) dois empregadores no mesmo ano — o limite é por pessoa ou por pagador? achar consulta DGT com número; (b) o motor faz o ajuste de fim de ano/saída? (Lily). Precedente nosso: HRBS-11310 (04/07/2026) validou 41,67 mensal isento |

## Fontes de mercado aceitas como camada 2
Manuais e blogs de softwares de folha (A3, Sage, PayFit, Cobee, Meta4), assessorias e escritórios, convenios coletivos, o cliente. Registrar o link e a data; abrir a página antes de citar.

# O que o Marko quer: o caminho de cada entrega ao governo, do sistema até a autoridade (2026-10-28)

> Montado a partir de 5 reuniões, lidas na íntegra em 28/10. Estado: [[ESTADO]] · Frente: [[rotinas]] (Certificação) · Sessão: [[sessoes/2026-10-28]].
> Fontes: [[raw/reunioes/2026-10-27-research-team-weekly.txt|weekly 27/10]] (Manju) · [[raw/reunioes/2026-10-27-call-wallisson-lituania-espanha.txt|call com o Vinícius 27/10]] · [[raw/reunioes/2026-10-07-research-team-weekly.txt|weekly 07/10]] · [[raw/reunioes/2026-10-09-call-manju-wallisson.txt|call com a Manju 09/10]] · [[raw/chats/2026-10-21-research-team-biweekly-marko-transcript.txt|bi-weekly 21/10]] (o Marko presente) · [[raw/reunioes/2026-10-27-spain-transition-to-HRB.txt|Espanha 27/10]] (o Marko presente).

## 1. O pedido em uma frase
Para cada país que está em produção, o Marko quer saber como cada entrega ao governo é feita hoje e como deveria ser feita. O objetivo é que toda entrega saia do sistema da Mercans e chegue à autoridade de forma automática, sem ninguém digitar à mão e sem terceiro. Assim a Mercans evita multa e surpresa.

> Manju, 27/10 13:08: o foco dele é que "whatever filings we are making, that is coming from our system and those are filed with the in automation process without any manual intervention, without any third party intervening".

## 2. Por que não é "só report"
| Até agora (o que já fazemos) | O que o Marko pede a mais |
|---|---|
| A pesquisa diz **qual** report vai ao governo, os requisitos e a spec, campo a campo. | O **passo a passo da entrega**: o que o sistema faz, o que o cliente faz, o que a autoridade faz. Cobre registro, assinatura, canal (portal, XML, API) e prazo (Manju 27/10 04:44 e 10:41). |
| A certificação interna valida se a spec e o arquivo final estão certos (07/10). | O **como**: o sistema gerou ou o time fez à mão? Usa portal? Corrige com o Claude antes de mandar? Tem terceiro? (você ao Vinícius, 27/10 01:00:12 a 01:02:46). |
| Olha só a nossa parte (a pesquisa vai para o Development e a Config). | O fluxo **entre todos os times**, até a entrega final: Development → Config → implementação → BAU/payroll → governo. A parte de compliance é a menos importante para ele (27/10 01:03:03). |
| Tax e social security. | **Toda** entrega de payroll ao governo: na Colômbia, por exemplo, também pensão e sindicato (Manju 09/10 02:18). |

> Manju, 27/10 10:08, quando você descreveu a validação de specs: "that is different than what I'm asking now".

## 3. O modelo: o que a Manju fez para o Vietnã (e o Taiwan)
Mostrado na tela em 27/10, de 10:16 a 11:30:
- **Hoje (Vietnã):** tudo é feito à mão por um terceiro ("ice"). O time pega o gross-to-net, entra no portal da autoridade (HTK), digita os dados, gera o XML no portal e envia.
- **Como deve ser:** a Mercans se registra na autoridade como agente (no Taiwan há essa categoria). O sistema gera o XML, o cliente autoriza e assina, e a Mercans transmite pelo próprio registro.
- **O que for necessariamente manual:** documentar passo a passo.
- **O resultado:** a lista do que falta no sistema para chegar lá. Isso vira desenvolvimento.

## 4. O que entregar, por país
1. **Lista de entregas ao governo**: report, autoridade, frequência e prazo. Sai da pesquisa e dos artefatos (CCG, specs, SIR).
2. **Como deveria ser**: o canal oficial (API, XML, portal), o registro e a assinatura exigidos e o que o sistema precisa ter. Isso é pesquisa nossa, com fonte oficial.
3. **Como é hoje**: perguntado ao BAU do país. Serve só para entender; o manual não é base (Manju 27/10 12:21). Perguntas diretas e simples (27/10 01:04:28 a 01:05:04):
   - o sistema gera o arquivo, ou vocês fazem à mão?
   - por qual canal enviam?
   - corrigem algo antes de enviar? O quê e com quê?
   - há terceiro envolvido?
4. **Diferença e plano**: o que falta no sistema, quem resolve (Development, Config ou registro na autoridade) e a prioridade.
5. **Validação dos arquivos finais** que o BAU já mandou (XML, PDF), no que for possível. Já existe parte disso na certificação (07/10).

## 5. O que entregar ao Marko
- **Primeiro:** um plano com o status, o que já foi feito, o que está em andamento e a data de fim por país (Manju 27/10 13:08 e 13:59).
- **No fim:** um relatório para ler de relance, com um gráfico por país: o que é gerado pelo sistema, o que é manual e o que falta (você ao Vinícius, 27/10 01:05:26).
- **Ordem:**
  - começar pela **Europa** (27/10 05:42); as listas do BAU master são de 9 a 10 países por pessoa (27/10 06:11);
  - antes de prometer datas, medir o tempo com **um país** (07/10, "Single country timing evaluation").

## 6. Quem faz e onde está
- **O Vinícius executa.** Você passou a tarefa a ele em 27/10 como secundária, depois de Lituânia e Espanha. O Samuel ajuda nas automações. Contatos do BAU: board "BAU master clients".
- **A Manju faz o mesmo nos países dela e nos da Shruti** (27/10 13:59).
- Até 28/10 não há registro de que tenha começado.

## 7. Outros pedidos do Marko (não confundir, mas andam juntos)
| Pedido | Origem | Situação |
|---|---|---|
| **Certificação interna das specs da Europa** (spec certa? report final certo?) e validação externa com software de terceiro. Motivo: o QCRM viu reports errados sendo corrigidos à mão com o Claude antes do envio. | weekly 07/10 | Em andamento: frente Certificação. |
| **Compliance calendar**: conferir e publicar no ambiente de produção os eventos de cada país (pagamentos, entregas, feriados), cerca de 60 países, 1 a 2 por semana, primeiro os que têm cliente ativo. Ferramenta do Manish (VPN). | 09/10 e 27/10 00:11 | Falta o plano com datas para o Marko. |
| **Trabalhar com o BAU** para entender como ele calcula e reporta, e capturar esse conhecimento (Colômbia: pensão e sindicato). | 09/10 01:00 | Colômbia fechada em 26/10. |
| **Plano do projeto de automação** (tickets → redline, alertas), com percentual e data. | 21/10 e 27/10 16:16 | Status enviado em 28/10 (cerca de 60%). Falta o plano com datas. |
| **QA independente na pesquisa**: um segundo agente revalida a pesquisa, mais validação de terceiros e offline. | 21/10 00:28 | Faz parte do método do pipeline. |
| **Base de conhecimento de compliance no novo suporte com IA**, que vai substituir o YouTrack para o cliente: falar com o time Arbites (Chris). | 21/10 00:33 | Sem registro de que tenha começado. |
| **Roteiro de pesquisa**: fechar a Europa Ocidental (Itália antes da Grécia; Alemanha, Suíça, França) e montar com a Yoyo o roteiro de 2027 (Japão, América do Sul). Nos EUA: multiestado e filing por provedor terceiro. | 21/10 00:12–00:21 | Com a Manju. |
| **Auditoria do ano inteiro das folhas da Espanha com o Claude** antes de fechar o ano, conferida por outra pessoa. | Espanha 27/10 22:55 | Pedido ao BAU (Mohamed); não é nosso. |

## 8. O que confirmar com a Manju antes de começar
- **Lista de países e ordem.** Os 9–10 do BAU master list de cada um, ou todos os 60 em produção?
- **Formato.** Pedir o documento do Vietnã e do Taiwan para usar como modelo.
- **Prazo.** Há data do Marko, ou propomos depois de medir um país?
- **Fronteira com a certificação interna.** Usar um único contato com o BAU por país para as duas coisas, para não perguntar duas vezes.

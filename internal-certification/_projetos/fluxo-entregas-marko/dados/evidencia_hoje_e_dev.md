# Evidência da rota de hoje e contato do Dev (29/10/2026)

Fontes: `scripts/buscar.py` e varredura literal do índice (tickets, reuniões, chats) em `C:\Users\instituto\Documents\brain-service\raw\`. Sem API do YouTrack, sem `.env`. Cada trecho foi aberto no arquivo antes de anotar. Caminhos abaixo são relativos a `raw/`. Sem dados de empregados.

## 1. Evidências por país (rota de hoje)

| País | Entrega | O que diz (trecho literal) | Arquivo:linha | Leitura |
|---|---|---|---|---|
| NO | a-melding (Altinn) | "I validated the A-melding XML for reMarkable Norway ... This file will likely fail or generate errors on submission — there are two systemic, file-wide defects that need fixing before we send it" | tickets/api/2026-10-16/HRBS-14231.md:25-27 | O HR Blizz gera o XML; a conferência é feita por nós/suporte antes de "send". Quem transmite e por qual canal não está dito. |
| NO | a-melding | "7. `loennsutbetalingsdato` empty in both files — mandatory for Altinn." | tickets/api/2026-10-16/HRBS-14231.md:209 | Arquivo do HR Blizz é feito para o Altinn. |
| NO | a-melding (correção de relatório) | "Report-side items from Mohit's table are deployed to production" (Drew Õispuu, 10/09) e "this is fixed" (16/10) | tickets/api/2026-10-16/HRBS-14231.md:92-94, :293-295 | Quem corrige o gerador do XML é o Dev (ver §3). |
| NL | Loonaangifte (XML de imposto) | "we are validating the Tax XML file through the VTS validation tool ... we are unable to submit the Tax XML to the tax authority, as the authority portal will reject it." | tickets/api/2026-10-16/HRBS-15179.md:34-36 | O XML sai do HR Blizz; a validação é no VTS e o envio é "ao portal da autoridade". O ticket é de um analista do lado do serviço/cliente (Umesh Gaikwad); a conta que de fato envia não está dita. |
| NL | Loonaangifte (referência de pagamento) | "Currently we are updating tax reference number manually under Legal entity HR fields-Tax Authority Bank Details." | tickets/api/2026-10-27/HRBS-9646.md:34 | Betalingskenmerk digitado à mão hoje; mesma página (:111) deixa em aberto se o produto executa o pagamento ou o cliente paga do próprio banco. |
| NL | Loonaangifte (Mammoet P09-P13) | "declaração (loonaangifte XML)" entre os 6 entregáveis por período; "Mammoet Nederland B.V. ... ~680 empregados" | chats/2026-10-20-claude-nl-automation-resumo.md:6 | Entrega por período, produzida por pipeline/validação nossa. Canal de transmissão não dito. |
| UK | EPS (HMRC) | "We need to generate the September 2026 EPS report and submit it to HMRC, as the client is following up on the submission." | tickets/api/2026-10-13/HRBS-15260.md:233 | Pedido do cliente (McDermott) ao serviço. O envio ao HMRC aparece como tarefa do serviço; mecanismo não dito. |
| UK | FPS / EPS | "The one that you have shared is FPS but the issue is with EPS file." (Afrin Fathima, 01/10) | tickets/api/2026-10-13/HRBS-15260.md:145 | HR Blizz tem arquivos FPS e EPS. |
| UK | FPS / RTI | "Are there any RTI/FPS reporting concerns with the off-cycle ..." | tickets/api/2026-10-13/HRBS-15864.md:113 | Cliente trata FPS/RTI como saída do sistema. |
| UK | FPS (pergunta aberta) | "whether the FPS has been submitted for each" (Sep e Oct) | tickets/api/2026-10-28/HRBS-16010.md:144 | Não sabemos se o FPS foi enviado; é pergunta em aberto no ticket. |
| UK | PGL1 (entrada) | "File API-REF-01-911-UK_PGL1_Inbound_to_UK-...json was imported ... with an HMRC PGL1 notice" | tickets/api/2026-10-28/HRBS-16010.md:77 | Entrada vinda do HMRC por interface API (puxa, não envia). |
| IE | Irish Tax Payroll Submission (ROS/PSR) | "the submission of payroll data (PSRs) requires a valid ROS Digital Certificate to connect to Revenue's systems" (Wallisson, 23/10/2025) | tickets/api/2026-10-09/CT-4078.md:70-74 | O software conecta direto ao ROS com certificado digital em nome da entidade: rota automatizada. |
| IE | RPN (tax cards) | "The software connects to the Revenue Online Service (ROS) using a ROS Digital Certificate to pull RPNs" | tickets/api/2026-10-09/CT-4078.md:65 | Pull automático. |
| IE | PSR e NAERSA | Config de saída "Irish Tax Payroll Submission" e "NAERSA Contribution Submission with Reconciliation Details"; erro "Outbound REST API Call failed" | tickets/api/2026-10-27/HRBS-13860.md:56-57 | Transmissão automática pelo HR Blizz (outbound config), com falhas tratadas no suporte. |
| IE | NAERSA | "softwareUsed=HRBlizz, softwareVersion=1.2.2 ... fileAcknowledged=true" | tickets/api/2026-10-27/HRBS-13860.md:184 | Prova de transmissão pelo próprio HR Blizz ao NAERSA. |
| IE | NAERSA | cliente pede: "amend the classes and submit the Naersa submissions for August today please." | tickets/api/2026-10-27/HRBS-13860.md:27-29 | Quem aciona o envio é o serviço/suporte, a pedido do cliente. |
| Geral | Estratégia | "right now ... all manual and it is all done through ice. Now, the intent of the management is to remove this ice ... we get this ... authorized from the customer ... transmit it through our registered ..." (Manju, sobre Vietnã/Taiwan) | reunioes/2026-10-27-research-team-weekly.txt:70-71 | Modelo do projeto. Hoje o padrão é manual via ICE onde não há XML; o alvo é automatizar. |
| Geral | Fonte do "como é hoje" | "How do we know the process for each country? ... That is what you can take from Bau. Team." | reunioes/2026-10-27-research-team-weekly.txt:70 (fala 12:08-12:15) | A rota de hoje de cada país deve vir do time BAU. |
| Geral | Intenção do diretor | "whatever filings we are making ... are filed with the in automation process without any manual intervention, without any third party intervening" | reunioes/2026-10-27-research-team-weekly.txt:81 | Objetivo, não evidência de rota. |
| Geral | Espanha/CI (referência) | "Integração outbound-dominante: HRBLIZZ gera o arquivo e o cliente submete no portal" | chats/2026-10-01-mercans-compliance.md:63 | Padrão histórico (Antes de 2026-08, ES e CI), não dos 12 países. Serve só de comparação. |
| Geral | Revisão dos filings | "reports generated by teams are not entirely correct and are being manually corrected using Claude before submission" | reunioes/2026-10-07-research-team-weekly.txt:41 | Europa primeiro; o relatório é corrigido à mão antes do envio. |

Achados que NÃO provam rota (ficam como contexto): UA "1C" em tickets/api/2026-10-15/HRBS-15864.md é imagem; as menções a 1C em `reunioes/2026-09-25-ukraine-migration-checkpoint.txt:49` são o sistema de folha anterior do cliente, para histórico (YTD), não canal de envio. A reunião 2026-09-04 com Ekaterina Kozak (Ukraine ICE) é sobre o cálculo da folha na ICE, sem trecho sobre o envio (conferido por grep de file/submit/portal/DPS/sign: só 2 acertos fracos, nenhum sobre envio).

## 2. Países sem nenhuma evidência da rota de hoje

Busca literal (com termos locais e genéricos) em tickets, reuniões e chats:

- **SE Suécia, FI Finlândia, EE Estônia, KZ Cazaquistão, AZ Azerbaijão, RU Rússia:** zero tickets em `raw/tickets/api` com o campo País igual a eles, zero ocorrência de Skatteverket, AGI, Tulorekisteri, Incomes Register, e-MTA, TSD (só a reunião 2026-10-09 usa "TSD" como exemplo do Taiwan/Estônia sem país confirmado, ver abaixo), KGD, ЭЦП. (RU, KZ e AZ: nenhum ticket e nenhuma reunião.)
- **DK Dinamarca:** só HRBS-15410 e HRBS-16573 (regulação e férias, não envio). Zero eIndkomst, NemID/MitID.
- **UA Ucrânia:** tickets só de WTC, DD e relatórios (HRBS-12548, SR-414/415 Form 1-PV). Nenhuma menção a DPS, KEP, ЭЦП, J0500111 como canal de envio. Há o nome DPS e J0510611 apenas como versão de formulário em `chats/2026-10-01-mercans-compliance.md:145`.
- **NO:** Altinn só como destino do arquivo; Maskinporten zero. **NL:** Digipoort e PKIoverheid zero.
- **UK:** Government Gateway zero.

Atenção sobre "TSD": `reunioes/2026-10-09-call-manju-wallisson.txt:97` ("this one declaration and payment is a TSD") é demonstração na ferramenta, e o país da tela não está no trecho. Não usar como evidência de EE sem confirmar.

Para estes países a única via é o time BAU (Manju, 27/10).

## 3. Contato do Dev (geração e transmissão no HR Blizz)

Nenhum ticket ou índice nomeia um "dono" formal por país para a transmissão. Os três nomes abaixo vêm de comportamento observado nos tickets, não de organograma.

| Nome | Papel observado | Evidência (ticket, data) |
|---|---|---|
| **Illya Virchenko (ivirchenko)** | Integration / Config Factory. Cuida da interface outbound e da resposta dos órgãos. | HRBS-13860 (Irlanda, NAERSA/ROS), comentário de 11/09/2026: "INT Team is already looking into the interface response investigation ... Please ensure all other questions are addressed to the relevant teams, e.g., Compliance, Report configuration" (tickets/api/2026-10-27/HRBS-13860.md:207-209). `fronteiras.md:21` lista "Integration (Illya Virchenko / Config Factory)" como dono de interface e integração. O chat registra "Ilia Virchenko: Integration / Config Factory" (chats/2026-10-01-mercans-design-dev-kb.md:119). |
| **Drew Õispuu (broispuu)** | Dev que corrige o gerador de relatório/XML em produção. | HRBS-14231 (Noruega, a-melding): "Report-side items from Mohit's table are deployed to production" (10/09/2026) e "@nkeer this is fixed" (16/10/2026) (tickets/api/2026-10-16/HRBS-14231.md:92-94, :293-295). Papel de Dev é inferência pelo conteúdo (sem título no ticket). |
| **Mohit Jain (mjain)** | Head of Compliance Product. Faz a ponte com o Dev e a fila do Marko; não é quem codifica. | Assinatura "Head of Compliance Product" (ex.: HRBS-15179.md:155-160); no HRBS-15179 (NL Tax XML, "Pending on Development team") direciona "Please raise this with Markko". `fronteiras.md:9,32` o lista com Configuration/Dev e Product. |

Citações de fluxo: o Romano Fusana (L2 Support, assignee de HRBS-13860 e ponte com o Dev; HRBS-15179.md:188-195 "Dev team has below verifications") é o canal prático para chegar ao Dev em incidentes de envio, mas é suporte, não Dev.

**Recomendação de quem perguntar**
1. **Rota de hoje por país (SE, FI, EE, DK, UA, KZ, AZ, RU):** primeiro o **time BAU** (Manju já mandou procurar, 27/10), depois o Dev.
2. **Quem transmite e como (NO, NL, UK, IE):** **Illya Virchenko** (Integration), pergunta fechada: "para IE (ROS/NAERSA) o outbound é automático; para NO (Altinn), NL (Digipoort), UK (HMRC FPS/EPS) existe outbound config no HR Blizz ou o cliente envia o arquivo gerado?".
3. **Gerador do arquivo (relatório/XML):** **Drew Õispuu**, para NO.
4. Passar por **Mohit Jain** quando a pergunta for de produto/prioridade (ele encaminha ao Marko).

## Bloco de prova

- **Fontes lidas (trechos abertos):** HRBS-14231, HRBS-15179, HRBS-15260, HRBS-15864, HRBS-16010, HRBS-9646, HRBS-13860, CT-4078; reuniões 2026-10-27-research-team-weekly, 2026-10-07-research-team-weekly, 2026-08-18-research-team-weekly (410-436, sem achado de canal), 2026-09-04-ekaterina-kozak-ukraine-ice; chats 2026-10-01-mercans-compliance, 2026-10-20-claude-nl-automation-resumo, 2026-10-01-mercans-design-dev-kb; `fronteiras.md`; `scripts/youtrack_indice.md` (só lista de títulos). Não li o `.env` nem usei a API.
- **Conferido mecanicamente:** varredura literal de todos os termos do pedido por regex sobre o índice do `buscar.py` (tickets, reuniões, chats), com e sem fronteira de palavra; contagem de tickets por campo País para os 12 países (cobre só `raw/tickets/api`, não toda a base do YouTrack).
- **Confiança:** alta (cerca de 90%) nos trechos citados; média (cerca de 60%) na conclusão "sem evidência" para SE, FI, EE, KZ, AZ, RU, porque o índice só tem tickets coletados em outubro e chats/reuniões selecionados. Baixa (cerca de 50%) nos papéis dos nomes do Dev (Drew e Illya): o papel é inferido por conteúdo e por `fronteiras.md`, sem organograma.
- **O que falta:** confirmar com BAU e Dev o canal real de NO, NL, UK, DK e demais; ver se existem tickets do YouTrack fora do coletado (Suécia, Finlândia, Estônia, Cazaquistão, Azerbaijão, Rússia); organograma de Development; recibos nos pacotes `internal-certification/<País>/` (não revistos nesta tarefa).

# Estado — frente alertas

> Escrito só pela janela desta frente. Criado em 2026-11-05 pela janela geral; reescrever a cada "fecha a sessão". Regras: [[frentes/alertas/CLAUDE|CLAUDE da frente]].

## Instruções vigentes
- 05/11 (usuário, pela janela geral): a frente cobre **tudo de alertas** (kit da Manju, alerta por país + monday, AI-Generated Alerts, Compliance Calendar, SCA) e é responsável por **dar início e fechar** cada alerta.
- 05/11 (usuário): **instalar o kit "Statutory Updates Tracking 2026" da Manju, com backup antes** de `~/mercans-pipeline` (sem remote, 2,1 GB).

- 06/11 (usuário): mensagens a terceiros objetivas, sem explicação longa.
- 06/11 (usuário): **ticket de alerta direto**: só abertura "Effective…", itens "antigo - novo", próximos passos em 1 linha, Official source, Mercans update; sem parágrafos de contexto. Modelo: CT-4632 (BH). Google Doc em `Country Folders/<País>/09 - Alerts/<ano>/`, nome com underscores, sem .docx ao lado.
- 06/11 (usuário): Namíbia: vigência **01/09/2026** (data da SSC).
- Passo final do alerta (modelo: e-mail do BH de 06/11 16:56): e-mail à **Usema** (uishtiaq@), Cc **Manju** (mshetija@) e **Mohsin** (mkhan@), assunto "<País>: <Assunto> - <data>", corpo "Dear Usema… Please find the link to the Statutory Alert document for <País> attached. <nome do Doc com link> Please review the format and publish it on the Mercans portal. Kind regards," + assinatura "Wallisson - Mercans". Namíbia: rascunho no Gmail em 06/11, não enviado.
- 06/11 (usuário), roteiro dos alertas dos países BAU: (1) cruzar a planilha de mudanças (`rascunhos/2026-11-06-alertas-todos-paises/…_v2.xlsx`) com a lista de responsáveis; (2) países sem dono → confirmar com o usuário; (3) filtrar os alertas dos países nossos; (4) país em design/desenvolvimento (ex.: CO, BE, FR, CA): conferir se a research atual já cobre a mudança; se não, atualizar a research e avisar o Dev ou mandar CR se o desenvolvimento já começou; (5) demais países: ticket de alerta, revisado com o usuário antes (só mudanças relevantes).
- 06/11 passo 2: usuário preencheu os donos (`rascunhos/2026-11-06-alertas-todos-paises/Country_Owners_2026-11-06_v2-usuario.xlsx`): nossos = BH, BE, BW, BG, CA, TD, CL, CO, CR, CI, EG, JO, KW, NA, NG, OM, Congo-Brazzaville, EUA (+ EE, FR, IE, NL, ES, UA da Sheet5); Austrália → Enaakshi; 24 sem dono → mensagem ao grupo RA Team (rascunho, não enviada).
- 06/11 call usuário × Vinícius (`raw/reunioes/2026-11-06-alertas-vinicius-congo-country-allocation.txt`):
  1. **Prioridade de hoje: ticket de alerta do Congo** ("era de setembro", 06:52); o Vinícius cria e manda ao usuário para conferir (10:40). A transcrição não diz qual Congo: a única mudança de setembro achada é a INPP da RD Congo (24/09/2025, CT-4383); na República do Congo a varredura de 06/11 não achou mudança confirmada (LFR 2026 e PLF 2027 não lidos). **Confirmar com o usuário.**
  2. País ativo → ticket de alerta; país em desenvolvimento (França, Bélgica, Colômbia) → CR ao Development dizendo que a lógica em construção muda (09:50–10:40).
  3. **Filtro: só mudanças com vigência a partir de 01/07/2026** (as de janeiro já teriam chegado); a planilha de mudanças precisa da coluna de vigência (07:38–09:32). Triagem do usuário: Austrália, Dinamarca e Egito não são nossos; Bahrein 01/01/2027 provavelmente não precisa; Colômbia 15/07 provavelmente já está na research (conferir); Estônia 01/01 provavelmente já enviada.
  4. Responsáveis: base = **Country Allocation** (Drive). Monday sem a República do Congo. O Vinícius atualiza o Country Allocation no Drive (países faltantes + marcações do usuário) e manda ao time com mensagem curta. **Esta frente não mexe no Country Allocation.**
  5. Depois do Congo, o Vinícius gera os alertas de todos os países nossos; revisão conjunta com o usuário (07:07, 10:53). Papel desta frente: conferir fonte oficial, manter a fila, preparar a revisão.
- 06/11: achada a lista oficial de responsáveis **"Country Allocation.xlsx"** (aba Country Allocation, coluna Team Member; cópia em `raw/drive/2026-11-06-country-allocation/`, md5 77B92EB9…). Dos 24 "sem dono", 23 têm dono nela (Shruti/Enaakshi); a Rússia está como "PROHIBITED LIST". Fora da lista: Congo-Brazzaville, Chade, Costa do Marfim. Divergências com a marcação do usuário: Bahrein, Kuwait, Omã (Enaakshi) e Egito (Shruti). RD Congo = Shruti.

## Fluxo do alerta de país (extraído do caso Namíbia, 06/11)
1. Sinal (reunião, chat, cliente, varredura) → confirmar o país exato (Congo ≠ RD Congo) e a mudança na fonte do sinal (transcrição).
2. Dono: Country Allocation → nosso? Sem dono → grupo RA Team.
3. Filtro: payroll e vigência ≥ 01/07/2026.
4. País ativo → alerta + ticket. Em desenvolvimento (CO, BE, FR, CA) → CR/research. Só research → atualizar research.
5. Já existe? YouTrack (Epic Regulation Update, HRBS do cliente) e alerta publicado.
6. Fonte oficial e vigência; conflito de data → usuário decide.
7. Planilha de mudanças: linha em "Alerts - in production", Action "Alert + ticket".
8. Word no modelo (AZ) → Drive `Country Folders/<País>/09 - Alerts/<ano>/` → Google Doc nativo, nome `CC_Assunto_Mês_Ano` com underscores, sem .docx.
9. Ticket: rascunho no YouTrack no modelo CT-4632 (texto direto; Official source; "Mercans update - [Doc](link)"; Development task, Country, Epic, Mohit, sprint, Start/Due, Original estimation e Estimation 1w, Acceptance NA, sem anexos) → usuário revisa e cria.
10. E-mail à Usema (Cc Manju, Mohsin) com o link do Doc → publicar no portal.
11. Registro: hub, estado, log, CONFERENCIA.md.
12. Fechar: Dev em produção + alerta publicado → comentar "Mercans Alert- <link>" no ticket.

## Modelo de alerta + ticket (claude.ai, projeto MERCANS, conversa "Arquivo alert", 06/11 ~16:30)
- Word do alerta montado sobre o modelo `AZ_Changes in Income Tax rate_Jan 2027.docx` (troca só capa, título, texto, tabela, impacto e fonte); nome `<CC>_<Assunto>_<Mês AAAA>.docx`; vira Google Doc ("Mercans' update").
- Ticket: Title = nome do alerta; Description "<País> - Effective <data>, … as under:" + itens antigo - novo + o que não muda + "Official source- <lei, artigo>: <link>" + "Mercans' update- <link do Doc>"; Acceptance criteria NA; campos Country, Epic Regulation Update, Sprint Year-end Updates 2027, Due date, Start date.
- 1º caso feito lá: BH_Increase in Employer Social Insurance Contribution_Jan 2027 (rascunho; o usuário tinha dito na call que Bahrein 01/01/2027 "provavelmente não precisa").
- **Namíbia (06/11): é o país que precisa do alerta** (não o Congo). Ponto a fechar antes: vigência do teto 12.500 = 01/03/2026 (GN 236/2026, GG 8975) × 01/09/2026 (PwC/Sage: adiado por Public Notice SSC de 07/08/2026, não achado em fonte primária); tetos futuros 14.000/15.000/16.000 (01/03/2027–2029). Ver [[Namibia]] Valores-chave.

## Plano em curso: BRD SCA até a nota 10 (usuário, 06/11)
- Plano e avaliação: [[revisoes/2026-11-06-brd-sca-plano-ate-10|BRD SCA: plano até 10]] (7 etapas; a etapa 1 é a instalação do kit abaixo). Seguir na ordem, sem parar entre etapas locais; parar só para Drive/envio/download e mudança de escopo.

## Próximo passo (primeira tarefa)
1. Ler no Gmail (Chrome) o e-mail da Manju "Statutory Updates Tracking & Handover to Development" (05/11 4:51; para Enaakshi e Wallisson; Cc Marko) e listar os anexos (nome e tamanho). Antes de baixar, dizer ao usuário o nome, a origem e o tamanho de cada arquivo e esperar o ok.
2. Copiar os anexos para `raw/drive/2026-11-05-statutory-updates-tracking/` (o processo de fim de ano e o kit) e ler `START HERE.md` → `windows-setup/README.md`.
3. Backup de `~/mercans-pipeline` antes de instalar (ex.: `~/mercans-pipeline_backup_2026-11-05`; conferir contagem de arquivos e tamanho).
4. Instalar pelo README (Git Bash), sem mexer no resto do pipeline. Rodar uma vez em teste e conferir a planilha gerada em `~/mercans-pipeline/statutory-update-tracker/outputs`.
5. Agendar a rodada de segunda e quinta 12:00 só depois do teste e do ok do usuário.

## Fila de alertas
| Data | Origem | País | Assunto | Etapa (1–7) | Próximo passo |
|---|---|---|---|---|---|
| 2025-12-16 | CT-4285 (Epic Regulation Update) | [[Lituania]] | Alerta 2026 corrigido pela fonte oficial | 6 | Conferir no YouTrack se o Dev liberou; opcional: destaque azul e Change summary (hub LT) |
| 2026-10-19 | AI-Generated Alerts (Usema) | EUA | OASDI 2027 $192.300; COLA 3,6% (SSA) | 3 | Confirmar se o texto completo chegou e se foi aprovado |
| 2026-04-05 | CT-4383 (Manju; Epic Regulation Update; Ready for Development, Mohit) | [[RD-Congo]] | Alerta "DRC_Statutory_Change_Alert_2026_v2" (Doc 14Lzp5RI…): INPP patronal a partir de 24/09/2025 (Arrêté interministériel de 24/09/2025, art. 3) + IRPP a partir de 01/01/2026 (Loi 23/053) | 6 | 06/11: Arrêté lido no original (art. 3: vigor na assinatura, 24/09/2025) → alerta certo; design (Effective Date 01-01-2026 na 9180151) diverge. Registrado em [[RD-Congo]]. Decisão do usuário: levar ao Dev/Lily ou aceitar 01/01/2026 |
| 2026-11-06 | Call usuário × Vinícius (06:52) | [[Congo]] (República do Congo, confirmado pelo usuário 06/11) | **PRIORIDADE DE HOJE:** ticket de alerta "de setembro" | 2 | 06/11: nenhuma mudança de folha em vigor achada: JO ordinários 28–45/2026 (jul–05/11) lidos por script, só o Arrêté 1560 DAS3 (já no research); LFR 2026 = só orçamento (página do Min. Finanças 14/07); Gmail desde 08/2026 sem e-mail de alerta do Congo. PLF 2027 (draft, `raw/docs/oficiais/CG/2026-11-06-PLF_2027_Parlement.pdf`, md5 D62EF6DA…): art. 50 pt 4 (116 F, família em 1º/jan, mudança só no ano seguinte), pt 8 (185 bis, fim de regimes/forfaits de ITS de expatriados em 01/01/2027), pts 20–21 (TUS paga até dia 15, só à administração fiscal; nova repartição), art. 4 (Estado paga IRPP e ½ patronal dos 30.000 primeiros novos declarantes; taxas CNSS/CAMU mantidas). Aguardar voto (dez.). Hipótese: o "de setembro" pode ser a Namíbia (teto 01/09/2026, mesma reunião BH). JO 18–27 (30/04–25/06) também sem folha. CNSS (cnss.cg): site em JS; Chrome sem permissão de leitura no domínio e a leitura dos dados por script foi bloqueada → usuário colou cnss.cg/#/actualites e #/documents (06/11): 3 notícias genéricas, todas datadas 06/11/2026 (data padrão do site, não de publicação) — modernização, novas agências, lembrete do prazo dia 15; documentos = formulários de imatriculação, Code de la sécurité sociale (Loi 004/86), guia eDéclaration, bordereau, DAS. **Nenhum comunicado de alíquota/teto. Conclusão: República do Congo sem mudança de folha em vigor desde 01/01/2026; não há ticket a abrir hoje.** DGID: impots.gouv.cg é só login (sem comunicados); finances.gouv.cg sem comunicado de folha (e-bulletin = só servidores públicos) |
| 2026-11-06 | Alerta Namíbia (decidido com o usuário) | [[Namibia]] | Teto SSC 12.500 desde 01/09/2026 (Gazette: 01/03/2026) + 14.000 em 01/03/2027 | 6 | 06/11: **postados pelo usuário**: ticket **CT-4633**, Google Doc (Namibia/09 - Alerts/2026) e e-mail à Usema. Fechar quando: Dev liberar (HRBS-16952, produção 09/11) + Usema publicar (comentar no CT-4633 "Mercans Alert- <link>"). Pendente à parte: CCG com teto antigo (versão nova + aviso ao Dev, ver [[Namibia]] Pendências) |
| 2026-11-06 | Reunião "Checks on BH" (raw/reunioes/2026-11-06-checks-bh-congo-gabon-namibia.txt) + HRBS-16791/14605/16952 | Namíbia | Teto SS 11.000→12.500 (NAD 112,50) desde 01/09/2026; Mohit aplicou, produção na publicação de segunda (09/11) | 6 | Fechar quando sair em produção (conferir HRBS-16952 após 09/11) |
| 2026-11-05 | AI-Generated Alerts (Usema/Manju) | [[Reino-Unido]] | National Living Wage £13,21 | aprovado pela Manju | Conferir na fonte oficial e registrar no hub com vigência |

## Compliance Calendar
- Pedido do Marko (via Manju, weekly 27/10): produção, ~60 países, 1–2 por semana, prioridade aos países com clientes ativos (BAU master list). Antes estava na frente Certificação, sem início registrado ([[ESTADO]]).
- Espanha conferida em 19/10: 10 eventos, 3 datas erradas, só jan–mar, nenhum evento publicado.
- Shruti (20/10): baseline de alertas com lacunas; resposta v2 (pedir arquivo, país e exemplos) **não enviada**.
- Reunião de 29/10 "Compliance Calendar Review, Reporting automation guide" (Manju, Enaakshi, usuário): notas do Gemini no Doc `1t7SPYLNcoUufhYBjmpL-DQSm3wCoFjt7LOHqn__EsOk` (não ingerido).

## Material de partida
- Processo anual: `raw/drive/2026-11-03-weekly-research/Annual Statutory Updates - Tracking, Development and Release Process.docx`.
- BRD da SCA: `~/Downloads/BRD_Statutory_Change_Alert_Automation_v1_1.docx` (28/08; não ingerido). Exemplo de alerta: `~/Downloads/Statutory Change Alert_ Ireland – Payroll Legislation Updates January 2026 (1).docx`.
- SCA no pacote de automação: `rascunhos/2026-10-27-pacote-automacao-samuel/00-LEIA.md`.
- Board do monday: `prompts/extracao-monday.md` (linha 12).
- 03/11 (weekly): a Manju pediu detalhes de como acompanhamos as mudanças de legislação (agendador do Claude); a Enaakshi pediu à Manju a skill do documento de alertas (`rascunhos/2026-11-04-triagem-chat.md`).

## Lacunas (o cérebro não tem)
- Como a Shruti detecta mudanças, cadência e critério de publicação no Compliance Calendar; país e arquivo do baseline dela.
- Se o kit da Manju, a SCA e o Compliance Calendar são o mesmo sistema ou se conversam.
- Treinamento "Compliance Calendar Overview/Demo" não ingerido; skill de alertas da Manju ainda não recebida.

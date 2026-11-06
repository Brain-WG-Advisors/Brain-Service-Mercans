# Triagem de e-mails — 2026-11-05 (~11h BRT)

Frente Gmail ([[frentes/gmail/estado|estado]]). Lido pelo Claude in Chrome, caixa wgomes@mercans.com (conferida no título). Busca `newer_than:3d`; abertas as conversas novas de 05/11 e as respostas de 04/11 ainda não registradas. Anterior: [[2026-10-28-triagem-emails]].

## Agir
1. **Manju, "Country payroll filing process flows and specs"** (05/11 8:45; para Wallisson, Enaakshi; Cc Marko). Kit "Country Filing Kit" (zip com README e amostra de Taiwan; usado em Vietnã e Taiwan) para documentar todas as obrigações de folha (declarações, pagamentos, documentos de fim de ano) e gerar process flows + report specs para automação. Focar nos **países da planilha do Andy** (anexa). "You own the work and sign-off for your countries." Depois: **ICE Usage Removal Programme**, onde o ICE ainda é necessário e o plano para mitigar. Pedido: executar; perguntas à Manju. Anexos não apareceram no texto lido: baixar o kit e a planilha (pedir ok para download). Frente provável: Pipeline/Certificação (decidir na geral).
2. **Manju, "Statutory Updates Tracking & Handover to Development"** (05/11 4:51; para Enaakshi e Wallisson; Cc Marko). Anexos: processo de mudança de fim de ano alinhado com o Development + kit "Statutory Updates Tracking 2026" (roda seg/qui 12:00 e gera uma planilha para o Dev por rodada; saída em `~/mercans-pipeline/statutory-update-tracker/outputs`). Pedido: instalar (START HERE.md → windows-setup/README.md, Git Bash). Regra dela: atualizar CCG/WTC/DD/specs **só na versão atual com change log, nunca gerar documento novo** (bate com a regra 10 / [[change-log-sem-documento-novo]]). Atenção: instala em `~/mercans-pipeline`, que não tem remote ([[mercans-pipeline-sem-remote]]): fazer backup antes.
3. **HRBS-16835 STG Spain, holerite** (Nihita 04/11 22:10, nos marcou; Katrin 05/11 6:41). Nihita: licença médica sem unidades/taxa no holerite; o módulo de licença usa 79308/79608/79708/79808 e não 79008/79014; 63714 (taxa) não mapeado; pergunta ao Brenet como mostrar taxa ≠ 100%. Katrin explicou que os elementos por faixa são do desenho, não customização, e **vai marcar call** para fechar a spec de mapeamento do holerite. Nosso: a pendência já registrada em [[Espanha]] (conferir na spec do Payslip ES se unidades/taxa desses elementos estão lá) antes da call. Ticket = janela Suporte.

## Só saber
4. **CR02 STG Spain (seguro-saúde), "URGENT: STG: Spain – Discrepancies"**: após nossa mensagem (00:04, €41,67/mês, pedido à Lily para configurar), Lily copiou o Mohit; Mohit (2:20) diz que **não aprovou CR com estimativa do Dev e que requisito de cliente é CR pago**; Nihita (4:44) respondeu que não é específico do cliente (prática comum na Espanha), CR é só governança, sem custo. Nada pedido a nós; discussão Mohit × Nihita. Se nos perguntarem: o rateio mensal é escolha de configuração dentro da lei (Lei IRPF art. 42.3.c, €500/ano por pessoa), ver [[servicos/lei-x-mercado]]. Registrar em [[Espanha]].
5. **HRBS-16407** (YouTrack, Lily atualizou 05/11 10:56): ticket da janela Suporte.
6. **Ucrânia, Nataliia (04/11 8:02)**, resposta ao nosso e-mail de 03/11: rota atual = arquivo HR Blizz → Medoc (Mercans valida) → cliente assina com o KEP do diretor e entrega pela Medoc; clientes não deram o KEP à Mercans. J0500111 e 1-PV confirmados. **Faltam na lista:** 1-борг (atraso salarial) e o novo relatório trimestral de emprego de pessoas com deficiência (2026, aceito desde 09/10). Itens 4–6 respondidos com 7 zips (relatório unificado set/2026 + recibos DPS, 1-PV mensal 09 e 3T, balancete, banco, holerites, confirmação 1-PV); itens 7–12 "depois". → Frente Certificação (Altium) e hub Ucrânia. Download dos anexos só com ok.
7. **Spain BIK for Gross-Up** (Gulnaaz 04/11): Lily liberou WTC V4.9 (campos M145) e a configuração vai às entidades (Vaishnavi, Abarna, Asad). Nada pedido a nós.
8. **AI-Generated Alerts** (Usema/Manju 05/11): Manju aprovou o alerta (UK, living wage £13,21). Nada a fazer.
9. **Suman, BE-CCG-001-v1.1** (04/11, 2 action items + atividade): já respondidos pela frente Chat em 04/11 13:44–13:45 (log). Conferir se há comentário novo depois disso.
10. **SR-224 ES Payslip**: Drew corrigiu e publicou em produção (04/11 13:36).
11. Agenda: McDermott Open Tickets Review sex 06/11 5:00 BRT (Lavanya); AI Pod roadmap seg 09/11 9:30 (Marko e Martin aceitaram); Ukraine checkpoint de 04/11 cancelado.

## Ignorar
Workday Innovation Partner (Mohsin), GitHub (Copilot, convite Brain-WG-Advisors, verificação), Anthropic login, Tactiq/Gemini (transcrições: regra de ingestão em `raw/reunioes/` é da geral), Trello, monday.

## Revisão ~17h BRT (pedido do usuário: quantos responder)
Erro da 1ª passada: li só as conversas novas da manhã e não conferi a **última mensagem** de cada conversa da caixa; chegaram pedidos depois. Conferido agora, conversa por conversa (Inbox, 10 dias).

**Responder (pedido direto a nós):**
- **R1. Nihita, "URGENT: STG: Spain – Discrepancies" (05/11 13:40), urgente.** (1) HRBS-16884: cálculo manual detalhado do IRPF dos 2 empregados (IDs no ticket) e como o sistema chega ao percentual; a Lily corrigiu a fórmula do 58294 na entidade, mas a validação do Claude ainda diverge. (2) HRBS-16927: faltam "Imp.Ingr. a Cta. Esp. Cgo.Emp" e "Imp.Ingr.a Cta.Valores Especie" (ingresso a cuenta de rendimentos em espécie; carro, estacionamento), Wallisson e Lily. (3) Coordenação com a Lily (fuso). (4) CR do seguro-saúde configurado para refazer os holerites **amanhã (06/11)**. Pede plano de ação e prazos. Tickets → janela Suporte; e-mail curto com o plano → aqui.
- **R2. Daniel, Namíbia teto SSC (05/11 15:12):** "ainda sai NAD 99,00 na folha de novembro de 2026, pode verificar?". Nosso valor (NAD 112,50 desde 01/09/2026, HRBS-14605) já foi confirmado em 03/11; a pergunta original (03/11) era se foi publicado em produção (HRBS-16791) = Development/Mohit ([[fronteiras]]). Resposta: valor confirmado; a publicação é do Dev, com Mohit em cópia.

**Analisar e talvez responder (Certificação):**
- **R3. Nataliia, Ucrânia (05/11 13:57):** arquivos de julho e agosto + respostas ponto a ponto.
- **R4. Suresh, Holanda/Excerpta (05/11 12:34):** comentários + relatórios anexos, resposta ao nosso e-mail de hoje.
- **R5. Marju, Estônia/Finlândia (05/11 16:46 e 17:08):** respostas sobre TSD/e-MTA, TÖR etc.; "the filing is done".

**Sem resposta necessária (conferido):** HRBS-16835 (Nihita 15:28 "Yes please Katrin", call), Umesh/Malika/Deepak (última mensagem é nossa, 17:02–17:03), Rússia (nossa à Olga 12:23), skills v2.12 (nossa), Abuja (nossa), Spain Migration (nossa 04/11), France Compliance (Mohit 03/11: artefatos congelados até o fim do desenvolvimento; só saber), Colombia PMI (Mohit 03/11; tratado em 04/11, regra 10), Lituânia (Kevin 02/11 "well noted"), Statutory Leaves EOR (Sadaf → Manju), Manju ×2 (executar, sem resposta).

## Não aberto (anterior a 04/11, conferir se já tratado)
Namíbia teto SSC (respondido por nós 03/11), Rússia (Sadaf/Olga → Certificação), Noruega SOP A-Melding e SOP Suécia (Manju 03/11), HRBS-16418 Henkel TN, HRBS-16010 McDermott PGL.

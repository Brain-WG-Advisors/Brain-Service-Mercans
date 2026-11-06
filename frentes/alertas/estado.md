# Estado — frente alertas

> Escrito só pela janela desta frente. Criado em 2026-11-05 pela janela geral; reescrever a cada "fecha a sessão". Regras: [[frentes/alertas/CLAUDE|CLAUDE da frente]].

## Instruções vigentes
- 05/11 (usuário, pela janela geral): a frente cobre **tudo de alertas** (kit da Manju, alerta por país + monday, AI-Generated Alerts, Compliance Calendar, SCA) e é responsável por **dar início e fechar** cada alerta.
- 05/11 (usuário): **instalar o kit "Statutory Updates Tracking 2026" da Manju, com backup antes** de `~/mercans-pipeline` (sem remote, 2,1 GB).

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

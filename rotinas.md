# Rotinas — as frentes do serviço

> Criado em 2026-10-15. Visão geral do que fazemos de forma recorrente. Sem agendamento: **o usuário avisa quando rodar** ("roda a frente N" / "abre o dia"). Detalhe de cada passo fica no [[CLAUDE]] e nas skills; aqui só o essencial.

## De rotina (entra coisa nova todo dia)

| # | Frente | Para que serve | Entrega | Estado fica em |
|---|---|---|---|---|
| 1 | **Suporte** (YouTrack) | Responder o que foi pedido a nós nos tickets | Rascunhos de resposta e arquivos, para ok do usuário | `frentes/suporte/estado.md` (tabela de tickets) |
| 2 | **Gmail** (Mercans) | Separar o que exige ação nossa | Lista curta: agir / só saber / ignorar | `frentes/gmail/estado.md` + `rascunhos/AAAA-MM-DD-triagem-emails*.md` |
| 3 | **Chat** (Mercans) | Idem, para as conversas do time (usuário cola/exporta) | Mesma lista curta | `frentes/chat/estado.md` + `rascunhos/AAAA-MM-DD-triagem-chat*.md` |

Cada frente 1–5 tem a sua janela do Claude Code, aberta na sua pasta `frentes/<frente>/` (abrir com `scripts/abrir_frentes.ps1`). Regras de convivência: [[CLAUDE]] → "Janelas paralelas".
- [[rascunhos/2026-10-16-triagem-emails|2026-10-16-triagem-emails]]: Triagem de e-mails de 16/10 pela janela Gmail (Chrome, só leitura)
- [[rascunhos/2026-10-19-triagem-emails|2026-10-19-triagem-emails]]: Triagem de e-mails de 19/10 (ceiling Costa do Marfim etc.)

## De fundo (sem horário, mas não pode cair no esquecimento)

| # | Frente | Para que serve | Entrega | Estado fica em |
|---|---|---|---|---|
| 4 | **Research pipeline** | Construir países novos e corrigir os existentes quando surge erro | País avançando de etapa; erro corrigido no pipeline/skill | `frentes/pipeline/estado.md` + hub do país ([[00-INDEX]]) + [[correcoes]]; backlog em `revisoes/2026-10-15-licoes-aprendidas/` |
| 5 | **Análise de Reports** (Internal Certification) | Validar os statutory reports do HRBLIZZ com os pacotes das SBCs | Workbook de validação + achados para implementation + cobranças em rascunho | `frentes/certificacao/estado.md` + seção "Internal Certification" do hub do país; método em [[analise-reports]] |

## "Abre o dia"
Passa pelas frentes 1–3 e entrega um painel único:
- **Urgente hoje** — calls, prazos, tickets com resposta nova.
- **Esperando o usuário** — rascunhos prontos para enviar, arquivos para importar.
- **Esperando outros** — o que está parado, com data do último movimento.

Frentes 4–5 entram no painel só se houver algo parado ou novo.

## Regras
- Nada sai sozinho: rotina lê, rascunha e resume; enviar/gravar continua com ok do usuário.
- Agendamento no Maestri: **não por enquanto** (decisão de 2026-10-15). Revisitar quando o ritmo manual estiver estável.

# Onde paramos

> Atualizado em 2026-10-26 (fim da sessão [[sessoes/2026-10-26]]; demais blocos sem mudança desde 2026-10-20). Reescrever a cada "fecha a sessão". Ler ao abrir a sessão.

## Colômbia PMI — pesquisa concluída (2026-10-26)
- Encerrada em 26/10: artefatos finais no Drive/Monday (7 specs v1.0, CCG v1.4, WTC v1.6, DD v1.3, SIR v1.1); delta ao design e e-mail de encerramento enviados pelo usuário; registros no chat "Research Pipeline II". Resumo: [[sessoes/2026-10-26]]; planilha [[Research Pipeline/Colombia/co-report-crosscheck/04-output/CONFIRMACAO-PROCESSOS-CO-2026-10-26.xlsx|CONFIRMACAO-PROCESSOS-CO-2026-10-26.xlsx]].
- YouTrack CT-4593/SR-470: o usuário decidiu não editar (27/10, janela Suporte); levantamento em `rascunhos/2026-10-26-youtrack-links-CO.md`.
- Depois: timeline do Andy quando o Mohit confirmar datas; skill `payroll-compliance-colombia` (#17). Com terceiros, sem bloquear: #54/#55 (cliente/BAU), #41/#51 (Manju/DIAN); dúvidas do design nas colunas T/U = suporte.

## Esperando o usuário (2026-10-20)
- #13037 (TI, Manette): ok para responder "VPN instalada; pasta = link de 13/10 ao Merlin (https://drive.google.com/drive/folders/1BArVL5SGDH1NbkLa0DJ-SR1sqnRz6Uo6); expiração 20/11/2026" → rascunho pela frente Chat. Apuração em `raw/chats/2026-10-20-manette-ti-vpn-pasta.md`.
- Enviar: feedback Montage P09 à Manju (`rascunhos/2026-10-20-feedback-manju-montage-P09.md`), Muhammad e Shruti (`rascunhos/2026-10-20-*`).
- Ruchi (Canadá, K2): bônus pago sozinho e a isenção de $3.500 (T4127), sem resposta.

## Frentes (desde 2026-10-15, cada uma na sua janela)
- Suporte (tickets): `frentes/suporte/estado.md`
- Gmail: `frentes/gmail/estado.md`
- Chat: `frentes/chat/estado.md`
- Pipeline: `frentes/pipeline/estado.md`
- Certificação (Internal Certification): `frentes/certificacao/estado.md`
- HRBS-14255 (Ucrânia, call de migração de 12/10, feriado): usuário confirmar se há algo pendente (o ticket saiu da fila).

## Em descanso (retomar quando o usuário escrever "descanso")
- **Mammoet NL (Nederland + Montage, P09–P13): solução para o caso inteiro** — gate pré-Marko + 4 combinados + crítica de especialista + motor de reconciliação + plano em fases. Pausado de novo em 2026-10-20. Só análise, sem execução até o usuário aprovar. Próximo passo: o usuário aprova a proposta → pauta da fase 0 (Manju/Yojana) e desenho técnico do motor. Tudo em `rascunhos/2026-10-20-DESCANSO-gate-pre-marko.md`.

## Em aberto (decisões do usuário)
- Padrões F48–F66 para o pipeline (`revisoes/2026-10-09-catalogo-erros-tickets-v2.md`).
- Levar às skills: erros da skill do Congo e do CCG/Alerta 2026 da Lituânia ([[correcoes]]).
- Achados fora do pedido nas specs da Ucrânia ([[Ucrania]] → Pendências).
- **Migração do brain (concluída 2026-10-27):** esta máquina e o GitHub iguais (merge com a outra máquina, pacote do pen drive restaurado, dados de clientes fora do git; branch local `backup/pre-limpeza-2026-10-27` tem dados de clientes: nunca enviar, apagar quando o usuário quiser). Outra máquina: `git pull` antes de mexer.
- **F6 Pipeline (2026-10-27):** 112 cartões (BE 40, CO 32, FR 40) ingeridos nos hubs, 9 entradas em [[correcoes]], `servicos/research-pipeline.md` e [[fronteiras]], tudo "validação humana pendente". **Usuário:** validar 2 lotes (67 risco alto + 5 sorteados) em `extracoes/2026-10-27-pipeline-*.md`. Destaques: hub BE tinha o 697,61/697,42 invertido (corrigido, C25); CO com dois decretos do SMMLV em conflito (C21) e CCG v1.4 contraditório sobre não residente (C22); FR pacote vigente = reemissão v1.0 de 06/10 promovida em 09/10. Pendentes: origem do `CO-compliance/colombia-artifacts-20261026-1016.zip`; `~/mercans-pipeline` sem remote (só ler).

## Ao abrir a próxima sessão
1. Ler este arquivo e o fim de [[log]].
2. Frentes 1–5: abrir com `scripts/abrir_frentes.ps1` (cada janela abre na sua pasta `frentes/<frente>/` e lê o seu `estado.md`).

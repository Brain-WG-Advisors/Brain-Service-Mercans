# Onde paramos

> Atualizado em 2026-10-26 (fim da sessão [[sessoes/2026-10-26]]; demais blocos sem mudança desde 2026-10-20). Reescrever a cada "fecha a sessão". Ler ao abrir a sessão.

## Colômbia PMI — pesquisa concluída (2026-10-26)
- Encerrada em 26/10: artefatos finais no Drive/Monday (7 specs v1.0, CCG v1.4, WTC v1.6, DD v1.3, SIR v1.1); delta ao design e e-mail de encerramento enviados pelo usuário; registros no chat "Research Pipeline II". Resumo: [[sessoes/2026-10-26]]; planilha `co-report-crosscheck/04-output/CONFIRMACAO-PROCESSOS-CO-2026-10-26.xlsx`.
- A confirmar: janela Suporte gravou CT-4593 (links novos) e SR-470 (rótulo SIR v1.1)? (pedido com ok do usuário em 26/10).
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
- **Migração do brain (2026-10-26, janela geral):** estado desta máquina registrado em commit **local** (inventário em [[inventarios/pipeline]]; memória do Claude do pipeline copiada para `raw/memoria-claude-code/mercans-pipeline/`). **Push bloqueado:** o commit `3810473` (não enviado) e as pastas novas de `internal-certification/` (Mammoet, Altium, KZ) trazem planilhas de folha de clientes (`01 Received/`, `_extracted/`) — regra: dado de cliente não sai da máquina. Decidir: tirar esses arquivos do histórico (via `.gitignore` + reescrever os commits locais) antes do push. O `MIGRACAO.md`, o `modelos/inventario.md` e a decisão 0.7/F6 do `PLANO.md` não existem neste clone (conferir no `origin/main` com `git fetch`). Pendentes: o zip `CO-compliance/colombia-artifacts-20261026-1016.zip` (origem?) e o repo `~/mercans-pipeline`, que não tem remote e tem 13 alterações sem commit em `dist/v2.12/`.

## Ao abrir a próxima sessão
1. Ler este arquivo e o fim de [[log]].
2. Frentes 1–5: abrir com `scripts/abrir_frentes.ps1` (cada janela abre na sua pasta `frentes/<frente>/` e lê o seu `estado.md`).

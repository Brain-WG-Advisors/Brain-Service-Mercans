# Estado — frente validacaoco

> Escrito só pela janela desta frente. Criado em 2026-10-29 pela janela geral; reescrever a cada "fecha a sessão".

## Em andamento
- 2026-10-29: sessão aberta. Passo 1 (método da França lido: `CLAUDE.md`, `HANDOFF.md`, `docs/test-plan.md`, `docs/runbook.md`) apresentado ao usuário.
- **Esperando o usuário:** escolha do oráculo (passo 2). Recomendação: oráculo próprio montado da lei (Python, parâmetros com fonte) + saída real do provedor da PMI (NE de setembro, mascarada) como "motor de terceiro"; calculadoras oficiais só para conferência pontual.
- 2026-10-29 (tarde): proposta completa gravada em `Research Pipeline/Colombia/2026-10-29-validacao-research/PROPOSTA.md` + `CONFERENCIA.md` (método aplicável, oráculos A–F, suíte ~60 casos). **Esperando o usuário:** ok em oráculo A+B, suíte + cobertura por artefato (§4), habilitação DIAN fora (G7) e fechar os 6 pontos abertos antes de rodar (§5). Se não responder: A+B.

- 2026-10-29: usuário deixou o agente escolher o motor de terceiro; pergunta se dá sem cadastro com e-mail. Resposta: sim, fase 1 sem e-mail (oráculo + calculadoras públicas + XSD + folha PMI mascarada); trial Aleluya só como fase 2, com ok dele.

- 2026-10-29: revisão aplicada em DRAFTs COVAL (revisao/, MD5-DRAFTS.txt). Espera o usuário: ok para promover (Drive: importar specs no .gsheet; WTC/CCG/DD versão nova; colar redline do SIR) e decisões dos itens não aplicados/prováveis; envio da MENSAGEM-MANJU-DRAFT.

- 2026-10-30: usuário APROVOU o plano de simulações e o uso da folha real de setembro (PMI, mascarada) como comparação (Test 4 / oráculo B). Feito: `test4-folha-setembro/RELATORIO-TEST4.md`; espera decisão do usuário sobre o 114-1 (só salarial × devengado) e o integral × Ley 1393.

- 2026-10-30: pesquisa oficial dos pendentes concluída → `pesquisa-2026-10-30/TABELA-CONSOLIDADA.md` (46 mudam, 5 nota, 2 abertos com posição provisória). Rodada 4 aplicada e conferida (DRAFTs COVAL, oráculo v2). **Espera o usuário:** ok para promover ao Drive (specs no .gsheet; WTC/CCG/DD versão nova; colar redline do SIR) e envio da mensagem à Manju. Resíduos: Circular 101/2025 revogada citada ~20x no CCG; layout Form 350 A92; aviso ao BAU sobre erros do provedor (114-1, 25%, art. 64).

- 2026-10-30: usuário mandou fazer o fechamento no modelo da França, passos 1–7 (baseline, finais limpos, Test 0, conferência da entrega, pacote de simulações, pacote de Design, skill). Passo 8 (promoção ao pipeline) e Drive: só com ok. Saída: `Research Pipeline/Colombia/2026-10-29-validacao-research/final/`.

- 2026-10-30 (fim): fechamento passos 1–7 CONCLUÍDO em `final/` (baseline, finais limpos + cross-check PASS, Test 0 + resíduos + consistência, simulações, design, skill .zip). **Espera o usuário:** ok para passo 8 (promoção ao ~/mercans-pipeline com Archived/ + log) e Drive (specs no .gsheet; WTC/CCG/DD versão nova; colar SIR); envio da mensagem à Manju; aviso ao BAU sobre erros do provedor. Aberto sem fonte: rateio 1/12 dos tetos 790/1.340 UVT.

- 2026-11-02: usuário mandou começar a pesquisa dos resíduos "antes que entreguemos algo errado ao BAU". Rodada em `pesquisa-2026-11-02/` (3 lotes: retenção, seguridade/PILA, prestações/NE/SIR/WTC). Pipeline/Drive/mensagens continuam esperando o "pode".
- 2026-11-02: rodada 5 pesquisada → `pesquisa-2026-11-02/TABELA-RODADA5.md` (8 mudanças + linha 346; 2 erros que iriam ao BAU: 1/12 dos tetos UVT e retenção de cesantías de não residente). Aplicando em DRAFT-R5 (`revisao/rodada5/`), finais aprovados intocados. Usuário quer apresentar ao BAU para validação; proposta: pacote + mensagem à Heidy (PMI Review) depois do Drive. Espera: ok para os DRAFT-R5 virarem finais, "pode" Drive, ok do formato do pacote BAU.

- 2026-11-02 (tarde): FINALIZADO localmente (release v1.6/1.8/1.5, specs v1.2, Payslip v1.3, SIR v1.3; cross-check PASS; simulações V1.1 PASS × oráculo; skill zip 4e5db61c…; design v1_2). Copiados ao Drive (md5 OK em 16 arquivos): WTC/DD/CCG versão nova, Payslip v1.3 (antigo → 18/Archived), specs xlsx _v1.2 em 17, simulações em 11, design v1_2 (v1_1 de 5/10 → 07/Archived). Falta: importar as 5 specs nos .gsheet e aplicar o SIR v1.3 no Google Doc (Chrome); rascunho Gmail esperando ok do usuário na janela Gmail; depois avisar o usuário para enviar.

## Instruções vigentes
- 02/11 (sequência de fechamento, decidida pelo usuário): (1) finalizar — rodada 5 aplicada e conferida vira os finais; (2) eu deixo em RASCUNHO o e-mail aos responsáveis (BAU/Heidy); (3) eu subo os arquivos ao Drive (ok dado para esta subida); (4) aviso o usuário; ele envia o e-mail só depois da subida ao Drive. Nunca enviar o e-mail.
- Sem criar conta com e-mail em serviço externo sem ok do usuário (29/10).
- Não mandar resumos à janela geral (painel lê sozinho); SendMessage à brain-service-5b só para pedir commit ou coordenação entre frentes (29/10).
- 2026-10-29: usuário confirmou: research CO NÃO está em produção (P1) → correção = nova versão, sem ticket ao Development; iniciação da validação aprovada (v0.3, F1 começa).
- Google (Drive/Docs/Sheets) só pelo Claude in Chrome; nunca o MCP do Google (29/10).
- Entre os gates GA/GB/GC: aplicar a opção recomendada e registrar no CONFERENCIA.md (aprovado 29/10). Continua pedindo ok: GA, GB, GC, Drive, ticket, e-mail, conta externa, apagar.
- 29/10: "faça tudo e só me apresente o resultado final em tabela: como está → o que pode mudar". Rodar F1–F4 sem paradas intermediárias; não alterar artefatos nem Drive; entregar só a tabela comparativa (proposta).
- 30/10: "tem o suficiente para pesquisas profundas em fontes oficiais e encontrar as decisões": ponto estatutário aberto → pesquisar até a fonte primária e decidir com fonte + confiança; ao usuário só decisão de negócio/escopo e os gates de envio/Drive.

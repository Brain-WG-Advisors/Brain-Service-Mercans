# Estado — frente chade

> Escrito só pela janela desta frente. Reescrito em 2026-10-30 ("fecha a sessão", [[sessoes/2026-10-30-chade]]).

## Em andamento
- **Teste do design no HRBlizz de aceite**: empresa "Mercans Chad - Compliance Testing" (REF-LE-04-422, COM-TD-0001, 0 empregados); tax year Chad 2026 (id 472). O System Settings dá erro 526 (SSL do lado do HRBlizz) depois do SSO.
  - 🔄 30/10: o usuário mandou o pedido ao **Ram Sakthi**, que é quem cuida do Chade (a Suman disse isso em 21/10; ela não respondeu a mensagem de 29/10). Pedido: export atual td_2026, erro 526, teste do nosso design na entidade. **Aguardando o Ram.**
  - Entrega: `Research Pipeline/Chad/2026-10-29-teste-design-hrblizz/` (PACOTE-CONTEXTO.md, rascunho-msg-suman.md).
- **Design v4** pronto só no computador: `Research Pipeline/Chad/2026-10-29-design-v4/` (10 cenários = v3, preflight OK). Decisão do usuário (29/10): Drive e teste no motor só depois da resposta do Dev.

## Coletado
- ✅ 30/10: conversa "Mercans payroll knowledge base overview IV" baixada para `raw/chats/conversas/2026-10-16-design-dev-kb-mercans-payroll-kb-overview-IV.md` (ramo atual: 333 mensagens, de 06/09 a 16/10; trecho do design: [263]–[333], linha 12823 em diante). Próximo passo: extrair cartões.

## Achados da preparação (não gravados no hub ainda)
- Nosso design vigente é o **v3** (`Chad/07-design/chad-design/`), não o "clean-room v1.0 de 24 artigos" que o hub cita. Atualizar o hub.
- O v3 contradiz a skill em 2 pontos, a resolver pela lei: TFE/TAFP na base ampla do Art. 189 (pela skill, segue a base do IRPP) e base NR 18% líquida das isenções do Art. 45 (pela skill, sem o Art. 45).
- `07-design/td.json` = export de 31 regs do Dev de 2026-07-02 (CT-A-580). É o "antes" para ver o que o Dev mudou.

## Passos 1–5 (30/10)
- Lei: `.../2026-10-30-export-ram/LEI-VEREDITOS.md` — 12 de 34 temas resolvidos pela lei (nosso certo em 9, Dev em 5); 4 ambíguos; 18 sem fonte (CGI consolidado no dgi.td exige CAPTCHA → usuário baixa; WTC V3.0 só em gsheet → usuário exporta xlsx).
- Simulação: `.../simulacao/RESULTADO.md` — 3 de 10 cenários batem.
- Correção: Art. 45-4° TEM teto 5.000/filho/mês (LF 2026 p.15) → v4 precisa voltar o teto; registrado em correcoes.md e hub.
- ⏳ Usuário: enviar 4 mensagens ao Ram (526, empregados de teste, troca de contas CNPS); baixar CGI no dgi.td; exportar WTC V3.0.

- 01/11: CGI 2026 + WTC V3.0 baixados; revisão no LEI-VEREDITOS.md: v4 16/23 (70%), Dev 10/23; lista de melhorias ao v4 pronta. Próximo: aplicar as melhorias no v5 (local) com ok do usuário; achar Lei CNPS 7/66 e decretos.

- 01/11: **design v5** em `Research Pipeline/Chad/2026-11-01-design-v5/` (local): 12/12 cenários e 20/20 extras exatos; QA independente PASS na rodada 3 (`QA-REVIEW.md`). Apresentação (inglês, 6 slides): https://claude.ai/artifact/K2HRBveV4KBfsVN1LN9Zas (privada).
- ⏳ Usuário: ok nas decisões técnicas D1 (transporte fora da CNPS, guia p. 8) e D2 (62867 tributável); depois corrigir `correcoes.md` 07/07 (transporte). Drive só com ordem.

- 02/11: planilha de comparação v5 × Dev (modelo BH/TD do projeto Design & Development KB): `Research Pipeline/Chad/2026-11-02-planilha-comparacao/TD_Design_Comparison_v5_vs_Dev.xlsx` (7 abas; semelhança 70%; lei: v5 34/34, Dev 13/34; 31 perguntas, 12 ★). Modelos em `modelos/`.

- 02/11: **design v6** (`Research Pipeline/Chad/2026-11-02-design-v6/`): forma do Dev onde a lei não obriga diferença; QA PASS r3. Corrigiu defeitos de matriz que o v5 também tem (6552%, 6261x, 62651–3, 6561x/6566x na TF/TA). Planilha `2026-11-02-planilha-comparacao/TD_Design_Comparison_v4_v5_v6_vs_Dev.xlsx` (geral 68|65|80%; ponderada pela lei 57|89|89%, Dev 36%). Apresentação de 01/11 está desatualizada (fala do v5).
- ⏳ Usuário: ok em D1 (transporte fora CNPS), D2 (62867 tributável), A20 (indenização na TF, inverte correcoes 07/07), A34 (operário <35).

- 02/11 16:11 UTC: System Settings (`system.acceptance.k8s.hrblizz.dev`) **continua com erro 526** (Cloudflare Ray ID a5446a128fd42fa2). Backoffice OK (entidade REF-LE-04-422 visível). Pedido ao Ram **enviado 02/11** pelo Google Chat (6 mensagens, com ok do usuário): carregar nossas regras como conjunto separado (tax year de teste) ligado só à entidade de teste + erro 526. Ram respondeu 03/11 02:38: "send the file to Mohit he will load the regulations". ✅ v6 no formato do Dev pronta (9 .md, roundtrip 12/12 + 26/26 idêntico; 6 itens não representáveis na CONFERENCIA, incl. campos DD/entidade e códigos WTC novos que não existem no HRBlizz) — **enviada 03/11 ao Mohit** no chat "Cross Training - Design Creation - Oct 16" (4 mensagens + `TD-Chad-v6-test-set.zip`, md5 51881863…, 9 .md; spec com seção "Prerequisites not yet in the system"), com ok do usuário. 🔄 Aguardando o Mohit carregar. em `Research Pipeline/Chad/2026-11-03-v6-formato-dev/`; envio ao Mohit só com ok do usuário. Ram perguntou também (03/11 04:20) se houve mudança na research da Colômbia: fora desta frente.

## Fora desta frente
- O Ram cobrou em 29/10 a atualização da skill da Colômbia (CCG v1.4 etc.). O usuário respondeu "ok". É assunto da janela geral ou da frente que cuida da Colômbia.

## Instruções vigentes
- **02/11 (usuário): escrita liberada só na entidade de teste "Mercans Chad - Compliance Testing" (aceite)** — empregados de teste e folha de teste. **Não mexer nas regras td_2026 do Dev**: carga da v6 como conjunto separado só pelo Dev (pedir ao Ram). Fora disso, HRBlizz segue só leitura.
- **01/11 (usuário): objetivo = estudar o design do Dev × o nosso e absorver o máximo para aprimorar o nosso, feito por nós com IA.** Não precisamos de entidade de teste, formulário (Suman/Jasper), empregados de teste nem correção do 526. Passos 3 (no sistema) e 4 descartados; a simulação local substitui.
- HRBlizz só leitura, ambiente de teste; nunca digitar senha nem salvar, aprovar ou alterar.
- Não mandar resumos à brain-service-5b; SendMessage só para commit ou coordenação entre frentes.
- Contato do Dev para o Chade: **Ram Sakthi**.
- Respostas ao usuário muito objetivas. Mensagens a terceiros: uma frase por parágrafo (o usuário envia uma por uma).

# Serviço — Análise de Reports (Internal Certification)

> Frente 5 de [[rotinas]]. Estado e pacotes: `frentes/certificacao/estado.md`. Pasta de trabalho: `C:\Users\instituto\Documents\internal-certification` (o `CLAUDE.md` e o `PLANO_DE_ACAO_VALIDACOES.md` de lá mandam no detalhe).
> Índice: [[00-INDEX]] · Fora do escopo: [[fronteiras]]

## O que recebemos (entradas)
- Pacote do último período fechado de um cliente por país, enviado pela **Primary SBC** (board monday 2072701698 "BAU Master Client List"): statutory report(s) como enviados + recibo da autoridade, G2N, contracheques, GL, arquivo bancário, master data (+ report anterior se houver correção).
- Canal: Google Chat ou Gmail (coletado pelas janelas [[rotinas]] 2/3 ou pela própria frente via Chrome), salvo em `<País>/<Cliente> - <AAAA-MM>/01 Received/` sem renomear, com `received.txt` (quem, canal, data, bytes, sha256).

## O que entregamos (saídas)
- Workbook `<CC>_<Cliente>_<AAAA-MM>_Validation.xlsx` em `02 Validation`: Cover, Executive Summary (qualificado, nunca "tudo correto"), Assumptions, Findings Register, Coverage, Reconciliation, Recalculation, Not Tested, Sources.
- Severidade única: High / Medium / Low / Observation. Todo controle termina em Pass, Finding, Not tested (com motivo e o que destrava) ou Out of scope.
- Resumo EN para implementation, resumo PT para o usuário, cobranças às SBCs em rascunho (`followups.md`).
- Holanda: Audit Report no modelo `Mammoet_P09-P13_Audit_Report.docx` (decisão D-04, 2026-10-14).
- Painel consolidado: [[internal-certification/Acompanhamento_Internal_Certification.xlsx|Acompanhamento_Internal_Certification.xlsx]].
- [[internal-certification/PLANO_DE_ACAO_VALIDACOES|PLANO_DE_ACAO_VALIDACOES]]: Plano de ação das validações por país (base: Holanda, set/2026): método e etapas
- [[internal-certification/PROMPT_VALIDACOES_PONTA_A_PONTA|PROMPT_VALIDACOES_PONTA_A_PONTA]]: Prompt de validação ponta a ponta da Internal Certification para os pacotes do escopo

## Como sabemos que ficou certo (qualidade)
- 8 etapas (PLANO §1): intake → base legal oficial em vigor (URL, versão, data, sha256 em `references/<país>/<ano>/`) → decisões de método com o usuário → leitores por cliente → recálculo de 100% dos empregados → amarrações report/G2N/contracheque/banco/GL/master → revisão de toda exceção na fonte → entrega.
- O contracheque é a âncora; dois arquivos concordarem não prova nada.
- Conferir que o recibo é **do mesmo report** (nº do empregador, IRmark, kenmerk, protocolo).

## Lições (o que já deu errado)
- Recibo de outra entidade no pacote: Sherwin NL (outro LH), Suécia (Kvittens da Quest Software AB num pacote da One Identity).
- ~40% das exceções automáticas da Holanda eram falsos positivos do script: mapear colunas lendo o arquivo do cliente.
- Tabelas em PDF: ler por posição (pdfplumber) e conferir contagem de linhas.
- Travas de execução (PLANO §4.1): senha nunca em comando; não alterar registro do Windows; testar o navegador com servidor 127.0.0.1 antes de usar o Chrome; scripts em arquivo, não heredoc; caminhos < 260 caracteres.
- Os achados recorrentes estão na **configuração dos itens de folha** (marcação fiscal/report), não no motor de cálculo.
- [[rascunhos/2026-10-16-credenciais-internal-certification|2026-10-16-credenciais-internal-certification]]: Varredura de credenciais em internal-certification/ (só estrutura; nenhum valor copiado)

## Padrões de achado por país
- Ver a seção "Internal Certification" de cada hub: [[Holanda]], [[Noruega]], [[Dinamarca]], [[Suecia]], [[Reino-Unido]], [[Ucrania]], [[Finlandia]], [[Estonia]], [[Irlanda]]. Cazaquistão, Azerbaijão e Rússia ainda sem hub (só no `estado.md` da frente).

## Método e ferramentas
- [[internal-certification/CLAUDE|CLAUDE da pasta internal-certification]]: contexto da pasta, ligação com a frente Certificação, regras e organização
- [[internal-certification/Netherlands/_tool/skill-references/control-register|control-register]]: Registro de controles: lista enumerada de checagens rodadas em toda validação NL
- [[internal-certification/Netherlands/_tool/skill-references/cross-document-reconciliation|cross-document-reconciliation]]: Metodologia de reconciliação entre documentos (ordem dos passos) da validação NL
- [[internal-certification/Netherlands/_tool/skill-references/systematiek-determination|systematiek-determination]]: Portão de determinação loon-in x loon-over antes dos testes de integridade do período NL

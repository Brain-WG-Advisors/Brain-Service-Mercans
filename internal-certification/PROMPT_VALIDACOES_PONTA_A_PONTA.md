# Prompt — Internal Certification: validações de ponta a ponta

> Como usar: abra uma **conversa nova** no Claude Code com a pasta `Documents\internal-certification` aberta, cole tudo o que está abaixo da linha e envie. Para rodar só um país, troque a lista da seção "Escopo desta rodada".

---

Você vai conduzir a Internal Certification dos statutory reports do HRBLIZZ (Mercans), do início ao fim, para os pacotes listados no escopo. Fale comigo (Wallisson) em português do Brasil; tudo o que for para colegas (workbook, resumo, follow-ups) vai em inglês.

## 0. Leia antes de qualquer ação
1. `CLAUDE.md` desta pasta (contexto, contatos, regras).
2. `PLANO_DE_ACAO_VALIDACOES.md` — **o método em 8 etapas, as decisões já tomadas (§4) e as regras de execução (§4.1)**. Elas valem como instrução minha.
3. A validação de referência: `Netherlands/<cliente> - 2026-09/02 Validation/` (workbooks, `_evidence/checks.json`, `review/curated.py`) e a ferramenta `Netherlands/_tool/` (nl_check.py, nl_stage2.py, clients.py, build_workbook.py). Reaproveite a estrutura; não reinvente.
4. O `received.txt` de cada pacote do escopo.

## 1. Escopo desta rodada (em ordem)
1. `Norway/Henkel Norway - 2026-09`
2. `Denmark/Sherwin Williams Denmark - 2026-09`
3. `Denmark/KGS Fire & Security Denmark - 2026-09` (banco = Out of scope)
4. `Sweden/Quest Software - 2026-09` → validar **One Identity Sweden AB (559400-9267)**; recibo, master e banco = Not tested
5. `Kazakhstan/Mastercard - 2026-10` → recálculo × G2N × ordens de pagamento × banco; report trimestral, GL e master = Not tested
Fora desta rodada: Azerbaijão (pulado), Finlândia, Estônia, Irlanda, Rússia (sem arquivos). Holanda, Reino Unido e Ucrânia já estão validados (`.done/validated`): não refazer.

## 2. Regras que não se negociam
- **Nunca** alterar nada em `01 Received`. Trabalhar só em `02 Validation/`, `validators/<cc>/` e `references/<país>/<ano>/`.
- **Nunca** enviar mensagem, e-mail ou arquivo. Cobranças são rascunhos em `02 Validation/followups.md`.
- **Sem amostragem:** toda checagem em 100% dos registros. Áreas limpas aparecem como linhas de Coverage.
- **Só fonte oficial primária, na versão em vigor no período** (autoridade fiscal/previdenciária do país). Baixar o documento; registrar URL, versão, data de publicação, data de leitura e sha256 em `references/<país>/<ano>/sources.md`. Skill `payroll-compliance-<país>` é mapa, não fonte. Valor sem fonte → a checagem vira Not tested.
- **O contracheque é a âncora.** Dois arquivos concordarem não prova nada. Nunca julgar um campo usando outro campo que também está sob teste.
- **Toda exceção automática é lida na fonte** antes de virar achado. Falso positivo fica em Coverage como "Pass (reviewed)" com o motivo.
- Severidade: **High** (valor retido/declarado errado, ou sem prova de aceite do report), **Medium** (campo do report ou documento ao cliente errado sem mover dinheiro), **Low** (apresentação ou arredondamento ≤ 0,10), **Observation** (precisa de confirmação do cliente).
- Inferência é marcada como inferência. Na dúvida sobre método, **pare e me pergunte** (ex.: sistemática de retroativo, regra de coluna por idade, tratamento de skattekort).
- Dados de empregados não saem desta máquina; nada vai para serviços externos ou portais de teste da autoridade.

## 3. Regras de execução (para não travar)
- Nunca colocar senha/segredo em comando. Arquivo protegido por senha → pular e me avisar.
- Nunca alterar registro do Windows ou configurações do sistema.
- Scripts Python: escrever com a ferramenta Write e executar o arquivo (nada de heredoc com aspas/`\b`). Usar um venv próprio (pandas, openpyxl, xlrd, pdfplumber, lxml, dbfread); `pdftotext` para contracheques.
- Extrair arquivos em `02 Validation/_extracted/` com caminhos curtos; checar caminhos > 240 caracteres.
- Tabelas oficiais em PDF: ler por posição de palavra (pdfplumber) e **conferir a contagem de linhas/degraus** antes de usar.
- Navegador (só se precisar baixar algo): `list_connected_browsers` e teste com servidor local em 127.0.0.1 para confirmar que é o Chrome **deste PC**; nunca usar outro aparelho.

## 4. Para cada pacote, execute as 8 etapas
**Etapa 0 — Intake.** Inventariar `01 Received` (tamanho, sha256), extrair para `_extracted`, identificar entidade (nº do empregador), período, frequência, moeda e headcount **a partir dos próprios documentos**. Conferir se o recibo da autoridade é do mesmo report (nº do empregador, ID/protocolo da mensagem, período). Escrever `02 Validation/intake.md`.

**Etapa 1 — Base legal.** Montar `references/<país>/2026/` com: especificação do report (XSD/campos/códigos) e regras de consistência publicadas; tabelas/fórmulas de imposto; alíquotas, bases, tetos, isenções e regras de arredondamento das contribuições; prazos. Cada item termina como valor com fonte, NOT LOCATED, OUT OF SCOPE ou N/A.
- Noruega: A-melding (XSD/veiledning Skatteetaten), tilbakemelding, forskuddstrekk, arbeidsgiveravgift por zona, feriepenger, OTP.
- Dinamarca: eIndkomst (feltnumre, Skattestyrelsen), AM-bidrag, A-skat via skattekort (trækprocent + fradrag), ATP, feriepenge.
- Suécia: AGI (XSD/fältlista Skatteverket 2026 — há cópia em `.claude/skills/payroll-compliance-sweden/_sources`, reconfirmar versão), skattetabeller 2026, arbetsgivaravgifter.
- Cazaquistão: legislação tributária e de contribuições **em vigor em 2026** (verificar se há novo Código Tributário a partir de 2026): ИПН, ОПВ, ОПВР, СО, СН, ВОСМС/ООСМС, e o formulário trimestral (ex.: 200.00).

**Etapa 2 — Decisões de método.** Registrar em Assumptions as decisões do §4 do plano. Qualquer decisão nova que mude o resultado: perguntar antes de testar.

**Etapa 3 — Leitores.** Criar `validators/<cc>/` reaproveitando o padrão da Holanda: `clients.py` com o mapeamento **lido do arquivo do cliente** (colunas do G2N → campos do report; template do contracheque; colunas do GL), leitor do report, do G2N, dos contracheques, do GL e do banco. Conferir totais lidos com os rodapés/totais impressos.

**Etapa 4 — Recálculo estatutário.** Imposto e contribuições de cada empregado com as tabelas/alíquotas oficiais e as regras de idade, teto, base e arredondamento do país.

**Etapa 5 — Amarrações.** Report ↔ G2N ↔ contracheque ↔ banco ↔ payment report ↔ GL ↔ master, por empregado e no total; GL débito = crédito; passivo de impostos/contribuições no GL = report; população igual em todos os documentos (explicar cada diferença). Retroativos: conciliar conforme a sistemática do país (e me perguntar se não estiver clara).

**Etapa 6 — Revisão.** Ler cada exceção na fonte. Escrever `02 Validation/review/curated.py` (achados finais + override de cada exceção automática + Not tested + reconciliações extras), no formato de `Netherlands/<cliente> - 2026-09/02 Validation/review/curated.py`.

**Etapa 7 — Entrega.**
- Workbook `02 Validation/<CC>_<Cliente>_<AAAA-MM>_Validation.xlsx` com as abas: Cover, Executive Summary (qualificado — nunca "tudo correto"), Assumptions, Findings Register (ID, Severity, Area, Finding, Evidence, Impact, Statutory basis, Status, Records), Coverage, Reconciliation, Recalculation (por empregado), Not Tested (motivo + o que destrava), Sources. Nunca sobrescrever versão existente (nova versão = v1.1).
- `02 Validation/summary_EN.md` (para implementation, sem instrução de configuração) e `02 Validation/resumo_PT.md` (5–10 linhas para mim).
- `02 Validation/followups.md` com rascunhos em inglês do que falta pedir.
- Criar `02 Validation/.done/validated` com data e nome do workbook.
- Acrescentar uma linha em `C:\Users\instituto\Documents\brain-service\log.md` (país, cliente, período, achados High/Medium, pendências).

**Critério de pronto:** entidade/período/recibo conferidos; fontes oficiais com versão em Sources; decisões em Assumptions; recálculo em 100%; amarrações feitas ou Not tested com motivo; toda exceção revisada; entregas gravadas; cérebro atualizado.

## 5. Ao final de cada país e da rodada
Me reporte em português: veredito por pacote, contagem de checks por estado, achados High e Medium (uma linha cada, com o valor), o que ficou Not tested e o que precisa ser pedido. Depois de todos os pacotes, atualize a tabela de status do `PLANO_DE_ACAO_VALIDACOES.md` (§2) e me diga qual é o próximo passo recomendado.

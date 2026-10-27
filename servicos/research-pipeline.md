# Serviço 1 — Research Pipeline

> Etapa 1 do fluxo. Método detalhado: skill `mercans-pipeline-methodology` (não copiar; linkar).
> Próximo: [[design]] · Índice: [[00-INDEX]]

## O que recebemos (entradas)
- **Pedido de país novo ou de atualização**, vindo do Team Lead / liderança de Compliance, com prioridade definida (ex.: Espanha e Ucrânia na frente, demais Média; board "Country AI Validation File Board" com prioridade dada pela liderança) (chat: mercans-compliance; chat: design-dev-kb).
- **Fontes oficiais do país** (leis, autoridades, manuais de formato). Só arquivos oficiais; cópia de terceiros precisa ser declarada como tal (chat: mercans-compliance).
- **Amostras e artefatos do cliente** (filings reais, relatórios, WTC/G2N legado), pedidos a BAU/implementação num e-mail consolidado por country owner (chat: compliance-research). Amostra real de filing prevalece sobre layout pesquisado.
- **Tickets resolvidos** que revelam drift em CCG/WTC/DD (insumo da automação drift-sync, ver [[suporte]]) (chat: compliance-research).
- **Gate de identificação do país** antes de iniciar o pipeline (skill `mercans-pipeline-methodology`).
- **PII mascarada:** dado de cliente (tax IDs, datas de nascimento, nomes) é mascarado antes de qualquer processamento por IA, manualmente até existir o pré-processador (decisão 2026-06-30, ELT) (chat: compliance-research).

## O que entregamos (saídas)
O pipeline tem 11 estágios (CCG, Scope Lock-In, Report Specs, DD, WTC, SIR, Payslip, Alignment, Audit+Fixer, QA, Skill Compiler) (chat: mercans-compliance; docs: orchestrator-handoff).

| Artefato | Formato | Padrão de nome | Observação |
|---|---|---|---|
| CCG (Country Configuration Guide / Payroll Regulation Guide) | .docx | `{CC}-CCG-{SEQ}-v{M}.{m}` | 13 módulos fixos; perguntas do template viram H3, cobertura ≥95% (check C11). Padrão-ouro: CCG da Bulgária (chat: mercans-compliance) |
| WTC (Wage Type Catalogue) | .xlsx | `{CC}-WTC-{SEQ}-v{M}.{m}` | Base CZ V2.0 + Global WTC (~300 códigos obrigatórios) + abas Global WTC Coverage e Form Reference Guide. Colunas laranja são do Dev (chat: mercans-compliance; chat: design-dev-kb) |
| DD (Data Dictionary) | .xlsx | `{CC}-DD-{SEQ}-v{M}.{m}` | Formato CZ V2.0, 8 abas; só as colunas azuis (4472C4) são nossas. Só master data de input do usuário, só setor privado (chat: mercans-compliance) |
| Report Specs | .xlsx | `{CC}-{AUTORIDADE}-{SEQ}` (ex.: ES-AFI-001, CI-CNPS-001, UA-1PV-001) | Padrão Espanha de 9 abas (modelo ES-M296-001), Sheet 4 com colunas A–U. Divergência entre fontes: "10 abas / 22 colunas" vs "9 abas / 21 colunas" [INCERTO] (chat: mercans-compliance) |
| SIR (Statutory Integration Register) | índice + runbooks por integração [INCERTO: formato do arquivo] | `{CC}-SIR-INDEX-001` | Classifica o país como HAS_INTEGRATIONS / MANUAL_ONLY / NO_INTEGRATIONS; runbook de 7 fases por integração (chat: compliance-research; chat: design-dev-kb) |
| Payslip Generator | .xlsx | `{CC}-PSL-{SEQ}` | 5 abas (EN / local / Payslip Spec / Unit Rate Details / Population Range), "mesmo modelo da Espanha" vale para o Payslip Spec 1 (chat: mercans-compliance) |
| Skill `payroll-compliance-<país>` | SKILL.md + `references/` | `payroll-compliance-{país}` | Router fino + um .md por artefato (padrão Chile/Canadá); description ≤1.024 caracteres (chat: mercans-compliance) |

- **Versionamento:** `{CC}-{TYPE}-{SEQ}-v{MAJOR}.{MINOR}[-DRAFT-{TICKET}-{AAAA-MM-DD}].ext`. Na aprovação, tirar o bloco DRAFT e arquivar a final anterior em `Archived/`; deve haver exatamente uma final vigente por artefato. Toda edição atualiza o Version Control (uma frase por edição). **Version Control (decidido em 2026-10-15):** uma linha por versão, número em sequência (x.y, nunca repetir o mesmo número em entregas diferentes), data como data (`d-mmm-yy`, não texto), descrição de no máximo 2 linhas no formato "ticket: o que mudou (onde)"; justificativa e fonte vão no ticket e no hub, não no VC. O nome da planilha acompanha a maior versão (ex.: DD ES renomeado V4.0 → V4.9). Nas specs AFI da Espanha o nome do arquivo ficou fixo e a versão evolui só no VC (chat: mercans-compliance).
- **Drive "Compliance Team":** pasta por país com subpastas 01–16 (CCG em `05 - Payroll Regulation Guide`, WTC em `03 - WTC`, DD em `02 - DD`, Report Specs em `12 - Country Report Codes`) (chat: mercans-compliance).
- **Status "Submitted for design"** no Monday marca o que passou da pesquisa para o [[design]] (decisão 2026-06-30, Manju) (chat: compliance-research).

## Como sabemos que ficou certo (qualidade)
- **Fonte primária alcançada diretamente**; duas fontes secundárias concordando não bastam; esquema/taxa/template copiado de outro artefato não é fonte primária. Piso de 95% de precisão (a reunião de 30/06 falava em ~90% hoje) (chat: mercans-compliance; chat: compliance-research).
- **Audit mecânico C1–C22 + fixer** (Stage 9) com override justificado de falso positivo (C20 dá FAIL como falso positivo confirmado em todos os países) e **QA cross-check** (Stage 10), ex.: FR em 87/100 "NEEDS PATCHES" (chat: mercans-compliance; chat: design-dev-kb).
- **Consistência entre artefatos:** CCG × WTC × DD × Report Specs devem concordar (alignment patch DD × Specs no FR: 26/26 asserções) (chat: design-dev-kb).
- **Validação contra amostra real** (ex.: A3 na Espanha) antes e depois do deploy das specs (tickets: ES-A).
- **Edição de xlsx:** patch cirúrgico no XML (nunca round-trip openpyxl em arquivo com desenhos); checar well-formedness, desenhos byte-idênticos e diff célula a célula; verificação visual antes de entregar (chat: mercans-compliance).
- **Confiança declarada** antes de enviar; "tem certeza?" / "100%?" = reverificar do zero (chat: mercans-compliance).
- **Humano no loop:** a automação nunca edita artefato vivo; gera tracked change/rascunho e preserva o original (chat: compliance-research).
- Método completo nas skills `mercans-pipeline-methodology` e `mercans-compliance-workflow`.

## O que já deu errado
Erros de **processo** (erros de valor/artefato por país ficam em [[correcoes]]):
- **Erro de parsing recorrente Stage 1 → Stage 2** (v2.8) e **falso positivo do check C20**; correção não registrada [INCERTO] (chat: compliance-research; chat: mercans-compliance).
- **Edição indevida de planilha de outro time:** Claude editou Income Nature/Income Key da BA (Lily Li) sem pedido; regra desde 2026-05-23: nunca editar (chat: mercans-compliance).
- **Corrupção por ferramenta:** Excel converteu ranges de posição em datas; `delete_rows` do openpyxl corrompe xlsx com desenhos (chat: mercans-compliance).
- **Versionamento:** arquivo com nome v1.0 e conteúdo v1.1 (FR-DD); versões paralelas de spec e versão anterior apagada com outro time trabalhando nela (ver [[suporte]]) (chat: design-dev-kb; tickets: ES-A, OUT).
- **Fonte secundária errada ou desatualizada** (FR: valores de blogs; UA: blogs concordando numa resposta errada, a lei primária reverteu; UA: sample validado contra formulário já superado) (chat: design-dev-kb; chat: mercans-compliance).
- **Lente errada:** resposta com lente de consultoria fiscal em vez de fornecedor de software de folha (NL, HRBS-10545) (chat: mercans-compliance).
- **Resíduo de país anterior** em artefato novo (FR com "Description (NL)"; CCG com IDs de série da Bélgica) (chat: design-dev-kb).
- **Pendência de processo (OD-13):** ticket HRBS- de Compliance Support edita artefato direto ou escala para CT-? Sem decisão da liderança (chat: mercans-compliance).
- **Segurança:** chave da Anthropic API exposta; rotacionar no Passbolt [INCERTO onde ocorreu] (chat: compliance-research).
- **Qualidade de IA:** a IA erra ou omite ~15% em pesquisa estatutária (TR e HU precisaram de retrabalho); payslip de Turkey reprovado por não mostrar bruto e líquido por elemento (chat: design-dev-kb; chat: compliance-research).

**Referência de automação (orquestrador):** ver `raw/docs/2026-09-10-orchestrator-skill-gemini.md`, `raw/docs/2026-09-11-orchestrator-handoff.md` e `raw/docs/2026-09-11-setup-shared.md` (PoC de state-machine para o pipeline; não faz parte do serviço entregue).

## Países
[[Africa-do-Sul]] · [[Alemanha]] · [[Australia]] · [[Bahrein]] · [[Belarus]] · [[Belgica]] · [[Botsuana]] · [[Bulgaria]] · [[Canada]] · [[Chade]] · [[Chile]] · [[China]] · [[Chipre]] · [[Colombia]] · [[Congo]] · [[Costa-Rica]] · [[Costa-do-Marfim]] · [[Dinamarca]] · [[Egito]] · [[Espanha]] · [[Estonia]] · [[Filipinas]] · [[Finlandia]] · [[Franca]] · [[Gabao]] · [[Guine-Equatorial]] · [[Holanda]] · [[Hungria]] · [[India]] · [[Indonesia]] · [[Irlanda]] · [[Kuwait]] · [[Libano]] · [[Lituania]] · [[Malasia]] · [[Marrocos]] · [[Mocambique]] · [[Namibia]] · [[Noruega]] · [[Portugal]] · [[RD-Congo]] · [[Reino-Unido]] · [[Romenia]] · [[Singapura]] · [[Suecia]] · [[Tailandia]] · [[Tchequia]] · [[Ucrania]] · [[Vietna]]

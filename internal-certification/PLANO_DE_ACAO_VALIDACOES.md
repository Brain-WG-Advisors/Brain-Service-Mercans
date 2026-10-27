# Plano de ação — validações da Internal Certification (todos os países)

Versão 1.0 · 14-10-2026 · base: a validação da Holanda (3 clientes, setembro de 2026)

Objetivo: validar, para cada país, um pacote real produzido pelo HRBLIZZ (report estatutário, G2N, contracheques, GL, arquivo bancário, dados mestre) contra a legislação em vigor e contra os próprios documentos, em 100% dos registros, e devolver os achados para implementation/dev. Validamos e reportamos; não refazemos filings nem prescrevemos configuração.

---

## 1. O método (o que fizemos na Holanda, generalizado)

Cada pacote passa pelas mesmas 8 etapas. Nenhuma etapa é pulada; o que não puder ser feito vira "Not tested" com motivo e o que destrava.

| # | Etapa | O que fazer | Saída | Lição da Holanda |
|---|---|---|---|---|
| 0 | **Intake** | Inventariar `01 Received` (hash, descompactar em `02 Validation`), identificar **entidade, período, frequência, moeda, headcount**; conferir se o recibo é **do mesmo report** (nº do empregador, protocolo, IRmark, kenmerk) | `intake.md`, `received.txt` atualizado | Recibo da Sherwin NL era de outro LH; o da Suécia é de outra entidade |
| 1 | **Base legal oficial** | Baixar da autoridade a especificação do report (XSD/campos), listas de códigos, tabelas/fórmulas de imposto, alíquotas, tetos, prazos — **na versão em vigor no período**; registrar URL, versão, data, sha256 | `references/<país>/<ano>/` + `sources.md` | Tabelas em PDF: ler por posição (pdfplumber) e conferir a contagem de linhas — o pdftotext perdeu linhas |
| 2 | **Decisões de método (gate)** | Levantar as escolhas que mudam o resultado e **pedir decisão ao Wallisson antes de testar** | Assumptions no workbook | Holanda: loon-in × loon-over. Cada país terá o seu (ver §3) |
| 3 | **Leitores (parsers)** | Ler report, G2N (mapear **por cliente** as colunas → campos do report, lendo o próprio arquivo), contracheques (template do cliente), GL, banco | Tabelas normalizadas + totais conferidos com os rodapés | Os 3 G2N da Holanda tinham layouts diferentes; contracheque em PT/EN/NL e números US/EU |
| 4 | **Recálculo estatutário** | Imposto e contribuições **por empregado** com as tabelas/alíquotas oficiais; regras de idade, tetos, bases | Tabela de recálculo por empregado | Regra de coluna AOW (idade), salário BT negativo, diferenças de centavos por fórmula × tabela |
| 5 | **Amarrações entre documentos** | Report ↔ G2N ↔ contracheque (âncora) ↔ banco ↔ payment report ↔ GL ↔ dados mestre; débito = crédito; população igual em todos | Reconciliação total e por empregado | Retroativo (loon-over) explica diferença G2N × report — conciliar no total com os saldos de correção |
| 6 | **Revisão de cada exceção** | Ler **toda** exceção automática na fonte; separar erro real de falso positivo; escrever o registro curado | `review/curated.py` (registro) | ~40% das exceções da Holanda eram falsos positivos do script (mapeamento, regra mal aplicada) |
| 7 | **Entrega** | Workbook (Cover, Executive Summary qualificado, Assumptions, Findings Register, Coverage, Reconciliation, Recalculation, Not Tested, Sources) + resumo EN + resumo PT; cobranças em rascunho | `<CC>_<Cliente>_<AAAA-MM>_Validation.xlsx` | Severidade única: High / Medium / Low / Observation |

**Regras fixas:** fonte primária oficial em vigor; sem amostragem; o contracheque é a âncora; dois arquivos concordarem não prova nada; nada é enviado sem "aprovado"; dados de empregados não saem desta máquina.

**Ferramenta:** reaproveitar a estrutura da Holanda (`Netherlands/_tool`, skill nl-payroll-validator v1.5): um `clients.py` por país (mapeamento por cliente), um verificador estatutário por país (`validators/<cc>/`), as amarrações genéricas (G2N, contracheque, SEPA/banco, GL, master) e o mesmo gerador de workbook.

---

## 2. Situação dos pacotes (14-10-2026, atualizado ao fim da rodada NO/DK/SE/KZ)

| País | Pacote | Status | Próximo passo |
|---|---|---|---|
| Holanda | Excerpta, Quest, Sherwin — set/26 | ✅ Validação completa 14/10 (v1.1, ~93%) + Audit Report no modelo Mammoet | Restam 5 itens/pacote que dependem de documento (Digipoort, Whk, originais, contracheques de agosto, WKR/Jaarloon BT/AOK) — rascunhos em followups.md |
| Reino Unido | McDermott UK — set/26 | ✅ Validado | 2º cliente (Christina) opcional |
| Ucrânia | Altium — ago/26 e set/26 | ✅ Validados | Recibo do 1-PV; D1 de julho |
| Noruega | Henkel Norway AS — set/26 | ✅ Validado 14/10 (qualificado; 1 High: fagforeningskontingent fora da base do trekk/fradrag) | Cobrar Umesh: GL 'CORRECTED', dados do carro, termos OTP, sindicato |
| Dinamarca | Sherwin Williams DK — set/26; KGS — set/26 | ✅ Validados 14/10 (Sherwin: Medium 0069 líquido; KGS: High seguro-saúde não tributado) | Cobrar Rakshitha: arquivo efetivamente enviado (Sherwin); tipo de cobertura de saúde e master (KGS) |
| Suécia | One Identity Sweden AB — set/26 | ✅ Validado 14/10 com ressalva (High: sem Kvittens desta entidade; High: payout de férias na tabela mensal) | Cobrar Athul: Kvittens 559400-9267, master, banco, skattebeslut do Magnus |
| Cazaquistão | Mastercard — out/26 | ✅ Validado parcial 14/10 (contribuições e ordens conferem; ИПН Not tested) | Cobrar Malika: 200.00 do 3º tri + recibo, YTD do ИПН, GL |
| Azerbaijão | Cliente a confirmar — set/26 | ⏸️ Pulado (zip AES + .rar; aguardando autorização/extração pelo Wallisson) | Fora desta rodada |
| Finlândia, Estônia | — | ⏳ Sem resposta (Marju) | Onda 3 |
| Irlanda | — | ⏳ Sem SBC definido | Onda 3 |
| Rússia | — | ⏳ Sem contato (Sadaf) | Onda 3 |

---

## 3. Plano por país

Os itens de base legal abaixo são **o que buscar**; todo valor e versão é confirmado na fonte oficial antes do uso (as skills `payroll-compliance-<país>` servem de mapa, não de fonte).

### Onda 1 — pacotes completos

**Noruega · Henkel Norway AS (917472890) · set/2026**
- Report: A-melding (XML) + tilbakemelding (recibo JSON). Conferir que o recibo é desta A-melding (referência/ID da mensagem, org.nr, período).
- Base legal: XSD e veiledning da A-ordningen (Skatteetaten) em vigor; regras de forskuddstrekk (tabela/percentual do skattekort); arbeidsgiveravgift (zona); feriepenger; OTP se presente.
- Decisão de método (gate): o skattekort de cada empregado não vem no pacote → o recálculo do imposto testa consistência com o tipo de trekk informado, não a taxa em si; confirmar com Wallisson.
- Amarrações: A-melding × G2N × contracheques × banco (EE) × GL (3 versões — usar a final e explicar o "CORRECTED") × conciliação (ods) × master.
- Esforço estimado: 1 dia (primeiro pacote do país: parsers + base legal).

**Dinamarca · Sherwin-Williams Denmark A/S (SE 24502511) · set/2026** (+ KGS Fire & Security)
- Report: arquivo eIndkomst enviado + "Afstemning af indberetninger" do SKAT (recibo/conciliação por campo — feltnumre 0013, 0015, 0016, 0019...).
- Base legal: especificação de campos do eIndkomst (Skattestyrelsen) em vigor; AM-bidrag; A-skat pelo skattekort (taxa + fradrag); ATP; feriepenge/feriegodtgørelse.
- Decisão de método: skattekort não vem no pacote → testar A-skat = (base − AM) × taxa − fradrag com os parâmetros do contracheque/G2N; validar a soma dos campos contra a Afstemning do SKAT (prova externa).
- KGS: mesmo método, sem banco (money movement fora da Mercans) → banco = Out of scope.
- Esforço: 1 dia (Sherwin) + 0,5 dia (KGS reaproveitando).

**Suécia · One Identity Sweden AB (559400-9267) · set/2026**
- Problema: o zip é da One Identity; o Kvittens e o master são da Quest Software (556602-0433).
- Decisão (Wallisson): validar a One Identity com o que veio (recibo = Not tested) **ou** aguardar o conjunto coerente.
- Base legal: AGI (arbetsgivardeklaration på individnivå) — XSD/fältlista do Skatteverket (há cópia no skill: agd_1.1.xsd, fältlista, struktur — reconfirmar versão 2026), skattetabeller 2026, arbetsgivaravgifter.
- Esforço: 1 dia.

### Onda 2 — pacotes incompletos (validar o que der; o resto Not tested)

**Cazaquistão · Mastercard · out/2026 (folha no 1C)**
- Veio: G2N 1C, PRE template, contracheque, banco (Swift), 7 ordens de pagamento de tributos (ИПН, ОПВ, ОПВР, СО, СН, ВОСМС, ООСМС).
- Falta: report trimestral + recibo (já pedido 13/10), GL, master.
- Pode-se validar já: recálculo dos tributos por empregado × G2N × ordens de pagamento × banco.
- Base legal: Código Tributário e leis de pensão/seguro social/saúde do Cazaquistão **em vigor em 2026** (verificar se houve novo Código Tributário a partir de 2026), formulário do report trimestral (ex.: 200.00) e suas regras.
- Nota: contracheque com nome "August" na pasta de outubro — confirmar.

**Azerbaijão · cliente a confirmar · set/2026 (folha em Excel)**
- Veio: zip criptografado (banco PDF, PRE template, contracheques .rar, lista de pessoal).
- Antes de começar: **autorização do Wallisson para abrir** o zip com a senha recebida; pedir que próximos envios usem o Drive da Mercans (domínio mercans.me fora da organização).
- Falta: report(s) + recibo, GL, nome do cliente.
- Base legal: imposto de renda retido e contribuições DSMF (seguro social), seguro-desemprego e médico obrigatório em vigor 2026; declarações no e-taxes.gov.az.

### Onda 3 — aguardando arquivos

| País | Report principal (a confirmar) | Ação agora |
|---|---|---|
| Finlândia | Tulorekisteri (ilmoitus palkkatiedoista) | Cobrar Marju (2ª vez) com cópia para Manju |
| Estônia | TSD + anexos (mudança para formato data-based em out/2026) | Idem |
| Irlanda | Payroll Submission Request (PSR) + RPN | Definir SBC com Manju/Marko |
| Rússia | 6-NDFL, RSV, EFS-1 (folha no 1C) | Pedir à Sadaf o contato |
| Reino Unido (2º) | FPS/EPS | Opcional; Christina |

---

## 4. Decisões (tomadas em 14-10-2026)

| País | Decisão tomada | Motivo |
|---|---|---|
| Noruega, Dinamarca | Sem skattekort no pacote: o recálculo testa a **consistência** do trekk/A-skat com os parâmetros impressos no contracheque/G2N; a taxa do skattekort fica como premissa | Recomendado; aprovado |
| Dinamarca | Validar **Sherwin Williams DK e KGS**; banco da KGS = Out of scope (money movement fora da Mercans) | Recomendado; aprovado |
| Suécia | Validar **One Identity Sweden AB (559400-9267)** com AGI, G2N, GL e contracheques (conjunto coerente, mesmo run); recibo, master e banco = Not tested; cobrar ao Athul o Kvittens da 559400-9267, master e banco | O zip é coerente para a One Identity; só o Kvittens e o master são da Quest |
| Cazaquistão | Começar já: recálculo × G2N × ordens de pagamento × banco; report trimestral, GL e master = Not tested até chegarem | Recomendado; aprovado |
| Holanda (outbound) | **Atualizado 14/10: o papel é só validar e reportar, não corrigir.** O outbound é o Audit Report de validação no modelo Mammoet_P09-P13_Audit_Report.docx, emitido com o que o pacote tem; documentos ausentes entram como limitação de escopo. Quest emitido: NL_Quest_2026-09_Audit_Report_v1.1.docx (v1.0 substituída). Excerpta e Sherwin: mesmo critério quando solicitado | Escopo: validamos e reportamos (CLAUDE.md) |
| **Azerbaijão** | **Pulado nesta rodada.** O zip é AES com senha no e-mail e o .rar exige extração; abrir exige autorização explícita do Wallisson | Wallisson pediu para pular (14-10) |

## 4.1 Como evitar as travas que aconteceram (regras de execução)

| Trava | Causa | Regra |
|---|---|---|
| Comando recusado (zip do Azerbaijão) | Senha de arquivo dentro de um comando | Nunca colocar senha/segredo em comando. Arquivo protegido → pular e pedir ao Wallisson que extraia ou autorize antes |
| Bloqueio "Irreversible Local Destruction" | Tentativa de alterar o registro do Windows | Não alterar configurações do sistema; se for necessário, gerar o arquivo e o Wallisson executa |
| Navegador errado (outro Windows / Mac) | Claude Desktop e Claude Code disputando a extensão; sessão presa a outro aparelho | Antes de usar o Chrome: `list_connected_browsers` + teste com servidor local em 127.0.0.1; usar só o navegador deste PC |
| Caminho > 260 caracteres | Pastas longas + nomes de arquivo longos | Extrair em `02 Validation/_extracted` com nomes curtos; usar o prefixo `\\?\` quando preciso; rodar em pasta curta |
| Heredoc quebrado / caracteres de controle | Python com aspas e `\b` dentro de heredoc no bash | Escrever scripts com a ferramenta Write e executar o arquivo |
| Falsos positivos do script | Mapeamento de colunas presumido, regra aplicada fora do escopo | Mapear colunas lendo o arquivo do cliente; ler cada exceção na fonte antes de virar achado |

---

## 5. Cronograma proposto

| Quando | O quê |
|---|---|
| Dia 1 | Decisões do §4; cobranças em rascunho (Christina, Marju, Sadaf, Malika, Pari, Athul/Suécia) para aprovação |
| Dias 1–2 | Onda 1: Noruega → Dinamarca (Sherwin + KGS) → Suécia |
| Dias 3–4 | Onda 2: Cazaquistão e Azerbaijão (parcial; completar quando chegar o report) |
| Contínuo | Onda 3 conforme os arquivos chegarem; reprocessar NL/UK/UA no próximo período reaproveitando os validadores |

Ao fim de cada país: workbook em `02 Validation`, resumo EN para implementation, resumo PT para o Wallisson, registro no cérebro (hub do país, `log.md`) e lições novas neste plano.

---

## 6. Critério de "pronto" por pacote

- [ ] Entidade, período e recibo conferidos (identificadores batem)
- [ ] Base legal do ano com URL/versão/data em `Sources`
- [ ] Decisões de método registradas em `Assumptions`
- [ ] Recálculo em 100% dos empregados
- [ ] Amarrações report/G2N/contracheque/banco/GL/master feitas (ou Not tested com motivo)
- [ ] Toda exceção automática revisada (achado ou "Pass (reviewed)")
- [ ] Workbook + resumos entregues; cobranças em rascunho
- [ ] Cérebro atualizado

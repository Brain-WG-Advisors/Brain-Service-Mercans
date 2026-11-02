# EUA: processo de filing por terceiro (federal e estados)

Data: 2026-10-29. Frente EUA. Decisão do diretor (2026-10-21): filings estatutários por provedor terceiro, sem integração com ADP; o motor da Mercans calcula, o provedor deposita e arquiva. Registro de fontes: `US-compliance/00-official-sources/_register-shards/mandate-FILING.csv` (ids US-FIL-001 a 027).

Já sabido (não refeito): Form 8655 Rev. 1-2024 (linha 19 estado/local); Rev. Proc. 2012-32 (empregador continua responsável; seção 5.05, aviso trimestral).

**Confiança geral: 60%.** Federal bem coberto. Estados: 8 dos 10 prioritários com pelo menos uma fonte oficial lida; TX, IL e MI bloqueados (ver "O que falta"). Mercado de provedores: evidência fraca (só páginas de vendor, tier B).

## 1. Federal

### 1.1 Reporting Agent (Pub. 1474, Rev. 4-2026) [A.2, US-FIL-001]
- **Quem pode ser:** "accounting service, franchiser, bank, service bureau, or other entity authorized to perform payroll services for other businesses" (seção 04.02). Um provedor de filing recebendo arquivo do nosso motor se enquadra como service bureau.
- **Autorização:** o contribuinte (a Mercans, por entidade empregadora/EIN) assina o Form 8655; o agente envia à IRS (Ogden, fax ou lista eletrônica). Cópia fica com o agente até prescrever o último return (03.01). Assinatura eletrônica do 8655 só nos dois métodos de autenticação + dois de captura da 01.04 (foto-ID presencial ou autenticação por terceiro; stylus ou checkbox com data, hora e IP).
- **Lista do agente:** adições e exclusões em listas separadas, com EIN do agente, EIN do cliente, nome e endereço; obrigatoriamente eletrônica acima de 100 submissões por semana, e o único canal é SLFT B2B (o SDT foi desativado em dezembro de 2025; exige certificado de identidade comprado de terceiro) (01.06, 01.10).
- **O que a IRS aceita processar no RAF:** 940, 941, 943, 944, 945 e as versões -X (941-X, 943-X, 945-X podem ir por e-file), CT-1, 1042; mais autorização de depósito (FTD/FTP) e de divulgação de informação (notices de W-2/1099) (01.05, 02.01).
- **Depósitos:** o agente faz FTD "via EFTPS or the Federal Tax Application (FTA)" (02.01).
- **O que o empregador continua devendo:** a autorização "does not relieve the taxpayer of the responsibility (or from liability)" por entrega e depósito no prazo; o agente deve dar declaração escrita ao contratar e no mínimo trimestralmente (01.01, Rev. Proc. 2012-32 seção 5.05).
- **O que o empregador assina:** Form 8655 (um por EIN) e, se o provedor exigir, o contrato de serviço. Não assina cada 94x quando o agente está autorizado a assinar/arquivar (isso vem do próprio 8655; ver linha 19 já conhecida para estado/local).
- Não lido: Pub. 3112 (participação no e-file) e Rev. Proc. 2007-40, citadas pela Pub. 1474. Para o provedor ser aceito como e-file provider, o requisito dele é com a IRS, não nosso; confirmar com o provedor.

### 1.2 W-2: SSA / EFW2
- **Página da SSA** [A.2, US-FIL-002]: ano fiscal 2026 usa **EFW2 Publication 42-007** (EFW2C é 42-014); "developers of payroll and tax reporting software must follow these file formats"; envio por Business Services Online.
- **Versão exata do EFW2 2026 e data de revisão: não confirmada.** O PDF `26efw2.pdf` bloqueou (403 no WebFetch; o visualizador do Chrome não devolveu texto) [US-FIL-003, gated]. Pista tier B (Sovos, US-FIL-004): spec de 2026 publicada em 20/08/2026, com novos códigos Box 12 (TA, TP, TT), campos para J/K/L/P e o campo combinado de uncollected tax on tips (A e B) dividido em dois. Uma busca citou uma segunda versão de 12/10/2026, sem fonte lida: tratar como não confirmada.
- Registros do EFW2 e regras de assinatura/PIN do empregador: não lidos (mesmo bloqueio). Não usar de memória.
- O formato EFW2 também é aceito por vários estados para W-2 estadual (ex.: pista de MI e HI; ver seção 2).

## 2. Estados: mecanismos comuns

Padrões que apareceram nas fontes lidas:
1. **Autorização estadual separada do 8655.** Cada agência de UI (workforce) e cada agência de imposto de renda tem a própria autorização, em geral eletrônica no portal do estado (PA UCMS handshake; CA e-Services for Business) ou formulário (CA DE 48, FL DR-835, OH WT 8655, PA REV-677, NC DES POA).
2. **Programa de bulk filer para provedores**, com cadastro, teste e identificador do agente (NY Pub. 72.5: aprovação prévia, arquivo de teste, até 30 dias, agent ID; OH bulk filer com ETIN + OHID, FTP seguro; CA FSET).
3. **FSET (Federal/State Employment Taxes):** padrão XML da IRS/FSET que CA (web service) e OH (v4.4) implementam; IL também anuncia FSET (pista, não lido).
4. **Formatos de wage report de UI:** ICESA (posições fixas), CSV próprio do estado, XML, MMREF-1 (CA). EFW2 serve para W-2 estadual onde o estado aceita.

### Tabela por estado (prioridade 10)
Legenda: **[lido]** = fonte oficial lida nesta sessão; **[pista]** = só título/URL de resultado de busca, não lido; **[bloqueado]** = host recusou acesso daqui. "Withholding" = retenção de imposto de renda estadual. Estados sem imposto de renda sobre salário: TX e FL (só UI).

| Estado | Formulário/mecanismo de agente (POA) | Wage report de UI em lote | Withholding em lote | Fonte |
|---|---|---|---|---|
| CA | **DE 48** Power of Attorney Declaration, online (e-Services) ou correio; assinante: dono/sócio/diretor; data da assinatura até 30 dias antes do envio; DE 231PRA descreve Payroll Reporting Agent [lido] | **DE 9C** por Upload Bulk Return File (zip até 10 MB): XML, ICESA ou MMREF-1; ou CSV (SSN, nome, total subject wages, PIT wages, PIT withheld, wage plan code); ou **FSET** XML web service [lido] | Mesmo DE 9C carrega PIT wages e PIT withheld por funcionário; DE 9 (return) via e-Services [lido em parte] | US-FIL-005, 006; https://edd.ca.gov/pdf_pub_ctr/de8300.pdf |
| TX | **C-42** Written Authorization to Represent Employing Unit (TWC) [pista, bloqueado] | ICESA e TXUS (spec no site da TWC) [pista, bloqueado] | Não se aplica (sem imposto de renda estadual) | US-FIL-018 |
| NY | **POA-1** (tax.ny.gov/poa) [pista]; para NYS-45 em lote, o agente recebe um **agent identification number** de 3 dígitos [lido] | **NYS-45** Web Upload (Pub. 72.5, 2/25): UI + withholding + salários por funcionário num único arquivo; serviços que reportam para 10+ empregadores; aprovação prévia + teste, até 30 dias [lido] | Mesmo arquivo NYS-45 (NYS, NYC e Yonkers retidos por funcionário) [lido] | US-FIL-007, 021; https://www.tax.ny.gov/pdf/publications/withholding/pub72-5.pdf |
| FL | **DR-835** Power of Attorney and Declaration of Representative (inclui Reemployment tax) [lido] | **RT-6** (leiaute de importação/XML não obtido) [lacuna] | Não se aplica | US-FIL-015 |
| IL | IDES: upload em lote de POA eletrônica por service bureau sob MOU; IDOR: IL-8655 por cliente [pista, bloqueado] | IDES: leiaute ICESA e CSV trimestral (UI-3/40) [pista, bloqueado] | IDOR: FSET para withholding [pista, bloqueado] | US-FIL-019 |
| PA | UI: handshake eletrônico no **UCMS** (TPA registra, ganha Representative Identifier de 10 dígitos, empregador atribui, TPA aceita) [lido]; Receita: **REV-677** (tributo/período; tabelião ou 2 testemunhas) [lido] | **UC-2010 Rev 11-25**: upload de arquivo até 500 KB (.ICS ou .CSV), FTP até 200 MB, pre-file CSV para TPAs; acima de 100 empregados obrigatório arquivo [lido] | Programa de lote da PA DOR não localizado [lacuna] | US-FIL-008, 009, 010 |
| OH | **WT 8655** Payroll Service Company Authorization (limited POA; agente prova autorização à ODT em 24 h) [lido] | ODJFS: spec JFS 20233 [pista, não lido] | **Bulk Filing** (Implementation Guide Parte A, rev. jan/2025): IT 501, IT 941, SD 101, SD 141, FSET v4.4, FTP seguro, bulk filer com ETIN + OHID; cliente precisa de conta ativa [lido] | US-FIL-011, 012 |
| NC | UI: **POA and Declaration of Representative** da DES (um por agente por empregador; papéis separados) [lido; número do form não mostrado]; Receita: POA não localizado [lacuna] | DES: upload ICESA/CSV [pista, não lido] | **eNC3 Web File Upload**: flat file .txt para NC-3, W-2 e 1099, vários negócios no mesmo arquivo, sem cadastro; NC-5 em lote não localizado [lido em parte] | US-FIL-013, 014 |
| MI | UIA 1488 (UI) e Treasury **151** (tributo) [pista, bloqueado] | MiWAM, formato não lido [bloqueado] | SUW e-file Handbook 2026 [pista, bloqueado]; busca indica que Treasury aceita EFW2 ou Pub. 1220 para W-2 [pista] | US-FIL-020 |
| GA | DOR **RD-1063** Reporting Agent Authorization (página sem detalhe) e **RD-1061** POA [lido só o título / pista] | DOL UI File Upload: CSV ou Excel, resposta por e-mail em 1 h [lido]; leiaute de registro não estava na página | G-7 / G-7M: programa de lote não localizado [lacuna] | US-FIL-016, 017 |

## 3. Mercado: provedores (tier B, apenas documentação do vendor)

Achado central: **o mercado "recebe arquivo de um motor externo e só arquiva/deposita" é estreito.** A maioria dos provedores é (a) parte de um motor próprio de folha, (b) camada de formulários/e-file dentro de outro software, ou (c) serviço acoplado a uma plataforma específica. Nenhuma das páginas lidas declara, em termos explícitos, aceitar um register genérico de um motor externo. Isso precisa ser perguntado a cada provedor (RFP), não assumido.

| Provedor | Entrada aceita (conforme a página) | Cobertura declarada | Reporting Agent / depósito | Observação |
|---|---|---|---|---|
| OneSource Virtual (OSV) | "in-tenant" no Workday; outros sistemas não declarados | "federal, state, and local", depósitos, W-2 e retificações; 50 estados não declarado | Não declarado | Serve se o motor fosse Workday; não é o nosso caso |
| Greenshades | Conectores (Dynamics GP, Business Central, Sage Intacct, Acumatica, Bullhorn, Avionté) + API pública; a folha roda no Greenshades | 941, SUTA, retornos locais trimestrais; 940 e W-2 no blog | Blog descreve o 8655 do cliente; status de agente não declarado | Perguntar se aceita só o filing sem rodar a folha |
| Aatrix | Parceiro em 60+ sistemas de folha; método de integração não declarado | W-2, 1099, 941, UI federal/estadual, withholding, new hire | Depósito e status de agente não declarados | Camada de formulário e e-file, não de depósito |
| TaxBandits (API) | API (SDKs Java, Node, .NET, Python), sandbox | W-2, 941, 940, Schedule R, withholding estadual, UI estadual, new hire | Depósitos não mencionados | Boa para e-file dos federais e W-2; não resolve depósito |
| Check (checkhq) | Embedded payroll com motor próprio (resumo de busca; docs sem conteúdo) | Alegam 50 estados + DC e local | Alegam filing e remessa | Provavelmente exige rodar a folha no Check |
| Symmetry | APIs de cálculo e guias de filing | 7.000+ jurisdições (cálculo) | Não é filer | Alternativa de cálculo, não de filing |

Sem leitura: Paycor, Paylocity, Ceridian/Dayforce, Vertex (calcula, não arquiva folha), Equifax/TALX (UI), Alight, Thomson Reuters, Wolters Kluwer. Encaminhamento sugerido: RFP curto com 6 perguntas (aceita arquivo/API de motor externo? Reporting Agent no federal? POA estadual nos 50+DC? depósito na conta do empregador ou em trust? local? SLA e responsabilidade por penalidade?).

## 4. Dados mínimos que o motor deve entregar por funcionário e por período

Derivado só do que foi lido (CA DE 8300 CSV, NY Pub. 72.5, Pub. 1474, OH Bulk Guide). Itens marcados "a confirmar" dependem do EFW2 2026 e dos leiautes que não consegui ler.

**Por entidade empregadora (cliente do agente):** EIN, razão social e endereço (devem bater com a IRS, Pub. 1474 01.10); números de conta estaduais de withholding e de UI por estado (NY: "employer registration number" de UI de 7 dígitos; CA: employer payroll tax account; OH: conta ativa de withholding); autorizações assinadas (8655 e POA estaduais).

**Por funcionário e por trimestre (mínimo comprovado):**
- SSN, nome (primeiro, inicial, último). CA CSV exige os quatro campos; duplicidade de SSN não é permitida, uma linha por funcionário por trimestre, salvo wage plan code diferente.
- Salário total sujeito a UI (CA "total subject wages"; NY "total UI remuneration").
- Salário sujeito a retenção de imposto de renda estadual e o imposto estadual retido (CA PIT wages e PIT withheld; NY gross federal wages e tax withheld).
- Para NY: imposto retido separado de NYS, NYC e Yonkers. Para OH: imposto de distrito escolar (código de 4 dígitos do school district do residente) além do estadual. Isso obriga o motor a guardar **estado de trabalho, estado e localidade de residência, código local**.
- Wage plan code (CA: A, J, L, P, R, S, U) e equivalentes por estado.
- Código de estado de UI (onde o trabalho é localizado) e semanas/horas só onde o estado exigir [a confirmar por estado].

**Por período de folha (depósitos federais):** imposto de renda federal retido, FICA (OASDI e Medicare, parte do empregado e do empregador, Medicare adicional), data de pagamento (para a regra de prazo de depósito) e valores a depositar por jurisdição. O arquivo deve manter centavos (o 941 não arredonda para dólar inteiro, US-FED-005).

**Anual (W-2, EFW2) [a confirmar no 42-007 de 2026]:** salário federal, SS e Medicare wages, gorjetas, Box 12 com códigos, wages e imposto estadual/local por jurisdição, dados do empregado e do empregador. Atenção às mudanças de 2026 citadas pelo tier B (TA, TP, TT; uncollected tax split).

**Frequência:** depósitos por ciclo de folha; wage report e returns trimestrais; W-2 anual (prazo SSA 1 de fevereiro de 2027, pista tier B).

## O que falta (para fechar)

| Item | Por que não fechou | O que fecharia |
|---|---|---|
| EFW2 2026 (versão, registros, assinatura/PIN) | ssa.gov/employer/efw/26efw2.pdf bloqueou | Baixar o PDF por outro caminho (usuário no navegador) |
| TX C-42 e leiaute TWC | twc.texas.gov com geobloqueio CloudFront | Acesso de outra rede ou o usuário baixar |
| IL (IDES POA upload, ICESA, IDOR FSET) | DNS falhou em ides.illinois.gov e tax.illinois.gov | Repetir de outra rede |
| MI (UIA 1488, Treasury 151, handbook SUW 2026) | michigan.gov 403 | Idem |
| FL RT-6 leiaute; PA DOR e GA DOR e NC DOR POA/lote | Não localizados nas páginas lidas | Busca dirigida estado a estado (paralelizável: 50+DC buscas independentes) |
| Mercado | Vendor docs não declaram aceitar motor externo | RFP aos provedores |

## Fontes lidas (resumo; detalhe no CSV)

| Fonte | URL | Lida em | Tier |
|---|---|---|---|
| IRS Pub. 1474 (Rev. 4-2026) | https://www.irs.gov/pub/irs-pdf/p1474.pdf | 2026-10-29 | A.2 |
| SSA EFW2 e EFW2C (página) | https://www.ssa.gov/employer/EFW2&EFW2C.htm | 2026-10-29 | A.2 |
| SSA EFW2 2026 (PDF) | https://www.ssa.gov/employer/efw/26efw2.pdf | não lido (gated) | A.2 |
| Sovos: SSA EFW2 2026 | https://sovos.com/regulatory-updates/trr/ssa-releases-2026-specifications-for-filing-forms-w-2-and-w-2c-electronically-efw2-efw2c/ | 2026-10-29 | B |
| CA EDD DE 48 | https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de48.pdf | 2026-10-29 | A.2 |
| CA EDD DE 8300 (7-24) | https://edd.ca.gov/pdf_pub_ctr/de8300.pdf | 2026-10-29 | A.2 |
| NY Pub. 72.5 (2/25) | https://www.tax.ny.gov/pdf/publications/withholding/pub72-5.pdf | 2026-10-29 | A.2 |
| PA UC-2010 (11-25) | https://www.pa.gov/content/dam/copapwp-pagov/en/dli/documents/uc/uc-forms/uc-2010.pdf | 2026-10-29 | A.2 |
| PA DLI, Using a Tax or Payroll Service | https://www.pa.gov/agencies/dli/resources/for-employers-and-educators/how-to-file/using-a-tax-or-payroll-service | 2026-10-29 | A.3 |
| PA REV-677 (07-25) | https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/otherforms/documents/rev-677.pdf | 2026-10-29 | A.2 |
| OH WT 8655 | https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/employer_withholding/generic/wth_wt8655.pdf | 2026-10-29 | A.2 |
| OH Bulk Filing Guide Parte A | https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/employer_withholding/Bulk%20Filing%20Guide/BulkFilingImplementationGuideA_OHTAX_02242026.pdf | 2026-10-29 | A.2 |
| NC DES POA (instruções) | https://www.des.nc.gov/documents/downloads/power-attorney-instructions/open | 2026-10-29 | A.3 |
| NC DOR eNC3 Web File Upload | https://www.ncdor.gov/taxes-forms/withholding-tax/enc3-web-file-upload | 2026-10-29 | A.3 |
| FL DOR DR-835 | https://floridarevenue.com/Forms_library/current/dr835.pdf | 2026-10-29 | A.2 |
| GA DOL UI wage file upload | https://gta.georgia.gov/unemployment-insurance-wage-file-upload | 2026-10-29 | A.3 |
| GA DOR RD-1063 (página) | https://dor.georgia.gov/rd-1063-reporting-agent-authorization | 2026-10-29 | A.3 |
| TX, IL, MI, NY POA-1 | ver CSV US-FIL-018 a 021 | não lidos (pista) | A.2 |
| OneSource Virtual, Greenshades, Aatrix, TaxBandits, Check, Symmetry | ver CSV US-FIL-022 a 027 | 2026-10-29 | B |

Bloco de prova: pedido (1 a 4) coberto; fontes por afirmação no CSV; teste: texto dos PDFs extraído e lido (Pub. 1474, DE 48, DE 8300, Pub. 72.5, UC-2010, REV-677, WT 8655, Bulk Guide A, NC DES, DR-835). Confiança 60%; falta o que a tabela "O que falta" lista.

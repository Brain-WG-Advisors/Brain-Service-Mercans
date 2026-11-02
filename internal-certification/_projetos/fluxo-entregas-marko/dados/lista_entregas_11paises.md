# Lista de entregas de payroll ao governo e pagamentos: DK, NL, SE, UK, UA, FI, EE, IE, KZ, AZ, RU (leitura de 29/10/2026)

Só material interno (SOPs do Drive, hubs e artefatos nossos, pacotes da certificação). Nada de web, nada alterado. Texto de SOP citado em inglês, no original. A Noruega fica com outra pessoa (ver seção 12).

## 0. Como ler

- **Parte:** Tax / Social security / Other / Payments.
- **"Quem envia hoje segundo o SOP":** frase literal do SOP. Onde o SOP não diz o ator (frase impessoal), está escrito "SOP impessoal". Onde não há SOP, a célula traz a evidência de pacote/hub marcada como `PACOTE:` ou `HUB:`, que não é SOP.
- **[Verify]:** só uma fonte cita, ou o SOP é antigo, ou há conflito entre fontes.
- O Drive só tem SOP de país (pasta `01 - SOP`) para **DK, NL, UK (pasta `GB`), IE**. Para **SE, UA, FI, EE, KZ, AZ, RU** a pasta `01 - SOP` só tem o arquivo-modelo "Testfile for copying folders.gdoc". A pasta `United Kingdom` não tem `01 - SOP`; o SOP do UK está em `Country Folders\GB\01 - SOP\`.
- O board monday "BAU Master Client List" (lido por outro agente em `dados/monday_12paises.md`) mostra que existem **SOPs por cliente em Google Docs** (links) para DK, NL, SE, UA, FI, EE; eles **não estão em disco** e não foram lidos aqui. É a principal lacuna para "quem envia hoje".

### SOPs lidos

| País | Arquivo (Drive: `G:\Drives compartilhados\Compliance Team\Country Folders\...`) | Data do SOP | Observação |
|---|---|---|---|
| DK | `Denmark\01 - SOP\Compliance SOP Statutory report Denmark.docx` | Metadados internos: criado 2022-10-10, modificado 2023-03-09; mtime do arquivo 2025-06-25. Versões antigas em `Old\` (V1 2022-09-27, V2 2023-03-09). Sem data impressa. | Texto fala de NemId e de "tax rate is 22% for the year 2022": conteúdo de 2022/2023. **[Verify] tudo.** |
| NL | `Netherlands\01 - SOP\Mercans_Compliance SOP_Netherlands_V1.docx` (e `Mercans_SOP_Netherlands_V1.pdf`, mesmo texto) | Capa: "01 December 2021", "(c) 2021 Mercans LLC". Docx criado no Drive em 2025-04-01; PDF 2025-03-31. Cita "in 2024: 67 years" e Handboek 2021. | Texto de 2021, com ajuste de 2024. **[Verify] tudo.** |
| UK | `GB\01 - SOP\Mercans_SOP_GB.pdf` | "(c) 2024 Mercans LLC"; arquivo de 2024-10-11. | Contém uma linha estranha do **Filipinas** (BIR 2316) dentro da tabela do UK: sobra de modelo. Conferir. |
| IE | `Ireland\01 - SOP\SOP Ireland.pdf` | Arquivo de 2025-08-04; fala de ERR "introduced in 2024". `Archived\SOP final version.docx` não abre (não é docx válido; provável atalho do Drive): não lido. | Único SOP com marcas de escopo legíveis para todos os reports. |

Extração: `python -I` com python-docx/pypdf, tabelas e marcas de caixa (☒/☐) lidas do XML.

---

## 1. Dinamarca (DK)

SOP: `Denmark\01 - SOP\Compliance SOP Statutory report Denmark.docx`, seção "Statutory Filings & Contributions" (tabela) e "Reports Summary". Data: conteúdo 2022/2023 [Verify]. Hub: `brain-service\paises\Dinamarca.md` (skill `payroll-compliance-denmark`, lida 2026-10-02). Specs no Drive: `Denmark\12 - Country Report Codes\Report Specs\` (ATP, E-Income, Stat) e `Reports\` (e-income, PBS).

| Parte | Entrega (nome oficial) | Autoridade | Frequência | Prazo | Quem envia hoje segundo o SOP (frase literal) | Canal citado no SOP | Fonte | Data do SOP |
|---|---|---|---|---|---|---|---|---|
| Tax | Skattekort bestilling (tax card subscription; relatório de assinatura) | Skatteforvaltningen (The Danish Customs and Tax Administration) | Antes de cada folha | "Before each payroll run" | "From the payroll engine a report is pulled. The report is uploaded at www.skat.dk, via NemId." (SOP impessoal; marcado In-Scope e Online Filing) | skat.dk com NemId; arquivo em formato fixo (campos: CPR, nº do empregado, data de início, tipo de cartão) | SOP DK, tabela "Statutory Filings & Contributions", linha 1; "Report samples > Tax card subscriptions"; "Reports Summary" | 2022/23 [Verify] |
| Tax | Hentning af skattekort (coleta do cartão de imposto) | Skatteforvaltningen | Antes de cada folha | "Before each payroll run" | "Logon to www.skat.dk with NemId. / Go to the Tax card sections and collect the report of new or changed tax card. / Upload the report to the payroll engine." (SOP impessoal; é entrada, não envio) | skat.dk com NemId; arquivo em formato fixo | SOP DK, tabela, linha 2 | 2022/23 [Verify] |
| Tax + Social security (A-skat, AM-bidrag, ATP, férias, pensão no mesmo relatório) | E-indkomst indberetning (relatório mensal de renda e imposto retido) | Skatteforvaltningen | Após cada folha | "Latest at the end of the month." (SOP). HUB/facts: set/26 = 12.10.2026 (SMV, regra geral: dia 10 do mês seguinte) ou 30.09.2026 (empregador grande) | "The report is pulled from the payroll engine. / Logon to Skat via NemId and upload the report. / Wait couple of hours... / Check that the report has been fully accepted. / If any rejected, correct those manually." Depois: baixar Year-to-date, "Reconcile against the payroll engine. / Save the reconciliation for audit purpose." (SOP impessoal; In-Scope, Online) | skat.dk (eIndkomst) com NemId, upload. HUB: skill diz que o produto trata eIndkomst como M2M (MQ ou Sterling File Gateway): divergência com o SOP, **[Verify]** | SOP DK, tabela linha 3; Reports Summary. PACOTE: `internal-certification\Denmark\*\01 Received\received.txt` (eIndkomst upload xlsx + "SKAT, eIndkomst, Afstemning af indberetninger-Sept'26.pdf" nos dois clientes); `references\Denmark\2026\facts.md` §3 (S04/S05) | 2022/23 [Verify] |
| Other | FravaersStatistik (estatística de ausência) | Statistics Denmark (DA / DS Statistic) | Anual | "28th of February of the following year" | "Report is pulled from the payroll engine. / The file is uploaded on the indberetning.da.dk site." (SOP impessoal; **Add-On Service**, Online) | indberetning.da.dk | SOP DK, tabela linha 4; Reports Summary | 2022/23 [Verify] |
| Other | StrukturStatistik (estatística de salários) | Statistics Denmark | Anual | "28th of February of the following year" | idem ("The file is uploaded on the indberetning.da.dk site."); Add-On | indberetning.da.dk | SOP DK, tabela linha 5 | 2022/23 [Verify] |
| Other | KonjunkturStatistik (estatística de salários) | Statistics Denmark | Trimestral | "1st of March, June, September, December" | idem; Add-On | indberetning.da.dk | SOP DK, tabela linha 6 | 2022/23 [Verify] |
| Payments / Social security | ATP (parte empregado 1/3, empregador 2/3) | ATP | (mensal, pelas horas) | n/d no SOP | SOP só descreve o cálculo: "The payment is calculated based on the hours worked during the period"; não diz quem paga | n/d. Drive tem "PBS report (1).xlsx" e "Denmark ATP Report Spec.xlsx" em `12 - Country Report Codes` | SOP DK, "Social security" | 2022/23 [Verify] |
| Payments / Social security | Samlet Betaling (encargos do empregador) | Autoridades dinamarquesas (fatura) | Trimestral (HUB RPT-005) | n/d no SOP | "The other part of the social security is invoiced as Samlet Betaling, directly from the authorities to the employer." (fatura vai direto ao empregador) | n/d | SOP DK, "Social security"; HUB `Dinamarca.md` ficha (RPT-005, só HUB: **[Verify]**) | 2022/23 [Verify] |
| Payments / Tax | Pagamento de A-skat + AM-bidrag | Skattestyrelsen | Mensal, junto do eIndkomst | HUB/facts: mesmo dia do relatório (12.10.2026 / 30.09.2026 em set/26); "at most 5 weekdays before" | SOP **não** tem linha de pagamento. PACOTE: Sherwin traz "BankFile ... EE" e "ER" XML; KGS: "banco = Out of scope, money movement fora da Mercans" (hub, IC) | n/d no SOP | HUB `Dinamarca.md` (IC); `facts.md` §3 e §10 [só HUB/facts: **[Verify]**]. monday: Statutory Payments marcado em 1 de 6 clientes DK | n/a |
| Other (só HUB) | FerieKonto (RPT-003/004; avisos de transição RPT-008/009, 31 dez e 31 jan); notificação de ausência/refusion (RPT-006); lønsumsafgift (RPT-007) | FerieKonto; Udbetaling Danmark; Skattestyrelsen | vários | HUB: ver `payroll-compliance-denmark` | SOP não cita | HUB: eIndkomst é M2M; Samlet Betaling e lønsumsafgift são portais | HUB `Dinamarca.md`, "Relatórios principais"; confiança do hub em lønsumsafgift ~60% (O-4). **[Verify]** | n/a |

Sem dados no SOP: Skat (formulários de imposto de empresa), IVA etc. são da empresa, não da folha.
monday (outro agente): Statutory Filings marcado em 6/6 clientes DK; payroll em HR Blizz (5) e Manual (1).

---

## 2. Holanda (NL)

SOP: `Netherlands\01 - SOP\Mercans_Compliance SOP_Netherlands_V1.docx` (e PDF), seções "Summary of Periodic Statutory Filings", "Payments to the Statutory Bodies", "Year-End Activities". Capa 01/12/2021 [Verify]. Hub: `brain-service\paises\Holanda.md`. Drive `12 - Country Report Codes\AI Reports Spec` tem as specs NL-BD-001 Loonaangifte, NL-BD-002 Jaaropgaaf, NL-BD-003 Correctie-Loonaangifte, NL-UWV-001 Ziekmelding, -002 Hersteldmelding, -003 WAZO-Aanvraag, -004 WIA-Aanvraag. Regra do SOP: "Statutory filings and payments are not included in the standard scope. When the Client has requested Mercans to provide the statutory filings and payments related services, such services may include the following filings." (todas as linhas: In-Scope ☐, Add-On ☒).

| Parte | Entrega (nome oficial) | Autoridade | Frequência | Prazo | Quem envia hoje segundo o SOP (frase literal) | Canal citado no SOP | Fonte | Data do SOP |
|---|---|---|---|---|---|---|---|---|
| Tax + Social security | Wage tax and social securities combined period declaration (Aangifte loonheffingen) | Belastingdienst | A cada 4 semanas ou mensal | "One month after the month end for the monthly filing frequency and 4 weeks after the end of the 4-week period for 4-week filing frequency." | "When the Client has requested Mercans to provide the statutory filings and payments related services, such services may include the following filings." (add-on; SOP não diz quem transmite). Também: "The wage tax and employee social security contributions are reported on as single declaration and paid within one month after the end of the reporting period." | SOP não cita canal. HUB: Digipoort M2M (WUS/FTP, PKIoverheid). PACOTE: Sherwin traz XML da aangifte + "Full original response message.json" + "Original response (FTP Files Download Business Successful Result)" | SOP NL, tabela "Summary of Periodic Statutory Filings", linha 1; "Payments to the Statutory Bodies". HUB `Holanda.md` (Relatórios principais, SIR). PACOTE: `internal-certification\Netherlands\Sherwin Williams - 2026-09\02 Validation\_extracted\` | 01/12/2021 [Verify] |
| Tax | Final levy on certain employment costs (eindheffing WKR) | Belastingdienst | Anual | "Annually in December or the following February"; pagamento "Within 30 days from the end of the reporting period" | "Client provides the additional wage types to be reported in the periodic tax returns as non-cash or informative wage types to Mercans. Mercans' scope does not include reporting non-employment or payroll related / taxable payments." | via a declaração periódica | SOP NL, "Payments to the Statutory Bodies", tabela linha 2 | 01/12/2021 [Verify] |
| Tax | Final levy on excessive severance packages (aangifte loonheffingen pseudo-eindheffing excessieve vertrekvergoeding) | Belastingdienst | Mensal, no período da rescisão | "Within 30 days from the end of the reporting period" | "Mercans completes the form and the Client submits the form Aangifte loonheffingen pseudo-eindheffing excessieve / vertrekvergoeding' online." (ator explícito: Mercans preenche, **cliente envia**) | online (formulário; HUB: única em papel/online fora do Digipoort) | SOP NL, tabela linha 3; HUB `Holanda.md` | 01/12/2021 [Verify] |
| Tax | Year-end Income Tax Declaration (Form 5) | Belastingdienst | Anual | "December or February of the following year." | SOP impessoal (Add-On). O próprio SOP diz: "There is no formal year-end filing for employers." | n/d | SOP NL, tabela de filings (linha final) e "Year-End Activities". Conflito interno do SOP: **[Verify]** | 01/12/2021 [Verify] |
| Tax / Employee | Annual Tax Statement (Jaaropgaaf, PDF) | Belastingdienst (modelo) / empregado | Anual | "February of the Following Year" | "As a standard service, Mercans will issue the Annual Income Statements for employees to the Client and the Client is responsible for the distribution of the statements to the employees." | PDF, entregue ao cliente | SOP NL, "Year-End Activities" e tabela | 01/12/2021 [Verify] |
| Social security | Registro de new hires/leavers (Belastingdienst e UWV) | Belastingdienst / UWV | Contínuo | n/a | "The registration of the New Hires and Leavers with the Social Security Authority will take place automatically based on the periodic tax reports." (idem tax). SOP: "There is no year-end declaration for Social Security." | via aangifte periódica | SOP NL, "Registration of New Hires and Leaver..." | 01/12/2021 [Verify] |
| Other | Uniforme Pensioenaangifte (UPA), pensão setorial | Pension funds (sectors) | Mensal | "10 days after month end" | SOP impessoal (Add-On) | n/d | SOP NL, tabela de filings | 01/12/2021 [Verify] |
| Other | Pension Plan Specific Format, pensão da empresa | Pension funds (company) | Mensal | "10 days after month end" | SOP impessoal (Add-On) | n/d | SOP NL, tabela | 01/12/2021 [Verify] |
| Other | Stichting PAWW, Online Filing | Stichting PAWW | A cada 4 semanas ou mensal | igual ao da aangifte (um mês / 4 semanas) | SOP impessoal (Add-On) | "Online Filing" | SOP NL, tabela | 01/12/2021 [Verify] |
| Other | CBS, dados estatísticos (online) | CBS | Mensal | "One month after the month-end." | SOP impessoal (Add-On); "Employers are obliged to comply with the data requests, when requested by the government" | Online | SOP NL, tabela | 01/12/2021 [Verify] |
| Other (só HUB/Drive) | Correctiebericht (correção de aangifte); Loonstaat; ziekmelding/hersteldmelding/WAZO/WIA ao UWV | Belastingdienst; UWV | evento | HUB: correção em até 8 semanas | SOP não cita | HUB `Holanda.md`: "não há relatório periódico UWV separado"; specs UWV existem no Drive mas não consta se foram entregues. **[Verify]** | HUB `Holanda.md`; Drive `12 - Country Report Codes\AI Reports Spec` | n/a |
| Payments | Pagamento do wage tax + contribuições de empregado (loonheffingen) | Belastingdienst | Mensal (ou 4 semanas) | "Due Date to pay contribution: One month after the end of the payroll period"; tabela: "Within 30 days from the end of the reporting period" | "Statutory filings and payments, money movement services and payments to third parties are add-on services. When the Client has opted for the statutory filings and payments services, the services include the below activities." (SOP impessoal) | "Payment Options: Bank transfer. The payment reference is given in the annual letter the employer receives with the reporting and payment due dates." Tabela: "online payment through bank transfer (SEPA)" | SOP NL, "Payments to the Statutory Bodies" > Social Security / Tax Agency; tabela linha "Monthly Payment" | 01/12/2021 [Verify] |

PACOTES NL (set/26): Quest Software B.V., Sherwin Williams Valspar B.V., Excerpta Medica B.V. Cada um traz o XML da aangifte (`...L01.09.2026.xml`) e o "Wage Tax Overview"; só o da Sherwin traz resposta do Digipoort, e é "recibo de outro LH" (hub). Hub: "o Athul diz que não guardam confirmação da Belastingdienst" (cobranças C-14/15/16 em rascunho). Quest e Excerpta trazem arquivo de banco SEPA (`..._SEPA_Bank_file` / `Deustche_Bank_xml_report`); o da Quest é malformado (hub). monday (outro agente): Statutory Filings 13/13 clientes NL; Statutory Payments só 3/13 (KGS NL, BAH, Magnit).

---

## 3. Suécia (SE)

**Sem SOP no Drive** (`Sweden\01 - SOP` só tem Testfile). Fontes: hub `brain-service\paises\Suecia.md` (skill `payroll-compliance-sweden`), `internal-certification\references\Sweden\2026\facts.md` §4, pacote `Sweden\Quest Software - 2026-09`. monday (outro agente): SOP por cliente em Google Docs (link `1OCjpHx2cxtGEAn3KQ1Xtz2SFL0xRyM...`), Filings 6/6 e Payments 5/6; payroll em HRB PAC. SOP por cliente não lido.

| Parte | Entrega (nome oficial) | Autoridade | Frequência | Prazo | Quem envia hoje segundo o SOP (frase literal) | Canal citado no SOP | Fonte | Data do SOP |
|---|---|---|---|---|---|---|---|---|
| Tax + Social security | Arbetsgivardeklaration på individnivå (AGI) = huvuduppgift + individuppgift + frånvarouppgift (schema 1.1.18.x) | Skatteverket | Mensal | Até dia 12 do mês seguinte; dia 17 nos períodos de julho (vence em agosto) e dezembro (vence em janeiro) para faturamento até 40 MSEK. Acima de 40 MSEK: declarar dia 26 (27 dez), pagar dia 12 (SFL 26 kap. 26/30/32 §§). Período 202609 = 12/10/2026 | sem SOP. PACOTE: AGI XML (`Skatteverket.xml`, "created 2026-09-22 13:16 by HrBlizz"); Kvittens (recibo Skatteverket, enviado 2026-10-09 13:25) foi anexado por Athul S no board monday "Global Statutory Filings Tracker" (item "Sweden - AGI Reporting - September 2026"). Quem aperta "enviar": **não consta** | n/d (sem SOP). HUB: AGI via XSD da Skatteverket; PACOTE: recibo "Kvittens" | `references\Sweden\2026\facts.md` §4 (S22/S23); `Suecia.md` (Relatórios principais); `Sweden\Quest Software - 2026-09\01 Received\received.txt` e `02 Validation\intake.md` | sem SOP |
| Tax | Pedido de reembolso växa-stöd (novo em 2026) | Skatteverket | n/d | n/d | sem SOP | n/d | HUB `Suecia.md`. Só HUB (confiança 93%): **[Verify]** | sem SOP |
| Tax | Kontrolluppgifter remanescentes | Skatteverket | Anual | 31 jan (HUB) | sem SOP | n/d | HUB `Suecia.md`; confiança ~70% (U6). **[Verify]** | sem SOP |
| Tax | FOS/CSR (fråga om skatteavdrag, consulta de tabela de imposto) | Skatteverket | evento | n/a | sem SOP | API (HUB, confiança 60%) | HUB `Suecia.md`. **[Verify]** | sem SOP |
| Payments | Pagamento de arbetsgivaravgift + skatteavdrag (no skattekonto) | Skatteverket | Mensal | Dia 12 (17 em jan/ago); acima de 40 MSEK, dia 12 também | sem SOP. PACOTE: "Bank file for the Sweden September run" **não foi enviado** (Pending); o Kvittens traz total de taxas+imposto 555 757 SEK (Quest AB) | n/d | `facts.md` §4; `received.txt`. **[Verify]** | sem SOP |
| Other (não estatutário) | ITP/SAF-LO, Collectum, Fora | privados | n/d | n/d | sem SOP | n/d | HUB `Suecia.md`: "canais não pesquisados" (U9). Fora do escopo estatutário | sem SOP |

Observação do pacote: o zip veio da pasta "Quest Software", mas contém dados da One Identity Sweden AB (559400-9267); o Kvittens e o master data são da Quest Software AB (556602-0433). Recibo, master e banco = Not tested (hub).

---

## 4. Reino Unido (UK)

SOP: `GB\01 - SOP\Mercans_SOP_GB.pdf` (c) 2024, tabela "Statutory Filings & Contributions" p. 7-13 e "Reports Summary" p. 21. As marcas de escopo (☐) no PDF vêm todas vazias: **o SOP não diz se é In-Scope ou Add-On** [Verify]. A linha BIR 2316 (Bureau of Internal Revenue, Filipinas) nas p. 12-13 é de outro país: sobra de modelo [Verify]. Hub: `brain-service\paises\Reino-Unido.md` (etapa em andamento; skill `payroll-compliance-uk`).

| Parte | Entrega (nome oficial) | Autoridade | Frequência | Prazo | Quem envia hoje segundo o SOP (frase literal) | Canal citado no SOP | Fonte | Data do SOP |
|---|---|---|---|---|---|---|---|---|
| Tax + Social security (NIC, student loans no mesmo FPS) | Full Payment Submission (FPS) | HMRC | Semanal/Mensal (a cada folha) | "On or before pay day." | "As an employer running payroll, you need to report your employee's pay, any payrolled benefits, and deductions in a Full Payment Submission (FPS)" (SOP impessoal, texto de gov.uk) | "E-filing using your payroll software." Link: RTI internet submissions 2025 to 2026 technical specifications. PACOTE: `FPS_<cliente>_202609.xml` + ACK do HMRC colado por Srikanth no Chat | SOP UK p. 7, 14, 21; PACOTE `United Kingdom\McDermott UK - 2026-09\01 Received\HMRC_acknowledgements_FPS_EPS_202609 (from Chat).txt` (IRmarks do ACK batem com os do XML, conferido) | 2024-10 |
| Tax + Social security | Employer Payment Summary (EPS), inclui reclamar SMP/SPP/SAP/ShPP/SPBP, Employment Allowance, CIS, Apprenticeship Levy | HMRC | Mensal | "By 19th of following tax month" | SOP impessoal | "E-filing using your payroll software." | SOP UK p. 7-9; PACOTE: `EPS_<cliente>_202609.xml` + ACK | 2024-10 |
| Tax | P45 (saída/rescisão) | HMRC (formulário entregue ao empregado) | Evento | "On Termination/ Resignation" | "On Termination/ Resignation, employer will generate P45 using payroll software and provide employees a copy." | payroll software | SOP UK p. 9-10 | 2024-10 |
| Tax | P60 End of Year Certificate | HMRC (entregue ao empregado) | Anual | "By 31st May after the end of the tax year." | "Use your payroll software to generate P60 at the end of tax year. Submit P60 to employees." | payroll software | SOP UK p. 10 | 2024-10 |
| Tax | P11D Expenses and Benefits | HMRC | Anual | "By 6th July after the end of the tax year." | SOP impessoal | "E-filing using your payroll software." (link gov.uk P11D/P9D) | SOP UK p. 11-12 | 2024-10 |
| Tax (só HUB) | P11D(b), CIS300, Gender Pay Gap, relatório de employment intermediary | HMRC; Equality (GPG) | anual/mensal/evento | HUB: só prazos do intermediary; resto n/d | SOP não cita | HUB: FPS/EPS são M2M | HUB `Reino-Unido.md` (Relatórios principais). **[Verify]** | n/a |
| Tax (entrada) | Avisos do HMRC: SL1, SL2, PGL1, PGL2 (student loan) | HMRC | Evento | n/a | "HMRC will tell you if you need to stop making loan deductions from your employees' pay. They'll send you: form SL2 for student loans / form PGL2 for postgraduate loans" | n/d | SOP UK p. 6 | 2024-10 |
| Payments | Pagamento de PAYE/NIC ao HMRC | HMRC | Mensal (HUB: n/d) | **n/d no SOP** | SOP não tem linha de pagamento. PACOTE: `Payment Report ... Monthly September.xlsx`, `Pension_Payment_Report` e arquivos de pagamento (`MYPAY_GBR_G1_092026...`, `mcd3...gpg`): conteúdo não identificado como pagamento ao HMRC | n/d | PACOTE `02 Validation\_extracted\`. **[Verify]**. monday (outro agente): Statutory Payments marcado em 0/8 clientes UK | n/a |

Evidência de quem envia no pacote McDermott UK: HUB registra "F-01: senha do Government Gateway em texto aberto nos arquivos do pacote". INFERÊNCIA: os envios FPS/EPS usam credencial do cliente no Government Gateway; **[Verify]** (não confirmado quem usa).
monday (outro agente): Statutory Filings marcado em apenas 1 de 8 clientes UK (reMarkable, Payroll HR Blizz); os outros 7 são "HR Support Services" (NGA) sem payroll. McDermott UK não aparece na lista de 8: conflito de escopo [Verify].

---

## 5. Ucrânia (UA)

**Sem SOP** em `Ukraine\01 - SOP`. Fontes: hub `brain-service\paises\Ucrania.md` (47 KB), pasta Drive `Ukraine\17 - Statutory Reports\DPS - State Tax Service\` (specs `UA-1PV-001`, `UA-1PV-002`, `UA-4DF-001`, `UA-D1-001`, `UA-D5-001`, `UA-D6-001`; oficiais: Poryadok 24/01/2025, F0510110.xsd), pacote `Ukraine\Altium - 2026-08` e `2026-09`. monday (outro agente): payroll "External Supplier" (ActivPayroll 4, Direct Lead 2); Filings 6/6; Payments 0/6. SOPs por cliente em Google Docs (Altium, SDL, GSK) não lidos.

| Parte | Entrega (nome oficial) | Autoridade | Frequência | Prazo | Quem envia hoje segundo o SOP (frase literal) | Canal citado no SOP | Fonte | Data do SOP |
|---|---|---|---|---|---|---|---|---|
| Tax | Declaração J05 (Podatkovyi rozrakhunok) com anexo 4DF (PDFO/imposto pessoal, Military levy) | DPS (State Tax Service) | Mensal (pessoa jurídica); só FOP: trimestral | n/d interno (HUB: PDFO/Military levy são **pagos** no momento da transferência do salário; 3 dias bancários só para dinheiro/espécie) | sem SOP. PACOTE: mensagem de Nataliia Hahan (SBC Ukraine) no Chat de 07/10: "Here is the Tax report" (zip "Unified PIT and SSC reports_August_2026") e "Receipt of the August Tax report" (`J1499202 Квитанція №2.pdf`). HUB: "Recibo DPS do J0500111 (aceito 21/09/2026)". Quem transmite à DPS: **não consta** | n/d. HUB: portal da DPS; XML assinado com KEP (para o 1-PV) | HUB `Ucrania.md` (linha 86: frequência 4DF/D1: Law 4536-IX, MinFin Orders 4/243/284, HRBS-12631); `Ukraine\Altium - 2026-08\01 Received\received.txt` | sem SOP |
| Social security | D1 (ESV: Unified Social Contribution), anexo do J05 | DPS | Mensal (FOP trimestral) | n/d | sem SOP (mesmo envio do "Unified PIT and SSC reports") | n/d | Specs Drive `UA-D1-001_..._v3.4.xlsx`; HUB (SR-160) | sem SOP |
| Other | D5 (Labour Relations): eventos de admissão/demissão | DPS | Por evento (7 tipos, HUB) | n/d | sem SOP | n/d | Spec Drive `UA-D5-001_..._v3.4.xlsx`; HUB (SR-162). **[Verify]** | sem SOP |
| Other | D6 (Special Seniority; formulário J0510611 v11) | DPS | Gatilho em 2 camadas (HUB) | n/d | sem SOP | n/d | Spec Drive `UA-D6-001_..._v3.2.xlsx`; HUB (SR-163). **[Verify]** | sem SOP |
| Other | 1-PV mensal (Звіт із праці, S0301016), staff = categorias 1-2 do D5 | Derzhstat (Державна служба статистики) | Mensal | n/d | PACOTE: Nataliia: "Here is the statistic report monthly"; recibo do 1-PV **não recebido** (hub) | Respondent's Cabinet (Кабінет респондента) (HUB, SR-415 PDF) | Spec Drive `UA-1PV-001_..._v5.3.xlsx`; HUB (SR-414, linha 99 e 120) | sem SOP |
| Other | 1-PV trimestral (S0301121) | Derzhstat | Trimestral | n/d | PACOTE: `Altium_1PV_3Q_2026.zip` | XML assinado com KEP, só eletrônico (HUB: Law 2524-IX art. 10(4), ⚠️ vigência?) | Spec Drive `UA-1PV-002_..._v1.5.xlsx`; HUB (SR-415). **[Verify]** | sem SOP |
| Other | Pedido ao Pension Fund (`Application_PF_08.xls`); relatório de licença médica do PF | Pension Fund | n/d | n/d | PACOTE: arquivo enviado pela Nataliia; função não descrita | n/d | `received.txt` (ago/26); HUB HRBS-12548 (itens 3-4 bloqueados) **[Verify]** | sem SOP |
| Payments | Pagamento de salário e impostos por banco | Banco / DPS | Mensal | PDFO/Military levy no momento da transferência (HUB) | PACOTE: `Altium_Payment report_08.pdf` ("Bank Payment report"), `31082026.DBF` ("Bank Payments file"), `Altium_1C Payments_Balance_08.xml` ("Bank Payments for 1C client"). Hub: cadeia bancária e GL fecham | arquivo DBF/XML para o banco | PACOTE `received.txt` (update de 09/10); HUB `Ucrania.md`. monday: Statutory Payments 0/6 (o pagamento de impostos fica com o cliente/ActivPayroll?) **[Verify]** | sem SOP |

---

## 6. Finlândia (FI)

**Sem SOP** e **sem pacote** da certificação (Marju Martinson não respondeu em 07/10 e 09/10; C-11). Fontes: hub `brain-service\paises\Finlandia.md` (skill `payroll-compliance-finland`) e Drive `Finland\09 - Alerts\2026\` (alertas de taxas, não filings). monday: SOPs por cliente em Google Docs (Signant Health, Orica, Henkel, Sherwin Finland) não lidos; Filings 5/5, Payments 0/5.

| Parte | Entrega (nome oficial) | Autoridade | Frequência | Prazo | Quem envia hoje segundo o SOP (frase literal) | Canal citado no SOP | Fonte | Data do SOP |
|---|---|---|---|---|---|---|---|---|
| Tax + Social security | Palkkatietoilmoitus (FI-RPT-001, earnings payment report) | Tulorekisteri (Incomes Register, Verohallinto) | A cada pagamento | "5 dias após o pagamento"; data de pagamento anda para trás (TSL 2:15) | sem SOP | SOAP/SFTP (HUB) | HUB `Finlandia.md` (Relatórios principais e armadilha 9). Só HUB: **[Verify]** | sem SOP |
| Tax + Social security | Työnantajan erillisilmoitus (FI-RPT-002, relatório separado do empregador) | Tulorekisteri | n/d | n/d | sem SOP | n/d | HUB `Finlandia.md`. **[Verify]** | sem SOP |
| Other | Invalidação de relatório (FI-RPT-003); formulários em papel TULOR 6101e/6103e | Tulorekisteri | evento | n/d | sem SOP | papel/portal | HUB `Finlandia.md`. **[Verify]** | sem SOP |
| Payments | Pagamento da retenção e do seguro-saúde do empregador (FI-PAY-004); multa por atraso €3 por dia (53/2018 § 23) | Verohallinto | n/d | n/d | sem SOP | n/d | HUB `Finlandia.md`. **[Verify]** | sem SOP |
| Other | Contribuições TyEL (seguradoras de pensão), Työllisyysrahasto | Seguradoras / Työllisyysrahasto | n/d | n/d | sem SOP | n/d | HUB lista os órgãos mas não os relatórios. Lacuna | sem SOP |

---

## 7. Estônia (EE)

**Sem SOP**, **sem pacote** (Marju Martinson não respondeu, C-11). Fontes: hub `brain-service\paises\Estonia.md` (skill `payroll-compliance-estonia`). monday: Bally Estonia, payroll HR Blizz, ActivPayroll; Filings 1/1, Payments 0/1; SOP por cliente em Google Docs não lido.

| Parte | Entrega (nome oficial) | Autoridade | Frequência | Prazo | Quem envia hoje segundo o SOP (frase literal) | Canal citado no SOP | Fonte | Data do SOP |
|---|---|---|---|---|---|---|---|---|
| Tax + Social security | TSD (Tulu- ja sotsiaalmaksu deklaratsioon) com anexo 1 (EE-RPT-01/02) | EMTA (Maksu- ja Tolliamet) | Mensal | n/d no hub. **Mudança em 01/10/2026**: TSD passa a data-based (anexos 1 e 2 se fundem, XBRL GL; CSV tolerado até o fim de 2027) | sem SOP | M2M via X-tee (`tsd/confirmTsd`, `getTsdStatus`, `getTsdFeedback`) segundo o HUB; XML atual deixa de valer em 01/10/2026 | HUB `Estonia.md` (Relatórios principais; armadilha 15; §3.1). Só HUB: **[Verify]** | sem SOP |
| Tax | TSD anexo 4 (fringe benefits, EE-RPT-04) | EMTA | Mensal | n/d | sem SOP | idem | HUB `Estonia.md`; códigos 4010/4020 do anexo 4 não localizados. **[Verify]** | sem SOP |
| Social security / Other | Registro de emprego TÖR | EMTA | Por evento | n/d | sem SOP | X-tee (`tor/TOOTREG/v2`) | HUB `Estonia.md`. **[Verify]** | sem SOP |
| Other | ESD e INF (INF 14 é o mais relevante) | EMTA | n/d | n/d | sem SOP | "canais ESD/INF assumidos por analogia (60%)" | HUB `Estonia.md`. **[Verify]** | sem SOP |
| Other | Certificado de rescisão da Töötukassa | Eesti Töötukassa | Por evento | n/d | sem SOP | n/d | HUB `Estonia.md` (formulário prescrito não lido, 65%). **[Verify]** | sem SOP |
| Payments | Pagamento dos impostos e contribuições do TSD | EMTA / Tervisekassa | n/d | n/d | sem SOP | n/d | **Sem fonte interna**; lacuna | sem SOP |

---

## 8. Irlanda (IE)

SOP: `Ireland\01 - SOP\SOP Ireland.pdf` (agosto de 2025). Tabela "SUMMARY OF REPORTS" p. 6 e texto "SUBMISSION DEADLINES AND PROCEDURES" p. 5. Marcas lidas no PDF: **In-Scope ☒, Add-On ☐, Online ☒, Manual ☐** para as cinco linhas. Hub: `brain-service\paises\Irlanda.md` (skill `payroll-compliance-ireland`). **Sem pacote** da certificação. monday (outro agente): os 5 clientes IE são "SaaS" (HR Blizz) com Filings e Payments **não marcados** e sem SBC: conflito com o SOP [Verify].

| Parte | Entrega (nome oficial) | Autoridade | Frequência | Prazo | Quem envia hoje segundo o SOP (frase literal) | Canal citado no SOP | Fonte | Data do SOP |
|---|---|---|---|---|---|---|---|---|
| Tax + Social security (PAYE, PRSI, USC) | Payroll Submission Request (PSR) | Revenue Commissioners | A cada período de pagamento | "on or before making payments to employees" / "on or before each pay date" | "Employers in Ireland are required to submit several statutory reports to the Revenue Commissioners." (SOP genérico, sem dizer se é a Mercans) | ROS (Revenue Online Service); HUB: M2M HTTP Signatures, assíncrono | SOP IE p. 4-6; HUB `Irlanda.md` | 2025-08 |
| Tax | Enhanced Reporting Requirements (ERR) | Revenue | A cada período (tempo real) | "Report specific non-taxable payments in real-time, as they occur." | idem | ROS; HUB: M2M | SOP IE p. 4-6 | 2025-08 |
| Tax | SARP Employer Return (Special Assignee Relief Programme) | Revenue | Anual | n/d (anual) | "Employers must submit an annual SARP Employer Return through the eSARP portal for employees availing of SARP relief." | eSARP portal, via ROS | SOP IE p. 4-5 | 2025-08 |
| Tax (entrada) | Revenue Payroll Notification (RPN) | Revenue | Antes de cada folha | "Obtain an up-to-date RPN for each employee before running payroll." | idem (é entrada, não envio) | ROS/API | SOP IE p. 4-5 | 2025-08 |
| Other | Gender Pay Gap report | Revenue / Gender Pay Gap Information Act 2021 | Anual | n/d (empregadores > 250 começaram em 2022) | "The Gender Pay Gap Information Act 2021 requires employers in Ireland to report their hourly gender pay gap" | n/d. HUB não cita este report: **[Verify]** | SOP IE p. 4, 6 | 2025-08 |
| Payments / Tax + Social security | Declaração e pagamento mensal (statement da Revenue) | Revenue | Mensal | Statement até dia 5; aceitar até dia 14; "Monthly: Return due 14 days after end of month; payment 14 days after the end of the month (23 days for ROS users who file and pay online)"; trimestral e anual com datas parecidas | "Based on the employer payroll submissions, Revenue will make a statement available to the employer by the 5th of the following month. The employer has until 14th of that month to accept the statement." | ROS; HUB: Variable Direct Debit | SOP IE p. 5; HUB `Irlanda.md` | 2025-08 |
| Social security / Other (só HUB/Drive) | NAERSA: arquivo de contribuição (AECS) e AEPN (My Future Fund / auto-enrolment) | NAERSA | Por folha (HUB: "duas remessas e dois pagamentos na mesma data") | n/d | SOP não cita | Portal (HUB; formato do arquivo ~70%, U3). Drive `12- Country Report Codes\NAERSA\` | HUB `Irlanda.md` (armadilha 7 e 16). **[Verify]** | n/a |
| Other (só Drive) | ERN (Employer Return Notification), Return Reconciliation Report, Payroll Submission Report, RPN Response | Revenue | n/d | n/d | SOP não cita | Drive `Ireland\12- Country Report Codes\` (pastas ERN, ERR, Payroll Submission Report, Return Reconciliation Report, RPN - Response) | Listagem de nomes. **[Verify]** | n/a |

---

## 9. Cazaquistão (KZ)

**Sem SOP.** Hub `brain-service\paises\Cazaquistao.md` (criado 27/10, sem skill nem ficha). Fontes oficiais lidas pela certificação em 14/10/2026 (adilet.zan.kz) estão em `internal-certification\references\Kazakhstan\2026\{facts,sources}.md` e `text\`. Pacote `Kazakhstan\Mastercard - 2026-10` (Malika Iskakova, In-Country Expert). monday (outro agente): 1 cliente, payroll "External Supplier", Filings e Payments **não marcados**.

| Parte | Entrega (nome oficial) | Autoridade | Frequência | Prazo | Quem envia hoje segundo o SOP (frase literal) | Canal citado no SOP | Fonte | Data do SOP |
|---|---|---|---|---|---|---|---|---|
| Tax + Social security | Форма 200.00 (declaração de ИПН e СН, que também leva ОПВ, ОПВР, СО, ОСМС) com anexo por empregado no 4T | KGD (Комитет государственных доходов) | Trimestral | 15 do 2º mês após o trimestre (4T/2026 = 15/02/2027, cálculo); (S01 arts. 445, 562) | sem SOP. PACOTE: Malika: "statutory report(s) and authority receipt not sent - filed quarterly"; em 19/10 mandou o `200-Tax declaration...` (recibo da KGD não consta). Quem transmite: **não consta** | n/d. Forma: MinFin Order 39 de 20/01/2020, anexos 121/122 (S05); aprovação específica 2026 sob o novo Código **não localizada**. Site da KGD inacessível (N1) | `references\Kazakhstan\2026\facts.md` §8; `received.txt`. Hub: F-06 High (folha de out declarada como 3º mês do 3T; C-18 em rascunho). **[Verify]** | sem SOP |
| Payments | ИПН (КБК 101201, КНП 911) | KGD | Mensal | até dia 25 do mês seguinte ao do pagamento (S01 art. 440 п.4) | sem SOP. PACOTE: pasta `Taxes Oct/03-10-26.1/` com 7 ordens de pagamento (ИПН, ОПВ, ОПВР, СО, СН, ВОСМС, ООСМС) | ordens de pagamento (preparadas no 1C ZUP) | `facts.md` §1 e §8; `received.txt` | sem SOP |
| Payments / Social security | ОПВ (10%, КНП 010) | GCVP / Fundo de pensões | Mensal | dia 25 do mês seguinte (S03 art. 248 п.9) | idem | idem | `facts.md` §3 | sem SOP |
| Payments / Social security | ОПВР (3,5%, КНП 089) | idem | Mensal | dia 25 | idem | idem | `facts.md` §4 | sem SOP |
| Payments / Social security | СО (5%, КНП 012) | GFSS | Mensal | dia 25 (S03 art. 246 п.1) | idem | idem | `facts.md` §5 | sem SOP |
| Payments / Tax | СН (6%, КБК 103101, КНП 911) | KGD | Mensal | dia 25 (S01 art. 560 п.1) | idem | idem | `facts.md` §6 | sem SOP |
| Payments / Social security | ВОСМС (2%, КНП 122) e ООСМС (3%, КНП 121) | FSMS | Mensal | dia 25 (S04 art. 30 п.6) | idem | idem | `facts.md` §7 | sem SOP |
| Other | Payroll file ao banco ("Salary Oct": transferência com arquivo Swift txt) | Banco | Mensal | n/d | PACOTE: `October 26.zip`, pasta `Salary Oct/` | arquivo Swift txt | `received.txt` | sem SOP |

---

## 10. Azerbaijão (AZ)

**Sem SOP, sem hub, sem pacote completo.** Pacote `Azerbaijan\Client TBD - 2026-09` (Pari Azizzade, e-mail de 12/10): `September Payroll Documents.zip` (protegido por senha) com `Bank payment September.pdf`, `PRE_Template_2026_PRE_AZ_September_2026.xlsm`, `September payslip.rar`, `Staff_list_English.xlsx`. **Rodada pulada em 14/10 por decisão do usuário; nada extraído.** "Not received: statutory report(s) as submitted + authority receipt, GL." Drive: `Azerbaijan\09 - Alerts\2026\` tem um alerta sobre mudança de taxas e seguridade social (jan/2026), lista de nomes apenas. monday (outro agente): 1 cliente, External Supplier, Filings e Payments **não marcados**.

| Parte | Entrega (nome oficial) | Autoridade | Frequência | Prazo | Quem envia hoje segundo o SOP (frase literal) | Canal citado no SOP | Fonte | Data do SOP |
|---|---|---|---|---|---|---|---|---|
| (lacuna) | Nenhuma entrega de payroll ao governo identificável no material interno | n/d | n/d | n/d | sem SOP. PACOTE: só "Bank payment September.pdf" indica pagamento de salários; nenhum relatório ou recibo estatutário recebido | n/d | `Azerbaijan\Client TBD - 2026-09\01 Received\received.txt` | sem SOP |

---

## 11. Rússia (RU)

**Sem nenhuma fonte interna.** Sem SOP (só Testfile em `Russia\01 - SOP`), sem hub, sem pacote da certificação, pastas `07/09/14` do Drive vazias. A única informação é do monday (outro agente): 4 clientes, payroll "External Supplier", Filings 4/4 marcados, Payments 0/4, Partner Direct Lead, SBC Sadaf Nishat (backup Salman Saeed).

| Parte | Entrega (nome oficial) | Autoridade | Frequência | Prazo | Quem envia hoje segundo o SOP (frase literal) | Canal citado no SOP | Fonte | Data do SOP |
|---|---|---|---|---|---|---|---|---|
| (lacuna) | Nenhuma entrega identificável no material interno | n/d | n/d | n/d | sem SOP | n/d | `dados/monday_12paises.md` (só flags de escopo) | sem SOP |

---

## 12. Noruega (NO), seção à parte

Está com outra pessoa; não levantado aqui. Já existe `...\fluxo-entregas-marko\paises\NO_fluxo_entregas.md`. Para conferência cruzada: o hub `Noruega.md` lista a-melding mensal (NO-RPT-001), Avstemmingsrapport, Sammenstilling anual, pagamento de forskuddstrekk (1º dia útil após a folha) e de arbeidsgiveravgift/finansskatt (bimestral, dia 15), RF-1354, inntektsmelding NAV, Oppdragsregisteret, Aa-register. `Norway\01 - SOP` só tem `NO_SOP V1.0 .gdoc` e `Norway Standard Operating Procedure (CSOP).gdoc` (gdoc: não lido).

---

## 13. Contagem de entregas por país

Contagem de linhas de entrega nas tabelas acima (inclui payments; exclui as linhas de "lacuna").

| País | Entregas listadas | Com SOP | Linhas só de HUB/Drive (a confirmar) |
|---|---|---|---|
| DK | 9 | sim (2022/23) | 3 (Samlet Betaling, pagamento A-skat/AM, FerieKonto/refusion/lønsumsafgift) |
| NL | 12 | sim (2021) | 1 (UWV/Correctiebericht) |
| SE | 6 | não | 6 (tudo hub/facts) |
| UK | 8 | sim (2024) | 2 (P11D(b)/CIS300/GPG; pagamento PAYE/NIC) |
| UA | 8 | não | 8 |
| FI | 5 | não | 5 |
| EE | 6 | não | 6 |
| IE | 8 | sim (2025) | 2 (NAERSA, ERN/Reconciliation) |
| KZ | 8 | não | 8 (norma + pacote) |
| AZ | 0 | não | lacuna |
| RU | 0 | não | lacuna |

Países sem SOP em disco: **SE, UA, FI, EE, KZ, AZ, RU** (7). SOPs desatualizados: DK (2022/23) e NL (2021).

---

## Bloco de prova

**Fontes lidas (inteiras ou nas seções citadas):**
- SOP DK docx (texto, tabelas e marcas de caixa); SOP NL docx e PDF (texto e tabelas; marcas conferidas por XML); SOP UK PDF (24 páginas, todas as páginas de filings e Reports Summary); SOP IE PDF (7 páginas, inteiro).
- Hubs `Dinamarca, Holanda, Suecia, Reino-Unido, Ucrania, Finlandia, Estonia, Irlanda, Cazaquistao` (seções de órgãos, relatórios principais, armadilhas, IC); `Noruega` só a linha de relatórios.
- `internal-certification\references\Kazakhstan\2026\facts.md` (inteiro até §9), `Sweden\2026\facts.md` §4, `Denmark\2026\facts.md` §3 (prazos).
- `received.txt` de DK (2), NL (3 + referência dos 6 Mammoet não lida), SE, UK, UA (2), KZ, AZ; `intake.md` de SE; lista de `_extracted` de UK, UA, NL, SE.
- Listagens do Drive: `12 - Country Report Codes` de DK, NL, SE, IE, UA; `17 - Statutory Reports` de UA; `01 - SOP` dos 12 países.
- `dados/monday_12paises.md` (outro agente, só como pista de escopo: flags de Filings/Payments e existência de SOPs por cliente).

**Conferido mecanicamente:**
- Extração de texto dos 4 SOPs por `python -I` (python-docx, pypdf); marcas ☒/☐ do DK e NL lidas do XML do docx (DK: três reports de Skat In-Scope+Online; três estatísticas Add-On+Online; NL: todas Add-On); marcas do IE lidas do PDF (In-Scope ☒, Online ☒ nas 5 linhas); marcas do UK vêm todas ☐ (não informativas).
- Datas dos SOPs: metadados internos do docx (`core.xml`) para DK e NL; mtime do arquivo para UK/IE.
- Frases literais copiadas da extração; eventuais quebras de linha do PDF foram juntadas.

**Confiança:** ~85% de que a lista cobre o que o material interno disponível em disco diz. Nenhum SOP por cliente (Google Docs) foi lido, então "quem envia hoje" está abaixo de 50% para SE, UA, FI, EE, KZ, AZ, RU. Para DK/NL/UK/IE as frases do SOP são literais, mas os SOPs de DK e NL são de 2021-2023 e o de UK/IE não diz quem transmite; esses ficam [Verify].

**O que falta:**
1. SOPs por cliente (Google Docs no monday) de DK, NL, SE, UA, FI, EE, que dizem quem envia hoje: precisam ser exportados como docx/pdf pelo usuário.
2. Prazos internos para UA (todos), FI (exceto 5 dias), EE (todos), KZ (aprovação do formulário 200.00 em 2026).
3. Pagamento de PAYE/NIC (UK), de impostos (EE, FI), de ESV (UA): nenhuma fonte interna.
4. Azerbaijão e Rússia: nenhuma fonte; precisam do SBC (Sadaf Nishat) ou de pesquisa externa fora deste escopo.
5. Os SOPs `Norway\...\*.gdoc` e `Ireland\...\Archived\SOP final version.docx` não abriram.
6. Linha BIR 2316 (Filipinas) no SOP do UK: confirmar com o dono do SOP.

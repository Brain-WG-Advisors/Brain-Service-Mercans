# Lições da Internal Certification para o próximo Research Pipeline

Fonte analisada (somente leitura): `C:\Users\instituto\Documents\internal-certification`, mais a memória e a transcrição do Claude (`C:\Users\instituto\.claude\projects\c--Users-instituto-Documents-internal-certification\8ae80473-…jsonl`; a pasta `memory\` está vazia) e o log `C:\Users\instituto\Documents\brain-service\log.md` (entradas de 14 e 15-10-2026).
Para cruzar os achados com as skills, as skills distribuídas no kit (`Internal_Certification_Kit_2_Skills.zip`) foram extraídas para o scratchpad (`…\scratchpad\kit2\`). Nada foi alterado na pasta de origem.

Convenções:
- **[INFERÊNCIA]** marca uma conclusão minha que não está escrita nas fontes.
- Os caminhos relativos partem de `internal-certification\`.

---

## 1. Inventário

**O que é.** A Internal Certification valida os statutory reports que o HRBLIZZ (Mercans) produz para clientes reais. Para cada pacote de um período fechado, o report enviado à autoridade é conferido com o recibo, o G2N, os contracheques, o GL, o arquivo bancário e os dados mestre, em 100% dos registros e contra a fonte oficial do ano. A regra é validar e reportar: não se refazem filings nem se prescreve configuração (`CLAUDE.md`, decisão D-04 de 14-10).

As skills `payroll-compliance-<país>`, que são o produto do Research Pipeline, entram só como **"mapa, não fonte"** (`PROMPT_VALIDACOES_PONTA_A_PONTA.md` §2; `PLANO_DE_ACAO_VALIDACOES.md` §3).

**Período do trabalho.** Pedidos às SBCs em 07-10-2026. A Ucrânia e o Reino Unido foram validados entre 07 e 09-10, a Holanda e a rodada NO/DK/SE/KZ em 14-10, e a planilha de acompanhamento foi gerada em 14-10 às 20:15. Os períodos de folha cobertos vão de agosto a outubro de 2026.

**Status por pacote** ([[internal-certification/Acompanhamento_Internal_Certification.xlsx|Acompanhamento_Internal_Certification.xlsx]], aba Painel)

| Pacote | Report | Pass | Finding | Not tested | Cobertura* | Recibo prova aceite? | Situação |
|---|---|---|---|---|---|---|---|
| NO-HENKEL (Henkel Norway AS, set/26) | A-melding v2.3 + tilbakemelding | 34 | 9 | 4 | 91% | Sim (GODKJENT) | Fechado |
| DK-SHERWIN (Sherwin-Williams Denmark A/S, set/26) | eIndkomst + SKAT Afstemning | 18 | 5 | 2 | 92% | Sim | Fechado |
| DK-KGS (KGS Fire & Security Danmark ApS, set/26) | eIndkomst + Afstemning | 15 | 5 | 4 | 83% | Sim | Fechado (banco fora do escopo) |
| NL-QUEST (Quest Software B.V., set/26) | Loonaangifte | 60 | 9 | 5 | 93% | Não | Falta recibo Digipoort |
| NL-SHERWIN (Valspar B.V., set/26) | Loonaangifte | 48 | 18 | 5 | 93% | Não (recibo de outro LH) | Falta recibo |
| NL-EXCERPTA (Excerpta Medica, set/26) | Loonaangifte | 60 | 5 | 5 | 93% | Não | Falta recibo |
| SE-ONEID (One Identity Sweden AB, set/26) | AGI | 19 | 6 | 6 | 81% | Não (Kvittens de outra entidade) | Falta recibo |
| KZ-MASTERCARD (rep. office, out/26) | Ordens de pagamento (200.00 não veio) | 14 | 6 | 5 | 80% | Não | Parcial |
| UA-ALTIUM-08 (Altium, ago/26) | Податковий розрахунок (4ДФ/Д1/Д5) + 1-ПВ | 33 | 13 | 12 | 79% | Parcial | Falta recibo |
| UA-ALTIUM-09 (Altium, set/26) | só G2N | 9 | 4 | 7 | 65% | Não | Parcial |
| UK-MCDERMOTT (McDermott UK, set/26) | FPS/EPS (RTI) | 50 | 4 | 17 | 76% | Não | Falta resposta HMRC |
| AZ (cliente a confirmar, set/26) | — | 0 | 0 | 0 | — | — | Pulado (zip AES + .rar) |
| FI, EE, IE, RU | — | — | — | — | — | — | Sem arquivos, sem SBC ou sem contato |

\*Cobertura calculada por mim com a fórmula da aba Legenda: (Pass + Finding) ÷ (Pass + Finding + Not tested).

**Achados abertos.** São 79 no total, todos com status "Aberto" na aba Achados: 10 High, 23 Medium, 30 Low e 16 Observation. Há ainda 7 ações de configuração ou processo, 16 cobranças e 4 decisões (aba Ações).

**Skills disponíveis no momento da validação.** As skills `payroll-compliance-*` estavam na lixeira de skills (`.claude/skills/.trash/…`, lista na transcrição de 14-10 15:11). A validação seguiu só com fontes oficiais baixadas. O kit `Internal_Certification_Kit_2_Skills.zip` empacota cópias de DK, EE, FI, IE, NL, NO, SE e UK, mais o `nl-payroll-validator`. Não há skill para Ucrânia, Cazaquistão, Rússia ou Azerbaijão. Para a Ucrânia foram usados os artefatos do Drive: `Ukraine_Country_Configuration_Guide_FY2026-V1_6.docx` e `Ukraine_Wage_Type_Catalogue_Mercans_V3_6.xlsx`. A V4.2 do WTC é um atalho `.gsheet` e não pôde ser lida.

---

## 2. Catálogo de achados

Legenda da coluna **Origem**:
- **CFG**: erro de configuração ou motor do HRBLIZZ no cliente. A skill, se tivesse sido aplicada, já trazia a regra certa.
- **SKILL**: lacuna, erro ou ambiguidade no artefato do pipeline (skill, CCG, WTC, Report Spec, DD ou Payslip).
- **SKILL+CFG**: erro de configuração que a lacuna da skill não preveniu.
- **TPL**: template global de rótulos ou documentos do HRBLIZZ.
- **DADO**: dado mestre ou do cliente.
- **PROC**: processo de entrega do pacote (arquivo errado, recibo ausente).

Na coluna **Artefato**, a referência a um arquivo de skill indica onde a regra está, ou onde deveria estar.

### 2.1 Achados dos pacotes (aba Achados do tracker)

| ID | País/cliente | Achado (valor real) | Origem | Artefato do pipeline afetado | Sev. | Evidência |
|---|---|---|---|---|---|---|
| NO-F01 | NO Henkel | Contribuição sindical (G2N 21126, 552 NOK × 4) não deduzida da base do trekk nem informada como fradrag "fagforeningskontingent" na A-melding. 1.036 NOK retidos a mais em setembro, padrão o ano todo | CFG. A skill está certa: `payroll-compliance-norway/SKILL.md` regra 7; `02-wtc.md` 8.04 (cap 8.700); `06-payslip.md` B5 | WTC: flag "reduz base do trekk" + código de fradrag no Report Spec | High | `Norway/Henkel…/02 Validation/review/curated.py`; `references/Norway/2026/sources.md` S13/S14 |
| NO-F02 | NO Henkel | "Skattepliktig inntekt" do contracheque exclui benefícios (carro, seguros) que estão na base do trekk | CFG/Payslip. A skill exige base especificada (`06-payslip.md` B5) | Payslip Generator | Medium | idem |
| NO-F03 | NO Henkel | Provisão de férias no GL 69.341,85 contra G2N/contracheque 47.099,61; suplemento de 60+ zerado no contracheque e presente no G2N | CFG | WTC/GL mapping | Medium | idem |
| NO-F04 | NO Henkel | Rodapé do GL imprime 808.367,52, mas as linhas somam 832.018,75 | CFG/TPL | — | Low | idem |
| NO-F05 | NO Henkel | Prêmio OTP lançado despesa contra despesa | CFG | GL mapping | Obs | idem |
| NO-F06 | NO Henkel | Master: nacionalidade "Canada" para 6 noruegueses; 62100 ≠ salário; Employment ID vazio | DADO | DD (regras de validação de master) | Obs | idem |
| DK-SH-F01 | DK Sherwin | Fratrædelsesgodtgørelse declarada no felt 0069 líquida (571.251) em vez de bruta (579.251,40), contrariando a vejledning §8.4.3 | SKILL+CFG. A skill diz "felt 69, tax-free bottom slice 8.000" (`01-ccg.md` l.629-631; `02-wtc.md` DK-6010), mas não diz que o 0069 leva o valor bruto | Report Spec eIndkomst (regra de população do campo) | Medium | `Denmark/Sherwin…/review/curated.py` |
| DK-SH-F02 | DK Sherwin | O arquivo de upload do pacote difere do que o SKAT recebeu (0013/0069); CPR com hífen | PROC/DADO | DD (formato do CPR: 10 dígitos) | Obs | idem; `_skat.txt` |
| DK-SH-F03 | DK Sherwin | Store bededag 0,45% sobre salário + benefícios, sem a pensão do empregador. Pela LOV 214/2023 seriam 4.035,60 em vez de 3.907,67. A KGS, no mesmo motor, usa salário + pensão | SKILL (ausente). Zero ocorrências de "bededag" na skill DK | CCG/WTC DK | Obs | idem |
| DK-SH-F04 | DK Sherwin | Base do ferietillæg/feriegodtgørelse inclui fri bil, telefone e seguro-saúde, que o FL §19(2) exclui [INFERÊNCIA da validação] | SKILL (parcial). `SKILL.md` regra 10 trata só dos add-backs (pensão e AM), não da exclusão de benefícios mantidos nas férias | CCG/WTC DK (flag "ferieberettiget") | Obs | idem |
| DK-KGS-F01 | DK KGS | Seguro-saúde (62610, 86,69 DKK × 5) fora do 0013 e sem felt 0026: AM 6,94 e A-skat ~29-37 por pessoa/mês não retidos. A Sherwin tributa o mesmo benefício | SKILL+CFG. A skill DK-4020 deixa o AM como `[VERIFY]` e manda só para o felt 13, sem o 0026 (`02-wtc.md` l.94) | WTC DK + Report Spec (0026) | **High** | `Denmark/KGS…/review/curated.py`; `references/Denmark/2026/facts.md` A1 |
| DK-KGS-F02 | DK KGS | Contracheques sem CPR; o do desligado mostra "A-SKAT 0,00 / fradrag 0,00" ao lado de 6.286 retidos; YTD inconsistente | CFG/Payslip | Payslip Generator | Medium | idem |
| DK-KGS-F03 | DK KGS | Contas do GL rotuladas errado ("Pension skyldig" com líquido; "ATP skyldig" com A-skat); G2N soma a coluna de CPR no GRAND TOTAL | TPL | — | Low | idem |
| NL-Q-F01 / NL-SW-F03 | NL Quest, Sherwin | AantVerlU = 176 (22 dias × 8) para mensalistas, quando o Handboek §29.9 pede a média 173 (40 × 52 / 12). Na Sherwin, 190 de 222 IKVs | SKILL (ausente). `04-reports-spec.md` l.357 e `05-data-dictionary.md` W18 dizem só "paid hours in the period", sem a regra de média para salário mensal fixo | Report Spec / DD NL | Medium | `Netherlands/_tool/curated.py`; workbooks v1.1 |
| NL-Q-F02 | NL Quest | Contracheque final do desligado imprime 173,33 h sem salário pago | CFG/Payslip | Payslip | Low | idem |
| NL-Q-F03 | NL Quest | 2º SEPA inválido (separador de milhar em InstdAmt/CtrlSum, EndToEndId repetido, nome de outro cliente "Kantar") | CFG/TPL | SIR (formato bancário) | Medium | idem |
| NL-Q-F04 / NL-SW-F09 | NL Quest, Sherwin | Rótulos do GL com regimes de outros países: "6064 - EOBI (employer)" para Zvw, "6068 - EIS" para AWf, "Social Fund", "Premium WE Revised" | TPL. Catálogo global de elementos com nomes de PK/MY | WTC (rótulo local por elemento global) | Low | idem |
| NL-Q-F05 / NL-EX-F05 | NL Quest, Excerpta | "Wage Tax Overview" imprime prazo 30-10-2026; o oficial (tijdvakcode 6090) é 31-10-2026 | CFG/TPL | Report Spec (calendário de prazos) | Low | idem |
| NL-Q-F06 | NL Quest | Arbeidskorting declarada 2,25; a tabela dá 0,00 | CFG | — | Obs | idem |
| NL-Q-F07 | NL Quest | Compra de férias deduzida do líquido, sem reduzir o salário fiscal | CFG/contrato | — | Obs | idem |
| NL-Q-F08 / NL-EX-F06 | NL Quest, Excerpta | Sem resposta Digipoort ou recibo da Belastingdienst; o "Wage Tax Overview" é do HRBLIZZ | PROC | SIR (o que conta como recibo) | High | idem |
| NL-Q-F09 | NL Quest | Whk declarada 1,45%; pequeno empregador do setor 42 → 1,25% [INFERÊNCIA pelo porte] | CFG/DADO | CCG (tabela setorial Whk: a QA da skill NL admite U1, tabela de 69 linhas ~85%) | Obs | idem; `payroll-compliance-netherlands/references/07-qa-report.md` l.511 |
| NL-Q-F10 / NL-EX-F07 | NL Quest, Excerpta | Contracheque soma indenização/transitievergoeding (SrtIV 62) na coluna SV-loon; o retorno está certo | CFG/Payslip | Payslip | Medium | idem |
| NL-Q-F11 / NL-EX-F08 | NL Quest, Excerpta | Home allowance de €100 e auxílio-telefone isentos sem designação WKR (isenção específica €2,45/dia) | CFG/contrato | WTC (já tem NL-401 €2,45) | Obs | idem |
| NL-SW-F01 | NL Sherwin | O recibo Digipoort é de outro loonheffingennummer (868240503L01) | PROC + proteção de dados | — | High | idem |
| NL-SW-F02 | NL Sherwin | Desligado em idade AOW: 155,82 de imposto regular, quando a coluna AOW dá 0,00 | CFG. A skill tem as colunas AOW (`01-ccg.md` l.170-212) | Motor/WTC | High | idem |
| NL-EX-F01 | NL Excerpta | Empregado em idade AOW desde 26-01-2026: retenção 452,16, valor que não existe em nenhuma coluna; a tabela dá 485,08. Retido −32,92 | CFG | Motor | High | idem |
| NL-SW-F04 | NL Sherwin | Jaarloon BT 0,00 no contracheque com tarifa especial aplicada | CFG/Payslip | Payslip | Medium | idem |
| NL-SW-F05 | NL Sherwin | Alleenstaandeouderenkorting aplicada sem evidência de direito (€19,83) | DADO | — | Obs | idem |
| NL-SW-F06 | NL Sherwin | Reden einde 99 usado como fallback | CFG | DD (lista de códigos com regra de uso) | Medium | idem |
| NL-SW-F07 / NL-EX-F02 | NL Sherwin, Excerpta | Imposto por fórmula, não por tabela: 58 IKVs (Sherwin) e 19 (Excerpta) com diferença de €0,01 a 0,09 | CFG | CCG (regra "tabela é normativa") | Low | idem |
| NL-SW-F08 | NL Sherwin | "In dienst" = data de admissão original, e não a data com o LH | CFG/Payslip | — | Low | idem |
| NL-SW-F10 | NL Sherwin | Indicadores ZVW/WW/WIA do contracheque contradizem o retorno em 6 casos | CFG/Payslip | Payslip | Medium | idem |
| NL-SW-F11 | NL Sherwin | Coluna "Tabel" do contracheque omite o elemento 62730 em 8 casos; imposto correto | CFG/Payslip | Payslip | Medium | idem |
| NL-EX-F03 | NL Excerpta | Bloco de correção de agosto com saldo 0 | DADO | — | Obs | idem |
| NL-EX-F04 | NL Excerpta | Loonheffingskorting em 2 IKVs do mesmo desligado (verde 43,96%); se indevida, €70,29 | CFG (regra do motor) | CCG (LHK em 2ª IKV) | Obs | idem |
| SE-F01 | SE One Identity | Sem Kvittens desta entidade; o Kvittens e o master são da Quest Software AB 556602-0433 | PROC + dados de outra entidade | — | High | `Sweden/Quest Software…/02 Validation/intake.md` |
| SE-F02 | SE One Identity | Payout de férias salvas (79421) retido pela tabela mensal, e não pelo engångsbelopp (SFL 11 kap. 17 §). Elisabeth: 5.543 SEK a menos | CFG. A skill está certa: `02-wtc.md` SE-SEM-07 método ENG; `01-ccg.md` §4.3 | WTC (método de retenção por elemento) | High | `…/review/curated.py` |
| SE-F03 | SE One Identity | Contracheque: imposto acumulado = imposto do período (ex.: bruto YTD 3.576.682,20 contra skatt YTD 289.167) | CFG/Payslip | Payslip | Medium | idem |
| SE-F04 | SE One Identity | FK487 = 466.506 (arredondado) contra o método Skatteverket 466.505 (öre descartado, §12.6.1) | CFG | Report Spec AGI (regra de arredondamento) | Low | idem |
| SE-F05 | SE One Identity | Admissão com imposto que só a tabela 39 produz; nenhum município tem tabela acima de 37 | DADO | — | Obs | idem |
| SE-F06 | SE One Identity | Endereços inconsistentes (Houston TX no contracheque contra Sollentuna na AGI) | DADO | — | Obs | idem |
| KZ-F01 | KZ Mastercard | ИПН 40.589,78 acima do cálculo do mês (40.034,85 sem dedução básica); a conferência exige o YTD (art. 441) | DADO (falta YTD) | — | Obs | `Kazakhstan/…/review/curated.py` |
| KZ-F02 | KZ Mastercard | Contracheque com "Total deducted" = bruto, líquido 0,00, 20 dias contra 21 e arquivo chamado "August" | CFG/Payslip | Payslip | Medium | idem |
| KZ-F03 | KZ Mastercard | PRE template com datas de julho, PR560 em dobro (909.883,40), #NAME?, nº de empregado errado | TPL | — | Medium | idem |
| KZ-F04 | KZ Mastercard | СО arredondado para cima (+0,62 KZT); a regra de arredondamento não foi localizada | CFG + lacuna de referência | CCG KZ (inexistente) | Low | `references/Kazakhstan/2026/facts.md` |
| KZ-F05 | KZ Mastercard | Rótulos de СН e СО trocados no funding/GL | TPL | WTC (rótulos) | Low | idem |
| UA-08-F01 | UA Altium ago | 32 de 42 contracheques omitem o benefício in natura compensado no líquido (222.175,45) | CFG/Payslip | Payslip UA | Medium | `Ukraine/Altium - 2026-08/02 Validation/_scripts/checks_08.py` |
| UA-08-F02 | UA Altium ago | Norma de agosto 19 dias/152 h; sob lei marcial seriam 21/168. Proporcionalização /19 superestima 19.370,33 UAH | CFG + SKILL desatualizada. O CCG V1.6 diz "martial law extended to 4 May 2026"; a extensão vigente vai até 31-10-2026 | CCG UA (calendário/lei marcial) | Medium | `_evidence/ref_CCG_V1_6.txt` l.5; `build_workbooks.py` S-10 |
| UA-08-F03 / UA-09-F01 | UA Altium | Férias pagas depois do prazo de 3 dias antes do início (3 casos em agosto, 6 em setembro) | CFG/processo | CCG (timing) | Medium | idem |
| UA-08-F04 / UA-09-F03 | UA Altium | PIT do código 126 com ±0,01 em relação a 18% da renda grossed-up | CFG (arredondamento) | — | Low | idem |
| UA-08-F05 | UA Altium | Resíduo de 0,01 do ЄСВ alocado numa linha do Д1 | CFG | Report Spec Д1 | Low | idem |
| UA-08-F06 | UA Altium | Categoria 47 (mobilizados) inclui prêmio que é categoria 1 | CFG | Report Spec Д1 / WTC (categoria por elemento) | Low | idem |
| UA-08-F07 | UA Altium | G2N EN rotula o adiantamento como "Net Pay"; data de desligamento vazia; .xlsx que é BIFF | TPL | — | Low | idem |
| UA-08-F08 | UA Altium | Datas de pagamento conflitam entre 1C, banco e G2N (31.08 contra 04.09) | DADO/PROC | — | Low | idem |
| UA-08-F09 | UA Altium | GL sem o lançamento do código 126 (222.175,45) | CFG | GL mapping | Low | idem |
| UA-08-F10/F11 | UA Altium | Data de nascimento com dia/mês trocados (contra o RNOKPP); data de admissão divergente | DADO | DD (validação cruzada DOB × RNOKPP) | Low | idem |
| UA-08-F12 | UA Altium | Part-time registrado como Full Time com salário 1.888 | DADO | DD | Medium | idem |
| UA-08-F13 | UA Altium | Contratado pago em conta que não é IBAN | DADO | DD (formato IBAN UA) | Low | idem |
| UA-09-F02 | UA Altium set | Auxílio-doença do Fundo recuperado como "Overpayment in August" (−8.907,15) e PIT/ML repetidos | CFG | CCG (sick benefit/carry-forward) | Medium | `Ukraine/Altium - 2026-09/…/checks_09.json` |
| UA-09-F04 | UA Altium set | Folha de setembro intitulada "за серпень" | TPL | — | Low | idem |
| UK-F01 | UK McDermott | FPS/EPS com o Sender ID e a senha do Government Gateway em texto claro, circulando no zip do Chat | CFG/PROC. A skill está certa: `payroll-compliance-unitedkingdom/references/03-sir.md` l.97-102 manda redigir a cópia armazenada | SIR (redação de credencial no arquivo) | High | `United Kingdom/…/_scripts/build_workbook.py` F-01 |
| UK-F02 | UK McDermott | "Payroll ID changed" = yes em 65 de 69 registros, todo mês | CFG. A skill está certa: `04-reports-spec.md` item 39 | Report Spec FPS | Medium | idem |
| UK-F03 | UK McDermott | NIC do empregador arredonda meio pêni para cima, contra a regra do CWG2 §1.7 (£0,005 desconsiderado) | CFG. A skill está certa: `01-ccg.md` l.156 | Motor | Low | idem |
| UK-F04 | UK McDermott | Faixa avançada escocesa: diferença de 1p (constantes do motor) | CFG | — | Low | idem |
| UK-F05 | UK McDermott | YTD do contracheque ≠ FPS 79A em £1,25 | CFG/Payslip | Payslip | Low | idem |
| UK-F06 | UK McDermott | Desligado reenviado com data de saída e pagamento zero, sem indicador de "payment after leaving" | CFG | Report Spec FPS (itens 41/51) | Low | idem |
| UK-F07 | UK McDermott | Arquivos live com comentários dos samples do HMRC e Timestamp de teste | TPL | Report Spec (template de produção derivado de sample) | Low | `_evidence/schematron_validation.txt` |
| UK-F08 | UK McDermott | KIT Days sem horas no contracheque [INFERÊNCIA] | CFG/Payslip | Payslip | Low | idem |

### 2.2 Achados sobre os próprios artefatos e skills (revelados ao usar a certificação)

| ID | Artefato | Achado | Sev. (minha) | Evidência |
|---|---|---|---|---|
| SK-01 | Distribuição de skills | As 8 skills `payroll-compliance-*` usadas como mapa estavam na lixeira (`.claude/skills/.trash/`) no dia da validação, junto com BE, ES, FR, DE, CZ e outras. O validador teve de trabalhar sem elas, e o kit passou a empacotar cópias | High | transcrição 14-10 15:11; `Internal_Certification_Kit_2_Skills.zip` |
| SK-02 | Skill DK | 46 marcadores `[VERIFY]` não resolvidos numa skill entregue. DK-4020 (seguro-saúde) tem o AM em `[VERIFY]` e a certificação achou um High exatamente nesse item | High | `kit2/…/payroll-compliance-denmark/references/02-wtc.md` l.94; contagem por grep |
| SK-03 | Skill DK | Store bededag (suplemento 0,45%, LOV 214/2023) ausente da skill | Medium | grep "bededag" = 0 |
| SK-04 | Skill DK | Felt 0069 sem a regra "valor bruto antes dos 8.000"; felt 0026 (seguro-saúde) não citado | Medium | `01-ccg.md` l.629-631 |
| SK-05 | Skill DK | Sem fixação da versão vigente da Indberetningsvejledning: v16.9 vale 01.07–31.08.26 e v17.0 a partir de 12.10.26, sem versão listada entre 01.09 e 11.10 | Low | `references/Denmark/2026/facts.md` l.4 |
| SK-06 | Skill NL | Regra de AantVerlU para salário mensal fixo (média 173) ausente; causou um Medium recorrente em 2 clientes | Medium | `payroll-compliance-netherlands/references/04-reports-spec.md` l.357 |
| SK-07 | Skill NL | 5 `[VERIFY]` e lacuna U1 (tabela setorial Whk ~85%) admitidas na própria QA da skill | Low | `07-qa-report.md` l.45, 511 |
| SK-08 | nl-payroll-validator v1.4 | Desatualizada para o ano: resumos `.md` só de 2025 (rates, codes e controls-2025); para 2026 só os PDFs; `validate.py` com `FREQ="4weken"` por padrão, enquanto os clientes de 2026 são mensais; parser da tabela que **descartava linhas**. Recuperada da lixeira e corrigida para a v1.5 (2026 mensal, 4 correções, regressão idêntica nos 3 pacotes) | High | `Netherlands/_tool/validate.py` l.30-64; `brain-service/log.md` 14-10 |
| SK-09 | CCG UA V1.6 | Status da lei marcial desatualizado ("Extended to 4 May 2026, 18th extension"); a extensão vigente vai até 31-10-2026 | Medium | `_evidence/ref_CCG_V1_6.txt` l.5 |
| SK-10 | CCG UA V1.6 | Contradição interna no teto do ЄСВ: "15× MW" (l.70, 74) contra "20× MW" (l.101, 149). 172.940 = 20 × 8.647 | Medium | idem; `build_workbooks.py` S-13 |
| SK-11 | CCG UA V1.6 | Gross-up de BIK "÷ 0,77" (18% + 5%, l.252/262). O arquivo real usa ÷ 0,82 (5.166,80 → 6.300,98), e a posição da DPS (ЗІР) é não aplicar o coeficiente ao military levy [INFERÊNCIA: a fórmula do CCG está errada] | High | idem; `checks_08.json` |
| SK-12 | CCG UA V1.6 | A correção da V1.2 (sem piso de ЄСВ no mês de admissão ou desligamento) não chegou a todas as ocorrências. Ainda há "Joining month: … prorated, min base 4.740,61" (l.161) e o exemplo com "prorated min base 5.858,61" (l.326) | Medium | idem |
| SK-13 | CCG UA V1.6 | Valor não verificado entregue: "UAH 320,000 … approximately — verify exact amount" (l.172) | Low | idem |
| SK-14 | CCG/WTC UA (histórico) | Cadeia de correções pós-entrega vindas da operação real (HRBS-12631, HRBS-14331, migração 1C→HRB): piso de ЄСВ, proporcionalização por dias úteis, momento de remessa do PDFO, base de média para férias (Poryadok 100 п.4), janela de férias, regra de 2 meses para viagem/doação | High (padrão) | `ref_CCG_V1_6.txt` l.550-560; `ref_WTC_V3_6.txt` l.13-19 |
| SK-15 | Report Specs UA | Não existe spec do formulário principal J0500111, ao qual o LINKED_DOCS dos anexos deve apontar. As ordens 243/284 (vigentes desde 17-07-2026) passaram o C_DOC_VER para 11, e a SPR_VER de 06-03-2026 só tinha a v10 | High | `brain-service/log.md` 14 e 15-10 |
| SK-16 | WTC UA | A V4.2 é um atalho `.gsheet` e não pode ser lida fora do Google; a validação usou a V3.6 | Medium | `build_workbooks.py` S-13 |
| SK-17 | Sem skill | KZ: novo Código Tributário 214-VIII em vigor desde 01-01-2026. Ele revoga o código de 2017: СН 6% sem dedução do СО, ИПН 10%/15% cumulativo (art. 441), fim do ajuste de 90%, ОПВР 3,5%. Uma base montada sobre o código de 2017 estaria inteiramente errada | High (risco) | `references/Kazakhstan/2026/facts.md` |
| SK-18 | Config NL (fora da pasta) | HRBS-14394: o PE 52990 "Maximum SS Base" mostra 5.509 contra 6.617,42 de 2026 (valor do ano não atualizado) | Medium | `brain-service/log.md` 15-10 |
| SK-19 | Skills NO, SE, UK | Corretas em todos os pontos testados: sindicato §5-9, AGA, G 136.549, skattetrekkskonto abolida, SE-SEM-07 ENG, youth 20,81 com truncamento, item 39 do FPS, regra de £0,005, redação de senha. Os erros desses países são de configuração | — (positivo) | greps em `kit2/…` |

---

## 3. Gaps dos artefatos e skills que a certificação revelou (generalizados)

1. **A skill certa não chega à configuração.** Em NO-F01, SE-F02, UK-F01/02/03 e NL AOW, a regra estava correta na skill ou no WTC e mesmo assim a folha saiu errada. Falta o elo rastreável entre a linha do WTC e o elemento configurado no cliente.
   A própria leitura da transcrição (14-10 17:21) conclui: "Nenhum erro está na fórmula de cálculo. Todos estão na configuração dos itens de folha."
   Consequência: o WTC é o artefato de maior risco. Ele precisa de flags testáveis (base de imposto, base de contribuição, campo do report, método de retenção) e de um diff contra a configuração real.
2. **Configuração divergente entre clientes do mesmo país e do mesmo motor.** Seguro-saúde e base do Store bededag diferem entre Sherwin e KGS; a Quest bate a tabela NL exatamente, enquanto a Excerpta e a Sherwin calculam por fórmula. O artefato do país não funciona como baseline obrigatório.
3. **Marcadores `[VERIFY]` e valores "approximately — verify" em artefatos publicados.** São 46 na DK e 5 na NL, mais o CCG UA l.172. A certificação achou um High exatamente num `[VERIFY]` (DK-4020).
4. **Regras de população de campo incompletas nos Report Specs/DD.** A skill diz qual campo existe, mas não como preencher no caso difícil:
   - 0069 bruto antes da isenção;
   - 0026 para seguro-saúde;
   - AantVerlU como média para mensalista;
   - categoria 1 contra 47 no Д1;
   - FK487 com öre descartado por alíquota;
   - itens 41/51 do FPS para pagamento após desligamento.
5. **Regras de arredondamento.** Aparecem em NL (tabela contra fórmula), UK (meio pêni), SE (FK487), KZ (СО, regra NOT LOCATED) e UA (kopeck no 126 e no Д1). O artefato precisa dizer, por valor, a direção do arredondamento e se a tabela é normativa.
6. **Valores do ano e status temporais desatualizados.** Aparecem em:
   - lei marcial UA até 04-05-2026;
   - versão do formulário UA (C_DOC_VER 10 → 11 em julho/2026);
   - teto SS NL 5.509 contra 6.617,42;
   - nl-payroll-validator com referências de 2025;
   - KZ com código novo em 2026.

   Leis e especificações mudam no meio do ano: skattevedtak NO alterado em 19-06-2026; eIndkomst v16.9/v17.0; ordens UA 243/284. O artefato precisa de "valid_from/valid_to" e de um gatilho de revisão.
7. **Correções parciais que não se propagam.** O CCG UA corrigiu o piso do ЄСВ num lugar e deixou o exemplo antigo em outros dois. O CCG UA também afirma 15× e 20× MW para o mesmo teto.
8. **Payslip Generator sem asserções testáveis.** Defeitos de contracheque apareceram em todos os países (NO, DK, SE, KZ, NL, UA, UK):
   - YTD de imposto = período;
   - totais errados;
   - CPR ausente;
   - SV-loon com indenização;
   - colunas de tabela sem elemento;
   - indicadores contraditórios;
   - benefício in natura omitido.

   O spec descreve o conteúdo, mas não traz invariantes verificáveis (roll-forward, soma das linhas = total, campos iguais ao report).
9. **Rótulos globais vazando para o país.** GL NL com "EOBI", "EIS" e "Social Fund"; СН/СО trocados no KZ; adiantamento chamado "Net Pay" no G2N EN da UA. O baseline global de elementos precisa de nome local obrigatório por país no WTC.
10. **SIR e Report Spec sem higiene de template de produção.** O FPS live trazia comentários do sample do HMRC e Timestamp de teste. A credencial ficou em texto claro em cópia arquivada; a skill UK já alertava, mas não havia check.
11. **Recibo da autoridade não modelado como artefato.** Os pacotes NL e SE trouxeram o "Wage Tax Overview" do HRBLIZZ ou o Kvittens de outra entidade. O SIR deve especificar o que é prova de aceite por país (tilbakemelding/GODKJENT, SKAT Afstemning, Digipoort status, Kvittens, HMRC ack, квитанція ДПС №2) e os identificadores que a ligam ao report.
12. **Cobertura de países.** Não há base de UA, KZ, RU e AZ em formato de skill; para a UA há artefatos no Drive em `.gsheet` ilegível offline. Para o KZ, a mudança de código em 2026 mostra que o mandato de país precisa checar se a lei foi substituída por inteiro.
13. **Formato de distribuição.** Skills foram apagadas ou movidas sem aviso, o WTC só existia como atalho `.gsheet` e as skills tiveram de ser empacotadas manualmente num zip. Falta um canal de entrega versionado e verificável (hash).

---

## 4. Metodologia e ferramental reutilizáveis, e como viram gate do pipeline

### 4.1 Método em 8 etapas (`PLANO_DE_ACAO_VALIDACOES.md` §1)

| Etapa | O que faz | Lição registrada |
|---|---|---|
| 0 Intake | Inventário com sha256; extração para `_extracted`; entidade, período, frequência, moeda e headcount lidos dos documentos; recibo do mesmo report | Recibo da Sherwin NL era de outro LH; o Kvittens SE era de outra entidade |
| 1 Base legal | Download da autoridade, na versão em vigor no período; `sources.md` com URL, versão, data de leitura e sha256; cada item termina como valor, NOT LOCATED, OUT OF SCOPE ou N/A | Tabelas em PDF: ler por posição (pdfplumber) e conferir a contagem de linhas, porque o pdftotext perdeu linhas |
| 2 Decisões de método (gate) | Escolhas que mudam o resultado são decididas por um humano antes do teste | NL: loon-in × loon-over (`systematiek-determination.md`: "opposite answers on the same file"); NO/DK: sem skattekort, testar consistência |
| 3 Parsers | Mapeamento de colunas **lido do arquivo de cada cliente** (`Netherlands/_tool/clients.py`) | Os 3 G2N NL tinham layouts diferentes; contracheques em PT/EN/NL com números US/EU |
| 4 Recálculo | Imposto e contribuições por empregado, com tabelas oficiais, regras de idade, teto e arredondamento | Coluna AOW; centavos de fórmula × tabela |
| 5 Amarrações | Report ↔ G2N ↔ contracheque (âncora) ↔ banco ↔ payment report ↔ GL ↔ master; débito = crédito; população | Retroativo loon-over concilia no total com os saldos de correção |
| 6 Revisão | Cada exceção automática é lida na fonte; override em `review/curated.py` | ~40% das exceções da Holanda eram falsos positivos do script |
| 7 Entrega | Workbook (Cover, Executive Summary qualificado, Assumptions, Findings, Coverage, Reconciliation, Recalculation, Not Tested, Sources), resumos EN/PT, `followups.md` em rascunho, `.done/validated` | Severidade única High/Medium/Low/Observation; nunca "all correct" |

### 4.2 Ferramental existente (reaproveitável como gate)

**`validators/common/`**
- `framework.py`: classe `Evidence`, com o `checks.json` padrão (checks / recon / not_tested / recalc / exceptions) e `TOL = 0,005`.
- `intake.py`: sha256 e extração; nunca escreve em `01 Received`. No kit v2 ganhou bloqueio de zip slip, zips aninhados e caminhos com mais de 260 caracteres.
- `hrb.py`: leitores genéricos do G2N e do GL Report do HRBLIZZ, com cabeçalho de metadados e `.xls` via xlrd.
- `bank.py`: pain.001 (NbOfTxs, CtrlSum).
- `pdfwords.py`: palavras com posição, para desenhar leitores de contracheque.
- `build_workbook.py`: workbook padrão a partir do `checks.json` + `curated.py`.
- `tracker.py`: painel de acompanhamento; recusa sobrescrever.

**Por país**
- `validators/no/no_check.py` + `trekk.py`: trekktabeller 2026 em formato texto (tabela 4 | período 1 | tipo 1 | grunnlag 6 | trekk 6; regra "maior grunnlag ≤ base").
- `dk/dk_check.py`: eIndkomst contra a SKAT Afstemning, campo a campo.
- `se/se_check.py`: XSD AGI 1.1, FK497 = ΣFK001, FK487 pelo método Skatteverket, tabela/engångsbelopp, frånvaro §5.6.
- `kz/kz_check.py`: recálculo de ИПН, ОПВ, ОПВР, СО, СН e ОСМС × 1C × ordens MT102 (КНП/КБК).
- `nl/` (nl_full, nl_v11, audit_report e specs por cliente).

**NL**
- `Netherlands/_tool/` com `validate.py` (1.664 linhas, skill nl-payroll-validator), `nl_check.py`, `nl_stage2.py`, `g2n.py`, `payslips.py`, `clients.py`, `curated.py`.
- Tabelas 2026 lidas por posição: `Netherlands/_references/2026/*.rows.json`.

**UK** (`United Kingdom/…/_scripts/`)
- `xsd_validate.py` e `sch_validate.py`: Schematron RIM 2027 v1.0; FPS PASS com 837 regras disparadas.
- **`sch_negative_test.py`**: muta o XML em memória para provar que o Schematron dispara.
- `irmark.py`: recálculo do IRmark, que bateu nos 2 arquivos.
- `uk_rules.py`: tabelas B-D, NIC.

**UA** (`Ukraine/…/_scripts/`)
- `parse_1c.py`, `parse_reports.py`, `parse_payroll.py`, `checks_08/09.py`, `unpack_try*.py` (o XML "PACKED_XML" não foi desempacotado).

**Kit de agentes** (`Internal_Certification_Kit_1_Core.zip`, `.claude/agents/`)
- intake → references ‖ parsers → validator → reviewer → report.
- O **reviewer** re-deriva tudo "without importing the validator's code", com no máximo um retrabalho e veredito CONFIRMED/REJECTED.
- O **references** define que cada item termina como valor, NOT LOCATED, OUT OF SCOPE ou N/A; nunca vem da memória nem de site secundário; nunca de outro ano.
- `run_certification.ps1` grava `.done/<stage>` e pula etapas concluídas.

**Catálogo de controles do `nl-payroll-validator`** (`skill-references/control-register.md`)
- Áreas: A escopo e integridade; B consistência interna; C bases; D tabelas; E prêmios; F AWf; G indicadores; H horas; I desligamentos; J contracheques; K pagamentos/GL; L gross-to-net (G-S1…G-S9, X-02, X-20); M master/config.
- ~100 controles, cada um S (script) ou R (revisor), citando poortcontrole ou L-code.
- Regras do registro: "every run produces every row"; "a value absent from a master extract is not by itself a defect".

**Tolerâncias explícitas** (UA A-09)
- Exatidão ao kopeck nas amarrações.
- ±0,01 por pagamento quando o PIT/ML é retido a cada pagamento.
- ±0,03 em relações agregadas construídas sobre arredondamento por pessoa.

**Provas externas usadas**
- SKAT Afstemning, campo a campo.
- Tilbakemelding e a-ordningen GODKJENT.
- Kvittens com FK487/FK497.
- Ordens de pagamento com КНП/КБК.

### 4.3 Como transformar em gate do pipeline

1. **Novo estágio "Certificação contra folha real" antes da promoção da skill e dos artefatos.** Rodar o validador derivado da skill em pelo menos um pacote real e recente do país, quando houver cliente ativo, ou num pacote sintético com valores oficiais. Todo achado com origem SKILL bloqueia a promoção. Os achados CFG viram issue para implementation, sem bloquear.
2. **O pipeline passa a emitir um 8º artefato: `control-register.md` + `validate.py` por país**, no modelo do nl-payroll-validator. Hoje o pipeline produz o que configurar, mas não como verificar.
   Cada linha do WTC e do Report Spec gera ao menos um controle (ID, teste, população, fonte, tolerância, S/R). Isso fecha o gap 1 (§3): os flags do WTC passam a ser asserções executáveis contra o G2N e o report.
3. **Diff WTC × configuração real.** Para cada elemento do G2N de um cliente certificado, comparar os flags (base de imposto, base de contribuição, campo do report, método de retenção) com a linha do WTC. Divergência é finding. O baseline do país é normativo; se dois clientes divergem, um deles está errado.
4. **Lint de residual antes de publicar:**
   - zero `[VERIFY]`, "verify exact amount", "approximately" ou `RESEARCH-GAP` em artefato publicado;
   - checagem de consistência interna dos valores (mesmo parâmetro, um único valor; o teto ЄСВ não pode ser 15× e 20×);
   - checagem de propagação: a correção de uma regra varre todas as ocorrências e os exemplos.
5. **Prova de que o validador dispara (teste negativo).** Mutar a entrada e confirmar que o controle falha, como o `sch_negative_test.py` do UK. Isso se aplica também ao QA do pipeline: um check que nunca reprova não prova nada.
6. **Regressão.** Cada achado SKILL de certificação vira caso de teste permanente da skill do país (pacote mínimo + resultado esperado). A v1.5 do nl-payroll-validator foi validada com "regressão idêntica nos 3 pacotes NL".
7. **Revisor independente que não importa o código do construtor**, como o agente reviewer do kit. Isso espelha o compliance-qa-auditor e deve exigir re-derivação numérica, não leitura.

---

## 5. Regras e melhorias de processo, por estágio

### 5.1 Escopo e mandato
- Fixar ano, período e frequência do caso de uso antes de tudo. O nl-payroll-validator nasceu 4-semanal/2025 e os clientes de 2026 eram mensais.
- **Gate de decisões de método** com um humano antes de testar: loon-in × loon-over, tratamento sem skattekort, regra por idade. As decisões ficam registradas em Assumptions (`PLANO` §4).
- Verificar se o diploma principal foi substituído no ano (KZ: novo Código Tributário em 01-01-2026). A substituição muda o mandato inteiro.
- Status temporais (lei marcial, regimes transitórios, versões de formulário) entram no mandato com "valid_to" e data de revisão.
- Travar a definição do entregável antes de produzir. A decisão NL mudou de "Audit Report só depois das correções (opção B)" para "validar e reportar com o que tem" no mesmo dia (`brain-service/log.md` 14-10).
- Cobrir os países sem base (UA, KZ, RU, AZ) e os que dependem de 1C (KZ, RU): a operação existe e a skill não.

### 5.2 Pesquisa de fontes
- Somente a fonte primária da autoridade, na versão em vigor no período. Registrar URL, versão, publicação, data de leitura e sha256 (`references/<país>/2026/sources.md`). Valor sem fonte vira NOT LOCATED e o check correspondente vira Not tested, nunca Pass.
- Não usar valor de site terceiro mesmo quando disponível. No DK, o personfradrag 54.100 de terceiro foi recusado, e o skat.dk carrega o valor via JS.
- Técnicas que funcionaram:
  - adilet.zan.kz pela API JSON, guardando `is_current` e `raw/*.content.json` (KZ);
  - retsinformation e lovdata consolidados, com a nota "sist endret";
  - zip oficial das trekktabeller (NO);
  - diff entre versões (eIndkomst v16.9 × v17.0 com tabelas idênticas).
- Bloqueios documentados:
  - zakon.rada.gov.ua, tax.gov.ua e president.gov.ua com 403 ou conexão recusada (UA);
  - kgd.gov.kz e gfss.kz com timeout (KZ);
  - www4.skatteverket.se com WAF;
  - skat.dk renderizado no cliente.

  Regra: quando a fonte primária está inacessível, corroborar com ≥2 secundárias, marcar como Assumption e não promover a fato (UA S-01…S-12).
- Comparar a cópia antiga com a nova por sha256. Na SE, a cópia da skill era byte-idêntica ao download de 14-10; na UK, DIG/RIM no Drive com sha256 idêntico ao oficial. Isso prova que a skill está atual sem reler tudo.
- Procurar alterações no meio do ano (skattevedtak NO 19-06-2026; ordens UA 243/284 de 17-07-2026; Lag 2026:100 de 01-04-2026 na SE).
- Tabelas em PDF: extração por posição de palavra e conferência da contagem de linhas/degraus. O pdftotext e o parser antigo perderam linhas. O kit v2 tornou o pdftotext obrigatório para contracheques e reprovou o pdfplumber naquele uso; para tabelas oficiais, o uso validado foi o pdfplumber por posição. **Testar o extrator por tipo de documento.**

### 5.3 Construção do artefato
- Para cada campo do report, a regra de população dos casos de borda: valor bruto antes de isenção, campo adicional obrigatório, média contra efetivo, categoria por natureza.
- Para cada valor monetário, a regra de arredondamento: direção, momento, nível (linha, pessoa ou total) e se a tabela é normativa sobre a fórmula.
- No WTC, por elemento: método de retenção (tabela/engångsbelopp/percentual), base de imposto, base de cada contribuição, campo(s) do report, inclusão em férias/ferietillæg, **rótulo local obrigatório** (contra "EOBI/EIS" no NL) e conta GL sugerida.
- No Payslip, invariantes testáveis:
  - roll-forward do YTD;
  - YTD de imposto ≥ período;
  - Σ linhas = totais;
  - campos iguais ao report (base tributável, SV-loon, indicadores, horas, Jaarloon BT, CPR/ID);
  - benefício in natura compensado visível.
- No SIR: o que é prova de aceite por país e como ligá-la ao report (nº do empregador, ID da mensagem, período, totais); redação de credenciais em cópias; formato oficial do arquivo (XML compactado da UA em "PACKED_XML", windows-1251, C_DOC_VER).
- Não publicar artefato só em `.gsheet`: exportar sempre `.xlsx`/`.docx` legível offline (WTC UA V4.2).
- No DD: regras de validação cruzada de master data (DOB × ID nacional, como o RNOKPP; formato de CPR e IBAN; part-time × salário mínimo; data de admissão única).

### 5.4 QA e auditoria
- Re-derivar numericamente, sem confiar no texto: tetos (172.940 = 20 × 8.647), gross-up (÷0,82 contra ÷0,77), exemplos recalculados.
- Sweep de propagação após qualquer correção: todas as ocorrências, inclusive exemplos e notas de desenvolvedor (CCG UA l.161 e l.326).
- Zero `[VERIFY]` no artefato publicado (46 na DK). Lacunas admitidas na QA (NL U1) viram pendência rastreada, não nota de rodapé.
- Teste negativo do validador e do lint, para provar que reprovam.
- Toda exceção automática é lida na fonte. Falso positivo vira "Pass (reviewed)" com o motivo. Na NL, ~40% das exceções eram falsos positivos, por mapeamento presumido ou regra aplicada fora do escopo.
- Nunca julgar um campo por outro que também está sob teste. Dois arquivos concordarem não prova nada; o contracheque é a âncora.
- Escala única de severidade: High (dinheiro retido ou declarado errado, ou sem prova de aceite), Medium (campo do report ou documento ao cliente sem mover dinheiro), Low (apresentação ou arredondamento ≤ 0,10), Observation (precisa de confirmação).
- Executive Summary sempre qualificado; inferência marcada como inferência.

### 5.5 Entrega e promoção
- Uma skill ou artefato só é promovido depois de certificado contra pelo menos um pacote real (ou sintético oficial) do ano vigente (§4.3).
- Nunca sobrescrever versão: nova versão = v1.1, mantendo a v1.0 intacta (workbooks NL v1.1, Audit Report Quest v1.1). O `tracker.py` e o `make_workbook` recusam sobrescrever.
- Instalação das skills verificável: manifesto com hash. A skill na lixeira deve gerar alerta, não ser descoberta no dia da validação.
- Pacote de saída padronizado e em inglês: workbook, `summary_EN.md` sem instrução de configuração, `resumo_PT.md`, `followups.md` em rascunho e `.done/validated`.
- Nada é enviado sem "Aprovado para envio" explícito.

### 5.6 Operação e infraestrutura (`PLANO` §4.1 e kit v2)
- Nunca colocar senha ou segredo em comando. Arquivo protegido é pulado e o humano é avisado (zip AES do AZ).
- Nunca alterar o registro do Windows ou configurações do sistema. O conflito de ponte Chrome × Claude Desktop foi resolvido com `.reg` gerado para o usuário executar (`_chrome_fix/`).
- Navegador: `list_connected_browsers` + teste com servidor em 127.0.0.1 para garantir que é o Chrome deste PC.
- Caminhos com mais de 260 caracteres: extrair em pasta curta (`_extracted`), usar o prefixo `\\?\` e checar com mais de 240.
- Scripts Python escritos com Write e executados como arquivo; nada de heredoc com aspas ou `\b`. Usar venv próprio e `python -I`.
- Dados pessoais não saem da máquina e não vão para portais de teste da autoridade. O RNOKPP fica só no workbook interno de evidências.
- Resposta cortada no meio exigiu "Resume" (transcrição 14-10 16:01). Gravar progresso em arquivo por etapa (`.done/<stage>`) para retomar.
- Dependências que precisaram de autorização externa (Gmail e Monday no claude.ai) bloquearam verificações; listá-las no início da rodada.

---

## 6. Recomendações concretas para o próximo pipeline

1. **Estágio 12, "Real-payroll certification gate"**, entre o QA e a promoção.
   - Entrada: um pacote HRBLIZZ real do país (report + recibo + G2N + contracheques + GL + banco + master) ou pacote sintético oficial.
   - Saída: workbook no formato da certificação.
   - Critério: zero achados de origem SKILL em aberto; achados CFG geram tickets.
2. **Gerar `validators/<cc>/control-register.md` + `validate.py` como artefato do pipeline.** Uma linha de controle por regra do CCG, flag do WTC, campo do Report Spec e invariante do Payslip, no formato do `nl-payroll-validator/references/control-register.md`, com "every run produces every row".
3. **Dar ao WTC um esquema de flags testável e um diff de configuração.**
   - Colunas obrigatórias: método de retenção, base de imposto, base por contribuição, campo(s) do report com regra de população, inclusão em férias, rótulo local e conta GL.
   - Script de diff WTC × G2N/config do cliente.
   - Itens prioritários a revisar já, pelos achados:
     - sindicato (NO);
     - seguro-saúde → 0013 + 0026 (DK);
     - severance → 0069 bruto (DK);
     - Store bededag e base do ferietillæg (DK);
     - payout de férias → engångsbelopp (SE);
     - AantVerlU média (NL);
     - colunas AOW e tabela normativa (NL).
4. **Lint de publicação obrigatório**, com teste negativo:
   - (a) zero `[VERIFY]`, "approximately", "verify exact" e `RESEARCH-GAP`;
   - (b) mesmo parâmetro com um único valor em todo o dossiê;
   - (c) propagação de correções (exemplos e notas incluídos);
   - (d) recálculo dos exemplos numéricos;
   - (e) datas de validade (status temporal com `valid_to` ≥ data de publicação).
5. **Calendário de revisão por mudança de ano e de meio de ano.** Para cada fonte, registrar `valid_from/valid_to` e um checagem periódica de nova versão (hash). Exemplos: formulários UA C_DOC_VER, eIndkomst v17.0, trekktabeller, Lag 2026:100, teto SS NL. Divergência de hash abre uma rodada de atualização.
6. **Cobertura das lacunas reais.** Corrigir o CCG UA (SK-09 a SK-13), criar a spec do J0500111 (SK-15), exportar o WTC UA V4.2 para `.xlsx` (SK-16) e construir a base KZ sobre o Código 214-VIII (reaproveitar `references/Kazakhstan/2026/facts.md`). Planejar RU e AZ (1C, Excel).
7. **Payslip com invariantes**, e testes que rodam no G2N + contracheque do pacote de certificação (lista em §5.3).
8. **SIR com "prova de aceite" por país e higiene de template**: identificadores de ligação, redação de credenciais, proibição de comentários de sample em arquivo live e formato de arquivo oficial.
9. **Pipeline de fontes com fallback documentado**: API oficial quando o site bloqueia (adilet); e, quando nada funciona, ≥2 secundárias marcadas como Assumption, nunca como fato.
10. **Distribuição de skills com manifesto e hash**, e verificação de presença antes de cada uso. As skills foram encontradas na `.trash`.
11. **Feedback em loop fechado.** Cada achado com origem SKILL na certificação e cada correção pós-entrega (histórico de versões do CCG UA: V1.2, V1.4, V1.5, V1.6; HRBS-12631, 14331, 14394) entra no failure log do pipeline como padrão novo (ex.: "regra corrigida num lugar e não nos exemplos", "status temporal sem data de validade", "flag de imposto deixado em VERIFY").
12. **Parsers HRBLIZZ como biblioteca compartilhada** (`validators/common/hrb.py` + mapeamento por cliente lido do arquivo). O pipeline pode publicar o "layout de saída esperado" (G2N, GL, payslip) por país para reduzir os falsos positivos (~40% na NL).

---

## 7. Pendências e itens abertos

**Achados.** Todos os 79 achados estão "Aberto" no tracker. Ações de configuração pendentes com implementation:
- A-01 sindicato NO;
- A-02 seguro-saúde DK em todos os clientes;
- A-03 0069 bruto;
- A-04 payout de férias SE (aguarda decisão D-02);
- A-05 Store bededag/ferietillæg (aguarda D-03);
- A-06 templates de contracheque NO/DK/SE/KZ;
- A-07 exigir das SBCs o arquivo exatamente como enviado + recibo.

**Cobranças em rascunho, não enviadas** (C-01…C-16):
- Umesh: GL "CORRECTED", carro, OTP, sindicato; Digipoort 002879487L01.
- Rakshitha: arquivo eIndkomst enviado; tipo de seguro-saúde; master KGS.
- Athul: Kvittens 559400-9267, master, banco, skattebeslut do Magnus; Digipoort e Whk NL; arquivo bancário da Quest.
- Malika: 200.00 + recibo, YTD ИПН, dedução básica, GL.
- Suresh: Digipoort, agosto original, WKR.
- Srikanth: resposta HMRC.
- Nataliia: recibo do 1-PV, Д1 de julho.
- Marju: FI/EE.
- Sadaf: contato RU.

**Decisões pendentes:**
- D-01: abrir o zip AZ.
- D-02: leitura da SFL 11:17.
- D-03: base do Store bededag.
- C-13: SBC da Irlanda.

**Not tested estruturais:**
- recibos (NL ×3, SE, UK, UA);
- skattekort/skattebeslut (NO, DK, SE): testada só a consistência;
- YTD (KZ, NL agosto, UK agosto);
- XML UA empacotado ("PACKED_XML");
- arquivo `.gpg` UK;
- regra de arredondamento KZ (NOT LOCATED);
- personfradrag e AES DK (NOT LOCATED);
- release R1 2026 da a-melding e reemissão das trekktabeller após 19-06-2026 (NOT LOCATED, INFERÊNCIA de que as de 2026 seguem valendo);
- posição 131 238881-17/111 da Skatteverket sobre arredondamento (bloqueada).

**Itens do pipeline revelados e sem dono:**
- correções do CCG UA (SK-09 a SK-13);
- spec J0500111 e C_DOC_VER 11 (SK-15);
- WTC UA em `.gsheet` (SK-16);
- 46 `[VERIFY]` da skill DK e lacunas de Store bededag e 0026 (SK-02 a SK-04);
- regra de AantVerlU na skill NL (SK-06);
- HRBS-14394 (teto SS NL 2026);
- reinstalação e versionamento das skills que estavam na `.trash` (SK-01);
- ausência de skill para UA, KZ, RU e AZ.

**Questões de dados e privacidade a tratar:**
- credencial do Government Gateway da McDermott em texto claro já arquivada em `01 Received` e em `_extracted` (UK-F01);
- dados de outro empregador recebidos nos pacotes NL-Sherwin e SE.

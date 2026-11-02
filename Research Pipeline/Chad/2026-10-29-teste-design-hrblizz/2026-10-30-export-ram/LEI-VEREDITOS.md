# Chade: vereditos pela lei (Dev × nosso v4)

> Entrada: [[COMPARACAO]] · Hub: [[Chade]] · Feito em 2026-10-30 (frente Chade). Só leitura da lei e do WTC; nada foi alterado no v4, no hub, no Drive ou em ticket.

**Regra usada:** só fonte primária lida nesta tarefa (texto da lei de finanças, que reproduz o artigo do CGI "ancien" e "nouveau"). Onde o artigo não pôde ser obtido, o item fica **SEM FONTE**, mesmo que Dev e v4 concordem.

**Siglas:** `LF26` = Loi n°008/AN/SENAT/2025 (LF 2026, vigente desde 2026-01-01). `LF25` = Loi n°033/PR/2024 (LF 2025). `LF24` = Loi n°031/PT/2023 (LF 2024). "p." = página do PDF (= número impresso no rodapé). Trechos com a ortografia original.

---

## 1) Tabela de vereditos (34 temas estatutários)

| # | Item | Dev | Nosso v4 | Veredito | Fonte exata (artigo, página, trecho) | Confiança |
|---|---|---|---|---|---|---|
| 1 | Tabela do IRPP | 0/10,5/15/20/25/30; 800 mil · 6M · 7,5M · 9M · 12M | igual | **AMBOS CERTOS** (fecha R1/A1 do v4) | CGI art. 1-IV, na redação do LF26 art. 3, p. 3–4: tabela « 0 et 800 000 0% … Plus de 12 000 000 30% » (vigente desde 2026-01-01) | 100% |
| 2 | Arredondamento do IRPP FLOOR(x+0,5) | sim | sim | SEM FONTE | regra de cálculo; nenhum artigo lido trata de arredondamento | — |
| 3 | CNPS do empregado deduzida da base do IRPP | sim | sim | SEM FONTE | CGI art. 47 (e art. 9-11, citado pelo art. 1-IV) não obtidos | — |
| 4 | Abono familiar | isento até 5.000 × dependentes/mês | isento por inteiro | **DEV CERTO** (com ajuste: é **por filho**, e o abono pago pela CNPS entra dentro dos 5.000) | CGI art. 45-4°, texto reproduzido no LF26 art. 8, p. 15 (mantido: « Le reste sans changement », p. 16): « ne peut excéder mensuellement par enfant la somme de 5.000 Francs sur laquelle viennent… s'imputer les allocations versées par la CNPS » | 95% |
| 5 | Transporte isento até 30% | sim | sim | **AMBOS CERTOS** | CGI art. 45-13°, LF26 art. 8, p. 16: « dans la limite de 30% calculées sur le salaire de base mensuel de chaque employé » | 100% |
| 6 | Transporte só se concedido a todos | não tem | 58207 = 1 | **NOSSO CERTO** | CGI art. 45-13°, LF26 p. 16: « lorsqu'elles profitent à tout le personnel de l'entreprise » | 100% |
| 7 | Indenização: plano social × individual | 6218% isento de IRPP sempre | isento só no plano social; individual tributável no IRPP | **NOSSO CERTO** (IRPP). A parte CNPS/TFE fica SEM FONTE | CGI art. 45-10°, LF26 p. 16: « indemnités de licenciement ou de départ volontaire versées dans le cadre d'un plan social ». WTC v1.1 (62180–62182, 62880): linha = indenização ordinária, tributável | 95% |
| 8 | Teto da aposentadoria complementar (3,5%) | sem teto | 3,5% do salário-base | SEM FONTE | CGI art. 47 não obtido. (O art. 26-III-2° do LF26 p. 8, teto de 15% para expatriado, é do IS, não do IRPP) | — |
| 9 | Não residente: taxa | 18% | 18% | **AMBOS CERTOS** | CGI art. 116 (LF25 art. 25, p. 42): « Cette retenue, dont le taux est fixé à 18% »; antes 25% (LF24 art. 28, p. 34–35) | 100% |
| 10 | Não residente: base | bruto, sem art. 45 | 58105 menos isenções do art. 45 | **AMBÍGUO** (ver seção 3) | CGI art. 116 (LF25 p. 42) fixa taxa e retenção, sem definir base; o art. 45 diz « Sont affranchis de l'Impôt » sem limitar a residentes; o LF25 tirou a frase « se substitue au tarif fixé par l'article 115 » | 60% |
| 11 | Não residente: TFE/TAFP | calcula | não calcula | SEM FONTE | artigos da taxe forfaitaire e da taxe d'apprentissage (base, sujeito passivo) não obtidos | — |
| 12 | Não residente: CNPS | todos os ramos | por ramo (flags) | SEM FONTE | lei/decretos da CNPS não obtidos | — |
| 13 | Deficiente, jovem graduado, diplomata | isentos; jovem 60 meses | igual | **AMBOS CERTOS** (com artigo) | Diplomata: CGI art. 3-2° (LF26 art. 5, p. 6). Jovem graduado: art. 3-4° (LF25 art. 23, p. 41): « jeunes diplômés âgés de moins de 35 ans … pendant une période de cinq ans ». Deficiente: saiu do art. 3-3° e foi para o **art. 45-18°** (LF26 art. 5 e 8, p. 6 e 16). Ver nota N2 | 95% |
| 14 | CNPS: taxas (3,5 / 5 / 7,5 / 4) | sim | sim | SEM FONTE | Lei 7/66 e decretos de 2009 não obtidos | — |
| 15 | CNPS: piso e teto | 60.000 / 500.000 | igual | SEM FONTE | idem | — |
| 16 | CNPS sobre o piso em mês sem salário | sem condição | só se 58130 > 0 | SEM FONTE | idem | — |
| 17 | Abono familiar fora da CNPS | sim | sim | SEM FONTE | idem | — |
| 18 | Meal cash 6566% na CNPS | fora | dentro | SEM FONTE | idem. (WTC v1.1, 65660–65662 "Meal cash benefit": PFM/AT/PVID = Yes, apoia o v4, mas WTC não é lei) | — |
| 19 | Meal cash 6286% no IRPP/TFE/TAFP | tributável | só 62867 | **AMBÍGUO** (código) | Lei: o art. 45 (1° a 18°, LF26 p. 15–16) não isenta auxílio-refeição em dinheiro → tributável no IRPP. Mas no WTC v1.1 (único xlsx) a série 6286x **não existe** (62800–62859 = Expense reimbursement; 6287x = Special allowance) | 70% |
| 20 | Benefício em espécie: forfait × MIN(real; %) | forfait | MIN | SEM FONTE | CGI art. 46 (LF 2019 art. 7) não obtido | — |
| 21 | Benefício em espécie: percentuais | sim | sim | SEM FONTE | idem | — |
| 22 | Benefício em espécie: base do % (58105 com ou sem espécie) | com | sem | SEM FONTE | idem | — |
| 23 | Espécie na CNPS e na TFE (valor real) | sim | sim | SEM FONTE | idem + CNPS | — |
| 24 | Bolsa escolar (6274%, 6580%) | fora de tudo | tributável | **AMBÍGUO** | CGI art. 45-9°, LF26 p. 16: « Les bourses d'enseignement ou de perfectionnement ». WTC v1.1: 62740/62750 = "Education & Schooling allowance" (abono em dinheiro, não bolsa); 65800–65809 = "Benefit earning" genérico | 65% |
| 25 | Seguro-saúde (6563%) no IRPP | fora | tributável | **NOSSO CERTO** (IRPP) | o art. 45 (1° a 18°) não traz isenção de seguro-saúde (LF26 p. 15–16); regra geral do art. 1-II-1° (LF26 p. 3): « Traitements, salaires, indemnités, émoluments » são renda. CNPS/TFE: SEM FONTE | 75% |
| 26 | Diárias, passagem, mudança 2 | fora | fora | **AMBÍGUO** | CGI art. 45-15° (LF26 p. 16): passagem de férias isenta « dans la limite de la valeur d'un billet par an et par personne »; art. 45-2° (p. 15): verbas de despesa da função isentas até 15% | 70% |
| 27 | TFE 7,5% | sim | sim | SEM FONTE | artigo da taxe forfaitaire não obtido | — |
| 28 | TFE/TAFP: base | tira isenções | base ampla | SEM FONTE | idem | — |
| 29 | TAFP 1,2% e arredondamentos | sim | sim | SEM FONTE | idem | — |
| 30 | Redução da TFE/TAFP (0/100/50%) | só isenção total da TFE | 0/100/50 na TFE e na TAFP | **NOSSO CERTO** | CGI art. 158 (LF24 art. 7, p. 4): « 50% de la taxe forfaitaire (TF) ; 50% de la taxe d'apprentissage (TA) » por 10 anos. Isenção total de TF **e** TA: LF 2020 art. 14, na redação do LF24 art. 6 (p. 3) e do LF26 art. 6 (p. 7) | 95% |
| 31 | Limite de reporte 58106 e taxa 58131 | sim | sim | SEM FONTE | parâmetro de relatório, não de lei lida | — |
| 32 | Multas por atraso + crédito da TAFP por formação | tem | não tem | **NOSSO CERTO** (só o crédito). Multas: SEM FONTE | LF26 art. 47 (p. 67–68): o CIFP substitui as isenções da TA (arts. 180–186 revogados, LF26 arts. 22–28, p. 32–34) e é « imputable sur l'impôt sur les sociétés »: não abate a TAFP da folha | 85% |
| 33 | Despesas profissionais 30% / verba de despesa 15% | não tem | não tem | **AMBOS ERRADOS** (falta a isenção de 15% do art. 45-2°). Os 30% ficam SEM FONTE | CGI art. 45-2°, LF26 p. 15: « n'excède pas un pourcentage de 15 % calculé sur la masse globale des salaires et desdites allocations » | 85% (15%) |
| 34 | Prelevamento para a Segurança Alimentar (PSA) | não tem | não tem | **AMBOS ERRADOS**. Correto: 400 FCFA/mês por empregado, desconto do empregado | CGI arts. 837–839 (LF24 arts. 18 e 21–23, p. 20–22): « fixé à 400 FCFA/mois et par employé »; sem alteração no LF25 e no LF26 (busca no texto) | 95% |

### Notas
- **N1 (item 4):** a fórmula do WTC v1.1 (linha 62760) já é a da lei: `isento = MIN(valor; 5.000 × filhos − abono CNPS)`. O Dev usa "dependentes" (`$hr.number_of_dependents`) e não desconta o abono da CNPS: ajustar para filhos e para a imputação.
- **N2 (item 13):** o art. 3-4° também isenta « ouvriers recrutés par les entreprises du régime du réel » por 5 anos (LF25 p. 41); nenhum dos dois designs tem essa categoria. Desde 2026 a deficiência é a do Código do Trabalho e da OIT (art. 45-18°).
- **N3 (WTC):** a maior versão no Drive `02-wtc` é `CHAD - WTC_V3.0.gsheet`, que não tem xlsx. Li o `TD-WTC-001-v1.1.xlsx` (md5 `26263474acab0277d9d3d334b781abfd`). Os códigos 62867/6286x que o v4 e o Dev usam não estão no v1.1. Para fechar os itens 19 e 24, falta a exportação xlsx da V3.0.

---

## 2) Contagem

| Veredito | Itens | Qtde |
|---|---|---|
| AMBOS CERTOS | 1, 5, 9, 13 | 4 |
| NOSSO CERTO | 6, 7, 25, 30, 32 | 5 |
| DEV CERTO | 4 | 1 |
| AMBOS ERRADOS | 33, 34 | 2 |
| AMBÍGUO | 10, 19, 24, 26 | 4 |
| SEM FONTE (artigo não obtido) | 2, 3, 8, 11, 12, 14–18, 20–23, 27–29, 31 | 18 |

**Nota do nosso design:** **9 de 34** temas confirmados certos pela lei (4 + 5). 3 confirmados errados (4, 33, 34), 4 ambíguos e 18 sem fonte. Entre os 12 temas já resolvidos pela lei, acertamos 9 (75%). O Dev acerta 5 dos 12 (1, 4, 5, 9, 13).

---

## 3) Ambíguos (prontos para decisão do cliente/BAU)

| # | Ponto | Nossa posição recomendada | Alternativa | Fonte | Confiança |
|---|---|---|---|---|---|
| 10 | Base do não residente (18%) | Aplicar as isenções do art. 45: o artigo vale para « l'Impôt » sem distinguir residência, e o art. 116 só muda a forma de cobrança (retenção) e a taxa | Bruto sem isenções (Dev e skill, esclarecimento 2): a retenção substitui a tabela e não haveria isenções | CGI art. 45 (LF26 p. 15–16); art. 116 (LF25 p. 42) | 60% |
| 19 | Meal cash 6286x | Tributável no IRPP (o art. 45 não isenta refeição em dinheiro), **se** o código for de fato auxílio-refeição; se for reembolso de despesa com comprovante, fica fora (art. 45-2°, até 15%) | Seguir o v4 (só 62867) | CGI art. 45 (LF26 p. 15–16); WTC V3.0 (falta o xlsx) | 70% |
| 24 | "Bolsa escolar" 6274x/6580x | Tributável (v4): o WTC chama de "Education & Schooling allowance", que é abono em dinheiro e não « bourse d'enseignement » | Isenta (Dev e skill): só se o código pagar uma bolsa de estudo ou de aperfeiçoamento ao próprio empregado | CGI art. 45-9° (LF26 p. 16) | 65% |
| 26 | Passagem e diárias | Passagem de férias isenta até 1 bilhete por ano e por pessoa, na tarifa normal até o local de origem; diárias e despesas da função isentas dentro do limite de 15% do art. 45-2° | Fora de tudo, sem limite (Dev e v4 hoje) | CGI art. 45-15° e 45-2° (LF26 p. 15–16) | 70% |

---

## 4) Fontes baixadas

Pasta `raw/docs/oficiais/TD/`. Data de download: 2026-10-30.

| Arquivo | URL de origem | md5 | Observação |
|---|---|---|---|
| `2026-10-30-LF-2026-Loi-008-AN-SENAT-2025.pdf` | https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf (Ministério das Finanças, oficial) | `d7f772cb26e1c7b143d8980ce64051f1` | 87 p., digitalizado; OCR (Windows OCR) em `…ocr.txt` (md5 `f905a001…`). Páginas citadas conferidas na imagem |
| `2026-10-30-LF-2025-Loi-033-2024.pdf` | https://ecofinances.gouv.td/wp-content/uploads/2026/04/LF-2025-_-Loi-033-du-06-dc-2024-1.pdf (oficial) | `dc3935a6453181c14b1a10df7f17cf11` | 63 p., digitalizado; OCR em `…ocr.txt` (md5 `9936cdf7…`) |
| `2026-10-30-LF-2024-Loi-031-PT-2023-cabri.pdf` | https://www.cabri-sbo.org/uploads/bia/Chad_2024_Approval_External_EnactedBudget_MinistryOfFinanceAndBudget_ECCASCEN-SAD_French_833643.pdf (espelho CABRI, documento do Ministério) | `8cda3c83446d3fc4c79897f727426f6b` | 79 p., com texto; extração em `…cabri.txt` (md5 `91e073a7…`) |

**Não obtidos** (tentativas e motivo):
- **CGI consolidado (2025/2026):** dgi.td (verificação Cloudflare com CAPTCHA, não resolvida), impots.td / finances.gouv.td (DNS ou 404), africa-laws.org (CGI 2016: host de arquivos fora do ar), droit-afrique.com (403 em todo o site). As edições 2024–2026 só aparecem à venda (Droit-Afrique). Sem o CGI faltam os arts. 44, 46, 47, 2-VI, 115 e os da TF e da TA.
- **LF 2019 a 2023 (texto fiscal):** LF 2019 só no droit-afrique (403); no CABRI, 2022 e 2023 são só o livro do orçamento, sem a parte fiscal (baixados, conferidos e descartados).
- **Código do Trabalho (Lei 038/PR/1996):** ILO NATLEX com verificação Cloudflare.
- **CNPS (Lei 7/66, decretos 1634–1636/2009):** nenhum host oficial ou institucional acessível (o SSA dos EUA deu 403).

---

## 5) Fora do pedido (não alterei nada; para o hub e para `correcoes.md`, com o seu ok)
- `correcoes.md` (2026-07-07, Chade) e a decisão do hub de 2026-07-07 dizem que o "Art. 45-4° não tem teto" e que o 5.000 "é o valor CNPS de CI". **O texto do art. 45-4° tem o teto de 5.000 por filho e por mês** (LF26 p. 15). A correção de julho está errada e o teto deve voltar.
- Lacuna R1 do v4 (tabela do IRPP não confirmada): fechada pelo LF26 art. 3.
- O v4 cita o "art. 3" para a deficiência: desde 2026 a base é o art. 45-18°.

---

## Bloco de prova
- **Pedido → resposta:** passo 1 → seção 4 (3 leis de finanças oficiais baixadas, com md5; o que faltou está listado com o motivo). Passo 2 → tabela da seção 1, com os 34 temas e veredito para cada um. Passo 3 (WTC) → itens 7, 18, 19 e 24 e nota N3: os códigos foram lidos no WTC v1.1 xlsx, e a V3.0 não tem xlsx. Passo 5 → seção 3.
- **Fontes:** cada veredito diferente de SEM FONTE cita o artigo, a lei que o altera e a página. Trechos curtos copiados da imagem das páginas (LF26 p. 3, 4, 6, 15, 16, 32–34, 67–68; LF25 p. 41–42; LF24 p. 3, 4, 20–22, 34–35).
- **Teste:** busca no texto inteiro do LF25 e do LF26 para confirmar que os arts. 837–839 (PSA) e 45 não mudaram de novo; md5 dos arquivos.
- **Confiança:** 95–100% nos itens 1, 4, 5, 6, 7, 9, 13, 30 e 34; 75–85% nos itens 25, 32 e 33. **Não está pronto como relatório final:** 18 temas dependem de artigos que não consegui baixar (CGI arts. 44/46/47, TF/TA, CNPS). Para fechar, falta o CGI 2025/2026 (dgi.td pelo navegador, com você passando a verificação) e a exportação xlsx do WTC V3.0.

## Quem mexeu
| Data | Frente | O quê |
|---|---|---|
| 2026-10-30 | chade | vereditos pela lei (LF 2024–2026); WTC v1.1 |
| 2026-11-01 | chade | revisão com o CGI 2026 (dgi.td) e a WTC V3.0; seção "O que aprender do design do Dev" |

---

# Revisão 2026-11-01 (CGI 2026 oficial + WTC V3.0)

> Esta revisão **substitui** os vereditos acima onde houver diferença. As seções anteriores ficam como histórico.

**Fontes novas**
- `raw/docs/oficiais/TD/2026-11-01-CGI-TCHAD-2026-FINAL-dgi.pdf` (dgi.td, 452 p., md5 `139d53269c4ae6d100dcda8298d55b20`). Texto extraído com PyMuPDF para `…-dgi.txt` (md5 `7f219acfa9003adbfd8df8ea74fc273a`). "p." abaixo = página do PDF; a página impressa é p. − 1.
- `CHAD-WTC_V3.0-export-2026-11-01.xlsx` (nesta pasta, md5 `04e06a491c7157e4cfe7e051df0dec9e`), 618 linhas. Colunas: Tax / CNPS / Apprenticeship / Lump-Sum (TF) / Non-Resident.

**O que a WTC V3.0 diz dos códigos em disputa**
| Código | Nome na V3.0 | Tax · CNPS · TA · TF |
|---|---|---|
| 62860–62865 | Meal/food allowance | Yes · Yes · Yes · Yes |
| 62866 / 62867 | Birth allowance / **Death allowance** | Yes · Yes · Yes · Yes |
| 62868–62869 | Gift allowance/voucher | Yes · Yes · Yes · Yes |
| 62740–62742 | Education & Schooling allowance 4 | No · No · No · No |
| 65800–65809 | **School Scholarship** | No · No · No · No |
| 62180–62182 | Severance & Seniority | No · No · No · No |
| 65630 | Health Insurance Benefit | No · No · No · No |
| 65660–65662 | Meal cash benefit | Yes · No · Yes · Yes |
| 62750–62752 / 62760–62762 | Family Allowance / Family allowance (MLA, Children) | Yes · No · Yes · Yes |
| 21640–21649 | **Voluntary** Contribution (pre-tax) | No · No · No · No |
| 62550 / 62560 / 62570 / 6557x / 6558x | Travel ticket / Relocation 2 / Per diem | No · No · No · No |

## R1) Tabela revisada (34 temas)

| # | Item | Dev | Nosso v4 | Veredito | Fonte exata (CGI 2026, artigo, página, trecho) | Confiança |
|---|---|---|---|---|---|---|
| 1 | Tabela do IRPP | igual | igual | **AMBOS CERTOS** | art. 1-IV, p. 14: « 0 et 800 000 0% … Plus de 12 000 000 30% » | 100% |
| 2 | Arredondamento do IRPP | FLOOR(x+0,5) | igual | SEM FONTE | art. 847, p. 168: retenção « à l'aide d'un barème fourni par l'Administration ». O arredondamento está no barème da DGI, que não temos | — |
| 3 | CNPS do empregado deduzida | sim | sim | **AMBOS CERTOS** | art. 47-I, p. 30: « ainsi que les retenues effectuées au titre de la sécurité sociale » | 100% |
| 4 | Abono familiar | 5.000 × dependentes | isento por inteiro | **DEV CERTO** (ajustar para **por filho** e imputar o abono da CNPS) | art. 45-4°, p. 29: « ne peut excéder mensuellement par enfant la somme de 5.000 Francs ». A WTC V3.0 marca 6275x/6276x como Tax Yes integral, o que também diverge da lei | 95% |
| 5 | Transporte 30% | sim | sim | **AMBOS CERTOS** | art. 45-13°, p. 30 | 100% |
| 6 | Transporte só se para todos | não | sim | **NOSSO CERTO** | art. 45-13°, p. 30: « lorsqu'elles profitent à tout le personnel » | 100% |
| 7 | Indenização plano social × individual | 6218% isento | só plano social isento | **NOSSO CERTO** (IRPP). Na TFE, os dois excluem e a lei inclui (ver N5) | art. 44-I, p. 29: « indemnités, y compris les indemnités de départ à la retraite ou pour service rendu » entram na renda; art. 45-10°, p. 30: isenção só « dans le cadre d'un plan social » | 95% |
| 8 | Aposentadoria complementar | sem teto | até 3,5% | **NOSSO CERTO** (falta a condição de obrigatória) | art. 47-I, p. 30: « dans la limite de 3.5 % des appointements »; 47-II: « doivent revêtir un caractère obligatoire ». A V3.0 chama 2164x de "Voluntary Contribution": se for voluntária, não é dedutível | 95% |
| 9 | Não residente: 18% | 18% | 18% | **AMBÍGUO** (mudou: era AMBOS CERTOS) | art. 116, p. 43: 18% para « personnes visées au VI de l'article 2 et à l'article 60 ». O art. 2-VI (p. 15) trata de direitos autorais/patentes e do art. 49; o art. 60 (p. 33), de artistas. Salário de não domiciliado: art. 44-II-2° (p. 29), tributável pela tabela (art. 847) | 65% |
| 10 | Não residente: base | bruto | com isenções do art. 45 | **AMBÍGUO** | art. 45 « Sont affranchis de l'Impôt », sem limitar a residentes (p. 29); art. 104-I (p. 42): não domiciliados são tributados sobre a renda obtida no Chade | 65% |
| 11 | Não residente: TFE/TAFP | calcula | não calcula | **DEV CERTO** | TF, art. 187 (p. 60): incide sobre salários pagos, a cargo de quem paga, sem condição de residência. TA, art. 173 (p. 59): « montant brut des appointements, salaires… payés par les entreprises » | 95% |
| 12 | Não residente: CNPS | todos os ramos | por ramo | SEM FONTE | falta a lei da CNPS (Código de Previdência Social / Lei 7/66 e decretos de 2009) | — |
| 13 | Deficiente, jovem graduado, diplomata | IRPP certo; TFE/TAFP calculados para 2 e 3 | igual | **AMBOS ERRADOS** (parcial) | IRPP certo: art. 3-2° e 3-4° (p. 15) e 45-18° (p. 30). Falta nos dois a isenção de TF e TA sobre a parte da folha paga a « jeunes diplômés âgés de moins de 35 ans, les personnes handicapées et les ouvriers âgés de moins de 35 ans » (art. 188-10°, p. 61; art. 174-3°, p. 59), sem limite de 5 anos. Falta também a categoria « ouvriers » | 90% |
| 14 | CNPS: taxas | 3,5 / 7,5 / 4 / 5 | igual | SEM FONTE | lei/decretos da CNPS | — |
| 15 | CNPS: piso e teto | 60 mil / 500 mil | igual | SEM FONTE | idem | — |
| 16 | CNPS sobre o piso com salário zero | sem condição | só se 58130 > 0 | SEM FONTE | idem | — |
| 17 | Abono familiar fora da CNPS | sim | sim | SEM FONTE | idem (a WTC V3.0 também marca CNPS No) | — |
| 18 | Meal cash 6566% na CNPS | fora | dentro | SEM FONTE | idem. A WTC V3.0 marca 65660 com CNPS **No** (igual ao Dev; a v1.1 dizia Yes) | — |
| 19 | 6286x no IRPP/TFE/TAFP | tributável (série inteira) | só 62867 | **DEV CERTO** | V3.0: 62860–65 são auxílio-refeição e 62868–69, presente. O art. 45 (p. 29–30) não isenta nenhum dos dois, e o art. 44-I inclui « gratifications ». O v4 tributa justamente o 62867 (Death allowance), que pode ser capital de óbito isento (art. 45-11°, p. 30): ver N6 | 85% |
| 20 | Espécie: forfait × MIN(real; %) | forfait | MIN | **NOSSO CERTO** | art. 46-III, p. 30: « Ceux-ci sont plafonnés »; 46-V: a indenização representativa entra « dans la limite des taux » | 85% |
| 21 | Espécie: percentuais | 20/10/15 (75 mil)/5/4/4/4/3/2 | iguais | **AMBOS CERTOS** | art. 46-III, p. 30: logement 20, électricité 4, eau 4, véhicule 10, gaz 2, téléphone 3, équipement 5, domesticité 4, nourriture 15 « avec un maximum de 75.000 F CFA par mois » | 100% |
| 22 | Espécie: base do % | 58105 com espécie | só dinheiro | **NOSSO CERTO** | art. 46-I e II, p. 30: base = « traitements, indemnités, allocations… ainsi que de tous les avantages en argent »; « Le total des éléments cités au I servira de base ». Obs.: o texto 2026 **não** tem mais « net des cotisations sociales » | 90% |
| 23 | Espécie na TFE/TAFP pelo valor real | sim | sim | **AMBOS CERTOS** (TF/TA). Na CNPS, sem fonte | art. 189-2°, p. 61: « avantages en nature… pour leur montant réel »; art. 173, p. 59: base inclui « avantages en nature » | 95% |
| 24 | Bolsa escolar (6274x, 6580x) | fora de tudo | tributável e na base | **PARCIAL** | IRPP: 6580x = "School Scholarship" (V3.0), isenta pelo art. 45-9° (p. 30, « bourses d'enseignement ») → Dev certo. TFE/TAFP: base bruta, sem as isenções do art. 45 (art. 189-1°, « allocations »; art. 173) → nosso certo. 6274x ("Education & Schooling allowance") é abono e não bolsa → tributável (v4) | 80% |
| 25 | Seguro-saúde 6563% | fora de tudo | tributável | **NOSSO CERTO** | não há isenção no art. 45 (p. 29–30); o art. 9-I (p. 16) inclui « la valeur des profits et avantages en nature »; na TF, art. 189-2° | 80% |
| 26 | Diárias, passagem, mudança 2 | fora | fora | **AMBÍGUO** | art. 45-15° (p. 30): passagem de férias até « un billet par an et par personne »; art. 45-2° (p. 29): verbas de despesa até 15%. Reembolso de despesa real não é renda (art. 9-I, p. 16) | 70% |
| 27 | TFE 7,5% | sim | sim | **AMBOS CERTOS** | art. 190, p. 61: « fixé à 7,5 % du montant brut des sommes imposables » | 100% |
| 28 | Base da TFE/TAFP | tira transporte isento, 6276%, 62229 | base ampla | **NOSSO CERTO** | art. 189-1°, p. 61: « montant brut des traitements… indemnités diverses, allocations, gratifications »; art. 173, p. 59: « montant brut des appointements… rétributions quelconques ». As isenções do art. 45 valem só para « l'Impôt » (IRPP). As únicas isenções de TF/TA são as dos arts. 188 e 174 | 90% |
| 29 | TAFP 1,2% e arredondamentos | sim | sim | **AMBOS CERTOS** | art. 178, p. 60: « 12 pour mille »; art. 177: fração de até 1.000 desprezada, « arrondi à la dizaine de Francs la plus voisine » | 100% |
| 30 | Redução 0/100/50 TFE e TAFP | só isenção total da TFE | 0/100/50 nas duas | **NOSSO CERTO** | art. 158, p. 56: « 50% de la taxe forfaitaire (TF) ; 50% de la taxe d'apprentissage (TA) »; isenção total pelo LF 2020 art. 14 (LF26 art. 6) | 95% |
| 31 | Limite 58106 e taxa 58131 | sim | sim | NÃO É TEMA DE LEI | parâmetro de relatório | — |
| 32 | Multas + crédito da TAFP | tem | não tem | **NOSSO CERTO** (crédito) | o crédito de formação (CIFP, LF26 art. 47) abate o IS; os arts. 180–185 estão revogados (p. 60). As multas existem (art. 1051: majoração de 100% por infração aos arts. 116/857; art. 1052: 10% por atraso, p. 208), mas são cobrança do Fisco ao empregador, não cálculo de folha | 85% |
| 33 | 30% / 15% de despesas | não tem | não tem | **AMBOS ERRADOS** (falta a isenção de 15%). Os 30% **não existem** para salários | art. 45-2°, p. 29 (15% « sur la masse globale des salaires et desdites allocations »). Para salários, o art. 47 (p. 30) só deduz aposentadoria obrigatória e previdência social. Os 30% do hub (`hub:74`) não têm base | 90% |
| 34 | PSA 400 FCFA/mês | não tem | não tem | **AMBOS ERRADOS** | arts. 837–839, p. 166: « fixé à 400 FCFA/mois et par employé »; devido pelos empregados do setor formal privado | 100% |

### Notas da revisão
- **N4 (9/10):** pela letra do CGI 2026, o 18% do art. 116 não alcança o salário do não residente; esse salário seria tributado pela tabela (arts. 44-II-2° e 847). Dev, v4 e skill usam 18%. Fica AMBÍGUO porque a prática da DGI pode ser outra; precisa de consulta formal à DGI (já é pendência do hub).
- **N5 (7, TFE):** a base da TF inclui « indemnités diverses » (art. 189-1°), sem excluir a indenização de demissão. Os dois designs e a decisão do hub de 07/07 ("severance fora da TFE") deixam fora. Pela letra, entra (70%).
- **N6 (19):** 62866 (auxílio-nascimento) é « allocation d'assistance à famille » e cai no teto do art. 45-4°. 62867 (auxílio-óbito) pode ser o « capital décès » isento do art. 45-11°. O resto da série 6286x é tributável.
- **N7 (WTC V3.0 × lei, fora do escopo do design):** a V3.0 marca como Tax No a indenização 6218x (art. 44-I diz tributável) e o seguro-saúde 65630 (não há isenção); marca como Tax Yes integral o abono familiar 6275x/6276x (o art. 45-4° isenta até 5.000 por filho).

## R2) Contagem revisada

| Veredito | Itens | Qtde |
|---|---|---|
| AMBOS CERTOS | 1, 3, 5, 21, 23, 27, 29 | 7 |
| NOSSO CERTO | 6, 7, 8, 20, 22, 25, 28, 30, 32 | 9 |
| DEV CERTO | 4, 11, 19 | 3 |
| AMBOS ERRADOS | 13, 33, 34 | 3 |
| PARCIAL (cada lado certo numa parte) | 24 | 1 |
| AMBÍGUO | 9, 10, 26 | 3 |
| SEM FONTE | 2 (barème da DGI), 12, 14–18 (lei da CNPS) | 7 |
| Não é tema de lei | 31 | 1 |

**Nota do nosso design:** a lei resolveu **23** temas. O nosso está certo em **16 de 23 (70%)**, mais metade do item 24. O Dev está certo em 10 de 23 (43%).

## R3) Ambíguos revisados (para decisão do cliente/BAU)
| # | Ponto | Posição recomendada | Alternativa | Fonte | Confiança |
|---|---|---|---|---|---|
| 9/10 | Não residente empregado | Tabela progressiva com as isenções do art. 45 (letra dos arts. 44-II-2°, 45, 116 e 2-VI) | 18% sobre o bruto (prática de Dev, v4 e skill); se mantido, aplicar ao menos o art. 45 (o v4 já faz) | CGI 2026, p. 15, 29, 43 | 65% |
| 26 | Passagem e diárias | Passagem de férias isenta até 1 bilhete por ano e por pessoa; diárias e mudança com comprovante fora (reembolso); verba fixa sem comprovante dentro do limite de 15% do art. 45-2° | Fora de tudo, sem limite | art. 45-2° e 45-15°, p. 29–30 | 70% |
| 24 (6274x) | Abono escolar | Tributável no IRPP e na base da TFE/TAFP | Isento, como bolsa (WTC V3.0) | art. 45-9°, p. 30 | 75% |

## R4) O que continua sem fonte, e qual norma falta
- **CNPS (itens 12, 14–18):** a lei de previdência social (Lei 7/66 e alterações) e os decretos de 2009 (taxas, piso, teto, base de contribuição, abono e refeição), que não estão no CGI. Falta o texto oficial (CNPS ou Journal Officiel).
- **Arredondamento do IRPP (item 2):** o barème oficial da retenção (art. 847) publicado pela DGI.
- **Code du Travail:** necessário só para a definição de deficiência (art. 45-18°) e do auxílio-refeição como condição de trabalho. Não muda nenhum veredito acima.

---

# O que aprender do design do Dev

Pontos em que o Dev está mais certo ou mais completo que o v4, e mudança recomendada para o v4. **Não aplicado**: depende do ok do usuário.

| # | O que o Dev faz melhor | Mudança recomendada no v4 | Fonte |
|---|---|---|---|
| 1 | Teto do abono familiar (5.000) | Isenção de 627%% = MIN(valor; 5.000 × filhos − abono CNPS); excesso tributável no IRPP. Trocar "isento por inteiro". Corrigir também `correcoes.md` (07/07) e a decisão do hub | art. 45-4°, p. 29 |
| 2 | Não residente paga TFE e TAFP | Tirar `NOT(EQUALS($58218;1))` das pré-condições da TFE (`v4:1290`) e da TAFP (`v4:1375`) | arts. 187 e 173, p. 59–60 |
| 3 | Série 6286x tributável | Tributar 62860–62865 e 62868–62869 no IRPP (58105) e na TFE/TAFP. 62866 entra no teto do art. 45-4°; 62867, decidir se é capital de óbito (isento) | art. 44-I, 45-4°, 45-11°; WTC V3.0 |
| 4 | Bolsa de estudo isenta de IRPP | 6580x fora da 58105 (IRPP), mas mantida na base da TFE/TAFP | art. 45-9°, p. 30; art. 189 |
| 5 | TFE sem arredondamento | Tirar FLOOR(x+0,5) da TFE (C11). Só a TAFP tem regra de arredondamento | art. 190 × art. 177, p. 60–61 |
| 6 | Multas modeladas (notionals 64550–64554) | Opcional: não é cálculo de folha. Se o cliente quiser controle, só a majoração de atraso (art. 1052, 10%). O crédito da TAFP do Dev **não** deve ser copiado | arts. 1051–1052, p. 208; LF26 art. 47 |
| 7 | Limite dentro da fórmula, com MIN() (C4) | Não é lei. Vale considerar se a conta-teto do v4 (A10) falhar no teste do motor | — |

Mudanças que valem **para os dois** (não estão em nenhum):
- PSA de 400 FCFA/mês por empregado: desconto do empregado, reportado como o IRPP (arts. 837–839, p. 166).
- Isenção de TF e TA sobre a parte da folha de jovens diplomados com menos de 35 anos, deficientes e operários com menos de 35 anos, em empresa do regime real (art. 188-10°, p. 61; art. 174-3°, p. 59).
- Isenção de 15% das verbas de despesa da função (art. 45-2°, p. 29).
- Dedução de aposentadoria complementar só se obrigatória (art. 47-II). Se 2164x é voluntária (WTC V3.0), não deduz.
- Indenização individual dentro da TFE (art. 189-1°, « indemnités diverses »), 70%.
- No v4, citar o art. 45-18° para deficiência e o art. 3-4° para jovem graduado, e acrescentar a categoria « ouvriers » (art. 3-4°).
- Não residente: decidir com a DGI entre 18% e a tabela progressiva (N4).

O que **não** copiar do Dev: base 58105 com espécie (art. 46-I/II), forfait sem comparar com o valor real (art. 46-III « plafonnés »), aposentadoria sem teto (art. 47-I), indenização ordinária isenta (art. 44-I), seguro-saúde isento, base da TFE/TAFP com as isenções do IRPP (arts. 189 e 173), falta da condição "para todo o pessoal" no transporte (art. 45-13°).

## Bloco de prova (revisão)
- **Pedido → resposta:** sem fonte, ambíguos e itens que dependem de código → tabela R1 (34 temas, veredito com artigo e página do CGI 2026). WTC V3.0 → quadro de códigos e itens 4, 7, 8, 18, 19, 24, 25, 26. Seção anterior preservada. "O que aprender do Dev" → seção final.
- **Fontes:** CGI 2026 da DGI, arts. 1, 2, 3, 9, 44, 45, 46, 47, 60, 104, 116, 158, 173–178, 187–190, 837–839, 847, 1051–1052, lidos no texto extraído (páginas indicadas). WTC V3.0 lida célula a célula nas colunas A, B e K–O.
- **Teste:** md5 do PDF conferido (`139d5326…`, igual ao informado); busca de "non-résident"/"non domicilié" no CGI inteiro para o N4; busca de "30 %" para confirmar que não há abatimento de 30% sobre salários.
- **Confiança:** 90–100% nos itens de taxa e base (1, 3, 5, 11, 21, 23, 27–30, 34); 80–90% em 7, 8, 13, 19, 20, 22, 24, 25, 33; 65–70% nos ambíguos. Os 7 itens sem fonte dependem de normas fora do CGI (CNPS, barème da DGI).

---

# Revisão 2026-11-01 (b): CNPS e decisões

> Acrescenta a R1–R4. Onde houver diferença, vale esta seção. Nada foi alterado no v4, no hub, no Drive ou em ticket.

**Fontes novas** (pasta `raw/docs/oficiais/TD/`, baixadas em 2026-11-01)
| Arquivo | Origem | Nível | md5 |
|---|---|---|---|
| `2026-11-01-CNPS-textes-reglementaires-wayback-20260922.html` | cnps-tchad.com, página "Textes réglementaires" (cópia do Wayback de 22/09/2026: o site da CNPS está com o certificado vencido) | A (lista oficial dos textos vigentes) | `9bd8e28b04836cd78e5cfb7cbfc314ba` |
| `2026-11-01-CNPS-Guide-de-l-employeur-2019.pdf` (+ `.txt`) | cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LEMPLOYEUR.pdf (Wayback, 17/07/2024), guia oficial da CNPS, ed. 2018/2019 | A− (institucional, cita os decretos) | `8253ae77032c64f97458fa0d707d1d32` |
| `2026-11-01-Decret-1635-PR-PM-MFPT-2009-prestations-familiales-droitafrique.pdf` | droit-afrique.com (Wayback, 03/07/2024), texto integral do decreto | B (reprodução de editora jurídica) | `30953807d2462378272a806590159f85` |
| `2026-11-01-Decret-1636-PR-PM-MFPT-2009-pensions-droitafrique.pdf` | droit-afrique.com (Wayback, 24/05/2022), texto integral | B | `4caf3326d734f949240443a7d997b974` |
| `2026-11-01-HUB-IIT-fiche-2-emploi-Tchad-2023.pdf` | hub-iit.org, ficha de jan/2023 (SMIG pelo Dec. 55/PR/11) | B | `b1b07e888ec3464397ab9e12a53863f7` |

"Guia p." = página do PDF do guia da CNPS.

## B1) Tabela de decisões

| # | Item | Decisão | Valor/regra com vigência | Fonte exata | Confiança |
|---|---|---|---|---|---|
| 14 | CNPS: taxas | **AMBOS CERTOS** | A partir de 2009-12-04: PFM 7,5% empregador (dos quais 0,25% repassados pela CNPS ao ONAPE, sem taxa a mais); AT/MP 4% empregador (taxa única, sem classe de risco); PVID 5% empregador + 3,5% empregado. Total 20% | Dec. 1635/2009 art. 1–2; Dec. 1636/2009 art. 1; Dec. 1634/2009 (4%; texto não obtido: lista oficial da CNPS, item 6, e guia p. 8) | 95% |
| 15 | CNPS: teto | **AMBOS CERTOS** | 500.000 FCFA/mês, o mesmo nas 3 caixas (6.000.000/ano), desde 2009-12-04 (antes, Dec. 1137/2007). O teto é **anual**: regularização no fim do ano sobre o total pago no ano (guia p. 12) | Dec. 1635 art. 4; Dec. 1636 art. 3; guia p. 9 e 12 | 95% |
| 15 | CNPS: piso | **AMBOS CERTOS** | Base mínima = SMIG 59.995 arredondado a 60.000 FCFA/mês, a partir de 2011 (Dec. 1111/PR/PM/MFPT/2011, de 18/10/2011) | guia p. 7 e 9 (exemplo: salário 40.000 → base 60.000); lista oficial, itens 10–11; HUB-IIT 2023 (Dec. 55/PR/11: 60.000) | 85% |
| 16 | Piso com salário zero | **NOSSO CERTO** (só se houver salário no mês) | A contribuição incide sobre o que foi pago no mês; o piso corrige a base de quem recebeu, e não cria base em mês sem pagamento | guia p. 7 (« salaires… versés aux salariés entre le premier et le dernier jour du mois ») e p. 9 | 75% |
| 17 | Abono familiar fora da CNPS | **AMBOS CERTOS** | Fora da base. O abono pago pela própria CNPS também fica fora (é benefício legal) | guia p. 8 (« Allocations familiales » na lista de exclusões); Dec. 1635 art. 3 (« à l'exclusion… des prestations légales de la sécurité sociale ») | 90% |
| 18 | Meal cash 6566% na CNPS | **DEV CERTO** (fora); a WTC V3.0 diz o mesmo | A « prime de panier » sai da base como reembolso de despesa. Já o auxílio-refeição geral 6286x entra (é « avantage en espèce »), como já marca a V3.0 | guia p. 7 (« Prime de panier »); Dec. 1635 art. 3 / 1636 art. 2 | 75% |
| 12 | Não residente: CNPS | **DEV CERTO** (todos os ramos) | Contribui em PFM, AT/MP e PVID como qualquer empregado, « quelle que soit… leur nationalité ». Exceção: empregado destacado coberto por convenção bilateral ou multilateral (CIPRES), que exige certificado de destacamento. Não está em nenhum dos designs | guia p. 6 (Art. 4 do Dec. 51/PR/MTJS/DTMOPS de 09/03/1970) | 80% |
| 23 | Espécie na CNPS | **AMBOS CERTOS** (entra) | Entra a « contre valeur des avantages en nature ». O arrêté de avaliação (Dec. 1635 art. 5) não foi obtido. Usar o valor real (mesmo critério da TF, art. 189-2°) | Dec. 1635 art. 3 e 5; Dec. 1636 art. 2 e 4 | 75% (o valor) |
| 7 (CNPS) | Indenização de demissão na CNPS | fora | Exclusão das « indemnités ayant un caractère de dédommagement » | Dec. 1635 art. 3; Dec. 1636 art. 2 | 75% |
| extra | Transporte na CNPS | **fora inteiro** (diverge do hub e de `correcoes.md` de 07/07: "excesso sujeito a CNPS") | A « Indemnité mensuelle de transport » e as « Indemnités de déplacement » saem da base da CNPS, sem limite. O limite de 30% vale só para o IRPP (art. 45-13°) | guia p. 8 | 75% |
| 9/10 | Não residente: IRPP | **DECIDIDO: tabela progressiva**, não 18%. Dev, v4 e skill errados | Salário de empregado não domiciliado (atividade no Chade e empregador estabelecido no Chade) é renda do art. 44 e sofre retenção pela tabela (art. 847, art. 1-IV), com as isenções do art. 45, os forfaits do art. 46 e as deduções do art. 47, como para o residente. O 18% do art. 116 vale só para: (a) o art. 2-VI, isto é, direitos autorais, licenças e marcas, e a renda BNC do art. 49 (que exclui as rendas dos arts. 1 a 48); (b) os artistas do art. 60. O art. 123 confirma que o 18% é para « activités (BNC) ». O art. 857 (18%) vale para pagamentos a « tiers n'ayant pas d'installation professionnelle », ou seja, prestadores, e não empregados. Vigência: desde 2025-01-01 (LF25 art. 25), igual em 2026 | CGI 2026, `…-dgi.txt`: art. 2-III/VI (l. 589–700, p. 14–15), art. 44-II-2° (l. 2502–2525, p. 29), art. 49-I (l. 2751–2770, p. 31), art. 60 (l. 3002, p. 33), art. 116 (l. 4334, p. 43), art. 847 (l. 19140, p. 168), art. 857 (l. 19274, p. 170). LF24 art. 31 (art. 123, `…cabri.txt` l. 1494–1501); LF25 art. 25 (`…ocr.txt` l. 2023–2037). md5 do CGI: `139d53269c4ae6d100dcda8298d55b20` | 85% |
| 26 | Passagem, diárias, mudança | **DECIDIDO** | IRPP: (1) passagem de férias isenta até 1 bilhete por ano e por pessoa (empregado, cônjuge e dependentes), na tarifa normal do local de trabalho ao local de origem, se a despesa for real; o excesso é tributável. (2) Diária ou verba fixa para despesa da função: isenta até 15% de (salário + essas verbas), se usada no seu objeto; o excesso é tributável. (3) Reembolso de despesa real com comprovante: não é renda (o art. 44-I só inclui reembolsos pagos a « dirigeants de société »). TF/TA: (1) e (2) entram na base (« indemnités diverses, allocations »); (3) fica fora. CNPS: (1), (2) e (3) fora (« indemnités de déplacement », reembolso de despesa). Vigência: CGI 2026 | art. 45-2° e 45-15° (p. 29–30), art. 44-I (p. 29), art. 189-1° (p. 61), art. 173 (p. 59); guia CNPS p. 7–8 | 75% |
| 24 | 6274x (abono escolar) e 6580x (bolsa) | **DECIDIDO** | 6274x "Education & Schooling allowance": tributável no IRPP, na TF, na TA e na CNPS (abono em dinheiro). 6580x "School Scholarship": isenta de IRPP (art. 45-9°, que não exige que o bolsista seja o empregado); dentro da TF/TA (base bruta, arts. 189-1° e 173) e da CNPS (« tout autre avantage en espèce », sem exclusão). A WTC V3.0 (No em tudo) diverge na TF/TA/CNPS | art. 45-9° (p. 30); arts. 173 e 189 (p. 59 e 61); Dec. 1635 art. 3 | 75% (6274x), 65% (6580x na CNPS) |
| 2 | Arredondamento do IRPP | **DECIDIDO: convenção técnica**, não regra de lei | O CGI 2026 não traz regra de arredondamento para o IRPP. Só há regras para outros tributos: TA (art. 177, dezena), IS (art. 143), foncier (arts. 771 e 787). O art. 847 manda reter « à l'aide d'un barème fourni par l'Administration », que não foi obtido (dgi.td responde 403). O XAF não tem subunidade, então manter o arredondamento da retenção mensal ao franco inteiro (FLOOR(x+0,5)), como Dev e v4, marcado como convenção até ter o barème | CGI 2026, busca de « arrondi », « millier », « dizaine », « centaine » no texto inteiro (l. 5275, 6454, 6778, 6879, 17506, 17771) | 70% |

## B2) Notas
- **N8 (CNPS, o que muda na prática):** as 3 caixas têm o mesmo teto (o Dec. 1636 art. 3 remete ao teto da PFM). Como o teto é anual, o design precisa da regularização de dezembro (já é pendência do hub: "regularização anual CNPS"). Multa de atraso da CNPS: 1‰ por dia, com vencimento no dia 20 do mês seguinte, ou do trimestre para quem tem menos de 20 empregados (guia p. 11). É cobrança, não folha.
- **N9 (9/10):** o empregado não domiciliado que fica mais de 183 dias em 12 meses passa a ser domiciliado (art. 2-I-2°), o que reforça a tabela. A consulta formal à DGI (pendência do hub) ainda vale, mas a letra da lei já basta para o design.
- **N10 (transporte):** o hub (linha "Transporte") e `correcoes.md` (2026-07-07) dizem que o excesso sobre 30% é "sujeito a CNPS". O guia oficial tira o transporte inteiro da base da CNPS. Fica para o hub e para `correcoes.md`, com o ok do usuário.

## B3) O que continua sem fonte
- **Texto da Lei 7/66** (Code du travail et de la prévoyance sociale) e do **Dec. 1634/2009** (AT/MP 4%): há só a lista oficial e o guia, sem o texto integral.
- **Arrêté de avaliação das vantagens em espécie na CNPS** (Dec. 1635 art. 5).
- **SMIG depois de 2011:** nenhum decreto oficial novo foi achado. A lista oficial da CNPS de 09/2026 ainda cita os Decs. 55/2011 e 1111/2011. Um site secundário (africarrieres) fala em 89.625 FCFA "desde 2015", sem citar decreto e contra o guia oficial de 2019: descartado.
- **Barème da DGI para a retenção (art. 847):** necessário para o arredondamento.
- **Notas circulares CNPS de 2025** (n° 023, 077 e 107): só o título aparece na página; o conteúdo não foi arquivado.
- **Tentativas sem sucesso:** cnps-tchad.com direto (certificado vencido; contornar o TLS foi negado e não foi tentado), ssa.gov SSPTW (403), dgi.td/documents (403), Wayback CDX (fora do ar em alguns momentos).

## Bloco de prova (b)
- **Pedido → resposta:** Tarefa A → B1, itens 12, 14–18 e 23, mais 7-CNPS e transporte, com as fontes salvas e o md5 de cada uma. Tarefa B → B1, itens 9/10, 24, 26 e 2.
- **Fontes:** decretos 1635/1636 lidos no texto integral (artigos citados); guia da CNPS lido nas p. 6–12; CGI 2026 lido nos arts. 2, 44, 45, 49, 60, 116, 173, 189, 847 e 857, com o número da linha do `.txt`; LF24 (art. 123) e LF25 (art. 116, ancien/nouveau).
- **Teste:** md5 de todos os arquivos novos; busca de « arrondi »/« millier »/« dizaine »/« centaine » no CGI inteiro; conta do exemplo do guia conferida (4.000.000 → 500.000 × 20% = 100.000, dos quais 17.500 do empregado = 3,5%).
- **Confiança:** taxas e teto 95%; piso 85%; não residente 85%; o resto entre 65% e 80%. O que falta está em B3.

| Data | Frente | O quê |
|---|---|---|
| 2026-11-01 | chade | revisão (b): CNPS (decretos de 2009, guia oficial) e decisão dos ambíguos 9/10, 24, 26 e do arredondamento |

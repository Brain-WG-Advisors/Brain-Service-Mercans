# Bélgica — auditoria de idioma dos artefatos (inglês × idioma local)

> Janela Pipeline, 2026-10-16. **Só leitura**: nenhum artefato foi alterado e não houve versão nova. Pedido da janela geral, aprovado pelo usuário em 16/10.
> **Base:** os 14 arquivos de `Downloads\BE-export-2026-10-16\`, lidos de uma cópia de trabalho.
> **Regra do usuário:** só fica em idioma local a coluna ou linha cujo cabeçalho ou contexto peça isso. Exemplos: "Local Name", "Label in Local Language", "Field Name (NL/FR)", "Description (NL)", "Report Name (Local)"; nomes oficiais de formulário, campo, zona ou documento da autoridade; valores literais de XML/XSD. Todo o resto deve estar em inglês: descrições, Field Explanation, notas, regras, títulos e instruções.
> **Origem do pedido:** Suman pediu "Field Explanation em inglês" ([[2026-10-13-triagem-chat-desde-09-10]] C4).

## Resumo por arquivo

| # | Arquivo | Violações (células) | Duvidosos (células) |
|---|---|---|---|
| 1 | BE-CCG-001-v1.0.docx | 0 | 0 |
| 2 | BE-SIR-001-v1.0.docx | 0 | 0 |
| 3 | BE-WTC-001-v1.0 (1).xlsx | 0 | 0 |
| 4 | BE-DD-001-v1.0.xlsx | **879** | 162 |
| 5 | BE_Compliance_Payslip_Generator.xlsx | 0 | 16 |
| 6 | BE-NSSO-001-Dimona-Spec.xlsx | **207** | 58 |
| 7 | BE-NSSO-002-DmfA-Spec.xlsx | **597** | 237 |
| 8 | BE-NSSO-003-DmfAModification-Spec.xlsx | **569** | 237 |
| 9 | BE-NSSO-004-DRS-Spec.xlsx | **518** | 169 |
| 10 | BE-NSSO-005-Limosa-Spec (1).xlsx | 0 | 0 |
| 11 | BE-FIN-001-Finprof274-Spec.xlsx | 0 | 0 |
| 12 | BE-FIN-002-Belcotax28110-Spec.xlsx | 0 | 0 |
| 13 | BE-FEBELFIN-001-SEPACreditTransfer-Spec.xlsx | 0 | 0 |
| 14 | BE-FEDRIS-001-WorkAccident-Spec.xlsx | **389** | 122 |
| | **Total** | **3 159** | **1 001** |

**Onde está o problema:**
- Specs que importaram o glossário da NSSO (Dimona, DmfA, DmfA Modification, DRS e FEDRIS/Work Accident). As colunas Conditional Reason, Format, Field Explanation e Option Values foram copiadas do glossário oficial em francês, sem tradução.
- DD: a coluna "English Description" das option mappers da NSSO traz só metadados e a frase literal da autoridade em NL/FR; não há descrição do código em inglês.
- Os outros 8 arquivos seguem a regra. Onde aparece termo local, ele está em coluna local ou entre parênteses como nome oficial (ex.: WTC "Wage withholding tax (bedrijfsvoorheffing)").

## Classificação das colunas (o que deve ser local e o que deve ser inglês)

### Specs (as 9 de Report Spec, aba principal "<Report> Spec")
| Coluna | Deve ser | Motivo |
|---|---|---|
| A Field Name (EN) | Inglês | Cabeçalho |
| B Field Name (FR — official NSSO glossary) / (NL) / (NL — UNOFFICIAL) | **Local** | Cabeçalho; nome oficial da zona |
| C Record Type | Inglês (com nome oficial do bloco entre parênteses) | Descrição do bloco |
| D Field Position ("Zone 00296") / H Position (XPath) / K Example | Literal | Identificador ou valor de XML |
| G Conditional Reason | Inglês | Regra |
| J Format | Inglês (máscara e tipo AN/N literais) | Explicação do formato |
| L System Mapping, N Relevant for Payroll, P–S | Inglês | Regra ou nota |
| M Field Explanation | Inglês | Cabeçalho e pedido do Suman |
| O Option Values | Inglês (códigos literais) | Regra e lista de valores |
| T Query to RA | Inglês | Pergunta ao analista (ver dúvida D1) |
| Field Options: C Description (EN) = inglês; D Description (NL) = **local**; B Option Code = literal; E Authority Reference = inglês, com título oficial do documento | | Cabeçalho |
| Report Matrix: B "Report Name (EN)" = inglês; C "Report Name (Local)" = **local**; linha 4 "Document Title" = inglês + nomes oficiais NL/FR | | Cabeçalho e nome oficial |
| Version Control, Payroll Scope Summary, File Structure, Population Rules, Example Analysis | Inglês | Instrução ou nota |
| Sample File | Literal | Conteúdo do arquivo |

### DD (BE-DD-001)
| Aba / coluna | Deve ser | Motivo |
|---|---|---|
| ID Information E, Country Fields F "Label in Local Language" | **Local** | Cabeçalho |
| ID Information C/F/H/V, Country Fields D/G/I/W | Inglês | Cabeçalho, descrição ou nota |
| Country Option Mappers D "Abbreviation", E "Local Name" | **Local** | Cabeçalho |
| Country Option Mappers B, **F "English Description"** | Inglês | Cabeçalho |
| Currency / Country Codes ISO | Literal | Listas ISO |

### WTC
- B "Wage Type Name in English": inglês.
- C "Wage Type Name in Local Language": **local**.
- As demais colunas e abas (Sick Leave, Tax Credit, Global WTC Coverage, Form Reference Guide): inglês.

### Payslip Generator
- "Belgium (NL)" e "Payslip Spec 1" C "Field Name (NL)": **local**.
- "Belgium (EN)", "Compliance Payslip", "Payslip Spec 1" B/D/E/F, Field Option, Population Range, UnitRate: inglês.

### CCG e SIR (docx)
- O texto corrido e as tabelas devem estar em inglês. As exceções são os nomes oficiais (ex.: "Fedris (Federaal agentschap … / Agence fédérale …)"), os títulos de documentos de fonte e as colunas marcadas como locais. Exemplo de coluna local: SIR §5.1.3, tabela 30, coluna "Label (FR)" com os rótulos oficiais das anomalias.

## Violações (detalhe)

Contagem = células não vazias da coluna com texto em FR ou NL, inteiro ou parcial, sem a descrição equivalente em inglês. Linhas de bloco (`═══ BLOCK …`) ficam fora. Em todas as violações o idioma atual é **francês** (glossário NSSO), salvo no DD, onde é NL/FR. O idioma esperado é sempre **inglês**.

### BE-NSSO-001-Dimona-Spec.xlsx — 207
| Aba | Coluna | Linhas | Células | Exemplo |
|---|---|---|---|---|
| Dimona Spec | G Conditional Reason | 13–93 | 46 de 54 | G13 "Obligatoire si l'employeur possède un numéro ONSS définitif et si le « Numéro d'entreprise »(zone 00014) n'est pas présent." |
| Dimona Spec | J Format | 4–93 | 25 de 77 | J4 "AN(10) — format: AAAA-MM-JJ · AAAA est l'année · MM est le mois . JJ est le jour" |
| Dimona Spec | M Field Explanation | 3–93 | 74 de 77 | M3 "Zone qui décrit la teneur d'un formulaire." |
| Dimona Spec | O Option Values | 3–93 | 54 de 77 | O3 "Voir annexe 11-Identification du formulaire. Cette zone doit avoir comme valeur « DIMONA »." |
| Field Options | C Description (EN) | 92–100 | 8 | C92 "CP auxiliaire ouvriers — Commission paritaire auxiliaire pour ouvriers." (nenhuma palavra em inglês) |

### BE-NSSO-002-DmfA-Spec.xlsx — 597
| Aba | Coluna | Linhas | Células | Exemplo |
|---|---|---|---|---|
| DmfA Spec | G Conditional Reason | 19–269 | 126 de 140 | G19 "Obligatoire si le trimestre de déclaration est antérieur au troisième trimestre 2004." |
| DmfA Spec | J Format | 4–265 | 46 de 237 | J4 (mesmo texto do Dimona J4); J109 "AN(9) — format: CCC. CC ou CCC. CC. CC" |
| DmfA Spec | M Field Explanation | 3–270 | 229 de 237 | M139 "Montant sur lequel un taux doit être appliqué afin de connaître le montant de la déduction…" |
| DmfA Spec | O Option Values | 3–270 | 188 de 237 | O270 "Nombre entier positif et élément de [1; 99999999999]. Le montant est exprimé en eurocents." |
| Field Options | C Description (EN) | 28–36 | 8 | C33 "CP banques — Commission paritaire pour les banques." |

### BE-NSSO-003-DmfAModification-Spec.xlsx — 569
| Aba | Coluna | Linhas | Células | Exemplo |
|---|---|---|---|---|
| DmfA Modification Spec | G Conditional Reason | 19–269 | 126 de 140 | G20 "Obligatoire si le trimestre de la déclaration est le 4e trimestre de l'année et si l'employeur occupe des travailleurs manuels." |
| DmfA Modification Spec | J Format | 4–265 | 46 de 237 | J5 "AN(12) — format: HH: MM: SS. SSS . HH sont les heures…" |
| DmfA Modification Spec | M Field Explanation | 5–269 | 209 de 237 | M7 "Restated at its corrected value for the original quarter. Le type indique la nature du formulaire électronique." (116 células começam em inglês e continuam em FR) |
| DmfA Modification Spec | O Option Values | 3–270 | 188 de 237 | O128 "Nombre entier et élément de [0; 99]." |

### BE-NSSO-004-DRS-Spec.xlsx — 518
| Aba | Coluna | Linhas | Células | Exemplo |
|---|---|---|---|---|
| DRS Spec | G Conditional Reason | 21–284 | 78 de 120 | G67 "Obligatoire si la déclaration DRS concerne une administration provinciale ou locale…"; G92 "Interdit" |
| DRS Spec | J Format | 4–289 | 42 de 235 | J112 "AN(7) — format: --MM-JJ . MM est le mois . JJ est le jour" |
| DRS Spec | M Field Explanation | 4–289 | 212 de 235 | M93 "Nombre moyen contractuel d'heures subsidiées par semaine par un fonds Maribel social." |
| DRS Spec | O Option Values | 3–289 | 186 de 235 | O142 "1=heure 2=jour 3=semaine 4=mois 5=trimestre 6=année Les valeurs permises pour les blocs 90014 et 90552 sont…" |

### BE-FEDRIS-001-WorkAccident-Spec.xlsx — 389
| Aba | Coluna | Linhas | Células | Exemplo |
|---|---|---|---|---|
| Work Accident Spec | G Conditional Reason | 19–199 | 60 de 118 | G36 "Obligatoire si il s'agit de l'adresse de correspondance(Type Of Address=="1")…"; G19 "Interdit" |
| Work Accident Spec | J Format | 4–217 | 32 de 179 | J109 "N(4) — format: HHMM: . HH sont les heures . MM sont les minutes" |
| Work Accident Spec | M Field Explanation | 4–218 | 155 de 179 | M108 "Moment précis, exprimé en heures et minutes. Début de la pause pour le jour où l'accident s'est produit." |
| Work Accident Spec | O Option Values | 3–218 | 134 de 179 | O218 "Une série de 25 caractères maximum." |
| Field Options | C Description (EN) | 49–57 | 8 | C49 "CP auxiliaire ouvriers — Commission paritaire auxiliaire pour ouvriers." |

### BE-DD-001-v1.0.xlsx — 879 (aba Country Option Mappers, coluna F "English Description")
As células abaixo têm só metadados em inglês ("Applicability", "Quarters", "Valid", "Sector"). O significado do código aparece apenas em NL/FR: em "Contribution type:" / "Category:" e na frase "Authority's wording (Dutch|French, verbatim): '…'". Ou seja, a descrição em inglês do código não existe.

| Option mapper | Linhas | Células | Idioma atual | Exemplo |
|---|---|---|---|---|
| NSSO Worker Code | 115–300 | 186 | NL | F115 (código 241): "Contribution type: Bijdrage niet gebonden aan een natuurlijke persoon. Worker type: Andere (type werknemers)… Authority's wording (Dutch, verbatim): 'Jaarlijkse bijdrage voor dekking…'" |
| NSSO Employer Category | 303–591 | 289 | NL | F520 (632): "Sector: Privé. Valid … Authority's wording (Dutch, verbatim): 'Werkgevers die ressorteren onder het paritair subcomite…'" |
| Joint Committee Number | 594–818 | 225 | NL | F601 (102.05): "Category: Paritaire organen bevoegd voor de werknemers die hoofdzakelijk handarbeid verrichten…" |
| Work Reorganisation Measure | 842–899 | 58 | FR | F848 (6): "Applicability: … Authority's wording (French, verbatim): 'Prépension à mi-temps'." |
| Employment Promotion Measure | 902–916 | 15 | FR/NL | F903 |
| Legal Basis for Part-Time Work With Benefit Retention | 1806–1815 | 10 | FR/NL | F1807 |
| DmfA Remuneration Code | 1926–1969 | 44 | FR | F1928 (3): "… Authority's wording (French, verbatim): 'Les indemnités qui sont payées au travailleur lorsqu'il est mis fin au contrat…'" |
| DmfA Service Code | 1972–2023 | 52 | FR | F2023 (301): "… 'toutes les données relatives au temps de travail couvertes par une indemnité exonérée…'" |

Observação: as linhas 284–300 (NSSO Worker Code) não têm código. São comentários do tipo "Contribution type: - Gewone bijdrage : stemt overeen met…", todos em NL, e estão incluídas nas 186.

## Casos duvidosos (decisão do usuário)

| # | Arquivo / aba / coluna | Linhas | Células | Exemplo | Por que é dúvida |
|---|---|---|---|---|---|
| D1 | Specs Dimona (3–93), DmfA (3–270), DmfA Mod. (3–270), DRS (3–289), FEDRIS (3–217) — coluna **T Query to RA** | ver ao lado | 58 + 237 + 237 + 169 + 122 = **823** | DmfA T3 "Anomaly codes on the ACRF: Non présent 00296-001 B Pas dans le domaine de définition 00296-008 B…" | O prefixo está em inglês; os rótulos das anomalias são texto oficial da ACRF (Annexe 30). Pela regra, não são nome de formulário, campo ou zona, o que pede inglês; mas são texto literal da autoridade. O SIR resolve isso com uma coluna própria "Label (FR)". |
| D2 | DD Country Option Mappers F — NSSO Worker Status, Risk Identification (DRS Annexe 12) | 68–110; 1846–1923 | 24 + 78 = **102** | F73 "Worker employed outside the normal labour circuit. … Authority's remark (Dutch, verbatim): 'Het gaat om werknemers…'" | A descrição em inglês existe; o que sobra é a citação literal da autoridade dentro da coluna em inglês. Pode ficar como citação oficial ou passar para "Local Name". |
| D3 | DD Country Option Mappers F — Health Insurance Fund Code | 1381–1459 | **60** | F1390 "Christelijke Mutualiteit van het Land van Waas en Dendermonde (Christian)"; F1440 "Office régional du Hainaut (Mons) (Auxiliary (CAAMI/HZIV))" | É nome próprio oficial da mutualidade, com o tipo em inglês entre parênteses. Nome de instituição não está nos exemplos da regra. |
| D4 | Payslip Generator / Payslip Spec 1 / B "Field Name (EN)" | 2, 12, 27, 44, 55, 66, 77, 82, 91, 101, 122, 134, 146, 155, 167 | **15** | B12 "Employer Fields  /  Gegevens van de werkgever" | Faixas de seção bilíngues numa coluna EN; a coluna C (NL) já existe ao lado. |
| D5 | Payslip Generator / Belgium (EN) / C12 | 12 | **1** | "200 - Aanvullend Paritair Comité voor de Bedienden" | Nome oficial da comissão paritária no holerite em inglês; pela regra pode ficar, mas o resto da aba está traduzido. |

Fica em local, conforme a regra (não conta como violação nem como dúvida):
- Report Matrix C "Report Name (Local)" e títulos oficiais na linha 4.
- SIR §5.1.3 "Label (FR)" e os títulos de documentos em §7.2–7.4.
- Exemplos de mensagens de erro do Belcotax no SIR §5.2.2.
- Nomes oficiais entre parênteses no WTC, no DD Country Fields e no CCG (ex.: "Fedris (Federaal agentschap… / Agence fédérale…)").
- Campos "vak"/"zone" citados nas notas.

## Decisões para o usuário
1. **D1, Query to RA (823 células):** traduzir os rótulos das anomalias para o inglês, mantendo código e gravidade? Ou manter os rótulos em FR como texto oficial, com o prefixo em inglês? Recomendo traduzir, citando a Annexe 30 como fonte, como o SIR já faz numa coluna separada.
2. **Option Values (O) e Format (J):** confirmar que os códigos e as máscaras ficam literais (ex.: `0=`, `AN(10)`, `AAAA-MM-JJ`) e que só o texto passa para o inglês. Também: os rótulos dos códigos (ex.: "3=Annulation") vão para o inglês? Recomendo inglês, mantendo o rótulo oficial entre parênteses quando for nome da autoridade.
3. **DD English Description (879):** escrever a descrição em inglês de cada código e manter ou não a citação "Authority's wording (…, verbatim)" no fim (vale também para D2). Recomendo manter a citação, porque é fonte, e acrescentar o inglês antes dela.
4. **D3 mutualidades (60):** manter o nome oficial (recomendado) ou traduzir?
5. **D4/D5 payslip (16):** deixar as faixas só em inglês na coluna B? (Recomendado: sim, o NL já está na coluna C.) E manter o nome oficial da comissão paritária no holerite EN?
6. **Field Options "CP …" (24 células: Dimona, DmfA, FEDRIS):** acrescentar o nome em inglês da comissão e manter o nome oficial francês entre parênteses?

## Achados fora do pedido (não são de idioma)
- Payslip Generator, aba "How to set up Payslip" I7–I10: o exemplo ainda mostra **Mercans Estonia**, Tartu, Estonia, período 10/2023. É o exemplo do template, não da Bélgica.
- Colunas "Description (NL)" dos Field Options com `NOT FOUND`: Limosa D3–D7 e D12 (6 células), DRS D6–D19 (7), DmfA D8/16/52/53/89 (5), FIN-001 D60/68/69 (3), FEBELFIN D22/42 (2), FEDRIS D59 (1), DmfA Modification D11 (1). Não é problema de idioma; é lacuna de conteúdo.
- FEDRIS Field Options E29 cita "BE-DD-001-v1.4", mas o export do DD chama-se `v1.0`. É preciso conferir a versão vigente no Drive antes de qualquer correção (regra 8).

## Como foi conferido
- Inventário de todas as abas e colunas dos 12 xlsx (cabeçalho, estado da aba) e de todos os parágrafos e células das tabelas dos 2 docx.
- Classificador de idioma por palavras funcionais FR/NL/DE/EN. Texto entre parênteses e entre aspas é ignorado, porque é nome oficial. Termos ambíguos (type, code, zone, occupation, de, of) foram tirados da contagem. Palavras isoladas em FR ("Interdit", "Obligatoire", "Facultatif", "Non présent") foram tratadas à parte.
- Todo grupo de violação foi conferido à mão, com amostra no início, no meio e no fim da faixa. Falsos positivos foram excluídos:
  - "Medecins en formation — Doctors in specialist training", nas Field Options;
  - nomes de países NIS no DD;
  - "Régime 5" em N19.
- A contagem do DD separa as células sem significado em inglês (violação) das que têm inglês e mais a citação literal (dúvida D2).
- Limite: a contagem automática pode errar por poucas células nas bordas (frases curtas, mistas). As faixas e os exemplos acima foram lidos diretamente no arquivo.

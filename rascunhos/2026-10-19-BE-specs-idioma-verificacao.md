# Bélgica: verificação de idioma das Report Specs nas versões vigentes

> Janela Pipeline, 2026-10-19, a pedido da janela geral (decisão do usuário: Bélgica, um item por vez, começando pelas Report Specs). **Só análise:** nada foi corrigido, não há versão nova e o Drive não foi tocado.
> **Origem:** pedido da Suman, "Field Explanation dos Report Specs BE em inglês" ([[2026-10-13-triagem-chat-desde-09-10]] C4; call de 16/10, `raw/chats/2026-10-16-cross-training-design-creation.txt`, 45:17 e 49:57).
> **Regra aplicada:** a mesma da auditoria de 16/10 ([[2026-10-16-BE-auditoria-idioma]]). Só fica em idioma local a coluna cujo cabeçalho peça isso (ex.: "Field Name (FR — official NSSO glossary)", "Description (NL)"), além dos nomes oficiais e dos literais de XML. Todo o resto vai para o inglês.

## 1. Versão vigente de cada spec

São **9** Report Specs BE, não 10. A pasta `Belgium\12- Country Report Codes` do Drive tem 9 `.gsheet` e nenhuma pasta `Archived`. "As do FIN" são 2: FIN-001 e FIN-002. O nome do arquivo não traz versão; a versão está na aba Version Control.

| Spec | Versão vigente (Version Control) | Onde (oficial) | Última alteração do .gsheet | Export usado (md5) |
|---|---|---|---|---|
| BE-NSSO-001 Dimona | 1.0 (2026-09-16, "Aprovedd") | Drive, 12- Country Report Codes (.gsheet) | 09/10/2026 07:08 | `Downloads\BE-export-2026-10-16\` 259c07cf… |
| BE-NSSO-002 DmfA | 1.0 (2026-09-16) | idem | 09/10/2026 07:09 | f97c844d… |
| BE-NSSO-003 DmfA Modification | 1.0 (2026-08-14) | idem | 16/09/2026 17:35 | 527cce1f… |
| BE-NSSO-004 DRS | 1.0 (2026-09-16) | idem | 09/10/2026 07:11 | e2813a0d… |
| BE-NSSO-005 Limosa | 1.0 (2026-09-16) | idem | 16/09/2026 17:38 | d867da19… |
| BE-FIN-001 Finprof 274 | 1.0 (2026-09-16) | idem | 09/10/2026 06:42 | 664c6170… |
| BE-FIN-002 Belcotax 281.10 | 1.0 (2026-09-16, **Draft**) | idem | 09/10/2026 06:46 | 62502227… |
| BE-FEBELFIN-001 SEPA | 1.0 (2026-09-16) | idem | 09/10/2026 06:40 | 74ef694e… |
| BE-FEDRIS-001 Work Accident | 1.0 (2026-09-16) | idem | 16/09/2026 17:23 | de94e9cc… |

- **Os exports de 16/10 são as vigentes.** O export foi feito em 16/10 às 09:54. A última alteração de cada `.gsheet` no disco `G:` é igual ou anterior a 09/10, então nenhuma spec mudou depois do export. Os 9 arquivos de `Downloads\BE-export-2026-10-16\` também não foram alterados desde 16/10 09:54: são os mesmos que a auditoria leu.
- **Cópias mais antigas, não usadas:**
  - `Downloads\BE-NSSO-005-Limosa-Spec.xlsx` (25/08), anterior à linha 1.0;
  - `~/mercans-pipeline/BE-compliance/04-reports-spec/*.xlsx` (16/09, pipeline).
- **Limite:** o conector do Google Drive pediu novo login, então a data de alteração vem do `G:` (Drive para desktop), não da API. Se você quiser certeza total, abra o histórico de versões de uma das specs no Sheets.
- **Nenhuma spec falta exportar.**

## 2. Idioma nas versões vigentes

Contagem = células da coluna com texto em FR (glossário NSSO) sem o equivalente em inglês. Os números da auditoria de 16/10 foram conferidos à mão e continuam valendo. A reaplicação de hoje, com um classificador novo e independente, dá números próximos (entre parênteses). A diferença vem do critério de borda do classificador, não do conteúdo: os arquivos são idênticos.

| Spec | G Conditional Reason | J Format | M Field Explanation | O Option Values | T Query to RA (dúvida D1) | Field Options C "Description (EN)" |
|---|---|---|---|---|---|---|
| Dimona | 46 de 54 (46) | 25 de 77 (23) | 74 de 77 (51 + 15 mistas) | 54 de 77 (47) | 58 (26 + 23) | 8 "CP …" (9) |
| DmfA | 126 de 140 (125) | 46 de 237 (42) | 229 de 237 (205 + 17) | 188 de 237 (160 + 11) | 237 (204 + 3) | 8 "CP …" (9) |
| DmfA Modification | 126 de 140 (125) | 46 de 237 (42) | 209 de 237 (200 + 22) | 188 de 237 (160 + 11) | 237 (204 + 3) | 0 |
| DRS | 78 de 120 (74) | 42 de 235 (40) | 212 de 235 (169 + 18) | 186 de 235 (167 + 4) | 169 (164 + 3) | 0 |
| FEDRIS Work Accident | 60 de 118 (74) | 32 de 179 (29) | 155 de 179 (115 + 24) | 134 de 179 (90 + 24) | 122 (116 + 14) | 8 "CP …" (9) |
| Limosa | 0 | 0 | 0 | 0 | 0 | 0 |
| Finprof 274 | 0 | 0 | 0 | 0 | 0 | 0 |
| Belcotax 281.10 | 0 | 0 | 0 | 0 | 0 | 0 |
| SEPA | 0 | 0 | 0 | 0 | 0 | 0 |

**Colunas que ficam em idioma local por cabeçalho (não contam):**
- Spec, coluna B: "Field Name (FR — official NSSO glossary)" nas 5 NSSO/FEDRIS, "(NL)" no FIN-001 e FIN-002, "(NL — UNOFFICIAL)" no Limosa e "(NL — descriptive)" no SEPA.
- Field Options, coluna D: "Description (NL)", em todas as specs.
- Report Matrix: "Report Name (Local)".
- Coluna D "Field Position" ("Zone 00296"): literal.

As colunas G, J, M, O e T **não** são locais pelo cabeçalho; a regra pede inglês nelas.

### Exemplos reais (2 por coluna com violação)

**Dimona**
- G: G13 "Obligatoire si l'employeur possède un numéro ONSS définitif et si le « Numéro d'entreprise »(zone 00014) n'est pas présent."; G53 "Obligatoire si l'employeur est concerné par le système des sous-entités. Interdit dans les autres cas."
- J: J4 "AN(10) — format: AAAA-MM-JJ · AAAA est l'année · MM est le mois . JJ est le jour"; J51 "AN(9) — format: CCC ou CCC. CC ou CCC. CC. CC"
- M: M3 "Zone qui décrit la teneur d'un formulaire."; M4 "Date à laquelle le formulaire est créé."
- O: O3 "Voir annexe 11-Identification du formulaire. Cette zone doit avoir comme valeur « DIMONA »."; O46 "La date de fin doit être inférieure à l'année en cours+10 ans et supérieure ou égale à 1999-01-01…"
- T: T13 "Anomaly codes on the ACRF: Invalide 00011-003 B Interdit 00011-005 B Incompatible avec le numéro d'identification…"; T21 "Anomaly codes on the ACRF: Invalide 00025-003 B Incompatible avec le NISS 00025-348 NP"
- Field Options C: C92 "CP auxiliaire ouvriers — Commission paritaire auxiliaire pour ouvriers."; C93 "CP mixte des mines — Commission nationale mixte des mines."

**DmfA**
- G: G19 "Obligatoire si le trimestre de déclaration est antérieur au troisième trimestre 2004."; G110 "Obligatoire si, à partir du 1/2024, le travailleur avec un contrat flexi-job n'a pas été déclaré…"
- J: J4 (mesmo texto do Dimona J4); J65 "AN(9) — format: CCC ou CCC. CC ou CCC. CC. CC"
- M: M4 "Date à laquelle le formulaire est créé."; M142 "Nombre de mois faisant l'objet, au cours du trimestre traité, de la prise en charge temporaire, par l'ONSS…"
- O: O6 "0=Original 1=Modification 2=Duplicata 3=Annulation 4=Révision 5=Rappel 6=Clôture…"; O130 "Nombre entier positif et élément de [0; 99999999999]. La valeur zéro est autorisée uniquement…"
- T: T3 "Anomaly codes on the ACRF: Non présent 00296-001 B Pas dans le domaine de définition 00296-008 B…"; T148 "Anomaly codes on the ACRF: Non présent 00143-001 B Invalide 00143-003 B…"
- Field Options C: C28 "CP auxiliaire ouvriers — Commission paritaire auxiliaire pour ouvriers."; C29 "CP mixte des mines — Commission nationale mixte des mines."

**DmfA Modification**: o padrão é o mesmo do DmfA, linha por linha, em G, J, O e T. A diferença está na coluna M, onde o texto começa em inglês e continua em FR:
- M: M5 "Restated at its corrected value for the original quarter. Moment précis, exprimé en heures, minutes, secondes et millièmes de secondes."; M143 "Restated at its corrected value for the original quarter. Numéro d'identification d'une personne physique au sein de la sécurité sociale…"
- G: G19 e G110, mesmos textos do DmfA.
- O: O3 "Voir annexe 11-Identification du formulaire. DMFA pour les déclarations multifonctionnelles trimestrielles"; O130 (igual ao DmfA).

**DRS**
- G: G21 "Interdit"; G140 "Obligatoire si(bloc 90553) la période de référence ne correspond pas au 2 ème trimestre complet…"
- J: J4 (igual ao Dimona J4); J74 "AN(9) — format: CCC ou CCC. CC ou CCC. CC. CC"
- M: M4 "Date à laquelle le formulaire est créé."; M143 "Montant, exprimé en cents, correspondant à la rémunération pour les heures supplémentaires…"
- O: O4 "AAAA est un élément de [année en cours-1; année en cours]; La date ne peut pas se trouver dans le futur…"; O139 "Bloc 90552: [2015-12-01, date du jour] Bloc 90553: [2016-04-01, date du jour]"
- T: T3 "Anomaly codes on the ACRF: Intitulé anomalie Code anomalie Gravité Non présent 00110-001 B…"; T143 "… Non présent 00406-001 B Non numérique 00406-002 B…"

**FEDRIS Work Accident**
- G: G19 "Interdit"; G110 "Obligatoire si 00430 Identification Of Risk= "001" Interdit si 00430 Identification Of Risk= "002""
- J: J4 (igual ao Dimona J4); J109 "N(4) — format: HHMM: . HH sont les heures . MM sont les minutes"
- M: M4 "Date à laquelle le formulaire est créé."; M109 "Moment précis, exprimé en heures et minutes. Indication du moment précis auquel la victime a signalé l'accident du travail à son employeur."
- O: O4 "AAAA est un élément de [année en cours-1; année en cours]…"; O92 "Une série de 30 caractères maximum."
- T: T3 "Anomaly codes on the ACRF: Intitulé anomalie Code anomalie Gravité Non présent 00110-001 B…"; T107 "… Non présent 00247-001 B Pas dans le domaine de définition 00247-008 B…"
- Field Options C: C49 "CP auxiliaire ouvriers — Commission paritaire auxiliaire pour ouvriers."; C50 "CP mixte des mines — Commission nationale mixte des mines."

**Limosa, Finprof 274, Belcotax 281.10 e SEPA**: 0 violações. O texto local está só nas colunas locais por cabeçalho ou entre parênteses, como nome oficial.

## 3. Diferenças em relação à auditoria de 16/10

- **Conteúdo: nenhuma.** As vigentes são os mesmos 9 arquivos auditados em 16/10, sem alteração depois disso. As 5 specs com violação e as 4 sem violação continuam as mesmas.
- **Correção de um detalhe:** são 9 specs, não 10. O pedido dizia "10 Report Specs", mas a pasta do Drive tem 9.
- **Ponto aberto do FEDRIS ("BE-DD-001-v1.4"):** está resolvido como fato, mas o problema é maior do que o descrito em 16/10:
  - as **9 specs** citam "BE-DD-001-v1.4", não só o FEDRIS: 791 citações no total (DmfA 212, DRS 161, FEDRIS 127, DmfA Mod. 121, Dimona 96, Belcotax 37, Limosa 26, SEPA 7, Finprof 4);
  - o DD vigente no Drive é `02- DD\BE-DD-001-v1.0.gsheet` (alterado em 17/09/2026). A Version Control dele tem só a linha 1.0 (2026-09-16, "Initial version.");
  - **não existe v1.4 no Drive.** Em Downloads há uma `BE-DD-001-v1.2-DRAFT-2026-08-20.xlsx` (anterior);
  - não é de idioma, mas mexe nas mesmas specs.

## 4. O que depende do usuário (só as decisões que afetam as specs)

As decisões completas estão em [[2026-10-16-BE-auditoria-idioma]] § "Decisões para o usuário". Afetam as specs:

1. **Decisão 1 (D1), coluna T Query to RA (823 células):** traduzir os rótulos das anomalias da ACRF (Annexe 30), mantendo código e gravidade, ou manter em FR como texto oficial?
2. **Decisão 2, colunas O e J:** confirmar que códigos e máscaras ficam literais (`0=`, `AN(10)`, `AAAA-MM-JJ`) e que só o texto passa para o inglês. Também decidir se os rótulos dos códigos ("3=Annulation") vão para o inglês.
3. **Decisão 6, Field Options "CP …" (24 células: Dimona, DmfA, FEDRIS):** nome da comissão em inglês, com o nome oficial em FR entre parênteses?
4. **Nova, por causa do item 3:** na correção das specs, a citação "BE-DD-001-v1.4" deve:
   - (a) passar para "v1.0", a vigente no Drive;
   - (b) esperar a promoção de uma DD nova;
   - ou (c) ficar como está?

   Mexer nas 791 citações é uma propagação à parte e pede a decisão antes.

Recomendação de ordem: corrigir primeiro G e M (Conditional Reason e Field Explanation), que são o pedido da Suman e não dependem de decisão. Depois J e O, conforme a decisão 2. Por último T e Field Options, conforme as decisões 1 e 6.

## Como foi conferido
- Drive: listagem de `Belgium\12- Country Report Codes` e `02- DD`, com a data de alteração de cada `.gsheet`. Downloads e `mercans-pipeline\BE-compliance\04-reports-spec`: procura por specs BE mais novas que o export (nenhuma).
- Version Control de cada export lida com openpyxl, numa cópia de trabalho no scratchpad (somente leitura).
- Idioma: classificador por palavras funcionais FR/NL × EN, ignorando texto entre parênteses e aspas. Palavras isoladas ("Interdit", "Obligatoire") contam como violação. Foi rodado sobre as colunas G, J, M, O e T da aba principal e sobre a coluna C das Field Options. Os exemplos acima foram lidos direto nas células.
- Citações "BE-DD-001-v*": busca por regex em todas as células das 9 specs.

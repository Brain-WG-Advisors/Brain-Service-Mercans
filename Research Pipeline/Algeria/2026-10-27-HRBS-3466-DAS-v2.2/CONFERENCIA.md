# HRBS-3466 (Argélia / Henkel): spec DAS v2.2, conferência

> Tudo aqui é **local**. Nada foi para o Drive, o YouTrack, e-mail ou chat. Status da v2.2: **Draft**. A v2.1 continua CURRENT até o usuário aprovar.

## Arquivos
| Arquivo | md5 | O que é |
|---|---|---|
| [[Research Pipeline/Algeria/2026-10-27-HRBS-3466-DAS-v2.2/DZ-CNAS-DAS-CountryStandard-Spec_v2.2.xlsx\|DZ-CNAS-DAS-CountryStandard-Spec_v2.2.xlsx]] | `3c22c5ebd960ed9d259072bfff5f41b8` | Spec v2.2 (12 abas da v2.1 + aba nova "Henkel Configuration") |
| `build_v2_2.py` | ver `md5sum` | Gera a v2.2 por cirurgia XML. Uso: `python -I build_v2_2.py <v2.1.xlsx> <v2.2.xlsx>` |
| `compare_v21_v22.py` | ver `md5sum` | Compara v2.1 × v2.2 célula a célula e valida o XML |
| `changes_manifest.json` | — | As 135 células alteradas/novas, cada uma com o ID da mudança (C1..C11), antes e depois |
| `conferencia-v2.2-log.txt` | — | Saída da comparação: todas as diferenças, contagens e varreduras |

**Base:** [[raw/docs/drive-exports/2026-10-23/DZ-CNAS-DAS-CountryStandard-Spec_v2.1.xlsx|DZ-CNAS-DAS-CountryStandard-Spec_v2.1.xlsx]] (md5 `5e4d67e1c2a4a6bc660972647d5e2a11`), export do `.gsheet` do Drive (`12- Country Report Codes\DAS file\`).
**DD:** [[raw/docs/drive-exports/2026-10-27/DZ-DD-001-v1.1.xlsx|DZ-DD-001-v1.1.xlsx]], copiado para [[raw/docs/drive-exports/2026-10-27/DZ-DD-001-v1.1.xlsx|DZ-DD-001-v1.1.xlsx]] (md5 `37d2ea88e2ba99d216a8ebd3579d7be5`, idêntico ao do Drive). Observação: a aba Version Control desse arquivo só registra a linha 1.0, embora o nome do arquivo seja v1.1.

## Fontes (relidas por mim em 2026-10-27)
| Fonte | Onde | O que sustenta |
|---|---|---|
| CNAS, *Guide de Télédéclaration* (SHA-256 `1b37da0c1fa6cef0…`) | [[raw/docs/oficiais/DZ/2026-10-23-CNAS-guide-teledeclaration.pdf\|2026-10-23-CNAS-guide-teledeclaration.pdf]] | p.14: o EMS considera movimento "tout changement du numéro employeur dont le salarié est rattaché". p.35–36: nome `D20E/D20S` + "Numéro du Cotisant sur 10 positions", e a tabela de campos. p.36: M/J/H, Observation "dans la mesure du possible", centimes, "aucun cas avoir de séparateur de rubriques". p.41–42: "Numéro cotisant (employeur) erroné", "Nombre de mois/jours incorrect". |
| Loi n° 83-14 du 2 juillet 1983, JORADP n° 28 (escaneada; li a imagem das p.21–22 do arquivo, p.1217–1218 do JO) | [[raw/docs/oficiais/DZ/2026-10-23-JORADP-1983-028-Loi-83-14.pdf\|2026-10-23-JORADP-1983-028-Loi-83-14.pdf]] | Art. 14: "dans les trente (30) jours qui suivent la fin de chaque année civile … par trimestre". O art. 16 original dizia 10 % + 2 % por mês. |
| Loi n° 04-17 du 10 novembre 2004, JORADP n° 72 de 13/11/2004 | [[raw/docs/oficiais/DZ/2026-10-23-JORADP-2004-072-Loi-04-17.pdf\|2026-10-23-JORADP-2004-072-Loi-04-17.pdf]] | Art. 11 (novo art. 16): "pénalité égale à 15 % du montant des cotisations dues … majorée de 5 % par mois de retard". Art. 12 (art. 16 bis): "mille dinars (1.000 DA) par travailleur et/ou inexactitude". |
| DAS 2024 aceita da Henkel (anexos do ticket) | `raw/tickets/api/anexos/HRBS-3466/` | Nº `1638091858` no nome e no campo 1 (entête e os 80 registros); endereço do entête em Dely Ibrahim; unidade `J` nos 4 trimestres dos 80 registros. Conferi isso por script, sem extrair dado pessoal. |
| DZ-DD-001-v1.1 | ver acima | Nomes reais: `Employer.CNASNumber`, `Employer.CNASCentre`, `Employer.LegalName`, `Employer.Address` (sede), `Employee.SSNumber`, `Employee.JobTitle`. Não existem: denominação, endereço do estabelecimento, vínculo empregado → estabelecimento, frequência de pagamento/unidade DAS. |

## Decisões
- **Cirurgia XML e zip.** As 12 abas da v2.1 não têm imagem nem comentário (os 12 `drawingN.xml` estão vazios). Mesmo assim, não usei `openpyxl.save()`. As partes não alteradas são copiadas com conteúdo idêntico (o log mostra "identica" para cada uma). Os textos novos foram **acrescentados** ao `sharedStrings.xml`, sem mexer nos índices existentes.
- **Destaque.** Cada célula alterada ou nova recebeu um clone do seu estilo original com o preenchimento `FFDDEBF7`. Nas células da DAS Spec, isso substitui a cor de tier (verde/amarelo) só nelas.
- **Altura de linha.** Ajustei só a altura das linhas que receberam texto maior, para o texto não ficar cortado. Nenhuma coluna, posição ou campo de layout foi mexido.
- **Population Rules.** As regras novas entraram **depois** da última linha (26–29), sem deslocar nada.
- **Mantidos de propósito:**
  - A aba "Change Log vs Pipeline" (inclusive N-08, que cita "31 January" e "15% + 2%/month") é o histórico da v2.1. Não reescrevi o histórico; a correção está registrada na linha v2.2 do Version Control.
  - O Sample File ainda mostra Observation preenchida (CADRE etc.). Continua válido, porque o campo é opcional, e mexer nele seria fora das 11 mudanças. ⚠️ Pode ser alinhado ao default em branco numa próxima versão, se o usuário quiser.
  - Field Options F7–F9 ("Use when pay frequency is …") e Example Analysis, salvo D10 e D17.
  - `DD: Payroll.ReferenceYear` (L6 e L20) **também não existe no DD v1.1**, mas não estava entre os 6 nomes pedidos. Ficou como está; ver Lacunas.
- **"Working Hours".** A v2.1 não tinha esse texto (grep no `sharedStrings.xml`: 0 ocorrências). A v2.2 proíbe o uso de forma explícita nos mapeamentos de duração ("Never hours; never 'Working Hours'").

## Antes → depois, por mudança
| ID | Mudança | Células | Antes → depois (resumo) |
|---|---|---|---|
| C1 | Geração por estabelecimento | Report Matrix B21; DAS Spec L4, L19, M21, M39, M40; File Structure C7, C27; Validation E10 (STR-05); Population Rules A26:D29 (novas) | "1 par por nº CNAS" → mais a chave empregado → estabelecimento → nº CNAS (10), centre payeur (5), Dénomination, Raison sociale, Adresse. `N° Ligne` reinicia por arquivo. Transferência no ano marcada como **⚠️ PROPOSAL – NO PRIMARY SOURCE** (só a p.14, EMS). |
| C2 | Nome do arquivo | DAS Spec M3, M18; File Structure C5, C6 | Mais: o cotisant é o nº CNAS (10) do estabelecimento, o mesmo em todos os registros. |
| C3 | Mapeamentos × DD | DAS Spec L7, L8, L10, L22; L27/30/33/36 (com C6); L28/31/34/37 (com C4) | `Employer.CNASPayingCentre` → `Employer.CNASCentre`. `Employer.Denomination` → NEW DD FIELD (proposed): Establishment Denomination. `Employer.RegisteredAddress` → NEW DD FIELD (proposed): Establishment Address (`Employer.Address` = só a sede). `Employee.SocialSecurityNumber` → `Employee.SSNumber`. `Employee.PayFrequency` → NEW DD FIELD (proposed): DAS Duration Unit / Pay Frequency. `Payroll.ContributoryBase Qn` → resultado de folha, WT 64551 (to be confirmed by Development). |
| C4 | Duração em dias | DAS Spec L26/29/32/35, M26, M29, M32, M35; Population Rules C9 (com C6) | Unidade J = DIAS 0–92 (convenção Henkel: 90 menos dias de ausência não remunerada; WTs 63121/63122/63129/63801 to be confirmed by Development). M26: "NO SEPARATOR … correct per the guide (p.36)", com o exemplo do 143J inválido. Nunca horas. |
| C5 | Observation | DAS Spec K41, L41, M41; File Structure C39 | "CADRE" / `Employee.JobTitle` → "(20 spaces)" / "Blank (20 spaces) by default; JobTitle só se o cliente pedir". |
| C6 | Unidade = parâmetro do cliente | DAS Spec M27/30/33/36; Evidence Register D16; Validation E49 (SEM-03) | "MUST be derived from pay frequency, never hard-coded" → parâmetro do cliente (M pelo guia p.36; Henkel histórico J). A decisão é do cliente. |
| C7 | SEM-02 → WARN | Validation C48 (A→B), D48 (BLOCK→WARN), E48; Population Rules C10, D10 (A→B); DAS Spec G26/29/32/35 | Explica que o guia não traz a regra e que o arquivo aceito tem 9 casos. |
| C8 | Prazo e penalidade | Report Matrix B13, B14, B15; Validation E57, F57 (HSK-01) | "31 January … CNAS communiqués confirm" → texto do art. 14 (30 dias; 30/01 na contagem literal; ⚠️ 31/01 sem texto regulamentar). "15% + 2%/month (CNAS communiqué)" → art. 16 (Loi 04-17) 15 % + 5 %/mês e art. 16 bis 1.000 DA. |
| C9 | Células-fórmula | Example Analysis D10, D17 | `<f>` com `#ERROR!` → texto "Equals 4 x 2,700,000,000 exactly (ARI-01)." / "Equals 0 + 1,800,000,000 + …". Conferi as contas: 4 × 2.700.000.000 = 10.800.000.000 e a soma dá 7.200.000.000. |
| C10 | Version control | Version Control A15:F15; Report Matrix B22 | Nova linha 2.2 / 2026-10-27 / resumo / Draft / Wallisson Gomes. Report Matrix "Version" → "2.2 – Draft; 2.1 remains current". |
| C11 | Aba Henkel Configuration | aba nova (51 células); Version Control B5 (aviso de anexo de cliente) | 3 locais × nº CNAS, centre payeur, Dénomination, Raison sociale, Adresse, população, unidade, Observation, fonte. |

## Conferência
- **Comparação célula a célula** (`compare_v21_v22.py`, log em `conferencia-v2.2-log.txt`): **135 células diferentes, 135 no manifesto, 0 fora do manifesto, 0 sem destaque azul, 0 falhas.** Por aba: Version Control 7 · Report Matrix 5 · Evidence Register 1 · DAS Spec 38 · File Structure 5 · Population Rules 19 · Validation Rules 7 · Example Analysis 2 · Henkel Configuration 51. As abas Change Log, Payroll Scope Summary, Field Options e Sample File ficaram **sem alteração**.
- **XML:** todas as partes `.xml`/`.rels` passam no parser. Nenhuma parte foi perdida, e `testzip` deu OK. Partes alteradas: workbook, rels, Content_Types, sharedStrings, styles, sheets 1/3/4/6/7/9/10/11 e a sheet13 nova; todas as outras são idênticas.
- **Abre sem erro:** openpyxl carrega o arquivo. O Excel (COM, só leitura) abriu com 13 abas, e D10 é exibido como texto.
- **Validador do toolkit** (`mercans-artifact-toolkit/scripts/validate_workbook.py`): sem erro de fórmula. Saem 31 BLOCKERs C29 "residual marker", **todos** vindos do texto "TO BE CONFIRMED (BY CLIENT / by Development)" que a tarefa exige (DAS Spec L26–L37 e a aba Henkel). A v2.1 dá PASS. Isso é coerente com o status **Draft**: a v2.2 não pode ser promovida a final enquanto esses itens estiverem abertos.
- **Varreduras:** nenhuma célula começa com "=". Nenhum dos nomes inexistentes no DD sobrou. Nenhum número de 12 dígitos (nº de segurado) na aba Henkel. Não copiei nome, salário nem nº de segurado dos anexos.

## Lacunas
- ⚠️ **Nºs CNAS, centre payeur, Dénomination, Raison sociale, Adresse e população** de Reghaia e Chelghoum Laid, e todos os campos menos o nº de Dely Ibrahim: TO BE CONFIRMED BY CLIENT.
- ⚠️ **Não está provado** que os 3 locais tenham nº CNAS distinto, nem que o nº 1638091858 cubra só Dely Ibrahim: o arquivo de 2024 trazia 80 empregados sob um único nº.
- ⚠️ **Transferência entre estabelecimentos no ano:** proposta sem fonte primária.
- ⚠️ **Unidade J × M para a Henkel:** decisão do cliente.
- ⚠️ **WT 64551 (base) e 63121/63122/63129/63801 (ausências):** to be confirmed by Development. Não dá para validar no DZ-WTC-001-v1.0, que não tem códigos Mercans.
- ⚠️ **Prazo:** 30 × 31 de janeiro. Falta comunicado ou arrêté da CNAS.
- ⚠️ **Arts. 14 e 16:** alterações posteriores à Loi 04-17 (leis de finanças, Loi 08-08) não verificadas.
- ⚠️ **`DD: Payroll.ReferenceYear`** (DAS Spec L6/L20): não existe no DZ-DD-001-v1.1 e não foi tratado (fora dos 6 nomes pedidos). Decidir se entra numa v2.3 ou no pedido de DD v1.2.
- ⚠️ **NEW DD FIELD (proposed)** a levar ao DD v1.2: Employee Establishment (CNAS employer-number assignment); Establishment Denomination; Establishment Address; DAS Duration Unit; Pay Frequency.
- ⚠️ **Version Control do DZ-DD-001-v1.1:** só registra a linha 1.0.

## Rodada 2 (achados #2–#10 da `REVISAO-independente.md`)
**Como gerar:** `build_v2_2.py` (v2.1 → r1) e depois `build_v2_2_r2.py <r1> <v2.2> <anexo D24E>` (r1 → v2.2 final). A técnica é a mesma: edição XML + zip e destaque `FFDDEBF7`.
- `changes_r2.json`: antes da rodada 2 → depois.
- `changes_manifest.json`: consolidado v2.1 → final.

**Arquivo final:** [[Research Pipeline/Algeria/2026-10-27-HRBS-3466-DAS-v2.2/DZ-CNAS-DAS-CountryStandard-Spec_v2.2.xlsx|DZ-CNAS-DAS-CountryStandard-Spec_v2.2.xlsx]], md5 `88273b04328d37734e77292c525ca06c`. Substitui o `3c22c5eb…` da rodada 1.

| # | Células | Antes (r1) → depois |
|---|---|---|
| 2 | DAS Spec L6, L20 | `DD: Payroll.ReferenceYear` → "Run parameter (reference year, CCYY) - not a DD field" |
| 3 | DAS Spec L4, L7, L9, L10, L19, L22, L23, L24, L25, L39, L40, L41 (12) | `DD: X.Y` → `DD: X.Y - Field Name '<nome real>' (DZ-DD-001-v1.1, <aba>)`. Os nomes reais são: Employer CNAS Contributor Number, Employer CNAS Paying Centre e Employee CNAS Social Security Number (aba ID Information); Employer Legal Name, Employer Head-Office Address, Surname, First Name, Date of Birth, Date of Hire, Date of Termination e Job Title / Occupation (aba Country Fields). Conferi os nomes no [[raw/docs/drive-exports/2026-10-27/DZ-DD-001-v1.1.xlsx\|DZ-DD-001-v1.1.xlsx]]. |
| 4 | DAS Spec L26, L29, L32, L35; M27, M30, M33, M36 (8) | Saíram "e.g. Henkel", a convenção 90 e os WTs de ausência. Ficou a regra genérica: J = DIAS 0–92, com a convenção de dias do cliente e as ausências registradas no anexo do cliente; unidade = parâmetro do cliente. A convenção e os WTs continuam na aba Henkel (B11). L28/L31/L34/L37 (WT 64551, "to be confirmed by Development") **ficaram**: é regra do país, sem nome de cliente, como o coordenador permitiu. Resultado: nenhuma célula fora da aba Henkel cita "Henkel", salvo Version Control B5/D15 (o aviso do anexo e o registro da versão). |
| 5 | Evidence Register D9; Field Options F7, F8, F9 | "Unit derived from pay frequency" / "Use when pay frequency is …" → "Selected through the client-level DAS unit parameter", com a referência ao guia p.36 de cada código. |
| 6 | Report Matrix B28 | "… the M/J/H unit rule, the deadline and … taken verbatim from the guide" → o prazo saiu da lista do guia, e a frase nova diz que a fonte é a Loi 83-14 art. 14 (30 dias; ⚠️ 31/01 não confirmado). O resto do texto ficou igual. |
| 7 | Sample File A10, A11, A12, A13 | As últimas 20 posições (Observation: CADRE / TECHNICIEN / OUVRIER / AGENT) → 20 espaços. Cada registro continua com 194 posições, e as somas não mudam. Fiz as 4 linhas, e não só a A10, para a amostra inteira seguir o default. |
| 8 | Henkel C5, D5, E5, F5 | TO BE CONFIRMED BY CLIENT → valores lidos nas posições 16–130 do entête aceito `D24E1638091858` (dados da empresa), cada um com "(from accepted DAS 2024 header; client to confirm)": centre `11628`; Dénomination `HENKEL ALGERIE SPA`; Raison sociale `PROD DETERGENTS,PROD NETTOYAGE`, com a nota de que o campo trazia a atividade e não a razão social; Adresse `N779 PROP MED ZAOUI G VENTS 01 DELY IBRAHIM  ALGER`. |
| 9 | Population Rules D28 | A → B |
| 10 | DAS Spec I3, I18 | 17 → 18 (`D26E0555775111.TXT` tem 18 caracteres) |

**Não feitos (por instrução):**
- #1 é dependência externa.
- #12 e #13 são cosméticos; o azul de destaque fica.
- #11 fica anotado para o **DD v1.2**: o formato do nº CNAS no DD é "N10 + clé" (ID Information J12), contra N(10) na spec e "10 positions" no guia p.35.

**Conferência da rodada 2:**
- Comparação v2.1 × v2.2 final, célula a célula: **154 células diferentes**, todas no manifesto. Nenhuma ficou fora, nenhuma ficou sem destaque azul, **0 falhas**. Na rodada 2 mudaram 38 células.
- Por aba: VC 7 · RM 6 · ER 2 · DAS Spec 48 · FS 5 · Field Options 3 · PR 19 · VR 7 · EA 2 · Sample File 4 · Henkel 51. Só as abas Change Log e Payroll Scope Summary ficaram intactas.
- O XML de todas as partes passa no parser, e o `testzip` deu OK.
- O Excel (COM, só leitura) abriu as 13 abas: I3 = 18 e L6 = run parameter.
- O validador do toolkit caiu de 31 para 23 BLOCKERs C29. Todos são o "TO BE CONFIRMED" esperado: DAS Spec L28/31/34/37 e a aba Henkel.

## Histórico de alterações
| Data | Frente | O quê |
|---|---|---|
| 2026-10-27 | Suporte (agente construtor) | Gerou a v2.2 (Draft) a partir da v2.1 com as 11 mudanças C1–C11 e a aba Henkel Configuration. Conferência célula a célula: 135 diferenças, todas no manifesto. Local; nada foi para o Drive/YouTrack. |
| 2026-10-27 | Suporte (agente construtor), rodada 2 | Corrigiu os achados #2–#10 da revisão independente (38 células). v2.1 × final: 154 diferenças, todas no manifesto, 0 falhas. Novo md5 `88273b04…`. #11 anotado para o DD v1.2. |

## Arquivos da entrega
- [[Research Pipeline/Algeria/2026-10-27-HRBS-3466-DAS-v2.2/REVISAO-independente|REVISAO-independente]]: Revisão independente (FAIL) da spec DAS v2.2 do HRBS-3466: diff próprio de 131 células, 1 BLOCKER, 3 MAJOR, 9 MINOR.

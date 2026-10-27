# HRBS-3466: Argélia / Henkel: relatório DAS da CNAS (dz-das / dz-das-header)

> Análise só leitura, feita em 2026-10-23 pela janela Suporte. Nada foi postado, enviado ou alterado no Drive. Não há dados pessoais de empregados nesta nota: os arquivos anexos foram analisados só pela estrutura (posições, comprimentos, separadores, somas).

## Metadados
| Campo | Valor |
|---|---|
| Ticket | [HRBS-3466](https://youtrack.hrblizz.dev/issue/HRBS-3466): "Algeria DAS report creation" (origem: HRBS-191 / FD#49165) |
| Cliente / país | Henkel / Argélia (DZ) |
| Report codes | `dz-das` (detalhe/salariés) e `dz-das-header` (entête/employeur) |
| Reporter | Vaishali Venkataramani |
| Estado | SLA Exempt, Medium, Service Request. Assignee: wgomes desde 22/10 (antes: Shruti/skamble, que recebeu da Manju em 16/09) |
| Prazo do cliente | Relatório necessário até o fim de dez/2026 (Vaishali, 07/10/2026), para a DAS de 2026, a ser entregue em jan/2027 |
| Cópia do ticket | `raw/tickets/api/2026-10-23-ex-skamble/HRBS-3466.md`; anexos em `raw/tickets/api/anexos/HRBS-3466/` |
| Tickets relacionados (não lidos) | HRBS-11592 "Henkel Algeria - Issue in Social security base - urgent" (Pending on reporter, 16/10); CT-3940 "DZ: Configure reports at country level for Algeria" (fonte: `scripts/youtrack_indice.md`) |

## O que foi pedido a nós
O último comentário que nos cabe é o da **Crina (09/07/2026): "please provide the specification for this new report"**, pedido à Manju, que passou para a Shruti em 16/09 e agora está conosco. Depois disso, a Vaishali (07/10) só pede status ("will require to share this report by end of Dec 2026").

Ou seja, o que nos pedem é **a especificação (spec + mapeamento/DD) para o time de desenvolvimento refazer o relatório**, cobrindo:
- os 3 pedidos do cliente (descrição, 25/12/2025):
  - (C1) um DAS por local (DelyIbrahim, Reghaia, Chelghoum Laid);
  - (C2) 2 arquivos por local (empregados + entidade);
  - (C3) nome `D` + `E`/`S` + ano + nº CNAS;
- as 4 correções da Vaishali (31/12/2025):
  - (V1) os dois relatórios gerados por local;
  - (V2) "Employer No." não aparece;
  - (V3) "Observation" (posição do empregado) não é necessária;
  - (V4) a data de nascimento aparece grudada com as horas trabalhadas.

O Mohit (31/12/2025) disse que o relatório "is not yet configured properly. The Specification never came for mapping", e pediu também o **Data Dictionary**. A Katrin (26/02/2026) devolveu o ticket a Compliance por falta de documentação.

## Histórico do ticket
| Data | Quem | O quê |
|---|---|---|
| 2025-12-25 | Vaishali | Abre o ticket com C1–C3 e anexa os arquivos D24E/D24S, que são os arquivos submetidos no ano anterior (DAS 2024) |
| 2025-12-29 | Sohail | Diz que o relatório foi criado por Compliance e configurado pelo "brenet" |
| 2025-12-31 | Vaishali | Pede ETA |
| 2025-12-31 | Mohit | Diz que o relatório nunca recebeu spec para mapeamento e precisa ser desenvolvido de novo. Passa para Research e pede o DD da Argélia |
| 2025-12-31 | Vaishali | Lista V1–V4 com print (`image.png`) |
| 2026-01-05/12 | Vaishali | Cobra por ser declaração estatutária. Mohit marca uma reunião |
| 2026-01-06 | Manju | Pergunta ao Mohit se há ação de Research |
| 2026-02-12 | Vaishali | Conta que a DAS de 2025 foi submetida com base no relatório do sistema "with some manual changes" e que o relatório precisa ser revisto para 2026 |
| 2026-02-26 | Katrin | Devolve a Compliance: "we don't have report documentation" |
| 2026-07-09 | Crina | Pede a spec à Manju |
| 2026-09-16 | Manju → Shruti | Atribuição (`rascunhos/2026-10-22-triagem-tickets-enaakshi-shruti.md`) |
| 2026-10-07 | Vaishali | Pede update: prazo fim de dez/2026 |
| 2026-10-22 | — | Atribuído a wgomes |

## Layout oficial (fonte primária)
**Fonte primária do formato:** *Guide de Télédéclaration* da CNAS, servido pelo próprio portal em `https://teledeclaration.cnas.dz/pdf/Guide%20TELE-DECLARATION.pdf`. Baixei hoje: 66 p., SHA-256 `1b37da0c1fa6cef00e07c304bd2069bce06dfcbaaf0ef10595d0cc5f80338020`, **idêntico byte a byte** à cópia do Drive (`12- Country Report Codes\DAS file\Social Security Reports Guide TELE-DECLARATION.pdf`) e ao hash que a spec v2.1 registra. Cópia local: `raw/docs/oficiais/DZ/2026-10-23-CNAS-guide-teledeclaration.pdf`. O PDF não tem data, e a CNAS não publica XSD nem cahier des charges à parte.

**Canal (p.33–34, fig. 4.1–4.2):** menu D.A.S do portal. O empregador sobe juntos o arquivo **"Entête" (Employeur)** e o arquivo **"Détail" (Salariés)**.

**Nome dos arquivos (p.35–36):**
- Entête: `D20E0555775111.TXT`, "où 20 est l'année de la DAS à déclarer ; E pour un fichier entête ; … Numéro du Cotisant sur 10 positions ; TXT le format".
- Détail: `D20S0555775111.TXT`, com "S pour un fichier détail (salariés)".
- Logo, `D` + ano em 2 dígitos + `E`/`S` + nº cotisant (10) + `.TXT`. Isso confirma o C3. Os anexos do cliente seguem essa regra (`D24E1638091858`, `D24S1638091858`), mas com extensão em minúsculas (`.txt`), e foram aceitos.

**Entête (p.35):** 13 campos, total de 216 posições.

| # | Campo | Tipo | Tam. | Posição |
|---|---|---|---|---|
| 1 | N° Employeur | Num | 10 | 1–10 |
| 2 | Type de déclaration (N normale / C complémentaire) | Alpha | 1 | 11 |
| 3 | Année Réf | Num | 4 | 12–15 |
| 4 | Centre Payeur | Num | 5 | 16–20 |
| 5 | Dénomination | Alpha | 30 | 21–50 |
| 6 | Nom ou Raison Sociale | Alpha | 30 | 51–80 |
| 7 | Adresse | AlphaNum | 50 | 81–130 |
| 8–11 | Montant Total Trimestre 1..4 | Num | 4×16 | 131–194 |
| 12 | Total Annuel des Salaires | Num | 16 | 195–210 |
| 13 | Nombre Total des travailleurs | Num | 6 | 211–216 |

**Détail (p.36–37):** 23 campos, total de 194 posições.

| # | Campo | Tipo | Tam. | Posição |
|---|---|---|---|---|
| 1 | N° Employeur | Num | 10 | 1–10 |
| 2 | Année Réf | Num | 4 | 11–14 |
| 3 | N° Ligne | Num | 6 | 15–20 |
| 4 | N° Immatriculation + Clé | Num | 12 | 21–32 |
| 5–6 | Nom / Prénom | Alpha | 25+25 | 33–82 |
| 7 | Date de Naissance | jjmmaaaa | 8 | 83–90 |
| 8–10 | T1: Durée (3) + Unité (1) + Salaire (10) | Num/Alpha/Num | 14 | 91–104 |
| 11–13 | T2 (idem) | | 14 | 105–118 |
| 14–16 | T3 (idem) | | 14 | 119–132 |
| 17–19 | T4 (idem) | | 14 | 133–146 |
| 20 | Montant Annuel des Salaires | Num | 12 | 147–158 |
| 21 | Date Entrée | jjmmaaaa | 8 | 159–166 |
| 22 | Date Sortie | jjmmaaaa | 8 | 167–174 |
| 23 | Observation | AlphaNum | 20 | 175–194 |

**Regras do guia (observações da p.36):**
- Unidade da duração: **M** para mensalistas, **J** para diaristas, **H** para horistas.
- "Dans la mesure du possible, indiquez dans la colonne observation la fonction du salarié." O campo é recomendação, não obrigação, e por isso **o V3 é atendível**: deixar 20 espaços.
- "Tous les montants devront être déclarés **en centimes** sans le séparateur décimal."
- "Les fichiers texte ne devront en aucun cas avoir de **séparateur de rubriques** mais il faudra respecter les tailles et le format." A p.41 lista "Présence d'un caractère de tabulation" como erro sintático.
- O guia **não define** alinhamento nem preenchimento (esquerda/direita, espaço/zero), nem terminador de linha.

**Controles do portal (p.41–42):**
- Sintáticos: nº e chave do cotisant, tipo, ano, centro, formatos de montante, data e duração, unidade, "Nombre de mois/jours incorrect".
- Semânticos: entête × détail (efetivo e totais por trimestre), cada trimestre contra a DAC, nome/prénom/data de nascimento contra o cadastro.

**Obrigação legal:** Loi n° 83-14 du 2 juillet 1983, JORADP n° 28 de 05/07/1983, p.1217–1218. Cópia: `raw/docs/oficiais/DZ/2026-10-23-JORADP-1983-028-Loi-83-14.pdf`; o PDF é escaneado e eu li a imagem das p.21–22 do arquivo.
- **Art. 14** (Titre IV "Déclaration des salaires"): "Tout employeur est tenu d'adresser, **dans les trente (30) jours qui suivent la fin de chaque année civile**, à l'organisme compétent de sécurité sociale, une déclaration nominative de salaires et de salariés, faisant ressortir les rémunérations perçues entre le premier et le dernier jour, **par trimestre**, ainsi que le montant des cotisations dues." O alinéa 2 permite mudar a periodicidade por via regulamentar.
  - Lida ao pé da letra, a regra dá **30 de janeiro**. CCG, spec v2.1 e imprensa dizem **31 de janeiro**. A notícia da Radio Algérie sobre a DAS 2025 fala em "du 1er au 31 janvier 2026", mas é fonte secundária e não consegui abri-la (URL rejeitada). ⚠️ Não achei texto regulamentar que fixe 31/01; cnas.dz não respondeu hoje. Recomendação: tratar como prazo **30/01**, o mais conservador, ou confirmar o comunicado da CNAS.
- **Art. 16, redação da Loi n° 04-17 du 10 novembre 2004** (JORADP n° 72 de 13/11/2004, art. 11; cópia em `raw/docs/oficiais/DZ/2026-10-23-JORADP-2004-072-Loi-04-17.pdf`): a falta da declaração de salários "entraîne une pénalité égale à **15 %** du montant des cotisations dues. Cette pénalité est majorée de **5 % par mois** de retard".
  - O **art. 16 bis** (art. 12 da 04-17) acrescenta 1.000 DA por trabalhador omitido ou por inexatidão.
  - A 04-17 não altera o art. 14.
  - ⚠️ Não verifiquei se leis posteriores (LF, Loi 08-08) mudaram de novo os art. 14 e 16.

**Uma DAS por nº de empregador (justificativa do C1/V1):**
- (a) Pelo formato (guia p.35–36): cada arquivo traz um único `N° Employeur` no nome e em todos os registros, e a p.41 rejeita "Numéro cotisant (employeur) erroné".
- (b) A p.14 do guia trata como movimento (EMS) "tout changement du **numéro employeur** dont le salarié est rattaché". Logo, o empregado fica vinculado a um nº de empregador e pode mudar de um para outro.
- (c) Loi 83-14, art. 6 e art. 21: as declarações vão ao "organisme de sécurité sociale **territorialement** compétent" ou "dont il relève territorialement".
- Conclusão: há um par E+S **por nº de empregador CNAS**. Se cada local da Henkel tem nº CNAS próprio, isso dá um DAS por local.
- ⚠️ Nenhuma fonte primária diz literalmente "1 DAS par établissement". E **não está provado que os 3 locais da Henkel tenham nº CNAS distintos**: o pedido do cliente indica que sim ("CNSSnumber" por local), mas os números não estão no ticket.

## Estrutura dos arquivos anexos
Fiz a análise mecânica com Python (`-I`) sobre `raw/tickets/api/anexos/HRBS-3466/`, mascarando o conteúdo. São os arquivos **submetidos e aceitos** da DAS 2024.

**`D24E1638091858.txt` (entête):**
- 216 bytes, 1 registro, sem terminador de linha, ASCII.
- Bate **campo a campo** com a p.35: nº 10 | `N` | `2024` | centro 5 díg. | Dénomination 30 | Raison sociale 30 | Adresse 50 (endereço de **Dely Ibrahim**) | T1–T4 e total com 16 posições cada | efetivo 6 (`80`).
- Números alinhados à **esquerda e completados com espaços**, sem zeros à esquerda.
- O campo 6 traz a **atividade** com vírgula, não a razão social, e mesmo assim foi aceito.

**`D24S1638091858.txt` (détail):**
- 80 registros com CRLF entre eles (79 CRLF, sem CRLF no fim), ASCII.
- **195 posições** por registro: as 194 do guia mais um `0` constante na posição 195, em todos os registros.
- Posições 1–194 batem com a p.36–37:
  - nº empregador igual ao do entête;
  - ano `2024`;
  - N° Ligne 1..80 alinhado à esquerda;
  - nº de segurado com 12 dígitos;
  - nome e prénom com 25 posições;
  - nascimento `jjmmaaaa` (todas datas válidas);
  - por trimestre, duração em 3 posições à esquerda (`90 `, `0  `, `30 `…), unidade **`J` em 100% dos registros** e salário em 10 posições à esquerda;
  - anual em 12 posições;
  - entrada sempre preenchida, saída preenchida em 5 registros (o resto são 8 espaços);
  - **Observation em branco** (20 espaços) nos 80.
- Duração máxima 90, ou seja, convenção de 30 dias por mês.

**Conferências aritméticas no arquivo aceito:**
- Efetivo 80 = 80 registros. T1, T2 e T4 do entête = soma do détail. Total anual = soma dos anuais.
- **T3 do entête difere da soma do détail em 1 cêntimo**, e **1 registro tem anual ≠ T1+T2+T3+T4 (1 cêntimo)**. Mesmo assim o arquivo foi aceito.
- **9 trimestres com duração e salário descasados:**
  - 7 com duração > 0 e salário 0 (empregados ativos);
  - 2 com duração 0 e salário > 0 (desligados).
- Montantes com cêntimos diferentes de zero, o que é coerente com a regra "en centimes".

**Print da Vaishali (`image.png`, saída do produto de 2025):** confirma 3 problemas.
- **V2 confirmado:** o registro do empregado começa **em branco nas posições do N° Employeur**, seguido de `2025` + nº de linha.
- **V3 confirmado:** a Observation sai com o cargo (texto do tipo "Material Mgmt Forkli…", truncado em 20).
- **V4, "data grudada":** depois do prénom aparece `jjmmaaaa` seguido de `143J`, ou seja, data de nascimento (8) + **duração T1 = 143** + unidade `J`.
  - Pelo guia, o layout é de largura fixa **sem separador**, então a data "grudar" na duração é o **formato correto**. Em `90 J` só parece haver espaço porque a duração tem 2 dígitos e o restante do campo é espaço. A spec v2.1 mostra o mesmo efeito na amostra (`…11121995520H…`).
  - **O defeito real é o valor:** 143 dias num trimestre é impossível (máximo 92; na convenção do cliente, 90). Isso cai em "Nombre de jours incorrect" (p.42). A spec de abril chama o campo de "Working Hours" e o exemplo dela é `160`, então o produto provavelmente põe **horas** (ou outra contagem) com unidade `J`.
  - ⚠️ Inferência baseada numa linha só do print. Confirmar com a saída completa do produto.

**Cópias com o mesmo nome no Drive (`12- Country Report Codes\DAS file\D24E…/D24S…`):** não são as aceitas.
- **D24S do Drive** (22/09/2025, 15.306 bytes): 86 registros com 174/182 posições.
  - Duração alinhada à direita (` 90`).
  - **Salário trimestral com 12 posições em vez de 10**, o que desloca tudo a partir de T2.
  - Anual grudado com a data de entrada.
  - Sem Observation. Linhas vazias no fim.
- **D24E do Drive** (06/01/2026, 206 bytes): sem tipo, ano e centro (o nome começa na posição 11), **com tabulações** entre os montantes (rejeição p.41) e linhas extras.
- ⚠️ Pela estrutura, parecem saídas antigas do produto, mas não sei a procedência. Recomendo renomear ou mover essas cópias para não serem confundidas com as submetidas (decisão do usuário, porque o Drive não deve ser mexido por mim).

## Estado das nossas specs
**Três versões existem:**

| Spec | Onde | Data | Natureza |
|---|---|---|---|
| "DAS Algeria Report Specification" | Drive `DAS file\…gsheet`; export `raw/docs/drive-exports/2026-10-23/DAS Algeria Report Specification.xlsx` | v1.0 de 06/01/2025, "In Progress" (Manju); gsheet de 24/04/2026 | Spec de **mapeamento do produto** (é a que está configurada) |
| "DZ-CNAS-DAS-AnnualSalaryDeclaration-Spec" (AI) | Drive `Specs (AI)\` | v1.0 de 30/06/2026, "Final" | Spec estatutária gerada pelo pipeline (CCG Agent v2.8) |
| "DZ-CNAS-DAS-CountryStandard-Spec_v2.1" | Drive `DAS file\…gsheet` (08/10); export `raw/docs/drive-exports/2026-10-23/` | v2.1 de 17/09/2026, CURRENT | Padrão de país (provavelmente trabalho da Shruti, que pegou o ticket em 16/09) |

**Spec de abril (produto):**
- Abas Employee e Header com posições corretas (1–194 / 1–216), mas:
  - o **Header tem "?" em quase todo o mapeamento** (Employer No., tipo, centro, denominação, razão, endereço, totais), o que explica o V2;
  - Employer No. no détail diz "From Legal entity fields each location has different number saved over separate field";
  - **Observation = `POSTPAD($employee.position; 20; '')`**, que causa o V3;
  - **12 linhas "Working Hours Month 1..12" e "Salary Quarter Month 1..12" todas nas posições 91–93 / 95–104** (lixo de template), com a duração rotulada "Total hours" e exemplos 160/170/180/190, provável causa do 143J;
  - unidade "Days … need to add J";
  - salário = WT 64551; desconto de licença = WT 63121+63122+63129+63801.
- A aba "New format Specs" traz um layout **inventado** (Record Type `00`/`10`, Total Cotisations, Nationalité, LF) que não tem nada a ver com a CNAS.
- A Report Matrix descreve a **DAC** ("CNAS_DAC_MOIS") e afirma "CNAS does not accept centimes", o que **contradiz o guia p.36**.
- A aba Options é de outro país (códigos fiscais da Indonésia).
- **Não serve para entregar.**

**Spec AI v1.0:**
- Layout fiel ao guia.
- Erros: exemplos com zeros à esquerda (`000001`, `000022`, `003M00270…`), o que contradiz o arquivo aceito; Date Sortie `00000000`; Encoding "N/A — keyed online form", errado.
- Não tem regra por local.

**Spec v2.1 (CountryStandard):** é a mais completa e a única próxima de entregável.
- **Certo, conferido por mim contra o guia e os anexos:**
  - os 36 campos, posições e tamanhos (entête 216 / détail 194);
  - nome `D{YY}E|S{cotisant10}.TXT`;
  - cêntimos; sem separador nem tab;
  - alinhamento à esquerda com espaços (tier B, observado no arquivo aceito);
  - Date Sortie = 8 espaços;
  - CRLF no détail e nenhum terminador no entête;
  - 195ª posição tratada como artefato e excluída;
  - **regra "one file pair per CNAS employer number"** (Report Matrix B21, File Structure, STR-05);
  - Observation **opcional** ("May be left blank");
  - amostra que bate: rodei os 4 registros com 194 posições, o entête com 216, e as somas T1–T4, anual e efetivo conferem.
  - Hash do guia confere.
- **Cobertura dos pedidos:**

| Pedido | v2.1 cobre? | Observação |
|---|---|---|
| C1/V1 por local | **Parcial** | Diz "1 par por nº CNAS", mas **não define a chave de agrupamento** (empregado → local/estabelecimento → nº CNAS, centro e endereço), nem a regra para quem muda de local no ano |
| C2 2 arquivos | Sim | Entête + détail |
| C3 nome do arquivo | Sim | `D{YY}E/S{cotisant10}.TXT`; aceita-se `.txt` minúsculo, como nos anexos |
| V2 Employer No. | **Parcial** | Mapeia "DD: Employer.CNASNumber", mas o DD (DZ-DD-001 v1.1) tem esse campo "constant per establishment" **sem vínculo do empregado ao estabelecimento**; e o produto guarda o nº "over separate field" por local (spec de abril) |
| V3 sem Observation | **Parcial** | Opcional, mas o System Mapping continua "DD: Employee.JobTitle" e o exemplo traz "CADRE". Para a Henkel precisa ser explícito: **20 espaços** |
| V4 data grudada | **Parcial** | O layout e a amostra estão certos. Falta escrever, para o dev, que a ausência de separador é correta e que a duração deve ser 0–92 em dias (ou meses/horas conforme a unidade), não horas com `J` |

- **Defeitos e lacunas da v2.1:**
  1. **Mapeamentos que não existem no DD v1.1:** `Employer.Denomination`, `Employer.RegisteredAddress` (o DD tem só `Employer.Address` = sede), `Employer.CNASPayingCentre` (no DD é `Employer.CNASCentre`), `Employee.SocialSecurityNumber` (no DD é `Employee.SSNumber`), `Employee.PayFrequency` (ausente), `Payroll.ContributoryBase Qn` (não é campo de DD). Não há **nenhum campo de estabelecimento/local de trabalho** no DD.
  2. **Wage types:** a v2.1 não aponta qual resultado do produto é a base CNAS trimestral nem quais WTs reduzem a duração. A spec de abril usa WT 64551 e 63121/63122/63129/63801, mas o **DZ-WTC-001-v1.0 não tem coluna de código Mercans preenchida**, então não há como validar esses códigos no nosso WTC.
  3. **Unidade:** a v2.1 exige M para mensalistas (guia p.36, correto). Mas o arquivo aceito da Henkel usa **J/90 para todos**. Mudar para M/3 altera o histórico de períodos de seguro do cliente. Isso é **decisão do cliente/Vaishali**, e a spec precisa de um parâmetro por cliente.
  4. **SEM-02 / regra de pareamento duração↔salário (BLOCK, "tier A"):** o guia **não traz** essa regra, e o arquivo aceito a viola 9 vezes (7 duração>0/salário 0; 2 duração 0/salário>0). Rebaixar para WARN/tier B, ou definir o tratamento (licença sem vencimento, pagamento após saída).
  5. **SYN-05 / STR-06** (só letras e espaços nos campos Alpha): o arquivo aceito tem vírgula no campo 6. Manter como saneamento é ok, mas não chamar de rejeição comprovada.
  6. **Prazo e penalidade:** v2.1 diz 31/01 "art. 14" e "15% + 2%/mês". Pela lei, o art. 14 diz "30 jours qui suivent la fin de chaque année civile" e o art. 16 (redação da 04-17) diz **15% + 5% por mês**, mais 1.000 DA por omissão ou inexatidão (art. 16 bis).
  7. **Células com erro:** Example Analysis D10 e D17 começam com "=" e viram fórmula (`#ERROR!` na exportação).
  8. Aba "Change Log vs Pipeline" cita "pipeline specification v1.1", mas a do Drive (AI) é v1.0. Divergência de numeração.
  9. Formato "house" ok, mas o pedido do Mohit (DD) segue sem resposta. A spec é **padrão de país**, e de propósito "no client, legal-entity or site-specific content". Falta o **anexo de configuração Henkel**: 3 nºs CNAS, centros, denominação/raison sociale/endereço por local, unidade, Observation em branco, população por local.

## Veredito
**A v2.1 está correta no layout estatutário, mas não está pronta para entregar ao dev/Reports.** Ela resolve C2, C3 e a base de V2–V4, porém deixa sem definição justamente o que o cliente pediu de novo, que é a geração por local, e mapeia campos que não existem no nosso DD. A spec de abril (a que o produto usa) e a AI não servem como base.

**O que falta, exatamente:**
1. **Regra de geração por local**: definir a chave empregado → local/estabelecimento → nº CNAS (10), centro payeur (5), Dénomination, Raison sociale e endereço do estabelecimento. Gerar um par E+S por nº CNAS distinto na população do ano. Definir a regra para transferência entre locais no ano (⚠️ sem fonte; proposta: cada par traz só os trimestres e salários sob aquele nº, com Date Entrée e Date Sortie do vínculo ao nº, coerente com o EMS da p.14) e a numeração `N° Ligne` reiniciada por arquivo.
2. **Nome do arquivo**: `D` + YY + `E`/`S` + nº CNAS do local + `.TXT`, com o mesmo nº nos registros (STR-01).
3. **Mapeamento para campos reais do produto/DD** (substituir os 6 nomes inexistentes) e acrescentar ao DD: "Employee Establishment / CNAS employer number assignment", "Establishment address", "Pay frequency / DAS unit".
4. **Base trimestral e duração**: indicar o resultado/WT do produto da base CNAS por trimestre (validar 64551 com o dev) e a fórmula da duração em **dias, 0–92** (convenção atual da Henkel: 90 por trimestre menos ausências não remuneradas), com a lista de WTs de ausência validada. Isso substitui "Working Hours".
5. **Observation**: para a Henkel, 20 espaços (V3). Na spec país, mapping "blank by default".
6. **Unidade**: parâmetro por cliente. Henkel = `J` (histórico aceito) ou `M` (guia), conforme a Vaishali confirmar.
7. Corrigir os itens 4, 6 e 7 dos defeitos acima (pareamento, prazo/penalidade, células `#ERROR!`).
8. Validador pré-envio (já descrito na v2.1: ARI-01…04) obrigatório na saída. O arquivo aceito tinha quebra de 1 cêntimo que o portal não pegou.

## Achados fora do pedido
(Vão para o hub `paises/Argelia.md`, que ainda não existe, e não para o ticket.)
- **CCG DZ-CCG-001-v1.0** diz "Contribution bases and amounts on CNAS declarations are reported in **dinars**" (seção de arredondamento; linha "Monetary fields on the G50, G29, DAC and DAS…"). Isso contradiz o guia CNAS p.36, que diz cêntimos.
- O CCG e a v2.1 dão o prazo da DAS como 31/01, enquanto a Loi 83-14 art. 14 diz 30 dias após o fim do ano civil. Confirmar com comunicado oficial.
- A v2.1 traz penalidade "15% + 2%/mês", mas a Loi 04-17 art. 11 (novo art. 16) diz 15% + 5%/mês.
- O arquivo DAS 2024 aceito tem quebra de 1 cêntimo no T3 do entête e em 1 registro anual. O portal não rejeitou. A DAS 2025 foi "submitted… with some manual changes" (Vaishali, 12/02). Pode haver divergência DAS × DAC a regularizar com declaração `C`. Não sabemos.
- Cópias "D24E/D24S" no Drive com estrutura diferente das submetidas (tabs, salário com 12 posições): risco de alguém usá-las como referência.
- A spec de abril tem a aba Options de outro país (Indonésia) e a Report Matrix da DAC. Precisa ser arquivada ou marcada como obsoleta quando a nova for entregue.
- O DZ-WTC-001-v1.0 está sem código Mercans em todas as linhas: nenhum relatório DZ consegue citar WT pelo nosso WTC.
- HRBS-11592 (Henkel Argélia, "Issue in Social security base - urgent") afeta diretamente os montantes da DAS. Ler antes de fechar o mapeamento da base.

## Rascunho de resposta (EN)
> Para comentário no HRBS-3466. **Não postado.** Apresentar ao usuário antes.

```
Hi @vvenkataramani @mjain,

This ticket is now with me. Status and plan:

1. We are finalising the DAS specification (header "E" file + employee "S" file) against the CNAS télédéclaration guide. It will cover:
   - one E/S file pair per CNAS employer number (i.e. per location: Dely Ibrahim, Reghaia, Chelghoum Laid);
   - file names D + YY + E/S + 10-digit CNAS employer number (e.g. D26E1638091858.TXT / D26S1638091858.TXT);
   - Employer No. populated on every record;
   - Observation left blank;
   - quarterly duration limited to days worked (0-92, unit J), which fixes the "143J" value after the date of birth. The layout has no separators, so the date of birth is always followed directly by the Q1 duration.

2. To complete the Henkel mapping, please confirm for each of the 3 locations:
   - CNAS employer number;
   - paying centre code (centre payeur);
   - denomination and address as registered with CNAS;
   - which employees belong to each location.
   Please also confirm that unit "J" (days, 90 per full quarter) should stay as in the 2024 file.

3. Proposed ETA: specification to Development by 06-Nov-2026 (subject to the data above), development and test files from Development by 04-Dec-2026, and UAT with Henkel by 15-Dec-2026, ready for the DAS 2026 filing (due January 2027).

Kind regards,
Wallisson
```

## O que precisa ser feito
| # | Passo | Quem | Data proposta |
|---|---|---|---|
| 1 | Validar esta análise e o rascunho; decidir se o ETA é esse | Usuário | 24–27/10 |
| 2 | Postar o comentário (draft) e pedir os dados dos 3 locais e a decisão J × M | Usuário (Suporte) / Vaishali responde | 27/10 → resposta até 31/10 |
| 3 | Ler HRBS-11592 (base CNAS da Henkel) e CT-3940 | Janela Suporte | 27/10 |
| 4 | Gerar a **v2.2** da spec país a partir da v2.1: regra por estabelecimento, mapeamentos para campos reais, duração em dias, Observation em branco por default, pareamento como WARN, prazo/penalidade com a Loi 04-17, células `#ERROR!`. Mais o **anexo de configuração Henkel** (3 locais) | Nós (pipeline/suporte) | até 06/11 |
| 5 | DD: acrescentar campos de estabelecimento (nº CNAS, centro, endereço) por empregado e "pay frequency/unit" (DZ-DD-001 v1.2) | Nós | até 06/11 |
| 6 | Confirmar com o dev o resultado/WT da base CNAS trimestral (64551?) e os WTs de ausência | Mohit / dev | até 06/11 |
| 7 | Desenvolvimento dos dois reports (`dz-das`, `dz-das-header`) por local + validação ARI-01..04 | Mohit / Reports | 06/11 → 04/12 |
| 8 | Teste: gerar com os dados de 2026 e conferir posição a posição contra a spec (nós) e contra a DAC (Henkel) | Nós + Vaishali | 04–15/12 |
| 9 | Registrar no cérebro: hub `paises/Argelia.md`, correções (CCG em dinares, prazo/penalidade da v2.1), log | Janela geral | após o ok do usuário |

## Lacunas
- ⚠️ **Os nºs CNAS, centros e endereços dos 3 locais**: não estão no ticket. Só o de Dely Ibrahim aparece (nome do anexo / entête).
- ⚠️ Se cada local da Henkel tem mesmo nº CNAS próprio: o pedido indica que sim, mas não foi provado.
- ⚠️ A regra para empregado transferido entre locais dentro do ano: sem fonte primária.
- ⚠️ Prazo exato (30 × 31 de janeiro): falta o comunicado/arrêté da CNAS. cnas.dz estava inacessível hoje e a Radio Algérie (secundária) rejeitou o acesso.
- ⚠️ Se os art. 14 e 16 da Loi 83-14 foram alterados depois da Loi 04-17: não verificado.
- ⚠️ A origem do valor "143" com unidade J: inferido de uma linha do print. Precisa da saída completa do produto de 2025 e da configuração atual.
- ⚠️ Procedência dos D24E/D24S do Drive (estrutura diferente dos anexos).
- ⚠️ Os códigos WT 64551 / 63121 / 63122 / 63129 / 63801: não validáveis no nosso WTC (sem códigos).
- ⚠️ A DAS 2025 que a Henkel submeteu ("with some manual changes"): não temos o arquivo. Seria a melhor referência atual.
- ⚠️ Se o portal aceita `.TXT` em maiúsculas e minúsculas: os anexos aceitos usam `.txt`, e o guia mostra `.TXT`.

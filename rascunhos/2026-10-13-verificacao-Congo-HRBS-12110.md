# Verificação em fonte primária: Congo (Brazzaville), afirmações do rascunho HRBS-12110

> Data: 2026-10-13. Objeto: afirmações de `rascunhos/2026-10-09-HRBS-12110-revisao-matriz-Congo.md`.
> Método: só texto oficial (Journal officiel em sgg.cg, finances.gouv.cg, portal CNSS). A skill `payroll-compliance-congo` e o CCG serviram só de pista.
> PDFs oficiais salvos em `raw/docs/oficiais/CG/` (lista no fim).
> Rascunho: nada foi enviado ao cliente e nenhuma outra nota foi alterada.

## Resumo dos vereditos

| # | Afirmação | Veredito | Base oficial |
|---|---|---|---|
| 1a | Bordereau nominativo mensal CNSS, antes do dia 15 de N+1, pelo portal e-déclaration | **PARCIAL.** O portal e a declaração nominativa mensal estão CONFIRMADOS. O prazo do dia 15 NÃO FOI CONFIRMADO em fonte oficial: só achei o Code de sécurité sociale de 1986, art. 22, em cópia não oficial, e ali são 15 dias se a empresa tem mais de 20 empregados; nos outros casos o prazo é trimestral. | edeclaration.cnss.cg; Loi 004/86, art. 22 (cópia Droit-Afrique) |
| 1b | Declaração mensal ITS + TUS (parte DGID) até o dia 15 de N+1, online (e-Taxe/SYSTAF), agregada, sem XML/XSD | **PARCIAL.** O prazo do dia 15 está CONFIRMADO (art. 461 bis do CGI, criado pela LF 2026), mas **em agosto o prazo é o dia 20**. E-Tax está CONFIRMADO. SYSTAF NÃO FOI CONFIRMADO. "Agregada" é **contraditado em parte**: o CGI, art. 177 bis, exige todo mês o *état* nominativo do art. 176 de quem emprega mais de 3 pessoas. "Sem XML" NÃO É VERIFICÁVEL em fonte oficial. | LF 2026, art. 47 (art. 461 bis do CGI), p. 71 e p. 99; CGI arts. 176/177 bis |
| 1c | DAS anual (DAS1+DAS2+DAS3) à CNSS e à DGID, prazo 31 de março | **CONTRADITO quanto ao prazo.** O texto oficial disponível do CGI (art. 176) diz "dans le courant du mois de janvier". Não achei 31 de março em nenhuma fonte oficial. A obrigação também existe na CNSS (CSS 1986, art. 23), mas a modalidade fica para um arrêté, que não encontrei. | CGI t.1 art. 176 (finances.gouv.cg); Arrêté 1560/2026 art. 3 |
| 2a | CAMU: 4,55% empregador / 2,27% empregado (Décret 2024-133) | **CONFIRMADO** | Décret 2024-133, art. 2 (JO n°20-2024) |
| 2b | Solidariedade 0,5% acima de 500.000 XAF | **CONFIRMADO, mas com outra base legal.** Não está no Décret 2024-133. É um *tributo* da LF 2021 (loi 66-2020), mantido pelo art. 42 da LFR 2021 (loi 37-2021): retenção na fonte, contencioso pelo CGI. | JO édition spéciale n°5-2021, pp. 27–28 |
| 2c | Recolhimento da CAMU pelo circuito CNSS (Décret 2024-131) | **CONTRADITO.** O Décret 2024-131 manda o empregador repassar **diretamente à CAMU**, em até **5 dias** após o fim do mês, com declaração nominativa 10 dias antes do vencimento. O decreto não menciona a CNSS. O portal da CNSS tem só os tipos "Déclaration CNSS" e "Déclaration TUS". | Décret 2024-131, arts. 4, 14, 15, 16, 21 |
| 3 | TUS de 7,5% a cargo do empregador, repartida em 5,475% CNSS / 2,025% DGID a partir de 01/01/2026 (LF 2026) | **CONFIRMADO, com a conta derivada.** A taxa de 7,5% vem da lei de criação da TUS (LFR 2012). A LF 2026 reparte 27% para o Estado (DGID) e 73% para a CNSS. 27% × 7,5% = 2,025% e 73% × 7,5% = 5,475%. A LF 2026 não escreve esses percentuais. Antes, na LF 2025, o Estado ficava com 15% + FNH 5%. | Loi 8-2012, arts. 4 e 6; LF 2026, art. 47, ponto 23 (art. 8 nouveau), p. 79; Arrêté 1560/2026, art. 2 |
| 4 | DAS3 (resumo por número de partes) criada pela LF 2026, art. 116 H–I | **CONFIRMADO, com correção.** O artigo certo é o **116 I, al. 1** (o 116 H trata da retenção). A DAS3 vale **"au titre de l'année 2025"**, ou seja, já na DAS entregue em 2026. O modelo foi fixado pelo Arrêté n°1560 de 10/07/2026. | LF 2026, art. 116 I (p. 66); JO n°30-2026, p. 834 |
| 5 | Língua oficial: francês (Constituição, artigo) | **CONFIRMADO.** Constituição de 25/10/2015, **art. 4**. | sgg.cg, Constitution |
| Conta | ITS de 279.300 = ITS **anual de um** empregado, não o total mensal de 120 | **SE SUSTENTA** (ver cálculo) | LF 2026, arts. 116, 116 A, 116 G |

---

## 1. As três declarações

### 1a. Bordereau nominativo mensal CNSS
- **Portal (CONFIRMADO).** https://edeclaration.cnss.cg/ (acesso em 2026-10-13): *« Plateforme de Déclaration Nominative des Salaires et des Cotisations Sociales »*; *« Effectuer vos Déclarations Nominative Mensuelle des Salaires et des Cotisations (DNMSC) »*; tipos de declaração: *« Déclaration CNSS »* e *« Déclaration TUS »*. **Não há tipo CAMU no portal.**
- **Prazo (NÃO CONFIRMADO em fonte oficial).** A única referência achada é o Code de sécurité sociale, Loi n°004/86 de 25/02/1986, **art. 22, 1°**, em cópia Droit-Afrique hospedada em liziba.cg. Não é fonte oficial e serve só de pista: *« Les cotisations font l'objet d'un versement par l'employeur à la Caisse dans les quinze (15) jours de chaque mois si l'employeur occupe plus de vingt (20) travailleurs et dans les (15) premiers jours de chaque trimestre dans les autres cas. »*
  - Consequência: "antes do dia 15" vale para quem tem **mais de 20 empregados**. O cliente da matriz tem 120, então está coberto. Para empresas menores, o texto de 1986 prevê recolhimento **trimestral**. Falta conferir no JO se a Loi 31-2011 ou um texto posterior mudou isso.
  - O art. 461 bis do CGI (LF 2026) vale para "impôts, droits et taxes" e não alcança contribuições sociais.

### 1b. Declaração mensal ITS + TUS (DGID)
- **Prazo do dia 15: CONFIRMADO, com exceção em agosto.** LF 2026 (loi n°42-2025), art. 47, item 13, que cria o art. 461 bis do CGI t.1 (JO éd. spéciale n°3-2026, p. 71):
  > *« Article 461 bis nouveau : Les délais d'accomplissement des obligations déclaratives et des échéances de paiement des impôts, droits et taxes sont désormais fixés au plus tard le 15 de chaque mois, sauf pour le mois d'août où le délai est avancé au 20 du mois, quel que soit le nombre effectif de jours ouvrés compris dans cet intervalle, selon le calendrier fiscal publié par l'administration fiscale. Tout délai de déclaration ou de paiement différent des dispositions ci-dessus est nul et de nul effet. »*
  - ⚠️ **Inconsistência dentro da própria LF 2026.** Na parte de execução orçamentária (p. 99) consta: *« Les contribuables remplissent leurs obligations de déclaration et de paiement des impôts, droits et taxes au plus tard le 20 de chaque mois conformément aux dispositions de l'article 461 bis du CGI, tome 1 »*. A regra codificada (art. 461 bis) diz 15. Recomendo citar o 15 e registrar a divergência.
  - Histórico: o CGI, art. 173 (redação da LF 2014, conforme o recueil UNICONGO, que não é oficial) dava **20 dias**. A lei de criação da TUS (2012, art. 7) dizia *« avant le 20 du mois suivant »*. O art. 461 bis torna nulo qualquer prazo diferente.
- **Canal E-Tax: CONFIRMADO.** LF 2026, p. 99: *« souscription de la déclaration … en ligne, sur la plateforme dédiée E-Tax »*; pagamento *« E-pay accessible via E-Tax »*. O CGI, art. 130 (LF 2026, p. 66), obriga as empresas do *régime du réel* à *« télé déclaration et au télépaiement »*.
- **SYSTAF: NÃO CONFIRMADO.** Não aparece em nenhum texto oficial consultado.
- **"Agregada": contraditado em parte.** O CGI t.1, **art. 177 bis**, diz: *« La déclaration visée à l'article 176 ci-dessus doit être souscrite chaque mois par les employeurs occupant plus de trois personnes. Cette disposition ne fait pas obstacle à la déclaration annuelle des salaires. »* O art. 176 é um *état* **por pessoa** (nome, salário, retenção, filhos, NIU). Fonte: CGI Tome I em finances.gouv.cg, edição antiga, pp. 112–113 impressas; o recueil 2023 tem a mesma redação.
  - Na lei, portanto, há uma obrigação mensal **nominativa** para quem emprega mais de 3 pessoas. Se o formulário do E-Tax é agregado, isso é prática do portal e não conseguimos ver sem login. Sugestão: tirar "agregada" da resposta ou escrever "formulário E-Tax; o CGI art. 177 bis prevê état nominativo mensal".
- **"Sem XML/XSD": NÃO VERIFICÁVEL.** Nenhum texto oficial trata de formato de arquivo. A afirmação pode ficar como constatação de prática, mas sem citar lei.

### 1c. DAS anual
- **DAS1/DAS2/DAS3 à DGID (CONFIRMADO).** Arrêté n°1560 de 10/07/2026 (JO n°30-2026, de 23/07/2026, p. 834), art. 3: *« La DAS modèle 3 est soumise aux mêmes obligations de production, de délai et de contrôle que les déclarations annuelles des salaires modèle 1 et modèle 2 prévus par le code général des impôts. »*
- **À CNSS também (CONFIRMADO em substância, só por cópia não oficial).** CSS 1986, art. 23, 1°: *« L'employeur est tenu de produire chaque année une déclaration annuelle … Cette déclaration est adressée à la Caisse selon les modalités fixées par arrêté du Ministre chargé de la Sécurité Sociale. »* Na lei é uma obrigação separada, não o "mesmo modelo" da DGID. O Arrêté 1560, art. 2, volet 2, faz a DAS3 trazer a TUS repassada à DGID e à CNSS, mas a DAS3 é entregue à DGID.
- **Prazo de 31 de março: CONTRADITO** pelo texto oficial disponível. CGI t.1, **art. 176** (redação da LF 2007): *« … sont tenus de remettre **dans le courant du mois de janvier** de chaque année à l'Inspecteur Divisionnaire des Contributions Directes et Indirectes, un état présentant, pour chacune des personnes qu'ils ont occupées au cours de l'année précédente … »*. Logo, o prazo legal é **31 de janeiro**. O 31 de março só aparece em blogs (congopaie). ⚠️ O CGI publicado em finances.gouv.cg é uma edição antiga, de por volta de 2003, posta no ar em 28/03/2021. Não achei alteração posterior do art. 176 na LF 2021, na LFR 2021, na LF 2025 nem na LF 2026. Recomendação: trocar "31 de março" por "janeiro (CGI art. 176)" ou pedir confirmação ao cliente ou à DGID.

## 2. CAMU
- **Taxas (CONFIRMADO).** Décret n°2024-133 de 27/03/2024, **art. 2** (JO n°20-2024, de 16/05/2024, p. 548):
  > *« - employeurs publics et privés : 4,55 % de la masse salariale brute ; - employés publics et privés : 2,27 % du salaire brut ; »*
  O compte rendu do Conseil des ministres de 20/03/2024 traz os mesmos números.
- **Solidariedade de 0,5% acima de 500.000 (CONFIRMADO, com outra base).** Ela **não** está no Décret 2024-133. Base legal: LF 2021 (loi n°66-2020), mantida pela LFR 2021, loi n°37-2021 de 13/08/2021, **art. 42** (JO éd. spéciale n°5-2021, de 19/08/2021, pp. 27–28):
  > *« Art. 2 : Sont soumis … : … - Les titulaires de hauts revenus pour la fraction de revenu supérieure à 500 mille francs CFA. » « Art. 4 : Le taux de la taxe est égal à 0,5% … » « Art. 5 : La taxe est recouvrée : … pour les titulaires de hauts revenus, par voie de retenue à la source par l'organe payeur qui en est le redevable légal. » « Art. 7 : Le contentieux … est régi par le code général des impôts. »*
  - É um **tributo** retido na fonte e regido pelo CGI. Isso combina com a nossa regra de recolher à DGID, e não à CNSS. A lei **não diz** se a base é mensal ou bruta; fala só em "fraction de revenu". A LF 2026 (p. 6) lista a *« Contribution de solidarité pour la couverture de l'assurance maladie »* entre as receitas destinadas ao seguro-saúde.
- **Circuito CNSS (CONTRADITO pelo Décret 2024-131).** Décret n°2024-131 de 27/03/2024 (JO n°20-2024, pp. 543–545):
  > *« Article 14 : Les employeurs sont responsables du reversement des cotisations … »* *« Article 15 : Les cotisations font l'objet d'un reversement par l'employeur à la caisse d'assurance maladie universelle dans les cinq (5) jours suivant la fin de chaque mois. »* *« Article 16 : Dans les dix (10) jours avant la date d'exigibilité, les employeurs font parvenir à la caisse d'assurance maladie universelle une déclaration nominative des salaires et des cotisations selon les imprimés définis par la caisse d'assurance maladie universelle. »* *« Article 21 : … majoration de retard de 3% … »*
  - O decreto não menciona a CNSS. Se na prática a CAMU é recolhida na guia da CNSS, isso vem de outro instrumento (convênio CAMU–CNSS, circular), que não encontrei. **Não citar o Décret 2024-131 como base do "circuito CNSS".** Isso também afeta a skill e o CCG, que afirmam "CAMU collected through the CNSS circuit".

## 3. TUS
- **7,5% sobre o bruto, devida pelo empregador (CONFIRMADO).** Loi n°8-2012 de 11/05/2012 (LFR 2012), parte "Institution de la taxe unique sur les salaires" (JO éd. spéciale n°1-2012, p. 22 do PDF):
  > *« Article 4 : Sont assujetties à la taxe unique sur les salaires, les personnes morales de droit public ou de droit privé, employant un ou plusieurs travailleurs. » « Article 6 : Le taux de la taxe unique sur les salaires est fixé à 7,5% du salaire brut. »*
- **Repartição 2026 (CONFIRMADO, com a conta derivada).** LF 2026, art. 47, ponto 23 (JO n°3-2026, p. 79):
  > *« Article 8 (nouveau) : La taxe unique sur les salaires est répartie comme suit : ETAT 27% / FIGA 10% / FONEA 23% / ACPE 10% / FNH 5% / ADPME 5% / ACPCE 5% / Université Marien NGOUABI 5% / ANIRSJ 10%. Alinéa 2 nouveau : La part revenant au budget de l'Etat est recouvrée par l'administration fiscale. Alinéa 3 nouveau : Les parts affectées au [FIGA, ACPE, FONEA, ADPME, ACPCE, ANIRSJ, université] et au fonds national de l'habitat (FNH) sont recouvrées par la Caisse Nationale de Sécurité Sociale (CNSS) comme en matière de cotisations sociales. »*
  - Conta: DGID = 27% × 7,5% = **2,025%**; CNSS = 73% × 7,5% = **5,475%**. A lei dá só as frações; os percentuais sobre o bruto são calculados por nós.
  - Na LF 2025 (loi 47-2024, art. 8, JO n°15-2024, pp. 35–36), o Estado ficava com 15% e o FNH (5%) **não** estava na lista da CNSS. A divisão 27/73 é, portanto, a da LF 2026, que vale para 2026.
  - O Arrêté 1560/2026, art. 2, volet 2, confirma que a TUS é *« reversée d'une part à l'administration fiscale (DGID) et d'autre part à l'administration sociale (CNSS) »*.

## 4. DAS3
- LF 2026, **art. 116 I**, al. 1 (JO n°3-2026, p. 66):
  > *« Article 116 I : 1. Au titre de l'année 2025, les employeurs soumis à l'obligation de produire la déclaration annuelle des salaires doivent produire une annexe dite DAS 3 suivant le modèle fixé par arrêté du ministre des finances. Cette annexe est un état récapitulatif de la DAS1 par nombre de parts des personnes imposées à l'impôt sur les traitements et salaires. »*
- O 116 H trata da retenção e do caráter liberatório; não trata da DAS3. Corrigir para "art. 116 I". A DAS3 já vale para o ano-base 2025, com entrega em 2026. O modelo veio no **Arrêté n°1560 de 10/07/2026** (JO n°30-2026, p. 834), com dois volets: por número de partes e por *ordonnateur délégué* (DGID e CNSS), com a TUS.

## 5. Língua oficial
- Constituição de 25/10/2015 (JO 2015 éd. spéciale n°8), **art. 4**, 4º parágrafo: *« La langue officielle est le français. Les langues nationales véhiculaires sont le lingala et le kituba. »* Fonte: https://www.sgg.cg/fr/journal-officiel/constitution.html

---

## Conta do ITS (base mensal 230.400 XAF; 1 parte)

Regras (LF 2026, JO n°3-2026, pp. 64–65):
- Art. 116: *« une déduction de 20% est appliquée au montant net calculé après déduction de la part salariale des cotisations sociales de retraite »*.
- Art. 116 A: *« le salaire net imposable, arrondi au millier de franc inférieur, est divisé en un certain nombre parts … L'impôt brut est égal au produit de la cotisation ainsi obtenue par le nombre de parts »*.
- Art. 116 G: *« 1 200 F CFA pour la fraction comprise entre 0 et 615 000 ; 10% … 615 001 et 1 500 000 ; 15% … 1 500 001 et 3 500 000 ; 20% … 3 500 001 et 5 000 000 ; 30% … 5 000 001 et suivant »*. 116 G.2 fala em *« impôt annuel minimum »* e 116 G.3 em *« acompte mensuel retenu à la source »*.
- A tabela é anual: o 116 G.2 diz "impôt annuel" e o 116 I.2 manda calcular *« comme en matière d'IRPP »*, que é imposto anual.

| Passo | Cálculo | XAF |
|---|---|---|
| Origem da base | 300.000 bruto − 4% PVID = 288.000; × 0,80 = 230.400 (bate com 27.648.000 ÷ 120) | 230.400/mês |
| Anualizar | 230.400 × 12 | 2.764.800 |
| Arredondar para baixo, ao milhar (116 A) | | 2.764.000 |
| Quociente (1 parte) | 2.764.000 ÷ 1 | 2.764.000 |
| Faixa 0–615.000 | fixo | 1.200 |
| Faixa 615.001–1.500.000 | 885.000 × 10% | 88.500 |
| Faixa 1.500.001–2.764.000 | 1.264.000 × 15% | 189.600 |
| **ITS anual / empregado** | 1.200 + 88.500 + 189.600 | **279.300** |
| **ITS mensal / empregado** | 279.300 ÷ 12 | **23.275** |
| **Total mensal, 120 empregados** | 23.275 × 120 | **2.793.000** |
| Total anual, 120 empregados | 279.300 × 120 | 33.516.000 |

Variante: se o arredondamento ao milhar for feito na base **mensal** (230.000 × 12 = 2.760.000), o ITS anual fica em 278.700, o mensal em 23.225 e o total mensal dos 120 em 2.787.000. A lei não diz em qual base se arredonda.

**Conclusão: a afirmação se sustenta.** 279.300 é exatamente o ITS **anual de um** empregado com essa base, idêntico ao exemplo canônico do CCG (bruto de 300.000). O total mensal certo para 120 empregados iguais é **≈ 2.793.000 XAF**, cerca de 10 vezes o valor da matriz. Isso confirma o "ITS ~10×" da nossa revisão de 13/08. Ressalva para a resposta: o ITS é progressivo e calculado por empregado, com partes individuais. Uma base agregada dividida por 120 só vale se todos tiverem o mesmo salário e 1 parte. Convém dizer isso para que o cliente não tome 2.793.000 como valor exato da folha real.

---

## O que mudar no rascunho do ticket (sugestão; não aplicado)
1. CAMU: tirar "pelo circuito CNSS (Décret 2024-131)". O decreto manda declarar e pagar à **CAMU** (5 dias após o fim do mês, declaração nominativa). Se a prática for a guia da CNSS, dizer que é prática e não citar o decreto.
2. Solidariedade de 0,5%: base legal é a **LFR 2021 (loi 37-2021), art. 42**, não o Décret 2024-133.
3. DAS: prazo legal é **janeiro (CGI art. 176)**, não 31/03. Ou então marcar o prazo como "a confirmar com a DGID".
4. DAS3: "LF 2026, art. 116 I + Arrêté n°1560/2026"; já se aplica à DAS de 2025.
5. DGID mensal: prazo dia 15 (**dia 20 em agosto**), art. 461 bis do CGI (LF 2026). Tirar "SYSTAF". Não afirmar "agregada" como regra legal (o art. 177 bis prevê état nominativo mensal). "Sem XML" só como constatação de prática.
6. CNSS: o prazo do dia 15 vale para quem tem mais de 20 empregados (CSS 1986, art. 22; não encontrei o texto oficial).

Itens que também atingem a skill e o CCG e devem ir para `correcoes.md`, se o usuário aprovar: CAMU "via CNSS" atribuído ao 2024-131; prazo da DAS de 31/03; ausência da exceção de agosto; DAS3 citada como "116 H–I".

## Fontes oficiais salvas em `raw/docs/oficiais/CG/`
| Arquivo | O que é | URL de origem |
|---|---|---|
| `congo-jo-2026-3-2.pdf` | JO éd. spéciale n°3-2026 (05/01/2026): LF 2026, loi n°42-2025 | https://sgg.cg/JO/2026/congo-jo-2026-3-2.pdf |
| `congo-jo-2026-3-4.pdf` | Mesma edição, outro arquivo do mesmo JO (o título traz "loi n°42-2025" completo) | https://sgg.cg/JO/2026/congo-jo-2026-3-4.pdf |
| `congo-jo-2026-30.pdf` | JO n°30-2026 (23/07/2026): Arrêté n°1560 (modelo DAS3) | https://sgg.cg/JO/2026/congo-jo-2026-30.pdf |
| `congo-jo-2024-20.pdf` | JO n°20-2024 (16/05/2024): Décrets 2024-131, 2024-132, 2024-133 (CAMU) | https://www.sgg.cg/JO/2024/congo-jo-2024-20.pdf |
| `congo-jo-2025-06.pdf` | JO n°6-2025: arrêté da base de cotização CAMU (independentes), aplica o art. 2 do 2024-133 | https://www.sgg.cg/JO/2025/congo-jo-2025-06.pdf |
| `compte-rendu-cmd-2024-03-20.pdf` | Compte rendu do Conseil des ministres de 20/03/2024 (taxas CAMU) | https://www.sgg.cg/ccm/compte-rendu-cmd-2024-03-20.pdf |
| `congo-jo-2021-05-sp.pdf` | JO éd. spéciale n°5-2021: LFR 2021, loi 37-2021 (art. 42, solidariedade CAMU 0,5%) | https://www.sgg.cg/JO/2021/congo-jo-2021-05-sp.pdf |
| `congo-jo-2012-01-sp.pdf` | JO éd. spéciale n°1-2012: LFR 2012, loi 8-2012 (criação da TUS a 7,5%) | https://www.sgg.cg/JO/2012/congo-jo-2012-01-sp.pdf |
| `CGI-Tome-I-finances-gouv-cg.pdf` | CGI t.1, publicado pelo Ministério das Finanças (edição antiga; arts. 173, 176, 177 bis) | https://www.finances.gouv.cg/sites/default/files/documents/CGI%20Tome%20I.pdf |
| `constitution-2015-sgg-cg.html` | Constituição de 2015 (página oficial do SGG) | https://www.sgg.cg/fr/journal-officiel/constitution.html |

Consultadas só como pista (não oficiais, não salvas): Code de sécurité sociale 1986 (cópia Droit-Afrique em liziba.cg); recueil de textos fiscais UNICONGO/Sutter & Pearce 2023; blogs congopaie e PaySpace.

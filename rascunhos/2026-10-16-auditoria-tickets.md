# Auditoria independente dos rascunhos de ticket — 2026-10-16

> Revisor: janela **Certificação** (não escreveu as respostas). Pedido da janela geral (brain-service-d7), a pedido do usuário. Só leitura: nada editado no YouTrack, nas specs nem no Drive.
> Método: último comentário dirigido a nós → afirmações atômicas → fonte primária reaberta por mim → teste mecânico (diff célula a célula, lxml × XSD) → cobertura. % = ✅ / (afirmações + itens do pedido); ⚠️ e ❌ valem 0. Sem arredondar para cima.
> Rascunhos auditados = **draftComments atuais no YouTrack**, lidos pela API (só leitura) às ~13:10 de 16/10, não a cópia em `rascunhos/`.
> Ferramentas e cópias: scratchpad desta janela (`audit/`): `xdiff.py`, `rowdiff.py`, `samplecheck.py`; specs copiadas do Drive e de Downloads com md5 conferido.

---

## SR-414 (UA, 1-ПВ mensal) — Spec v5.5

**Pedido (Lily, 16/10 08:09):** "Some fields under **Sample** sheet are missing in the **UA-1PV-001 Spec** sheet. Pls align them and **highlight your changes in a different color**."

**Arquivos:** base = export ativa `UA-1PV-001_MonthlyLabourReport_Spec (8).xlsx` (planilha de 16/10 07:40, md5 b19a1ec7); nova = Drive `…_v5.5.xlsx` (md5 **e06e6954** ✅ igual ao informado).

**Diff célula a célula (base × v5.5):**
- Version Control: só a linha 20 (5.5) acrescentada.
- Spec: linhas 5–14 sem mudança; U15/U16 "Not identified…" → `N1`/`N2`; linhas 17–42 novas (cabeçalho + 25). A Seq (col. D) e o Version Control B13/B14 passaram de 1.0 para 1 (número, formato General): não muda nada na tela.
- Sample: A2 (nota) reescrita; 10 linhas novas; nenhuma linha antiga alterada.
- Demais 8 abas: 0 diferenças.
- **Fora do pedido:** nada.

**Testes mecânicos:**
- Sample da v5.5 × XSD oficial S0301016 + common_types Держстат 14.05.2025 (lxml): **válida**.
- Cobertura: os 31 elementos da Sample têm menção na coluna U (30 com linha própria; FIRM_EDRPOU continua na linha 6).
- Ordem das linhas 30–42 = ordem do XSD (FIRM_ZIP, FIRM_OBL, FIRM_CITY, NOMER, OBL, RAY, VIK_TEL, VIK_EMAIL, KATOTTG_FACT, RUK, ZIP_FACT, OBL_FACT, CITY_FACT).

| # | Afirmação do rascunho | Fonte primária (reaberta) | |
|---|---|---|---|
| 1 | É a spec v5.5 | Drive `_v5.5.xlsx`, md5 e06e6954; Version Control linha 20 | ✅ |
| 2 | Mudanças destacadas em azul-claro | Todas as células novas/alteradas = `FFDDEBF7` (diff de preenchimento) | ✅ |
| 3 | Linhas 17–42 na aba Spec | Diff: linhas 17 (cabeçalho) a 42 | ✅ |
| 4 | Uma linha para cada elemento da Sample sem linha própria | Teste de cobertura 31/31 | ✅ |
| 5 | "the 12 DECLARHEAD elements" | Linhas 18–29: os 12 do XSD (sem SOFTWARE, que não está na Sample) | ✅ |
| 6 | + FIRM_ZIP, FIRM_CITY, NOMER, OBL, RAY, VIK_TEL, VIK_EMAIL, KATOTTG_FACT, RUK, ZIP_FACT, CITY_FACT | Linhas 30–42 | ✅ |
| 7 | FIRM_OBL e OBL_FACT obrigatórios fora de Kyiv e Sevastopol | Modelo Держстат S0301016, aba "Контролі", controles 18 e 19 ("за винятком міст зі спеціальним статусом (Київ і Севастополь)") | ✅ |
| 8 | Na ordem do XSD | XSD S0301016 | ✅ |
| 9 | Sample: + FIRM_ZIP, FIRM_CITY, ZIP_FACT, CITY_FACT, KATOTTG_FACT, OBL, RAY, RUK, VIK_TEL, VIK_EMAIL | Diff da Sample: exatamente esses 10 | ✅ |
| 10 | Fontes: controles Держстат e lista de campos técnicos, na coluna M | "Контролі" 14–20 (RUK, tel. ≥5, e-mail com @, endereços, КАТОТТГ); `tekh-polia.xlsx`: OBL e RAY "так", preenchidos do cartão da empresa; coluna M cita cada um | ✅ |
| 11 | Linhas 15–16: os elementos XML são N1 e N2 | Formulário S0301016, p. 2, "Пояснення до розділу I": N1 (ряд. 1040 ±25%), N2 (зарплата ±10%) | ✅ |
| 12 | Ponto aberto (linha 33): KVED quando NOMER = 1, a confirmar com o Держстат | Controle 2 (NOMER > 1 → N_1, N_2, KVED obrigatórios) × controle 3 (KVED ≠ 0, "обов'язкове заповнення", sem condição); nenhuma fonte trata NOMER = 1. Conflito real, declarado com honestidade | ✅ |

Conteúdo interno da spec (não está no comentário, conferido por amostragem): Format 3.1, Tabela 1 (TIN, C_DOC_TYPE "Завжди рівний 0", C_DOC_CNT, C_REG/C_RAJ pelo SPR_SSCU, PERIOD_TYPE, "Формат рррр", "ддммрррр", nenhum elemento do cabeçalho vazio exceto SOFTWARE) ✅; SPR_SSCU: м. Київ = 80, locais 361… ✅; ГУС Львів 1-ПВ (місячна) 2026, slide 5 (NOMER = 1 sem subdivisões) ✅; campos do DD V4.2 citados na coluna L (company_postal_code, company_city, director_authorized_person, dps_region_code/dps_district_code) existem na Country Fields ✅.

**Cobertura do pedido**

| Item | |
|---|---|
| Alinhar a Spec com a Sample | ✅ (31/31) |
| "Highlight your changes in a **different color**" | ⚠️ A base já tinha **13 células no mesmo azul `FFDDEBF7`** (U5–U16 e X9, das entregas de 13–15/10). A v5.5 usou o mesmo azul: a Lily não distingue o que mudou hoje do que já estava destacado, e a mudança de U15/U16 cai em células que já eram azuis. |

**% = 13/14 = 92%** (12 afirmações ✅ + 1 de 2 itens de cobertura).

**Veredito: AJUSTAR (só a cor).**
- Correção proposta: pintar as mudanças de 16/10 numa cor que não existe no arquivo (por exemplo, laranja-claro `FFFCE4D6`). A outra opção é tirar o azul antigo de U5–U16/X9. Depois, trocar "changes in light blue" no comentário pela cor nova. Há um conflito com o padrão interno (azul `FFDDEBF7`, CLAUDE.md item 7), e o pedido explícito da Lily deve prevalecer. **Decisão do usuário.**
- Ponto aberto (KVED): o rascunho é honesto e não afirma nada que não esteja provado. Isso não derruba o % das afirmações, mas a **Sample não está garantida contra o controle 3 do Держстат**: um arquivo gerado sem KVED pode ser recusado. Confiança no artefato: alta, com esse risco declarado. Falta dizer **quem** vai confirmar com o Держстат (sugestão: deixar como pendência no hub [[Ucrania]]). Pista para o hub, não para o ticket: o formulário diz, sob KVED, "код виду економічної діяльності визначається автоматично".

---

## SR-415 (UA, 1-ПВ trimestral) — Spec v1.7

**Pedido (Lily, 16/10 08:07):** igual ao SR-414, para a aba UA-1PV-002 Spec: alinhar com a Sample e "highlight your changes in a different color".

**Arquivos:** base = export ativa `UA-1PV-002_QuarterlyLabourReport_Spec (6).xlsx` (planilha de 16/10 08:14, md5 2a12a3a7; Version Control até 1.4); nova = Drive `…_v1.7.xlsx` (md5 **8702daf1** ✅).

**Diff célula a célula:** Version Control: só a linha 18 (1.7). Spec: nenhuma linha antiga alterada; linhas 31–56 novas. Sample: A2 reescrita + 8 linhas novas. Demais abas: 0. **Fora do pedido:** nada.

**Testes:** Sample × XSD S0301121 (lxml): **válida**. Cobertura: 36/36 elementos com menção na coluna U (33 com linha própria; FIRM_EDRPOU, FIRM_NAME e FIRM_KVED nas linhas existentes). Ordem das linhas 44–56 = ordem do XSD S0301121 (… OBL, RAY, VIK_TEL, VIK_EMAIL, NOMER, RUK, ZIP_FACT, OBL_FACT, CITY_FACT, KATOTTG_FACT).

| # | Afirmação do rascunho | Fonte primária (reaberta) | |
|---|---|---|---|
| 1 | É a spec v1.7 | Drive `_v1.7.xlsx`, md5 8702daf1; Version Control linha 18 | ✅ |
| 2 | Mudanças em azul-claro | Todas `FFDDEBF7` | ✅ |
| 3 | Linhas 31–56 | Diff | ✅ |
| 4 | Uma linha para cada elemento da Sample sem linha própria | Cobertura 36/36 | ✅ |
| 5 | Os 12 do DECLARHEAD | Linhas 32–43 | ✅ |
| 6 | + FIRM_ZIP, FIRM_CITY, OBL, RAY, VIK_TEL, VIK_EMAIL, NOMER, RUK, ZIP_FACT, CITY_FACT, KATOTTG_FACT | Linhas 44–56 (OBL e RAY já estavam na Sample, mas sem linha própria) | ✅ |
| 7 | FIRM_OBL e OBL_FACT obrigatórios fora de Kyiv e Sevastopol | Modelo S0301121, "Контролі" 60 e 61 | ✅ |
| 8 | Ordem do XSD | XSD S0301121 | ✅ |
| 9 | Sample: + FIRM_ZIP, FIRM_CITY, ZIP_FACT, CITY_FACT, KATOTTG_FACT, RUK, VIK_TEL, VIK_EMAIL | Diff: exatamente esses 8 (o rascunho, corretamente, não lista OBL/RAY, que já estavam) | ✅ |
| 10 | Fontes: controles Держстат, na coluna M | "Контролі" 56–62; coluna M cita cada um | ✅ |
| 11 | Ponto aberto (linha 51): N2 (KVED) quando NOMER = 1 | Erratum oficial do XSD S0301121: "Код виду економічної діяльності за КВЕД структурного підрозділу… N2"; controle 3 (NOMER > 1 → N9, N1, N2) × controle 4 (KVED ≠ 0, sem condição). Formulário p. 1: N9 = nome, N1 = atividade | ✅ |

Conteúdo interno: NOMER = 1 vem do slide 5 do ГУС Львів para o **mensal**. No trimestral, isso fecha pelo controle 2 do S0301121 (NOMER = NOMER do 1-ПВ mensal, aviso), que a linha 51 cita ✅. PERIOD_MONTH = último mês do trimestre (Format 3.1, Tabela 1) ✅.

**Cobertura:** alinhar ✅; "different color" ⚠️ (a base já tinha **24 células** da coluna U no mesmo azul).

**% = 12/13 = 92%.**

**Veredito: AJUSTAR (só a cor)**, com a mesma correção e a mesma decisão do SR-414. O ponto aberto (N2) foi tratado com honestidade; vale o mesmo risco do controle 4 na Sample.

### correcoes.md — as 3 entradas novas de 16/10 (1-ПВ)
| Entrada | Bate com a mudança? |
|---|---|
| Sample sem endereço/КАТОТТГ/contato; mensal sem OBL/RAY | ✅ A nota antiga da Sample dizia exatamente "address and contact elements are optional in the XSD and omitted"; a trimestral já tinha OBL/RAY e a mensal não; controles mensal 14–20 e trimestral 56–62 conferidos; acréscimos conferidos no diff. |
| Linhas 15–16: "Not identified…" → N1/N2 | ✅ Texto antigo de U15/U16 confere; formulário p. 2. |
| NOMER "C, só com subdivisão" → obrigatório, = 1 | ⚠️ O valor correto está provado (controle 1 + slide 5). O erro descrito estava nos rascunhos v5.3/v1.5, que foram retirados do Drive, então não consigo conferir o texto antigo. |

---

## SR-160 (UA, D1) — zero × omitir + correção da coluna 21

**Pedido (Lily, 16/10 10:56):** (1) confirmar "Y: sempre escrever, inclusive 0/0.00, nunca omitir nem tag vazia"; (2) "C: só quando a condição é atendida, senão omitir; G23 e G18 não seguem a regra; se são escritos com 0, devem ser Y?"; (3) "N: omitir quando não há valor; e se for 0, escreve ou não?"; ou uma coluna "omit if zero". Ela vai aplicar a mesma regra aos outros reports.

**Arquivos:** base = export ativa `UA-D1-001_UnifiedSocialContribution_Spec (4).xlsx` (16/10 11:56, md5 16f62c1b); nova = Drive `_v3.4.xlsx` (md5 **6f327ef9** ✅).

**Diff célula a célula:** Version Control linha 19; D1 Spec: A30, B30, G30, L30, M30, F32/G32, F33/G33; XML Sample File: as linhas de T1RXXXXG18 saem e as de T1RXXXXG24 entram (o resto só desloca). **U30 (BA Mapping) não mudou: continua `$hr.labour_book_holder_indicator::key`.** Fora do pedido: só a correção da linha 30, que é erro nosso e precisa mesmo ser comunicado.

**Testes:** Sample v3.4 × XSD J0510111 (pacote oficial j0500111, common_types da ДПС) com lxml: **válida** (a base também era). Mapeamento linha da spec → elemento na Sample: todo Y está na Sample; nenhum C sem condição aparece; LINKED_DOCS e SOFTWARE com `xsi:nil`.

| # | Afirmação do rascunho | Fonte primária (reaberta) | |
|---|---|---|---|
| 1 | Y é sempre escrito, inclusive 0 / 0.00 | Coerente com a Sample v3.4. **Mas a própria spec contradiz isso na linha 23 (T1RXXXXG14, Y):** "populate on ONE ROW ONLY… **Zero or blank on other rows**" | ⚠️ |
| 2 | C só quando a condição é atendida; senão, omitido (sem 0, sem tag vazia) | Linhas C (10, 11, 18, 21, 22, 24, 27, 34, 44, 47) coerentes com a Sample; Format da ДПС permite a ausência (ver 11) | ✅ |
| 3 | A v3.4 elimina as duas exceções | G23 → Y; G18 fora da Sample (diff) | ✅ |
| 4 | Linhas 32–33 (G23, G24) agora Y | F32/F33 C → Y | ✅ |
| 5 | Porque o formulário J0510111 define as colunas 23 e 24 como indicadores 1/0 ("1 - так, 0 - ні") | J0510111.pdf (pacote oficial v11), cabeçalhos 23 "Ознака наявності спецстажу (1 - так, 0 - ні)" e 24 "Ознака нового робочого місця (1 - так, 0 - ні)" (renderizado e lido) | ✅ |
| 6 | Linha 27 (G18) continua C | F27 = C | ✅ |
| 7 | A Sample não escreve mais G18 | Diff + contagem lxml: 0 ocorrências | ✅ |
| 8 | N: "omitted when there is no value" | **Contradiz a frase seguinte** (os dois N do D1 vão com `xsi:nil`, não omitidos). XSD: LINKED_DOCS e SOFTWARE `minOccurs="0" nillable` (as duas formas valem); Format: só eles podem ficar vazios no DECLARHEAD. A pergunta "e se for 0?" fica sem resposta | ⚠️ |
| 9 | No D1, os N são só LINKED_DOCS e SOFTWARE (cabeçalho) | Linhas 62 e 64 são as únicas com F = N | ✅ |
| 10 | Enviados com `xsi:nil="true"` | Sample (lxml: só esses dois com nil) | ✅ |
| 11 | No Format da ДПС, elemento ausente do DECLARBODY = vazio | Format (Додаток 1 do наказ 729): "Якщо елемент відсутній у тілі документа (елемента DECLARBODY), то його значення теж вважається пустим" | ✅ |
| 12 | наказ Міндоходів № 729 de 29.11.2013 | Página da ДПС: "Наказ Міндоходів від 29.11.13 № 729" | ✅ |
| 13 | O XSD J0510111 torna opcional toda coluna da tabela | T1RXXXXG5…G26 todos `minOccurs="0" nillable="true"` | ✅ |
| 14 | Linha 30 (G21) corrigida na v3.4 | A/B/G/L/M30 mudaram | ✅ |
| 15 | Coluna 21 = "Ознака основного місця роботи" (local principal, 1/0), não indicador de carteira de trabalho | J0510111.pdf, cabeçalho 21 (recorte em 300 dpi) | ✅ |

**Cobertura**

| Item | |
|---|---|
| (1) Regra Y | ⚠️ Respondida, mas a linha 23 da spec (Y) ainda diz "zero or blank": a regra que a Lily vai aplicar a todos os reports conflita com a spec |
| (2) Regra C + G23/G18 | ✅ |
| (3) Regra N + "e se for 0?" | ⚠️ Contraditória e sem a resposta do zero |
| Ponto de atenção da geral: avisar que o BA Mapping da linha 30 aponta para `labour_book_holder_indicator` | ❌ **O rascunho não avisa.** Ele diz "Row 30 is corrected", mas a coluna U (da Lily) ficou igual, e é ela quem precisa trocar o mapeamento |

**% = (13 + 1) / (15 + 4) = 14/19 = 73%.**

**Veredito: AJUSTAR.** Correções propostas:
1. Item 3 do comentário: "Optional (N): in D1 only LINKED_DOCS and SOFTWARE (header). Without a value they are sent as `xsi:nil="true"`, as in the sample; under the ДПС format they are the only header elements that may be empty. Neither carries a number, so the zero case does not arise."
2. Acrescentar ao parágrafo da linha 30: "The BA mapping in row 30 (`$hr.labour_book_holder_indicator`) refers to the labour book and needs to be revised." Escolher o campo é da Lily. Só como pista, não como prescrição: o DD V4.2 tem `labour_registry_person_category` (Country Fields linha 47, "1 = hired employee, main place of work; 2 = … concurrent job"), mas ele é da D5 e tem as categorias 4–9.
3. Spec: a linha 23 (G14, Y) diz "Zero or blank on other rows". Ou vira "0 on the other rows" ou ganha uma exceção explícita. **Antes de mudar, ler o Порядок §IV p. 23–24 citado** (eu não li). Até lá, o item 1 do comentário deve mencionar a exceção.

---

## HRBS-15216 (UA, DD da Nataliia, devolvido pela Config)

**Pedido (Vaishnavi, 16/10 08:53):** "We are not configuring anything related to the regulation… We cannot modify the regulation fields… Kindly review Natalia's comment and take this forward accordingly." O pedido original da Nataliia (descrição, 25/09) era tornar 7 campos não obrigatórios, apagar o 1C, renomear o ЄСВ Rate Effective Date, criar "SSC Rate", explicar TSB/ESV Category e traduzir. Em 26/09 ela pediu "update the DD fields in the Altium test entity REF-04-254".

**Arquivo:** export `Ukraine_Data_Dictionary_V4.2 (1).xlsx` (Downloads, 16/10 11:28, md5 785dcfd8). O `.gsheet` V4.2 no Drive foi alterado pela última vez às 08:22 de 16/10, antes da export, e não existe V4.3.

| # | Afirmação do rascunho | Fonte primária (reaberta) | |
|---|---|---|---|
| 1 | As mudanças estão no DD desde a V4.0 (Version Control, 30/09) | Version Control linha 26: "4.0, 2026-09-30, HRBS-15216 (Nataliia Hahan): …" | ✅ |
| 2 | Continuam na versão vigente, V4.2 | Drive: V4.2 é a maior; export posterior à última edição | ✅ |
| 3 | Contract Start Date, Oblast (Region), Street and Building Number, Postal Code e TSB Eligibility opcionais | Country Fields linhas 25, 17, 13, 15, 34 = O | ✅ |
| 4 | 1C Personnel Number removido | Nenhuma linha | ✅ |
| 5 | ЄСВ Rate Effective Date renomeado SSC Rate Effective Date | Linha 41 (código `esv_rate_effective_date`) | ✅ |
| 6 | Supporting Document Reference (D5) conditional mandatory | Linha 56 = CM | ✅ |
| 7 | Sem campo SSC Rate | Nenhuma linha "SSC Rate" além da 41 | ✅ |
| 8 | Enquadramento: "The DD changes **Nataliia requested** are in the DD" | Ela pediu D5 "should not be mandatory" e um campo "SSC Rate"; entregamos CM e **não** criamos o SSC Rate (correção de 28/09). A frase lista os dois corretamente, mas chama tudo de "o que ela pediu" | ⚠️ |

**Ponto de atenção da geral:** a versão sem o fronteiras.md está confirmada; o rascunho não cita a fronteira.

**Cobertura**

| Item | |
|---|---|
| "Review Natalia's comment" (o DD está certo?) | ✅ |
| "Take this forward" (quem leva os campos para o nível de país) | ⚠️ O rascunho só constata fatos e marca @lli **sem pedir nada**. Sem próximo passo, o ticket deve voltar de novo para nós |

**% = (7 + 1) / (8 + 2) = 8/10 = 80%.**

**Veredito: AJUSTAR.**
1. Trocar "The DD changes Nataliia requested are in…" por "The DD changes made for Nataliia's request are in…".
2. Dizer o próximo passo em forma de pergunta, que não precisa de fonte. Por exemplo: "@lli, the V4.2 country fields are ready; could you confirm who applies them at country level for REF-04-254?" Quem marcar e o que pedir é **decisão do usuário** (o fronteiras.md aponta Configuration Analyst / Dev, mas a fonte é chat interno).

---

## HRBS-14528 (ES, SILTRA `.msj`)

**Pedido (Shyam, 16/10 07:56):** a integração do `.msj` já existe; "what Wallisson has mentioned in comment, for that please schedule a call to have understanding of this requirement".

| # | Afirmação do rascunho | Fonte primária (reaberta) | |
|---|---|---|---|
| 1 | Nosso comentário de 28/09 não é requisito, só descreve o `.msj` | Comentário de 28/09 relido: descritivo ("The .msj files are just a heads-up…") | ✅ |
| 2 | É um "Aviso de notificación en Sede Electrónica" da TGSS | Os dois `.msj` (anexos 1994345724 e 1996557362): `LIN"Aviso de notificación en Sede Electrónica - ANSEm3"`; "competencia de Tesorería General de la Seguridad Social" | ✅ |
| 3 | Assunto (NMTT1HAF10) | `T=(NMTT1HAF10)`, `/ASUNTO/=(NMTT1HAF10)` | ✅ |
| 4 | Com data e hora | `ETINMTT0… 202609012311`; `/FECHA/=02-09-2026 /HORA/=21:37:39` | ✅ |
| 5 | NIF da empresa | `0B78001963` (formato de pessoa jurídica) | ✅ |
| 6 | Link da Sede | `http://run.gob.es/ydylkn` | ✅ |
| 7 | A notificação só pode ser lida na Sede | Texto do `.msj` + Orden ISM/903/2020 art. 8.1 ("acceda al contenido… a través de dicha sede") | ✅ |
| 8 | Sem acesso em 10 dias naturais desde a disponibilização = rejeitada (art. 8.1) | BOE consolidado (atualizado em 01/06/2026), art. 8.1, 2º parágrafo: "Se entenderá rechazada la notificación si, transcurrido el plazo de diez días naturales desde la puesta a disposición… no se accede a su contenido" | ✅ |
| 9 | Com o `.msj` já integrado, nada mais é preciso da Compliance | Condicional à afirmação do próprio Shyam (16/10); integração é da Integration/Config ([[fronteiras]], linha 20) | ✅ |

**Cobertura:** o pedido de call foi respondido de forma implícita (nada mais é preciso) ✅. Nada fora do pedido.

**% = 10/10 = 100%.**

**Veredito: PODE ENVIAR.** Opcional: tornar explícito "no call is needed". Detalhe de estilo: "(subject (NMTT1HAF10))" tem parênteses duplos.

---

## HRBS-14394 (NL, teto da SV / 52990)

**Pedido (Abarna, 16/10 10:06, para @anaik):** "Please confirm from wellison that which formula i need to update? share that WTC or formula please. as in compliance pay elements we don't update anything by ourselves."

**Arquivos:** WTC `Netherlands Wage Type Catalogue V3.3.xlsx` (Downloads, export de 15/10 10:57). O `.gsheet` V3.3 no Drive foi alterado pela última vez em 13/10 08:12 e não existe V3.4. Handboek: `raw/docs/oficiais/NL/2026-10-13-handboek-loonheffingen-2026-versie-maart-2026-lh0221t61fd.pdf`.

| # | Afirmação do rascunho | Fonte primária (reaberta) | |
|---|---|---|---|
| 1 | Não há fórmula para compartilhar a partir do WTC | Ver 2 e 4 | ✅ |
| 2 | 52990 não está no WTC master holandês | Busca no arquivo: só aparece no Version Control | ✅ |
| 3 | Removido na v2.0, 31/07/2025 | Version Control linha 23: "2.0, 2025-07-31… Delete 52990", Released | ✅ |
| 4 | 52999 (Social Security Ceiling) é Interim Calculation Output, sem fórmula no WTC (V3.3, linha 239) | Wage Type Catalogue A239 = 52999, E239 = Interim Calculation Output, F239 vazia | ✅ |
| 5 | Dia 305,41; semana 1.527,09; 4 semanas 6.108,38; mês 6.617,41; trimestre 19.852,25; ano 79.409,00 | Handboek 2026 (março 2026), Tabel 11 "Loontijdvakbedragen maximumpremieloon en maximumbijdrageloon", p. 519 do PDF: valores idênticos | ✅ |
| 6 | Fonte: Handboek Loonheffingen 2026, Bijlage 1, tabel 11 | Mesma página (tabelas de prêmios da Bijlage 1) | ✅ |

**Cobertura:** "which formula / share WTC or formula" ✅ (não existe fórmula no WTC; valores dados). Risco, não falha: a Abarna sugere que pay element de compliance não é dela. O rascunho não diz quem ajusta a fórmula de 52990 na configuração do cliente, e está certo em não prescrever configuração. Pode haver um novo pingue-pongue; quem deve ser marcado fica com o usuário.

**% = 7/7 = 100%.**

**Veredito: PODE ENVIAR.** Pista opcional (sem afirmar nada novo): no master, o tipo de período do teto vem do 58204 (`$hr.max_ss_base`, linha 267).

---

## SR-163 (UA, D6) — nota sobre o schemaLocation

**Pedido:** **nenhum dirigido a nós.** A última menção a @wgomes é de 15/10 10:43 e foi respondida às 17:29. Hoje a conversa é só entre Lily e mjohn (12:53, "Done. updated."). A triagem da própria Suporte registrou "Nenhum nosso". A nota é proativa, por decisão da geral.

**Anexos lidos:** `20261016-0832 - special_seniority new template.xml` (linha 2) e também os **arquivos gerados pelo sistema**: `20261016-0626 - Special Seniority Report 2026-02-01 - 2026-02-28.xml` e `20261016-0832 - Special Seniority Report sample test.xml`. **Os dois saem com `xsi:noNamespaceSchemaLocation="J0510610.xsd"`**, o que contradiz o mjohn ("Root element… is not part of the output file"). A sample das 08:32 sai **sem** C_REG, C_RAJ e C_STI_ORIG.

| # | Afirmação do rascunho | Fonte primária (reaberta) | |
|---|---|---|---|
| 1 | Template de 16/10, linha 2: `xsi:noNamespaceSchemaLocation="J0510610.xsd"` | Anexo 08:32, linha 2 | ✅ |
| 2 | Com C_DOC_VER 11 | Mesmo anexo, `<C_DOC_VER>11</C_DOC_VER>` | ✅ |
| 3 | O Format da ДПС exige que o root DECLAR referencie o arquivo do schema | Format: "Кореневим елементом є елемент з іменем DECLAR, при оголошенні цього елемента вказується посилання на схему контролю даних (XML схему)" | ✅ |
| 4 | Nome = C_DOC + C_DOC_SUB + C_DOC_VER (2 dígitos) + .xsd | Format: "Файл з XML-схемою іменується… позиції з 1 по 3… C_DOC; з 4 по 6… C_DOC_SUB; з 7 по 8… C_DOC_VER, доповненого зліва нулем до 2 символів; файл має розширення xsd" | ✅ |
| 5 | Para a versão 11: J0510611.xsd | Pacote oficial v11 `J0510611.xsd`: C_DOC_SUB fixed 106, C_DOC_VER fixed 11 (linhas 93–94) | ✅ |
| 6 | "(Format, наказ Міндоходів № 729 of 29.11.2013, **Додатки 1–2**)" | Data e número ✅ (página da ДПС). A regra do nome e da referência está no **corpo** do Format, não nos Додатки. Додаток 1 (п. 6) só mostra a estrutura (`"ім'я файла, що містить XML-схему"`) e Додаток 2 (п. 11) o exemplo `J0100112.xsd` | ⚠️ |
| 7 | C_REG, C_RAJ e C_STI_ORIG obrigatórios no XSD J0510611 | Linhas 97, 98 e 102, sem `minOccurs="0"` | ✅ |
| 8 | E precisam ter valor no arquivo de teste | Format: "Жодний з описаних вище елементів (крім елементів LINKED_DOCS та SOFTWARE)… не може мати пусте значення"; a sample das 08:32 sai sem os três | ✅ |

**Cobertura:** não há pergunta. Pelo protocolo (CLAUDE.md, item 3), "se ninguém nos mencionou nem perguntou, não há o que responder". Enviar é **decisão do usuário**. O defeito é real e afeta a aceitação do D6, então recomendo enviar, mas com a evidência mais forte.

**% = 7/8 = 87%** (só as afirmações; não há pedido para medir a cobertura).

**Veredito: AJUSTAR (citação) + decisão do usuário.**
1. Citação: "(Format approved by наказ Міндоходів № 729 of 29.11.2013; example in its Додаток 2)".
2. Citar o **arquivo gerado** e não só o template, porque isso responde à afirmação do mjohn de que o root não sai no output: "The generated test file of 16/10 (Special Seniority Report sample test.xml) starts with `xsi:noNamespaceSchemaLocation="J0510610.xsd"` and has no C_REG, C_RAJ, C_STI_ORIG."
3. Como o mjohn disse "Done. updated." às 12:53 (sem anexo novo), confirmar antes de enviar que o problema ainda existe.
4. Achado lateral (hub, não ticket): na tabela de 06:26, a Lily escreveu que o root gerado é `J0510411.xsd`; o arquivo real diz `J0510610.xsd`.

---

## Resumo

| Ticket | % | Veredito | O que ajustar |
|---|---|---|---|
| SR-414 | 92% | Ajustar | Cor diferente do azul que já existia (pedido explícito da Lily); decisão do usuário × padrão interno |
| SR-415 | 92% | Ajustar | Idem |
| SR-160 | 73% | Ajustar | Avisar do BA Mapping da linha 30 (`labour_book_holder_indicator`); item 3 (N) contraditório e sem resposta ao zero; linha 23 da spec (Y "zero or blank") contradiz a regra Y |
| HRBS-15216 | 80% | Ajustar | "changes made for her request"; dizer o próximo passo (quem leva os campos para o nível de país; decisão do usuário) |
| HRBS-14528 | 100% | Pode enviar | Opcional: "no call is needed" |
| HRBS-14394 | 100% | Pode enviar | — |
| SR-163 | 87% | Ajustar + decisão | Ninguém nos perguntou; citação (corpo do Format, não Додатки 1–2); citar o arquivo gerado, que contradiz o mjohn; conferir se o "Done. updated." das 12:53 já resolveu |

Nada foi editado nem enviado por esta janela.

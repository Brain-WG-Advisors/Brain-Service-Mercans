# Respostas da fila — 2026-10-16 (janela Suporte)

> Tarefas da janela geral (aprovadas pelo usuário em 16/10). **Nada gravado no YouTrack** (nenhum draftComment) e nenhum envio. Base: [[2026-10-16-triagem-tickets]].

---

## HRBS-14528 (ES, SILTRA `.msj`) — rascunho para o Shyam

**O que ele pede:** a Config diz que a integração do `.msj` já existe e pede uma call para entender "o que o Wallisson mencionou" (nosso comentário de 28/09).

**Leitura:** nosso comentário de 28/09 foi só descritivo (o que o arquivo contém), não um requisito novo. Basta dizer isso; a call não é necessária.

**Rascunho (EN):**

> Hi @stripathi,
>
> My comment of 28/09 is not an additional requirement. It only describes what the .msj contains: a TGSS "Aviso de notificación en Sede Electrónica" (subject (NMTT1HAF10)) with the date and time, the company NIF and the Sede link. The notification itself can only be read in the Sede; if it is not accessed within 10 calendar days of being made available, it is deemed rejected (Orden ISM/903/2020, art. 8.1). With the .msj already integrated in HRBlizz, nothing further is needed from Compliance.

**Fontes (lidas hoje):**
- Conteúdo do `.msj`: anexos `raw/tickets/api/anexos/HRBS-14528/20260912-2225 - 1994345724.msj` e `- 1996557362.msj`: linha `LIN"Aviso de notificación en Sede Electrónica - ANSEm3"`, `ASUNTO=(NMTT1HAF10)`, NIF, URL `run.gob.es`, e o próprio texto "Se dispone de un plazo de 10 días naturales… se entenderán que han sido rechazadas y por tanto practicadas".
- Prazo de 10 dias: Orden ISM/903/2020, art. 8.1, 2º parágrafo ("Se entenderá rechazada la notificación si, transcurrido el plazo de diez días naturales desde la puesta a disposición de la notificación en la SEDESS, no se accede a su contenido"). Texto consolidado do BOE, última atualização em 01/06/2026: https://www.boe.es/eli/es/o/2020/09/24/ism903/con
- Pela [[fronteiras]], integração e configuração são da Config; a nossa parte (dizer o que é o arquivo e o efeito legal) foi entregue em 28/09.

**Confiança:** 100% (as duas fontes relidas hoje; a última frase é condicional à afirmação do próprio Shyam de que o `.msj` já está integrado).

---

## HRBS-15216 (UA, DD da Nataliia, devolvido pela Config) — proposta

**O que pedem:** Vaishnavi (Config, 16/10): "não configuramos nada de regulação; se os campos estiverem no nível de país, aparecem na entidade; não podemos alterar campos de regulação". Pede que levemos adiante o pedido da Nataliia de 26/09 ("update the DD fields in the Altium test entity REF-04-254").

**Evidência (diverge da recomendação da geral):** a alteração do artefato **já foi entregue**. Não há DD novo a fazer:
- DD **V4.0** (Version Control, 30/09): "HRBS-15216 (Nataliia Hahan): Contract Start Date, Oblast (Region), Street and Building Number, Postal Code set to Optional; 1C Personnel Number removed; ЄСВ Rate Effective Date renamed SSC Rate Effective Date; Supporting Document Reference (D5) set to Conditional Mandatory…".
- Na export do **DD V4.1** (`Downloads/Ukraine_Data_Dictionary_V4.1.xlsx`, 14/10), aba Country Fields: Street and Building Number = O; Postal Code = O; Oblast (Region) = O; Contract Start Date = O; TSB Eligibility = O; SSC Rate Effective Date (renomeado) = CM; Supporting Document Reference (D5) presente; nenhuma linha "1C Personnel Number". O SSC Rate não foi criado, como corrigimos em 28/09.
- Vigente: DD **V4.2**. **Conferido na export de hoje** (`Downloads/Ukraine_Data_Dictionary_V4.2 (1).xlsx`, 16/10 11:28, baixada pelo Chrome com ok do usuário), aba Country Fields: linha 13 Street and Building Number = O; 15 Postal Code = O; 17 Oblast (Region) = O; 25 Contract Start Date = O; 34 TSB Eligibility = O; 41 SSC Rate Effective Date = CM; 56 Supporting Document Reference (D5) = CM ("Mandatory only when a D5 labour event is reported"); nenhuma linha "1C Personnel Number" nem "SSC Rate". Version Control 4.0 (30/09) com o registro do HRBS-15216.
- Quem aplica o DD no nível de país: pela [[fronteiras]] (linha 9), "Desenho oficial de regulação em produção" é do **Configuration Analyst / Dev (Mohit, Ruchi, Lily, Suman, Luci)**, não nosso.

**Achados no DD (fora do pedido; não entram no ticket, a decidir):** na aba SaaS da V4.1, `TSB Eligibility` aparece com código `tab_eligibility` (na Country Fields é `tsb_eligibility`), e `Oblast (Region)` continua ligado à lista "Ukrainian Oblasts", embora o option mapper tenha sido removido na V3.6. Não sei o que significa a coluna "Yes/No" da SaaS (sem cabeçalho), então não concluo nada sobre a obrigatoriedade ali.

**Rascunho (EN), se o usuário concordar:**

> Hi @vmane1@mercans.com,
>
> The DD changes Nataliia requested are in the Ukraine Data Dictionary since V4.0 (Version Control, 30/09) and remain in the current version, V4.2: Contract Start Date, Oblast (Region), Street and Building Number, Postal Code and TSB Eligibility optional; 1C Personnel Number removed; ЄСВ Rate Effective Date renamed SSC Rate Effective Date; Supporting Document Reference (D5) conditional mandatory; no SSC Rate field. Applying the country-level DD in the system sits with the Configuration Analyst / Dev team (@lli).

(Quem marcar: a confirmar com o usuário; a Lily é a BA dos SR da Ucrânia.)

---

**Confiança:** fatos do DD 100% (export V4.2 lida célula a célula). A frase "aplicar no nível de país é do Configuration Analyst / Dev" vem só do [[fronteiras]] (fonte interna, chat) → **90%**. Alternativa 100%: tirar essa frase e terminar em "…no SSC Rate field." marcando @lli.

---

## SR-414 / SR-415 (UA, 1-PV) — specs prontas (scratchpad), não copiadas para o Drive

**Pedido (Lily, 16/10 11:09 / 11:07):** campos da aba Sample faltando na aba Spec; alinhar e destacar em outra cor.

**Base:** exports de hoje pelo Chrome (ok do usuário): `Downloads/UA-1PV-001_MonthlyLabourReport_Spec (8).xlsx` (planilha ativa 16/10 07:40) e `UA-1PV-002_QuarterlyLabourReport_Spec (6).xlsx` (08:14). Diff da (8) contra a v5.2 do Drive: só V9 e V11 (edições da Lily).

**Feito:**
- `scratchpad/out/UA-1PV-001_MonthlyLabourReport_Spec_v5.3.xlsx`: linhas 17–30 (cabeçalho de seção + 13 linhas: TIN, C_DOC, C_DOC_SUB, C_DOC_VER, C_DOC_TYPE, C_DOC_CNT, C_REG, C_RAJ, PERIOD_MONTH, PERIOD_TYPE, PERIOD_YEAR, D_FILL, NOMER), Seq 13–25, tudo em `FFDDEBF7`; Version Control 5.3 (linha 20).
- `scratchpad/out/UA-1PV-002_QuarterlyLabourReport_Spec_v1.5.xlsx`: linhas 31–46 (os 12 do DECLARHEAD + OBL, RAY, NOMER), Seq 25–39, `FFDDEBF7`; Version Control 1.5 (linha 18).
- Coluna V (BA Mapping) das linhas novas em branco (é da Lily).

**Conferência mecânica:** diff célula a célula base × nova: nenhuma alteração fora das linhas novas e do Version Control. Teste "todo elemento da Sample tem linha/menção na coluna U": 21/21 (mensal) e 28/28 (trimestral); FIRM_EDRPOU/FIRM_NAME/FIRM_KVED continuam nas linhas existentes (6–8 mensal; 4 trimestral). As duas Samples validam no XSD oficial (lxml): S0301016 e S0301121 com o common_types do Держстат de 14.05.2025.

**Fontes de cada linha nova:** XSD S0301016/S0301121 (fixed de C_DOC, C_DOC_SUB, C_DOC_VER; tipos); Держстат Format 3.1, Tabela 1 (TIN, C_DOC_TYPE "Завжди рівний 0", C_DOC_CNT, C_REG/C_RAJ pelo SPR_SSCU.XML, PERIOD_MONTH "останній місяць у звітному періоді", PERIOD_TYPE "1-місяць, 2-квартал…", D_FILL "ддммрррр"); SPR_SSCU (Kyiv = 80, locais 361…; no SPR_STI da ДПС Kyiv = 26); lista de campos técnicos do Держстат (OBL/RAY: КАТОТТГ, обов'язкове, preenchido do cartão da empresa); erratum oficial do XSD S0301121 (NOMER = "Номер структурного підрозділу"); Роз'яснення 19.1.2-12/24-24 п. 8 e 19.1.2-12/25-24 п. 5 (dados do subdivisão estrutural).

**Rascunho SR-414 (EN):**

> Hi @lli,
>
> Spec v5.3: rows 17–30 added to the UA-1PV-001 Spec sheet for the Sample elements that had no row (the 12 DECLARHEAD elements and NOMER), in Sample order, highlighted in light blue.

**Rascunho SR-415 (EN):**

> Hi @lli,
>
> Spec v1.5: rows 31–46 added to the UA-1PV-002 Spec sheet for the Sample elements that had no row (the 12 DECLARHEAD elements, OBL, RAY and NOMER), in Sample order, highlighted in light blue.

**Confiança:** 100% (cada linha com fonte primária lida hoje; teste de cobertura e diff). Falta só o usuário aprovar a cópia para o Drive (`_v5.3` e `_v1.5`) e importar.

**Fora do pedido (→ hub, não ticket):** a lista de campos técnicos do Держстат marca OBL e RAY como obrigatórios também no 1-ПВ **mensal**, mas o XSD S0301016 os tem como `minOccurs="0"` e a Sample mensal não os traz.

---

## HRBS-14394 (NL) — pergunta nova da Abarna (13:06)

**Pedido:** "Please confirm from Wallisson which formula I need to update? share that WTC or formula" (para @anaik).

**Fato:** no WTC NL **V3.3** (export 15/10 10:57; `.gsheet` sem alteração desde 13/10 08:12) não existe fórmula para o teto: 52990 foi apagado (Version Control 2.0, 31/07/2025, "Delete 52990"); 52999 "Social Security Ceiling" (linha 239) é "Interim Calculation Output" com a coluna Formula vazia; o tipo de período vem do 58204 (`$hr.max_ss_base`, linha 267). Valores 2026 relidos hoje: Handboek Loonheffingen 2026 (versão março 2026), Bijlage 1, tabel 11, p. 519.

**Rascunho (EN):**

> Hi @Abarna @anaik,
>
> There is no formula to share from the WTC: 52990 is not in the Netherlands master WTC (removed in v2.0, 31/07/2025), and 52999 (Social Security Ceiling) is an Interim Calculation Output with no formula in the WTC (V3.3, row 239). The 2026 maximum premium wage per pay period is: day €305.41, week €1,527.09, 4 weeks €6,108.38, month €6,617.41, quarter €19,852.25, year €79,409.00 (Belastingdienst, Handboek Loonheffingen 2026, Bijlage 1, tabel 11).

**Confiança:** 100%.

---

## SR-163 (UA, D6) — nota para a Lily (schemaLocation)

**Prova:** `raw/docs/oficiais/UA/2026-10-16-VERIFICACAO-D6-schemaLocation.md` (Format da ДПС, наказ Міндоходів № 729 de 29.11.2013: o root DECLAR referencia o schema; nome = C_DOC + C_DOC_SUB + C_DOC_VER + .xsd; Додаток 1 e 2). Template do Dev 16/10 08:32, linha 2: `J0510610.xsd` com `C_DOC_VER` 11.

**Rascunho (EN):**

> Hi @lli,
>
> D6 template of 16/10 (special_seniority new template.xml), line 2: xsi:noNamespaceSchemaLocation="J0510610.xsd" with C_DOC_VER 11. The ДПС format requires the root DECLAR to reference the XML schema file, named C_DOC + C_DOC_SUB + C_DOC_VER (2 digits) + .xsd; for version 11 that is J0510611.xsd (Format, наказ Міндоходів № 729 of 29.11.2013, Додатки 1–2). C_REG, C_RAJ and C_STI_ORIG are required in XSD J0510611 and must carry values in the test file.

**Confiança:** 100% para o que está escrito (não afirma rejeição pela ДПС).

---

## SR-160 (UA, D1) — pergunta nova da Lily (13:56): zero × omitir — **bloqueado**

**Pedido:** regra consistente para quando escrever 0/0.00 e quando omitir (Y/C/N), com G22, G23, G24, G12/G13/G15, G18 como exemplos; ou uma coluna "omit if zero".

**Provado (fonte primária):** Format da ДПС (наказ 729): elemento vazio = `xsi:nil="true"` obrigatório; elemento ausente no DECLARBODY = valor vazio. XSD J0510111: `T1RXXXXG12`–`G26` e `R01G16`–`R01G20` todos opcionais (`minOccurs="0"`, `nillable`).

**Desbloqueado (16/10 tarde):**
- Export de hoje pelo Chrome (ok do usuário): `Downloads/UA-D1-001_UnifiedSocialContribution_Spec (4).xlsx`.
- Formulário oficial `raw/docs/oficiais/UA/j0500111-extraido/J0510111.pdf` renderizado como imagem (PyMuPDF) e lido: colunas 21 "Ознака основного місця роботи (1 - так, 0 - ні)", 22 "Ознака неповного робочого часу (1 - так, 0 - ні)", 23 "Ознака наявності спецстажу (1 - так, 0 - ні)", 24 "Ознака нового робочого місця (1 - так, 0 - ні)", 25 "Ознака (0,1)" com nota 13 (só para "Звітний новий" e "Уточнюючий"), 26 "Ознака наявності трудового договору з нефіксованим робочим часом (1 - так, 0 - ні)", nota 14 ("наявність та/або відсутність").
- **Erro nosso achado:** a spec D1 (linha 30) chamava a coluna 21 de "Labour Book Indicator ⚠ UNVERIFIED"; o formulário diz "Ознака основного місця роботи". O BA Mapping (coluna U, da Lily) usa `$hr.labour_book_holder_indicator`.

**Spec D1 v3.4 (scratchpad, não copiada):** `scratchpad/out/UA-D1-001_UnifiedSocialContribution_Spec_v3.4.xlsx` (com a correção da linha 30) e `scratchpad/out/semG21/…v3.4.xlsx` (sem ela). Mudanças: F32/F33 C→Y e G32/G33 com a fonte; amostra sem T1RXXXXG18 e com T1RXXXXG24 = 0 (válida no XSD J0510111, lxml); Version Control 3.4. Diff: só essas células e as linhas 53–64 da amostra (deslocadas).

**Rascunho (EN):** `rascunhos/2026-10-16-youtrack-drafts/SR-160.md` (itens 1–3 da Lily + base do Format/XSD + correção da linha 30).

**Confiança:** 100% (formulário oficial v11 lido, XSD J0510111, Format da ДПС; amostra validada).

---

## HRBS-14996 (CI) — nada a responder no ticket

Último comentário: Mohit, 29/09 06:03 ("Done… Select Stop Tax as Yes"); estado Resolved. Ninguém perguntou nada a nós depois disso no ticket. A pergunta sobre a IFPGAZ 2026 não está no ticket (deve estar no e-mail, frente Gmail).

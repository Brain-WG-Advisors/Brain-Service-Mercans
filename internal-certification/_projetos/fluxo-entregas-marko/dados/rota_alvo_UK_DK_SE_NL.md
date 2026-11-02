# Rota-alvo das entregas de payroll: Reino Unido, Dinamarca, Suécia, Holanda (29/10/2026)

> Escopo: só a **rota-alvo** (o que a fonte oficial diz). A rota de hoje não foi pesquisada aqui.
> Lidas em 29/10/2026. Arquivos em `brain-service/raw/docs/oficiais/<CC>/2026-10-29-canal/` (UK = `GB`). Cada trecho literal foi conferido por script contra o arquivo baixado (ver bloco de prova).
> Siglas de fonte: **G**=Reino Unido, **D**=Dinamarca, **S**=Suécia, **N**=Holanda. Descrição de cada fonte na seção "Fontes" de cada país.

---

## 1. Reino Unido (HMRC)

| Entrega | Canal oficial | Figura de agente/intermediário | Credencial | Autorização do cliente | Recibo | Mudanças/prazos | Fonte |
|---|---|---|---|---|---|---|---|
| **FPS** (Full Payment Submission), em ou antes do dia do pagamento | RTI por software de folha ("internet submissions"); o software cria os relatórios e envia online. Obrigatório: o agente "must send" o FPS. Nome técnico do protocolo (XML via Government Gateway/Transaction Engine): **[Verify]** | Tax agent com **PAYE agent ID code** e serviço **PAYE for Agents**; "payroll agent" é categoria interna do HMRC (G6) | **Government Gateway user ID e senha** associados ao PAYE for Agents + agent reference number. Quem detém: o agente (bureau) | Formulário **64-8** (seção "Employers' PAYE"), ou autorização online (Online Agent Authorisation) | Recibo eletrônico ("electronic receipts for all of your submissions", G1). Nome técnico da resposta do RTI: **[Verify]** | Ver linha de mudanças abaixo | G1, G2, G3, G4, G6, G9 |
| **EPS** (Employer Payment Summary), até o dia 19 do mês fiscal seguinte | Igual ao FPS (RTI) | Igual | Igual | Igual | Igual ao FPS | — | G1, G2 |
| **P11D / P11D(b)** (benefícios, após o ano fiscal) | Serviço online **PAYE for Agents** (agente envia P11D, P11D(b) e as "Amendment") ou software | Igual | Igual (Gateway do PAYE for Agents) | Igual (64-8) | Recibo eletrônico (G1) | **A partir de 06/04/2027**: carros, vans, combustível e benefício médico passam a ser reportados pelo FPS (folha); **a partir de 06/04/2028**: a maior parte dos demais. P11D permanece para empréstimos e acomodação. | G1, G7, G8 |

**Mudanças e prazos (2026-2027) que afetam o canal**
- **Registro obrigatório de payroll agents como tax adviser no HMRC: a janela abre em 18/11/2026** (G7). Isto atinge a Mercans/bureau se prestar serviço de folha e falar com o HMRC em nome de clientes. Detalhe do critério: **[Verify]** (a página de checagem do HMRC não foi baixada).
- **BiK em folha (FPS) a partir de 06/04/2027** (G8) e fase 2 em 06/04/2028 (G8).
- **Formulário FBI 2 foi retirado**; só 64-8 (G5). O manual interno PAYE21165 ainda cita "signed FBI 2" (G6): conflito entre páginas do próprio HMRC, **[Verify]**.
- Há especificação técnica RTI 2027-28 publicada (G9); versão genérica 1.94 de 06/04/2026 (G9).

### Fontes (Reino Unido)
- **G1** `gb_paye_for_agents.html` · https://www.gov.uk/guidance/payecis-for-agents-online-service
  - Trecho: “Your payroll software will create the new reports you need and send the payroll information online.” (O seu software de folha cria os relatórios e envia as informações online.)
  - Trecho: “When your payroll software sends your reports, you’ll need your Government Gateway user ID and password associated with PAYE for agents to access them.” (Quando o software envia os relatórios, você precisa do ID e senha do Government Gateway associados ao PAYE for Agents.)
  - Trecho: “you must send your payroll information to us using a Full Payment Submission” (você deve enviar as informações de folha usando um FPS.)
  - Trecho: “have an agent reference number” (ter um agent reference number.)
  - Trecho: “set up authorisation for each of your clients” (configurar a autorização de cada cliente.)
  - Trecho: “get electronic receipts for all of your submissions” (obter recibos eletrônicos de todos os envios.)
  - Trecho: “You can use PAYE for Agents to send HMRC any of these reports:” (Você pode usar o PAYE for Agents para enviar ao HMRC estes relatórios:) com a lista P11D, P11D Amendment, P11D(b), P11D(b) Amendment.
  - Trecho: “For tax year 2024 to 2025 you must continue to submit P11Ds for benefits and expenses that have not been payrolled.” (Para 2024-25 deve-se continuar a enviar P11D dos benefícios não passados em folha.)
- **G2** `gb_report_payments.html` · https://www.gov.uk/guidance/what-payroll-information-to-report-to-hmrc
  - Trecho: “you need to report your employee’s pay, any payrolled benefits, and deductions in a Full Payment Submission (FPS) on or before their payday” (é preciso reportar pagamento, benefícios em folha e deduções em um FPS em ou antes do dia do pagamento.)
  - Trecho: “You will also need to send an Employer Payment Summary (EPS) by the 19th of the following tax month” (também é preciso enviar o EPS até o dia 19 do mês fiscal seguinte.)
- **G3** `gb_64-8.pdf` · https://assets.publishing.service.gov.uk/media/6852e9f02b367fdd44c15e8a/64-8.pdf (versão 05/25)
  - Trecho: “Employers' PAYE” (seção do formulário)
  - Trecho: “I authorise the agent named above to use PAYE online services to receive information over the internet from HMRC on my behalf and I have given my agent Government Gateway ID and PAYE agent ID code.” (Autorizo o agente a usar os serviços PAYE online para receber informações do HMRC em meu nome e dei ao agente o Government Gateway ID e o PAYE agent ID code.) Observação: o 64-8 autoriza o agente a RECEBER informações; o envio (FPS) é coberto em G6.
- **G4** `gb_authorising_agent.html` · https://www.gov.uk/guidance/authorising-an-agent-to-deal-with-your-tax-affairs
  - Trecho: “When authorised, your agent will have access to your employees’ personal and financial information.” (Quando autorizado, o agente terá acesso às informações pessoais e financeiras dos seus empregados.)
- **G5** `gb_agent_paper_forms.html` · https://www.gov.uk/guidance/applying-for-client-authorisation-using-hmrc-paper-forms e `gb_fbi2.html` · https://www.gov.uk/government/publications/tax-agents-and-advisers-authorising-an-agent-to-use-payecis-online-services-internet-fbi-2
  - Trecho (agent_paper_forms): “Your clients can use form 64-8 to authorise you to act on their behalf for:” (Seus clientes podem usar o 64-8 para autorizar você a agir em nome deles para:) seguido de “PAYE for employers”.
  - Trecho (fbi2): “The link to form FBI2 has been removed because you can now use form 64-8 to authorise an agent.” (O link do FBI2 foi removido porque agora se usa o 64-8.)
- **G6** `gb_paye21165.html` · https://www.gov.uk/hmrc-internal-manuals/paye-manual/paye21165 (manual interno do HMRC)
  - Trecho: “We must have a signed FBI 2 authorisation before we can send information to agents using PAYE online for Employers - Internet. We can however receive information, on behalf of the employer from any agent or representative.” (Precisamos de FBI 2 assinado para ENVIAR informação a agentes; podemos porém RECEBER, em nome do empregador, de qualquer agente.)
  - Trecho: “A payroll agent may be employed by an employer to predominately handle the payroll for that employer.” (Um payroll agent pode ser contratado por um empregador para tratar predominantemente da folha dele.)
- **G7** `gb_employer_bulletin_oct2026.html` · https://www.gov.uk/government/publications/employer-bulletin-october-2026/october-2026-issue-of-the-employer-bulletin
  - Trecho: “The registration window for payroll agents opens on 18 November 2026.” (A janela de registro para payroll agents abre em 18/11/2026.)
  - Trecho: “If you provide payroll or PAYE services and communicate with HMRC on behalf of clients as part of your business, you may need to register under HMRC’s mandatory tax adviser registration requirements.” (Quem presta serviços de folha/PAYE e fala com o HMRC em nome de clientes pode ter de se registrar na exigência de registro de tax adviser.)
  - Trecho: “You need to submit a P11D for each employee in receipt of benefits and or non-exempt expenses unless you registered with us online before 6 April 2025 to tax them through your payroll.” (É preciso enviar P11D por empregado, salvo se registrou online antes de 06/04/2025 para tributar via folha.)
- **G8** `gb_bik_2027_mandatory_rti.html` · https://www.gov.uk/government/publications/changes-to-reporting-of-benefits-in-kind-from-april-2027/mandatory-reporting-of-benefits-in-kind-in-real-time-information-rti-from-april-2027
  - Trecho: “The measure will have effect from 6 April 2027.” (A medida vale a partir de 06/04/2027.)
  - Trecho: “will be required to report the benefit through payroll software and deduct tax in real time” (será exigido reportar o benefício pelo software de folha e deduzir o imposto em tempo real.)
  - Trecho: “From April 2028, most remaining benefits in kind, except for employer provided loans and accommodation, will be mandated to be reported and paid in the same way.” (A partir de abril/2028, a maior parte dos demais benefícios, exceto empréstimos e acomodação, será obrigatória da mesma forma.)
- **G9** `gb_rti_generic_spec.html` · https://www.gov.uk/government/publications/real-time-information-internet-submissions-generic-technical-specifications e `gb_rti_dev_support.html` · https://www.gov.uk/government/collections/real-time-information-online-internet-submissions-support-for-software-developers
  - Trecho (generic_spec): “Internet submissions technical specifications for Real Time Information online software developers.” (Especificações técnicas de envio pela internet do RTI para desenvolvedores de software.)
  - Trecho (generic_spec): “How to use the internet services has been updated to version 1.94.” (O documento "How to use the internet services" foi atualizado para a versão 1.94.)
  - Trecho (dev_support): “Real Time Information internet submissions: 2027 to 2028 technical specifications” (título de especificação publicada para 2027-28.)

---

## 2. Dinamarca (Skattestyrelsen / Skatteforvaltningen)

| Entrega | Canal oficial | Figura de agente/intermediário | Credencial | Autorização do cliente | Recibo | Mudanças/prazos | Fonte |
|---|---|---|---|---|---|---|---|
| **Indberetning à eIndkomst** (lønoplysninger, A-skat, AM-bidrag, ATP, feriepenge; mensal) | Digital e obrigatória: via lønsystem adaptado, lønservicebureau, TastSelv Erhverv ou LetLøn. Para software: **2 soluções system-til-system, WebSphere MQ e Sterling File Gateway (SFG)**; a página lista também SFTP, WebService (WSDL 1.2), MyFileGateway e WebClient | **Lønservicebureau** (definição: quem indberetter ao mesmo tempo para mais de um SE-nr.) | Contrato próprio: o bureau "skal indgå en særlig aftale med Skattestyrelsen"; para SFG, aftale com Skattestyrelsen/IBM (partner mailbox); MQ idem. O guia técnico diz que a segurança do envio "baseres på netværkssikkerheden". Tipo de certificado/chave por canal: **[Verify]** (não aparece no guia v5.0 de 2021) | O bureau recebe acesso do **Skatteforvaltningen**: "giver vi dem adgang ... Du skal derfor ikke give lønbureauet adgang". Revisor/rådgiver é outro caso: o cliente dá acesso (revisorordning) via MitID Erhverv Rettighedsadministrator | **Indberetningskvittering** (código INDBKVIT) e **INDBKVITLB** para o bureau; advisering de erros incluída | Sem mudança de canal 2026-27 encontrada: **[Verify]**. "Den juridiske vejledning 2026-2" confirma a obrigação digital | D1, D2, D3, D4, D5 |
| **Pagamento de A-skat e AM-bidrag** | O site orienta como terceiro passo ("Betal A-skat og am-bidrag til os"); canal de pagamento e prazo exatos: **[Verify]** (a seção não foi lida) | — | — | — | — | Juros contam do prazo original; o prazo de 14 dias acabou em 01/07/2023 (D1) | D1 |
| **Outros reports do empregador** | Não pesquisado além da eIndkomst; ATP e feriepenge aparecem como campos dentro da indberetning (D1) | — | — | — | — | — | D1 |

### Fontes (Dinamarca)
- **D1** `dk_saadan_indberetter.html` · https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/saadan-indberetter-du-loen-eindkomst
  - Trecho: “Hvis et lønbureau skal indberette for dig, giver vi dem adgang til at indberette på vegne af din virksomhed. Du skal derfor ikke give lønbureauet adgang.” (Se um bureau de folha for indberetter por você, nós damos a ele acesso para indberette em nome da sua empresa. Você não precisa dar acesso ao bureau.)
  - Trecho: “Hvis en revisor eller rådgiver skal indberette for dig, skal du først selv have adgang til eIndkomst.” (Se um contador ou consultor for indberetter por você, você precisa primeiro ter acesso à eIndkomst.)
  - Trecho: “Derefter skal du give dem adgang til at indberette for dig via den såkaldte revisorordning.” (Depois você dá a eles acesso via a chamada revisorordning.)
  - Trecho: “Som lønservicebureau skal du kontrollere, at nye kunders registreringsforhold tillader indberetning til eIndkomst.” (Como lønservicebureau você deve checar que o registro dos novos clientes permite indberetning.)
  - Trecho: “Du kan indberette via eget lønsystem eller direkte i eIndkomst.” (Pode-se indberette pelo próprio sistema de folha ou direto na eIndkomst.)
  - Trecho: “3. Betal A-skat og am-bidrag til os” (3. Pague A-skat e AM-bidrag a nós.)
  - Trecho: “Hvis du bruger lønbureau eller revisor, kan de have kortere frister end normalt.” (Se usa bureau ou contador, eles podem ter prazos mais curtos que o normal.)
- **D2** `dk_system_til_system.html` · https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/saadan-indberetter-du-loen-eindkomst/vejledninger-til-eindkomst-mq-og-sfg
  - Trecho: “På denne side kan du læse om vores 2 system-til-system-løsninger til kommunikation med eIndkomst.” (Nesta página: nossas 2 soluções system-a-system para comunicação com a eIndkomst.)
  - Trecho: “kvittering for indberetninger” (recibo das indberetninger; listado entre o que as duas soluções cobrem.)
  - Trecho: “eIndkomst: WebService WSDL version 1.2 (zip)” (arquivo listado na página.)
- **D3** `dk_teknisk_vejledning_mq_sfg.pdf` (versão 5.0, 30/08/2021) · https://www.skat.dk/media/wewdbl2h/eindkomst-teknisk-vejledning-til-mq-og-sfg.pdf
  - Trecho: “Virksomheder, der skal agere lønservicebureau, skal indgå en særlig aftale med Skattestyrelsen om dette.” (Empresas que atuem como bureau de folha devem firmar um acordo especial com a Skattestyrelsen.)
  - Trecho: “I denne sammenhæng er alle, der indberetter samtidigt for mere end et SE-nr., at betragte som et lønservicebureau.” (Aqui, quem indberetter ao mesmo tempo para mais de um SE-nr. conta como bureau.)
  - Trecho: “Der returneres kvittering inkl. eventuel advisering om fejl i indberetning.” (Devolve-se recibo, com eventual aviso de erro.)
  - Trecho: “INDBKVITLB Indberetningskvittering til lønservicebureau” (código do recibo para o bureau.)
- **D4** `dk_juridisk_vejledning_AB1341.html` · https://info.skat.dk/data.aspx?oid=2284512 (Den juridiske vejledning 2026-2, A.B.1.3.4.1)
  - Trecho: “Indberetning til eIndkomst skal ske digitalt ved at sende indkomstoplysningerne via et lønsystem, som er tilpasset eIndkomst, ved at” (A indberetning deve ser digital, enviando os dados por um sistema de folha adaptado à eIndkomst, por meio de:) seguido de "benytte et lønservicebureau", "bruge TastSelv Erhverv", "bruge LetLøn".
  - Trecho: “Den juridiske vejledning 2026-2” (edição lida.)
- **D5** `dk_giv_adgang.html` · https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/saadan-faar-du-adgang-til-eindkomst-og-letloen/faa-og-giv-adgang-til-eindkomst-og-letloen
  - Trecho: “For at kunne tildele din rådgiver eller revisor rettigheder til at indberette og forespørge i eIndkomst på vegne af din virksomhed, skal du være MitID Erhverv Rettighedsadministrator og selv have rettigheder til eIndkomst.” (Para dar ao consultor/contador direitos de indberette em nome da empresa, você precisa ser MitID Erhverv Rettighedsadministrator e ter direitos na eIndkomst.)

---

## 3. Suécia (Skatteverket)

| Entrega | Canal oficial | Figura de agente/intermediário | Credencial | Autorização do cliente | Recibo | Mudanças/prazos | Fonte |
|---|---|---|---|---|---|---|---|
| **Arbetsgivardeklaration (AGI)**, mensal, até o dia 12 do mês seguinte (para a maioria) | Três vias: e-tjänst "Lämna arbetsgivardeklaration" (com "Deklarera via fil", arquivo XML), **API aberta "Arbetsgivardeklaration inlämning" (v1.6)** a partir do lönesystem, ou formulário em papel. O API é opcional ("ett annat sätt"); o sistema precisa estar adaptado | **Programvaruföretag** (contrato de acesso ao API) + **deklarationsombud / behörig företrädare / registreringsombud** do lado do empregador | **OAuth 2.0 Authorization Code Grant**, organização autenticada com **organisationscertifikat**; software identificado por **Client ID/Secret**; o provedor em nuvem pode usar o próprio certificado | **O empregador (ou ombud com e-legitimation) revisa e assina no Mina sidor**: o API só carrega o underlag e "låser" o período; assinatura e envio NÃO são feitos pelo API. Ombud designado pelo empregador via SKV 4809 / e-tjänst "Ombud och behörigheter" | **Kvittens** (data e hora, quem enviou, kvittensnummer, resumo e OCR/bankgiro) | Ver abaixo | S1, S2, S3, S4 |
| **Pagamento de skatteavdrag e arbetsgivaravgifter** | Conta de imposto da empresa (skattekonto); instrução na mesma página: "Inbetalning till skattekonto" | — | — | — | A kvittens traz valor a pagar, vencimento, bankgiro e OCR | — | S1 |

**Mudanças e prazos**
- O contrato de provedor é fechado com o Skatteverket antes de usar o API (S3). A tjänstebeskrivning v1.6 lida é de 16/02/2023 (doc. v1.13); se há versão mais nova: **[Verify]**.
- Mudanças recentes de conteúdo da teknisk beskrivning 1.1.18.2: redução temporária de arbetsgivaravgifter para 18-22 anos desde abril/2026; arquivo via filöverföringstjänst limitado a 300 MB (antes 500 MB); não se aceita mais AGD com mais de seis anos (S4). Nenhum anúncio de corte do canal API encontrado: **[Verify]**.

### Fontes (Suécia)
- **S1** `se_lamna_agd.html` · https://www.skatteverket.se/foretag/arbetsgivare/lamnaarbetsgivardeklaration.4.41f1c61d16193087d7fcaeb.html
  - Trecho: “Ett annat sätt att lämna arbetsgivardeklarationen är direkt i företagets lönesystem via öppet API. Det förutsätter att lönesystemet är anpassat för det.” (Outra forma de entregar é direto no sistema de folha da empresa por API aberto. Pressupõe que o sistema esteja adaptado.)
  - Trecho: “Du låser redovisningsperioden i e-tjänsten Lämna arbetsgivardeklaration i ytan som heter Granska, eller via API.” (Você trava o período no e-tjänst, em "Granska", ou via API.)
  - Trecho: “Om du vill att någon annan ska lämna din arbetsgivardeklaration kan du utse ett deklarationsombud som kan lämna din deklaration via e-tjänsten på Mina sidor.” (Se quer que outra pessoa entregue a declaração, pode designar um deklarationsombud.)
  - Trecho: “Både behöriga företrädare och deklarationsombud kan granska, signera och skicka in uppgifter.” (Tanto representantes autorizados quanto deklarationsombud podem revisar, assinar e enviar.)
  - Trecho: “Registreringsombud har tillgång till alla funktioner utom att signera och skicka in.” (O registreringsombud tem acesso a tudo exceto assinar e enviar.)
  - Trecho: “När du har fått din kvittens har Skatteverket tagit emot din arbetsgivardeklaration.” (Ao receber a kvittens, o Skatteverket recebeu a declaração.)
  - Trecho: “På kvittensen framgår det när arbetsgivardeklarationen är inlämnad med datum och klockslag.” (A kvittens mostra quando foi entregue, com data e hora.)
  - Trecho: “De allra flesta ska lämna in arbetsgivardeklarationen senast den 12:e i den efterföljande månaden.” (A grande maioria entrega até o dia 12 do mês seguinte.)
  - Trecho: “Kom ihåg att betala in avdragen skatt och arbetsgivaravgifter till företagets skattekonto” (Lembre de pagar o imposto retido e as contribuições patronais na conta de imposto da empresa.)
- **S2** `se_tjanstebeskrivning_agd_inlamning.pdf` (Tjänstebeskrivning v1.6, doc. 1.13, 2023-02-16) · https://www7.skatteverket.se/portal-wapi/open/apier-och-oppna-data/utvecklarportalen/v1/getFile/tjanstebeskrivning-agd-inlamning/pdf/1.0.3/tjanstebeskrivning-agd-inlamning.pdf
  - Trecho: “Auktorisation sker med hjälp av Oauth 2.0 authorization Code Grant, där organisationen autentiseras med hjälp av ett organisationscertifikat.” (A autorização usa OAuth 2.0 Authorization Code Grant, com a organização autenticada por certificado organizacional.)
  - Trecho: “Arbetsgivare och deras ombud genom nyttjande av lönesystem eller andra utbetalare genom affärssystem.” (Consumidores previstos: empregadores e seus ombud via sistema de folha, ou outros pagadores via sistema de negócio.)
  - Trecho: “Funktionen granska/signera hanteras alltså inte direkt via tjänsteanrop i Skatteverkets öppna API.” (A função revisar/assinar não é feita por chamada do API aberto.)
  - Trecho: “Efter granskning kan arbetsgivardeklarationen signeras och skickas in.” (Após a revisão, a declaração pode ser assinada e enviada.)
  - Trecho: “Underlaget anses aldrig inkommet till Skatteverket så länge det ligger i det egna utrymmet.” (O material nunca é considerado recebido enquanto estiver no espaço próprio.)
  - Trecho: “kan molntjänstleverantören använda ett eget Organisationscertifikatet för autentisering av den Externa användaren.” (o provedor de nuvem pode usar o próprio certificado para autenticar o usuário externo.)
  - Trecho: “resulterar i en kvittens på att arbetsgivardeklarationen är mottagen.” (resulta em uma kvittens de que a declaração foi recebida.)
- **S3** `se_avtal_agd_inlamning.pdf` (modelo de contrato) · https://www7.skatteverket.se/portal-wapi/open/apier-och-oppna-data/utvecklarportalen/v1/getFile/avtal-api-arbetsgivardeklaration-inlamning
  - Trecho: “Skatteverket har godkänt Programvaruföretagets ansökan om anslutning till API:et.” (O Skatteverket aprovou o pedido de conexão da empresa de software ao API.)
- **S4** `se_tekn_beskr.html` · https://www.skatteverket.se/foretag/arbetsgivare/lamnaarbetsgivardeklaration/tekniskbeskrivningochtesttjanst/tekniskbeskrivning1111.4.7eada0316ed67d7282a791.html
  - Trecho: “Teknisk beskrivning (1.1.18.2) för arbetsgivardeklaration” (versão lida.)
  - Trecho: “Skatteverket har beslutat att ändra maxstorleken för filer som skickas via filöverföringstjänsten. Från september är den nya maxstorleken 300 MB, jämfört med tidigare 500 MB.” (O Skatteverket reduziu o tamanho máximo de arquivo na filöverföringstjänst para 300 MB, antes 500 MB.)
  - Trecho: “Nedsättningen gäller från och med april 2026” (A redução vale desde abril de 2026.)
  - Trecho: “Det innebär att det inte längre är möjligt att skicka in arbetsgivardeklarationer som är äldre än sex år.” (Não é mais possível enviar declarações com mais de seis anos.)

---

## 4. Holanda (Belastingdienst / Logius)

| Entrega | Canal oficial | Figura de agente/intermediário | Credencial | Autorização do cliente | Recibo | Mudanças/prazos | Fonte |
|---|---|---|---|---|---|---|---|
| **Aangifte loonheffingen** (inclui eerstedagsmelding) | **SBR via Digipoort**, canal seguro do governo; software próprio de aangifte deve usar SBR ("verplicht") | **Intermediair** (fiscaal dienstverlener); no lado Digipoort, "hubgebruiker" usa a conexão do intermediário/softwareleverancier | **PKIoverheid services servercertificaat** (comprado de um TSP; KVK-number) do aanleveraar; quem detém: o intermediário (ou o empregador, se tiver conexão própria) | O cliente permanece responsável. Mecanismo formal de machtiging específico para loonaangifte via Digipoort (ketenmachtiging / Machtigingenregister Digipoort): **[Verify]** | **Ontvangstbevestiging** na software do remetente + atualização do "Overzicht aangiften en opgaven" no portal; o intermediário também recebe aviso de recebimento | Prazos e mudanças 2026-27: **[Verify]** (não lidos) | N1, N2, N3, N4, N5, N6 |
| **Jaaropgaaf / outros** | Não pesquisado | — | — | — | — | — | — |

### Fontes (Holanda)
- **N1** `nl_sbr.html` · https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/intermediairs/aangifte_doen/standard_business_reporting e `nl_wat_betekent_sbr.html` · https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/intermediairs/aangifte_doen/standard_business_reporting/watbetekentsbsvooru
  - Trecho: “U gebruikt dan het beveiligde digitale kanaal van de overheid: Digipoort.” (Então você usa o canal digital seguro do governo: Digipoort.)
  - Trecho: “Om berichten via Digipoort te kunnen versturen en ontvangen, hebt u een PKIoverheid services servercertificaat nodig.” (Para enviar e receber mensagens via Digipoort é preciso um certificado de servidor PKIoverheid services.)
  - Trecho (wat_betekent_sbr): “de aangifte loonheffingen en eerstedagsmelding” (a declaração de loonheffingen e a eerstedagsmelding, listadas entre as que se fazem com SBR via Digipoort.)
- **N2** `nl_hoe_doe_je_aangifte_lh.html` · https://stichtingenvereniging.belastingdienst.nl/aangifte/aangifte-loonheffingen/hoe-doe-je-aangifte-loonheffingen/ (página da Belastingdienst para stichtingen e verenigingen)
  - Trecho: “Maar je bent dan wel verplicht hiervoor Standard Business Reporting (SBR) te gebruiken.” (Mas então é obrigatório usar o SBR.)
  - Trecho: “Hij stuurt de aangifte vervolgens naar de Belastingdienst.” (Ele então envia a declaração à Belastingdienst; sobre o fiscaal dienstverlener.)
  - Trecho: “Wees je er dan van bewust dat de stichting of vereniging altijd zelf verantwoordelijk blijft voor het indienen van de juiste aangifte loonheffingen.” (Esteja ciente de que a organização continua sempre responsável por entregar a declaração correta.)
- **N3** `nl_logius_aansluiten.pdf` · https://www.logius.nl/sites/default/files/bestanden/website/Aansluiten%20op%20Digipoort.pdf
  - Trecho: “heeft een overeenkomst met een externe softwareleverancier / intermediair / hub om berichtenverkeer via hun Digipoort-aansluiting te gebruiken.” (tem acordo com um fornecedor de software/intermediário/hub para usar a conexão Digipoort deles.)
  - Trecho: “heeft geen eigen aansluiting, die heeft de intermediair.” (não tem conexão própria; quem tem é o intermediário.)
  - Trecho: “Verplicht voor gebruik Digipoort” (sobre o certificado PKIoverheid.)
- **N4** `nl_logius_pki.html` · https://www.logius.nl/english/pkioverheid/instructions-digipoort
  - Trecho: “Purchase a PKIoverheid certificate based on your KVK-number from a Trust Service Provider (TSP).” (Compre um certificado PKIoverheid baseado no número KVK de um Trust Service Provider.)
- **N5** `nl_toelichting_meldingen_lh.pdf` (LH 512, documento antigo; ver [Verify]) · https://download.belastingdienst.nl/belastingdienst/docs/toelichting_meldingen_verzenden_aangifte_lh5121t5fd.pdf
  - Trecho: “ontvangstbevestiging in software van verzender van aangifte” (confirmação de recebimento no software do remetente.)
  - Trecho: “bijwerken van Overzicht aangiften en opgaven op beveiligde gedeelte van onze internetsite” (atualização do painel "Overzicht aangiften en opgaven" na área segura.)
- **N6** `nl_gegevens_aangifte_lh_2025.pdf` (Gegevensspecificaties aangifte loonheffingen 2025) · https://download.belastingdienst.nl/belastingdienst/docs/gegevens_aangifte_loonheffingen_2025_lh9861t51fd.pdf
  - Trecho: “Als er geen fouten worden geconstateerd, dan krijgt ook de intermediair bericht van de Belastingdienst dat de loonaangifte is ontvangen en verwerkt kan worden.” (Se não há erros, o intermediário também recebe aviso de que a declaração foi recebida.)
  - Trecho: “Aan A&A kantoren en andere intermediairs die voor verschillende inhoudingsplichtigen aangifte doen” (a escritórios e outros intermediários que declaram para vários inhoudingsplichtigen; pedido de preencher o campo do aanleveraar.)

---

## [Verify] (lacunas que a fonte lida não resolve)

1. **UK:** nome técnico do protocolo do FPS/EPS (XML via Government Gateway / Transaction Engine) e nome do recibo/resposta do RTI: está na especificação "How to use the internet services v1.94" (ODT, não baixada).
2. **UK:** se um bureau sem agent code precisa de uma conta de PAYE for Agents própria para enviar o FPS de cada cliente ou usa as credenciais do cliente. G1 diz que o software usa o Gateway do PAYE for Agents; confirmar com o Dev e com a especificação.
3. **UK:** conflito entre G5 (FBI2 retirado) e G6 (manual interno ainda cita FBI 2).
4. **UK:** critério exato do registro de tax adviser para payroll agents (janela 18/11/2026): página de checagem do HMRC não lida.
5. **DK:** tipo de credencial por canal (SFG/MQ/SFTP/WebService); o guia v5.0 de 2021 só fala em segurança de rede. Ler Vejledning til MyFileGateway/SFTP/WebService.
6. **DK:** canal e prazo de pagamento de A-skat e AM-bidrag; prazos de indberetning para empresa privada; qualquer mudança 2026-27 (nada achado).
7. **SE:** existe versão da tjänstebeskrivning mais nova que a v1.6 (2023)? Há plano de descontinuar o login anterior? Nenhum anúncio lido.
8. **NL:** mecanismo de machtiging do empregador ao intermediário para loonaangifte (ketenmachtiging no Machtigingenregister Digipoort ou apenas o uso do loonheffingennummer). A pesquisa só mostrou o Machtigingenregister em outro contexto (UWV).
9. **NL:** o documento N5 é antigo e fala de canal BAPI; usado só para a existência do recibo. Confirmar o nome atual das mensagens de retorno no SBR (berichtspecificatie).
10. **NL:** prazos de corte e mudanças 2026-27 não pesquisados.
11. **SE/NL/DK/UK:** a Mercans está registrada como agente/intermediário/lønservicebureau/payroll agent em algum deles? Isto é "rota de hoje", fora deste arquivo.

---

## Bloco de prova

- **Fontes lidas** (baixadas em 29/10/2026 com curl, salvas em `raw/docs/oficiais/{GB,DK,SE,NL}/2026-10-29-canal/`): GB 9 arquivos (gov.uk), DK 5 (skat.dk, info.skat.dk), SE 5 (skatteverket.se, www7.skatteverket.se), NL 8 (belastingdienst.nl, logius.nl). Skatteverket recusa o curl padrão; funcionou com `--http1.1 --tlsv1.2` e user agent de navegador.
- **Teste mecânico:** todos os trechos entre aspas “...” da seção Fontes foram buscados por script nos textos extraídos dos arquivos baixados (HTML sem tags; PDF por pdftotext, com e sem layout), ignorando espaços. Resultado do script: ver linha abaixo.
- **Resultado da conferência:** 78 trechos conferidos, 78 achados no arquivo indicado (a única falha inicial era um trecho atribuído ao arquivo errado e foi corrigida). Conferência feita pelo texto extraído; a tabela de cada país é síntese minha dos trechos, não é citação
- **Confiança:** UK 80%, DK 80%, SE 85%, NL 65%. UK/DK/SE: canal e figura do agente com fonte; faltam credencial técnica e o nome do recibo do RTI (UK) e credencial por canal (DK). NL: canal, certificado e figura do intermediário com fonte; a autorização formal do empregador não foi resolvida pela fonte. As traduções são minhas.
- **O que falta:** itens [Verify] acima; nenhuma afirmação de "rota de hoje" foi feita.

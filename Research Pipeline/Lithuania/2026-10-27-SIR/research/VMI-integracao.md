# Lituânia: integração da folha com a VMI (GPM313 mensal, GPM312 anual)

Levantamento de 2026-10-27, só com fontes oficiais da VMI (EDS deklaravimas.vmi.lt e documentos publicados nele). Material bruto em `raw/docs/oficiais/LT/2026-10-27-VMI-reports/` (já existia) e `raw/docs/oficiais/LT/2026-10-27-VMI-integracao/` (novo; URLs e md5 em `_FONTES.md`). Ligado a: [[Lituania]] (hub), SIR da Lituânia.

Nenhum login feito, nenhum envio, nenhuma operação de web service chamada. Única chamada a endpoint: GET público da descrição WSDL (`?WSDL`) do serviço de upload, para conferir se ele ainda existe (ver F11).

## Fontes

| # | Documento | Emissor / data | Onde |
|---|---|---|---|
| F1 | "Elektroninio deklaravimo sistema. Versija 2.01. Deklaracijų teikimas žiniatinklio paslauga" (`EDSUplaodFileViaWebService-v2-2010_08_19.doc`) | VMI, nome do arquivo com data 2010-08-19 | `2026-10-27-VMI-reports/` (md5 aae02f12…) |
| F2 | Página EDS "Žiniatinklio paslauga" (LT e EN) | VMI EDS, lida em 2026-10-27 | `2026-10-27-VMI-integracao/EDS_Ziniatinklio_paslauga.html`, `EDS_EN_Ziniatinklio_paslauga.html` |
| F3 | Página EDS "Apie formų teikimą / Formų teikimo būdai" | VMI EDS, 2026-10-27 | `EDS_PradineInformacija.html` |
| F4 | Página EDS "Užpildytų formų persiuntimas" (+ subpáginas certificado e assinatura) | VMI EDS, 2026-10-27 | `EDS_Failu_persiuntimas_1.html`, `EDS_Deklaruoti_sertifikata.html`, `EDS_Elektroninis_parasas.html`, `EDS_persiusti_el_parasu_pasirasyta_dokumenta.html` |
| F5 | Página EDS "Pildymas tiesiogiai portale" | VMI EDS, 2026-10-27 | `EDS_Pildymas_portale.html` |
| F6 | Regras de uso do EDS: ordem VA-72 de 2021-10-26 (texto com a alteração VA-88 de 2022-10-29), LT e EN, + anexo | VMI, baixado do EDS (página "Apie EDS") | `EDS_taisykles_VA72_LT.docx`, `EDS_rules_VA72_EN.docx`, anexos |
| F7 | Ajuda do EDS: "Formų statusų reikšmės", "Kaip prisijungti?", "Kaip tapti registruotu EDS naudotoju?", "Užsienio valstybės pilietis…", "Teisių administravimas", "El. paštas pranešimams", "Kvalifikuotas sertifikatas" | VMI EDS, 2026-10-27 | `EDS_HelpItem_*.html` |
| F8 | Notícias do EDS: 2026-08-27 "Dėl prisijungimo prie EDS"; 2026-04-15 "Dėl pateiktų deklaracijų apdorojimo vėlavimo" | VMI EDS | `EDS_Naujiena_*.html` |
| F9 | Regras GPM313 (VA-121 de 2017-12-20, última alteração VA-105 de 2025-11-20), versão "nuo 2026" | VMI | `2026-10-27-VMI-reports/x_IN_GPM313_DOC/IN_GPM313_nuo_2026.docx` |
| F10 | Regras GPM312 (VA-9 de 2018-02-06, alteração VA-24 de 2026-03-26) | VMI | `2026-10-27-VMI-reports/x_IN_GPM312_DOC/IN_GPM312.docx` |
| F11 | WSDL publicado hoje em `https://deklaravimas.vmi.lt/EDSWebServiceUploadFile/EDSWebServiceUploadFile.asmx?WSDL` | VMI, lido em 2026-10-27 | `EDSWebServiceUploadFile_WSDL_live.xml` |
| F12 | MXFD GPM313 (CreatedOn 2025-11-04) e GPM312 (CreatedOn 2026-05-11), atributos de `<FormDef>` | VMI (ABBYY eFormDesigner 2.5) | `2026-10-27-VMI-reports/x_GPM313_mxfd/`, `x_GPM312_mxfd/` |
| F13 | Lista de formulários do EDS filtrada GPM313 / GPM312 | VMI EDS, 2026-10-27 | `2026-10-27-VMI-reports/EDS_Formu_sarasas_filtro_*.html` |

## Base legal da entrega

- GPM313: a declaração é preenchida no sistema de declaração eletrônica da VMI (F9 §6). É entregue conforme as regras VA-135 (F9 §13) e **"teikiamos ir tikslinamos tik elektroniniu būdu"** pelo EDS (http://deklaravimas.vmi.lt), conforme as regras de uso do EDS VA-72 (F9 §14). Prazo: até o dia 15 do mês seguinte (F9 §12).
- GPM312: declaração e anexos L/U são preenchidos no EDS (F10 §11), entregues conforme VA-135 (F10 §58) e só por via eletrônica pelo EDS, conforme VA-72 (F10 §59). Prazo: até 15 de fevereiro do ano seguinte (F10 §57).
- O próprio EDS marca o GPM313 como "Teikiama tik elektroniniu būdu" a partir de 2018 (F13, coluna Pastabos).

## Canais

| Canal | Direção | Quem usa | Autenticação | Formato | Documentação |
|---|---|---|---|---|---|
| **1. Preenchimento on-line no portal EDS** ("Deklaravimas → Pildyti formą") | Pagador → VMI | Usuário do EDS com direito de representar o pagador | Login no EDS (F7 "Kaip prisijungti?": sistemas externas, meios dados pela VMI ou assinatura eletrônica; desde 1º de setembro, só pelos meios do portal "Elektroninių valdžios vartų" e fim do login direto por bancos, F8 2026-08-27). Assinatura eletrônica opcional (F5) | Formulário web; o portal calcula os campos de soma e acusa erros na hora (F5) | F5; F6 §21.1 |
| **2. Upload de arquivo ("Persiųsti failą" / "Persiųsti užpildytą formą")** | Pagador → VMI | Usuário do EDS; arquivo gerado por programa de contabilidade ou outro software | (a) **Logado no EDS:** assinatura eletrônica não é exigida. (b) **Sem login:** só com documento assinado por assinatura eletrônica qualificada e certificado declarado no EDS (F4) | "Formato indicado nos requisitos técnicos de preparação do documento publicados no site do EDS" (F6 §21.2). FFData: ver "Formato" | F4; F6 §21.2 |
| **3. Web service ("žiniatinklio paslauga") EDSWebServiceUploadFile** | Pagador/software → VMI (envio) e consulta de estado VMI → software | Software de contabilidade/folha; ativação **só por representantes de pessoa jurídica** (F2) | Usuário e senha próprios do serviço, criados no EDS em "Nustatymai → Mano duomenys" (F2; F1 "Autentifikavimas"); SSL (F1). **Precisa de confirmação humana no portal** (ver fluxo) | SOAP 1.1 document/literal; arquivo `.ffdata` ou `.ffdata` zipado, em Base64 (F1 SubmitFile) | F1 (spec 2010); F2; F6 §21.3; F11 |
| 4. `FFDataCollectServer` = `https://deklaravimas.vmi.lt/EDSMdocUploadService/MdocUploadService.svc` | Provavelmente envio (nome do atributo) | NOT LOCATED | NOT LOCATED | NOT LOCATED | Só aparece como atributo no MXFD do GPM313 e do GPM312 (F12). Nenhuma página ou documento oficial localizado descreve este endpoint. **Não usar como canal sem documentação.** |
| 5. `URLUpdateForm` = `http://deklaravimas.vmi.lt/PublicServiceREST` | VMI → software (atualizar o modelo do formulário, pelo nome) | NOT LOCATED | NOT LOCATED | NOT LOCATED | Só atributo do MXFD (F12). Uso não documentado. |

A lista dos três modos de entrega (portal, upload, web service) é oficial em dois lugares: F3 ("Dokumentus galima pateikti: …tiesiogiai EDS portale; …persiunčiant per EDS portalą; …naudojantis žiniatinklio paslauga („web service")") e F6 §21.1–21.3.

### Autenticação e representação (vale para os canais 1–3)

- Para entrar no EDS, a pessoa se autentica pelos meios da VMI previstos nas regras VA-83 de 2010-07-21 (F6 cap. II; F7 "Kaip tapti…"). Desde 2021-12-01 não se assinam mais contratos com o EDS: basta aceitar as regras de uso (F7 "Teisių administravimas").
- Representação de pessoa jurídica: o dirigente recebe os direitos de rever e enviar documentos, de assinar eletronicamente e de administrar representantes. Ele pode delegar a outras pessoas, inclusive "Tik nurodytas" (só formulários escolhidos, ex. GPM313/GPM312) (F6 cap. II; F7 "Teisių administravimas"). O responsável pela contabilidade da PJ (pessoa física ou jurídica) pode receber os direitos automática ou manualmente (F6 cap. II).
- **Estrangeiro sem registro na VMI** (relevante para operador de folha fora da Lituânia): (1) pedido à AVMI com o formulário "Užsienio piliečio prašymas suteikti prisijungimo prie VMI informacinių sistemų priemones", com identidade comprovada (cópia notarial se for por correio); ou (2) declarar no EDS um certificado qualificado de assinatura **emitido por prestador na Lituânia** (F7 "Užsienio valstybės pilietis"). O certificado qualificado é sempre de pessoa física, nunca da PJ (F4 "Elektroninis parašas").
- Web service: as credenciais são **do serviço**, separadas do login do EDS. A senha é guardada com hash; a ativação inicial é feita pelo usuário externo em "Deklaravimo būdai". Limite de 200 arquivos por dia e bloqueio de 30 min após 5 senhas erradas, ambos parâmetros configuráveis no `web.config` (F1 "Autentifikavimas"; valores de 2010, não confirmados hoje). `PersonCode` = código do contribuinte por quem se envia; o usuário precisa ter direito de enviar por ele (erro 302) (F1 SubmitFile).

### Formato

- O web service aceita "*.ffdata formatu arba suarchyvuotas *.ffdata failas *.zip formatu", em Base64 (F1 SubmitFile, parâmetro `File`). Ele verifica se o arquivo "yra *.ffdata formato" e se o formulário indicado no arquivo está registrado e válido no EDS (F1 SubmitFile, passos 5–6; erros 002 e 201).
- O modelo de cada formulário é publicado como MXFD (download "Forma elektroniniam pildymui" na lista de formulários, F13). GPM313: `FormDefId={EB03E9EF-39B0-457F-8264-79E86F053009}`, MXFD de 2025-11-04 (versão "2025-12-31"). GPM312: `FormDefId={DD0F88DD-A858-4595-AF2F-3643D0069A39}`, MXFD de 2026-05-11, com histórico que inclui dois FormDefId novos em 2026 (F12).
- **XSD do FFData: NOT LOCATED.** Nenhuma página do EDS lida nem o F1 publica XSD ou especificação do layout FFData. As regras de uso remetem a "dokumento parengimo techniniai reikalavimai, skelbiami EDS interneto svetainėje" (F6 §21.2, §26), mas a página com esses requisitos não foi localizada no mapa do site do EDS (`EDS_SvetainesStruktura.html`). O MXFD (XML do ABBYY eFormDesigner, com `FieldDataDef`, `MinValue`, `MaxValue`, `IsRequired`) é a única definição de campos encontrada.
- Assinatura no envio por arquivo sem login: as páginas citam a especificação MDOC-V1.0 e as regras de assinatura qualificada de documentos eletrônicos legíveis por computador (F4 "Sertifikato deklaravimas"). As regras de uso citam ADOC-V1.0 só para o anexo de representação enviado por e-mail (F6 cap. II).

## Web service de upload (F1, conferido com F11)

**Data e validade:** a documentação é a **versão 2.01, de 2010** (nome do arquivo `…-v2-2010_08_19.doc`). Indícios oficiais de que ainda vale:
1. A página atual do EDS "Žiniatinklio paslauga" (LT e EN, lida em 2026-10-27) aponta como "specifikacija" exatamente esse arquivo; o download tem o mesmo md5 `aae02f12…` (F2; `_FONTES.md`).
2. As regras de uso VA-72 de 2021, alteradas em 2022, mantêm o web service como 3º modo de entrega (F6 §21.3).
3. O WSDL publicado hoje no endereço do F1 expõe as mesmas duas operações e os mesmos elementos (F11). Diferenças: o WSDL atual também tem binding SOAP 1.2, e o `soap:address` aparece como `http://…`, enquanto o F1 indica `https://…`.

Não há documento oficial mais novo nem anúncio de desativação localizados. Não foi verificado, por limite da tarefa, se as operações respondem.

- **Endereço:** `https://deklaravimas.vmi.lt/EDSWebServiceUploadFile/EDSWebServiceUploadFile.asmx`; namespace `http://vmi.lt/EDSUploadFile.wsdl`.
- **SOAPAction:** `http://vmi.lt/EDSUploadFile.wsdl/SubmitFile` e `…/CheckFileState`.

### SubmitFile (envio)
| Campo | Tipo | Máx. | Obrig. | Descrição (F1) |
|---|---|---|---|---|
| File | texto Base64 | — | Sim | `.ffdata` ou `.zip` com `.ffdata` |
| FileName | "Skaičius" na tabela (sic; é nome) | 50 | Não | Nome exibido no portal; padrão "Failas.ffdata" |
| FileDescription | texto | 150 | Não | Descrição livre |
| AppName | texto | 100 | Sim | Nome do programa que envia |
| UserName | texto | 100 | Sim | Usuário do serviço |
| Password | texto | 25 | Sim | Senha do serviço |
| PersonCode | texto | 20 | Sim | Código do contribuinte declarado |

Retorno `SubmitFileResult`: `Result` (bool), `ErrorCode`, `Message` (em sucesso, inclui **a data até a qual o arquivo precisa ser confirmado no portal**) e `FileId` (GUID). No WSDL os campos de entrada aparecem com `minOccurs=0`; a obrigatoriedade vem da tabela do F1.
Erros: 000_ERROR, 001_NO_FILE_DATA, 002_FILE_FORMAT_NOT_VALID, 003_FILE_NOT_ACCEPTED, 101–106 (usuário inválido, bloqueado, senha errada, serviço desligado, usuário expirado, limite diário), 201_BAD_FORM_NAME, 301_NO_PERSON_LEGAL_CODE, 302_BAD_PERSON_LEGAL_CODE, 401/402 (sem usuário ou senha), 501_NO_APP_NAME. Sucesso: **900_SUCCESS** "Failas priimtas sėkmingai. Failas turi būti patvirtintas EDS portale iki {data}."

### CheckFileState (consulta de estado)
Entrada: `FileId` (GUID do SubmitFile), `AppName`, `UserName`, `Password`.
Retorno `CheckFileStateResult`: `Result`, `ErrorCode`, `Message`, mais:
- `FileStateData`: `UserConfirmedName`, `UserConfirmedCode` (quem confirmou), `FileConfirmStateCode` (**10** Patvirtintas, **20** Nepatvirtintas, **30** Pašalintas, **40** Nebetvirtinamas), `FileStateName`, `FileStateDate`;
- `DeclatationStateData` (sic): `DeclarationStateCode` (**9** aguardando checagem de outras declarações, **10** Pateikta, **21** Priimta, **22** Priimta su klaidomis, **41** retida por anulação de AS, **100** Anuliuota, **101** Nepriimta, **102** Atmesta, **103** Atmesta dėl tikrinimo, **115** Pateikta* (para o usuário, igual a 10)), `DeclarationActualityStateCode` (**10** Aktuali, **11** Aktuali dėl tikslinimo, **20** Neaktuali), nomes e datas.
Erros: 600, 601–607, 609_NEED_CHANGE_PASSWORD, 610_FILE_ID_EMPTY, 611_BAD_PERSON_LEGAL_CODE, 612_NO_FILE_FOUND, 613_NO_APP_NAME. Sucesso: 901_SUCCESS_CHECK_FILE_STATE.

## Fluxo do GPM313 e do GPM312 (do arquivo ao protocolo)

O fluxo é o mesmo para os dois; mudam o formulário, o período e o prazo (F9 §12: dia 15 do mês seguinte; F10 §57: 15 de fevereiro do ano seguinte).

**Pelo web service (canal 3)**
1. A PJ ativa o web service no EDS ("Nustatymai → Mano duomenys") e cria usuário e senha do serviço (F2).
2. A folha gera o `.ffdata` do formulário vigente (GPM313 ou GPM312 + anexos L/U), opcionalmente zipado, e codifica em Base64 (F1).
3. `SubmitFile` com `PersonCode` do pagador. Resposta 900_SUCCESS + `FileId` + data-limite de confirmação. O arquivo fica **"nepatvirtintas"** (F1 SubmitFile, passo 7).
4. **Confirmação humana obrigatória:** em até **3 dias**, um usuário externo com direito de enviar aquele formulário entra no EDS e confirma em "Deklaravimas → Patvirtinti užpildytą formą". Sem confirmação no prazo, a declaração é apagada e **a entrega não conta** (F2). O F1 diz que o prazo é configurado por formulário (`f_file_confirm_duration`); a página atual (F2) fixa 3 dias.
5. A folha consulta `CheckFileState(FileId)`: confirmação (10/20/30/40) e, depois de criada a declaração, o estado (21 aceita, 22 aceita com erros, 101 não aceita…) (F1; F2 "galite patikrinti… būseną").
6. Protocolo: no portal, "Pateikti dokumentai ir formos" registra o fato da entrega (F3). A data de entrega é fixada pelo software do EDS (F6 §24).

**Por upload (canal 2)**
1. Logado no EDS: "Deklaravimas → Persiųsti užpildytą formą" e envio do arquivo (F4).
2. O arquivo aparece em "Pateiktų dokumentų istorija → Persiųsti failai" e, se o processamento for bem-sucedido, depois em "Pateiktos formos" (F4). Em atraso de processamento, fica com status "Siunčiamas" (F8 2026-04-15).
3. Erros: no upload e no web service, o usuário é avisado pelos contatos registrados no EDS **depois do processamento** (F6 §26). No preenchimento on-line, o aviso vem na hora do envio (F6 §26).

**Status do documento no portal** (F7 "Formų statusų reikšmės"): "Dokumentas pateiktas, duomenys vertinami" → "Dokumentas priimtas" / "priimtas su nustatytais trūkumais" (erros não críticos, ver "Dokumento trūkumai") / "nepriimtas" (erros críticos) / "atmestas dėl kontrolės veiksmų" / "Dokumento duomenys anuliuoti".

**Avisos ao pagador**
- Não aceitação por motivo técnico (requisitos técnicos, assinatura sem direito, contribuinte ou período não identificável): aviso por meio eletrônico, de imediato e no máximo em **5 dias úteis** (F6 §26).
- Deficiências encontradas na checagem: **Pranešimas apie VMI pateikto dokumento trūkumus, formulário FR1025** (aprovado pela VA-135), com forma, prazo para corrigir e consequências (F6 §27).
- **Informacinis pranešimas:** aviso da administração tributária sobre erros ou divergências na declaração. Obriga a corrigir dentro do prazo indicado nele (GPM313: F9 §19.1 e §20; GPM312: F10 §64.1 e §66). Correção = nova declaração completa do mesmo mês ou ano (F9 §18; F10 §63). Se o GPM312 corrigir valores já declarados no GPM313 do mês, o GPM313 desse mês também tem de ser corrigido (F10 §65).
- Canal dos avisos: e-mail e telefone cadastrados no EDS, ou em "Mano VMI" quando o usuário representa a si mesmo. Quem representa outro contribuinte cadastra os contatos daquele representado em "Nustatymai → Atstovavimas → … ryšio priemonės". Sem contato válido, a VMI usa os contatos de outros registros (F6 cap. III; F7 "El. paštas"). Todas as informações sobre a declaração e a correção dos dados são dadas pelo EDS (F6 cap. III). O canal pelo qual o FR1025 e o informacinis pranešimas chegam (EDS, e-mail ou Mano VMI) não está especificado: **NOT LOCATED**.
- Anulação: feita no portal ("Pateiktos formos → Anuliuoti"), às vezes com aprovação de servidor da VMI (F7 "Pateikto dokumento duomenų anuliavimas"). **Não há operação de anulação no web service** (F1 só tem SubmitFile e CheckFileState).

## Inbound (VMI ou Sodra → folha)

- **Retorno do web service:** `CheckFileState` devolve à folha a confirmação e o estado da declaração (F1). É o único dado em formato de máquina que volta da VMI nas fontes lidas.
- **Avisos:** FR1025 e informacinis pranešimas (acima) chegam ao pagador, mas não há formato de máquina documentado: **NOT LOCATED**.
- **Sodra → VMI:** o GPM312 §10.1 (F10) diz que os dados de benefícios de doença, maternidade, paternidade, cuidado de filho e "ilgalaikio darbo" pagos pelo orçamento do Fundo do Seguro Social Estatal (Sodra), e os pagos pelo Fundo de Garantia, **podem ser fornecidos à VMI por outros meios que não a declaração**. Ou seja, o empregador não declara esses benefícios no GPM312. O mecanismo de troca entre Sodra e VMI não está descrito: **NOT LOCATED**.
- **VMI → empregador, dado que a folha precise importar** (ex.: NPD, cadastro do funcionário): **NOT LOCATED** nas fontes oficiais lidas. O portal só pré-carrega os dados cadastrais do pagador (Registro de Contribuintes) ao abrir um formulário novo (F5).

## Precisa de navegador

Respostas 403 (desafio "Just a moment…") ao script; nada foi contornado:
- https://e-seimas.lrs.lt/rs/actualedition/TAIS.237748/WcUJheToXE/
- https://e-seimas.lrs.lt/rs/actualedition/TAIS.363155/AzuJYvYuQq/
- https://e-seimas.lrs.lt/rs/legalact/TAD/a526a4c03efd11e68f278e2f1841c088/ (atos da VMI achados na busca por VA-72; qual ato é cada um não foi confirmado)
- https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/151e26c0369411ec99bbc1b08701c7f8/asr (link "Teisinė informacija" da página Apie EDS; não tentado, mesmo domínio)
- https://www.vmi.lt/evmi/elektroninio-deklaravimo-sistema, https://www.vmi.lt/evmi/nuotolines-paslaugos, https://www.vmi.lt/evmi/vmi-prisijungimo-priemoniu-gavimo-budai, https://www.vmi.lt/evmi/en/kas-yra-eds-ir-kaip-tapti-jos-naudotoju-/-atstovu-
- Texto consolidado oficial da VA-135 (inclui o formulário FR1025): não obtido.

## Lacunas

1. **XSD ou especificação do FFData:** NOT LOCATED. Os "requisitos técnicos de preparação do documento" citados em F6 §21.2/§26 não foram achados no site do EDS.
2. **`EDSMdocUploadService/MdocUploadService.svc`** (FFDataCollectServer do MXFD) e **`PublicServiceREST`** (URLUpdateForm): sem documentação oficial. Não se sabe se substituem ou complementam o web service de 2010.
3. **Ambiente de teste (sandbox):** NOT LOCATED em nenhuma fonte oficial.
4. **Web service atual?** Documento de 2010, ainda publicado e ainda exigido pelas regras de 2021/2022, e o WSDL de hoje bate com ele (F2, F6 §21.3, F11). Faltam uma versão mais nova da especificação e a confirmação de que os limites de 2010 (200/dia, 5 tentativas, 30 min) continuam.
5. **Confirmação humana:** o web service **não é ponta a ponta**. Toda entrega exige confirmação no portal, em até 3 dias, por pessoa com direito de envio (F2). Também não está documentado se um estrangeiro sem meios de login da VMI pode fazer essa confirmação depois da mudança de login de 1º de setembro (F8). NOT LOCATED.
6. **Canal e formato do informacinis pranešimas e do FR1025** (EDS, e-mail ou Mano VMI; formato de máquina): NOT LOCATED.
7. **Inbound Sodra→VMI e VMI→empregador:** só a menção do GPM312 §10.1. Mecanismo NOT LOCATED.
8. Texto oficial da VA-72 no e-seimas (para conferir a redação vigente além da cópia do EDS) e da VA-135: precisa de navegador.

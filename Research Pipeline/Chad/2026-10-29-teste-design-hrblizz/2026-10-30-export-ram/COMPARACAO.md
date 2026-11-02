# Chade: design do Dev (export do Ram, 30/10) × julho × nosso v4

> Hub: [[Chade]] · Conferência do v4: [[2026-10-29-design-v4/CONFERENCIA|CONFERENCIA v4]] · Pacote: [[PACOTE-CONTEXTO]]
> Feito em 2026-10-30 (frente Chade). Só leitura e comparação. Nada foi ao Dev, ao Drive nem a ticket.

**Siglas dos arquivos** (linha = `arquivo:linha`)
- `588` = `x/2  CT-A-588.md` (TD: New Design, 31 regulações td_2026; md5 `28fa82bb…`). `580` = `x/1  CT-A-580.md` (flags, notionals, quadro-resumo). `581`…`587` = `x/<n>  CT-A-58n.md` (páginas de base).
- `jul` = `G:\Drives compartilhados\Compliance Team\Country Folders\Chad\07-design\td.json` (export de 2026-07-02, 31 regs; md5 `bb62f014…`).
- `v4` = `../../2026-10-29-design-v4/chad-design-blueprint-claude-v4/SKILL.md`. `A#` = `ASSUMPTIONS.md`, `R#` = `RESEARCH_GAPS.md` da mesma pasta.
- `hub` = `paises/Chade.md` (raiz do cérebro).

---

## A) Julho × atual (Dev): mudou alguma coisa?

**Não houve mudança.** O Ram está certo.

| Conferência | Resultado | Prova |
|---|---|---|
| Número de regulações | 31 = 31 | `jul:3` (`regulationCount: 31`); `588`: 31 cabeçalhos `# 9148xxx` |
| Regulações adicionadas/removidas | nenhuma; mesmos 31 ordinais (9 a 261) e mesmos nomes | `jul:12`…`jul:2352` (`ordinal`) × `588:2`…`588:1368` |
| Classificação (tax group, rule group, taxation type, moeda, status, tax year) | idêntica nas 31 | script de diff campo a campo (abaixo) |
| Pré-condições | idênticas nas 31 | idem |
| Bandas (faixas, taxas, piso, teto, fórmula, contas débito/crédito) | idênticas, incluindo as 6 faixas do IRPP e as 6 bandas da CNPS | ex.: `jul:1805`/`588:1032` (EE 3,5 → 6020), `jul:1823`/`588:1033` (ER 7,5 → 2610) |
| Matrizes (conta, padrão, Yes/No) | idênticas nas 31 | idem |

Como foi conferido: script Python (`-I`, no scratchpad) leu as 31 regulações do `588` e do `jul` e comparou cada campo. Saída: 0 diferenças. As únicas diferenças são de apresentação: o `jul` usa UUID como `regulationId` e o `588` usa 9148xxx; no `588` a taxa aparece como "4.0"/"5.0" e no `jul` como 4.0/5.0 (mesmo valor).

Limite: comparei os dois exports. Não conferi o que está carregado no HRBlizz (o System Settings dá erro 526).

### A2) Inconsistências internas do pacote do Dev (doc × configuração)
As páginas CT-A-580/581–587 (documentação) não batem em 6 pontos com a configuração CT-A-588 (que é igual a julho). Vale perguntar ao Ram qual das duas é a intenção.

| # | Documentação diz | Configuração (588 = jul) tem | Linhas |
|---|---|---|---|
| D1 | Base "Cash Gross" sem a série 65xxx | 65%%% Yes (benefício em espécie entra no "cash gross" 58105) | `587:6-14` × `588:97` |
| D2 | CNPS: meal cash 6286% Yes | sem 6286% (nenhum padrão cobre 628xx, então fica fora por omissão) | `586:22` × `588:902-934` |
| D3 | Base não residente: meal cash 6286% Yes | sem 6286% (fora) | `583:12` × `588:137-148` |
| D4 | Bases TAFP e TFE: 58108 (abono familiar isento) Yes | sem 58108; tem 6276% No e mantém 6275% dentro | `584:5`, `585:5` × `588:793`, `588:856` |
| D5 | Base TFE sem 62229 | 62229 (6222%, pagamento discricionário único) No | `585` × `588:846` |
| D6 | Quadro: CNPS com 2610/2551 ao lado da EE 3,5 | EE 3,5 → 6020/2550; ER 7,5 → 2610/2551 | `580:67` × `588:1032-1033` |

---

## B) Atual (Dev) × nosso v4

### B1) Regra estatutária

| # | Tema | Dev (588) | Nosso v4 | Fonte que o v4 cita | Situação |
|---|---|---|---|---|---|
| 1 | Tabela do IRPP | 0 / 10,5 / 15 / 20 / 25 / 30%, faixas 800.000 · 6M · 7,5M · 9M · 12M (anual) `588:1197-1202` | igual `v4:1124-1129` | CGI Art. 1-IV `v4:1137`; escala não confirmada (A1, R1) | IGUAL (os dois herdam a lacuna R1) |
| 2 | Arredondamento do IRPP | FLOOR(x+0,5) `588:1280` | igual `v4:1170` | — | IGUAL |
| 3 | CNPS do empregado deduzida do IRPP | 3,5% negativo em 58100 `588:1036`, somado em `588:1124` | 3,5% em 58141 `v4:992`, somado em `v4:1088` | Art. 47 `v4:1091` | IGUAL |
| 4 | Abono familiar | isento até 5.000 × dependentes por mês `588:259`, `588:299` | isento por inteiro `v4:343` | CGI Art. 45; 5.000 vem do CGI do Congo, Art. 38-2° `v4:352`, R2 | DIFERENTE. Divergência do hub `hub:92`, `hub:121` **ainda vale** |
| 5 | Transporte | isento até 30% do salário-base; excesso tributável e na CNPS `588:181`, `588:220`, `588:904` | igual `v4:211`, `v4:302`, `v4:912` | Art. 45-13° `v4:310` | IGUAL. Divergência do hub `hub:94` era do WTC v1.1; Dev e v4 já aplicam 30% |
| 6 | Transporte só se "concedido a todos" | não tem | condição 58207 = 1 `v4:302` | Art. 45-13° `v4:310` | FALTA NO DEV |
| 7 | Indenização de plano social × individual | 6218% fora de IRPP, CNPS e TFE sempre `588:711`, `588:907`, `588:844` | plano social isento só com 58210 = 1 `v4:379`, `v4:391`; individual tributável no IRPP, fora de CNPS/TFE `v4:865`, `v4:1303` | Art. 45-10° `v4:393` | DIFERENTE no mecanismo. Se o código 6218x também for usado para indenização individual, o Dev isenta o que o v4 tributa. Resolver pelo WTC e pela lei |
| 8 | Aposentadoria complementar | 2164% dedutível sem teto `588:1076`, `588:1082` | 216%% dedutível até 3,5% do salário-base `v4:212`, `v4:1034`, `v4:1043` | CGI Art. 47 `v4:1045` | DIFERENTE. Pendência do hub `hub:123` (teto do Art. 47 na 9148181) **ainda vale** |
| 9 | Não residente: taxa | 18% `588:1319` | 18% `v4:1255` | Art. 116 `v4:1222` | IGUAL |
| 10 | Não residente: base | bruto (621–627, 629, 65%%% a valor cheio, 794), sem Art. 45 `588:131-148` | 58105 menos transporte, abono e plano social isentos `v4:1211-1220` | Art. 116 + Art. 45 `v4:1222` | DIFERENTE. A skill (esclarecimento 2, `hub:51`) apoia o Dev. Resolver pela lei |
| 11 | Não residente: TFE/TAFP | calcula (pré-condição só exclui diplomata) `588:1352`, `588:1391` | não calcula `v4:1290`, `v4:1375` | CCG Cenário B, A6 (sem artigo) | DIFERENTE. A skill (esclarecimento 1, `hub:50`) diz que NR com contrato local paga. Resolver pela lei |
| 12 | Não residente: CNPS | paga todos os ramos `588:1026` | por ramo, conforme flags 58202–58204 `v4:988-991` | A6 (sem artigo) | DIFERENTE. Resolver pela lei (skill, `hub:50`) |
| 13 | Deficiente, jovem graduado, diplomata | 58218: 2, 3 e 4 sem IRPP; jovem graduado tributa após 60 meses; diplomata fora de tudo `580:4-6`, `588:1274` | igual `v4:14`, `v4:1118`, `v4:1263` (nota da 9148075) | v4 não cita artigo | IGUAL. Artigo da isenção: resolver pela lei |
| 14 | CNPS: taxas | EE 3,5; ER 7,5 + 4,0 + 5,0; total 20 `588:1032-1037` | EE 3,5; PVID ER 5; PFM 7,5; AT/MP 4; total 20 `v4:988-993` | v4 não cita artigo (`hub:75`: Lei 7/66, Decretos 2009) | IGUAL |
| 15 | CNPS: piso e teto | 720.000 / 6.000.000 por ano (60.000 / 500.000 por mês), fixo `588:965` | igual `v4:947` | Suman 16/10 `v4:955` | IGUAL. Decisão do hub `hub:95` (piso fixo) vale para os dois |
| 16 | CNPS sobre o piso em mês sem salário | sem condição: o piso pode gerar CNPS com salário zero `588:959` | só se 58130 > 0 `v4:941` | Suman 16/10 (piso se aplica com matriz vazia) | DIFERENTE. Confirmar no teste de aceite |
| 17 | Abono familiar na CNPS | fora (6275%, 6276% No) `588:919-920` | fora (62760, 62762 No) `v4:879-880` | WTC `v4:914` | IGUAL na regra; códigos diferentes (ver C9) |
| 18 | Meal cash 6566% na CNPS | fora `588:929` | dentro (656%% Yes) `v4:908` | Art. 7 guia CNPS `v4:914` | DIFERENTE. A skill (esclarecimento 6, `hub:55`): isento até o limite legal. Resolver pela lei |
| 19 | Meal cash 6286% (628x) | IRPP, TFE e TAFP tributável `588:723`, `588:858`, `588:795`; CNPS e base NR fora por omissão (D2, D3) | só 62867 tributável no IRPP/TFE `v4:126`, `v4:1323`; resto da série 6286x fora; CNPS fora | WTC (código a código) | DIFERENTE. Divergência do hub `hub:93`, `hub:122` ("628x tributável", INCERTO) **ainda aberta** |
| 20 | Benefício em espécie: método | forfait: % × 58105, qualquer que seja o valor real `588:339`…`588:655` | MIN(valor real; % × remuneração em dinheiro), por conta-teto `v4:426`…`v4:757` | CGI Art. 46-III (LF 2019) « plafonnés » `v4:434` | DIFERENTE. Achado do hub `hub:104` ("9 forfaits") **ainda vale** |
| 21 | Benefício em espécie: percentuais | 20 / 10 / 15 (máx. 75.000/mês) / 5 / 4 / 4 / 4 / 3 / 2 `588:339-655` | iguais (comida: teto de 900.000/ano) `v4:253-261` | Art. 46-III `v4:269` | IGUAL |
| 22 | Benefício em espécie: base do % | 58105 inclui 65%%% (espécie a valor cheio) `588:97` | 58105 só dinheiro `v4:102-135` | Art. 46-I; CCG diz bruto (A2, R3) | DIFERENTE. Resolver pela lei (Art. 46-I ainda fala em "net des cotisations sociales") |
| 23 | Espécie na CNPS e na TFE | valor real (65%%% Yes) `588:931`, `588:864` | valor real `v4:905-910`, `v4:1340-1350` | Art. 7 guia CNPS; Art. 189 | IGUAL |
| 24 | Bolsa escolar (6274%, 6580%) | fora de IRPP, CNPS e TFE `588:721`, `588:736`, `588:918`, `588:855` | tributável e segurada (627%%, 658%% Yes) `v4:125`, `v4:910` | Art. 44, A3 | DIFERENTE. A skill (esclarecimento 4, `hub:53`) diz isenta. Resolver pela lei |
| 25 | Seguro-saúde (6563%) | fora de tudo `588:733`, `588:928`, `588:862` | tributável no IRPP (65630) `v4:822`; CNPS/TFE via 656%% | Art. 44, A3 | DIFERENTE. A skill: em grupo isento, individual tributável. Resolver pela lei |
| 26 | Diárias, passagem, mudança 2 | fora (6255%, 6256%, 6257%, 6557%, 6558%) `588:906-927` | fora (6255x, 6256x, 62570, 6557x, 6558x) `v4:868-890` | WTC | IGUAL |
| 27 | TFE: taxa | 7,5% `588:1397` | 7,5% `v4:1466` | Art. 190 `v4:1474` | IGUAL |
| 28 | TFE/TAFP: base | tira o transporte isento (58104) `588:841`, `588:778`; tira 6276%, mantém 6275% `588:856`; tira 62229 `588:846` | base ampla, sem tirar isenções do Art. 45 `v4:1296-1350` | Art. 189 `v4:1348` | DIFERENTE. A skill (esclarecimento 4, `hub:53`) diz base do IRPP. Divergência do `estado:16` **ainda vale**. Resolver pela lei |
| 29 | TAFP: taxa e arredondamento | 1,2%; base truncada a 1.000; imposto ao 10 mais próximo `588:772`, `588:1358` | igual `v4:1381`, `v4:1507` | Art. 178; Art. 177 (CCG) `v4:1433`, `v4:1515`; A7 | IGUAL |
| 30 | Redução da TFE/TAFP | só isenção total da TFE (58206 = 1) `580:10`, `588:1391`; sem 50%; TAFP sem redução | 0 / 100 / 50% na TFE **e** na TAFP `v4:19`, `v4:1466`, `v4:1507` | CGI Art. 158; LF 2024 art. 6–7 | FALTA NO DEV (50% e TAFP) |
| 31 | Limite de reporte 58106 e taxa total 58131 | 60.000/mês, piso = teto `588:31`; 58131 = 20 `588:1037` | igual `v4:170`, `v4:993` | relatórios (DAS, Récapitulatif); A15, A16 | IGUAL |
| 32 | Multas por atraso (IRPP normal, forfait, aprendizagem, CNPS) e crédito da TAFP por despesa de formação | notionals 64550–64554 `580:18-26` | não tem | — | FALTA NO NOSSO. Resolver pela lei (artigos fora do material) |
| 33 | Despesas profissionais (30%, `hub:74`) / ajuda de custo 15% (Art. 45-2°) | não tem | não tem (A4) | Art. 45-2° | FALTA NOS DOIS. Resolver pela lei |
| 34 | Taxa de segurança alimentar 400 FCFA/mês | não tem | não tem (A8) | LF 2024 art. 21–23 | FALTA NOS DOIS. Resolver pela lei |

### B2) Configuração do motor (Dev/Config; ver `fronteiras.md`)

| # | Tema | Dev (588) | Nosso v4 | Situação |
|---|---|---|---|---|
| C1 | Pares contábeis da CNPS | EE 3,5 → 6020/2550 (conta de despesa do empregador); ER 7,5 → 2610/2551 (desconto do empregado) `588:1032-1033`, `jul:1805`, `jul:1823` | EE → 2610/2551; PFM → 6020/2550 `v4:988`, `v4:990` | DIFERENTE. Parece troca no Dev; o próprio `580:67` lista na ordem do v4. As specs 005/006/007 mapeiam ao contrário (R13). **Prioridade** |
| C2 | Flags de ramo da CNPS (58202–58204) | não tem | tem `v4:15-17` | FALTA NO DEV (ligado aos itens 12 e A6) |
| C3 | `retro_` | não usa | usa onde há piso, teto ou tabela (A11) | FALTA NO DEV |
| C4 | Limite que depende de outro valor | MIN() na fórmula (`588:220`, `588:299`) | regulação própria + conta-teto (9148014/015, `v4:211-261`) | DIFERENTE (A10: não testado no motor) |
| C5 | Contas | iguais: 58105, 58008, 58104, 58108, 58120–58128, 58130, 58131, 58550, 58552, 58563, 58534, 58592, 58106. Só do Dev: 58103, 58107, 58100, 58101, 58110–58112 | só do v4: 58109, 58113, 58141, 58142, 58152, 58161–58169, 58171, 58172 | DIFERENTE (numeração interna; as contas que os relatórios leem coincidem) |
| C6 | Meses do jovem graduado (58205) | CEIL(YEARS_BETWEEN × 12) `580:8` | FLOOR(DAYS_BETWEEN / 30,4375) + 1 `v4:18` | DIFERENTE (pode dar 1 mês de diferença no limite dos 60) |
| C7 | Campos de HR | `$hr.employee_type`, `$hr.number_of_dependents`, `$legal_entity_hr.tfe_holiday_flag` `580:4-12` | `$hr.residency_status`, `$hr.number_of_dependent_children`, `$legal_entity_hr.tfe_tafp_relief` + novos (58207, 58210) `v4:14-22` | DIFERENTE |
| C8 | Matrizes | séries inteiras (621%%…629%%, 65%%%) | código a código conforme o WTC (confirmado 16/10) | DIFERENTE |
| C9 | Gross-up `_$$` | CNPS, IRPP residente e NR `588:1003`, `588:1251`, `588:1290` | mesmas três `v4:976`, `v4:1158`, `v4:1243` | IGUAL |
| C10 | Método do IRPP | anualiza (×período) → tabela `_monthly` → divide `588:1158`, `588:1241` | tabela anual dividida pelo período (`retro_simple_tax`) `v4:1112` | DIFERENTE no método; mesmo resultado num mês normal |
| C11 | Arredondamento da TFE | nenhum `588:1397` | FLOOR(x+0,5) `v4:1466` | DIFERENTE |
| C12 | Base do limite de transporte | 6210% (inclui 62104/62105) `588:187` | 58109 = 62100–62103, 62109 `v4:63-67` | DIFERENTE |
| C13 | Doc × configuração do próprio Dev | 6 pontos (tabela A2) | — | Perguntar ao Ram qual vale |

### Contagem
- **Regra estatutária (34 temas):** 15 IGUAL · 14 DIFERENTE · 2 FALTA NO DEV · 1 FALTA NO NOSSO · 2 FALTA NOS DOIS.
- **Configuração (13 temas):** 1 IGUAL · 9 DIFERENTE · 2 FALTA NO DEV · 1 inconsistência interna do Dev (6 pontos).

### Divergências já conhecidas do hub: ainda valem?
| Divergência | Ainda vale? |
|---|---|
| Teto de 5.000 por dependente (`hub:92`) | Sim: o Dev mantém (`588:259`) |
| Meal cash 628x tributável (`hub:93`) | Sim e continua incerta: o Dev tributa no IRPP; o v4 só tributa 62867 |
| Transporte 30% (`hub:94`) | Não é mais divergência entre Dev e nós: os dois aplicam 30% |
| Piso CNPS fixo (`hub:95`) | Os dois aplicam; ponto novo: CNPS sobre o piso em mês sem salário (item 16) |
| 9 forfaits sobre 58105 (`hub:104`) | Sim (item 20), e a base 58105 do Dev inclui espécie (item 22) |
| Teto do Art. 47 na 9148181 (`hub:123`) | Sim (item 8) |
| Pares da CNPS trocados (CONFERENCIA v4) | Sim (C1); já estava assim em julho |

---

## Bloco de prova
- **Pedido → resposta:** (A) julho × atual → seção A (sem mudança, com o diff campo a campo) + A2 (doc × config); (B) atual × v4 por tema → B1 (34 temas estatutários, com valor dos dois lados e o artigo que o v4 cita) e B2 (13 temas de motor); divergências do hub reconferidas na tabela final; (C) nenhum lado foi dado como certo: onde o material não traz a lei, ficou "resolver pela lei".
- **Fontes:** os 9 `.md` do export do Ram (`x/`), `td.json` de julho (Drive), `SKILL.md`, `ASSUMPTIONS.md`, `RESEARCH_GAPS.md`, `CONFERENCIA.md` do v4, `paises/Chade.md` e `frentes/chade/estado.md`. Nenhuma lei foi lida nesta tarefa: os artigos citados são os que o v4 e a skill citam.
- **Teste:** diff mecânico das 31 regulações (`588` × `jul`): 0 diferenças; diff das páginas de base 581–587 × matrizes do 588: 6 pontos (A2). Linhas conferidas com grep.
- **Confiança:** 95% na seção A e nos valores de cada lado. As classificações "DIFERENTE" que dependem do significado do código (itens 7, 17, 19, 24–26) precisam do WTC para fechar; o lado certo de cada divergência depende da lei.

## Quem mexeu
| Data | Frente | O quê |
|---|---|---|
| 2026-10-30 | chade | comparação criada (julho × atual; atual × v4) |

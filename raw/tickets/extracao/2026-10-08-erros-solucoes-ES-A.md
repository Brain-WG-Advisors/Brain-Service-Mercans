# Erros e soluções: Espanha, Seguridade Social / afiliação / integrações (grupo ES-A)

- **Grupo:** ES-A (Espanha: Fichero de Bases SLD, AFI/TrabajadoresTramos, AFI Outbound, CRA, confirmação de relatório AFI, notificações SILTRA, checklist de handover)
- **Data da análise:** 2026-10-08
- **Nota:** Análise de erros e soluções; complementa a extração factual de 2026-10-02 (`2026-10-02-tickets-ES-A.md`).
- **Arquivos lidos** (`raw/tickets/txt-utf8/`, todos lidos por inteiro; PDFs não foram necessários, nenhum .txt estava vazio):
  - SR-79: `18`, `30`, `39`, `44`, `54`, `61`, `87`, `103` (exportações de 2026-08-12, 08-21, 09-02, 09-04, 09-09, 09-11, 09-25, 10-08)
  - SR-80: `45`, `56`, `65` (2026-09-04, 09-09, 09-14)
  - SR-432: `79`, `85`, `104` (2026-09-22, 09-28, 10-08)
  - SR-81: `42` (2026-09-04)
  - HRBS-12839: `09` (2026-08-08)
  - HRBS-14528: `92` (2026-09-28)
  - CT-4321: `64` (2026-09-14)
- **Também consultados:** `raw/tickets/extracao/2026-10-02-tickets-ES-A.md`, `correcoes.md`, `mercans-pipeline/shared/country_failure_log.md` (F1 a F47).
- **Convenções:** datas com `~` são derivadas de "X days/months ago" a partir da data de exportação de cada snapshot (±1 dia, ±1 mês para "months ago"). Os snapshots antigos de SR-79 são subconjuntos do mais recente (conferido por diferença de vocabulário); o número do snapshot em que um comentário aparece pela primeira vez serve de limite para a data. Sem dados pessoais de empregados (NAF, IDs de empregado, CCC e IDs de entidade de teste foram omitidos). Papéis: Wallisson Gomes = Research Analyst (RA, nós); Lily Li = Business Analyst (BA); Drew Õispuu = Developer; Illya Virchenko e Katrin Rudi = Integration/alocação [INCERTO: papéis inferidos]; Gulnaaz = fornece amostras A3 (cliente KGS) [INCERTO].

---

## SR-79 — Spec do Fichero de Bases (SLD): mais de 12 rodadas de revisão até produção e novo requisito L03 de bônus

- **País / Cliente / Tipo / Prioridade:** Espanha / nenhum cliente (testes em entidade "Spain Reports Testing") / spec de Statutory Report (ES-BASES-001, XML enviado à TGSS via SILTRA) / Major
- **Snapshots lidos:** 18, 30, 39, 44, 54, 61, 87, 103 (2026-08-12 a 2026-10-08)
- **Estado no último snapshot (2026-10-08):** State "In Review"; Phase "Deployed To Production" (desde ~2026-09-17); Assignee Wallisson; due 31 Jan 2026 (vencida). Ainda há três perguntas abertas (ver final). Criado há 9 meses (~jan/2026).
- **Linha do tempo (rodadas de revisão):**
  - **R0 ~mar/2026 (Lily):** a spec usa os mesmos option mappers de base code e settlement type do AFI; pede conferir se as mudanças do AFI se aplicam. Mapeamento pronto exceto base code/amount. Pergunta se Authorized User ID = `$legal_entity_hr.red_authorization_code` ou "TGSS SILTRA Authorized User ID". Três ciclos de queries em roxo (colunas V, aba "Field Options"); Wallisson responde "queries reverted/reverted" sem registrar conteúdo no ticket.
  - **R1 ~mar-abr:** Lily pede confirmação de (1) base codes da indenização e (2) gatilho de população. Também diz que o desalinhamento de campos/cabeçalhos da spec deve ser corrigido pelo RA, não pelo BA (o mesmo ocorre na spec do M190, primeiros dois campos). Wallisson: 58197 (Prorated Severance Taxable) vai só no base code 701; 58198 (Exempt) não é reportado; gatilho = valor > 0, sem registros zerados. A tabela da resposta ainda mostrava 58197 → CRA 0054/I e 58198 → 0054/E (superada, ver SR-81).
  - **R2 ~abr (Illya):** exige na spec que o nome do arquivo e `referenciaExterna` sejam únicos entre todas as Legal Entities (rastreio de status da submissão). Lily acrescenta.
  - **R3 ~jul (v2.1):** Lily: coluna "AFI Field(s) Referenced" adicionada, novas queries na coluna X, seções DATOS LIQUIDACIÓN/DATOS MES/DATO DEL TRAMO sem campos sob o cabeçalho, pergunta onde se usa `IndicadorObligatoriedad (B/P)`. Wallisson acha por conta própria dois erros que ninguém perguntou (Control Date; 5 fórmulas de Ano e 1 de Mês com campo-fonte errado), responde com notas-ponteiro em vez de reorganizar; Lily rejeita ("reorg, confunde o dev"); Wallisson reorganiza fisicamente na ordem do schema oficial e atualiza ~40 referências "same as row X" (2 já apontavam errado). B/P explicado como gate por Codigo sobre o registro inteiro (Type + Code + Amount saem juntos).
  - **R4 ~jul:** Lily nota que a coluna V só cita L00/L02/L03 enquanto o DD tem mais tipos (lista de 14 códigos). Wallisson: tipos RETRO (L13, L90, L91, L92, L93, V03, V90) usam o mecanismo MesLiquidativo como L03; CURRENT = L00/L02; C02/C03/C90/C91 (colegios concertados) fora; tabela de 14 códigos acrescentada na Field Options (linha 133, para não deslocar o logo); Rectification Indicator omitido nos 14 tipos.
  - **R5 ~início de ago (antes de 08-12; Drew + Lily):** Drew (Dev) acha (1) 500 e 509 se sobrepõem (full-time em IT pago delegado entra nos dois e a base 58151 sai duas vezes), (2) `'BAS' + MMyyyy` tem 9 caracteres (limite 8) e não é único entre LEs, (3) os tipos retro não são testáveis porque nenhum campo HR guarda o período corrigido. Lily indica que os tipos retro ficam em `$legal_entity_hr.tgss_bases_settlement_type::key` e reporta que o CCC sai como zeros no XML. Wallisson (spec v2.3): 509 reescrito com wage types específicos, C-563 acrescentado (mapeado a 79415/79416), ReferenciaExterna = versão do Dev (últimos 4 do CCC + MMyy), CCC zerado = bug do Dev (mapeamento não chega ao XML), C-663 e WT 79012 deixados em aberto "sem chute".
  - **R6 ~08-12 a 08-21 (v2.4):** Lily propõe fórmulas de 509/500/563 e pede incluir o 563 na spec. Wallisson cruza com o WTC V4.4 e remove 79006/79007/79029/79030/79032 (códigos "Unit", contagem de dias), troca por Payouts 79429/79430/79432, remove 79417 (pago pela empresa) e 79406/79407 (BCCC = Yes, tratamento padrão no 500). Conjunto final do 509: 79418, 79419, 79420, 79421, 79423, 79424, 79429, 79430, 79432. Drew corrige o CCC (relatório lia snapshot de masterdata vazio) e implementa v2.4. Teste L00 aprovado pela Lily. Teste L03: Lily lista 5 falhas (PeriodoDesde/Hasta, FechaControl ausente, MesLiquidativo, datas de tramo, Contribution Base Amount com valor do período corrente em vez da diferença retro); Drew esclarece que falta campo para o mês a corrigir.
  - **R7 ~08-21 a 09-02:** Drew pergunta se vários meses retro geram vários Liquidacion ou arquivos. Wallisson: uma única Liquidacion com um bloco LiquidacionMes por mês corrigido (base: erro R9532 do manual TGSS impede repetir o mesmo mês; R9622/R9693 tratam liquidaciones de mais de um mês como normal). Gatilho a corrigir no Dev: loop em LiquidacionMes.
  - **R8 ~09-02 (Gulnaaz/A3 + análise assistida por IA):** Lily compara a spec com três amostras reais A3 (L03, L00+L13, L00) e lista 7 achados. Wallisson resolve: escopo de 10 tipos; Tipo e Código independentes; C/H/I = Concepto/Horas/Indicador; (1) hardcode `SolicitudRecepcionRNT = S` removido; (2) 497/498/499 = tramos 1/2/3 do solidarity surcharge (só primeiro tramo); (3) indicador 51 acrescentado; (4) 603 reetiquetado com tabela de pareamentos; (5) escopo do 509 validado contra o WTC; (6) lógica de datas do L03 confirmada; (7) "501→58554, 502→58558 corrigidos (estavam trocados)", demais códigos confirmados. Conflito apontado: 502 do manual oficial = "Other Overtime" × 502 da spec = "Common contingencies – Part-time".
  - **R9 ~09-04 (queries da Lily):** 563 mapeia 58151 com SUM(79415;79416)>0 ou a própria soma? 663? 601 exclui part-time? 79415/79416/79417 entram na condição de 500/509? Faltam base codes H e I na Field Options? Wallisson (respondido até 09-09): 58151 é o valor reportado e a SUM só abre o gate (pareamento IDC 21); 663 = 58151 com SUM(79412)>0 (79411, dia 1, excluído); 601 cobre full e part-time (H01 acompanha); 500/509 já corretos; Tipo I completo, Tipo H com 4 códigos acrescentados, mapeamento em aberto (não está no WTC nem no DD; `part_time_hours_per_week` falta no DD embora registrado como acrescentado); 604 "provável fantasma", não apagado.
  - **R10 ~09-08/09 (Lily):** a v2.4 anexada não reflete as mudanças feitas na spec linkada na descrição (ex.: 497/498/499). Wallisson consolida tudo no arquivo único da descrição ("ES-BASES-001_FicheroBases_Spec", sem sufixo de versão).
  - **R11 ~09-09 a 09-11 (horas e indicadores):** H01 → `$63958.amount`; H02 aplicável mas sem WT no WTC, sempre com o novo base code 537; H03/H04/H06 e H05 sem WT/campo no produto (gap de produto). Lily pede campos no DD; Wallisson (Spain DD v3.12): código de horas "01" (Bases.xsd v2.0.2: Codigo minLength 2/maxLength 3); 8 campos novos no DD (H02-H06, `software_vendor_code_registered_with_tgss`, `process_syntax_version_number`, `reason_for_l03_submission` com option mapper de 5 valores); 537 → 58151 (BCCC) porque horas complementares são horas ordinárias (art. 12.5 ET); indicadores 51/52/54 definidos; settlement type NÃO depende de seleção única de `tgss_bases_settlement_type`, cada tipo dispara por bloco/tramo; L13 exclusivo de desligado com férias pagas, usando os base codes que normalmente se aplicam.
  - **R12 ~09-11 (Lily + Wallisson):** Lily confirma que `tgss_bases_settlement_type` não deve ser campo de LE e pede condições exatas por tipo (a descrição da Field Options "não é clara nem precisa"); apresenta tabela de gatilhos com perguntas de escopo e quatro regras transversais. Wallisson reescreve L90/L91/L92/V03/V90 com a redação oficial da "Tabla de Tipos de Liquidación" (Manual de Usuario SLD, ago/2025), acrescenta nuance en-plazo/fuera-de-plazo ao L02, citação ao L93; V90 tem dois gatilhos alternativos (o primeiro foi perdido e achado em releitura). Regras transversais confirmadas: MarcaBorrado só para C00/C02/C03/C13/C90/C91/L03/L90; FechaControl só para L03/C03.
  - **R13 ~09-14 (Drew):** implementa tipo por gatilho por bloco, remove RNT, TipoDato C/H/I, mudanças da Field Options. Só L00 testável; pede à BA montar casos de teste (retro e L13) e confirma 563 = SUM(79415;79416) como na célula E145 (diz que Wallisson tinha dito 58151 gated) e 501/602 lendo 58554. ~09-16: teste L13 não apareceu no arquivo; Drew pede gerar do ciclo principal de fevereiro; passou. ~09-17: aceite e deploy em produção.
  - **R14 ~09-24 (Lily):** pede acrescentar 2 pay elements ao gatilho do L13; ~09-26 Drew: L13 agora usa 79450 + 79401 + 79452 como gatilho (com o flag de desligado) e como base, em acceptance e produção.
  - **R15 ~09-25 (decisão de escopo):** Lily pergunta se os tipos além de L00/L03/L13 estão em escopo ("segundo o consultor espanhol Raul não são usados"). Wallisson: L02, L90, L91, L92, L93, V03, V90 fora de escopo (confirmado na call do dia); só L00, L03, L13.
  - **R16 ~09-30 a 10-01 (novo requisito L03 de bônus, 4212x):** Lily acrescenta gatilho L03 para os pay elements 4212% (42120-42124; base code 500, ou 509 quando vale a condição E30): um bloco L03 por mês de acréscimo entre data inicial e final de cada entrada, valor = o valor armazenado. Drew levanta 6 dúvidas (quais elementos; como os valores chegam à folha; quantos meses para trás, o L03 atual cobre 3 meses mas o exemplo tem até 14; outros base codes; combinar com retro normal; entidade de teste). Respostas da Lily: 42120-42124 (WTC V4.6), datas início/fim de cada entrada funcionam como período retro, 500/509 só (por confirmação de Wallisson), blocos separados do retro normal, teste em ESP03. ~10-01 Drew: lógica 4212x em acceptance, testada só com dados fictícios (3 meses), pede entrada real e faz 2 perguntas (valor integral por mês ou rateado; sempre 500 porque o relatório não vê a situação de IT dos meses passados).
  - **R17 2026-10-08 (Lily, ~3 h antes do snapshot):** o elemento raiz `Bases` do XML gerado não tem namespace nem schemaLocation (as amostras A3 têm); propõe `<Bases xmlns:xsi=... xmlns="http://www.seg-social.es/creta/esquemas/V130/Bases" xsi:schemaLocation="... Bases.xsd">` e pede confirmação a Wallisson. Sem resposta no snapshot.
- **Problema relatado:** definição do mapeamento de produto do Fichero de Bases (base codes, settlement types, ReferenciaExterna, FechaControl, horas e indicadores) alinhada ao AFI e ao CRA, e geração de XML aceito pela TGSS. Os erros surgiram em três fontes: perguntas da BA na planilha, bugs/limites achados pelo Dev em teste e comparação com amostras reais A3.
- **Erro identificado** (artefato: Report Spec ES-BASES-001 e option mappers, salvo indicação; todos nossos, exceto onde marcado):
  1. Control Date tratado como flag de "late filing" (é a data de pagamento do salário, só L03); 5 fórmulas de Ano e 1 de Mês com campo-fonte errado (v2.1).
  2. 509 com flag genérico 58235 (qualquer licença, inclusive pago delegado) sobrepondo o 500; depois 79006/79007/79029/79030/79032 eram códigos "Unit"; 79417 pago pelo empregador; 79406/79407 em 509 indevidamente (v2.3 e v2.4). Falha de sincronização spec x WTC.
  3. C-563 (pago delegado IT, origem contingência comum) ausente, obrigatório junto ao 500; C-663 sem mapeamento (depois = 58151 com SUM(79412)>0).
  4. ReferenciaExterna `'BAS' + MMyyyy` com 9 caracteres e não único (limite do campo 1-8; requisito de unicidade de Illya).
  5. `SolicitudRecepcionRNT` obrigatório com hardcode "S" (ausente em arquivos reais).
  6. 497/498/499 (solidarity surcharge) usados em todos os arquivos A3 mas inexistentes na spec; indicador 51 ausente.
  7. 603 descrito como "AT/EP part-time"; é código de pareamentos de IT (500+603; 500+603+563; 500+603+663; 509+603).
  8. 501/502 trocados (leitura provável 501→58554, 502→58558 [INCERTO]); conflito de significado do 502 (oficial "Other Overtime" × spec "Common contingencies – Part-time").
  9. L02 documentado como "Error correction settlement" (é Complementaria por salarios de tramitación); descrições de L90/L91/L92/V03/V90 imprecisas; L01 existia como opção (não existe).
  10. Settlement type modelado como seleção única de legal entity (`tgss_bases_settlement_type`); a BA também chegou a afirmar isso e o Dev esperou esse campo; o correto é tipo por gatilho por bloco.
  11. L03 multi-mês: template com uma Liquidacion única; correto: um LiquidacionMes por mês.
  12. Código de horas "1" (correto "01", XSD exige comprimento mínimo 2).
  13. Seções vazias e campos fora de ordem na planilha (desalinhamento de cabeçalhos).
  14. `part_time_hours_per_week` registrado como acrescentado ao DD mas ausente (afirmação de conclusão sem verificação).
  15. Resposta nossa sobre 563 inconsistente (58151 gated em ~09-04 x "Formula unchanged: SUM(79415, 79416)" em v2.4); Dev pediu confirmação, sem resposta registrada.
  16. Root element `Bases` sem namespace/schemaLocation (Report Spec/gerador; descoberto contra amostras A3, 2026-10-08).
  17. Não é erro de spec: CCC saindo zerado (bug do Dev, relatório lia snapshot de masterdata vazio); L03/L13 não testáveis por falta de dados na entidade de teste.
  18. Divergência de versão do WTC citado: "V4.3" (resposta 663 e Drew), "V4.4" (cruzamento do 509), "V4.6" (link da Lily para 4212x); 4212x não existe no V4.3 nem na entidade de teste.
- **Causa raiz:**
  - Itens 1, 8, 9, 13: spec construída sem releitura contra o manual TGSS e o schema; o RA descobriu o erro 1 sozinho na revisão de v2.1, ou seja, a primeira versão foi entregue sem auditoria de campo-fonte (construção do artefato).
  - Item 2 e 3: spec escrita a partir de um flag genérico e dos wage types por memória, sem cruzar com o WTC vigente; correção só veio quando o Dev notou a sobreposição (sincronização entre artefatos, spec x WTC).
  - Itens 4, 12: limite de comprimento/enum do schema não aplicado ao padrão proposto (construção).
  - Itens 5, 6, 7: spec nunca foi comparada com arquivos reais; só a amostra A3 e a conferência do BA revelaram. 497-499 "sem documentação em lugar nenhum" (nem na referência oficial TGSS): a fonte oficial não cobria os códigos usados na prática (fonte legal/oficial incompleta).
  - Item 10: premissa de produto (BA e RA) de que o tipo vem de campo da LE; a geração real mistura tipos no mesmo arquivo (design).
  - Itens 14, 15, 18: controle de versões e de afirmações de conclusão frouxo; várias versões paralelas (v2.4 x arquivo linkado), a BA reclamou duas vezes de desencontro entre arquivos.
  - Item 16: o schema location não estava na spec; achado só ao comparar o XML gerado com as amostras reais [INCERTO: se a spec traz o root element].
- **Solução aplicada:**
  - Correções 1 a 12: feitas por Wallisson nas versões v2.1 (2026-07), v2.3 (início de agosto), v2.4 (~agosto 12-21) e no arquivo único "ES-BASES-001_FicheroBases_Spec" (~09-08 em diante, sem sufixo de versão); base: manual TGSS (erros R9532, R9622, R9693; Tabla de Tipos de Liquidación, Manual de Usuario SLD, ago/2025), Bases.xsd v2.0.2 (mar/2024), referência TGSS Codigos_Fichero_de_bases, art. 12.5 ET, WTC V4.4.
  - Spain DD v3.12 (~09-10) com 8 campos novos (H02-H06 etc.).
  - Dev (Drew): ~09-14 implementação por gatilho; ~09-16 aceite; ~09-17 produção; ~09-26 L13 com 79450+79401+79452 em produção; ~10-01 4212x em acceptance.
  - Decisão de escopo ~09-25: só L00, L03, L13.
  - CCC zerado corrigido pelo Dev (~início de ago).
  - Item 16 e 15, 14: não resolvidos no último snapshot.
- **O que não aconteceu / ficou aberto:**
  - Resposta de Wallisson sobre o namespace/schemaLocation do root `Bases` (R17).
  - Respostas às 2 perguntas finais do Dev sobre 4212x (valor integral por mês x rateio; sempre 500) e dados reais de teste (ESP03 sem 4212x). Sem fonte legal no ticket para o tratamento do bônus plurianual em L03; Lily afirma que "Wallisson confirmou só 500/509" (confirmação não aparece no ticket).
  - 563 (SUM x 58151 gated) e 501/602 lendo 58554: sem confirmação registrada; Dev implementou por conta.
  - H02-H06, 537, wage types: gaps de produto, sem WT no WTC; `part_time_hours_per_week` ausente no DD; 604 "provável fantasma" sem decisão.
  - Teste real de L03 retro com dados completos; limite de 3 meses retro do L03 atual x 12-14 meses exigidos pelo 4212x ("precisa de retrabalho", sem resposta se foi feito).
  - Spec e DD não registram que L02/L90-L93/V03/V90 saíram do escopo em ~09-25 [INCERTO: a spec pode ainda listar 10 tipos].
  - C-663 depende do WT 79012 (acidente de trabalho): decisão final ligada a 79412 foi dada em R9, não a 79012.
- **Tipo de erro:** T1 (L02/L03 e descrições de settlement types), T2 (509/500/563/663 e flags de base), T3 (códigos de base 497-499, 501/502, 537, 603, 563), T4 (DD: campos de horas/ETI/`reason_for_l03_submission`; `part_time_hours_per_week`), T5 (ReferenciaExterna, código de horas, root element, FechaControl, layout de seções), T6 (escopo de settlement types: 10 → 3), T7 (fórmulas de Ano/Mês e L03 multi-mês, 4212x), T8 (v2.4 x arquivo linkado; WTC V4.3/V4.4/V4.6; DD v3.9/v3.12), T11 (queries da BA), T12 (497-499 sem fonte oficial).
- **Lição para o pipeline:**
  - **F1 (Option mapper mismatch DD x Specs):** settlement types spec x DD x AFI divergentes; escapou porque cada artefato foi montado separadamente e a conferência veio só da BA.
  - **F13 (Mutual exclusion rules undocumented):** a sobreposição 500/509 é exatamente uma exclusão mútua não documentada; teria sido pega por C16 se a condição estivesse escrita nos dois lados.
  - **F14 (Code prefix inconsistency with official source):** 501/502 trocados e 502 com dois significados; o check de código vs fonte oficial não existe para base codes TGSS.
  - **F27 e F45 (artefato não ressincronizado; versões):** v2.4 x arquivo linkado, WTC citado em três versões; 4212x não existe no WTC citado.
  - **F29 (correção unidirecional certificada como completa):** "part_time_hours_per_week registrado como acrescentado" sem existir no DD.
  - **F41 (pesquisa sem oráculo independente):** as amostras A3 foram o oráculo que achou RNT, 497-499, 51, 603, e agora o namespace; o pipeline deveria exigir diff contra amostra real/XSD antes da entrega.
  - **F2 (códigos fora de escopo vazaram):** 10 settlement types especificados, só 3 usados; consultor local deveria ter decidido o escopo antes.
  - **F20 (gaps de WTC):** H02-H06 e 537 sem WT.
  - **NOVO: Limites de campo e enums da spec não validados contra o XSD (comprimento de ReferenciaExterna, código de horas "01", elemento raiz com namespace).** Teria sido pego por um lint que leia o Bases.xsd e compare comprimento/enum/namespace de cada campo da spec e do XML de exemplo.
  - **NOVO: Gatilho de relatório depende de dado que o motor não tem** (período retro, mês de acréscimo, situação de IT em meses passados, 4212x só visível na folha de pagamento). Teria sido pego por um check de "viabilidade do dado" (cada regra de população precisa citar o campo-fonte e se ele existe no DD/WTC/folha corrente).

---

## SR-80 — Spec AFI / TrabalhadoresTramos (ES-AFI-001): confusão inbound x outbound e auditoria da coluna "read-only"

- **País / Cliente / Tipo / Prioridade:** Espanha / nenhum cliente / spec de Statutory Report (na prática arquivo inbound da TGSS) / Major
- **Snapshots lidos:** 45, 56, 65 (2026-09-04, 09-09, 09-14)
- **Estado no último snapshot (2026-09-14):** Open; Phase "Development Phase – Developer"; Assignee Lily Li (era Drew em 09-04 e Wallisson em 09-09); due 31 Jan 2026 (vencida). Não resolvido (alocação ao time de Integration em discussão).
- **Linha do tempo:**
  - ~mar/2026: Lily cobra queries roxas não respondidas ("Field Options") e pergunta se Authorized User ID é `red_authorization_code`; Wallisson "queries reverted"; mapeamento confirmado depois (em ~mai): `Autorizado` = `$legal_entity_hr.red_authorization_code` (código RED do operador SILTRA, não é API key).
  - ~mai: payroll operation pede quatro "relatórios" (MA/MB/MC/MG). Lily pergunta se são estatutários e se a spec AFI ainda é necessária e qual o fluxo de quem para quem. Wallisson: são tipos de transação de afiliação (Alta, Baja, Cambio de Contrato, Cambio de Grupo), eventos em tempo real de HR/onboarding, normalmente não gerados pelo payroll, fora desta spec. Fluxo: sem API HRB-TGSS, SILTRA é Java desktop com certificado SILCON, operador manual; ES-AFI-001 TrabajadoresTramos é "Fichero de Respuesta de la TGSS", não gerado pela HRB.
  - ~mai: Lily conclui que então a spec não seria necessária para product mapping. Wallisson: incorreto, o mapeamento vale também para arquivos recebidos (HRB lê DatosTramo/DatoSolicitado: 500, 501, 502, 601, 602, 701, 702, 703 e B/P). Lily traz documento de outra IA dizendo que não há parsing; Wallisson: parcialmente certo, conclusão errada. Check competitivo (SAP HCM RPC_PAYES_CRETA_FILES/Note 2223843, a3innuva/a3nom, Sage Despachos, miNomina, wincreta, JMD, Logicsoftware): spec fica em escopo.
  - ~mai: campos: já no DD (NAF, documento, grupo, contrato, ocupação, província, CCC, Autorizado, coeficiente part-time derivado); READ-ONLY (CAF, DiasCotizados, DatoSolicitado, Peculiaridades); novos propostos: CNAE, TRL ("Work Risk Type", AT/EP) e ColectivoEspecial.
  - ~jul: Lily adiciona coluna U "READ-ONLY from TGSS Response (Y/N)" e queries na coluna X. Wallisson: coluna U "majoritariamente errada"; corrige Control Date Y→N, Collection Date/Time N→Y, bloco InformacionAfiliacion N→Y, Contribution Base Amount N→Y; corrige 4 linhas com conteúdo errado (Epígrafe, TRL, CatProfesional, CausaBaseAdicional); sincroniza Settlement Type com os 14 códigos (L01 não existe); v1.1. Lily: se a maioria dos campos não é read-only e o AFI é inbound, o mapeamento a campos HR é impossível, correto? Wallisson (após conferir o schema oficial): fica N o que é do lado da solicitação e ecoado (Autorizado, ReferenciaExterna, Ccc, CccConcertado, Periodo, Tipo, Control Date); vira Y o resto; v2.0 com aba "Audit Closure Memo".
  - ~jul: Lily: opções de settlement type na spec são mais que as do DD. Wallisson atualiza o DD para v3.9.
  - ~ago: Lily pede a Katrin atribuir ao time de Integration ("inbound interface"); Illya pede a referência da pesquisa; Wallisson: ES-TGSS-INT-IN-001; Illya pede acesso, concedido.
  - ~09-02: Illya: "aparece como Outbound report e requer report config". ~09-04: Drew pesquisa e afirma SR-370 = outbound (SolicitudTrabajadoresTramos, já em acceptance; no snapshot 45 dizia "passou aceite em 12 Aug", editado depois para "already built in acceptance"), SR-80 = inbound; Wallisson confirma contra o Manual de Usuario TGSS SLD (ago/2025).
  - ~09-09: Lily pede comparar a amostra A3 `A26S0003.AFI` com a spec; Wallisson: confere com TrabajadoresTramos, nenhuma mudança. Drew pergunta o que se espera dele. Lily: "AFI é inbound ou outbound?". ~09-10 Wallisson responde apenas "inbound".
  - 2026-09-14: Wallisson reconfirma com nomes completos: "inbound" referia-se a TrabajadoresTramos, não a "AFI" como categoria.
- **Problema relatado:** não ficou claro o que é "AFI" nesta spec, quem gera, se é inbound, se precisa de product mapping e qual o time responsável (Integration x report config); mais tarde, qualidade do mapeamento da coluna "read-only".
- **Erro identificado:**
  - Nossa resposta de ~mai: TRL = "Work Risk Type, determina taxa AT/EP; escala 000/500/800" (inventada); correto: Tipo de Relación Laboral.
  - Spec ES-AFI-001 v1.1: Epígrafe (54) como RETA (é predecessor pré-2007 de Ocupación); CatProfesional (57) como código CNO geral (só mineração de carvão); CausaBaseAdicional (60) ligada a maternidade/IT (são 001/901/902/903: part-time concentrado/relevista/aposentadoria parcial); coluna U majoritariamente errada; Settlement Type com L01 inexistente; DD x spec com settlement types diferentes (DD v3.9 corrigiu).
  - Resposta nossa de ~mai que previa novos campos CNAE/TRL/ColectivoEspecial: TRL baseado em premissa errada; não consta se TRL/CNAE/ColectivoEspecial foram criados [INCERTO].
  - Resposta curta "inbound" (09-10) ao pedido de comparar a amostra: ambígua, gerou confusão no Dev e na BA (comunicação, nosso).
  - [INCERTO] A amostra `A26S0003.AFI` foi dada em SR-80 (~09-09) como compatível com TrabajadoresTramos (inbound) e em SR-432 (~09-25) usada para validar o AFI outbound (Mensaje de Afiliación, campo de entidade de pensão em 43/43 registros). O mesmo arquivo não pode ser os dois formatos; uma das duas validações está provavelmente errada.
  - Nome do ticket/spec ("AFI – Affiliation Message") não corresponde ao conteúdo (TrabajadoresTramos), enquanto a mensagem de afiliação real (MA/MB/MC/MG) virou SR-432.
- **Causa raiz:**
  - TRL, Epígrafe, CatProfesional, CausaBaseAdicional, coluna U: pesquisa sem leitura direta do schema oficial; conteúdo plausível não verificado (research, construção do artefato). O Audit Closure Memo mostra que foi achado por auditoria própria, após revisão da BA.
  - Confusão inbound/outbound: título do ticket com nome diferente do arquivo, três specs com sigla "AFI" (SR-80, SR-370, SR-432), mais uma amostra real de nome "AFI" que serve a ambos [INCERTO]; classificação inbound x outbound não registrada num lugar único (comunicação, design de escopo).
  - Alocação (Integration x report config): processo de roteamento de ticket, não artefato.
- **Solução aplicada:** spec v2.0 com Audit Closure Memo e coluna U corrigida (~jul); DD v3.9 (~jul); referência de interface inbound ES-TGSS-INT-IN-001 entregue a Integration (~ago); esclarecimento de SR-80 inbound / SR-370 outbound confirmado com o Manual TGSS (ago/2025) em 2026-09-04 e reconfirmado em 2026-09-14. Fonte para a regra de fluxo: Manual de Usuario TGSS SLD ago/2025 e documentação SILTRA (sem citação precisa de página).
- **O que não aconteceu / ficou aberto:** decisão sobre equipe responsável (Integration x report config): ticket com Lily; nenhum desenvolvimento do inbound comprovado (Drew: "o que se espera de mim?"); MA/MB/MC/MG: ticket separado nunca citado nesta spec (SR-432 aparece como candidato [INCERTO]); criação de CNAE/TRL/ColectivoEspecial; verificação do arquivo A26S0003.AFI (ver contradição acima); mapeamento (coluna W) de campos "N" sem uso na leitura; trecho final de uma resposta de Wallisson ("Show more") truncado no PDF, conteúdo não consta.
- **Tipo de erro:** T1 (TRL, CausaBaseAdicional, Epígrafe, CatProfesional), T4 (coluna U e campos HR, DD x spec), T6 (inbound x escopo: spec em escopo apesar de não gerada; MA/MB/MC/MG fora), T8 (DD v3.9 x spec; amostra), T10 (BA acreditou que spec não era necessária), T11 (perguntas de fluxo e escopo), T12 (afirmações sem fonte precisa).
- **Lição para o pipeline:**
  - **F8 (Inbound integration scoped out incorrectly):** o próprio F8 cita "Spain SR-80". Aqui o erro foi o inverso do F8 no começo (a spec foi quase retirada por ser inbound) e depois ruído de roteamento; o check C10 (classificar inbound/outbound com `product_mapping_required`) deveria ter registrado a classificação de cada um de SR-80, SR-370, SR-432 num único lugar.
  - **F33 e F41:** conteúdo "inventado" (escala 000/500/800) e nomes de campo sem verificação contra o schema; teria sido pego por oráculo independente (schema TGSS) por campo.
  - **F1:** settlement type spec x DD.
  - **NOVO: Colisão de nomes de spec/tickets (mesma sigla "AFI" para três artefatos: TrabajadoresTramos, SolicitudTrabajadoresTramos, Mensaje de Afiliación).** Check: o nome da spec no título do ticket deve ser igual ao nome oficial do arquivo TGSS e declarar direção (in/out).
  - **NOVO: Respostas curtas a perguntas de classificação.** Regra editorial: responder sempre com nome completo do arquivo e direção.

---

## SR-432 — Spec AFI Outbound (Mensaje de Afiliación): tradução, 77 campos novos no DD e premissas do Dev

- **País / Cliente / Tipo / Prioridade:** Espanha / nenhum cliente (amostra A3 do cliente KGS) / spec de Statutory Report outbound / Major
- **Snapshots lidos:** 79, 85, 104 (2026-09-22, 09-28, 10-08)
- **Estado no último snapshot (2026-10-08):** Open; Phase "Development Phase – Developer"; Assignee Wallisson; due 29 Jan 2027. Criado ~2026-09-14. Em aberto: 4 premissas do Dev aguardando resposta; 10 campos de DD ainda não criados na entidade de teste.
- **Linha do tempo:**
  - ~09-20 (Lily): quase todos os campos da coluna A da aba "AFI Spec" e a coluna "Field Explanation" estão em espanhol; pede inglês. ~09-21 Wallisson: "fixed".
  - ~09-22: Lily pede checar queries da coluna V; Wallisson "Done". Phase ainda "Development Phase – Developer" no snapshot 79, vira "Product Mapping Phase – Business Analyst" no 85 e volta a Developer no 104.
  - ~09-23: Lily: queries em vermelho; Wallisson responde na coluna W, atualiza o DD (Version Control 4.6) com campos novos e option mappers e avisa que respostas anteriores mudaram (Version Control 1.2 da spec): linhas 173-174, DAM.2150-2170 só se aplica ao Special System 32, não é o coeficiente de part-time da reunião.
  - ~09-25: a pedido de Gulnaaz, valida contra A3 `A26S0003.AFI`: campo de entidade de pensão (pos. 40-44) confirmado em 43/43; campo reservado (2420) com posição corrigida de 18-21/len 4 para 18-23/len 6 (erro de digitação do manual TGSS); spec atualizada.
  - ~09-28 (Lily): DD tem 77 campos novos no total, "têm que ser criados mesmo?". Wallisson responde ~09-28: 12 necessários agora (linhas 155, 156, 157, 159, 165, 166, 168, 169, 170, 174, 221, 224), 7 constantes (176, 183, 184, 185, 187, 192, 231, N ou S na 231) e 58 não necessários agora (situações específicas: subcontratação, baixa por doença, estágios, part-time concentrado).
  - ~09-29 (Lily): pede confirmar a coluna U (verde escuro); as colunas de comentário RA ainda citam campos removidos; option mappers de campos removidos continuam no DD; zeros x branco divergem da coluna Example; "vamos fechar o mapeamento na call hoje". Wallisson entrega spec Version Control 1.4 e DD Version Control 29-Set-26: 76 células da coluna U respondidas; 58 campos "Not needed for now"; 7 "hardcode N" (S na linha 148); segmentos OTD, DBA, DSC, DJD, PIT fora do arquivo; option mappers órfãos removidos (T-12, nacionalidade para código numérico TGSS, mantido). Regra zeros/brancos: numérico = zeros, texto = espaços (corrigiu linhas 18-23, 259, 285). Mudança: Collective Agreement Code volta ao DD, então 13 campos necessários (exigido pela TGSS desde nov/2018, Boletín Noticias RED 5/2018); datas em AAAAMMDD (coluna M dizia DDMMAAAA); Employer Field = N nos segmentos do trabalhador; prazo de baja = 6 dias (RD 643/2026). Linhas 145, 148, 158, 165, 166, 170, 176: coluna U ainda aponta para campos que o DD marca como "não criar"; coluna W dá o valor fixo. Lily: "Mapping done"; pede a Katrin atribuir ao Dev.
  - ~10-01 (Drew/"Brenet"): para testar com eventos reais faltam os campos no DD da entidade de teste (`tgss_affiliation_action`, `tgss_affiliation_action_date`, `untaken_holiday_end_date`, `saa_period_start_date`, `saa_period_end_date`, `saa_indicator`, `additional_affiliation_situation_type`, `worker_identification_document_type`, `pension_plan_managing_entity`, `collective_agreement_code`) e pede confirmar 4 premissas (abaixo). 2026-10-08: Lily repassa as 4 perguntas a Wallisson, adicionando que o DD de 14 dígitos para collective agreement code está errado (spec tem 3 dígitos) e pede checar se o option mapper de worker collective deve ir em `$hr.collective_agreement_code`.
- **Problema relatado:** spec em espanhol, queries de mapeamento, necessidade/criação de campos novos no DD, validação contra amostra real, e ambiguidades de população que o Dev não consegue decidir.
- **Erro identificado** (Report Spec "Spain AFI Outbound" e Spain DD):
  1. Spec entregue com nomes de campo e explicações em espanhol (coluna A, Field Explanation).
  2. Resposta da reunião: DAM.2150-2170 = coeficiente de part-time (só vale para Special System 32).
  3. Campo reservado 2420 com posição errada (reproduzia erro do manual TGSS).
  4. DD com 77 campos novos, a maioria desnecessária; resíduos de campos removidos nos comentários RA e nos option mappers.
  5. Ambiguidade zeros x brancos (comentários x coluna Example), formatos de data (coluna M em DDMMAAAA, correto AAAAMMDD), Employer Field, prazo de baja (3 dias na spec/resposta anterior, correto 6 dias, RD 643/2026) e retirada/readição de Collective Agreement Code [conforme `correcoes.md` linha de 2026-09-21 a 09-29, também ETI.160].
  6. FAB Worker Collective (pos. 30-32, 3 dígitos) mapeado ao collective agreement code de 14 dígitos (campo/comprimento do DD x spec).
  7. Nome do arquivo e ETI control reference exigem número sequencial (como A26S0003) que o sistema não gera; Dev propõe `'A' + yyMMdd + '0'`.
  8. Colunas U/W inconsistentes com o DD em 7 linhas após remoção de campos (ver acima); 7 constantes citadas com linhas diferentes em duas mensagens (231 x 148 para "S") [INCERTO: renumeração].
  9. [INCERTO] sobre a validação com A26S0003.AFI, mesma amostra usada em SR-80 como TrabajadoresTramos.
- **Causa raiz:** spec construída a partir do manual em espanhol sem tradução (construção); lista de campos do DD gerada por varredura completa do layout TGSS em vez de "o que o payroll tem" (design de DD, conflito com F26 e com a regra de escopo do DD); respostas da reunião não registradas na spec; manual TGSS com erro de digitação (fonte oficial incorreta); Dev encontra premissas porque a população por evento (MA/MB/MC/ASA/MSA/ESA) e regras de comprimento/nome de arquivo não foram escritas na spec (população condicional rasa); remoção de campos do DD sem varrer referências (sincronização entre artefatos); fase do ticket avançou para Developer antes de fechar mapeamento [INCERTO: processo].
- **Solução aplicada:** tradução (~09-21); DD Version Control 4.6 (~09-23) e depois 29-Set-26 (~09-29); spec Version Control 1.2 (~09-23) e 1.4 (~09-29); posição do 2420 corrigida (~09-25; fonte: amostra A3 + manual TGSS); Collective Agreement Code readicionado com base em Boletín Noticias RED 5/2018; baja = 6 dias com base em RD 643/2026; formato AAAAMMDD; regra zeros/espaços do TGSS; 7 constantes e 58 campos fora do escopo; segmentos OTD/DBA/DSC/DJD/PIT fora do arquivo. Não resolvido: as 4 premissas do Dev.
- **O que não aconteceu / ficou aberto:**
  - Respostas às 4 premissas do Dev (DOM/LDD só em MA; ODL em toda ação exceto MB; FCT em ASA/MSA/ESA e em MB com data de fim de férias; DAM data de início só em MA e MC; FAB Worker Collective = zeros ou 3 dígitos; nome de arquivo/ETI sem sequência).
  - Criação dos 10 campos no DD da entidade de teste; decisão sobre `$hr.collective_agreement_code` (14 dígitos x 3) e option mapper de worker collective.
  - Os 7 resíduos de coluna U x DD (linhas 145, 148, 158, 165, 166, 170, 176).
  - Segmentos OTD, DBA, DSC, DJD, PIT "fora por enquanto" (sem critério de quando entram).
  - Alocação do ticket depois de "Mapping done" (Phase foi e voltou).
  - Nenhum artefato diz como MA/MB/MC/MG foram classificados fora do payroll no SR-80 e agora entram aqui [INCERTO].
- **Tipo de erro:** T4 (campos do DD, 77 → 13, comprimento 3 x 14), T5 (idioma, zeros/brancos, formato de data, posição de 2420, nome de arquivo), T1 (prazo de baja 3 → 6 dias, RD 643/2026), T6 (segmentos fora; 58 campos), T8 (spec x DD, colunas U/W), T11 (perguntas), T12 (manual TGSS com typo; baja sem fonte de comparação no ticket).
- **Lição para o pipeline:**
  - **F1** (option mappers órfãos após remoção) e **F29** (correção unidirecional: campos removidos do DD mas referências em colunas L e W continuam): a limpeza foi aplicada a metade do par.
  - **F5** (Population Rules rasas): as 4 premissas são regras de população por evento que faltavam na spec.
  - **F26** (valor calculado/transacional no DD, e DD maior do que o necessário): a lista de 77 campos novos é varredura do layout, não escopo.
  - **F9** (colunas de spec): formato de data da coluna M errado.
  - **F41:** a amostra A3 como oráculo achou o typo do manual; deveria ser etapa padrão antes de entregar à BA.
  - **NOVO: Entrega de spec em idioma da fonte (espanhol).** Check de linguagem (colunas A e Field Explanation em inglês).
  - **NOVO: Campos do DD derivados de varredura exaustiva do layout oficial sem classificar "necessário agora / constante / situação específica".** Check: cada campo novo de DD deve ter justificativa de uso (população) na spec; a lista de "novos" não pode ultrapassar o que a spec referencia.

---

## SR-81 — Spec CRA (ES-CRA-001): resposta errada sobre 58197/58198 e bugs de teste

- **País / Cliente / Tipo / Prioridade:** Espanha / nenhum cliente (entidade de teste) / spec de Statutory Report / Major
- **Snapshots lidos:** 42 (2026-09-04)
- **Estado no último snapshot (2026-09-04):** State "In Review"; Phase "Final Review"; Assignee Wallisson; spent time 1d 2h 17m; due 31 Jan 2026 (vencida). Aceite passou ~08-18. Em aberto: revisão de posição/comprimento do registro ETI e External Reference.
- **Linha do tempo:**
  - ~mar/2026: Lily cobra queries roxas (linhas 2-10 e 81 em diante, aba "Pay Elements with CRA Code") e Authorized User ID; Wallisson "reverted" (2 vezes); Lily remove linhas 58100, 58105, 58111, 58129 (sem indicador).
  - ~abr: Lily cria o campo de LE "TGSS CRA Action Type" e defaults TGSS CRA Settlement Type = 00 e Action Type = A. Wallisson: opções do DD confirmadas contra a Field Options; "blank" é só comportamento padrão da TGSS (Alta), não opção do mapper; defaults corretos; DD completado (label, descrição, referência do mapper).
  - ~abr: Lily: Settlement Month/Year = período em que a remuneração foi paga, então a tabela 58197/58198 (prorateada) não deveria estar no CRA. Wallisson (errado): CRA reporta 58197 (0054/I) e 58198 (0054/E) no mês de desligamento; "a tabela está correta; ambas as coisas são necessárias".
  - ~abr-mai: Lily contesta de novo (58184, 58186, 58188 são os usados no CRA, todos indicador E e não sujeitos a SS). Wallisson reconhece o erro: 58197 e 58198 NÃO aparecem no CRA, são construções de cálculo só do BASES (L03 nos 12 meses anteriores; 58198 não é reportado).
  - ~jun: Drew reconstrói o CRA contra ES-CRA-001 v2.2 (arquivo de 70 caracteres, ETI/DDE/TRB/CRE, 548 WTs mapeados, valores em centavos), 5 execuções de teste; "Ready for compliance testing".
  - ~jul: Lily: indicador do código 0001 é sempre I? Remuneration Amount = soma por conceito agrupada por código + I/E? Wallisson: sim e sim.
  - ~ago: v2.3 (mudanças em rosa). Drew confirma chave `CONCAT('CRE_'; código; '_'; I/E)`, e que 10 códigos misturam I e E (0033, 0042, 0043, 0044, 0045, 0046, 0050, 0054, 0055, 0062).
  - ~08-07: Lily testa `CRA__202602.CRA`: valor mantido no sistema sai zero; Settlement Year (19-22) e Settlement Month (23-24) trocados. ~08-16 Drew corrige; ~08-18 aceite; sample gerado.
  - ~09-04: Lily pergunta (1) External Reference sempre em branco? (2) Remuneration Amount vem do salary card ou do payroll result (empregado desligado no meio do mês mostra 6000 do salary card, esperava 4000)? Pede a Wallisson conferir posição e comprimento do registro ETI contra a amostra A3 `tc260704.cra`. Drew (11 min antes do snapshot): External Reference vazio por design (linha 9 sem mapeamento; sugere `$payroll.reference_code`); valor vem do resultado da folha: 62100 = 4.000 (prorrateado) + 79450 = 2.000, ambos mapeados ao código 0001, somados em 6.000; igual ao salary card por coincidência.
- **Problema relatado:** quais pay elements entram no CRA (severance), configuração dos campos de LE, e correção de bugs de saída (zeros, ordem ano/mês).
- **Erro identificado:**
  - **Resposta anterior (nossa, ~abr/2026):** dissemos que o CRA reporta 58197 (0054/I) e 58198 (0054/E) no mês de desligamento e que a tabela devia ficar; também em SR-79 a tabela mostrava essa mesma associação. Correto: CRA = 58184, 58186, 58188 (todos 0054/E); 58197/58198 = só BASES. Artefatos afetados: Report Spec ES-CRA-001 (tabela de mapeamento) e a resposta de SR-79. Origem: nosso.
  - Dev: valor mantido no sistema saía zero; posições 19-22 e 23-24 trocadas (bugs de geração, do Dev, não de spec).
  - Pendente: posição/comprimento do ETI x amostra A3 (não verificado); External Reference vazio por design; expectativa da BA (payroll result) vs resultado (6.000, soma de 62100 e 79450 mapeados em 0001); se o payout de férias (79450) deve realmente ir ao 0001 não é discutido [INCERTO].
- **Causa raiz:** mistura de dois conceitos (evento de pagamento no CRA x mecanismo de atribuição de base no BASES/L03); wage types criados para o BASES (58197/58198) herdaram mapeamento CRA na planilha, sem nota de que são "construções de cálculo". Etapa: construção do artefato e comunicação da resposta (resposta dada sem reler o que cada WT representa). Os bugs do Dev: implementação.
- **Solução aplicada:** Wallisson corrigiu a resposta em ~abr-mai; tabela do CRA limpa (58197/58198 fora); spec v2.3 com agrupamento por código + I/E; Dev corrigiu zeros e inversão ano/mês (~08-16); aceite ~08-18; defaults 00 e A confirmados. Base: não há fonte oficial no ticket (ES-CRA-001 v2.2, Table 84 citada em `correcoes.md` para 62983).
- **O que não aconteceu / ficou aberto:** revisão de posição/comprimento do ETI com A3 (`tc260704.cra`); decisão sobre preencher External Reference com `$payroll.reference_code`; as colunas ETI do arquivo gerado; sem resposta de Wallisson no snapshot.
- **Tipo de erro:** T6 (58197/58198 dentro do CRA), T3 (mapeamento de WT a código CRA), T5 (posições de campo, External Reference), T7 (agrupamento), T8 (tabela CRA x BASES x SR-79), T10 (expectativa da BA x resultado de folha), T11.
- **Lição para o pipeline:**
  - **F29** (correção unidirecional): a correção foi feita no CRA mas a tabela antiga continuava em SR-79 (e no histórico); a correção deveria ser medida nos dois lados (CRA e BASES).
  - **F45** (consistência entre artefatos): o mesmo WT com tratamento diferente em duas specs.
  - **F41:** comparar com a amostra A3 antes de entregar (o ETI foi pedido só em 09-04).
  - **NOVO: Wage type de cálculo (58197/58198) mapeado em relatório de evento de pagamento.** Check: cada WT mapeado a um relatório precisa declarar "evento de pagamento x construção de cálculo" e só os do primeiro tipo entram em relatórios de pagamento (CRA).

---

## HRBS-12839 — Confirmação de qual relatório é o "AFI" (pedido de informação)

- **País / Cliente / Tipo / Prioridade:** Espanha / todos os clientes ES (amostra do cliente KGS) / Service Request (Tier 3, Compliance Support) / Medium
- **Snapshots lidos:** 09 (2026-08-08)
- **Estado no último snapshot:** Open; Phase Live/BAU; Assignee Wallisson; criado por Gulnaaz ~2026-08-06; atualizado por Afrin Fathima ~08-07 (sem conteúdo de comentário). Sem resposta nossa registrada.
- **Linha do tempo:** ~08-06 Gulnaaz relata que a Espanha tem um relatório AFI "com a contribuição de pensão" enviado à Seguridad Social via SILTRA; vê "ES: AFI – Affiliation Message (Social Security) - SPEC" em desenvolvimento e anexa um AFI real (`A26G0002`) do cliente KGS; pede confirmar se é o mesmo relatório. ~08-07 atualização de Afrin Fathima sem texto. Nenhum comentário.
- **Problema relatado:** confirmar se a spec em desenvolvimento ("AFI – Affiliation Message") corresponde ao arquivo AFI que o cliente envia (contribuição de pensão) via SILTRA.
- **Erro identificado:** nenhum (pedido de informação). Ambiguidade de nomenclatura: o ticket descreve o AFI como "relatório com a contribuição de pensão"; AFI é mensagem de afiliação, e SR-80 (nesta época em desenvolvimento) é na verdade TrabajadoresTramos. [INCERTO: a pergunta do cliente tem premissa misturada].
- **Causa raiz:** [INCERTO] nomes de spec e de arquivo TGSS (AFI) não alinhados (ver SR-80); inbound x outbound não declarado. Etapa: comunicação/design de escopo.
- **Solução aplicada:** não resolvido no último snapshot (sem resposta). O esclarecimento relevante veio depois, em SR-80 (2026-09-04 a 09-14: TrabajadoresTramos = inbound, SolicitudTrabajadoresTramos = outbound) e SR-432 (AFI Outbound, ~09-14 em diante), sem vínculo explícito com este ticket [INCERTO]. Este ticket figura como menção de entrada em SR-80.
- **O que não aconteceu / ficou aberto:** resposta a Gulnaaz; confirmação se `A26G0002` corresponde à spec SR-432 (AFI outbound) ou à SR-80; fechamento do ticket.
- **Tipo de erro:** T11.
- **Lição para o pipeline:** NOVO (ver SR-80): nome oficial e direção do arquivo no título da spec; sem isso o suporte não consegue responder "é o mesmo relatório?". Check: tabela arquivo oficial TGSS ↔ spec ↔ direção ↔ amostra A3 no SIR.

---

## HRBS-14528 — Integração das notificações do SILTRA ao HRB (pergunta/pedido de pesquisa)

- **País / Cliente / Tipo / Prioridade:** Espanha / KGS (Kidde Global Solutions) / Question/Inquiry (Tier 3) / Medium
- **Snapshots lidos:** 92 (2026-09-28)
- **Estado no último snapshot:** Open; Phase Live/BAU; Assignee Wallisson; Support Group alterado para Compliance Support (~09-17); criado por Mohamed Nabil ~09-12; "Resolution Time -11d" (prazo vencido); atualizado por Manju Shetija ~09-24 (sem texto).
- **Linha do tempo:**
  - ~09-12: Mohamed Nabil pede integrar ao HRB as notificações recebidas no SILTRA: não é resposta a arquivo enviado, vem da Seguridad Social avisando de ação necessária; há uma resposta e um PDF com link para o portal SS; pasta do SILTRA `C:\SILTRA\SVA\Msjrec`; amostras `.msj` e PDF. A lista da descrição tem itens numerados 2 e 4; itens 1 e 3 não constam.
  - ~09-16: Katrin Rudi diz que é preciso pesquisa do time de Manju antes de configurar.
  - ~09-17: o support engineer (stripathi) troca o grupo para Compliance e pede devolver à configuração depois da pesquisa.
  - ~09-24: atualização de Manju Shetija (sem comentário visível).
- **Problema relatado:** receber/refletir no HRB as notificações do SILTRA (arquivos `.msj` e PDF com link).
- **Erro identificado:** nenhum (pedido de informação/novo requisito de integração).
- **Causa raiz:** não aplicável. [INCERTO] Lacuna de escopo: a integração SILTRA inbound de notificações não está no SIR/escopo do serviço; os fluxos documentados em SR-80 (SILTRA manual, sem API) não cobrem o canal de notificações.
- **Solução aplicada:** não resolvido no último snapshot; encaminhado a Compliance para pesquisa. Sem pesquisa registrada.
- **O que não aconteceu / ficou aberto:** a pesquisa de compliance, a decisão se é escopo de pesquisa do serviço ou de Integration, o formato `.msj`, a retorno para configuração; prazo vencido.
- **Tipo de erro:** T11, T6 (escopo da integração: nosso x Integration).
- **Lição para o pipeline:** F8 (Inbound integration scoped out incorrectly): este é o mesmo risco, uma integração inbound que ninguém classificou; o check C10 deveria listar, no SIR, todos os canais inbound do SILTRA (TrabajadoresTramos, notificações `.msj`, erros de validação do Bases) com `product_mapping_required` explícito. Não escapou do F8 porque o pipeline original só cobriu os arquivos de relatório; as notificações nasceram em Live/BAU.

---

## CT-4321 — Handover Checklist da regulação Espanha (pedido de informação sobre payslip)

- **País / Cliente / Tipo / Prioridade:** Espanha / nenhum / Research task, Epic "Regulation Build" (projeto Compliance) / Normal
- **Snapshots lidos:** 64 (2026-09-14)
- **Estado no último snapshot:** Status "Ready for Design"; Designer assignee Lily Li; QA Assignees Mohit Jain, Ruchi Gupta; Sprint 42; início 12 Jan 2026 e due/design due 31 Dec 2025 (due anterior ao início, inconsistência no ticket); criado ~jan/2026; atualizado por Wallisson ~jun/2026.
- **Linha do tempo:**
  - Lista de entregáveis: Payroll Configuration Guide 2026, WTC, DD, Modelo 296/216/190/111, Fichero de Bases, AFI, CRA. Os critérios de aceite (ICE, Advisory, pesquisa própria, simulações de terceiro) terminam com "Above list is confirmed" (sem evidência dos testes no ticket).
  - ~mar/2026: Manju Shetija envia a spec do payslip da Espanha para desenvolvimento.
  - ~abr: Lily pergunta se só precisa mapear a aba "ES - Statutory Research" do payslip e como mapear os campos de master data. Wallisson: a aba mapeia pay elements (earnings, deduções, bases, contribuições do empregador: WT → seção do payslip, flags BCCC/BCCP/IRPF); os campos de master data (empresa, NIF, CCC, nome, NAF, grupo de cotização, contrato, taxa IRPF) estão no layout "España (EN)" como referência, já definidos no DD. Comentário seguinte da Lily foi apagado.
- **Problema relatado:** BA sem clareza sobre o que mapear no payslip (pay elements x master data).
- **Erro identificado:** nenhum (pedido de informação). Observações: (a) a lista do handover não inclui Payslip, SEPE CERTIFICA/LLAMAMIENTO, SR-370 nem AFI outbound, que apareceram depois; (b) o item AFI da lista (SR-80) entrou no handover sem a classificação inbound x outbound resolvida [INCERTO]; (c) critérios de aceite marcados como confirmados sem evidência no ticket.
- **Causa raiz:** não aplicável ao pedido; [INCERTO] para (a)-(c): handover por lista de artefatos congelada em janeiro e specs que cresceram depois.
- **Solução aplicada:** resposta de Wallisson (~abr/2026) delimitando as duas abas do payslip. Ticket ainda "Ready for Design".
- **O que não aconteceu / ficou aberto:** atualização da lista de handover; evidência das 4 confirmações (ICE, Advisory, pesquisa própria, simulações com software de terceiros); conflito de datas do ticket.
- **Tipo de erro:** T11 (T9 por contexto: payslip).
- **Lição para o pipeline:** F41 (pesquisa sem oráculo independente): o item "verificamos com software de terceiros" é marcado sem evidência; F45 (consistência de versões): a lista de handover não cita versões (WTC/DD) e a de specs ficou desatualizada. NOVO: o handover checklist deve citar versão vigente de cada artefato e anexar evidência dos critérios de aceite.

---

## Tabela-resumo

| ID | País | Tipo(s) | Artefato | Resolvido? | F-xx / NOVO |
|---|---|---|---|---|---|
| SR-79 | ES | T1, T2, T3, T4, T5, T6, T7, T8, T11, T12 | Report Spec ES-BASES-001 (v2.1/2.3/2.4/arquivo único), Field Options, DD v3.12, WTC V4.3/4.4/4.6 | Parcial: em produção desde ~2026-09-17; abertos: namespace do root `Bases`, 4212x, 563, 604, gaps H02-H06/537 | F1, F2, F13, F14, F20, F27, F29, F41, F45; NOVO (limites/enums vs XSD; gatilho sem dado-fonte) |
| SR-80 | ES | T1, T4, T6, T8, T10, T11, T12 | Report Spec ES-AFI-001 TrabajadoresTramos (v1.1→v2.0), DD v3.9 | Parcial: spec e DD corrigidos; alocação Integration x report config e verificação da amostra A3 abertas | F1, F8, F33, F41; NOVO (colisão do nome "AFI"; respostas curtas) |
| SR-432 | ES | T1, T4, T5, T6, T8, T11, T12 | Report Spec AFI Outbound (VC 1.2→1.4), DD (VC 4.6→29-Set-26) | Não: mapeamento fechado (09-29) mas 4 premissas do Dev e 10 campos de DD pendentes | F1, F5, F9, F26, F29, F41; NOVO (spec em espanhol; DD por varredura exaustiva) |
| SR-81 | ES | T3, T5, T6, T7, T8, T10, T11 | Report Spec ES-CRA-001 (v2.2→V2.3), DD (TGSS CRA Action/Settlement Type) | Parcial: em aceite (~08-18); ETI e External Reference abertos | F29, F41, F45; NOVO (WT de cálculo em relatório de pagamento) |
| HRBS-12839 | ES | T11 | Esclarecimento "AFI" (SR-80/SR-432) | Não (sem resposta registrada) | NOVO (nome oficial + direção no título da spec; ver SR-80) |
| HRBS-14528 | ES | T11, T6 | Integração de notificações SILTRA (.msj) | Não (encaminhado a Compliance, sem pesquisa registrada) | F8 |
| CT-4321 | ES | T11 (T9) | Handover Checklist; Payslip spec (aba Statutory Research) | Parcial: dúvida de payslip respondida; checklist sem evidências | F41, F45; NOVO (handover com versões e evidências) |

## Padrões recorrentes no grupo

- **Spec nunca confrontada com amostra real/XSD antes da entrega:** SR-79 (RNT hardcode, 497-499, indicador 51, 603, namespace), SR-432 (typo do manual no campo 2420, nome de arquivo sem sequência) e SR-81 (ETI x A3) só acharam o erro quando a BA ou o Dev rodaram contra amostras A3 ou geraram o XML (F41); falta o check de diff contra oráculo e de limites de campo do XSD (ReferenciaExterna, "01" x "1", 3 x 14 dígitos).
- **Spec x WTC x DD fora de sincronia:** 500/509 sobrepostos por flag genérico, wage types "Unit" no lugar de Payouts, WTC citado como V4.3/V4.4/V4.6, 4212x inexistente no WTC citado, DD v3.9/v3.12/4.6 e colunas U/W apontando para campos removidos (F1, F27, F29, F45).
- **Respostas nossas dadas sem reler a fonte:** TRL "Work Risk Type", 58197/58198 no CRA, DAM.2150-2170 como part-time, 563 com duas fórmulas, L02 "Error correction", resposta curta "inbound". Em todas o conteúdo era plausível, mas não verificado; a correção veio da BA ou do Dev (F33, F41).
- **Confusão de classificação de arquivo (inbound/outbound, nome "AFI"):** SR-80, SR-370, SR-432, HRBS-12839 e CT-4321 usam a mesma sigla para três arquivos TGSS; a mesma amostra A26S0003.AFI foi dada como TrabajadoresTramos e como Mensaje de Afiliación [INCERTO]. Relacionado a F8; falta uma tabela única arquivo TGSS, direção, spec, amostra.
- **Escopo definido tarde:** 10 settlement types especificados e depois reduzidos a 3 por decisão do consultor local (~09-25); 77 campos de DD reduzidos a 13; o BASES precisa de dados que o motor não tem (período retro, acréscimos 4212x, situação de IT de meses passados). O escopo e a viabilidade do dado deveriam ser decididos antes de escrever a regra de população (F2, F5, F26).
- **Gaps de produto tratados caso a caso:** H02-H06, 537 e C-663 sem wage type; `part_time_hours_per_week` dado como criado e inexistente; sem registro único de gaps (F20, F29, F30).
- **Múltiplos arquivos e versões paralelas:** v2.4 x arquivo linkado de SR-79, duas versões de DD em SR-432, spec e DD com datas diferentes de revisão; a BA reclamou duas vezes. Uma só cópia, citada pela versão, deve ser regra (F45).
- **Prazos e fechamento:** todos os specs com due date de jan/2026 continuam abertos em outubro/2026 (SR-79 em produção mas com revisões contínuas; HRBS-14528 com resolução vencida), indicando que a revisão da BA continua depois do deploy; não é um erro de conteúdo, mas indica que o gate de revisão não fecha antes da produção.

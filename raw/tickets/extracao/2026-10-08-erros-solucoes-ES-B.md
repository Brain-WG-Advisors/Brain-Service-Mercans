# Espanha (ES-B) — Erros e soluções: IRPF (M190, M111, M296), Employee Tax Certificate, SEPE Llamamiento, Finiquito, HRBS-13757 e CT-A-485

**Grupo:** ES-B (Espanha — IRPF, finiquito, SEPE, regulation specs)
**Data da análise:** 2026-10-08
**Nota:** Análise de erros e soluções; complementa a extração factual de 2026-10-02.

**Arquivos lidos (`raw/tickets/txt-utf8/`):**
- SR-83: `17`, `26`, `43`, `57`, `67`, `73`, `74` (todos "... Modelo 190 ... SPEC")
- SR-82: `40`
- SR-85: `41`
- SR-144: `55`
- SR-342: `60`
- SR-365: `07`
- HRBS-13757: `59`, `77`
- CT-A-485: `66` (o .txt está embaralhado; conferi com `pdftotext -layout` do PDF original em `youtrack_tickets\`)

Apoio: `correcoes.md`, `shared/country_failure_log.md` (F1–F47), `2026-10-02-tickets-ES-B.md`, `revisoes/2026-10-05-detalhe-ES.md`.

**Convenções.** As datas dos snapshots são a data de exportação impressa no cabeçalho do PDF, em formato M/D/AA. As datas dos eventos são aproximadas (≈), derivadas de "X days ago" contra a data do snapshot. Os comentários de Lily Li e Drew Õispuu têm o mesmo timestamp relativo nos vários snapshots, então a ordem dos eventos é confiável e as datas são aproximadas. Os anexos (imagens de erro do portal AEAT, .txt gerados, planilhas) não estão no texto: o conteúdo deles "não consta". Quando a nota fala em "o spec", é a planilha anexada ou a descrição da tarefa, que não vêm no texto.

---

## SR-83 — Modelo 190 (IRPF, declaração anual): spec ES-M190-001

- **País / Cliente / Tipo / Prioridade:** Espanha / Mercans, entidades de teste (Spain Reports Testing; a empresa de teste e o nº de linha "Spain all clients" aparecem em HRBS-13757) / Statutory Report SPEC (projeto SR, fase Final Review) / Major.
- **Snapshots lidos:** 17 (12/08/2026), 26 (19/08/2026), 43 (04/09/2026), 57 (10/09/2026), 67 (15/09/2026), 73 (16/09/2026 13:54), 74 (16/09/2026 18:53). Conferi o diff entre eles: os 17→26→43→57→67 acrescentam comentários; 73 e 74 só acrescentam o último comentário de Wallisson e o pedido de Lily.
- **Estado no último snapshot:** "In Review". Prazo 31/01/2026 (vencido). Na 4ª rodada de erro do portal AEAT, Wallisson corrigiu Family Situation, Contract Type e Descendants, e ficou "Still open": mapear 4 campos novos do DD para Descendants e investigar por que Year of Birth ainda falha nos registros 2/4. Lily pediu a explicação da lógica de Descendants e a remoção dos campos duplicados do DD.
- **Papéis:** Lily Li (Business Analyst, testa e pede mudanças), Wallisson (Research Analyst, dono do spec e do WTC), Drew Õispuu (Developer), Brenet (Developer, citado no campo).

### Linha do tempo (rodadas de revisão)

Rodada 0, ≈mar/2026 (comentários "5/6 meses atrás"):
- Lily pede revisar queries em roxo, coluna V da aba "Modelo 190 Spec", e duas queries novas sem resposta (campos *Incapacity In-Kind Value* e *Incapacity In-Kind Withholding*).
- Wallisson: "queries reverted". O conteúdo das respostas não consta.

Rodada 1, ≈jun/2026 (spec configurado em acceptance):
- Drew diz que o report está configurado em acceptance.
- Lily informa a atualização da aba "Income Type Clave and Subclave" (research update): pay elements 65816–65819 e 65830–65839 passam a AEAT Key L / Subkey 24; 65820–65829 e 65840–65849 saem do report (sem key/subkey). Drew confirma a implementação (L/24 para os dois primeiros blocos, "fully excluded" para os outros).

Rodada 2, ≈21/07/2026 (comentários de Lily "23 dias atrás" e Wallisson "22 dias atrás" no snapshot 17):
- Lily levanta 6 pontos: (1) WTC tem 3 wage types em Clave B, mas o spec dizia só A/L/G em escopo; (2) in-kind em Clave G = zero?; (3) campo "In-Kind + Ingreso a Cuenta – Clave G": zero ou branco?; (4) linha 71 sem informação; (5) *Incapacity Gross Amount* = só 79414+79415 (falta 79416?); (6) colunas V e W removidas, campos sem informação.
- Wallisson responde: Clave B entra no escopo (WTC correto: 79429, 79430, 79432 = B, pago directo INSS/mutua); in-kind não zera por padrão em Clave G; linha 71 já preenchida; **79416 (sickness leave 16–20 dias) estava faltando e foi adicionado** a *Incapacity Gross Amount* e *Incapacity Withholdings*; colunas V/W corrigidas. Anexa `ES-M190-001_Modelo190_Spec_v2.7`.
- Lily: **Wallisson atualizou o arquivo errado.** O v2.7 não tinha as edições dela; as edições foram feitas na descrição da tarefa ("Spain Modelo 190 ... SPEC"), que é a versão que o dev usa. Pediu para não apagar os destaques rosa dela (são as mudanças que o dev lê) e para marcar em outra cor os campos aplicáveis a Clave B.
- Wallisson (≈22/07): arquivo atualizado. BIK em Clave G = zero, mas como "derived-zero" e não hardcoded (in-kind é válido para G no AEAT; é zero só porque não existem pay elements de BIK para G). Os dois campos de incapacity in-kind (posições 282–321) são só Clave A. Coluna X (roxo) marca os campos aplicáveis a B: identificação, Income Type, 4 valores, bloco pessoal/familiar, Irregular Income Reduction, Deductible Expenses; B.01 apenas: Incapacity Gross/Withholdings; **não** se aplicam a B (vermelho): Contract Type, Contract End Date, Geographic Mobility, e os dois in-kind de incapacity.
- Lily (≈22–25/07): mais queries (colunas V, linhas 55–60, 57, 59, 60, 109). Pede nova coluna no WTC para marcar renda irregular; Wallisson: "adicionada na V4.2 do WTC" (≈25/07).
- Lily (≈26/07) pede a Drew atualizar linhas 25–29, 55–58, 60–61, 68–75, 82, 107.

Rodada 3, ≈04–10/08/2026:
- Drew (≈04/08), "Done and in Acceptance", mas com 4 pendências: (1) linhas 55–58 e 107 com posição "TBC" no spec; a linha 58 (union dues) não existe no WTC; (2) linha 27, Clave B: "YTD de 79429, 79430, 79432" está em Annual Withholdings, mas são payouts, então a lógica de retenção e a subclave de cada um não estão claras; (3) split de incapacity withholding (linhas 27/61); (4) linha 107 (Accrual Year): `wage_type.accrual_period_year` **não existe no modelo de dados** (mesma lacuna de SR-342); campo fica 0000.
- Lily (≈06/08): pede a posição exata de cada linha; pergunta se a linha 107 deve ser removida (as linhas 59/60 originais foram removidas na call); pergunta como calcular Annual Withholdings para B (a lógica atual de A/L/G usa 2552, 2592, 2593 e 58176 menos 79414/79415/79416).
- Wallisson (≈10/08): posições Row 57 = 171–183, Row 58 = 184–196, Row 107 = 148–151; linhas 55/56 não têm posição própria (excesso tributável é absorvido na linha 26, 82–94); **linha 107 permanece** (campo real, obrigatório quando aplicável; as referências às linhas 59/60 estavam velhas); **Row 27 Clave B = zeros** (pago directo, empregador não retém); **79429/79430 devem ser Subclave 03, não 01** (AEAT FAQ); **79432 não é Clave B** (é L/27, maternidade/paternidade isenta).
- Lily (≈12/08): pergunta a qual clave pertence a absorção nas linhas 55/56; aponta que **o WTC (79429/79430/79432) contradiz** o que Wallisson afirmou; pede atualização do WTC. Também testa a saída (M190__2026.txt) e aponta: Declaration ID de saída incorreto; dúvida sobre um trecho destacado; pede ao Drew implementar posições e Row 27 = zeros.

Rodada 4, ≈13–19/08/2026:
- Wallisson (≈13/08): linhas 55/56 → Row 26 **Clave A** (as duas linhas são escopo só de A). **WTC V4.4**: 79429 e 79430 Subclave 01 → 03; 79432 Clave B → Clave L, Subclave 01 → 27 (L.27 = prestaciones públicas por maternidad ou paternidad exentas; fonte citada: "AEAT Diseños Lógicos 190"). Destaque laranja.
- Drew (≈14/08): Declaration ID corrigido (1902026000001; sequencial 000001 até a entidade ser mantida); os caracteres destacados "19743" e "01" são dois campos cada (ano de nascimento 1974 + situação familiar 3; deficiência 0 + tipo de contrato 1), "ambos corretos"; posições 57/58/107 já estavam corretas; Row 27 B = zeros feito; **linhas 55/56 precisam de códigos de wage type Mercans**; linha 107 **ainda bloqueada** (sem fonte de dado). 79429/79430 produzem B/03; 79432 produz L/27.
- Lily (≈19/08): não achou no spec o campo "ano de nascimento 1974"; pergunta por que deficiência e tipo de contrato ficam adjacentes. Pede a Wallisson revalidar as posições ("as per Brenet, não batem") e fornecer a especificação governamental do M190.

Rodada 5, ≈19/08–04/09/2026 (posições):
- Wallisson (≈19/08): posições conferidas contra o Diseño Lógico 190 (ejercicio 2025; PDF anexado). A saída do Drew estava correta; **o erro era do spec**: Family Situation Key em 265 (correto 157), Disability Percentage em 333 (correto 167), Contract Type em 351–352 (correto 168), **Birth Year sem linha** (adicionado em 153–156). Linhas 57/58/107 (TBC) preenchidas: 171–183, 184–196, 148–151.
- Drew (≈20/08): "já implementado, pode testar".

Rodada 6, ≈03–15/09/2026 (rejeição no portal AEAT):
- Lily (≈03/09) compara a amostra do A3 (`Report190_...txt`, `M190__2025 HRB files.txt`) com o gerado (`M190__2026 (1).txt`) e relata erro no upload do portal (print; texto do erro não consta).
- Wallisson (≈04/09): causa: **posições do Type 2 ausentes do spec, geradas em branco onde a AEAT exige zero**. Adicionou: Owner of cohabitation unit pos. 169; Geomobility pos. 328→170 (corrigida); Payments in kind/incapacity/passed-on 309–321; Childhood Help Add-on 322; Withholdings estado/Navarra/Álava/Guipúzcoa/Vizcaya 323–387; Excesses shares start-ups 388; Entrepreneurship fund income 389; Key B.01 benefit types 390–394. **Removeu "White Type 2", campo "fabricado" nas posições 471–483, dentro da zona de brancos obrigatórios 395–500.**
- Lily (≈09/09): 5 campos novos sem mapeamento confirmado; pede exemplo de *Incapacity In-Kind Withholding Passed-On*. Lily também questiona dois registros extras no arquivo gerado.
- Drew (≈10/09): os dois registros extras são os tipos B/03 e L/27, cujo **filtro de wage type era cópia placeholder do filtro L/01**, porque a aba "Income Type Clave and Subclave" não atribuía WT a B/03 nem L/27. Assim, quem tem L/01 recebia também B/03 e L/27 com valores zero.
- Wallisson (≈10/09): "All 5 mappings confirmed correct", verificado contra o Diseños Lógicos 190 (ejercicio 2025), o texto BOE (Orden HAC/1431/2025) e a cópia v3.3 do Compliance. *Passed-On* (309–321) = valor do ingreso a cuenta (296–308) repassado ao empregado; é dependente direto do 296–308, que já é zero, portanto zero.
- Lily (≈11/09) pede corrigir: registros de outras claves não devem ser gerados com zeros se só existe L/01; atualizar linhas 7, 46, 48, 64–68, 82–86, 91, 93, 94.
- Drew (≈14/09): grupos B/03 e L/27 removidos (sem mapeamento no spec); linhas implementadas (pos 169=0; pos 170 = geographic mobility do campo HR; 309–321 zeros; 322=0; 323–387 zeros; 388, 389 = 0; 390–394 = 0; 395–500 brancos); base de severance em 471–483 removida; "trailing junk line" removida. Lily: "Acceptance testing passed".
- Lily (≈15/09): os campos **Contact Person Phone (12/13) e Contact Person Name** estavam mapeados no HRB diferente do spec (mesmo problema do M296); ela mesma alterou o mapeamento no sistema "por urgência" e pediu confirmação; Drew corrigiu e deployou em produção (≈15/09). Depois disso, o erro do portal **continuou** para Birth Year, Family Situation Key e Contract Type.
- Wallisson (≈15/09, editado): Year of Birth está correto; **Family Situation Key**: o spec tinha 6 códigos, a AEAT define 3, e o código 1 estava invertido (dizia "sem filhos", a AEAT exige filho dependente); corrigido para 3 códigos e escopo A, B (01/03/04/99), C. **Contract Type**: spec tinha 2 dígitos com códigos 01–05 (outra classificação); a AEAT usa 1 dígito, códigos 1–4, só Clave A; corrigido. **Descendants** (renomeado de "Number of Children"): estava em 266–267 (dentro de *Incapacity Income*); a posição real é 223–228, composto de 4 partes; "direct cause of error 21902B on Record 3". Mudanças em amarelo. Aberto: dev mapear 4 campos novos do DD (col V, linha 32) e investigar por que Year of Birth ainda falha nos registros 2/4 ("not a spec defect").
- Lily (≈16/09): pede a lógica de mapeamento de "Descendants (Mínimo por Descendientes)" e a remoção dos campos duplicados que já existem no DD.

Nota de HRBS-13757 que afeta o M190: Gulnaaz relata que **não residentes aparecem no arquivo do 190**. O texto não registra correção. Lily explica que Ejercicio = 2026 é rejeitado pela AEAT porque o exercício ainda não terminou (ver item 9 abaixo).

### Problema relatado
O report Modelo 190 gerado pelo HRB tinha divergências de mapeamento e de leiaute contra a especificação do AEAT (Diseño Lógico 190) e contra o A3, e era rejeitado no upload ao portal.

### Erros identificados (cada achado; artefato; responsável)
1. **Cobertura de Clave B** — spec dizia A/L/G em escopo; WTC já tinha B em 79429/79430/79432. Artefato: Report Spec M190 × WTC. Erro: **nosso** (sincronização). Correção: B incluída no escopo + coluna X marcando campos aplicáveis (≈22/07).
2. **79416 faltando** em *Incapacity Gross* e *Incapacity Withholdings*. Artefato: spec. Nosso. Adicionado ≈21/07.
3. **Afirmação de Wallisson de 21/07 (79429/79430 = B.01; 79432 = B)** estava errada. Correto: 79429 e 79430 = B/03; 79432 = L/27 (já registrado em `correcoes.md`, 2026-08-10). Artefato: WTC V4.2/4.3 e spec. Nosso (resposta anterior e WTC). Corrigido no WTC V4.4 (≈13/08).
4. **Arquivo errado atualizado** (v2.7 em vez da descrição da tarefa) — comunicação/versionamento. Nosso.
5. **Posições TBC / referências velhas** (linhas 55–58, 107; referências às linhas 59/60). Nosso (spec incompleto). Posições dadas ≈10/08; linha 107 mantida.
6. **Posições erradas e campos ausentes no spec** (Family Situation 265→157, Disability 333→167, Contract Type 351–352→168, Geomobility 328→170, Descendants 266–267→223–228, Birth Year sem linha → 153–156). Artefato: Report Spec ES-M190-001. Nosso. Corrigidos entre ≈19/08 e ≈15/09.
7. **Posições do Type 2 ausentes** (169, 309–394) geradas em branco onde a AEAT exige zero; **campo inventado "White Type 2" em 471–483** (zona de brancos). Nosso. Corrigido ≈04/09; implementação do dev ≈14/09.
8. **Códigos e domínios errados**: Family Situation com 6 códigos (AEAT: 3; código 1 invertido) e escopo errado; Contract Type com 2 dígitos/códigos 01–05 (AEAT: 1 dígito/códigos 1–4/Clave A). Nosso. Corrigido ≈15/09.
9. **Registros B/03 e L/27 gerados com zero** por filtro placeholder — origem: spec sem WT atribuído a B/03 e L/27. Nosso (lacuna do spec) + implementação (filtro copiado). Dev removeu os grupos ≈14/09 [INCERTO se, depois que 79429/79430 → B/03 e 79432 → L/27 ficaram no WTC V4.4, os grupos precisam ser recriados; Drew havia dito em ≈14/08 que eles produzem B/03 e L/27, e depois removeu os grupos sem WT "no spec"; contradição não resolvida no texto].
10. **Accrual Year (linha 107)** sem fonte de dados (`wage_type.accrual_period_year` inexistente no modelo de dados). Nosso/implementação (lacuna de DD). **Não resolvido** no último snapshot ("still blocked"; campo 0000).
11. **Linhas 55/56 sem códigos de wage type Mercans** para mapear. Aberto.
12. **Contact Person Phone/Name**: mapeamento no HRB diferente do spec. Implementação/DD × spec. Lily corrigiu no sistema; Drew corrigiu e deployou.
13. **Declaration ID** de saída incorreto. Implementação do dev; corrigido ≈14/08.
14. **Não residentes aparecem no 190** (HRBS-13757). Escopo/população. Não consta correção.
15. **Ejercicio = 2026 rejeitado** pelo portal: não é defeito de formato, é regra de negócio (não se declara exercício ainda em curso). Tipo: erro de teste, não do artefato (explicação de Lily).
16. **Year of Birth ainda falha nos registros 2/4** após as correções. Causa não identificada; Wallisson afirma que "não é defeito do spec". Aberto.

### Causa raiz
- Spec construído **sem validação campo a campo contra o Diseño Lógico oficial** (posições e domínios foram digitados/derivados e só viraram verdade quando o portal AEAT rejeitou). Evidências: 6 posições erradas, 1 campo ausente, Type 2 inteiro ausente, domínios inventados (6 códigos vs 3; 01–05 vs 1–4), campo "White Type 2" dentro da zona em branco. Etapa: construção do Report Spec (e ausência de QA contra o oráculo oficial). [INCERTO] se parte veio de herança do template de outro país; o ticket não diz.
- Divergência entre **WTC e spec** (Clave B, subclaves de 79429/79430/79432), por correções feitas num artefato sem varrer o outro (sincronização, etapa design/WTC).
- Spec com **"TBC" e referências obsoletas** em campos obrigatórios (linhas 55–58, 59/60, 107): perguntas abertas deixadas no artefato entregue ao dev.
- **Modelo de dados/DD** sem o campo de retro year e sem código de WT para as linhas 55/56: lacuna de DD (etapa design).
- Dois locais de verdade (arquivo anexado v2.7 × descrição da tarefa) → edições no lugar errado.

### Solução aplicada
Spec corrigido em várias iterações (ver rodadas) com base no Diseño Lógico 190 ejercicio 2025 e na Orden HAC/1431/2025 (BOE) citados por Wallisson; WTC V4.2 (coluna de renda irregular, ≈25/07) e V4.4 (≈13/08: 79429/79430 B/03; 79432 L/27); Drew implementou zeros do Type 2, geomobility, remoção de "White Type 2" e dos grupos B/03 e L/27, Declaration ID, e deploy em produção ≈15/09. Alguns itens dependem de anexos que não constam do texto (os links do Diseño Lógico, a FAQ da AEAT citada).

### O que não aconteceu / ficou aberto
- Year of Birth continua falhando nos registros 2/4 (causa desconhecida).
- Mapeamento dos 4 novos campos do DD para Descendants e remoção dos duplicados (pedido de Lily em 16/09, sem resposta).
- Linha 107 (Accrual Year) bloqueada por falta de fonte de dado; linhas 55/56 sem códigos de WT.
- Não residentes no 190: sem resposta.
- Retestar no portal AEAT com exercício encerrado (2025) ainda não consta.
- O destaque "Passed-On" foi confirmado só por Wallisson; sem teste com valor não zero.

### Tipo de erro
T5, T4, T6, T2, T8, T3, T12 (em menor grau), T10 (Ejercicio 2026), T11.

### Lição para o pipeline
- **F4 (Wrong file format)** pede o formato do arquivo; aqui o formato (TXT posicional) estava certo mas as **posições e domínios** não foram verificados. **F40/F41** (oráculo independente: validador da autoridade, C35) cobrem o princípio, mas só para DSN-Val; não existe checagem equivalente para o M190 (diff posição/len/domínio × Diseño Lógico AEAT). **NOVO: Posições/domínios de arquivo posicional sem diff contra o Diseño Lógico oficial.** Check que teria pegado: tabela campo/posição/len/domínio extraída do .xls oficial (ex. `dr111e16v18.xls` para o 111) comparada célula a célula com o spec (campo ausente, posição divergente, domínio divergente, bytes não cobertos).
- **F10 (Missing sub-forms)**: Type 2 incompleto. **F2 (Out-of-scope codes leaked)** e **F26**: o campo "White Type 2" é inventado, coberto parcialmente por F2.
- **F27 (Downstream artifact not re-synced after a source correction)** e **F7 (WTC wage type tax codes wrong)**: Clave B/subclaves WTC × spec. Escapou porque a correção foi feita em um só artefato.
- **F6 (Open queries unanswered)**: "TBC" no spec.
- **NOVO: Dados de teste com exercício em curso** (Ejercicio 2026) — teste de portal deve usar exercício encerrado, ou sandbox AEAT.
- **NOVO: Grupos de registro gerados com filtro placeholder copiado de outro grupo**; check: toda combinação clave/subclave precisa de ≥1 wage type no spec ou é removida.

---

## SR-82 — Modelo 111 (IRPF, retenções trimestral/mensal): spec

- **País / Cliente / Tipo / Prioridade:** Espanha / Mercans, entidade Spain Compliance QC / Statutory Report SPEC / Major.
- **Snapshots lidos:** 40 (03/09/2026).
- **Estado no último snapshot:** "In Review" (Final Review). O texto é cortado no pedido de Lily para remover opções do DD ("the highlighted options" não constam).
- **Linha do tempo:**
  - ≈jun/2026: Drew declara "Developer Testing — Complete", mas só testou o próprio arquivo contra o spec (campo a campo, ✅).
  - ≈jul/2026: Lily pede atualizar linhas 3 (filing trimestral), 24 e 27 (**substituir 57176 por 58176**), 29–31 (Clave G, adicionadas por Wallisson). Drew revisa e atualiza.
  - ≈ago/2026: Lily pergunta quais filers foram desenvolvidos (mensal ou trimestral) e se gerar em fevereiro acumula Jan+Fev; marca como crítica (≈12/08).
  - ≈14/08: Drew corrige a premissa: Jan+Fev acumulado não é período AEAT válido (mensal = só fevereiro; trimestral = 1T depois de março). O label do período estava certo, mas a janela de dados fixa em 2 períodos. Hoje um run de fevereiro gera arquivo "1T" com Jan+Fev. Propõe 2 variantes (Monthly 1 período; Quarterly 3 períodos), como no Gross to Net.
  - ≈17–19/08: Lily alinha mensal/trimestral; Drew implementa duas custom reports sobre a mesma configuração (`es-modelo-111-monthly`, `es-modelo-111-quarterly`) e dispensa o campo novo, usando `$report.label`. Regra de uso: o trimestral é um lookback a partir da folha de geração, então deve ser gerado do último mês do trimestre.
  - ≈20–21/08: acceptance passa para mensal e trimestral (NIF da empresa estava em branco no trimestral, corrigido por Drew).
  - ≈02/09: Lily relata erro no upload ao portal, compara com amostra do A3 e vê comprimento diferente em "company legal name"; pergunta o impacto do campo em M111/M190/M216/M296.
  - ≈02/09: Wallisson: causa raiz — *Company Legal Name* (12–51, 40 chars) eram dois campos AEAT fundidos, Denominación o Apellidos (23–82, 60) + Nombre (83–102, 20) = 80 chars. Os 40 chars faltantes deslocaram todas as posições seguintes, incluindo 6 campos de contagem de destinatários (9→8 chars) e o IBAN (24→34 chars). Tabela de campos refeita contra `dr111e16v18.xls` e conferida byte a byte contra A3 e HRB. Amendment Type: 538 (Declaración Complementaria, "X") e 539–551 (justificante anterior, 13 dígitos). Verificou M190 e M216: já corretos. **Spec v4**.
  - ≈03/09: Lily pede (1) preencher campos em branco nas colunas B–S (Tax Year, [05] In-Kind Value, [11], [17], [23], [26], [29] e "Reserved for Colegio Concertado"), (2) adicionar `$legal_entity_hr.previous_m111_justificante_number` ao DD, (3) remover opções de DD (o sistema só suporta original e substitutiva).
- **Problema relatado:** arquivo gerado rejeitado no portal AEAT; depois, ambiguidade de período (mensal vs trimestral).
- **Erro identificado:** (a) campo *Company Legal Name* modelado como 1 campo de 40 chars em vez de 2 campos AEAT, deslocando todas as posições; (b) códigos 57176 nas linhas 24/27 (corrigidos para 58176) [INCERTO se 57176 era erro de digitação]; (c) janela de dados fixa em 2 períodos (nem mensal nem trimestral) — implementação; (d) campos obrigatórios em branco nas colunas B–S e campo do DD ausente (Amendment). Responsável: nosso (spec) e implementação (janela).
- **Causa raiz:** o spec foi construído sem diff contra o leiaute oficial `dr111e16v18`; o dev testou "contra o spec", logo o erro do spec passou nos testes do dev (teste circular). Janela de dados: requisito de filing (mensal vs trimestral) não detalhado no spec inicial ("quarterly = 1T–4T, monthly = 01–12 por company.filer_type" estava no spec, mas não o período de dados).
- **Solução aplicada:** Spec v4 (tabela reconstruída), duas custom reports (mensal/trimestral) com o mesmo reportCode; NIF corrigido; Lily acompanha novos campos.
- **O que ficou aberto:** colunas B–S em branco; campo `previous_m111_justificante_number` no DD; remoção de opções do DD; reteste no portal após o spec v4; impacto do campo (mensal/trimestral) nos outros modelos não respondido no texto. HRBS-13757 mostra que, mesmo depois (≈10/09), o Modelo 111 mensal e trimestral continua com erro de upload no portal; Lily informa em ≈11/09 que as posições foram ajustadas e que o 111 pode ser gerado de novo, e Wallisson diz que o campo do spec está correto e precisa de olhar do dev.
- **Tipo de erro:** T5, T4, T7 (janela/período), T3 (57176 vs 58176).
- **Lição para o pipeline:** **F21 (Filing mechanics misunderstood: monthly/quarterly/annual)** — cobre a diferença de periodicidade, mas aqui a lacuna foi a **janela de dados**, não a existência do filing. **F4**/**NOVO** (diff do leiaute oficial, ver SR-83): o teste "contra o spec" do dev é circular; só o oráculo oficial pega. **F40/F41** princípio idêntico (validar contra autoridade).

---

## SR-85 — Modelo 296 (IRPF não residentes, resumo anual): spec

- **País / Cliente / Tipo / Prioridade:** Espanha / Mercans / Statutory Report SPEC (In Review, Final Review) / Major.
- **Snapshots lidos:** 41 (04/09/2026).
- **Estado no último snapshot:** "In Review". Lily compara o arquivo gerado com o A3 e os campos numéricos em branco; a resposta de Wallisson não consta.
- **Linha do tempo:**
  - ≈mar/2026: Lily pede revisar queries em roxo, coluna U, "M296 Spec"; Wallisson "queries reverted".
  - ≈mai/2026: Lily pede confirmar mudança v2.1 (remoção do 65815 da aba "Income Nature and Income Key"). Wallisson contesta: pelo WTC v3.3, 65815 (Benefit Earning) tem AEAT 296 Key 20 / Subkey 01 e sujeito a retenção 216. Lily: na cópia atual do WTC, 65815 não tem chave 296 (flexible remuneration). Wallisson (≈jun): **estava usando a cópia de 30/04, onde 65815 ainda era Benefit Earning tributável; na V3.5 (mudança V3.4 de 07/05), 65815 virou Flexible Remuneration — Non-Taxable SS Subject**, sem mapeamento 296; remoção correta.
  - ≈jun/2026: Drew configura o report em acceptance.
  - ≈jul/2026: Lily pede atualizar linha 41 (**substituir 57176 por 58176**) e remover da aba "Income Nature and Income Key" 62149, 6298x, 79417–79424, 79429, 79430, 79432.
  - ≈ago/2026: Drew diz que as duas mudanças "não afetam a config" (Tax Withheld é soma direta de 2582; a população é por status de não residente), e encontra uma lacuna real: **Tax Residence Country (T2-040) em branco**, mapeado para o país de residência (ISO2). Campos condicionais ainda em branco: Recipient Address (T2-031), Birth Date/Place (T2-038/039), NIF no país de residência (T2-037). Os campos T2-025 a T2-030 (securities/loan) em branco são corretos.
  - ≈ago/2026: Lily testa e aponta: (1) % de retenção com 58205 = 3 saindo 2400, deveria ser 1900; (2) Repercuted Tax Payments: espaços ou zeros (spec: zeros); (3) Birth Date não aparece; (4) Tax Withheld não pode ser igual a 2582 (separar caixa e in-kind, como no Withholding Base Amount); (5) campos condicionais são exigidos pelo spec.
  - Drew: quatro dos cinco corrigidos; sobre o Tax Withheld, o spec divide proporcionalmente 2582 entre caixa (58176) e espécie (58177); destinatário com os dois precisa de 2 registros Type 2 (D e E). Confirma estrutura com Lily (≈06/08) e Wallisson (≈06/08): "your understanding is correct".
  - ≈12–14/08: Drew resolve; pede empregado de teste com caixa e in-kind e pergunta se o flag 58218 = 1 e o filtro `$hr.tax_residency_status` devem concordar (Lily: sim).
  - ≈18/08: Lily testa (ESG03 com BIK, ESG04 só caixa): (1) registro `00000004` não deveria existir; (2) o total de recipients (primeira linha) deveria ser 3 (conta de Type 2). Drew corrige (≈19/08); Lily: "Acceptance testing passed" (≈20/08).
  - ≈04/09: Lily compara com o A3 e relata erros de upload ao portal. Tabela de diferenças: Recipient Mediator Flag (134), Issuer Code Type (135), Declarant Payment Type (148), Accrual Tax Year (171–174), Loan Start Date (175–182), Loan Maturity Date (183–190), Lender Remuneration, Compensations (191–202), 203–214, Guarantees (215–226) saíam em branco e a AEAT exige zero (erros E020180/190/210/250/260/270/280/290/300); Record ID/Sequential (77–84) formato diferente do A3 ("00000001" vs "1" + espaços). Lily já alterou o mapeamento para zeros e pergunta se há mais campos e qual o formato correto do Record ID. A resposta de Wallisson não consta no snapshot.
- **Problema relatado:** divergência de retenção, estrutura Type 2 por natureza e rejeição no portal por campos numéricos em branco.
- **Erro identificado:** (a) taxa de retenção de não residente incorreta (2400 vs 1900) — spec/WTC (taxa por 58205) ou implementação [INCERTO qual; o texto não diz]; (b) Type 2 por natureza D/E exigida e não prevista na implementação inicial; (c) campos numéricos que a AEAT exige com zeros saíam em branco; (d) Tax Residence Country e campos condicionais em branco; (e) formato do Record ID divergente do A3; (f) nossa contestação da remoção do 65815 baseada em cópia desatualizada do WTC (resposta anterior nossa errada, já em `correcoes.md`); (g) o código de WT 58176/57176 trocado nas linhas.
- **Causa raiz:** spec e DD sem a regra "campo numérico nunca em branco" do leiaute AEAT; lacuna de leitura do spec sobre D/E; versão do WTC usada por Wallisson (30/04) não era a vigente (sincronização entre artefatos, etapa design/comunicação). Linha 41: Lily pediu 57176→58176 e Drew citou "58176→57176" (sentido oposto) no texto [INCERTO se foi erro de digitação em um dos dois].
- **Solução aplicada:** estrutura D/E implementada e aprovada em acceptance (≈20/08); zeros nos campos numéricos corrigidos por Lily no mapeamento (≈04/09); Tax Residence Country mapeado; remoção do 65815 aceita.
- **O que ficou aberto:** lista completa de campos a zerar; formato do Record ID; campos condicionais (endereço, nascimento, NIF no país de residência) dependem de decisão de mapeamento HR; retesto no portal. Em HRBS-13757, a rejeição do 296 foi atribuída por Lily ao exercício 2026 (ver abaixo) e por Wallisson a "spec confirmed correct, needs a Dev-side look".
- **Tipo de erro:** T5, T2 (taxa por tipo de não residente e 65815), T7 (split Tax Withheld), T8 (cópia de WTC antiga), T4.
- **Lição para o pipeline:** **F7** (códigos de tributação do WTC) e **F27** (artefato a jusante não ressincronizado) cobrem o 65815; escapou porque a decisão de Wallisson usou uma cópia local do WTC fora da versão vigente. **NOVO: Resposta a ticket baseada em cópia local do WTC não validada contra a versão vigente** (check: sempre citar a versão do WTC e conferir contra o arquivo vigente antes de contestar). **F4/NOVO** (diff do leiaute oficial: campos numéricos em branco vs zero-fill).

---

## SR-144 — SEPE Llamamiento (callback de fijo discontinuo): spec

- **País / Cliente / Tipo / Prioridade:** Espanha / Mercans, entidade de teste / Statutory Report SPEC (estado "Open", fase "Deployed To Production") / Major; prazo 28/02/2026.
- **Snapshots lidos:** 55 (09/09/2026).
- **Estado no último snapshot:** Open; em produção desde ≈08/09.
- **Linha do tempo:**
  - ≈jun/2026: Drew: pronto para teste em acceptance.
  - ≈jul/2026: Lily: pasta vazia ao baixar o report; "no mapping change required".
  - Drew: comportamento esperado — report orientado a evento; só gera arquivo quando `sepe_callback_start_date` cai no período (chamada de fijo discontinuo).
  - ≈ago/2026: Lily: acceptance passou (`SEPE_LLAMAMIENTO_B65685703_202602.xml`).
  - ≈08/09: Lily pede deploy; Drew deploya em produção.
  - ≈09/09: Lily compara com a amostra A3 (`L26S0001.XML`): o bloco `DATOS_USOLIBRE_EMPRESA` (A3: `E3|T079214|C389|F20250808`) não aparece no gerado. A explicação do campo no spec não é clara, então o sistema omite o bloco. Lily pergunta se é opcional e o que mapear. (A coluna "Status/ação sugerida" está truncada no texto.)
- **Problema relatado:** pasta vazia ao gerar; depois divergência com A3 (bloco ausente). Em HRBS-13757 (≈27/08), Gulnaaz relata "Unable to generate from HRB. No file being generated" para Llamamiento (provável mesma causa: nenhum empregado com data de chamada no período).
- **Erro identificado:** (1) A pasta vazia não foi erro (evento sem dado); mas a comunicação do usuário mostrou que o spec/relatório **não documenta o comportamento orientado a evento** [INCERTO: depende de o spec dizer isso; o texto não diz]. (2) **`DATOS_USOLIBRE_EMPRESA`**: spec ambíguo sobre o conteúdo; omissão pode causar rejeição [INCERTO se obrigatório; Lily pergunta, não consta resposta]. Responsável: nosso spec (explicação de campo pouco clara).
- **Causa raiz:** explicação do campo no spec insuficiente para mapear (regra de população/origem do dado ausente), com o dev omitindo o bloco; spec foi aprovado em acceptance e deployado antes de comparar com o arquivo real do A3 (a comparação com amostra só veio depois do deploy). Etapa: construção do spec/QA.
- **Solução aplicada:** nenhuma ainda para o bloco; o relatório foi deployado.
- **O que ficou aberto:** resposta de Wallisson sobre `DATOS_USOLIBRE_EMPRESA` (opcional? origem? mapeamento do valor `E3|T079214|C389|F20250808`); documentar o comportamento orientado a evento nas Population Rules; gerar arquivo de teste com dado de callback.
- **Tipo de erro:** T5, T11 (pasta vazia explicada), T4 (campo sem origem no DD).
- **Lição para o pipeline:** **F5 (Population Rules thin)** — evento/condição não documentados; **F9 (Thin spec column schema)** para a explicação do campo; escapou porque o aceite em acceptance não compara com amostra real do A3. **NOVO: Aceite/deploy antes de comparação com sample real da autoridade/legado** (check: não marcar "Passed" sem diff com arquivo oficial/legado).

---

## SR-342 — Employee Tax Certificate (Certificado de Retenciones): spec ES-CERT-001

- **País / Cliente / Tipo / Prioridade:** Espanha / Mercans / Statutory Report SPEC (In Review) / Major; prazo 31/08/2026.
- **Snapshots lidos:** 60 (11/09/2026).
- **Estado no último snapshot:** In Review; formato do PDF gerado difere do A3, sem resposta de Wallisson.
- **Linha do tempo:**
  - ≈jul/2026: Lily pede revisar queries na coluna V, "urgent"; Wallisson "reverted" (2×); "New 1" queries em vermelho.
  - ≈jul/2026: acordado criar novos pay elements para overpayment e original amount no WTC; Wallisson: "adicionado na V4.2 do WTC".
  - ≈ago/2026: Lily pede atribuir o desenvolvimento; "pending for a while".
  - ≈02/09: Drew: report em acceptance ("Spain Employee Tax Certificate").
  - ≈04/09: Lily pede **substituir 58176 por 58552 e 58177 por 58572** ("old codes should be replaced"); Drew atualiza.
  - ≈10/09: acceptance passou (`Certificado_Retenciones_ESP01_2026.pdf`).
  - ≈11/09: Lily compara com amostra A3: **os formatos são diferentes**; pede que as mudanças no spec sejam destacadas.
- **Problema relatado:** o PDF gerado não segue o formato do certificado do A3 (e de certificados reais da AEAT segundo HRBS-13757).
- **Erro identificado:** (a) códigos de wage type obsoletos (58176/58177) no spec; (b) layout do certificado diferente da amostra. Em HRBS-13757 (≈10/09), Gulnaaz relata "Annual Tax Certificate: Format does not match" com amostras de clientes; Wallisson (≈11/09): "format confirmed correct, verified against 5 real AEAT-issued certificates". Posição contraditória não resolvida: A3 × AEAT × HRB. Responsável: [INCERTO] — pode ser spec (nosso), ou diferença esperada A3 vs oficial.
- **Causa raiz:** códigos de WT mudaram depois do spec (58176/58177 → 58552/58572) sem varredura sistemática nas specs (sincronização entre artefatos). Formato: sem modelo oficial único; A3 usa um leiaute próprio [INCERTO].
- **Solução aplicada:** códigos substituídos por Drew (≈04/09); acceptance passou. Formato: não resolvido.
- **O que ficou aberto:** definir o leiaute correto (A3 vs oficial); campo `wage_type.accrual_period_year` (mesma lacuna de SR-83); Wallisson não respondeu ao pedido de Lily de 11/09.
- **Tipo de erro:** T3, T8, T5, T10 (formato A3 × oficial).
- **Lição para o pipeline:** **F27 (Downstream artifact not re-synced after a source correction)** e **F45 (cross-artifact consistency)**: nas outras specs do grupo, 58176/57176/58177 ainda aparecem (SR-82, SR-85), enquanto o CT-A-485 usa 58552/58572 nas linhas de não residente. **NOVO: Renomeação/retirada de código de WT sem varredura de todas as specs** (check: lista de códigos obsoletos do WTC contra todas as referências de specs e DD).

---

## SR-365 — Finiquito (ES-FINIQ-001): spec

- **País / Cliente / Tipo / Prioridade:** Espanha / Mercans / Statutory Report SPEC (In Review) / Major; prazo 31/08/2026; vinculado a HRBS-11970 ("Missing Finiquito Letter in Internal System").
- **Snapshots lidos:** 07 (07/08/2026).
- **Estado no último snapshot:** In Review; pergunta aberta sobre residente × não residente.
- **Linha do tempo:**
  - ≈21/07: Lily pede revisar queries (coluna W); Wallisson: "reverted"; aponta DD V3.9.
  - ≈21/07: novas queries em vermelho; Wallisson responde ≈22/07.
  - ≈31/07: Drew configura em acceptance; filtro de população: termination date de `$hr.sepe_last_day_worked`, com fallback para `$employee.last_working_date`, entre `period.begin_date` e `period.end_date` (mesma origem do SEPE CERTIFICA).
  - ≈03/08: Lily: acceptance feito; pergunta se vale o zero tax floor para empregado desligado (em fevereiro a taxa de IRPF era 0 porque a renda anual bruta ficou abaixo do piso).
  - ≈04/08: Wallisson: comportamento esperado. O desligamento (qualquer motivo, incluindo baja voluntaria) é gatilho de regularización (Art. 87.2.3º RIRPF); no finiquito, o valor anual comparado com o piso é recalculado para o acumulado real do ano. Se base menos mínimo pessoal ≤ 0, taxa 0 (Art. 86.1/87.3); sem correção retroativa (Art. 87.3); o piso de 2% do Art. 86.2 só vale para contratos de duração inferior a um ano, não para indefinido encerrado antes. (Sem links; "sem fonte no ticket" além dos artigos citados.)
  - ≈06/08: Lily: passou em acceptance (`Finiquito_ES__202602.pdf`); precisa da confirmação de Gulnaaz nas entidades dela.
  - ≈07/08: Lily: o spec não diz se o finiquito é só para residente ou também não residente.
- **Problema relatado:** taxa de IRPF 0 no finiquito de desligado (parecia defeito); escopo residente × não residente não definido.
- **Erro identificado:** nenhum quanto ao cálculo (pedido de informação, confirmado "not a defect"); **lacuna do spec** quanto a residentes/não residentes (T6) e a regra do piso zero para desligados não documentada no spec (mas consta no CCG segundo Lily: "em CCG compara com a renda anual bruta" — a leitura "annual gross" é ambígua para desligamento).
- **Causa raiz:** CCG/spec descrevem o piso zero comparado com a renda anual projetada, sem tratar o caso de recálculo no desligamento (comunicação/CCG); população do report não define a categoria fiscal. [INCERTO] se a explicação cabe no CCG.
- **Solução aplicada:** explicação de Wallisson (≈04/08); report aprovado em acceptance; a pergunta final (≈07/08) sem resposta no texto.
- **O que ficou aberto:** resposta residente/não residente; atualização do CCG/spec com a nota sobre o piso zero no desligamento; confirmação de Gulnaaz.
- **Tipo de erro:** T11, T6, T12 (artigos citados sem link no ticket).
- **Lição para o pipeline:** **F43 (Special populations not covered systematically)** — população especial (desligado, não residente) não coberta no spec; **F6** para pergunta aberta. Escapou por ser regra implícita no CCG. Check: a Population Rules de cada report declara explicitamente residente/não residente e desligados.

---

## HRBS-13757 — Spain Regulation: statutory report issues and testing feedback

- **País / Cliente / Tipo / Prioridade:** Espanha / "SPAIN all clients" (entidades de teste, incl. REF-04-261, Hermes Fund Managers Ireland Limited) / Incident (Tier 3) / Medium. Reporter Gulnaaz Parveen (HRBlizz Support), assignee Wallisson, Lily Li (compliance).
- **Snapshots lidos:** 59 (10/09/2026), 77 (18/09/2026). O 59 é subconjunto do 77 (comentários mais antigos); o 77 contém tudo e os comentários novos de ≈11/09 a ≈17/09.
- **Estado no último snapshot:** "Paused" (Pending on reporter).
- **Linha do tempo:**
  - ≈25/08: Gulnaaz abre com 4 itens: (1) SEPE CERTIFICA: schema XML não corresponde ao do site do SEPE (amostra A3 `C_20260724_23_004226`); (2) SEPE CONTRATA: upload OK no portal, aguardando confirmação; (3) SEPE LLAMAMIENTO: não gera arquivo (amostra A3 `L26G0001`); (4) SEPE PRORROGA: formato aparenta OK, enviado exemplo para validação.
  - ≈27/08: Gulnaaz: CERTIFICA ainda não busca os dados do representante legal; M216 trimestral e mensal OK; **M111 trimestral e mensal com o mesmo erro de upload**; M190: não residentes aparecem no arquivo, e o arquivo é rejeitado; M296 rejeitado.
  - ≈31/08: Lily explica M296 e M190: **o arquivo declara Ejercicio = 2026**, ano não encerrado; a AEAT rejeita (regra de negócio, "not a formatting bug"). Em CERTIFICA, `<Datos_Representante>` mostra os dados do representante legal na versão gerada por Lily. M111 e M190 em verificação.
  - ≈31/08: Gulnaaz pede (Fichero de Bases): muitos códigos sem mapeamento; quais settlement types podem ser combinados; nomear reports com "L" no início; escopo de settlement types (no A3 só L00, L13, L00+L13, L03); origem dos valores no L13. E pede conferir a lista CNO no CERTIFICA.
  - ≈31/08: Lily a Wallisson: recheck do spec de Fichero de Bases com a planilha `Codigoes Fichero de bases.xlsx`; CERTIFICA: código de profissão tem 7 dígitos no spec e 4 no DD, sem option mapper de CNO.
  - ≈01/09: Wallisson: L00 e L13 são independentes e podem coexistir; L03 só cobre períodos anteriores ao L00 corrente; **L01 não é código TGSS real** (sinalizado, não apagado); descrições de L02 e L03 estavam erradas e foram corrigidas contra o manual TGSS SLD; L13 (linha 135) já estava correto. CNO/CodProfesion: DD correto com 4 dígitos (CNO-11 e tabela T90); o **mapeamento passava o valor sem padding, mas o campo exige 7** — por isso o CNO válido 3123 foi rejeitado; corrigido com right-pad de zeros até 7. **Spec Fichero de Bases v2.5, CERTIFICA v1.1**.
  - ≈01/09: Lily: "in those two report tasks, no changes have been found". Wallisson: os dois foram atualizados a partir das versões do Drive; no CERTIFICA a correção do CodProfesion "já estava no arquivo (linha 30)"; adicionou uma aba Version Control; em Fichero de Bases reaplicou as correções L01/L02/L03 e preencheu retroativamente as entradas v2.3/v2.4 faltantes.
  - ≈02/09: Gulnaaz anexa os erros do M190 e M296 no portal (ainda ≈).
  - ≈04/09: Lily: padding do CNO resolvido (`SEPE_CERTIFICA_..._202602.xml`); M111: posições ajustadas (`..._02.111`, `..._1T.111`); **erro de exibição da taxa de IRPF no payslip resolvido** (deploy em produção no mesmo dia).
  - ≈10/09: Gulnaaz testa na entidade REF-04-261: **Model 111** (IBAN já atualizado no cadastro, ainda erro no portal), **Model 296** (erro no portal), **Annual Tax Certificate** (formato não corresponde; anexa 5 amostras de certificados de clientes e a amostra correta).
  - ≈11/09: Lily: no 296 o ano enviado foi 2026? Esse é o motivo da rejeição. Wallisson: M111 "field spec already confirmed correct (position, length, checksum)", precisa de olhar do Dev; M296 idem; Annual Tax Certificate "verified against 5 real AEAT-issued certificates".
  - ≈15/09: Gulnaaz: ainda erros no M190 (prints, REF-04-261). Lily atribui a Wallisson.
  - ≈17/09: Gulnaaz relata feedback do cliente: **o payslip da Espanha não traz campos obrigatórios por lei**: código de contrato (ex.: 100) e data de antiguidade.
- **Problema relatado:** relatórios estatutários espanhóis falhando em testes de upload (SEPE, 111, 190, 296), certificado anual em formato diferente, e payslip sem campos obrigatórios.
- **Erros identificados** (feedback de teste = erros):
  1. **CERTIFICA — CodProfesion sem padding de 7 dígitos** (mapeamento do spec): rejeição de CNO 3123. Artefato: Report Spec SEPE CERTIFICA. Nosso. Corrigido (v1.1).
  2. **Fichero de Bases (SR-79)** — códigos de settlement (L01 inexistente; descrições L02/L03 erradas); muitos códigos sem mapeamento. Artefato: Report Spec Fichero de Bases v2.3→v2.5. Nosso. Parcialmente corrigido; pedido de revisão completa sem fechamento de todos os códigos.
  3. **CERTIFICA — dados do representante legal** não buscados (entidade acceptance). Lily diz que gera `<Datos_Representante>` corretamente. Causa não identificada no texto. [INCERTO se era dado do cadastro].
  4. **SEPE LLAMAMIENTO sem arquivo**: ver SR-144 (evento sem dado). Não consta resposta nesta ticket.
  5. **Modelo 111**: erro de upload (mensal e trimestral) — o texto aponta posições (corrigidas por Lily, ≈04/09) mas o erro persiste em ≈10/09 com IBAN atualizado; Wallisson afirma que o spec está correto e pede olhar do dev. Responsável: **não determinado**.
  6. **Modelo 190**: não residentes no arquivo; rejeição. Responsável: spec/escopo + implementação. Não resolvido; ver SR-83.
  7. **Modelo 296**: rejeição por **Ejercicio 2026**; Lily atribui ao ano do teste; segue a discussão dos campos numéricos em branco (SR-85). Responsável: teste (input), mais spec (zeros).
  8. **Annual Tax Certificate**: formato difere das amostras; Wallisson afirma conformidade com 5 certificados da AEAT. Responsável: [INCERTO] (A3 e clientes usam outro leiaute).
  9. **Payslip**: erro de exibição da taxa de IRPF (resolvido); campos obrigatórios ausentes (código de contrato, data de antiguidade). Artefato: Payslip. Responsável: nosso (payslip). Aberto.
- **Causa raiz:** os testes de aceite foram feitos contra o spec e não contra o oráculo da autoridade (padding, posições, zeros). O ticket concentra os achados de teste de uma só vez porque o time de implementação/suporte só os subiu ao portal depois do deploy. Payslip: campos legais obrigatórios não levantados na pesquisa (etapa de research/Payslip). [INCERTO se o CCG cobre o recibo de salario obrigatório (Orden de 27/12/1994 — não consta no ticket).]
- **Solução aplicada:** CodProfesion right-pad (CERTIFICA v1.1), L01/L02/L03 corrigidos (Fichero de Bases v2.5), M111 posições ajustadas (Spec v4, SR-82), taxa do payslip corrigida e deployada (≈04/09).
- **O que ficou aberto:** M111 (erro persiste), M190 (não residentes, rejeição), M296 (ticket com teste em Ejercicio 2026), Annual Tax Certificate (formato), Llamamiento sem arquivo, payslip sem contract code e seniority date, mapeamento completo do Fichero de Bases.
- **Tipo de erro:** T5, T3, T6, T9, T10, T11, T12.
- **Lição para o pipeline:** **F4** (formato), **F40/F41** (oráculo/validador da autoridade) e o **NOVO** (diff de leiaute oficial) cobrem 111/190/296/CERTIFICA. **F43** para não residentes no 190 (população). **F2** (códigos fora de escopo vazaram — L01). **NOVO: Payslip sem checklist de campos legais obrigatórios por país** (check: lista de campos obrigatórios do recibo de salario nos artefatos de payslip). **NOVO: Teste de portal com exercício em curso** (ver SR-83).

---

## CT-A-485 — SPAIN: Regulation Specifications (artigo da Knowledge Base)

- **País / Cliente / Tipo / Prioridade:** Espanha / — / artigo de Knowledge Base (projeto Compliance), não é ticket / —.
- **Snapshots lidos:** 66 (15/09/2026). Criado por Mohit Jain ≈jan/2026, atualizado por Lily Li ≈14/09/2026; 21 sub-artigos (última atualização entre 03/02/2026 e 07/09/2026).
- **Estado no último snapshot:** vigente. Não há comentários nem histórico de revisões no texto.
- **Linha do tempo:** o artigo é uma foto única, sem comentários. Os sub-artigos (CT-A-486 Monthly Contribution Group 1–7, CT-A-487 Daily Group 8–11, CT-A-488 Part-Time Hourly Minimum Rate, CT-A-489 Zero Tax Floor, CT-A-490 Low Income Reduction, CT-A-491 IRPF Tax Table 2026, CT-A-492 Solidarity Quota, CT-A-496 BCCC Taxability Matrix, CT-A-497, CT-A-498 Pension Plans Limit, CT-A-501) têm data de última edição própria: os de **piso/teto de cotização e tabelas (486, 487, 488, 489, 490, 491, 492, 498) foram editados em 03–09/02/2026**; os de matriz de tributação entre 29/07 e 07/09/2026.
- **Problema relatado:** não há queixa no artigo. Há **suspeita informada pelo solicitante** (valores desatualizados, 1.424,50 × 1.424,40) e há o registro do próprio cérebro (`revisoes/2026-10-05-detalhe-ES.md`, B1/B2) que compara com a skill.
- **Erros identificados** (somente o que está no texto, mais comparação com o cérebro/skill):
  1. **Base mínima G4–7 = 1.424,50** em fórmulas dos flags/WTs (Group 4–7, Part-Time ceiling, Floor for Intern, Daily). Dentro do próprio artigo, o piso diário usado é **47,48** (`MULTIPLY(SUM(63952);47.48)`, linha de estagiário `MIN(...;MULTIPLY(47.48;$63952))`); 47,48 × 30 = **1.424,40**, não 1.424,50. O teto diário 170,04 × 30 = 5.101,20, consistente com o teto mensal. Logo o piso mensal e o piso diário estão **internamente inconsistentes**. O cérebro (`paises/Espanha.md`, `revisoes/2026-10-05-detalhe-ES.md`) registra que a skill, com base na Orden PJC/297/2026 (art. 3), indica 1.424,40, e que 1.424,50 é erro conhecido do engine. Artefato: KB CT-A-485 / WTs. Erro: nosso (artefato de design). Não corrigido no último snapshot.
  2. **Bases mínimas G1/G2/G3 = 1.929,00 / 1.599,60 / 1.391,70** (fórmulas dos pisos). O cérebro (revisão de 05/10) observa que a skill traz G1 1.989,30 / G2 1.649,70 / G3 1.435,20 (Orden PJC/297/2026 arts. 2–3), e que no KB G3 (1.391,70) < G4–7 (1.424,50), o que é incoerente. Pelo meu conhecimento, 1.929,00/1.599,60/1.391,70 seriam valores de 2025 e o **teto 5.101,20 é o de 2026** — tabela mista de anos [INCERTO: não confirmado em fonte; o ticket não dá fonte nem vigência]. Os sub-artigos de piso (CT-A-486/487/488) foram editados em 03–05/02/2026; se a Orden PJC/297/2026 for posterior a essa data [INCERTO: data da Orden não consta], eles poderiam ter sido escritos antes do valor oficial.
  3. **Mínimos horários part-time** (11,98 / 9,94 / 8,65 / 8,58), **teto/mín. diário** 170,04 / 47,48, **mín. de estagiário** 57,72 / 7,95 / 11,51 / 2,88 × dias (máx. 65,42) / 0,35 × dias (máx. 7,95): sem fonte e sem vigência no artigo [INCERTO se vigentes; o cérebro diz que mínimos part-time estavam desatualizados na KB v1 e foram corrigidos conforme WTC v3.6, `correcoes.md` "2026-06 a 2026-08"].
  4. **Rótulos "per km"** nas três diárias 26,67 / 91,35 / 48,08: erro de rótulo (são por dia; o cérebro/skill confirmam: 53,34/91,35 com pernoite; 26,67/48,08 sem). Só a quilometragem 0,26 é por km.
  5. **Sobreposição de faixas de desemprego**: indefinido `contract_type_key < 401` (1,55%/5,5%) e temporário `> 389` (1,6%/6,7%): chaves 390–400 casam com as duas linhas [INCERTO se há chaves nesse intervalo; é um check de gate morto/duplicado no estilo F46].
  6. **Placeholders "Check WTC"** para Disability Minimum (588 93), Ascendant Minimum (588 94) e Ascendant Disability Minimum no bloco de flags: valor não resolvido no artigo (F6).
  7. **Linhas de estagiário** (`58208 = 2` com três linhas Band com a mesma Band Assertion `EQUALS($58208;2)`, valores 57,72/7,95/11,51) — sem texto que explique qual linha vai a qual conta [INCERTO se é padrão do template ou duplicidade].
  8. **Texto de revisão dentro do artefato**: "Updated Regulation Assertion", "New TM:" nas linhas 2, 221, 251, 261, 281, 446 e 576 — histórico de edição misturado ao conteúdo (F47).
  9. **Códigos de WT**: o artigo não usa mais 58176/58177 e já usa 58552/58572 nas linhas de IRPF não residente; as specs SR-82/SR-85 ainda citavam 57176/58176/58177 (ver acima).
- **Causa raiz:** o artigo é um espelho do WTC/CCG/design em forma de texto, mantido manualmente: valores copiados de edições de fevereiro e atualizados em partes; piso mensal foi digitado a partir do SMI/engine em vez de derivado do diário × 30 (design, etapa de sincronização). [INCERTO] sobre a origem exata.
- **Solução aplicada:** nenhuma no próprio artigo. O cérebro registrou a proposta de ajuste (revisão de 05/10), aguardando aprovação.
- **O que ficou aberto:** confirmar quais valores estão em produção nos WTs (52982–52984 etc.); corrigir 1.424,50 → 1.424,40 (ou fixar a regra); revisar G1–G3 e vigência; resolver "Check WTC"; corrigir o rótulo "per km"; separar o histórico de revisão do conteúdo.
- **Tipo de erro:** T1, T7, T12, T8, T3.
- **Lição para o pipeline:** **F37 (A rate restated in prose contradicting the same file's own calculation)** é o análogo: piso mensal contradiz piso diário × 30. **F18 (Stale law references in CCG)** e **F44 (Single-pass research: numbers never re-verified)** para valores de 2025 convivendo com o teto de 2026. **F45** (consistência de fatos/versões entre artefatos) e **F46 (Technical design not derived from the research)** — o design (KB) devia ser derivado dos fatos (`fact-keys`) e não digitado à parte; C46 (cada número bate com o facts.json) teria pegado 1.424,50 vs 1.424,40. **F47** pelo texto de revisão no artefato. **F6** para "Check WTC".

---

## Tabela-resumo

| ID | País | Tipo(s) | Artefato | Resolvido? | F-xx / NOVO |
|---|---|---|---|---|---|
| SR-83 | ES | T5, T4, T6, T2, T8, T3, T10, T11 | Report Spec M190 (ES-M190-001), WTC V4.2–V4.4, DD | Parcial (Year of Birth, Accrual Year, Descendants-DD, não residentes abertos) | F4, F10, F27, F7, F6, F40/F41, F2; NOVO: diff de leiaute oficial; NOVO: ejercicio em curso; NOVO: grupo de registro com filtro placeholder |
| SR-82 | ES | T5, T4, T7, T3 | Report Spec M111 v4, DD | Parcial (reteste no portal; erro persiste em HRBS-13757) | F21, F4, F40/F41; NOVO: diff de leiaute oficial |
| SR-85 | ES | T5, T2, T7, T8, T4 | Report Spec M296, WTC V3.5 | Parcial (zeros e Record ID sem resposta) | F7, F27, F4; NOVO: resposta baseada em cópia local do WTC |
| SR-144 | ES | T5, T11, T4 | Report Spec SEPE Llamamiento | Não (bloco DATOS_USOLIBRE_EMPRESA em aberto) | F5, F9; NOVO: aceite antes de comparar com sample real |
| SR-342 | ES | T3, T8, T5, T10 | Report Spec ES-CERT-001, WTC V4.2 | Parcial (códigos trocados; formato aberto) | F27, F45; NOVO: renomeação de código de WT sem varredura |
| SR-365 | ES | T11, T6, T12 | Report Spec ES-FINIQ-001, CCG (zero tax floor), DD V3.9 | Parcial (cálculo explicado; residente × não residente aberto) | F43, F6 |
| HRBS-13757 | ES | T5, T3, T6, T9, T10, T11, T12 | Specs CERTIFICA/Fichero de Bases/M111/M190/M296, Payslip | Parcial (CERTIFICA e Fichero L01–L03 corrigidos; payslip rate OK; demais abertos) | F4, F2, F40/F41, F43; NOVO: checklist de campos legais do payslip; NOVO: ejercicio em curso |
| CT-A-485 | ES | T1, T7, T12, T8, T3 | KB Regulation Specifications (fórmulas dos WTs/flags) | Não (proposta de correção no cérebro aguardando aprovação) | F37, F18, F44, F45, F46, F47, F6 |

---

## Padrões recorrentes no grupo

- **Spec de arquivo posicional sem diff contra o leiaute oficial da AEAT.** M190 (6 posições erradas, Type 2 ausente, domínios errados), M111 (legal name em 1 campo em vez de 2, deslocando posições), M296 (campos numéricos em branco onde a AEAT exige zero, Record ID), CERTIFICA (CodProfesion sem padding de 7). Cada erro só apareceu quando o portal rejeitou. Teste do dev contra o próprio spec é circular.
- **Código de wage type retirado, renomeado ou reclassificado sem varredura nas specs.** 57176/58176/58177 → 58552/58572 (SR-82, SR-85, SR-342, SR-83, linha 41 com sentido oposto entre Lily e Drew); 65815 (SR-85); 79429/79430/79432 (WTC V4.4 e spec M190). Cada artefato é corrigido isoladamente.
- **Afirmações nossas tomadas como verdade sem conferir contra o artefato vigente.** Wallisson afirmou 79432 = B.01 e contestou a remoção do 65815 com cópia antiga do WTC; ambos viraram correção. Lição: citar a versão do WTC e checá-la contra o arquivo vigente antes de responder.
- **Lacunas de população e escopo.** Não residentes no 190, B/03 e L/27 gerados com zero, Type 2 por D/E no 296, residente × não residente no finiquito, evento sem dado no Llamamiento. Falta uma Population Rules que enumere as populações especiais.
- **Dados que o modelo não tem.** `accrual_period_year` (SR-83 e SR-342), campos de DD faltando (previous justificante, 4 campos de Descendants), mapeamento HR divergente do spec (Contact Person). O spec é entregue ao dev sem confirmar a existência da fonte no DD.
- **Aceite sem comparação com amostra real.** Acceptance passou em M190, M296, SEPE Llamamiento, Tax Certificate, e só depois a comparação com o A3/portal revelou diferenças. O teste usou exercício em curso (Ejercicio 2026) e foi rejeitado pelo portal por regra de negócio, o que mascara outros erros.
- **Valores estatutários sem fonte e sem vigência no design (CT-A-485).** Piso mensal 1.424,50 contradiz o diário 47,48 × 30 = 1.424,40; G1–G3 e G4–7 convivem com um teto de 2026 [INCERTO: possível mistura de anos].
- **Perguntas abertas e "TBC" ficam no artefato entregue.** Posições TBC, "Check WTC", querys sem resposta (Llamamiento, residente × não residente), pedido de Lily em 16/09 sem resposta.

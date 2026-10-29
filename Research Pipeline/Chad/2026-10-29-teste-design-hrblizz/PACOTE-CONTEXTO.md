# Chade — pacote de contexto para o chat do claude.ai (design)

> Rascunho de 2026-10-29 (frente Chade). **Não colado em nenhum chat.** Hub: [[Chade]] · Conferência: [[CONFERENCIA]]
> Fonte principal: conversa "Mercans payroll knowledge base overview IV" (projeto Mercans Design & Development Knowledge Base, org Mercans), mensagens [263]–[332], de 2026-10-09 a 2026-10-16. Link: https://claude.ai/chat/78168810-38d6-41e3-81f7-e6509308bcd8

---

## Texto para colar (início)

Contexto do projeto Chade (design de regulações), retomando de 16/10/2026.

**Pedido.** Cross-training de 09/10 (Manju, Mohit, Suman): "Complete Chad design". O teste é se o Claude produz sozinho um design de payroll no nível do time de Development, partindo só do CCG, do WTC e do DD do Chade (research de 2026), no formato de skill "Design Blueprint" (modelo: bahrain-design-blueprint), e depois compara com o design do Dev (skill chad-design-blueprint / td.json, 31 regulações, 02/07/2026).

**Onde paramos.**
- Design v1 (clean-room, 09/10) → comparado com o do Dev: semelhança geral 73,5% (resultados em 13 casos 77,9%; estrutura 57,3%). Das 23 divergências de valor, 14 (61%) vêm de lacunas/contradições da research (não residente, benefício em espécie como teto ou forfait, truncamento da TAFP, indenização de plano social na TFE).
- v2 (15/10): convenções do motor copiadas da produção (séries do Global WTC, Flat + `_post_formula`, bases `_period` creditando 99998, flags a partir de 1, CNPS numa regulação só). Foi o "80 e pouco %".
- **v3 (15/10, vigente)**, no Drive `Chad/07-design/chad-design/`, mais 4 posições da research:
  1. benefício em espécie com teto (valor real limitado à % do Art. 46 sobre a remuneração em dinheiro), não forfait (LF 2019 art. 7 / CGI art. 46-III);
  2. abono familiar totalmente isento, sem o teto de 5.000 XAF por filho (o teto vem do CGI do Congo-Brazzaville, art. 38-2°);
  3. TFE e TAFP na base ampla do Art. 189: transporte e abono familiar isentos ficam dentro, indenização (dano) fica fora;
  4. base de 18% do não residente líquida das isenções do Art. 45.
  Também tem a redução de TFE/TAFP por entidade (0/50/100%, LF 2024 art. 6–7), sem a flag 58205. Validação: 28/28 nos exemplos do CCG e matriz de 10 cenários + casos especiais.
- **Reunião de 16/10 (Suman, Mohit) respondeu às perguntas do design.** Com isso, fica definido o que entra na **v4, ainda não feita**:
  1. status do empregado na flag **58218** (0 residente, 1 não residente, 2 deficiente, 3 jovem graduado, 4 diplomata); nada na 58201 (reservada para reconciliação avançada);
  2. `retro_` de volta como padrão (só se omite quando a lei proíbe retroativo ou não há teto, piso nem tabela; o Chade tem teto na CNPS e tabela no IRPP);
  3. limites que dependem de outro valor ficam em regulação própria e entram como **conta-teto**: transporte (30% do salário-base), Art. 47 (3,5%) e os tetos do benefício em espécie (uma regulação, nove bandas);
  4. `_$$` (gatilho do gross-up) nas deduções do empregado que entram no gross-up: CNPS do empregado e IRPP;
  5. ler as Report Specs do Chade antes e criar no design as contas que os relatórios pedem (inclusive percentuais, como os 20 da CNPS);
  6. matrizes código a código conforme o WTC, como já estão (confirmado na reunião: o bruto do Dev, que pega a série inteira com reembolsos, é que diverge do WTC).
  Outras respostas da reunião: com a matriz vazia o piso da CNPS se aplica (a nossa condição `GREATER($58131;0)` evita CNPS sobre o piso num mês sem salário; confirmar testando); asserção por banda é aceita e o design deve ser **compacto**; a última faixa precisa de limite; contas contábeis pelo significado no catálogo global, com par empregado/empregador coerente; `_div12` só existe para as Filipinas.
- **Ambiente de teste (Mohit, 16/10):** pedir uma *legal entity* própria no HRB, no servidor de aceite (já vem com a configuração do país), por um formulário Google que a Suman ia mandar.

**Lacunas da research abertas (RESEARCH_GAPS do v3):** escala do IRPP 0/10,5/15/20/25/30% não confirmada (um guia de 2020 bate só com 0/10/20/30% e renda arredondada ao milhar); base do benefício em espécie (CCG: bruto; DD: salário-base; LF 2019 art. 46-I: remuneração em dinheiro líquida de contribuições sociais); cenários C e D do CCG; abatimento de 20% do residente no DD (abolido em 2018); 26 linhas "Yes-No" no WTC sem condição; WTC sem colunas TFE/TAFP; códigos `TD-` não mapeados ao Global WTC; DD sem campos de plano social, transporte "para todos" e redução de TFE/TAFP; taxa de segurança alimentar de 400 FCFA/mês (LF 2024 art. 21–23) fora do CCG; decreto de penhora (CdT art. 277) não público.

**Divergências com a skill payroll-compliance-chad a resolver pela lei (com artigo):**
- TFE/TAFP: v3 usa a base ampla do Art. 189; a skill (esclarecimento 4) diz que seguem a base do IRPP.
- Não residente: o v3 desconta as isenções do Art. 45; a skill (esclarecimento 2) diz 18% sobre o bruto, sem Art. 45.
- Refeição/prime de panier: a skill diz isenta dentro do limite legal; o hub registra 628x como tributável [INCERTO].

**Próximo passo:**
1. produzir a v4 com os 6 pontos acima e ler as Report Specs antes;
2. testar no HRB de aceite (legal entity própria);
3. comparar com o design do Dev liberado para teste.

Separar sempre a regra estatutária (nossa) da configuração do motor (Dev).

## Texto para colar (fim)

---

## Bloco de prova
- **Pedido → resposta:** (a) o que fazer para o Chade, quem pediu e onde parou → "Pedido", "Onde paramos" e "Próximo passo"; (b) pacote pronto → bloco entre "início" e "fim".
- **Fontes:** conversa IV, msg [265] (pedido do teste), [270] (73,5% / 77,9% / 57,3%), [276] (14 de 23 = 61%), [294] (v2), [332] (respostas da reunião de 16/10 e lista da v4); `07-design/chad-design/CHANGELOG.md`, `RESEARCH_GAPS.md` e `VALIDATION.md` (v3, 15/10); `raw/reunioes/2026-10-09-cross-training-design-creation-notas-curtas.txt` (ação "Complete Chad design"); hub [[Chade]] e skill (divergências).
- **Teste:** md5 do v3, Drive = Downloads (3 arquivos). Não achei no cérebro nem no claude.ai nada sobre o design do Chade depois de 16/10.
- **Confiança:** 90%. Faltam: (1) a cópia integral da conversa em `raw/` (precisa do seu ok para baixar); (2) não sei se o formulário da Suman chegou e se a legal entity foi pedida; (3) não li a íntegra das mensagens [277]–[331], só o início de cada pedido e as respostas-chave.

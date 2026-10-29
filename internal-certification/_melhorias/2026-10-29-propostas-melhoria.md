# Internal Certification: propostas de melhoria (rascunho, 29/10/2026)

> **Não enviado.** Rascunho para o usuário revisar. Base: os 83 achados da aba Achados do painel `Acompanhamento_Internal_Certification.xlsx` (atualizado em 29/10), de 11 pacotes em 7 países. Dos 83, 1 foi descartado (KZ F-01, fechado como correto) e 82 estão abertos: 11 High, 24 Medium, 30 Low e 17 Observation.
> Frente: [[frentes/certificacao/estado]] · Método: [[analise-reports]] · Projeto ligado: [[_projetos/fluxo-entregas-marko/PLANO_fluxo_entregas_v0.2|fluxo das entregas (Marko)]].
> **Regra:** a certificação só valida e reporta. As propostas para o sistema vão para implementation/dev como sugestão. Não prescrevemos configuração nem mapeamos wage types do cliente.
> **IDs dos achados:** `PACOTE F-nn`, como na aba Achados. No UK, os IDs do Audit Report (RF-, RD-, MD-) aparecem entre parênteses.

## Resumo em 1 parágrafo
Os 11 achados High caem em 4 grupos:
- **Sem prova de que a autoridade aceitou o report:** 4. Nos 4, o recibo faltava ou era de outra empresa.
- **Imposto calculado errado em casos especiais:** 5 (sindicato, seguro-saúde, aposentado, pagamento avulso).
- **Credencial exposta:** 1.
- **Período declarado:** 1.

O que mais se repete:
- **contracheque que não bate com o report:** 9 pacotes;
- **arredondamento por fórmula em vez da tabela oficial:** 6 pacotes;
- **GL com rótulos de outros países:** 5 pacotes.

As 3 melhorias de maior retorno:
1. conferir na entrada do pacote se o recibo é da mesma empresa e do mesmo report;
2. o sistema guardar o recibo da autoridade junto com cada entrega;
3. o implementation ter um teste-padrão por país para os casos especiais.

## 1. Padrões que se repetem nos achados

| # | Padrão | Achados | Pacotes |
|---|---|---|---|
| P1 | **Recibo da autoridade ausente, ou de outra empresa/report** | NL-QUEST F-08 (High), NL-EXCERPTA F-06 (High), NL-SHERWIN F-01 (High: recibo de outro loonheffingennummer), SE-ONEID F-01 (High: Kvittens da Quest Software AB), DK-SHERWIN F-02 (arquivo do pacote ≠ o que a SKAT recebeu); UA set/26 sem report nem DPS (C-17); UA ago/26 sem recibo do 1-PV (C-10); UK com ACK só depois, colado no Chat (C-09) | 7 de 11 |
| P2 | **Arquivo de outro cliente dentro do pacote** | SE-ONEID F-01 (master da Quest), NL-QUEST F-03 (arquivo bancário com nome de outro cliente), NL-SHERWIN F-01 (dados de outro LH) | 3 |
| P3 | **Contracheque que não bate com o report ou com a lei** | NO F-02, DK-KGS F-02, SE-ONEID F-03, KZ F-02, NL-QUEST F-02/F-10, NL-EXCERPTA F-07, NL-SHERWIN F-04/F-08/F-10/F-11, UK F-05/F-08, UA-08 F01 | 9 |
| P4 | **Imposto pela fórmula, com arredondamento próprio, em vez da tabela oficial** | NL-EXCERPTA F-02, NL-SHERWIN F-07, UK F-03/F-04, SE-ONEID F-04, KZ F-04, UA-08 F04/F05, UA-09 F03 | 6 |
| P5 | **Casos especiais errados: aposentado, desligado, pagamento avulso, admitido** | NL-SHERWIN F-02 (High), NL-EXCERPTA F-01 (High), SE-ONEID F-02 (High), NL-EXCERPTA F-04, SE-ONEID F-05, UK F-06 (RD-02), NL-SHERWIN F-06, NL-QUEST F-06 | 4 |
| P6 | **Benefício ou desconto sem o tratamento tributário certo** | NO F-01 (High: sindicato), DK-KGS F-01 (High: seguro-saúde), DK-SHERWIN F-03/F-04, NL-QUEST F-07/F-09/F-11, NL-EXCERPTA F-08 | 4 |
| P7 | **Campo declarado errado sem mexer em dinheiro** | NL-QUEST F-01 e NL-SHERWIN F-03 (176 h em vez de 173), DK-SHERWIN F-01 (campo 0069), UK F-02 (RD-01), UK MD-01, UA-08 F06 | 5 |
| P8 | **GL com rótulos de outros países ou de outra natureza** | NO F-03/F-04/F-05, DK-KGS F-03, NL-QUEST F-04 (rótulos "EOBI", "EIS"), NL-SHERWIN F-09, KZ F-03/F-05, UA-08 F09 | 6 |
| P9 | **Dados cadastrais (master) inconsistentes** | NO F-06, SE-ONEID F-06, UA-08 F10/F11/F12, UK MD-02 | 4 |
| P10 | **Prazo e período** | KZ F-06 (High: out/26 declarado no 3T), UK RF-02 (FPS depois do payday), UA-08 F03 e UA-09 F01 (férias pagas fora do prazo), UA-08 F08, UA-09 F04 | 3 |
| P11 | **Segurança dos dados** | UK F-01 (RF-01, High: usuário e senha do Government Gateway em texto aberto no XML), UK F-07 (RF-03: comentários do arquivo de teste do HMRC no arquivo de produção), AZ (zip com a senha no mesmo e-mail, D-01) | 2 + AZ |
| P12 | **Folha rodada fora do HR Blizz** | KZ (1C ZUP local, sem GL: F-06/F-03), UA (folhas e pagamentos do 1C: UA-08 F08) | 2 |

## 2. Propostas

### 2.1 Processo de certificação (dono: Compliance/Certificação)

| ID | Proposta | Sustentada por | Prioridade |
|---|---|---|---|
| M-01 | **Checklist fixo do pacote** (amplia a A-07). Cada pacote traz: 1) o arquivo exatamente como foi enviado; 2) o recibo da autoridade; 3) o master, o G2N, os contracheques, o GL e o banco da mesma empresa e do mesmo período; 4) o report do período anterior, para conferir o acumulado do ano; 5) a mensagem original de qualquer correção; 6) as notificações da autoridade, quando existirem (ex.: códigos fiscais do HMRC, decisão da taxa Whk na NL). Mandar esse checklist às SBCs uma vez, em inglês. | P1, P2; NL-EXCERPTA F-03 (agosto original), UK (limitações do Audit Report), NL-QUEST F-09 (taxa Whk) | **Alta** |
| M-02 | **Conferência na entrada (5 min, antes de validar).** O número fiscal do report tem de ser igual ao do recibo e ao do master (loonheffingennummer, organisasjonsnummer, PAYE ref, BIN/БИН). O identificador do recibo tem de bater com o arquivo (IRmark, kvittensnummer, referência do Altinn). Se não bater, cobrar na hora em vez de validar 100%. | SE-ONEID F-01, NL-SHERWIN F-01, NL-QUEST F-03, DK-SHERWIN F-02 | **Alta** |
| M-03 | **Senha nunca no mesmo e-mail do arquivo**; arquivo sem credenciais. Pedir que o arquivo protegido venha por um canal e a senha por outro, ou que o pacote venha por uma pasta compartilhada da Mercans. | AZ (D-01), UK F-01 | Alta |
| M-04 | **Um contato por país** para a certificação e para o projeto do Marko, conferido no monday (BAU Master Client List). Hoje a NL tem 3 contatos, a IE nenhum e a RU nenhum confirmado. | C-06/C-07/C-08, C-12, C-13 | Média |
| M-05 | **Decisões com prazo e opção padrão.** D-01, D-02 e D-03 estão paradas desde 14–16/10. Cada decisão passa a ter "se não houver resposta até a data X, seguimos com a opção A". | D-01, D-02, D-03 | Média |
| M-06 | **Uma rodada de cobrança por SBC, com tudo junto.** Hoje há cobranças em rascunho desde 09/10 (C-01 a C-05, C-14 a C-18). Enviar uma mensagem por pessoa, como na onda do projeto do Marko. | Aba Ações | Média |

### 2.2 Sistema (dono sugerido: implementation/dev, como proposta da certificação)

| ID | Proposta | Sustentada por | Prioridade |
|---|---|---|---|
| M-07 | **Guardar o recibo da autoridade junto com cada entrega** no HR Blizz (status do Digipoort, Kvittens, квитанція da DPS, ACK do HMRC, tilbakemelding do Altinn). Quando o sistema transmitir pela API, o recibo volta sozinho. É o mesmo ponto do projeto do Marko. | P1 (7 pacotes); projeto do Marko | **Alta** |
| M-08 | **Tirar as credenciais do arquivo arquivado e enviado ao cliente** (bloco `IDAuthentication` do FPS/EPS) e trocar a senha do Government Gateway da McDermott. | UK F-01 (RF-01, High) | **Alta (imediata)** |
| M-09 | **Teste-padrão por país no onboarding** (implementation), cobrindo pelo menos: aposentado (AOW/pensionista), desligado com verba rescisória, pagamento avulso (férias pagas em dinheiro, bônus), admitido no mês, contribuição sindical e seguro-saúde do empregador. Esses casos concentram 5 dos 11 achados High. | NL-SHERWIN F-02, NL-EXCERPTA F-01, SE-ONEID F-02, NO F-01, DK-KGS F-01; P5, P6 | **Alta** |
| M-10 | **Usar a tabela oficial, ou a regra de arredondamento dela, onde a lei manda.** Hoje o motor calcula por fórmula com arredondamento próprio. São diferenças de centavos, mas sistemáticas. | P4 (6 pacotes) | Média |
| M-11 | **Contracheque gerado pelos mesmos valores do report** (renda tributável, acumulado do ano, indicadores de seguro, horas). Amplia a A-06 para NL, UK e UA. | P3 (9 pacotes); A-06 | Média |
| M-12 | **Rótulos do GL e dos templates localizados por país.** Os rótulos de outros países aparecem no GL e no template PRE de clientes europeus e do KZ. | P8; NL-QUEST F-04, KZ F-05 | Baixa |
| M-13 | **Remover do template de produção os restos do arquivo de exemplo** (comentários de amostra do HMRC, Timestamp de teste) e conferir os indicadores que repetem todo mês (ex.: "Payroll ID changed"). | UK F-07 (RF-03), UK F-02 (RD-01) | Baixa |
| M-14 | **Alertar antes do prazo da entrega**, para o FPS sair até o payday e a A-melding até o dia 5. | UK RF-02 | Média |

### 2.3 Nosso método e validadores (dono: Certificação)

| ID | Proposta | Sustentada por | Prioridade |
|---|---|---|---|
| M-15 | **Painel atualizado pelos workbooks, sem edição à mão.** O `validators/common/tracker.py` só cria o painel e se recusa a sobrescrever. Ele também lê só `*_Validation.xlsx`, então a v1.1 do KZ (`*_Validation_v1.1.xlsx`) ficaria de fora. Proposta: modo "sincronizar", que lê a maior versão de cada workbook e preserva as colunas Status, Responsável e Comentário. O painel ficou de 14/10 a 29/10 sem atualização: UK com o recibo como "Não" e KZ sem o F-06. | Painel 29/10 (UK linha 14, KZ linha 12) | **Alta** |
| M-16 | **Um ID só por achado.** O Audit Report do UK renumerou os achados (RF-01 = F-01, TX-01 = F-03, ...) e criou novos (RF-02, MD-01, MD-02) que não estão no workbook. A proposta é usar no Audit Report o mesmo ID do workbook, ou incluir uma tabela de correspondência. | UK Audit Report 16/10 × workbook 07/10 | Média |
| M-17 | **Mesma contagem em todo lugar.** O `estado.md` mostra o UK com 50/4/17, o workbook com 66/8/4 (controles) e o KZ com 21/7/4 contra 14/6/5. A proposta é uma regra só: Pass, Finding e Not tested por controle, como na Legenda do painel. | `estado.md` × workbooks | Média |
| M-18 | **Controles reutilizáveis em `validators/common`:** 1) a conferência de entrada da M-02; 2) recibo × arquivo, generalizando o recálculo do IRmark do UK; 3) contracheque × report por pessoa; 4) seleção automática dos casos especiais da M-09 para revisão manual. | P1, P2, P3, P5 | Média |
| M-19 | **Tolerância de arredondamento escrita por país.** A diferença de centavos vira um único achado Low por pacote, citando a regra oficial de arredondamento. | P4 | Baixa |
| M-20 | **Escopo quando a folha roda fora do HR Blizz** (KZ, UA). Definir com a Manju o que certificamos: o report da autoridade gerado fora do sistema, ou só o que o HR Blizz produz. | P12; KZ F-06; projeto do Marko | Média |

## 3. Ligação com o projeto do Marko (fluxo das entregas)
- **M-07** é o mesmo objetivo do projeto: o sistema transmite e guarda o recibo. A certificação mostra o custo de não ter isso: 7 dos 11 pacotes ficaram sem prova de aceite, ou com prova de outra empresa.
- **Noruega:** a a-melding deixa de funcionar pelos papéis do Altinn II em 17/11/2026. Ver [[_projetos/fluxo-entregas-marko/paises/NO_fluxo_entregas|NO_fluxo_entregas]]. Isso é um risco a confirmar com o Dev, não um achado da certificação.
- **M-20** (KZ e UA fora do HR Blizz) é a linha "como é hoje" desses países no projeto.

## Bloco de prova
- **Pedido → resposta:**
  - padrões que se repetem: §1;
  - processo (o que pedir às SBCs, checklist, A-07): M-01 a M-06;
  - sistema: M-07 a M-14;
  - método e validadores: M-15 a M-20;
  - cada proposta com os achados que a sustentam, prioridade e dono.
- **Fontes:**
  - aba Achados do painel (83 linhas, lida em 29/10);
  - Findings Register do KZ v1.1;
  - Audit Report do UK de 16/10 (texto extraído do docx);
  - `validators/common/tracker.py` (l. 1–2 e 101: só cria; padrão `*_Validation.xlsx`);
  - aba Ações (C-, D-, A-).
- **Teste:**
  - contagem por severidade e por pacote refeita por script sobre a aba Achados;
  - o total dos High (11) confere com a soma dos grupos (4 + 5 + 1 + 1).
- **Confiança 85%:**
  - os padrões e os IDs foram conferidos;
  - a classificação de cada achado num padrão é julgamento nosso;
  - a prioridade e o dono são sugestões para o usuário decidir;
  - o UA ago/26 tem 13 achados e só foi lido pelo resumo da aba Achados.

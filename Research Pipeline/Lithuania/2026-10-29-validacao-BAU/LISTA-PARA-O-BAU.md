# Lituânia: o que só o BAU (ou quem vai operar) pode validar

> Hub [[Lituania]] · Método: [[Research Pipeline/Lithuania/2026-10-29-validacao-BAU/METODO-VALIDACAO-BAU]] · Correções: [[Research Pipeline/Lithuania/2026-10-29-correcoes/CONFERENCIA]] · Lacunas do SIR: `2026-10-29-correcoes/SIR/sections/s08_gaps.md`

**Status (30/10):** pronta para a reunião ELT de 02/11. Em 30/10 o Nabil respondeu que ninguém opera folha da Lituânia hoje, e o tema vai à ELT. Nada vai para os tickets até a validação.

**Atualização 30/10 (tarde):** B11 fechado por nós; B5, B6 e parte do B3 respondidos com fonte oficial; o que sobrou virou 6 perguntas oficiais em rascunho → [[Research Pipeline/Lithuania/2026-10-30-fontes-vigentes/RESULTADO-ETAPAS-1-2|RESULTADO-ETAPAS-1-2]]. Versões corrigidas só em local: SAM v1.2, GPM313 v1.3, SIR v1.2. De fato dependem de quem vai operar: B1, B9 (e B4 do cliente).

**Artefatos a validar** (todos no Drive, idênticos ao local em 30/10):
- SAM v1.1 (SR-419);
- GPM313 v1.2 (SR-420);
- GPM312 v1.2 (SR-421);
- SIR v1.1 (SR-479).

## 1. Processo de envio (SIR, fluxos OUT-01 a OUT-04)
| # | Pergunta | Onde está no SIR | Por que só o BAU |
|---|---|---|---|
| B1 | Quem gera e quem envia cada arquivo depois do go-live? Arquivos: SAM mensal à Sodra, GPM313 mensal e GPM312 anual à VMI | OUT-01, OUT-03, OUT-04 | É decisão de operação |
| B2 | O envio é por upload no portal (EDAS na Sodra, EDS na VMI) ou por web service? | s02_outbound, s04_tech | Depende do acesso que a empresa der |
| B3 | Quem confirma o GPM313 no EDS em até 3 dias? Um operador de fora da Lituânia consegue entrar no EDS depois de 1/9/2026? | s03_auth, lacuna G7 | Depende do login da empresa |
| B4 | Que procuração (*įgaliojimas*) a Accenture Lituânia vai dar à Mercans nos dois portais? | s03_auth | Depende do cliente |

## 2. Erros e correções (SIR, s05_errors)
| # | Pergunta | Onde está no SIR | Por que só o BAU |
|---|---|---|---|
| B5 | Como o BAU recebe e trata a recusa de um arquivo: mensagem do portal, e-mail aos contatos do EDS ou aviso FR1025? | s05_errors, lacuna G4 | Os avisos chegam a quem está cadastrado |
| B6 | Como será a correção de um SAM de mês passado (aviso revisado ou anexo PT) e de um GPM313 depois de mudança no GPM312? | s05_errors, lacuna G10 | É prática de operação; a regra vigente vai na nossa parte (seção 4) |

## 3. Doença e eventos (fora das specs atuais)
| # | Pergunta | Onde está | Por que só o BAU |
|---|---|---|---|
| B7 | Como chegam os dados dos atestados de doença da Sodra? Quem envia o NP-SD2 e o 9-SD? | IN-03, OUT-02, lacunas G1, G5, G13 | Depende de como o cliente opera hoje; o escopo da integração de licenças é decisão interna |
| B8 | Os formulários de evento 1-SD, 2-SD, 12-SD e 13-SD saem do HR Blizz ou são feitos à mão? | hub, pendência dos formulários SD | Define se precisamos de spec nova (mudança de escopo) |

## 4. Teste real
| # | Pedido | Critério de "0 erros" |
|---|---|---|
| B9 | Subir no EDS e no EDAS os arquivos do teste do Kevin e guardar o comprovante ou a mensagem de erro | Critério 7 do método: única prova de aceite pelo portal |
| B10 | Conferir com o BAU os códigos que o cliente vai usar (categoria de segurado, tipo de renda, tipo de pagamento) contra a aba Field Options de cada spec | Critério 3 |
| B11 | Como a SAM declara o mês em que o empregado passa do teto de 60 VDU (€138 729 em 2026). Nossa posição: acima do teto, o PSD (6,98), o Fundo de Garantia (0,16), o ILDIF (0,16) e os 3% continuam devidos; só as contribuições VSD vão a 0%. Base: XII-2604 art. 5(3) e 14(3); IX-1691 art. 8(1); I-1336 art. 10(9). Confirmar com a Sodra/BAU como isso aparece em P3, A11 e A12 | Critério 3 |

## O que fazemos sem o BAU (andamento em 30/10)
| Item | Situação |
|---|---|
| Specs × regras oficiais (MXFD da VMI, formato da Sodra) | Feito: GPM 0 erros; SAM 143/144 (divergência documentada) |
| Drive idêntico ao local (critério 6) | Feito em 30/10: 27 abas iguais, sem `#ERROR!` |
| Redação vigente da V-243 da Sodra | Feito: arquivada (redação de 2026-10-03) e citações da SAM reconferidas; correções na SAM v1.2 |
| Prazo em dia não útil (lacuna G15) | Feito: Sodra, V-243 ponto 125; VMI, IX-2112 art. 162(6). O GPM313 de 15/08/2026 passa a 17/08/2026 |
| Teto para Fundo de Garantia, ILDIF e 3% | Posição com base legal (ver B11); falta só confirmar como a SAM declara isso |
| Ambiente de teste da Sodra e da VMI (lacuna G3) | Nenhum publicado. A Sodra tem uma demonstração do EDAS ("UAB EDAS DEMO") só para navegação: o upload vai ao portal real. A página do serviço web da VMI não cita teste. O teste real continua no B9 |
| Arquivos do teste do Kevin passarem nas regras oficiais aqui na máquina | Depende de o Kevin mandar os arquivos |

# Lituânia: resultado das etapas 1 e 2 (30/10, tarde)

> Hub [[Lituania]] · Mudanças: [[Research Pipeline/Lithuania/2026-10-30-fontes-vigentes/MUDANCAS|MUDANCAS]] · Pesquisa B3/B5/B6: [[Research Pipeline/Lithuania/2026-10-30-fontes-vigentes/PESQUISA-B3-B5-B6|PESQUISA-B3-B5-B6]] · Lista: [[Research Pipeline/Lithuania/2026-10-29-validacao-BAU/LISTA-PARA-O-BAU|LISTA-PARA-O-BAU]]

Pedido do usuário (30/10): fazer a etapa 1 (o que é nosso) e levar a etapa 2 (perguntas oficiais à Sodra/VMI) o mais longe possível só com pesquisa. **Nada enviado, nada no Drive.**

## Fontes novas (arquivadas em `raw/docs/oficiais/LT/`)
| Arquivo | O quê | md5 |
|---|---|---|
| `2026-10-30-I-1336-VSD-suvestine-2026-07-01.docx/.txt` | Lei I-1336, redação 2026-07-01 a 2026-12-31 (e-TAR) | docx 3504ac8496cdbfc80938be7b97d0a1b3 |
| `2026-10-30-Sodra-SAM-originais/2026-10-30-sodra-SAM-v07-2026-02.zip` (+ `x_zip/SAM-v07.mxfd`) | Formulário oficial da SAM em vigor, definição criada 2025-12-31 | zip 8eb418f23b52aec86d660c9dfd55ea5e; mxfd fac5aad93aaf351e4787c5efcc1280ba |
| `2026-10-30-Sodra-SAM-originais/2026-10-30-sodra-sam-v07-pagina-2025-07.mxfd` | Versão avulsa da página (2025-07) | f5c26b25f5ace152c4d5fe2130fc27cb |
| `2026-10-30-sodra-imokos-lubos-e-tarifas_extrato.md` | Página da Sodra sobre o teto (2026-05-19) e tabela de tarifas (2026-01-22), trechos literais | — |

## Situação de cada item
| # | Antes | Agora | Confiança | Fonte |
|---|---|---|---|---|
| B11 teto na SAM | aberto | **Fechado:** A12 = A11 × P3 (ponto 55.2; erro C2344). Quando a SAM leva o segurado ao teto, a Sodra recalcula o mês sozinha e avisa a nova tarifa a todos os empregadores; essa tarifa é o P3 do mês seguinte (ponto 55.5). O formulário oficial não barra A12 diferente (a conferência está comentada no código), mas a regra e o C2344 mandam A11 × P3 | 90 % | Sodra "Įdarbinimas, pranešimai, įmokos ir tarifai" (2026-05-19); V-243 p. 55; `SAM-v07.mxfd` |
| 3 % no P3 | aberto | **Fechado:** a tarifa total da Sodra tem coluna própria "Bendras su 3 % kaupimu" (24,27 contra 21,27) | 95 % | tabela de tarifas da Sodra |
| O que continua acima do teto | posição 85 % | **Reforçado:** a lei em vigor põe no teto as contribuições do segurado e as do empregador pelas tarifas da lei do orçamento; PSD fora. Fundo de Garantia, ILDIF e 3 % vêm de outras leis. A página da Sodra cita "desde 2021 só a parte do segurado", mas isso é histórico: o texto em vigor (alterado por XV-633, 09/12/2025) inclui o empregador. Na prática, o P3 depois do teto é o que a Sodra avisar | 85 % (inalterado) | I-1336 art. 10(9) arquivado |
| Campo 5 × 11 | divergência | **Fechado:** formulário em vigor tem 5 casas e só aceita tarifa de 0,01 a 99,99 | 100 % | `SAM-v07.mxfd` (`ValidateRow3SD`) |
| `sam-v07.mxfd` não arquivado (G16) | aberto | **Fechado** para o mxfd; falta o PDF do DataService (abre no visualizador, não baixa) e a página S2 | — | — |
| Data do exemplo do GPM313 | 15/08 | **Corrigido:** 17/08, e Report Matrix!F2 com a regra do dia útil (também na SAM) | 100 % | IX-2112 art. 162(6); V-243 p. 125 |
| B6 correção da SAM (G10) | aberto | **Fechado em regra:** desde 2010 só por pedido PT eletrônico (V-243 p. 77.1.1, conferido). Sobra técnico: se o DataService aceita PT | 90 % | V-243 p. 77.1.1, 86-88, 91.3.1 |
| B5 recusa de arquivo | aberto | **VMI fechado:** status do formulário, aviso aos contatos do EDS em até 5 dias úteis (regras EDS p. 26), FR1025 (p. 27). **Sodra parcial:** status ERR do DataService; verificação adicional avisada pelo EDAS (V-243 p. 79, 84, 123). Prazo do FR1025 não achado | VMI 90 %, Sodra 65 % | PESQUISA-B3-B5-B6 |
| B3 login e confirmação no EDS | aberto | **Parcial:** envio por web service exige confirmar no EDS em até 3 dias ("Per 3 dienas", conferido), por qualquer usuário com direito; direitos dados em "Atstovavimas"; desde 1/9/2026 só os meios do portal do governo (conferido). Estrangeiro: pedido de meios à VMI ou certificado qualificado de prestador lituano. Não confirmado: se o portal do governo aceita meio estrangeiro (página atrás de verificação anti-robô, não contornada) | 85 % (40 % no pós-1/9) | PESQUISA-B3-B5-B6; páginas EDS arquivadas |

## O que sobrou para pergunta oficial (etapa 2), rascunho NÃO enviado
Quem envia e por onde é decisão do usuário. A Sodra responde pela conta do empregador ou pelo formulário de contato; a VMI pelo "Mano VMI". Os dois canais podem exigir a conta da Accenture Lituânia.

**À Sodra**
1. After the 60 VDU ceiling is reached, which total rate (P3) should the employer use for the following months: PSD 6,98 % plus the Guarantee Fund 0,16 % and the Long-term Employment Benefit Fund 0,16 % (and 3 % for pension-accumulation participants)?
2. Where an employee's pay is below the minimum monthly wage and the employer pays contributions on the difference (Law I-1336 art. 10(7)), should A11 in SAM3SD show the minimum wage or the actual pay?
3. Does the DataService web service accept PT correction requests (PT-SAM3SD), or only through the EDAS portal?

**À VMI**
4. From 1 September 2026, can a person outside Lithuania without a Lithuanian ID log in to EDS through the e-government gateway with a foreign eID or a qualified certificate from another EU country?
5. The 3-day period to confirm a declaration sent through the web service: calendar or working days?
6. What deadline does an FR1025 notice usually set to fix a deficiency?

## Nota estimada depois desta rodada
| Arquivo | Antes | Agora | O que falta |
|---|---|---|---|
| GPM312 v1.2 | 88 | 88 | portal |
| GPM313 v1.3 | 85 | 89 | perguntas 4 e 5 (operação); portal |
| SAM v1.2 | 75 | 87 | perguntas 1 e 2; portal |
| SIR v1.2 | 80 | 86 | perguntas 3 a 6; canal dos atestados (G1, fora da SAM); portal |
| **Geral** | 80 | **~88** | respostas oficiais (~90), teste do Kevin (~93), portal (98–100) |

## Arquivos regerados (só local, mesmos números de versão; nunca saíram do computador)
| Arquivo | md5 | Testes |
|---|---|---|
| `LT-SODRA-003-SAM-Spec_v1.2.xlsx` | 87bed94be9abc24397bb48a7d776f6f2 | RSPEC PASS; check_sam 106/0; 30 células × v1.1, todas destacadas |
| `LT-VMI-001-GPM313-Spec_v1.3.xlsx` | 703607856164c37056f4640988d02d35 | RSPEC PASS; check_gpm 0 erros; 8 células × v1.2, todas destacadas |
| `SIR/LT-SIR-001-v1.2.docx` | 804d89c4180a6e2ffbaffd3d7b5b0aa2 | abre; 22 páginas; lint 0; trechos novos sombreados |

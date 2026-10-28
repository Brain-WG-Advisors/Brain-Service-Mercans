# Sodra — SAM (declaração mensal de contribuições) — research pack

- Data: 2026-10-27 · Frente: Pipeline · País: Lituânia (LT)
- Status: **INCOMPLETO — base vigente (2026) não verificada.** Todas as fontes vigentes (sodra.lt, draudejai.sodra.lt, e-seimas.lrs.lt, e-tar.lt) responderam 403 (Cloudflare) a curl e WebFetch. A única fonte primária lida foi o portal legado do Seimas (`www.lrs.lt/tais-portal`), com a **redação de 2015-09-17** da ordem V-243. Tudo o que vem dela é **histórico** (SAM v05) e serve de linha de base para conferir no navegador, não de valor vigente.
- Pastas: fontes em `raw/docs/oficiais/LT/2026-10-27-Sodra-SAM/`.

Legenda de nível: **A** = lido na fonte primária baixada; **L** = pista (trecho de resultado de busca de página oficial ou fornecedor; NÃO lido na fonte; conferir no navegador).

## 1. Fontes

| # | Arquivo salvo | URL de origem | Data/versão | md5 | Nível |
|---|---|---|---|---|---|
| F1 | `2026-10-27_LRS_V-243_2010-06-04_redakcija-2015-09-17_lrs494520.html` | https://www.lrs.lt/tais-portal/dokpaieska.showdoc_l?p_id=494520 | Ordem do diretor da Fondo valdyba Nr. V-243, 2010-06-04, "Aktuali redakcija" de 2015-09-17 (após V-472 de 2015-09-15). Codificação cp1257 | 028c9d4399b19b32a84e80010e311a85 | A (histórico) |
| F2 | `2026-10-27_LRS_V-243_2010-06-04_originalas_lrs376373.html` | https://www.lrs.lt/tais-portal/dokpaieska.showdoc_l?p_id=376373 | Texto original V-243 (Valstybės žinios 2010-06-23, Nr. 73-3728) | d3c477182ae076a3503c80b296b59563 | A (histórico) |

Anexos de F1 (forma SAM-v05 e "SAM duomenų struktūros aprašas v5", links `dokpaieska.dok_priedas?p_id=345187` e `p_id=345183`) vieram vazios (0 bytes) e não foram guardados.

## 2. SAM — ato, versão, prazo

| Item | Achado | Fonte / nível |
|---|---|---|
| Ato que aprova forma e regras | Ordem do diretor da Valstybinio socialinio draudimo fondo valdyba **Nr. V-243, de 2010-06-04**, "Dėl Duomenų apie apdraustuosius ir draudėjus pateikimo ir tikslinimo taisyklių, socialinio draudimo pranešimų/prašymo formų ir jų elektroninių duomenų struktūros aprašų patvirtinimo". Aprova as "Duomenų apie apdraustuosius ir draudėjus pateikimo ir tikslinimo taisyklės" (Taisyklės), a forma SAM e o aprašas eletrônico do SAM. Revogou a ordem V-766 de 2009-12-24 (regras antigas do SAM). | F1, p. 1.1, 1.8, 1.17, 2.9 — A |
| Vigência em 2026 da V-243 | **NOT LOCATED.** Não foi possível abrir a versão consolidada vigente (e-tar/e-seimas 403). Não se sabe se a V-243 ainda é o ato vigente ou se foi substituída. | — |
| Nome da forma | Em 2015: "SAM pranešimas apie apdraustuosius už ataskaitinį laikotarpį" (forma versão 05). O nome "Mėnesinė socialinio draudimo įmokų deklaracija" citado no pedido **NÃO aparece** em F1; páginas da Sodra (busca) chamam de "SAM pranešimas" / "pranešimas apie priskaičiuotus atlyginimus ir įmokas". Nome oficial em 2026: NOT LOCATED. | F1 p. 1.8, 4.7 — A; demais — L |
| Versão do formulário | 2015: **v05** (forma e aprašas). Pista: **v07 desde 2019-02-01** (usada a partir dos dados de janeiro de 2019; campo P16 "įmokų tarifas" removido); v06 teria vigorado 2017-02-01 a 2019-01-31. Versão vigente em 2026: NOT LOCATED (sem prova de v08+). | F1 p. 1.8 — A; v06/v07 — L (página "SD pranešimų archyvas" da Sodra, via resultado de busca) |
| Periodicidade | Mensal: "Draudėjai kiekvieną mėnesį užpildo ir pateikia SAM pranešimą ir jo priedus" | F1 p. 46 — A (2015) |
| Prazo de entrega | "iki kito kalendorinio mėnesio 15 dienos" (até o dia 15 do mês seguinte) | F1 p. 52 — A (2015). Pista de 2026: "už 2026 m. gegužės mėnesį SAM pranešimą reikia pateikti iki 2026 m. birželio 15 d." — L |
| Prazo de pagamento das contribuições | NOT LOCATED (Lei I-1336 e regras de pagamento não abertas; e-seimas 403). | — |
| Dispensa de envio | Pode não enviar se no período não havia contribuições a calcular para nenhum segurado (salvo segurados com 2-SD no mês) e foram enviados 9-SD/12-SD para todo o período; não envia SAM para pessoas dos p. 16.10–16.13 e 16.17. | F1 p. 47 (red. 2015-01-01) — A (2015) |
| Um SAM por categoria | Se há segurados com tipos de seguro diferentes (tarifas diferentes), um SAM separado por categoria. Pista: a exigência caiu com a v07 (2019), quando o P16 (tarifa) saiu. | F1 p. 49 — A (2015); 2019 — L |
| Ordem de preenchimento | Dados do segurador (p. 14.2–14.9) → P14 e P17 (ano e mês) → P16 (tarifa) → anexos → SAM | F1 p. 53 — A (2015) |
| Canal | Documento eletrônico pelo EDAS (Elektroninė draudėjų aptarnavimo sistema), arquivo **FFData**, conforme o aprašas eletrônico, assinado com assinatura eletrônica qualificada | F1 p. 8 — A (2015) |

### 2.1 Campos do SAM (folha principal) — redação 2015 (v05)

| Campo | Nome / regra (lituano resumido) | Descrição | Fonte |
|---|---|---|---|
| 1 / 2 | lapo eilės numeris / lapų skaičius | nº da folha / total de folhas | F1 p. 14.1 |
| 3 | draudėjo pavadinimas | nome do segurador (empregador) | F1 p. 14.2 |
| 4 | draudėjo kodas | código do segurador na Sodra (opcional se tem código do Registro de Pessoas Jurídicas) | F1 p. 14.3 |
| 5 | juridinio asmens kodas | código da pessoa jurídica (PF não preenche) | F1 p. 14.4 |
| 6 | telefono numeris | telefone | F1 p. 14.5 |
| 7 | adresas | endereço da sede ou residência | F1 p. 14.6 |
| 8 | adresatas | unidade territorial da Sodra (opcional) | F1 p. 14.7 |
| 9 / 10 | registracijos data / numeris | data e nº de registro do documento | F1 p. 14.8–14.9 |
| P14 | metai | ano do período | F1 p. 53.2 |
| P17 | mėnuo | mês do período | F1 p. 53.2 |
| P16 | įmokų tarifas | tarifa de contribuição (pista: removido na v07, 2019) | F1 p. 53.3 — A; remoção — L |
| P20.1 / P21.1 | „x“ | marca se vai anexo SAM3SD / SAM3SDP | F1 p. 54.1 |
| P20.2 / P21.2 | lapų skaičius | nº de folhas do SAM3SD / SAM3SDP | F1 p. 54.2 |
| P23 | priedų lapų skaičius | total de folhas de anexos | F1 p. 54.3 |
| P20.3 / P21.3 | apdraustųjų skaičius | nº de segurados no SAM3SD / SAM3SDP | F1 p. 54.4 |
| P20.4 / P21.4 | pajamų suma | soma da base (renda sobre a qual incidem contribuições) | F1 p. 54.5 |
| P20.5 / P21.5 | įmokų suma | soma das contribuições | F1 p. 54.6 |
| P35 | „x“ (naujas SAM) | marca de SAM corretivo em papel | F1 p. 84 |
| P14T / P15T / P17T | ano / trimestre / mês corrigido | período corrigido (correção) | F1 p. 85–86, 108.2–108.4 |
| 11 / 12 / 13 / 14 | cargo / assinatura / nome do signatário; nome, telefone e e-mail de quem preencheu | — | F1 p. 14.13–14.16 |

Campos P1/P2/P3 (tarifa do segurador / do segurado / total) existem nas regras gerais dos SD (F1 p. 14.10–14.12); se eram usados no SAM v05: NOT LOCATED (forma não baixada).

Tipo/formato no XML: NOT LOCATED (aprašas não baixado). Valores: em euros com centavos desde 2015-01-01 (F1 p. 55.1–55.4).

## 3. Anexo SAM3SD

**O que é:** anexo do SAM "apie apdraustųjų (be atleistųjų) valstybinio socialinio draudimo įmokas" — base e contribuições do mês de **todos os segurados**, exceto os que tiveram 2-SD (fim do seguro) no mês. (F1 p. 46.1, 48.1 — A, 2015.) É o anexo usado para empregados comuns.

| Campo | Nome / regra | Descrição | Fonte |
|---|---|---|---|
| A1 | eilės numeris | nº sequencial do segurado | F1 p. 15.1 |
| A2 | asmens kodas | código pessoal | F1 p. 15.2 |
| A3 | socialinio draudimo numeris | nº de seguro social (opcional se A2 preenchido) | F1 p. 15.3 (red. 2014-05-01) |
| A4 | vardas, pavardė | nome(s) e sobrenome | F1 p. 15.4 |
| A11 | pajamų, nuo kurių skaičiuojamos įmokos, suma | toda a base do mês calculada para o segurado, em EUR com centavos, **exceto** renda de atividade esportiva/artística e de contratos de direitos autorais | F1 p. 55.1 (red. 2015-01-01) |
| A12 | įmokų suma | contribuições calculadas sobre A11 | F1 p. 55.2 |
| P7 | bendra pajamų suma | soma de A11 da folha | F1 p. 55.3 |
| P8 | bendra įmokų suma | soma de A12 da folha | F1 p. 55.4 |

Regras do SAM3SD (2015):
- Férias que atravessam o mês: salário de férias e contribuições repartidos por mês civil; não corrigir se o salário de férias não for recalculado por prorrogação por doença. (F1 p. 50)
- Prêmios, auxílios e outros pagamentos tributáveis: no período em que foram calculados; se o segurado foi desligado, entram corrigindo o 2-SD; salário determinado por tribunal: no período a que se refere (ou rateado por mês). (F1 p. 51)

Separação contribuição do empregado × do empregador, grupo de acidentes, tipo de contrato, teto anual de 60 VDU, diferença até o salário mínimo (art. 10(7) da Lei I-1336): **NOT LOCATED** no SAM/SAM3SD. F1 (2015) só tem A11 e A12 (soma única); se a v07 ou posterior separa campos, não foi possível verificar.

## 4. Anexo SAM3SDP

**O que é:** anexo do SAM "apie apdraustųjų valstybinio socialinio draudimo laikotarpius ir įmokas" — períodos de seguro e contribuições de casos especiais em que quem paga não tem vínculo de trabalho comum com o segurado. (F1 p. 46.2, 48.2 — A, 2015.)

Códigos de motivo (campo A5) — redação 2015:

| Código | Caso | Fonte |
|---|---|---|
| 01 | Desligados do serviço público que recebem compensação mensal (Lei do Serviço Público) e desligados de órgãos/empresas públicas a quem a indenização (išeitinė išmoka) do Código do Trabalho é paga mensalmente em partes iguais | F1 p. 48.2.1 |
| 02 | Militares voluntários, reserva ativa/preparada com pagamentos por exercícios/treinamentos/missões; conscritos em curso de comandantes | F1 p. 48.2.2 |
| 03 | Condenados à prisão que recebem salário | F1 p. 48.2.3 |
| 04 | Membros de conselhos municipais pagos por participar em sessões (só os que não trabalham no município por contrato de trabalho/serviço) | F1 p. 48.2.4 (V-472, 2015) |
| 99 | Outros casos em que o segurador sem vínculo de trabalho paga um benefício tributável (exceto esporte/artista/direitos autorais) | F1 p. 48.2.5 (V-472, 2015) |

| Campo | Nome / regra | Descrição | Fonte |
|---|---|---|---|
| A1–A4 | iguais ao SAM3SD | identificação do segurado | F1 p. 15.1–15.4 |
| A5 | priežasties kodas | código do motivo (tabela acima) | F1 p. 56.1 |
| A6 | priežastis | descrição do motivo | F1 p. 56.2 |
| A21 | draudimo laikotarpio pradžia | início do período de seguro no mês (regras especiais para servidores e militares voluntários) | F1 p. 56.3 |
| A22 | draudimo laikotarpio pabaiga | fim do período de seguro no mês | F1 p. 56.4 |
| A11 | pajamų suma | base do período A21–A22, EUR | F1 p. 56.5 |
| A12 | įmokų suma | contribuições do período | F1 p. 56.6 |
| P7 / P8 | totais da folha | somas de A11 / A12 | F1 p. 56.7–56.8 |

Pessoa sem código pessoal nem nº de seguro social: junto com o SAM3SDP vai cópia digital do documento de identidade, assinada com assinatura qualificada. (F1 p. 110)

Se o SAM3SDP ainda existe em 2026: NOT LOCATED.

## 5. Listas de códigos

| Lista | Achado | Fonte |
|---|---|---|
| Motivo do SAM3SDP (A5) | 01, 02, 03, 04, 99 (2015) | F1 p. 48.2, 56.1 — A (histórico) |
| Tipo de seguro / categoria de segurado no SAM | NOT LOCATED | — |
| Códigos de rendimento | NOT LOCATED (F1 não tem código de rendimento no SAM) | — |
| Motivo de correção (PT, campo 17.1) | existe o campo de código, mas a lista não está em F1 | F1 p. 107.4 |
| Códigos de erro do SAM | Existe documento oficial "SAM_klaidu_aprasymas.pdf" (códigos tipo C1000); não baixado (403) | L |

## 6. Formato eletrônico e canais de envio

| Item | Achado | Fonte |
|---|---|---|
| Formato | Arquivo **FFData** (XML), conforme o "Elektroninio SAM pranešimo ... formos duomenų struktūros aprašas" (versão 05 em 2015) | F1 p. 1.17, 8 — A (2015) |
| Canal | EDAS (Elektroninė draudėjų aptarnavimo sistema), regras pela ordem V-665 de 2007-12-20; assinatura eletrônica qualificada | F1 p. 8 — A (2015) |
| Versão vigente do arquivo, esquema/MXFD, nomes dos campos XML | NOT LOCATED (aprašas e páginas do EDAS 403) | — |
| API / web service | Pista (fornecedor, **não é fonte**): software de folha anuncia em 2026 envio do SAM3SD "per API į Sodros EDAS portalą" — https://instrukcijos.softera.lt/docs/payroll-202602-v24 (2026-04-16). Existência e especificação oficial da API: NOT LOCATED. | L |

## 7. Correção (tikslinimas)

| Regra | Fonte |
|---|---|
| Segurador que achar dado incompleto ou errado envia correção **imediatamente** (nedelsdamas). | F1 p. 76 (red. 2015-01-01) |
| Correção eletrônica pelo **PT** (prašymas dėl duomenų tikslinimo), com anexos **PT-SAM3SD** ("SAM pranešimo SAM3SD priedo duomenų tikslinimas") e **PT-SAM3SDP**. Também usado para SAM enviado fora do prazo. | F1 p. 103.6–103.7, 104 |
| Um PT por forma e por motivo de correção; não misturar moedas. | F1 p. 106 (red. 2015-01-01) |
| Campos do PT: 16 (forma/anexo corrigido), 17 (motivo), 17.1 (código do motivo), 17.2 (motivo de envio); nos anexos, 15.1/15.2/15.3 = ação "patikslinti" (corrigir), "pašalinti" (remover) ou "įrašyti" (incluir); P14T ano; P17T mês (ou P15T trimestre, até 2009); a parte "Registro duomenys" é preenchida automaticamente; em "Nurodomi teisingi duomenys" vão os dados corretos. | F1 p. 107–109 |
| Correção em papel do SAM: novo SAM com P35 = „x“; só os segurados alterados, com A11/A12 = **valor total corrigido do mês** (não a diferença); um SAM por mês corrigido. | F1 p. 84–87 |
| Pista 2026: software de folha cita no PT o campo "Tikslinimo tipas" (Correct / Remove / Enter) e "PT priežasties kodas" — consistente com F1 p. 108.1. | L |

## 8. Mudanças 2025–2026

- **NOT LOCATED** na fonte oficial. Nenhuma mudança de versão do SAM, campo novo ou fim de anexo em 2025–2026 pôde ser verificada.
- Pistas a conferir: (i) v07 desde 2019-02-01 com remoção do P16 (página "SD pranešimų archyvas"); (ii) se existe versão posterior à v07; (iii) a página da Sodra "SAM pranešimo pateikimo ir pildymo instrukcija" é a referência atual de preenchimento.

## 9. Precisa de navegador

Todas retornaram 403 (Cloudflare) a curl e WebFetch em 2026-10-27:

| O quê | URL |
|---|---|
| Instrução atual de preenchimento do SAM | https://sodra.lt/formos-ir-sablonai/sam-pranesimo-pildymas-ir-pateikimas/sam-pranesimo-pateikimas-ir-pildymas |
| Página do SAM (forma, versões, downloads) | https://sodra.lt/formos-ir-sablonai/sam-pranesimo-pildymas-ir-pateikimas |
| Histórico de versões das formas SD (SAM v06, v07…) | https://sodra.lt/sd-pranesimai/sd-pranesimu-archyvas |
| Formas e modelos para empregadores | https://sodra.lt/formos-ir-sablonai/draudejams |
| Códigos de erro do SAM | https://draudejai.sodra.lt/lt/esd-global/download/instrukcijos/SAM_klaidu_aprasymas.pdf |
| Regras de envio dos SD (PDF) | https://draudejai.sodra.lt/esd-global/download/SD_pranesimu_pateikimo_taisykles.pdf |
| Ordem V-243 no e-seimas (texto, alterações e consolidada vigente) | https://e-seimas.lrs.lt/rs/legalact/TAD/TAIS.376373/ |
| Página de contribuições/tarifas (EN) | https://sodra.lt/imokos/idarbinimas-pranesimai-imokos-ir-tarifai?lang=en |
| Lei I-1336 (prazo de pagamento, art. 10(7), teto de 60 VDU) | e-seimas / e-tar (consolidada vigente) |

No navegador, baixar: forma SAM vigente (PDF), "SAM ... duomenų struktūros aprašas" vigente, o MXFD/FFData do EDAS, a consolidada da V-243 (ou do ato que a substituiu) e a da Lei I-1336.

## 10. Lacunas

1. Ato vigente em 2026 (V-243 consolidada ou substituta) e versão vigente do SAM (v07 é só pista).
2. Nome oficial atual ("Mėnesinė socialinio draudimo įmokų deklaracija" não confirmado).
3. Campos do SAM/SAM3SD/SAM3SDP após 2019: separação empregado/empregador, grupo de acidentes, tipo de contrato, teto de 60 VDU, diferença até o salário mínimo (art. 10(7) I-1336).
4. Prazo de pagamento das contribuições.
5. Listas de códigos vigentes (tipo de seguro, motivos SAM3SDP após 2015, motivos do PT).
6. Esquema FFData/MXFD vigente e nomes dos campos XML; existência oficial de API do EDAS.
7. Mudanças 2025–2026.
8. Os dois anexos de 2015 (forma SAM-v05 e aprašas v5) vieram vazios do lrs.lt.

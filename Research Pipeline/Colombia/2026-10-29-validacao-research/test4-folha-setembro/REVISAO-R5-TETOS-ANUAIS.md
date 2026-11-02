# Test 4: revisão da rodada 5 (tetos anuais A-1 e cesantías A-2)

Data: 2026-11-02 · Frente: Validação CO · Ligações: [[RELATORIO-TEST4]], [[Colombia]], [[CONFERENCIA]] (pasta `2026-10-29-validacao-research`), `pesquisa-2026-11-02/LOTE-A-RETENCAO.md`

**Pergunta.** Depois das decisões de 02/11, quais "erros do provedor" do Test 4 (folha de set/2026 da PMI, mascarada) ainda podem ser afirmados ao BAU?
- **A-1:** os tetos de 790 UVT (ET 206 num. 10), 1.340 UVT (ET 336 num. 3; DUR 1.2.4.1.6 par. 3) e 3.800 UVT AFC (DUR 1.2.1.22.43) são **anuais**. A retenção mensal os controla pelo acumulado do ano, sem o limite de 1/12 (CE Sección Cuarta, rad. 24047, 28/10/2021).
- **A-2:** cesantías e intereses não sofrem retenção na fonte (Ley 100/1993 art. 135 par. 3; DUR 1.2.4.1.11).

O `RELATORIO-TEST4.md` e os `resultados*.json` anteriores **não foram alterados**. Este relatório não traz nenhum ID, nome ou salário individual: só contagens e totais.

## Regra usada

Não temos o histórico de jan–ago por empregado, então o saldo anual disponível em setembro é desconhecido. O script refaz a retenção de setembro com o oráculo v2 sem alterar o código: troca só o limite que ele lê, como no `oracle_r5_ytd.py`. São quatro cenários de saldo, aplicados aos três tetos (790, 1.340 e 3.800):

| Cenário | Saldo em setembro | Quando vale |
|---|---|---|
| S0 | 0 | Sem premissa nenhuma: o ano já teria consumido o teto todo. |
| S1 | 1/12 do teto | Premissa fraca. É a conta do oráculo v2 e do relatório original. |
| S4 | 4/12 do teto | **Premissa P:** em jan–ago o agente nunca deu mais que 1/12 por mês, então consumiu no máximo 8/12. |
| S12 | teto anual inteiro | Nada consumido (ex.: ingresso no mês). |

**Por que P se sustenta (confiança de 90%).** Nos 241 empregados com renda no Base of Withholding, o provedor **nunca** passa de 1/12:
- em nenhum caso a isenção de 25% fica acima de 790/12;
- em nenhum caso os benefícios aplicados ficam acima de 1.340/12.

Ou seja, a regra do sistema do provedor é cortar no 1/12, e o controle anual vale para os pagamentos do próprio agente (DIAN Concepto 011383/2024, IV.1: "en los pagos realizados a cada persona natural"). Aplicando essa regra todos os meses de jan–ago, o consumo do ano fica em até 8/12, e o saldo de setembro é de pelo menos 4/12.

O que não temos é o histórico mês a mês. Por isso P é premissa, não prova.

**Como cada caso foi classificado.** Sob P, a retenção correta de setembro fica no intervalo [R(S12), R(S4)]. Sem premissa nenhuma, fica em [R(S12), R(S0)]. A comparação é com a retenção do provedor, com tolerância de 100 COP:
- **(a) conclusivo:** o provedor reteve mais que R(S1). Isso já vale com a premissa fraca, e portanto também sob P.
- **(c) o provedor aplicou o 1/12:** cortou o 25% e/ou o teto conjunto no 1/12 quando o mês pedia mais, e reteve mais que R(S4).
- **(b) depende do acumulado:** o valor do provedor cai dentro do intervalo de P.
- **OK:** nenhum teto UVT entra (o mês fica abaixo de 1/12), e o resultado é o mesmo em S4 e em S12.

Entradas usadas: só as do próprio provedor no Base of Withholding (renda, INCRNGO, dependentes, prepagada, vivienda e AFC+APV), para isolar o efeito dos tetos. No procedimento 1 vale a tabela do art. 383. No procedimento 2, a conta é base × % do provedor; o % semestral não foi recalculado.

## Resultado por categoria (retenção, setembro/2026)

Diferença = retenção do provedor − cenário. Valor positivo = o provedor reteve a mais.

| Categoria | Empregados (proc. 1 / proc. 2) | vs S1 (mínimo, premissa fraca) | vs S4 (mínimo sob P) | vs S12 (máximo) | vs S0 |
|---|---|---|---|---|---|
| **(a)** nenhum benefício aplicado (mecanismo #2 do Test 4) | 4 (3 / 1) | **+7.685.264** | **+24.109.923** | +32.066.292 | 0 |
| **(c)** o provedor aplicou 1/12 (só 790/12: 78; 790/12 + 1.340/12: 33; só 1.340/12: 2) | 113 (65 / 48) | +30 (dentro da tolerância) | **+155.233.362** | +178.101.013 | −137.383.654 |
| (b) depende do acumulado | 0 | — | — | — | — |
| OK: os tetos não interferem | 115 (68 / 47) | 0 | 0 | 0 | −59.658.754 |
| Fora: "procedimento 3" (não recalculado) | 9 (1 sem benefício, 8 com 1/12) | — | — | — | — |
| **Total com renda no BoW** | **241** | | | | |

Leituras:
- **(a), os 4 recalculáveis.** O valor de S1 (7.685.264 COP) é exatamente a divergência de retenção do `resultados-v2.json` (4 linhas, 4 empregados). O número do relatório original continua válido, agora como **mínimo**.
  - Em todos os 4, a própria planilha do provedor calcula a isenção de 25% em 790/12 e mesmo assim não a aplica (a base gravável fica = renda − INCRNGO). O zero não vem de saldo anual esgotado: o próprio sistema mostra que havia saldo.
  - Em 2 dos 4, o 25% do mês passa até de 4/12 do teto. Nesses dois, só o mínimo sob P é seguro.
  - O 5.º empregado do mecanismo #2 está no "procedimento 3": a base gravável sem nenhum benefício continua errada pelo mesmo motivo, mas o valor não foi recalculado.
- **(c), os 113.** No v2 eles batiam com o oráculo, porque o oráculo também usava 1/12 (diferença máxima de 1 COP; daí vinham as 329 linhas de "tolerância" de retenção do Test 4, pela diferença 3.447.953 × 3.447.955,50). Com A-1 passam a ser retenção **a mais** em setembro:
  - pelo menos 155,2 M COP sob P, de 1.549 a 4,97 M por empregado, com mediana de cerca de 1,03 M;
  - **mas isso é efeito de prazo dentro do ano.** Se o pagamento se repete, o 1/12 dá os mesmos 790 (ou 1.340) UVT no total até dezembro, e o controle anual só antecipa o uso. A diferença no total do ano vem só da progressividade da tabela. O empregado também acerta na declaração anual.
- **(b).** Sob P não sobra nenhum caso. Sem P (cenário S0), *nada* que envolva tetos anuais seria afirmável, nem a categoria (a): reter sem benefício é exatamente o que um saldo esgotado produziria. A afirmação depende de P ou da premissa fraca, e a evidência dela está acima.
- **Lacunas do oráculo afetadas por A-1:** as 2 linhas "sem efeito" (coluna AFC/APV acima de 30% / 3.800 UVT ÷ 12) são de empregados da categoria (a). Com a A-1, o teto de AFC também passa a ser pelo saldo anual, e isso já está nos cenários acima. Elas não viram achado próprio.

## A-2: cesantías e intereses

- Na folha de setembro, 2 empregados recebem cesantías e intereses (WT 62110 "Cash-out of Severance Pay" e 62117 "Cash-out of Interest Severance Pay"). Nenhum recebe os adiantamentos 62126/62127.
- Nos 2, o valor **não entra** na renda de retenção: a parcela "other income" do Base of Withholding é menor que o valor pago de cesantías.
- **Nenhum caso de retenção sobre cesantías ou intereses.** A-2 não muda nenhum achado do Test 4.
- Os WT 62180/62181/63125 são indenização (art. 64), não cesantías.

## 114-1 e art. 64: não dependem de A-1 nem de A-2

| Achado | Contagem | Total | Por que não depende |
|---|---|---|---|
| Exoneração do art. 114-1 calculada com não salariais: o provedor cobra saúde patronal de 8,5%, ICBF de 3% e SENA de 2% de quem tem salário < 10 SMMLV | 8 empregados, 24 linhas | **+16.676.979 COP** pagos a mais pelo empregador no mês | O teste é em SMMLV, sobre o salário do mês (ET 114-1; DIAN Conceptos 8380/2024 e 7196/2025; CE S4 exp. 25302/2022). Não entra UVT, teto anual nem retenção. |
| Indenização art. 64 com a fração de ano truncada, nos casos sem parte variável | 9 valores (150 empregados com até 1 dia a menos) | **−10.603.423 COP** pagos a menos | CST art. 64 b), "proporcionalmente por fracción". O cálculo é trabalhista; o teste não calcula retenção sobre a indenização. |
| Indenização sobre o salário básico só (sem a parte variável) | 335 linhas | (abaixo da base com variável) | CST arts. 127 e 64. Não depende das decisões. Continua com confiança de 70% e fora do escopo estatutário do relatório (#8 do Test 4). |

A retenção sobre a indenização (ET 401-3) não foi testada no Test 4.

## O que fica afirmável ao BAU

1. **Retenção sem nenhum benefício** (25%, dependentes, AFC/APV): **5 empregados**.
   - Em 4, o provedor reteve a mais **pelo menos 7.685.264 COP**. Sob P, o mínimo é 24.109.923 COP; o máximo, 32.066.292 COP.
   - O 5.º está no procedimento 3: a base errada é afirmável, sem valor.
   - Regra: ET 206 num. 10, ET 336 num. 3, DUR 1.2.4.1.6 par. 3. A própria planilha do provedor calcula o alívio e não o aplica.
   - Para dizer ao BAU: o valor exato depende do saldo anual de cada empregado, que só o provedor tem.
2. **Exoneração do 114-1 com não salariais:** 8 empregados, 16.676.979 COP pagos a mais pelo empregador (sem mudança).
3. **Indenização art. 64 com a fração truncada:** 9 valores, −10.603.423 COP (sem mudança). A base sem a parte variável segue como ponto de confiança de 70%.

## O que sai, ou não deve ir agora como "erro do provedor"

- **(c), aplicação do 1/12 (113 empregados, ≥ 155,2 M COP a mais em setembro sob P):** é contrário à A-1, mas **não recomendo apontar ao BAU como erro do provedor agora**. Motivos:
  1. Até a R5, os nossos próprios finais diziam "Mercans applies one twelfth" (WTC Tax Credit A41/A65–A68, Coverage C16 item 4). Em 24/09, no HRBS-13627, também respondemos que o 1/12 é prática de mercado. A correção ainda depende do redline e do ticket ao Development (regra 9).
  2. É sobretudo efeito de prazo dentro do ano, como explicado acima.
  3. Depende da premissa P.

  Recomendação: levar como alinhamento depois que a A-1 entrar nos finais, junto com a pendência do HRBS-13627 no hub. Lá está registrado que o validador do cliente aplica 1.340 ÷ 12; com A-1, o risco não é de sub-retenção, e sim de retenção a mais no mês.
- **Nenhum outro achado de retenção sai.** O número de 7,69 M COP continua, agora como mínimo. Não há caso (b) sob P.
- **A-2:** nenhum achado entra nem sai.

Fora do pedido (não incluí acima): o v2 também tem 1 empregado com a exoneração no sentido oposto. O salário fica abaixo de 10 SMMLV, mas o IBC passa de 10 SMMLV (trava do campo 76), e o provedor exonera: −2.284.026 COP de saúde patronal, ICBF e SENA não cobrados. O aviso do hub fala só dos 8.

## Reproduzir
```
python -I scripts/leitor.py "<…>/co-report-crosscheck/03-client-reports-masked" <scratch>/entradas.json
python -I scripts/revisao_r5.py <scratch>/entradas.json resultados-v2.json resultados-r5.json
```
- O `resultados-r5.json` guarda só a categoria e as diferenças por índice mascarado, sem valores absolutos.
- Antes, o `comparar_v2.py` foi rodado de novo sobre o mesmo `entradas.json`, e o resultado é idêntico ao `resultados-v2.json` (classes e detalhe).
- md5:
  - `scripts/revisao_r5.py`: `454437f86ad93291f1c919b8a77da239`
  - `resultados-r5.json`: `16bff41af9e76603622ae00010b17fe0`
  - intactos: `RELATORIO-TEST4.md` `67ca4c53b1015f68e1bc1b2443a30e30`, `resultados-v2.json` `4d7d4c3dc18c95c42bfdf18167102d7b`, `resultados.json` `71995aa330ab036b87471497f4b5b3e8`

## Bloco de prova
- **Pedido → resposta:**
  1. Achados de retenção × teto mensal: classificados em (a), (b) e (c), com a regra e as contagens acima.
  2. A-2: 2 empregados com cesantías no mês, nenhum com retenção.
  3. 114-1 e art. 64: independentes das decisões (tabela acima).
  4. Arquivos gravados: este relatório, `scripts/revisao_r5.py` e `resultados-r5.json`. Os anteriores ficaram intactos.
- **Fontes:**
  - decisões A-1 e A-2 em `pesquisa-2026-11-02/LOTE-A-RETENCAO.md`: CE S4 rad. 24047/2021; Decreto 2231/2023 art. 9; DIAN 011383/2024 IV.1; Ley 100 art. 135 par. 3; DUR 1.2.4.1.11, todos lidos ali da cópia local;
  - redação vigente "Mercans applies one twelfth" em `revisao/rodada5/mudancas-RODADA5.md` (WTC A41, A65–A68, C16);
  - HRBS-13627 no hub `paises/Colombia.md`.
- **Teste mecânico:**
  - o cenário S1 reproduz ao COP a divergência v2 dos 4 empregados (7.685.264), e a categoria (c) em S1 fica em ±1 COP do v2;
  - 0 de 241 empregados acima de 1/12 no provedor, o que sustenta P.
- **Confiança:**
  - contas: 95%;
  - premissa P: 90% (sem o histórico mês a mês);
  - (a) afirmável como mínimo: 90%;
  - (c) como retenção a mais em setembro: 85% (procedimento 2 com o % do provedor; o % semestral também usa os tetos e não foi refeito).

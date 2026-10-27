# Pedido ao AUTOMATION — V3 de P12 e P13 (Montage) — 2026-10-21

Decisão do usuário (21/10): rodar P12 e P13 com as correções, em vez de levar ao Marko a mesma pergunta feita à Manju. Envio automático pelo Chrome bloqueado (dados de empregado no chat externo) → o usuário cola.
Base: [[2026-10-21-analise-relatorio-marko-v3-P09-P13]] §8.

## Texto para colar (não enviado)
PEDIDO — gerar V3 de P12 e P13 (Montage, correções do relatório v3.0 do Marko)

Decisão: corrigir EH-01, EH-02, EM-03 e EM-02 nos entregáveis, mesmo mudando net pay, imposto, prêmios e pagamento ao TSF. EM-01 fica como está (base do Handboek 2025 §11.2.3/§11.2.6/§11.2.9); não aplicar a opção B.

Base: os sets V2 de P12 e P13 (os mesmos do v3.0) e o histórico P01–P11 do full set.

1. P12 V3 (recalcular o período):
- EH-01 — 10000723: lançar 65802 = 10,725% × 3.756,57 = 402,89 (com LH e prêmios); saldo da reserva TSF corrigido.
- EH-02 — 10000726 e 10000736: estornar o 65802 do retro P06–P09 (111,09 e 90,55); não participam do TSF (IndDeelnTijdspf N desde o P06).
- EM-03 — 10000727/730/735: 65802 do P12 sobre 3.206,30 (e não 3.067,20): +13,48 / +14,06 / +12,89.
- Refazer G2N, holerites, GL, SEPA/payment report e a declaração do P12 (mesma cadeia de correções do V2).

2. P13 V3:
- Partir do P12 V3: tirar o que no P13 compensava o P12 (ex.: os 17,48 do 723) e recalcular saldos e TSF.
- EM-02 — 10000727: premieloon pelo VCR (Handboek 2025 cap. 6, p. 90/93), com teto acumulado; corrigir as bases de P02–P12 por blocos de correção (TijdvakCorrectie) na declaração do P13 e estornar o catch-up de P12–P13; total do ano continua 75.053,63.
- Refazer G2N, holerites, GL, SEPA/payment report e a declaração do P13 com o bloco do P12 corrigido.

3. Conferência antes de entregar: revalidar P12 e P13 com a skill do Marko (testes de EH-01, EH-02, EM-02, EM-03 sem achado); XML × XSD; G2N × holerite × GL × SEPA sem diferença; TotTeBet e saldos por período; mostrar antes → depois por empregado e o efeito no TSF (líquido esperado +224,20).

4. Entrega: zip V3 de P12 e de P13 (6 arquivos cada), Corrections Log de cada um e nota v1.2 (EH-01/EH-02/EM-02/EM-03 corrigidos; EM-01 com a tabela das 30 relações; OB-03/04/05 só na nota). Não mexer no Drive. Regras de sempre: sem "client confirmation"; escopo de pagamento = SEPA do set × G2N.

Se algum item exigir dado que não está na pasta (ex.: artigo da CAO, contagem de dias SV), diga qual e siga com o resto.

## Resposta do AUTOMATION (21/10) — parou antes de gerar
- Pergunta: VCR para todos os empregados ou só para o 727? Motivo: o 723 no P12 tem base de prêmio 5.835,69 com salário SV 5.578,30 ("mesmo padrão" do 727). Recomenda VCR para os seis, P01–P13.
- Imposto recalculado pela tabela de 4 semanas 2025 (reproduz 26/29 relações ao centavo, 3 com ±0,01). Taxas da G2N P12: PAWW 0,1%, WGA empr. 0,36%, AWf 2,74%, Aof 6,28%, Whk 0,72%, Zvw 6,51%.
- Núcleo calculado (sem EM-02): P12 líquido −106,82 (723 −206,70; 727/730/735 −18,97; devoluções de imposto 726 +65,16 e 736 +53,69); P13 líquido −9,75; TSF +224,20 (402,89 − 17,48 + 40,43 − 201,64, conferido).
- Faltam na pasta (não bloqueiam): artigo da CAO com as taxas TSF; dias SV do 726 (OB-05).

## Análise
- Base de prêmio acima do salário do período é o próprio VCR funcionando: quando o SV acumulado passa do teto acumulado, a base do período sobe até o teto acumulado (Handboek 2025 cap. 6, p. 93: "het cumulatieve maximumpremieloon"). O padrão do 723 no P12 sozinho não prova erro.
- O EM-02 é a **mistura** de métodos (P02–P04 e P09 por período no 727). O Marko testou todos e só apontou o 727.
- VCR é obrigatório por regra, não por escolha → aplicar a todos, mas só gerar bloco de correção onde a base declarada ≠ base VCR. Se aparecer diferença além do 727, listar antes de gerar.

## Texto para colar (não enviado)
VCR para todos: é a regra do Handboek 2025 cap. 6, não uma escolha por empregado. Mas a base acima do salário do período no P12 do 723 não é erro por si só: é o VCR recuperando o teto acumulado (p. 93). Recalcule P01–P13 dos seis pelo VCR e gere bloco de correção só onde a base declarada for diferente da base VCR. O Marko só apontou o 727; se aparecer diferença em outro empregado, liste (período, base declarada × VCR, prêmios) antes de gerar os arquivos. Sem diferença fora do 727, siga direto com os V3, a revalidação e a nota v1.2.

## Resposta 2 do AUTOMATION (21/10) — V3 em andamento
- VCR P01–P13 dos seis: só o 727 diverge (P02, P03, P06, P07, P08, P10, P11, P12, P13); 723/726/736 já no teto acumulado; 730/735 base = SV. Total do ano do 727: 75.067,11 (75.053,63 + 13,48 do EM-03). Tetos reduzidos do 726 (P09/P10) mantidos como declarados.
- Declarações: P12 TotGen 23.399 → 23.513 (saldos P06–P09 −118 pela devolução 726/736); P13 20.257 → 20.267 (blocos novos P02/P03 do 727; soma das mudanças nos blocos +143, compensada no período corrente: VCR só redistribui a base).
- SEPA: P12 24.166,74 → 24.059,90 (−106,84); P13 21.207,60 → 21.197,85 (−9,75); TSF +224,20. Conferi as somas por empregado: batem. Ele diz SEPA = G2N = GL e GL fechando.
- Não recalculado: PAWW (até €0,02 por empregado, como ressalva) e colunas informativas da G2N 58103/58104/58552.
- Falta: holerites (723 P12 precisa de linha nova 65802), revalidação + XSD ("se estiver no ambiente"), Corrections Logs, zips, nota v1.2. Pede "segue".

## Análise
- Contas conferidas (SEPA por empregado, totais, TSF). Coerente com a resposta anterior (−106,82 virou −106,84 porque agora entram os prêmios do empregado).
- Atenção 1: períodos do 727 que divergem pelo VCR (P02, P03, P06–P08, P10–P13) ≠ lista do Marko (P02–P04 e P09 por período). A nota v1.2 precisa explicar.
- Atenção 2: colunas da G2N não recalculadas podem gerar achado novo (o OB-06 já era 58551 G2N ≠ holerite).
- Atenção 3: o XSD da Loonaangifte 2025 não está no cérebro (raw/docs/oficiais/NL só tem os Handboeks). Se ele não tiver, a validação contra o XSD não pode ser declarada.

## Texto para colar (não enviado)
Segue. Antes de fechar:
1. Colunas 58103/58104/58552 da G2N: diga o que cada uma guarda e se a skill do Marko compara alguma com o holerite (o OB-06 já era 58551 G2N ≠ holerite). Se comparar, recalcule ou deixe igual ao holerite; não pode surgir divergência nova.
2. EM-02: a nota v1.2 tem que explicar por que os períodos do 727 corrigidos pelo VCR (P02, P03, P06–P08, P10–P13) não são os da lista do Marko (P02–P04 e P09 por período), com base declarada × VCR por período.
3. PAWW: mostre a diferença por empregado e período que fica de ressalva.
4. XSD: se o XSD da Loonaangifte 2025 não estiver no ambiente, diga isso no log e na nota; não declare a validação.
5. Holerite do 723 no P12: mesmo layout dos outros holerites do período, com a linha 65802 no lugar dela.
Na entrega, mostre o resultado da revalidação teste a teste (EH-01, EH-02, EM-02, EM-03 sem achado) e os hashes dos 12 arquivos.

## Resposta 3 do AUTOMATION (21/10) — V3 entregue no chat
- Arquivos: zips "Mammoet montage p12 2025 v3 20261020" e "p13 … v3 20261020" (6 arquivos + Corrections Log cada) e nota "…response to validation reports v2 0 v3 0 mercans v1.2 2026 10 21" (DOCX, 11 p.). SHA-256 dos 12 arquivos informados no chat (nomes iguais aos do V2).
- Fora do pedido: o EM-03 também ocorria no período corrente do P13 (65802 de 727/730/735 sobre o salário pré-CAO): +15,50 / +16,17 / +14,83. TSF total +270,70 (P12 +241,68; P13 +29,02). P13 líquido −30,75 (era −9,75). Total do ano do 727: 75.082,61. Contas conferidas.
- G2N: 58104 recalculada (a skill compara: G-17, X-07/X-08); 58551 ajustada (G-03 passa); 58103/58552 iguais (a skill não compara).
- EM-02: nota §4.2 com base declarada × VCR por período (P04/P05/P09 já coincidiam; P02/P03 recuperam o excesso do P01; P06–P08 e P11 teto por período; P10/P12/P13 recuperações parciais).
- PAWW não recalculado: ele corrigiu a estimativa dele, de €0,02 para até €0,40 (723 P12). Total estimado +0,24 (P12) e +0,03 (P13), como ressalva.
- XSD: não validado; dito no log e na §6 da nota.
- Holerite do 723 no P12: linha 65802 depois da 65800, conferida na imagem; líquido 3.900,37.
- Revalidação: EH-01 1→0, EH-02 8→0, EM-03 6→0, EM-02 9→0; motor de 69 testes igual ao V2 (P12 1 Fail = C-07/OB-04); cadeia P12 X-12/X-14 Fail → Pass. **Rodou 69 + 22 testes de 98 do catálogo; "os que faltam podem trazer algo novo".**

## Análise
- Somas conferidas (TSF 270,70; P12 241,68; P13 29,02; 727 75.082,61; P13 SEPA −30,75).
- Pendências antes de entregar: (1) rodar o catálogo completo de 98 testes (o v3.0 do Marko usou 92); (2) PAWW de até €0,40 sem recálculo; (3) zips com data 20261020 no nome (gerados em 21/10); (4) a correção extra no P13 tem de estar no Corrections Log e na nota; (5) baixar, arquivar no cérebro e conferir os hashes.

## Resposta 4 do AUTOMATION (21/10) — V3 final
- Zips Mammoet_Montage_P12_2025_V3_20261021.zip (sha256 bf0fa31e…) e P13 (067e496d…); nota v1.2 (d9b14bf8…, 11 p.). SHA-256 dos 12 arquivos + 2 Corrections Logs no chat.
- Catálogo 98 testes: P12 V2 81/4/3/10 → V3 82/3/3/10; P13 V2 83/3/3/9 → V3 84/2/3/9 (Pass/Fail/Obs/NT). Única mudança: G-13 Fail → Pass. Ressalva: os scripts da skill estão presos à Nederland; montou motor 69 + cadeia 22 + **16 testes implementados por ele** a partir das definições (X-04, X-05, A-09, C-10, C-11, G-06b, G-13, G-15, X-08, O-01..O-07) + G-11.
- Restantes (iguais ao V2, na nota §3): C-07 (P12, OB-04), E-06, G-14, F-07b, G-03, H-05. NT: O-01..07, E-05, H-03, X-08 P12.
- PAWW recalculado: 0,10% do SV com teto. 723 P12 +0,26 (não 0,40, porque bate no teto) e P13 −0,26; 727/730/735 +0,01/+0,02/+0,01; 726/736 0.
- Totais finais: P12 líquido −107,14 (SEPA 24.166,74 → 24.059,60); P13 −30,53 (21.207,60 → 21.177,07); TotGen P12 23.513, P13 20.296; TSF +270,70. Conferido.
- EM-03 no P13 corrente: no Corrections Log P13 (Summary + 39 linhas) e na nota §4.
- XSD indisponível: limitação no log e na nota.

## Análise
- Totais conferidos (−106,84 − 0,30 PAWW = −107,14; −30,75 + 0,26 − 0,04 = −30,53).
- Ponto de atenção: G-03 aparece entre os que seguem (58551 com teto × holerite sem teto), mas na resposta anterior ele disse "G-03 passa". Pedir esclarecimento ou checar no arquivo.
- Ressalva honesta: 16 testes foram implementados por ele, não são o código do Marko; o Marko pode chegar a resultado diferente nesses.
- Próximo: baixar os 3 arquivos (ok do usuário), arquivar em internal-certification/Netherlands/…/2026-10-21-V3, conferir SHA-256 e rodar a nossa conferência (XML ikv.py × G2N).

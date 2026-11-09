# EUA — Validação por estado (piloto)

Criado em 2026-11-06 (frente EUA), por decisão do usuário ("vamos fazer as validações por estado"). Liga: [[frentes/eua/estado|estado da frente EUA]], `../PLANO-ATE-O-FIM.md`, `../US-compliance/07-qa-crosscheck/QA-REPORT.md`.

## Objetivo
Cada estado ganha um veredito próprio "aprovado", com base em dois testes:
1. **Completa:** nenhuma lacuna média aberta; cada lacuna está fechada com fonte oficial ou registrada como limitação (lei não publicada), com data para reler.
2. **Certa:** cálculos conferidos contra um "juiz" independente (método França/Colômbia), com pelo menos 95% das linhas batendo e nenhum erro grave.

## Piloto
Federal + onda 1: CA, TX, NY, FL, IL, PA, OH, NC, MI, GA. São 120 lacunas abertas (FED 34, CA 10, TX 7, NY 10, FL 5, IL 9, PA 9, OH 10, NC 10, MI 8, GA 8; 7 médias, todas no federal).

## Passos
1. Fechar as lacunas do piloto lendo as fontes pelo Opera (VPN com saída nos EUA, `_pipeline/opera_read.py`), sem contornar bloqueio.
2. Levantar as opções de "juiz" e apresentar ao usuário antes de montar.
3. Montar o juiz e os casos por estado e rodar a suíte; cada diferença é decidida pela lei.
4. Gerar o veredito por estado e o relatório.
5. Corrigir: o que mudar nos documentos vira versão 1.1 (o pacote 1.0 ainda não foi entregue).

## Regras
- O pacote 1.0 em `US-compliance/10-release` não é tocado.
- Nada sobe ao Drive sem o ok do usuário.
- Revisão independente: no máximo 3 rodadas.

## Andamento
- 2026-11-06: plano criado. Passos 1 e 2 em paralelo.
- 2026-11-06: Passo 1 FED: 34 lacunas → 15 fechadas, 16 limitação (não publicado), 3 bloqueadas (crédito FUTA CA/VI sai 10/11; Pub 15-T 2027). Pontos para conferência do revisor: milhagem dividida (72,5¢ jan–jun / 76¢ a partir de 01/07), Rev. Proc. 2026-35, regra proposta das Trump accounts. Arquivo: US-compliance/_research/validation/gap-close-FED.md.
- 2026-11-06: Passo 1 concluído (2 rodadas). Das 120 lacunas do piloto: 73 fechadas, 39 limitação, 8 bloqueadas.
  - FED: 15 fechadas / 16 limitação / 3 bloqueadas.
  - Estados: 58 / 23 / 5. As bloqueadas são GA O.C.G.A. 34-8-155 e 34-8-35 (sem site oficial grátis), FL 155, MI 028/033 (PDF do Tesouro 403) e uma página do NY DOL.
  - Arquivos: `US-compliance/_research/validation/gap-close-{FED,W1}.md`; shards `S6V-FED/W1/W1B.csv` (ainda não juntados ao registro).
  - Ainda não aplicado aos facts: tudo vai junto na v1.1, depois da validação de cálculo.
  - Regra reforçada: nada de user-agent falso no curl (um agente tentou, o classificador barrou e ele parou).
- 2026-11-06: Juiz = opção A (grátis; sem resposta do usuário, segue o padrão anunciado). Passo 3 iniciado: calculador "às cegas".
- 2026-11-06: Passo 3 concluído. Juiz: 35/38 exemplos oficiais (as 3 diferenças são de NY, onde a conta impressa não fecha). 150 casos; 97,09% das linhas batem.
  - Vereditos: aprovados IL, NC, TX, FL, OH; com ressalva FED, CA, PA, MI; reprovados NY e GA (`compare/FINDINGS.md`).
  - Revisor (`compare/VERIFY-S1.md`): GA V-04 confirmado S1 (até 10/05 valiam 24.000/12.000/4.000 a 5,19%). NY V-01..03 rebaixados a S2: as faixas não estão no pacote; a escolha estava declarada, mas o pacote não se basta sozinho. Erro do juiz em OH confirmado.
  - Decisão (técnica, minha): carregar as faixas de NY como facts, igual à CA, para o pacote se bastar sozinho. Correções em curso para a v1.1.
- 2026-11-06: As 72 lacunas fechadas foram aplicadas aos facts (gaps.json: 474 abertas, 174 limitação, 104 fechadas). O registro passou de 2.712 para 2.827 linhas.
  - Defeitos achados: GA e-filing de UI obrigatório para todos a partir de 2026-08-09; TX: os campos da Labor Code 204.0025 são só proposta (a regra ch. 815 não foi adotada).
  - Para o revisor conferir: o agente preencheu effective_from = 2026-01-01 em 75 linhas novas do registro ("em vigor no ano do build, como lido") e renomeou 57 autoridades para a grafia da varredura.
  - Em curso: varredura FTC/Philadelphia (C41) e reconstrução v1.1 (CCG, WTC, RSPEC, DD, SIR).
- 2026-11-06 rodada 2: 99,24%; nenhum estado reprovado; GA e OH 100%, NY 99,46% (V-14 novo). Ver compare/FINDINGS.md.
- 2026-11-06 rodada 3: NY 100% com as tabelas por período; V-14 fechado.

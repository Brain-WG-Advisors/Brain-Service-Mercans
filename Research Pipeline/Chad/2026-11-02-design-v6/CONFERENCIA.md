# Chade — design v6 (conferência)

> Hub: [[Chade]] · Base: [[2026-11-01-design-v5/CONFERENCIA|CONFERENCIA v5]] · Comparação: [[2026-11-02-planilha-comparacao/CONFERENCIA|planilha v4/v5/v6 × Dev]]
> Rascunho local, 2026-11-02. **Não vai ao Drive nem ao Dev sem ok do usuário.** A pasta v5 não foi alterada.

## Fonte
- Regras: v5 (`../2026-11-01-design-v5/_build_v5.py`, depois de 2 rodadas de QA). Nenhuma regra de lei mudou.
- Forma: design do Dev td_2026 (`td.json` do Drive `Chad/07-design`, igual ao CT-A-588), lido por `sim_dev.py`: IDs, nomes, ordinais, grupos, contas, fórmulas.

## Decisões
1. Copiado do Dev onde a lei não obriga diferença:
   - IDs, nomes e ordinais: 30 das 31 regulações do Dev têm par com o mesmo ID, nome, ordinal, tax group e taxation type; 28 têm também o mesmo tax rule group;
   - a cadeia do IRPP em 5 regulações (58110 → 58111 → 58112, com `$period_divisor`);
   - os limites dentro de `MIN()`, a ordem das bandas da CNPS, os flags 58218 e 58205, e sem `retro_`.
2. Mantido do v5 e marcado **Deliberate divergence (law)** em 33 notas do SKILL (lista no CHANGELOG):
   - 9148011 do Dev sem par: o não residente vai pela tabela, e a base dele (58552) só existe depois da 9148191. Por isso o 58592 sai da regulação adicional 9148192.
   - 9148181 e 9148261 com `_post_formula`, porque precisam do teto de 3,5% e da redução de 50%.
3. Não copiado, por ser erro: a inversão EE/ER da CNPS do Dev (EE em 6020/2550, ER em 2610/2551). O v6 mantém 2610/2551 para o EE e 6020/2550 para o ER, como a WTC V3.0.
4. Regulações adicionais no padrão do Dev:
   - 9148034 (plano social);
   - 9148035 (15%, art. 45-2°);
   - 9148036 (passagem de férias);
   - 9148175 (teto de 3,5% da aposentadoria);
   - 9148192 (base do não residente para o relatório);
   - 9148271 (PSA).

   Total: 36 regulações (v5: 35).
5. Contas que só o v5 tinha e saíram: 58109, 58161–58169 e 58173.

## Antes → depois
Tabela regulação a regulação (v5 → v6) em `chad-design-blueprint-claude-v6/CHANGELOG.md`.

## Conferência
- `python -I -B _build_v6.py`:
  - 12/12 cenários e 20/20 extras iguais aos esperados, sem tolerância;
  - v6 × motor do v5, conta a conta: 32 casos × 36 contas = 1.152 valores, **0 diferenças**.
- Defeito achado e corrigido na própria execução: a 9148009 (ordinal 9) lia o 58105, que só nasce no ordinal 10, e o 58106 saía 0. Agora, como no Dev, ela lê os códigos de pagamento.
- SKILL.md: 36 regulações; 33 notas "Deliberate divergence (law)"; 0 marcas ⚠️.
- Não feito: motor real. A confirmar no aceite: `$period_divisor`, a tabela `simple_tax_monthly` sobre base anual, o `MIN()` com `MULTIPLY($58105;…)`, limites de faixa iguais e as contas-teto.

## Rodada 2 (pós-QA da v6, `QA-REVIEW.md`: 0 blocker, 2 major, 4 minor)
- **V1:** a série inteira de cada código agora entra por padrão, como no Dev:
  - `6552%` (combustível do carro, 65520–65523);
  - `6267%` / `6268%` (planos de benefício);
  - na CNPS, `6291%`/`6292%`/`6293%` e 62909 ficam fora.

  Conferi série por série contra os nomes da WTC V3.0. Ficaram como estão, por desenho: 62563 (bloco 6256x de reembolso) e 6585x (categoria do art. 46 por código). **O v5 tem o mesmo defeito** e não foi corrigido, porque o v5 fica como entregue. Teste novo E21: IRPP 23.214 (v5) → 26.364 (v6).
- **V2:** sem `retro_`, como o Dev. Decidido pelo texto:
  - guia da CNPS p. 7: « quelle que soit la période à laquelle ils se rapportent »;
  - CGI art. 189-1°: « sans qu’il y ait lieu de distinguer la période »;
  - art. 847: retenção sobre o que é pago.

  Efeito medido: um atrasado de 100.000 de um mês de 300.000, pago num mês de 900.000, dá IRPP 147.375 em vez de 132.507 e CNPS do empregado 17.500 em vez de 21.000. Confiança de 70% no IRPP. O A11 foi reescrito e há teste novo, o E22.
- **m1:** a 9148201 agora tem pré-condição SCALE, então 58110–58112 ficam 0 para os isentos. A comparação passou a cobrir 39 contas, mais a checagem de 58110/58111.
- **m2:** as referências do ASSUMPTIONS (A10, A12) e do RESEARCH_GAPS (R15, R27) agora usam os IDs e as contas do v6.
- **m3** e **m4:** registrados em A13 e A16, com o efeito de cada um.
- **Resultado:**
  - 12/12 cenários e 22/22 extras exatos;
  - v6 = v5 em 1.386 valores;
  - única diferença: o E21, efeito explícito do V1.

## Rodada 3 (pós-QA rodada 2: 1 major, 3 minor)
- **W1:** passaram a entrar em todas as bases o `6261%` (seguro-saúde: veredito 25, sem isenção no art. 45; 80%) e o `6265%` (abono social: art. 44-I, sem isenção no art. 45; guia da CNPS p. 7; 85%).
- **Varredura** dos 554 códigos Earning da WTC V3.0 pelo motor (`sweep()`):
  - achou e corrigiu o pagamento em dinheiro no lugar do benefício (6561x telefone, 6566x refeição), que estava fora da TF/TA;
  - fora de todas as bases ficaram só os 62560–62563 (reembolso, A22);
  - os 122 códigos que diferem da WTC caem nos grupos de decisão listados no VALIDATION.
- **W2:** a indenização 6218x passa a entrar na TF, como as gratificações de fim de contrato 629xx (art. 189-1°, 75%). Na TA, todos os pagamentos de rescisão ficam fora (art. 173, 60%). O A20 está fechado.
- **O v5 tem os mesmos defeitos** (V1, W1, a varredura e W2). Não corrigi lá, porque o v5 fica como entregue.
- Testes novos E23–E26. Resultado: 12/12 e 26/26 exatos; v6 = v5 em 1.540 valores, menos os 6 casos explícitos (5, E21, E23–E26).

## Bloco de prova
- **Pedido → resposta:** pasta v6 com `_build_v6.py`. Forma copiada do Dev onde a lei permite e divergências de lei marcadas. Resultados idênticos ao v5. VALIDATION, CONFERENCIA e CHANGELOG (tabela v5 → v6).
- **Fontes:** `td.json` (via `sim_dev.py`) e `_build_v5.py`. As regras de lei e os artigos são os mesmos do v5.
- **Teste:** os esperados, mais a comparação mecânica com o motor do v5 (1.152 valores).
- **Confiança:** 98% de que v6 = v5 nos casos testados. A aceitação das convenções novas depende do motor real.

## Quem mexeu
| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | frente Chade | v6 criado (forma do Dev, regras do v5) |
| 2026-11-02 | frente Chade | v6 rodada 2 pós-QA (V1 séries da matriz, V2 retro_, m1–m4) |
| 2026-11-02 | frente Chade | v6 rodada 3 pós-QA r2 (W1 6261%/6265% e varredura, W2 rescisão na TF/fora da TA) |
| 2026-11-02 | frente Chade | QA r3 X1: A20 marcado como decisão técnica da frente, pendente do ok do usuário (inverte correcoes.md 2026-07-07) |

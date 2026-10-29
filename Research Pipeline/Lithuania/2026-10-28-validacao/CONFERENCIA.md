# Lituânia — validação das specs e do SIR de 27/10 (28/10)

> Hub: [[Lituania]] · Entregas validadas: [[Research Pipeline/Lithuania/2026-10-27-reports/CONFERENCIA]] · [[Research Pipeline/Lithuania/2026-10-27-SIR/CONFERENCIA]] · Erro registrado: [[correcoes]] (2026-10-28) · Pedido ao BAU: [[rascunhos/2026-10-28-lituania-validacao-BAU]]

## Relatórios (3 auditorias independentes)
- [[Research Pipeline/Lithuania/2026-10-28-validacao/VAL-GPM313-GPM312|VAL-GPM313-GPM312]]: GPM313 e GPM312 v1.1 **reprovadas**. Os nomes e tamanhos de campo batem com o MXFD (12/12 e 41/41). Os exemplos e o formato não batem:
  - o código de pagador de exemplo 302123456 falha a checagem mod 11 do `ID_formatas_simple_f`;
  - os exemplos usam ponto decimal, e o formulário usa vírgula;
  - a amostra do GPM312 tem PVM inválido, U2=6 inválido em 2026 e caixas 4/5 que não somam com as linhas;
  - U12 e U15 deveriam ser condicionais.
- [[Research Pipeline/Lithuania/2026-10-28-validacao/VAL-SAM|VAL-SAM]]: SAM v1.0 **reprovada**. O envelope do FFData está errado. Faltam a vírgula decimal e as marcas 0/1 (confirmado no FFData oficial). DocDate e DocNumber não se preenchem. Faltam as taxas de 2026 e o teto de 60 VDU.
- [[Research Pipeline/Lithuania/2026-10-28-validacao/VAL-SIR|VAL-SIR]]: SIR v1.0 precisa de v1.1. Nenhum bloqueador; 6 achados MAJOR:
  - 9-SD dado como excluído, com a decisão em aberto;
  - IN-01 dado como resposta do NP-SD2, o que depende da G5;
  - faltam os contatos de erro do EDS;
  - falta o catálogo C23xx;
  - falta o bloco Document Control;
  - os originais da Sodra não foram arquivados.

## Drive × local (28/10, export CSV por aba)
- GPM313: idêntica.
- GPM312: 5 células `#ERROR!` (títulos que começam com "=" quebram na importação). As demais abas são iguais.

## Próximo
Este é o plano apresentado ao usuário em 28/10, à espera do ok:
1. Gerar SAM v1.1, GPM313/312 v1.2 e SIR v1.1 (local).
2. Revalidar.
3. Drive e tickets, com ok.
4. BAU (Kevin, HRBS-15253): amostras e teste.

## Frentes
| Data | Frente | O quê |
|---|---|---|
| 2026-10-28 | pipeline | Auditorias, comparação Drive × local, entrada em `correcoes.md` |

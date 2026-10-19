# Prompt: Fase 1, linha de base (Conjunto A do teste de exatidão)

> Usar no Claude Code. Saída: `testes/exatidao.md` ([modelo](../modelos/teste-exatidao.md)) + `testes/rodadas/AAAA-MM-DD/`.
> Plano: [[PLANO]] §5 Fase 1 e §7.

## Parte 1: gerar as perguntas (Claude Code)

```
Fase 1 do PLANO. Gere o Conjunto A do teste de exatidão a partir de correcoes.md.

1. SELEÇÃO (30 perguntas, estratificadas):
   - Por país, proporcional às correções, com teto e piso: Ucrânia 6, Espanha 6, França 2, Chile 2, Chade 2,
     e 1 de cada um dos demais países que têm correção (Irlanda, Holanda, Costa do Marfim, Reino Unido, Hungria,
     Gabão, Congo, Colômbia, Canadá, Bulgária). Se faltar, completar com Espanha/Ucrânia de tipo diferente.
   - Por tipo (anotar em cada uma): V = valor estatutário (alíquota, teto, prazo) · M = mapeamento (WT, clave,
     código de report, posição de campo) · R = regra de cálculo · P = processo/fronteira/versão.
     Mínimo: 8 V, 8 M, 6 R, 4 P.
   - Preferir correções com fonte nível A ou B. Correção com [INCERTO] não entra.
   - Pelo menos 10 em que o erro original foi NOSSO numa resposta de ticket (é o que mais acontece no dia a dia).

2. REDAÇÃO de cada pergunta:
   - Do jeito que o time ou a BA perguntaria num ticket, em inglês quando o caso original era em inglês.
   - Autocontida (país, ano, artefato/relatório), uma única resposta verificável.
   - Sem pista da resposta e sem citar a correção nem o ticket.
   - Sem dados pessoais nem nomes de clientes.

3. GABARITO de cada pergunta:
   - Resposta correta (curta) + fonte (nível A/B) + origem (linha de correcoes.md).
   - Critério ✅: o que TEM de aparecer (o valor/código exato, e a fonte, quando aplicável).
   - Critério ⚠️: certo, mas incompleto (ex.: valor certo sem vigência; código certo com justificativa errada).
   - Critério ❌: o erro original da correção OU qualquer outro valor/código.
   - Erro conhecido a vigiar: o "Errado" da correção (para reconhecer se o modelo repete).

4. Escreva tudo em testes/exatidao.md seguindo modelos/teste-exatidao.md.
   As perguntas ficam na tabela principal; o gabarito numa seção separada "Gabarito (não colar no claude.ai)".

5. Gere também testes/rodadas/AAAA-MM-DD-perguntas.txt só com as 30 perguntas numeradas, prontas para colar.

Mostre um resumo da estratificação (país × tipo) e pare para eu revisar antes de qualquer rodada.
```

## Parte 2: rodar no claude.ai (usuário)
1. Configuração da **rodada 1 (linha de base)**: claude.ai como o time usa hoje, com as skills da Mercans ativas, **fora** de qualquer projeto e sem o pacote do brain. Anotar a configuração na tabela Rodadas.
2. **Um chat novo por pergunta.** Colar só a pergunta, sem complemento, sem "tem certeza?" e sem segunda tentativa.
3. Copiar a resposta inteira para `testes/rodadas/AAAA-MM-DD/T-001.md` (um arquivo por pergunta).
   - Alternativa com Chrome: o Claude Code roda as perguntas no claude.ai pelo navegador e salva as respostas, sem alterar nada além de criar os chats novos.

## Parte 3: corrigir (Claude Code)

```
Corrija a rodada testes/rodadas/<AAAA-MM-DD>/ contra o gabarito de testes/exatidao.md.
Para cada pergunta: ✅/⚠️/❌ pelo critério ESCRITO (não reinterprete), 1 linha de justificativa citando o trecho
da resposta e "repetiu o erro conhecido?" (sim/não).
Preencha as tabelas Rodadas e Resultado por pergunta. Totais por país e por tipo (V/M/R/P).
Não altere o gabarito. Se achar que o gabarito está errado, liste à parte para eu decidir.
```

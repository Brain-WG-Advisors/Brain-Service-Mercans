# Test 0 dos finais CO (30/10/2026)

Ligado a [[CONFERENCIA]], [[RELEASE-CROSSCHECK]] e [[BASELINE]]. Mesmo papel do Test 0 da França (commit "FR finals: correct two statements found by Test 0").

**Revisor:** subagente independente que não editou os artefatos. Leu os 11 finais (texto extraído), o SIR v1.2, a TABELA-CONSOLIDADA e as fontes de `raw/docs/oficiais/CO/`. Varreu por script todos os números de 6 dígitos ou mais contra múltiplos de SMMLV e UVT e refez as contas dos exemplos principais.

**Resultado:** 5 erros confirmados pela fonte, 16 contradições, 7 dúvidas sem fonte local.

**Conferido por mim antes de corrigir** (fonte local lida):
- nota de vigência da Circular 101/2025: "Circular derogada por el artículo 1 de la Resolución 2708 de 2026";
- Ley 797 arts. 7 e 8: o art. 7 modifica o art. 20 da Ley 100, o art. 8 modifica o art. 27;
- ET art. 55: aportes voluntários ao RAIS são INCRNGO até 25% / 2.500 UVT;
- Ley 2466 art. 14, par. transitório: 80% desde 1/7/2025 e 90% desde 1/7/2026.

## Corrigido nos finais (15 achados; texto exato em `final/scripts/test0_corrections.py`)

| ID | O que estava errado | Onde | Base |
|---|---|---|---|
| T0-01 | Circular MinTrabajo 101/2025 citada como vigente, mas foi revogada | 24 parágrafos do CCG; WTC F65, F396 e Global WTC Coverage C14 | Nota de vigência (Res. 2708/2026) |
| T0-02 | Recargo dominical de 75% e hora extra dominical de 100%, valores de antes da reforma | Payslip Unit Rate Details B8 e B9 | Ley 2466 art. 14 |
| T0-03 | FSP citado como "art. 27 Ley 100, mod. art. 7 Ley 797" | Payslip A79 (EN e ES) | Ley 797 arts. 7 e 8 |
| T0-04 | Aporte voluntário ao RAIS posto dentro do teto de 40% / 1.340 UVT | NE M193 | ET art. 55 |
| T0-05 | Teto de 1.340 UVT da retenção citado só pelo ET 336 | NE M194; Payslip A82 (EN e ES) | DUR 1.2.4.1.6 par. 3 |
| T0-06 | No diagrama do Módulo 3, os 72 UVT parecem entrar na retenção | CCG, diagrama do Módulo 3 | A-08 |
| T0-07 | Integral com a ordem "40% e depois 70%" | CCG, diagrama e parágrafo dos 70% | T4-2 |
| T0-08 | Gratificação ocasional entrando no teste de 40% | CCG, tabela de classificação | T4-5 |
| T0-12 | Teste do 114-1 só sobre "earnings", sem os dois limites | WTC F400; Form. 350 C22 e M19; DD W97 | T4-1, AT2 campo 76 |
| T0-13 | "Os quatro IBC = 70%" no integral, sem o excesso da Ley 1393 | DD W36; PILA-003 G107 | T4-2 / T4-4 |
| T0-14 | Teste do 114-1 descrito só com um limite | CCG, exemplo do integral | T4-1 |
| T0-15 | SMMLV pelo Decreto 0159/2026, que perdeu efeito | PILA-007 Example Analysis D4 | Auto do CE de 9/7/2026 |
| T0-16 | Auxílio de transporte na base da indenização do art. 64 | NE M87, C25, D23 e D32; PILA-003 C26 | CST art. 64 + 127; T4-3 |
| T0-17 | Rótulos de conciliação misturando valor arredondado e não arredondado | Form. 350 B38; Form. 220 B36; Formato 2276 D27 | Guia do 220; DUR 1.6.1.11.11 |
| T0-19 | "per month" sobrando depois de "no monthly apportionment" | WTC Tax Credit A54 | Coerência com A53 |

**Reconferência depois das correções:**
- `release_crosscheck.py`: PASS, com cada correção declarada e provada;
- `docx validate`: PASS;
- `validate_workbook`: PASS nos 10 xlsx;
- nenhuma citação da Circular 101 ficou sem a nota de revogação no CCG, e nenhuma ficou no WTC.

## Não corrigido: decisão do usuário

> **Atualização de 30/10:** todos os itens abaixo foram decididos com fonte primária e aplicados nos finais. Ver [[RESIDUOS-DECISOES]].

Ou é mudança de classificação do WTC, que exige decidir a natureza de cada verba, ou a confiança ficou abaixo de 80%.

| ID | Achado | Por que ficou | Recomendação |
|---|---|---|---|
| T0-09 | WTC linhas 228 e 229 (auxílio-nascimento e casamento): F diz "mera liberalidad", mas V está "pacted" e Q/R/S/U "Yes/No" | Reclassificar muda a base | Se for mera liberalidade de fato: "non-remunerative" e Q/R/S/U = No |
| T0-10 | WTC linhas 175, 176, 201–217, 226 e 267: "non-remunerative" com Q/R/S/U "Yes/No" e AB "included in the Ley 1393 base" | Depende da natureza de cada verba (carro e mudança: meio de trabalho ou pacto?) | 175–176 = cópia de 173–174; 267 = "pacted"; 217 e 226 = No |
| T0-11 | WTC U260–U264 = "Yes", enquanto as linhas 255–259 têm "Yes/No" | Muda taxabilidade | U = "Yes/No" (Ley 1393 vale para os arts. 18 e 204) |
| T0-18 | Payslip H36: FSP arredondado para cima de 100 (convenção da PILA) | 70%; o valor do exemplo não muda | Usar ROUND ao peso, como H34/H35 |
| T0-20 | DD W46: os 72 UVT aparecem sem a ressalva "só na declaração anual" | 60% | Acrescentar a ressalva |
| T0-21 | NE M135: bônus não salarial "conta no teste de 40%" sem condição | 65% | Condicionar ao pacto do art. 128 |
| C1–C7 | Residência no ano do 183º dia × "desde el segundo año"; 184º dia em 31/12; CST 236A; saúde de 10% do pensionista; auxílio integral em meio período; vencimento do 350 para NIT 6; WTC linha 123 | Sem fonte local | Pesquisar antes de mexer |

## Bloco de prova
- **Pedido → resposta:**
  - revisor independente, que não editou nada;
  - achados conferidos contra a TABELA e as fontes oficiais;
  - corrigido o confirmado, com o registro nos changelogs;
  - reconferido com a ferramenta do passo 3.
- **Fontes:** as da coluna "Base" e, no detalhe, as de `test0_corrections.py`. Reli eu mesmo as 4 fontes listadas acima.
- **Teste:** `release_crosscheck.py` PASS; `validate.py` (docx) PASS; `validate_workbook` PASS; varredura das citações da Circular 101.
- **Confiança:**
  - 92% nas correções aplicadas;
  - T0-16 85%: a Ley 1/1963 não está no material local, e a correção se apoia no CST 64/127 e na decisão T4-3;
  - T0-12 75–90%, conforme o ponto.

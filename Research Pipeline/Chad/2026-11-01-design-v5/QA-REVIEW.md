# Chade — design v5: revisão independente de QA (rodada 1)

> Hub: [[Chade]] · Revisado: [[CONFERENCIA]] (v5) · Vereditos: [[LEI-VEREDITOS]]
> Revisor: compliance-qa-auditor (instância independente; não construiu o v5). Data: 2026-11-01. Modo: **só leitura**. Este é o único arquivo gravado; nada no v5, no hub, em `correcoes.md`, no Drive ou em ticket foi alterado. O `PROPAGATION-LEDGER.md` não foi tocado (fora do pedido).

## Veredito: **FAIL** (rodada 1)

| Severidade | Qtde |
|---|---|
| blocker | 2 |
| major | 7 |
| minor | 13 |

A aritmética está certa: os 12 cenários e os 11 extras batem com a minha conta à mão, e o `_build_v5.py` rodado de novo numa cópia no scratchpad gera o mesmo `SKILL.md`, byte a byte. O cerne estatutário (tabela, 45-2°/4°/9°/13°/15°, 46-III, 47, TF/TA, PSA, não residente pela tabela, taxas e teto da CNPS) confere com os textos primários. O FAIL vem de quatro coisas: (1) TFE com fração de franco em XAF (C28); (2) marcas abertas no artefato (C29); (3) um método de retenção que não foi sinalizado (anualizar ×12 o pagamento irregular); (4) uma regra legal faltando (operário no art. 3-4°) que a validação dá como "✅".

## O que foi feito (prova)
- **Fontes primárias abertas por mim** (md5 conferido igual ao declarado): CGI 2026 DGI `.txt` (`7f219acf…`; PDF `139d5326…`): arts. 1-IV (l. 563–583), 2 (l. 589–702), 3 (l. 703–719), 9 (l. 815), 44–47 (l. 2502–2726), 49 (l. 2751), 116 (l. 4334), 158 (l. 5951), 173–190 (l. 6287–6582), 837–839 (l. 18972–18990), 847 (l. 19140), 857. LF 2026 OCR: art. 3 (tabela), art. 5 (art. 3-3° suprimido), l. 578 (45-4°). LF 2024: arts. 837–839 (l. 783–802). Guia CNPS 2019 `.txt`, p. 6–12. Dec. 1635 e 1636/2009: texto extraído dos PDFs (droit-afrique, nível B). WTC V3.0 export (`04e06a49…`), 618 códigos, lida com openpyxl.
- **Reexecução:** `_build_v5.py` copiado para o scratchpad e rodado (`python -I`): `SKILL.md` idêntico; `VALIDATION-run.txt` idêntico no conteúdo (só muda a codificação do stdout). `comparar.py`/`sim_dev.py`: md5 `0e3709fe…`/`12d1108d…`, iguais aos de 30/10.
- **WebFetch não usado:** a P2 foi feita contra as cópias primárias arquivadas em `raw/docs/oficiais/TD/` (com md5), não contra os sites.

---

## Passe 1 — Rastreio de cada número à fonte (lido no texto)

| Valor no v5 | Onde (`_build_v5.py`) | Fonte lida | Resultado |
|---|---|---|---|
| Faixas 0 / 10,5 / 15 / 20 / 25 / 30% em 800.000 / 6M / 7,5M / 9M / 12M | 194–197 | CGI art. 1-IV (l. 572–583); LF 2026 art. 3 | ✅ (limites `.99`: ver m1) |
| 5.000 por filho/mês menos o abono CNPS | 139–142 | art. 45-4° (l. 2551–2570); LF 2026 l. 578 | ✅ (escopo do empregador: m7) |
| 15% de (salários + verbas) | 136–138, 151–154 | art. 45-2° | ✅ |
| 30% do salário-base, transporte para todos | 134, 143–145 | art. 45-13° | ✅ |
| 1 bilhete/ano/pessoa | 155–158 | art. 45-15° | ✅ |
| bolsa fora do IRPP | 164–167 | art. 45-9° | ✅ |
| 3,5% aposentadoria obrigatória | 134, 187–190 | art. 47-I/II | ✅ |
| 20/10/15 (75.000/mês)/5/4/4/4/3/2 | 97–107 | art. 46-III | ✅ |
| TF 7,5%; TA 12‰; fração ≤ 1.000 desprezada; dezena | 215–220 | arts. 190, 178, 177 | ✅ taxas; aplicação do art. 177 por empregado: m2 |
| 50% TF/TA | 216, 219 | art. 158 | ✅ |
| < 35 anos, regime do real (TF/TA) | 55–57 | arts. 188-10°, 174-3° | ✅ |
| 60 meses (jovem graduado, IRPP) | 64, 199 | art. 3-4° ("cinq ans") | ✅ prazo; faltam idade, regime e operário: M2 |
| PSA 400/mês | 221–223 | arts. 837–839 | ✅ |
| Não residente pela tabela; 18% só para 2-VI e 60 | 199–200, 204–209 | arts. 2-III/VI, 44-II-2°, 49-I, 116, 847, 857 | ✅ leitura confirmada |
| CNPS 7,5 PFM / 5 + 3,5 PVID | 27 | Dec. 1635 art. 1; Dec. 1636 art. 1 (nível B) + guia p. 8 (A−) | ✅ duas fontes |
| CNPS AT/MP 4% | 27 | **só** o guia p. 8 (Dec. 1634 não obtido) | ⚠️ uma fonte institucional (M7) |
| Teto 500.000/mês (6.000.000/ano) | 27, 175 | Dec. 1635 art. 4 ("500.000", sem período); Dec. 1636 art. 3; guia p. 9 e 12 | ✅ |
| Piso 60.000 (SMIG 59.995 de 2011) | 27, 174 | **só** o guia de 2019 p. 7 e 9, citando o Dec. 1111/2011 | ⚠️ vigência em 2026 não comprovada (M7) |
| "a partir de 2009-12-04" | 21, 24 | só no guia p. 8; o texto do decreto diz "de 2009", com efeito na assinatura | ⚠️ m13 |
| 58106 = 60.000 (limite do DAS) | 129–131 | sem fonte; o próprio v5 diz que é parâmetro de relatório (A16) | sinalizado |

**Valores copiados do Congo ou da Costa do Marfim:** nenhum. Procurei `Congo|Ivoire|CNSS|ITS|IGR|CMU|FDFP|IPRES…` em todos os arquivos do v5 e só achei a menção histórica em `RESEARCH_GAPS.md:8` (o v4 dizia "Congo wording"). O 5.000 por filho, antes tachado de "valor da CNPS da CI" (`correcoes.md:57`, hub l. 92), **é do Chade**: está no art. 45-4° do CGI 2026 e no LF 2026.

## Passe 2 — Os 12 cenários refeitos à mão

Convenção: base anual = base mensal × 12; tabela do art. 1-IV; ÷ 12; FLOOR(x+0,5). Líquido = dinheiro 62xxx − CNPS EE − IRPP − PSA − 21xxx.

| # | Conta à mão (resumo) | CNPS EE | IRPP | TFE | TAFP | PSA | Líquido | v5 |
|---|---|---|---|---|---|---|---|---|
| 1 | 350.000; tributável 337.750 → (4.053.000−800.000)×10,5%/12 = 28.463,75 | 12.250 | 28.464 | 26.250 | 4.200 | 400 | 308.886 | = |
| 2 | sem pagamento: piso não cria base; PSA exige 58105 > 0 | 0 | 0 | 0 | 0 | 0 | 0 | = |
| 3 | 700.000; CNPS teto 500.000; 682.500×12 = 8.190.000 → 546.000+225.000+138.000 = 909.000/12 | 17.500 | 75.750 | 52.500 | 8.400 | 400 | 606.350 | = (ver M1) |
| 4 | 600.000 + moradia 50.000 (teto 120.000); 632.500×12 → 789.000/12 | 17.500 | 65.750 | 48.750 | 7.800 | 400 | 516.350 | = |
| 5 | 300.000 + indenização 900.000 (fora da CNPS e da TFE); 1.189.500×12 = 14.274.000 → 2.503.200/12 | 10.500 | 208.600 | 22.500 | 3.600 | 400 | 980.500 | = (ver M1) |
| 6 | 400.000; pensão 30.000 com teto de 14.000; 372.000×12 → 384.720/12 | 14.000 | 32.060 | 30.000 | 4.800 | 400 | 323.540 | = |
| 7 | 300.000 + transporte 120.000 (90.000 isento; CNPS sem transporte); 319.500×12 = 3.834.000 → 318.570/12 = **26.547,5** | 10.500 | **26.548** | 31.500 | 5.040 | 400 | **382.552** | **26.547 / 382.553** |
| 8 | 300.000 + abono 30.000, 0 filhos (tudo tributável); 319.500 → **26.547,5** | 10.500 | **26.548** | 24.750 | 3.960 | 400 | **292.552** | **26.547 / 292.553** |
| 9 | igual ao 1; TF/TA × 0,5 | 12.250 | 28.464 | 13.125 | 2.100 | 400 | 308.886 | = |
| 10 | jovem graduado, mês 30, 30 anos, regime do real | 12.250 | 0 | 0 | 0 | 400 | 337.350 | = |
| 11 | não residente, 800.000; 782.500×12 = 9.390.000 → 546.000+225.000+300.000+97.500 = 1.168.500/12 | 17.500 | 97.375 | 60.000 | 9.600 | 400 | 684.725 | = |
| 12 | 6 filhos: isento 30.000; 289.500×12 = 3.474.000 → 280.770/12 = **23.397,5** | 10.500 | **23.398** | 24.750 | 3.960 | 400 | **295.702** | **23.397 / 295.703** |

Os 11 extras (E1–E11) também batem com a conta à mão. Cálculo, por exemplo, do E3: CNPS 340.500 × 3,5% = 11.917,5 → 11.918; IRPP 27.501,11 → 27.501; TFE 25.537,5. Do E4: isento = 15% × 401.000 = 60.150; IRPP 27.686,75 → 27.687; TAFP 4.812 → 4.810.

**Diferença de 1 XAF nos cenários 7, 8 e 12: quem está errado é o v5, não o valor esperado.** Nos três casos o IRPP mensal exato pela tabela é meio franco (26.547,5 e 23.397,5). O v5 grava `incomeTo` = 800.000,99 (`_build_v5.py:195`), e o motor local começa a faixa seguinte nesse limite (`_build_v5.py:320`). Assim, (X − 800.000,99) × 10,5% / 12 dá 26.547,4913, que arredonda para baixo. A tabela do art. 1-IV tributa o franco 800.001 em diante, ou seja, (X − 800.000). Conferido em Python: com limite 800.000, o resultado é 26.547,5 exato, que arredonda para 26.548. O valor esperado (meia unidade para cima, que é convenção e não regra do CGI) está certo. O erro de construção é do v5 (m1).

## Passe 3 — Coerência interna (resumo)
- **Ordinais:** todas as dependências rodam depois de quem as produz (58109→14→21; 58105→15/16→22/24; 31–39→41; 53→71; 61→71; 72→73/75; 81/82→83/84). ✅
- **Bases que apontam para regulações:** toda conta lida é escrita antes, dentro do design. Mas **cerca de 20 contas intermediárias e de razão não existem na WTC V3.0** (M3).
- **Isenções por tipo de empregado:** diplomata fora de tudo; deficiente e jovem graduado fora do IRPP, com TF/TA só pelo 58219; não residente em tudo. Faltam o operário do art. 3-4° no IRPP e a condição de idade e regime do jovem graduado (M2). O 58218 tem valor único, então não dá para marcar um não residente que também seja deficiente ou jovem graduado (impacto baixo agora que o não residente usa a tabela).
- **Contas da CNPS:** 2551 = EE, e 2537/2550/2560 = ER, como na WTC V3.0. ✅

## Passe 4 — Marcas residuais e afirmações sem rastreio
- `SKILL.md`: 3 ocorrências de `⚠️ PENDENTE-DECISÃO` (l. 3, 8, 143) e 2 de `⚠️ A CONFIRMAR` (l. 3/8 e 1057). A contagem da CONFERENCIA está certa. Pelo C29, isso é FAIL para a liberação (B2), embora a sinalização ao usuário esteja correta.
- Sem rastreio: diplomata fora da CNPS e da TF/TA (m8); 58131 = 20 (m3); "Flags take the meaning the global catalogue gives them" (m4).

## Passe 5 — Itens abertos: estão bem sinalizados?
| Item | Situação no v5 | Avaliação |
|---|---|---|
| Transporte inteiro fora da CNPS (AC1) | `⚠️ A CONFIRMAR`, com o efeito no cenário 7 (11.550 → 10.500) | **Sinalizado corretamente.** Falta registrar a hierarquia das normas: os Decs. 1635 art. 3 e 1636 art. 2 só excluem « remboursements des frais » e « indemnités ayant un caractère de dédommagement »; o transporte aparece só na lista do guia (p. 8). E o 6251x fica fora da CNPS sem entrar na isenção do art. 45-13° (M5, m11) |
| 62867 auxílio-óbito (P4) | `PENDENTE-DECISÃO`, tributável hoje | **Sinalizado corretamente** para o IRPP (art. 45-11° « Le capital décès »). A alternativa não diz o que muda na CNPS e na TFE (m12) |
| Arredondamento do IRPP | "convenção técnica, sem regra no CGI" | **Correto quanto à lei**: não há regra de arredondamento do IRPP no CGI (conferi; só os arts. 177, 143, 771 e 787). Mas o barème da DGI (art. 847) **saiu do RESEARCH_GAPS** (M7), e é esse barème que decide também o método de M1 |
| Não residente pela tabela | decidido, A25 | **Leitura legal confirmada** (art. 116 → 2-VI e 60; 2-VI → direitos e art. 49; 49 exclui as rendas dos arts. 1–48; art. 857 = terceiros sem estabelecimento). R21 (Report Spec) sinalizado. Confiança declarada acima da fonte (M6) |

---

## Achados

### Blockers
| ID | Padrão | Local | Evidência | Correção | Rota |
|---|---|---|---|---|---|
| B1 | C28 | `_build_v5.py:215–217` (9148083); `chad-design-blueprint-claude-v5/VALIDATION.md:38` (E3) | A TFE é lançada em 2563 sem arredondamento: E3 dá **25.537,5 XAF**. O XAF não tem subunidade (o próprio v5 diz isso em 9148073, `_build_v5.py:203`). O art. 190 não traz regra, mas um passivo com fração de franco não é pagável | Arredondar a TFE ao franco inteiro com convenção explícita (FLOOR(x+0,5), marcada como "convenção técnica, sem regra no CGI", igual ao IRPP) **ou** acumular a fração e arredondar só no total da empresa. Atualizar E3 para 25.538 | builder |
| B2 | C29 | `chad-design-blueprint-claude-v5/SKILL.md:3, 8, 143, 1057` | `⚠️ PENDENTE-DECISÃO` (P4) e `⚠️ A CONFIRMAR COM O USUÁRIO` (transporte) dentro do artefato | Decidir P4 e AC1 com o usuário e tirar as marcas. Até lá, o v5 não vai ao Dev (a CONFERENCIA já diz "Não pronto para o Dev") | usuário → builder |

### Major
| ID | Padrão | Local | Evidência | Correção | Rota |
|---|---|---|---|---|---|
| M1 | método / G-BUILD | `_build_v5.py:194–199` (9148072 `retro_simple_tax`, divisão por período); `_build_v5.py:315–323`; `ASSUMPTIONS.md` (sem item) | Cada mês é anualizado ×12, inclusive o pagamento irregular. Cenário 5: indenização de 900.000 retém **208.600** no mês. Pela renda anual (art. 1-I, « impôt annuel »; art. 1-IV, « Revenus annuels »), com 11 meses de 300.000, o imposto do ano é 375.270, e o saldo do mês da indenização seria cerca de 117.898: **≈ 90.700 retidos a mais**. Cenário 3 (13º): ≈ 11.100 a mais. E8 (excesso de passagem), mesma coisa. O Dev faz o mesmo (`x/2  CT-A-588.md`, 9148201/211/221), por isso a comparação não pega | Abrir item no ASSUMPTIONS ("método da retenção mensal para pagamento irregular: anualização simples × cumulativo/YTD × tratamento separado da gratificação; o barème da DGI do art. 847 decide") e, se aprovado, modelar YTD/cumulativo. Marcar os cenários 3 e 5 como "dependem do método" | fonte (barème DGI) → builder |
| M2 | F3 / lei | `_build_v5.py:64, 371`; `ASSUMPTIONS.md:28` (A19); `VALIDATION.md:41` (E5 ✅) | Art. 3-4° (CGI l. 715–719): « Les salaires versés aux jeunes diplômés âgés de moins de 35 ans **et aux ouvriers** recrutés par les entreprises du régime du réel… pendant une période de cinq ans » são isentos de IRPP. O E5 (operário de 25 anos, empresa do regime real) espera IRPP **28.464** e marca ✅. O jovem graduado é isento sem testar idade < 35 nem regime do real (58215). O A19 reconhece, mas a validação afirma como certo pela lei um valor que a lei contradiz | Construir no IRPP: isenção = 58215 = 1 e [(jovem graduado e 58216 < 35) ou operário] e meses ≤ 60, com contador de meses para o operário. Ou, se ficar para o v6, tirar o ✅ do E5 e marcar "fora da lei por decisão de escopo (A19)" | builder |
| M3 | G-BUILD / F25 | `ASSUMPTIONS.md:23` (A14); `_build_v5.py` inteiro | O A14 diz que as contas novas são 58114, 58115, 58173 e 2570. Na WTC V3.0 **também faltam** 58106, 58109, 58113, 58141, 58142, 58152, 58161–58169, 58171, 58172 (intermediárias), 2610, 6020, 6034, 6037, 6040, 6063 (razão) e 21600/21610/21611/21670/21699 (o cenário 6 usa 21600, que não existe). A V3.0 tem intermediárias próprias que o v5 ignora: 58100 « TD CNPS Contribution EE », 58103 « Transport Allowance Exemption », 58110/58111/58112 (anualizada / anual / período), as mesmas que o Dev usa | Refazer o A14 com a lista completa, vinda da WTC, e para cada conta escolher: reusar a da V3.0 (58100 no lugar de 58141, 58110–58112 no lugar de 58152) ou pedir criação (entrada no RESEARCH_GAPS) | builder |
| M4 | lei / TA | `_build_v5.py:81, 212–214` (9148082 usa `TFE_BASE`) | Art. 173 (CGI l. 6287): a TA incide sobre « appointements, salaires, avantages en nature et rétributions quelconques, **y compris les gratifications servies régulièrement** ». O art. 189-1° (TF) diz « gratifications » sem qualificar. A contrario, a gratificação não regular pode ficar fora da TA. A WTC V3.0 marca 62220–62229 « Bonuses – discretionary or one-time » e 62300/62305 (férias) com Apprenticeship **No**. O v5 usa a mesma base nas duas sem dizer por quê | Matriz própria da TAFP, ou item `PENDENTE-DECISÃO` com as duas leituras e a fonte. No mínimo, uma linha no ASSUMPTIONS e na nota da 9148082 | fonte → builder |
| M5 | coerência | `_build_v5.py:85` (`6251%` No na CNPS) × `_build_v5.py:144` (9148021 só `6252%`) | 62510–62512 « Car & Transportation allowance » sai inteiro da CNPS (como "transporte", guia p. 8) mas não entra na isenção de 30% do art. 45-13° no IRPP. Ou é transporte nas duas, ou em nenhuma | Decidir a natureza do 6251x e aplicar o mesmo tratamento: incluir `6251%` na 9148021 ou devolvê-lo à base da CNPS | builder |
| M6 | regra 11 (confiança) | `CONFERENCIA.md:69` | Declara "95% nas mudanças do CGI (1–10, **14–16**)". A fonte que o v5 diz seguir dá **85%** para o não residente (LEI-VEREDITOS B1, item 9/10) e **75%** para passagem/diárias (B1, item 26) | Mudar para 14 = 85%, 15–16 = 75%, e repetir os mesmos números no hub quando registrar | builder |
| M7 | G-PROP / C41 | `chad-design-blueprint-claude-v5/RESEARCH_GAPS.md` (sem itens) × `LEI-VEREDITOS.md` §B3 | Ficaram fora do RESEARCH_GAPS do v5: (a) **SMIG/piso** (o 60.000 vem do Dec. 1111/2011, citado só pelo guia de 2019; nenhuma fonte de 2026); (b) **barème da DGI** (art. 847), que decide o arredondamento e o M1; (c) texto do **Dec. 1634/2009**: o AT/MP 4% depende só do guia; (d) **arrêté** de avaliação da espécie (Dec. 1635 art. 5); (e) notas circulares da CNPS de 2025 (n° 023, 077, 107). A CONFERENCIA põe o piso em "75–85%", mas não há item que diga o que fecharia a lacuna | Acrescentar R22–R26 com fonte que fecharia cada um. O piso de 2026 vai ao source-hunter (fonte oficial A.1/A.2 do SMIG vigente) | source-hunter |

### Minor
| ID | Padrão | Local | Evidência | Correção | Rota |
|---|---|---|---|---|---|
| m1 | lei / validação | `_build_v5.py:195–197, 320, 380, 404` | Limites `x.99` → 1 XAF abaixo nos cenários 7/8/12 (Passe 2). Além disso, o status EDGE aceita até 1 XAF **em todas as colunas** desses cenários, o que esconderia um erro real de 1 XAF na CNPS ou na TFE | Gravar `incomeTo` = 800.000 / 6.000.000 / 7.500.000 / 9.000.000 / 12.000.000, com `incomeFrom` da faixa seguinte igual (se o motor aceitar). Reexecutar: 12/12 exatos. Restringir o EDGE à coluna IRPP | builder |
| m2 | lei | `_build_v5.py:213, 219` | Art. 177: « toute fraction du **montant global** des appointements imposables n'excédant pas 1.000 Francs est négligée. Le montant des impositions est arrondi… ». O v5 trunca e arredonda **por empregado**, e a soma fica abaixo do cálculo sobre o total da empresa | Registrar no ASSUMPTIONS como limitação de motor (por empregado × global), com o efeito máximo de cerca de 12 XAF por empregado, ou fazer o ajuste no relatório da TAFP | builder |
| m3 | G-BUILD | `_build_v5.py:182` (banda 6 → 58131); `ASSUMPTIONS.md:24` | Na WTC V3.0, 58131 = « TD CNPS Contribution EE ». O v5 grava ali a **taxa** 20, e grava também com salário zero, porque a fórmula roda sem base | Usar conta própria para a taxa total ou ler a taxa como constante no relatório. Condicionar a 58550 > 0 | builder |
| m4 | G-BUILD | `_build_v5.py:38–40, 243` | Na WTC V3.0, 58205 = « Young Graduate Start Date » (Flag). O v5 grava ali a contagem de meses e afirma que os flags têm "the meaning the global catalogue gives them" | Conta nova para a contagem, ou corrigir a frase e o nome do flag | builder |
| m5 | lei / TF | `_build_v5.py:72–77, 81` (`CASH_GROSS` sem `6264%`) | Os arts. 187 e 189-1° incluem « pensions (de retraite) » na base da TF. 62640–62649 « Pensions & Pension Refunds » ficam fora da TFE (certo para o IRPP, art. 45-1°, e para a TA, art. 173) | `('62649','6264%','Yes')` só na `TFE_BASE`, ou nota de que pensão não passa pela folha | builder |
| m6 | coerência / G-PROP | `_build_v5.py:85–86, 92`; `RESEARCH_GAPS.md:25` | 62780–62782 « Family allowance » têm CNPS **Yes** na V3.0; o v5 põe No, e o R19 não lista essa divergência. 62590/62591 « Birth and Marriage Allowance » ficam fora do teto do art. 45-4°, enquanto 62866 « Birth allowance » entra | Acrescentar 6278x ao R19; decidir se 6259x entra em `FAMILY` | builder |
| m7 | lei | `_build_v5.py:139–142` (9148016) | Art. 45-4°: o teto vale para o « montant total des allocations versées par l'employeur **autre que l'État, les Communes ou les organismes para administratifs** ». O v5 aplica a todos | Uma linha na nota (escopo = empregador privado) ou condição por tipo de entidade | builder |
| m8 | sem rastreio | `_build_v5.py:63, 67, 168, 172` | O diplomata fica fora da CNPS e da TF/TA sem fonte primária. O art. 188-5° isenta « ambassades étrangères » como **pagador**, não o empregado; a exclusão da CNPS vem só da skill (hub l. 54) | Citar a fonte ou anotar no ASSUMPTIONS | source-hunter |
| m9 | coerência | `chad-design-blueprint-claude-v5/CHANGELOG.md:36` | "the 12 scenarios and **9** extra checks"; o VALIDATION tem 11 (E1–E11) | Trocar para 11 | builder (direto) |
| m10 | rótulo velho | `simulacao/RESULTADO.md:1–3` | Cabeçalho "Feito em 2026-10-30… 10 cenarios do v4 rodados no v5", gerado pelo `comparar.py` sem alteração, numa saída de 01/11 | Corrigir a data e o texto no `rodar_comparar_v5.py`, fora do `comparar.py` | builder |
| m11 | sinalização | `chad-design-blueprint-claude-v5/ASSUMPTIONS.md:8` (AC1) | O item não diz que o texto dos decretos (norma superior) não cita o transporte; quem o lista é o guia p. 8 | Acrescentar "Dec. 1635 art. 3 / 1636 art. 2: só reembolso e dédommagement; transporte só no guia" para o usuário decidir sabendo disso | builder |
| m12 | sinalização | `ASSUMPTIONS.md:7` (P4) | A alternativa "isento" só mexe no `CASH_GROSS`. Pelo art. 189-1°, a TFE continua a incluir; na CNPS, o Dec. 1635 só exclui as prestações **legais** (pagas pela CNPS) | Descrever o efeito da alternativa em IRPP, TFE/TAFP e CNPS | builder |
| m13 | P2 / nível | `_build_v5.py:21, 24` | "from 2009-12-04" só aparece no guia p. 8. O texto dos decretos (droit-afrique, nível B) diz "de 2009", com efeito na assinatura | Citar a data como "guia p. 8" e registrar o Journal Officiel como fonte que falta | source-hunter |

---

## Propagação (para quem registrar; não fiz nenhuma alteração)
- B1/m1: muda o valor esperado de E3 e dos cenários 7/8/12. Consumidores: VALIDATION.md, VALIDATION-run.txt, CONFERENCIA §Conferência, simulação v5 × Dev.
- M1/M7: hub `paises/Chade.md` (Pendências), Report Spec IRPP-TS (DGI-001), CCG (método de retenção), skill `payroll-compliance-chad`.
- M5/AC1: `correcoes.md:59` (2026-07-07, transporte) e hub l. 95: já anotados no "Fora do pedido" da CONFERENCIA.
- m6: WTC V3.0 (6278x CNPS), junto com R18/R19.

## Checagens rodadas
P1–P5 completos. C28, C29, C30 (nível da fonte), C32 (mesmo valor em todo lugar: 400, 5.000, 15%, 60.000 e 500.000 são iguais em SKILL/CHANGELOG/ASSUMPTIONS/CONFERENCIA), F3, F18 (LF 2026 × CGI 2026: art. 3-3° suprimido, 45-18° vigente; tabela igual), F24 (sem MANDATE, n/a), F26 (nenhum valor calculado como flag de DD, exceto m4), G-BUILD, G-PROP, G-DERIVE (12 + 11 cenários refeitos). Não aplicáveis aqui (não é uma rodada do pipeline): C38/C40/C42–C46/C48–C71, `preflight_check.py`.

## Próximo passo
Rodada 2 com o builder: B1, M2, M3, M5, M6, m1–m4, m9, m10. Com o usuário: B2 (P4 e AC1), M4 e o método de M1. Com o source-hunter: M7, m8, m13. Teto de 3 rodadas.

| Data | Frente | O quê |
|---|---|---|
| 2026-11-01 | QA independente (frente Chade) | revisão adversarial do v5, rodada 1: FAIL (2 blocker, 7 major, 13 minor) |
| 2026-11-01 | QA independente (frente Chade) | rodada 2: FAIL (0 blocker, 3 major, 1 minor, todos novos); 22/22 achados da rodada 1 fechados |

---

# Rodada 2 (2026-11-01, depois da "rodada 3 pós-QA" do construtor)

## Veredito: **FAIL** (0 blocker, 3 major, 1 minor; todos novos)

Dos 22 achados da rodada 1, os 22 estão fechados. As correções introduziram dois defeitos novos e um problema de rastreio. Esta é a **rodada 2 de 3** do teto: se a rodada 3 falhar, o caso sobe para uma pessoa.

## Como conferi
- `_build_v5.py` novo copiado para o scratchpad e executado (`python -I`, rc 0). O `SKILL.md` gerado é **idêntico** ao da pasta. Rodei casos de borda que não estão no script, chamando o `outcome()` do próprio motor.
- Diff linha a linha entre o `_build_v5.py` da rodada 1 e o atual.
- Contas: todas as contas 58xxx e de 4 dígitos do script cruzadas com a WTC V3.0 (openpyxl) e com o texto do A14.
- Origem das "decisões do usuário": `frentes/chade/estado.md`, `log.md` e mensagens do usuário nas conversas da frente Chade (`~/.claude/projects/*frentes-chade*/*.jsonl`).

## Cenários refeitos à mão (faixas agora com limite redondo: imposto a partir do franco 800.001)
| # | Conta | IRPP | TFE | TAFP | Líquido | v5 |
|---|---|---|---|---|---|---|
| 3 | 682.500×12 = 8.190.000 → 546.000 + 225.000 + 138.000 = 909.000 / 12 | 75.750 | 52.500 | 8.400 | 606.350 | = |
| 5 | 1.189.500×12 = 14.274.000 → 2.503.200 / 12 | 208.600 | 22.500 | 3.600 | 980.500 | = (método: A26) |
| 7 | 319.500×12 = 3.834.000 → 318.570 / 12 = 26.547,5 → 26.548 | 26.548 | 31.500 | 5.040 | 382.552 | = (1 XAF resolvido) |
| 8 | igual ao 7 (0 filhos) | 26.548 | 24.750 | 3.960 | 292.552 | = |
| 11 | 782.500×12 = 9.390.000 → 1.168.500 / 12 | 97.375 | 60.000 | 9.600 | 684.725 | = |
| 12 | 289.500×12 = 3.474.000 → 280.770 / 12 = 23.397,5 → 23.398 | 23.398 | 24.750 | 3.960 | 295.702 | = |
| E15 | bônus único 6222x 100.000: CNPS 400.000 → 14.000; IRPP sobre 386.000 = 402.360 / 12; TAFP só sobre 300.000 | 33.530 | 30.000 | 3.600 | 352.070 | = |
| E16 | 6251x 120.000 = cenário 7 (30% = 90.000 isento; fora da CNPS) | 26.548 | 31.500 | 5.040 | 382.552 | = |
| E17 | pensão 6264x 50.000: fora do IRPP (45-1°), da CNPS e da TA; dentro da TF (art. 189-1° « pensions ») → TFE 350.000 × 7,5%; IRPP sobre 289.500 | 23.398 | 26.250 | 3.600 | 315.702 | = |
| E3 | TFE 25.537,5 → 25.538 (convenção de pagamento) | 27.501 | 25.538 | 4.080 | 300.681 | = |
| E5 / E12 / E14 | operário mês 30 isento; jovem graduado de 36 anos na contratação tributado; operário mês 61 tributado no IRPP e ainda isento de TF/TA | 0 / 28.464 / 28.464 | 0 / 26.250 / 0 | 0 / 4.200 / 0 | — | = |

## Achados da rodada 1: situação
| ID | Situação | Evidência |
|---|---|---|
| B1 | ✅ fechado | `_build_v5.py:224–225`: TFE FLOOR(x+0,5) com a redução dentro, marcada como convenção de pagamento; E3 = 25.538 |
| B2 | ✅ marcas retiradas | `SKILL.md`: 0 `PENDENTE`/`A CONFIRMAR`. **A atribuição das decisões está errada: ver N3** |
| M1 | ✅ documentado | A26: método, efeito (≈ 117.898 × 208.600) e R23 (barème da DGI). Não construído, o que é aceitável como limitação nomeada |
| M2 | ✅ construído | 58226 + 58225; E5, E12, E13, E14. **Regressão: N1; leitura do operário: N2** |
| M3 | ✅ fechado | A14 completo: todas as contas fora da V3.0 aparecem no A14 (faixas 58161–58169, 58202–58204, 58215–58217). 58100, 58101, 58103 e 58112 existem na V3.0. Renomeações pedidas em R27 |
| M4 | ✅ fechado | `TAFP_BASE` (`_build_v5.py:89`): 6222% No; 6264% fora. A30 |
| M5 | ✅ fechado | 9148021 com `6251%` (`_build_v5.py:152`); E16 |
| M6 | ✅ fechado | `CONFERENCIA.md:82`: 85% / 75% iguais aos da LEI-VEREDITOS |
| M7 | ✅ fechado | RESEARCH_GAPS R22–R26, R29, R30 |
| m1 | ✅ | limites redondos; `EDGE = set()`; 12/12 e 17/17 exatos sem tolerância. Fica no A21 a pergunta se o motor aceita limites iguais |
| m2 | ✅ | A31 |
| m3 | ✅ | banda 6 com `GREATER($58550;0)` |
| m4 | ✅ | flag renomeado, frase do catálogo corrigida, R27 |
| m5 | ✅ | `6264%` só na `TFE_BASE`; E17 |
| m6 | ✅ | R19 com 6278x e 6222x/62300/623xx; A33 (6259x) |
| m7 | ✅ | A29 |
| m8 | ✅ | A32 + R30 |
| m9 | ✅ | CHANGELOG: 17 extras |
| m10 | ✅ | cabeçalho do RESULTADO.md "Gerado em 2026-11-01" |
| m11 | ✅ | D1, nota de hierarquia das normas |
| m12 | ✅ | D2 + R28 (efeito em IRPP, TF/TA e CNPS) |
| m13 | ✅ | CNPS_SRC (`_build_v5.py:21`) + R29 |

## Achados novos
| ID | Sev. | Local | Evidência | Correção | Rota |
|---|---|---|---|---|---|
| N1 | **major** | `_build_v5.py:60–62` (58226); `_build_v5.py:38–40` (58205); RES l. 356 (58205 = 0 por padrão) | O operário (58217 = 1) **sem data de início** tem 58205 = 0. Então `LESS($58205;61)` é verdadeiro e o empregado fica **isento de IRPP para sempre**. Probe no motor do próprio script: operário de 45 anos, empresa do regime real, sem data → IRPP **0** (devido: 28.464). O mesmo vale para o jovem graduado sem data. No motor real, DAYS_BETWEEN com data vazia tem comportamento desconhecido | Exigir a data: acrescentar `GREATER($58205;0)` no 58226 e tornar o campo `young_graduate_employee_exemption_start_date` obrigatório no DD quando 58217 = 1 ou 58218 = 3. Acrescentar cenário "operário sem data → tributado" | builder |
| N2 | **major** | `ASSUMPTIONS.md:28, 36` (A19, A27); `CONFERENCIA.md:25` (decisão 11) | "Operário sem limite de idade no IRPP" é uma leitura de efeito grande: todo operário recrutado por empresa do regime real fica isento de IRPP por 5 anos, sem limite de idade. Pela gramática do art. 3-4°, a idade só acompanha « jeunes diplômés ». Mas os arts. 188-10° (TF) e 174-3° (TA), da mesma política (LFI 2021), dizem « **les ouvriers âgés de moins de 35 ans** ». O ponto não tem confiança nem alternativa escritas, como têm D1 e D2 | Registrar como decisão com alternativa ("operário < 35 anos, como nos arts. 188-10°/174-3°": efeito no E5 se tivesse 40 anos) e confiança (≤ 65%). Recomendo a leitura restritiva por coerência sistemática até haver circular da DGI. Acrescentar cenário com operário de 40 anos | builder (decisão com fonte) |
| N3 | **major** | `ASSUMPTIONS.md:3–8` ("Decisions taken by the user (1 Nov 2026)"); `CONFERENCIA.md:59–61`; `CHANGELOG.md:42` (R3-3); `_build_v5.py:136, 179` ("user decision") | Não achei mensagem do usuário que decida transporte na CNPS ou o 62867. A última mensagem do usuário na frente (2026-11-01T19:46, "sim, faça os passos 1 ao 5") aprova o plano de 18:09, cujo passo 3 é "Decidir os 3 pontos ambíguos: pesquisar… e fechar cada um com a nossa posição e a fonte". Não há registro no `estado.md` nem no `log.md`. As decisões cabem no mandato "pesquisar e decidir", mas são **nossas, não do usuário**. Rotulá-las "do usuário" esconde de quem é a responsabilidade e afeta `correcoes.md` 2026-07-07, que exige o ok do usuário | Trocar para "decisão da frente Chade (mandato do usuário de 01/11 19:46, passo 3), com fonte". Manter a correção de `correcoes.md` pendente do ok explícito do usuário. Registrar no `estado.md` da frente | builder → usuário |
| N4 | minor | `_build_v5.py:136` → `SKILL.md:145` | "alternative and its effect in ASSUMPTIONS **A28**". O A28 é o flag de status de valor único; a alternativa do 62867 está no **D2** (e no R28) | Trocar para "ASSUMPTIONS D2 / RESEARCH_GAPS R28" | builder (direto) |

## Checado sem achado
Faixas com `incomeTo` = `incomeFrom` da faixa seguinte (só falta a aceitação do motor, A21). TFE ao franco, com a redução de 50%/100% aplicada antes do arredondamento. Matriz da TAFP: precedência `6222%` No > `622%%` Yes. Contas da WTC V3.0 reaproveitadas existem com nome compatível (o 58101 "Voluntary Contribution" vai ser renomeado, R27). A26: conta conferida (375.270 − 257.372,5 = 117.897,5). Não residente: NR_SCALE, e 2592 só fora da isenção do 3-4°. Nenhuma marca residual no SKILL.md. md5 de `comparar.py`/`sim_dev.py` sem mudança.

## Próximo passo
Rodada 3 (a última): N1–N4. Se a rodada 3 falhar, o caso sobe para uma pessoa com os achados que restarem.

---

# Rodada 3 (final, 2026-11-01, depois da "rodada 4 pós-QA r2" do construtor)

## Veredito: **PASS** (0 blocker, 0 major, 0 minor novos)

Os achados N1–N4 estão fechados e não achei regressão. O teto de 3 rodadas não foi atingido com FAIL, então não há escalonamento. O PASS vale para o **design local**. Antes de ir ao Dev ainda faltam: o ok do usuário em D1/D2 (e, depois, em `correcoes.md` 2026-07-07), o método do pagamento irregular (A26, depende do barème R23) e o teste no motor real (A10–A12, A21, A23). A própria CONFERENCIA já lista esses pontos como impeditivos.

## Como conferi
- Diff entre o `_build_v5.py` da rodada 2 e o atual: as mudanças estão só no 58226, nos textos de D1/D2 e nos casos E18–E20.
- Reexecução no scratchpad (`python -I`): rc 0, `ALL EXPECTED (exact, every column)`, 12/12 cenários e 20/20 extras, `SKILL.md` idêntico ao da pasta, 0 marcas `PENDENTE`/`A CONFIRMAR`.
- Casos de borda fora do script, rodados no `outcome()` do motor: operário com 30 anos na contratação, hoje 37, mês 40 → IRPP isento, TF/TA devidas (idade atual ≥ 35, A27). Operário não residente de 25 anos, mês 10 → isento de tudo, menos CNPS e PSA. Deficiente sem data → isento de IRPP (art. 45-18°, sem prazo) e de TF/TA. Os três coerentes com a lei como o v5 a leu.

## Refeitos à mão
| # | Flags | Conta | CNPS EE | IRPP | TFE | TAFP | PSA | Líquido | v5 |
|---|---|---|---|---|---|---|---|---|---|
| E18 | operário, 45 anos, regime real, **sem data** (58205 = 0) | 58226 = 0 (`GREATER($58205;0)` falso) → tabela: 337.750×12 = 4.053.000 → 341.565/12 = 28.463,75; 58219 = 0 (45 ≥ 35) | 12.250 | 28.464 | 26.250 | 4.200 | 400 | 308.886 | = |
| E19 | operário, 40 na contratação, hoje 42, mês 30 | 58226 = 0 (58225 = 40 ≥ 35, leitura restritiva A34) → IRPP pela tabela; 58219 = 0 | 12.250 | 28.464 | 26.250 | 4.200 | 400 | 308.886 | = |
| E20 | jovem graduado, 30 anos, regime real, **sem data** | 58226 = 0 → IRPP devido; 58219 = 1 (58218 = 3, idade 30 < 35, real; os arts. 188-10°/174-3° não pedem data) → TF/TA 0 | 12.250 | 28.464 | 0 | 0 | 400 | 308.886 | = |
| 10 | jovem graduado, mês 30, 28 na contratação | 58226 = 1 → IRPP 0; 58219 = 1 → TF/TA 0; líquido 350.000 − 12.250 − 400 | 12.250 | 0 | 0 | 0 | 400 | 337.350 | = |
| E5 | operário, 25 anos, mês 30, regime real | 58226 = 1 (58225 = 28 < 35) → IRPP 0; 58219 = 1 → TF/TA 0 | 12.250 | 0 | 0 | 0 | 400 | 337.350 | = |

## N1–N4: situação
| ID | Situação | Evidência |
|---|---|---|
| N1 | ✅ fechado | `_build_v5.py:63`: `GREATER($58205;0)` no 58226. A19 e R31 (`RESEARCH_GAPS.md:37`) exigem a data no DD quando 58218 = 3 ou 58217 = 1. E18 e E20 provam que sem data o empregado é tributado |
| N2 | ✅ fechado | A34 (`ASSUMPTIONS.md:44`): leitura restritiva (< 35 na contratação também para o operário), 60%, com a alternativa e o efeito (E19: 28.464 → 0) e a mudança exata na fórmula. Base: arts. 188-10°/174-3° « les ouvriers âgés de moins de 35 ans » |
| N3 | ✅ fechado | "Technical decision of the Chade front… pending the user's ok" em `_build_v5.py:138, 181`, ASSUMPTIONS §3 (D1 75%, D2 65%), `CONFERENCIA.md:59–62` (mandato de 01/11 citado) e CHANGELOG R4-3. Nenhum "user decision" sobrou (grep) |
| N4 | ✅ fechado | `SKILL.md:145` aponta para "ASSUMPTIONS D2 / RESEARCH_GAPS R28" |

## Regressões procuradas (nenhuma)
O 58226 não alterou os cenários 10, E5, E12–E14 (refeitos ou relidos). O RES padrão (58225 = 28) não isenta ninguém sem data. NR_SCALE e RESIDENT_SCALE ainda excluem só quem tem 58226 = 1. As faixas redondas e a TFE ao franco estão iguais às da rodada 2.

| 2026-11-01 | QA independente (frente Chade) | rodada 3 (final): PASS; N1–N4 fechados, sem regressão; abertos fora do artefato: ok do usuário D1/D2, A26/R23, motor real |

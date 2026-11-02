# Chade — design v5 (conferência)

> Hub: [[Chade]] · Anterior: [[2026-10-29-design-v4/CONFERENCIA|CONFERENCIA v4]] · Vereditos: [[LEI-VEREDITOS]] · Comparação: [[COMPARACAO]] · Serviço: [[design]]
> Rascunho local, 2026-11-01 (rodadas 1, 2, 3 pós-QA e 4 pós-QA r2). **Não vai ao Drive nem ao Dev sem ok do usuário.** A pasta v4 não foi alterada.

## Fonte
- **Partida:** design v4 (`../2026-10-29-design-v4/`: `_build_v4.py`, blueprint v4, CONFERENCIA). Copiado para cá e gerado de novo por `_build_v5.py`.
- **O que mudar:** `../2026-10-29-teste-design-hrblizz/2026-10-30-export-ram/LEI-VEREDITOS.md` — rodada 1: "Revisão 2026-11-01" (R1, N4–N7) e "O que aprender do design do Dev"; rodada 2: "Revisão 2026-11-01 (b): CNPS e decisões" (B1–B3); rodada 3: `QA-REVIEW.md` desta pasta (QA independente, FAIL com 2 blocker, 7 major, 13 minor) e as decisões técnicas da frente sobre transporte na CNPS e 62867 (pendentes de ok do usuário).
- **Lei:** CGI do Chade 2026, edição DGI (`raw/docs/oficiais/TD/2026-11-01-CGI-TCHAD-2026-FINAL-dgi.pdf`, md5 `139d5326…`). Artigos relidos no texto: 3, 45, 46, 47, 116, 173, 174, 177, 178, 187–190, 837–839. "p." = página do PDF.
- **CNPS (rodada 2):** Dec. 1635 e 1636/PR/PM/MFPT/2009 e *Guide de l'employeur* da CNPS 2019 (`raw/docs/oficiais/TD/2026-11-01-*`, md5 na seção B da LEI-VEREDITOS). Relido no guia: p. 7 (base, piso), p. 8 (exclusões: transporte, deslocamento, abono), p. 12 (teto anual e regularização).
- **Códigos:** WTC V3.0 (`…/2026-10-30-export-ram/CHAD-WTC_V3.0-export-2026-11-01.xlsx`, md5 `04e06a49…`).
- **Design do Dev:** `…/x/2  CT-A-588.md` e `td.json` do Drive (simulação).

## Decisões técnicas (reversíveis)
1. Limite do abono numa regulação própria (9148016, tipo Formula, matriz = códigos de abono, conta 58107), como o Dev; a isenção (9148022) usa 58107 como conta-teto.
2. 15% do art. 45-2° como banda 10 da 9148015 + regulação 9148024, com um teto único para 6287x (código novo, R15), diária 62570 e 6557x/6558x.
3. Aposentadoria: a matriz exclui 2164x ("Voluntary Contribution" na V3.0).
4. PSA: 9148091, piso = teto 400, `_monthly`, só com 58105 > 0, todos menos diplomata; conta 2570 nova (R17).
5. Não residente pela tabela: 9148072 roda para ele; 9148074 copia 58552 em 58592 e 9148075 lança o resultado em 2592, para o relatório IRPP-TS continuar separando residente (2552) e não residente (2592).
6. Passagem de férias: 9148025 com limite anual vindo de campo novo do DD (58223), aplicado por pagamento (A24).
7. Regularização anual da CNPS em dezembro: não construída como regulação (precisa da semântica YTD do motor; A23).
8. Contas da CNPS iguais ao v4: EE → 2610/2551, ER → 6037/2537, 6020/2550, 6040/2560 (a WTC V3.0 confirma 2551 = EE e 2550 = ER).
9. (rodada 3) Faixas do IRPP com limite redondo: `incomeTo` 800.000 = `incomeFrom` da faixa seguinte (se o motor não aceitar limites iguais, o meio franco cai 1 XAF; A21).
10. (rodada 3) TFE paga ao franco inteiro, FLOOR(x+0,5): convenção técnica de pagamento (o XAF não tem fração), não arredondamento estatutário (o art. 190 não tem regra).
11. (rodadas 3–4) Isenção do art. 3-4° por flag derivado 58226: empresa do regime real, data de início informada e até 60 meses (0 < 58205 ≤ 60; data obrigatória no DD, R31), menos de 35 anos na contratação (58225) e jovem graduado ou operário. **Operário também < 35 (rodada 4): decisão técnica da frente, 60%.** O art. 3-4° (CGI 2026 p. 15, « jeunes diplômés âgés de moins de 35 ans et aux ouvriers recrutés… ») só liga a idade ao jovem diplomado, mas não a afasta expressamente para o operário, e os arts. 188-10°/174-3° (mesma LFI 2021) dizem « les ouvriers âgés de moins de 35 ans ». Alternativa: operário sem limite de idade (E19 pagaria IRPP 0 em vez de 28.464). ASSUMPTIONS A34, RESEARCH_GAPS R32.
12. (rodada 3) Contas intermediárias da WTC V3.0 reaproveitadas: 58100, 58101, 58103, 58112 (no lugar de 58141, 58142, 58171, 58152). O `rodar_comparar_v5.py` troca essas duas contas em memória nas linhas de dedução do `comparar.py`, que continua idêntico.

## Antes → depois (cada mudança com artigo)
| # | Mudança | Antes (v4) | Depois (v5) | Fonte |
|---|---|---|---|---|
| 1 | Teto do abono familiar | isento por inteiro | isento até 5.000 × filhos/mês − abono da CNPS; excesso tributável | CGI art. 45-4°, p. 29; LF 2026 art. 8, p. 15 |
| 2 | Não residente na TFE/TAFP | não calcula | calcula | arts. 187 (p. 60) e 173 (p. 59) |
| 3 | Série 6286x | só 62867 tributável | 6286% inteira no IRPP, TFE/TAFP e CNPS; 62866 no teto do abono; 62867 tributável (decisão técnica da frente, fonte: nome do código na WTC V3.0 × art. 45-11°; pendente de ok do usuário) | arts. 44-I, 45 (p. 29–30); Dec. 1635 art. 3 |
| 4 | Bolsa 6580x | tributável | fora do IRPP; dentro da TFE/TAFP e da CNPS | art. 45-9° (p. 30); arts. 189-1°, 173; Dec. 1635 art. 3 |
| 5 | Arredondamento da TFE | FLOOR(x+0,5) | nenhum | art. 190 (p. 61) × art. 177 |
| 6 | Isenção TF/TA de jovem diplomado < 35, deficiente, operário < 35 (empresa do regime real) | não tinha | flag 58219 tira o empregado das bases TFE/TAFP | arts. 188-10° (p. 61) e 174-3° (p. 59) |
| 7 | PSA | não tinha | 400 FCFA/mês, desconto do empregado | arts. 837–839 (p. 166) |
| 8 | Isenção de 15% das allocations spéciales | não tinha | MIN(verbas; 15% × 58105) sai do IRPP | art. 45-2° (p. 29) |
| 9 | Aposentadoria complementar | 216%% até 3,5% | igual, mas 2164x (voluntária) não deduz | art. 47-II (p. 30) |
| 10 | "30% despesas profissionais" | não existia no v4 (conferido) | continua sem | art. 47 (p. 30) |
| 11 | CNPS: taxas, teto, piso | sem fonte (valores do v4) | mesmos valores, agora com fonte: 3,5 EE + 5 ER (PVID), 7,5 (PFM), 4 (AT/MP); teto 500.000/mês nas 3 caixas (anual 6.000.000); piso 60.000 só em mês com salário | Dec. 1636 arts. 1, 3; Dec. 1635 arts. 1–2, 4; guia p. 7, 9, 12 |
| 12 | CNPS: base | matriz do v4 | espécie dentro; 6286x, 6274x, 6580x dentro; abono 6275x/6276x/6278x, meal cash 6566x, indenização, passagem, diária, mudança, 6287x fora; **transporte inteiro fora** (decisão técnica da frente, fonte: guia da CNPS p. 8; pendente de ok do usuário) | Dec. 1635 art. 3; Dec. 1636 art. 2; guia p. 7–8 |
| 13 | Não residente: CNPS | por ramo, cenário com ramos desligados | todos os ramos (flags padrão 1; 2 só para destacado com convenção) | guia p. 6 |
| 14 | Não residente: IRPP | 18% sobre 58592 | **tabela progressiva** com as isenções do art. 45 | arts. 44-II-2° (p. 29), 847 (p. 168); art. 116 (p. 43) só 2-VI e 60 |
| 15 | Passagem de férias 6255x | fora de tudo | IRPP: isenta até 1 bilhete/ano/pessoa (campo 58223); TFE/TAFP: dentro; CNPS: fora | art. 45-15° (p. 30); arts. 189-1°, 173; guia p. 8 |
| 16 | Diária 62570, 6557x, 6558x | fora de tudo | IRPP: dentro do teto de 15% (com 6287x); TFE/TAFP: dentro; CNPS: fora. Reembolso com comprovante (6256x) continua fora | art. 45-2°, 44-I; arts. 189-1°, 173; guia p. 7–8 |
| 17 | Arredondamento do IRPP | FLOOR(x+0,5) | igual, marcado "convenção técnica, sem regra no CGI" | CGI 2026 sem regra; art. 847 (barème da DGI não obtido) |
| 18 | Contas da CNPS | EE 2551 / ER 2550 | iguais (inversão do Dev não copiada) | WTC V3.0 |
| 19 | Limites das faixas do IRPP (rodada 3) | 800.000,99 / 6.000.000,99… | 800.000 / 6.000.000 / 7.500.000 / 9.000.000 / 12.000.000; cenários 7, 8, 12 exatos | art. 1-IV (p. 14) |
| 20 | TFE (rodada 3) | sem arredondamento (E3 = 25.537,5) | paga ao franco, convenção técnica (E3 = 25.538) | art. 190 (sem regra) |
| 21 | Art. 3-4° no IRPP (rodada 3) | só "jovem graduado ≤ 60 meses" | empresa do regime real + ≤ 60 meses + (jovem graduado < 35 na contratação **ou operário**) | art. 3-4° (p. 15) |
| 22 | Base da TAFP (rodada 3) | igual à da TFE | sem bônus único/discricionário 6222x e sem pensões 6264x (pensões entram só na TF) | art. 173 (« gratifications servies régulièrement »); arts. 187, 189-1° |
| 23 | 6251x (rodada 3) | fora da CNPS, fora da isenção de 30% | fora da CNPS e dentro da isenção de 30% junto com 6252x | art. 45-13°; guia p. 8 |
| 24 | Contas (rodada 3) | 58141, 58142, 58171, 58152 | 58100, 58101, 58103, 58112 (WTC V3.0); lista completa das novas em ASSUMPTIONS A14 | WTC V3.0 |
| 25 | Taxa 58131 (rodada 3) | gravada sempre | só com salário segurado (58550 > 0) | QA m3 |

Detalhe em inglês: `chad-design-blueprint-claude-v5/CHANGELOG.md` (rodada 1, R2-1 a R2-8 e R3-1 a R3-11).

## Decisões técnicas da frente (pendentes de ok do usuário) e o que continua aberto
Tomadas pelo mandato do usuário de 01/11 ("pesquisar e decidir": fechar cada ponto ambíguo com a nossa posição e a fonte). **São decisões da frente, não do usuário** (corrigido na rodada 4, achado N3 do QA).
- **Transporte na CNPS: fora por inteiro** — decisão técnica da frente (fonte: guia da CNPS p. 8), pendente de ok do usuário; 75%. Registrado que os decretos (Dec. 1635 art. 3, Dec. 1636 art. 2) não citam o transporte; só excluem reembolso de despesa e indenização de caráter reparatório. Só substitui `correcoes.md` 2026-07-07 depois do seu ok explícito. ASSUMPTIONS D1.
- **62867 auxílio-óbito: tributável** — decisão técnica da frente (fonte: nome "Death allowance" na WTC V3.0, lido como abono do empregador e não como o « capital décès » do art. 45-11°), pendente de ok do usuário; 65%. A alternativa (capital décès, isento de IRPP pelo art. 45-11°, mas dentro da TFE/TAFP e da CNPS) está descrita em ASSUMPTIONS D2 e RESEARCH_GAPS R28.
- **SKILL.md sem nenhuma marca ⚠️** (era 5).
- Continua aberto, fora do artefato: o método de retenção do pagamento irregular (A26, depende do barème da DGI, R23); regularização anual da CNPS (A23); lacunas de fonte R22–R26, R29, R30.

## Conferência
- `python -I _build_v5.py` (gera o SKILL.md e executa os mesmos dados; saída em `VALIDATION-run.txt`): **12 de 12 cenários exatos e 20 de 20 testes extras exatos**, sem tolerância (o status EDGE foi retirado). Esperados calculados à mão pela lei, não pelo motor. Cenários 3, 5 e E8 marcados como dependentes do método de retenção (A26): no cenário 5, pelo método cumulativo, a retenção do mês da indenização seria ≈ 117.898, e não 208.600.
- v5 × Dev (`simulacao/rodar_comparar_v5.py`; `comparar.py` e `sim_dev.py` com md5 `0e3709fe…` e `12d1108d…`, iguais aos originais): IRPP igual ao Dev em 5 de 12 (1, 2, 3, 9, 10). Nos cenários 8 e 12 a diferença é de 1 XAF e vem das faixas `x.99` do Dev; nos 4, 5 e 6 são pontos em que o CGI apoia o v5; o 7 vem da decisão do transporte na CNPS; o 11 vem da decisão sobre o não residente. Linha a linha: 2 de 10 exatos.
- SKILL.md: 35 regulações, **0 marcas ⚠️**.
- Achados do QA rodada 2 (N1–N4): corrigidos na rodada 4 (CHANGELOG R4-1 a R4-4).
- Achados do QA: os 2 blocker e os 7 major corrigidos; os minor m1–m13 tratados (corrigidos ou registrados em ASSUMPTIONS/RESEARCH_GAPS). Ver CHANGELOG R3-1 a R3-11.
- Não feito: `preflight_check.py` (não está nesta máquina); motor real (contas-teto, `retro_`, `_$$`, `_$$_monthly`, limites de faixa iguais, regularização anual da CNPS, método cumulativo).

## Fora do pedido (para o hub e `correcoes.md`, com o seu ok)
- `correcoes.md` 2026-07-07 está errado em dois pontos: "art. 45-4° sem teto" (o v5 aplica o teto) e, a confirmar, "excesso de transporte sujeito a CNPS" (R2, R20).
- WTC V3.0 × decisões: 6218x Tax No, 65630 Tax No, 6275x/6276x Tax Yes integral (R18); 6580x/6274x CNPS No, 6580x TF/TA No, passagem/diária Tax/TF/TA No (R19).
- Report Spec DGI-001: linha do não residente pensada para 18% (R21).
- Art. 3-4° (IRPP do jovem graduado/operário: < 35 anos e empresa do regime real) e indenização na TFE (art. 189-1°) não estavam nas listas de mudança: anotados (A19, A20).

## Bloco de prova
- **Pedido → resposta:** rodada 1 — pasta v5 + `_build_v5.py` com as 10 mudanças; estrutura do Dev no limite do abono e na TFE sem arredondamento; pendências marcadas; 12 cenários; VALIDATION; esta conferência. Rodada 2 — CNPS (taxas, teto, piso, base, não residente), não residente pela tabela, passagem/diária, 6274x/6580x e arredondamento aplicados (linhas 11–17 acima); cenários rodados de novo; VALIDATION e CONFERENCIA atualizados.
- **Fontes:** cada mudança cita artigo e página do CGI 2026 ou o decreto/página do guia da CNPS; relidos por mim nos `.txt` (CGI: arts. 45, 46, 47, 116, 173–190, 837–839; guia: p. 7, 8, 12). Os decretos 1635/1636 e as linhas do CGI sobre o não residente (arts. 2-VI, 44-II-2°, 49, 60, 847) foram tomados da seção (b) da LEI-VEREDITOS, que traz a linha de cada um.
- **Teste:** execução do design (12/12 e 20/20 exatos, sem tolerância; E18–E20 cobrem a falta de data e o operário de 40 anos); esperados à mão; md5 das cópias do `comparar.py`/`sim_dev.py`; pasta v4 e simulação de 30/10 sem alteração (datas de 29–30/10).
- **Confiança** (igual à da LEI-VEREDITOS): 95–100% nas mudanças do CGI 1–10 e 19–23 e nas taxas/teto da CNPS (11); **85%** no não residente (13–14); **75%** na passagem/diária (15–16) e na base da CNPS (12); 85% no piso (só o guia de 2019, R22); transporte fora da CNPS 75% (guia, decretos não citam). **Não pronto para o Dev** enquanto o motor real não confirmar contas-teto, `retro_`, `_$$`, limites de faixa iguais e a regularização anual, e enquanto o método de retenção do pagamento irregular (A26) não tiver o barème da DGI.

## Quem mexeu
| Data | Frente | O quê |
|---|---|---|
| 2026-10-29 | chade | v4 criada a partir do v3 + reunião 16/10 + 7 Report Specs (pasta `../2026-10-29-design-v4/`) |
| 2026-11-01 | frente Chade | v5 criado |
| 2026-11-01 | frente Chade | v5 rodada 2: decisões da LEI-VEREDITOS (b) aplicadas (CNPS, não residente, passagem/diária, 6274x/6580x, arredondamento); cenários e VALIDATION refeitos |
| 2026-11-01 | frente Chade | rodada 3 pós-QA |
| 2026-11-01 | frente Chade | rodada 4 pós-QA r2 |

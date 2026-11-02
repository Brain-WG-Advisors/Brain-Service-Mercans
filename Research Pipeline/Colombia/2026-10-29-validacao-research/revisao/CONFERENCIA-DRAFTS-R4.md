# Conferência dos DRAFTs: rodada 4 (COVAL, 2026-10-30)

Ligado a [[mudancas-RODADA4]], [[TABELA-CONSOLIDADA]], [[DECISOES-TEST4]], [[PENDENTES-CCG-WTC]], [[PENDENTES-SPECS-DD]], [[RODADA4-ORACULO-V2]], [[CONFERENCIA]].

## O que foi feito
- **Base:** os DRAFTs da rodada 3. O md5 de cada um conferiu com o `MD5-DRAFTS.txt` anterior antes de editar. As cópias de antes ficam em scratchpad `r4/pre_r4/` e `r4/CCG_pre_r4.docx`.
- **Arquivos alterados:** só os DRAFTs de `revisao/`. Os finais, o Drive (G:) e `~/mercans-pipeline` não foram tocados.
- **xlsx:** cirurgia no XML. As partes do zip que não mudaram são cópia byte a byte, e toda célula alterada leva fundo `FFDDEBF7`.
- **CCG:** `w:ins`/`w:del` com autor "Mercans Compliance (COVAL)" e data 2026-10-30. A data é diferente da das rodadas 1-3, para separar as rodadas.
- **SIR:** redline em markdown, na seção "Rodada 4".
- **Version Control:** uma frase "Round 4 (30-Oct-2026): …" acrescentada à linha da versão DRAFT de cada artefato. A versão continua a mesma.
- **Registro:** linha a linha, em `mudancas-RODADA4.md` (236 linhas: antes e depois verbatim). Os `CHANGELOG.md` de cada pasta ganharam a seção "Rodada 4".

## Status dos 54 itens
| Grupo | Itens | Status |
|---|---|---|
| Test 4 (5 muda) | T4-1, T4-2, T4-3, T4-4, T4-5 | APLICADOS. T4-4 já estava certo na PILA-003 (C19, M111). T4-5 já estava certo no CCG P546, no WTC V1 e na PILA C19; entrou a citação do CE 25907/2022 em P546 |
| CCG/WTC (20 muda) | A-08, A-11, F-09, D11, D15, D3, D5, D6, D9, A-14, F-10, F-14, F-11, A-10, A-12, SIM-06, SIM-10, F-12 | APLICADOS |
| CCG (já feitos na rodada 1) | A-03 (T71R4 = 6.960%, P534 apagado), F-01 (T201R1 = 3 anos) | Conferidos no DRAFT, sem nova edição |
| Specs/DD/Payslip/SIR (21 muda) | P-06, P-17, DD-10, DD-15, DD-16, DD-21, DD-24, NE-03, NE-04, NE-10, NE-18, F-06, SIM-07 (valor já aplicado; nota nova), F-11 (006), F-10 (006), PS-06, PS-11, PS-13, S-03, S-04, S-05 | APLICADOS |
| Não muda (5) | D13 (nota D207:D213), P-01 (nota P108), NE-15 (nota M78), DD-23 (I45: casillas 79-81), A-07 | Notas APLICADAS. A-07: a decisão não traz texto de nota (tabela completa), então não há o que aplicar |
| Abertos (3) | F-13 (CCG T150R3), S-07 (SIR), A-14 (CCG T65R5/T69) | Posição provisória aplicada com a marcação |
| Anteriores | DD-08 (DD K51/K94), NE-05 (rodada 2) | Já no DRAFT |

**Abaixo de 80%.** Todos levam "Position - confidence X%, confirm with …" na célula ou no parágrafo:
- D5 75% (WTC D123);
- D9 70% (D156, D324);
- D15 70% (D134);
- P-06 75% (P/C17);
- DD-21 75% (H7);
- NE-18 65% (D68, D69);
- SIM-07 75% (C26, C28);
- A-10 75% (CCG P420);
- F-13 70% (CCG T150R3).

**Mudanças por consequência, para não deixar contradição dentro do artefato.** Todas estão registradas no `mudancas-RODADA4.md`:
- A-08:
  - no CCG: P659, P761, T83R1, T123R3-R5, T202R11, P625;
  - no WTC: F392, F406 e Tax Credit A51, A53, A55:A57.
- T4-1:
  - no CCG: P545 STEP 4, T183R6 e P564;
  - na PILA-003: M36, M109, C7 e C34.
- T4-2: CCG P545 1.3 e T67R1; WTC F303, F390 e F395; PILA C20.
- NE-03: Example Analysis D28.
- P-06: as linhas de tarifa de 7 posições (114, 123, 137, 139, 141, 143, 145; colunas J, K, P), o Example Analysis, o registro do Sample File e A17/A117/A118.
- F-10 (006): Field Options D48.
- DD-21: Mappers G95.
- Payslip: a aba ES espelha a EN (PS-06, PS-11).

## Conferência mecânica (minha)
- **xlsx:** fiz o diff célula a célula antes × depois em todas as abas, comparando valor e preenchimento. As células alteradas são exatamente as do registro, sem nenhuma inesperada, e todas estão azuis. Contagem por arquivo:
  - WTC 44;
  - DD 52;
  - NE 11;
  - PILA-003 43;
  - PILA-007 2;
  - 002: 5;
  - 004: 2;
  - 005: 2;
  - 006: 4;
  - Payslip 7.
- **`validate_workbook.py`:** PASS em todos, menos o Payslip, que dá FAIL por um marcador "placeholder" que já existia antes da rodada 4. Nas specs, com `--artifact`, os FAIL de contrato (cabeçalho "RA Comments", colunas) são os mesmos de antes.
- **CCG:**
  - Ao rejeitar só as mudanças de 2026-10-30, o documento fica idêntico ao de antes da rodada.
  - O `docx/validate.py --author` dá "All validations PASSED" (7.976 → 7.976 parágrafos).
  - O arquivo abre no python-docx.
- **Contas:**
  - SIM-06: 249.095 × 21 ÷ 30 = 174.366,50. Total bruto 2.487.820,50. Líquido 2.305.220,50.
  - A-08: 4.368.000 ÷ 52.374 = 83,4002 UVT, faixa 0%, retenção 0.
  - Registro PILA-003: 693 posições preservadas, com as tarifas em 238-244, 308-314, 408-414, 424-430, 440-446, 456-462 e 472-478.

## Revisor independente (subagente, não editou nada)
- **Veredito:** o diff bate 1:1 com o registro; a rejeição só da rodada 4 no CCG volta ao estado anterior; as contas e as posições conferem; as fontes primárias amostradas (DIAN 11383/2024 IV.2, DUR 1.2.4.1.6 par. 3, Ley 2381 art. 20, Dec. 1083 art. 2.2.5.5.7, Ley 776 art. 3, Dec. 4982 art. 1, Oficio 16418/2019, DIAN 14745/2025) também conferem. Confiança de 90%.
- **Resíduos apontados e corrigidos nesta rodada:**
  - A-08 CCG P625 (bloqueava);
  - A-08 CCG T123R3;
  - A-08 WTC Tax Credit A51, A53 e A57;
  - WTC F406 (o "BOTH" que sobrou);
  - T4-2 WTC F395;
  - F-10 006 D48 (Decreto 1470);
  - P-06 PILA-003 A17, A117, A118 e P143/P145 ("Not an amount - no rounding.");
  - D15 D134 (o "confirm with …");
  - T4-3 F277:F280 (ponto entre as frases);
  - DD-21 G95 (98 e ZZZ);
  - T4-1 CCG P564.
- **Não corrigido, por ser só de layout:** no Form. 350, a linha 997 ocupou a linha em branco antes do tracejado (Sample File A92).
- **Depois das correções:** reconferi o diff (nenhuma célula inesperada, todas azuis), a rejeição da rodada 4 no CCG (idêntica) e o `docx/validate.py` (PASS).

## Oráculo v2 e suítes
Está em `oracle/RODADA4-ORACULO-V2.md`.
- **cases.json:** só C25 e C26 mudam (a CCF sem o excesso).
- **cases_research.json:**
  - RC03: base 4.368.000, retenção 0;
  - RC05: CCF 320.000.
- **Test 4:** a lacuna do oráculo foi de 7 para 0, e as divergências foram de 739 para 742.
  - Os 8 empregados do 114-1 seguem como erro do provedor: nenhum tem IBC de saúde de 10 SMMLV ou mais.
  - Achado novo: o E251, travado pelo campo 76, vai para revisão manual.

## O que falta (fora do pedido)
- A Circular MinTrabajo 101/2025 (revogada) segue citada em cerca de 20 lugares do CCG. Só P424 e P420 foram tratados (F-11 e A-10).
- O texto da Res. MinTrabajo 2708/2026 não foi lido.
- O SIR existe só como Google Doc: o redline tem de ser colado à mão.
- Nada foi ao Drive, a ticket ou a e-mail.

## Bloco de prova
- **Pedido → resposta:**
  - os 46 itens "muda", as 5 notas e os 3 abertos (tabela acima);
  - o oráculo v2 e as suítes;
  - a conferência independente com os resíduos corrigidos;
  - o MD5, o registro e esta conferência.
- **Fontes:** os textos e as fontes vêm das decisões de 30/10 (TABELA-CONSOLIDADA e lotes). Nas leituras primárias amostradas, o revisor não achou divergência.
- **Teste:** diff XML/célula, rejeição seletiva do docx, `validate.py` do docx, `validate_workbook.py`, contas refeitas, posições do registro PILA.
- **Confiança:** 92% na aplicação. A confiança jurídica de cada item é a da TABELA.

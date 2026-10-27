# CI — teto CNPS PF / AM / AT-MP: 70 000 → 75 000 XOF/mês (2026-10-16)

**Fonte:** communiqué CNPS de 11/01/2023 (`brain-service/raw/docs/oficiais/CI/2026-10-15-CNPS-communique-nouveau-plafond-2023.pdf`): a partir de 2023-01-01, teto mensal de AM / PF / AT-MP = 75 000; aposentadoria = 3 375 000; piso = 75 000. Base legal: Loi 99-477 art. 23. Derivados: 900 000/ano; 225 000/trimestre; PF 5% = 3 750; AM 0,75% = 562,50 → **563** nos exemplos (CCG §1.5, arredondamento ao franco); AT-MP 3% = 2 250.

**Decisões do usuário (16/10):** base do CCG = v1.1 (1); CCG v1.3, DISA v1.5, WTC v1.3, CNPS-001 v1.4, Design v1.2; AM = 563; "3 231/day" → "225 000/quarter"; WTC: corrigir também a aba ativa "Wage Type Catalogue V1".

## Arquivos
| Arquivo novo | Base (export do Drive em 16/10, 09:14–09:15) | Alterações |
|---|---|---|
| `CI-WTC-001-v1.3.xlsx` | `CI-WTC-001-v1.1 (1).xlsx` (VC até 1.2) | 22 células: 17 do teto + 5 da linha 1.3 no VC |
| `CI-CNPS-001-MonthlySocialContributions-Spec_v1.4.xlsx` | `…-Spec (1).xlsx` (VC até v1.3) | 43 células: 41 do teto/exemplos + 2 no VC |
| `CI-CNPS-002-DISAAnnualSalaries-Spec_v1.5.xlsx` | `…-Spec (1).xlsx` (VC até v1.3) | 10 células: 8 do teto/exemplos + 2 no VC (v1.4 não usada: rascunho local de 18/08 nunca publicado) |
| `CI-CCG-001-v1.3.docx` | `CI-CCG-001-v1.1 (1).docx` | 102 trechos (1 capa, 56 menções ao teto, 21 valores de PF/AM/AT, 24 totais refeitos) |
| `CI_Regulation_Design_v1_2.md` | `CI_Regulation_Design_v1_1.md` | 6 linhas (1, 89, 128, 220 ×2, 301, 423) + nota de changelog v1.2 |

Destaque: células xlsx com fill `FFDDEBF7`; trechos do docx com sombreamento `DDEBF7` (102 runs). O `.md` não tem cor: a lista está em `conferencia/logdesign.txt`.

## Antes → depois
A lista completa, célula a célula, está em `conferencia/` (`logwtc.txt`, `log001.txt`, `log002.txt`, `logccg.txt`, `logdesign.txt`). Em resumo:
- **WTC**: Q1/R1/S1 nas abas "Wage Type Catalogue V1" (ativa) e "Wage Type Catalogue" (oculta): "cap 70 000" → "cap 75 000". D/F332–334: "capped 70 000" → "75 000". F345/348/351: "840 000 XOF/year (12 x 70 000" → "900 000 … (12 x 75 000". Global WTC Coverage C8 (4×). Form Reference Guide E9.
- **CNPS-001** (abas Monthly e Quarterly): bases K15/18/21 8 400 000 → 9 000 000; PF K16 420 000 → 450 000; AM K19 63 000 → 67 500; AT K22 252 000 → 270 000; total do empregador K24 7 280 000 → 7 332 500; total K26 12 635 000 → 12 687 500; M15/18/21. Também: Report Matrix J3, Field Options A18/D18, File Structure B12, Population Rules C9/D9, Example Analysis (7), Sample File (4), Form Alignment A16.
- **CNPS-002**: M21, E35 840,000 → 900,000, F35; Sample File A12 840000 → 900000, A15 420000 → 450000 (6 meses), A18 630000 → 675000 (9 meses); Form Alignment C8, B27.
- **CCG**: total de encargos do empregador 111 625 → 112 063 (custo 1 111 625 → 1 112 063; expatriado 1 203 625 → 1 204 063); 69 625 → 70 063 (669 625 → 670 063; expatriado 724 825 → 725 263; aparece 2×); 14 500 → 14 938 (89 500 → 89 938); 101 125 → 101 563 (1 001 125 → 1 001 563); 48 625 → 49 063 (448 625 → 449 063); 449 875 → 450 313 (2 699 875 → 2 700 313).

## Conferência
1. Cada edição xlsx declara o valor antigo esperado: o script aborta se o valor não bater, se a célula tiver fórmula ou se o trecho não aparecer exatamente N vezes.
2. Comparação de todas as células de todas as abas, base × nova: as únicas diferenças são as da lista (WTC 22, 001 43, 002 10). Formatação igual à da base, salvo o fill. Nenhuma célula fora da lista mudou.
3. Varredura de resíduo (70 000 / 840 000 / 210 000 / 8 400 000 / 3 231) fora das edições: zero nos três xlsx e no docx.
4. As partes do zip não editadas (desenhos, comentários, mídia) foram copiadas byte a byte, e a lista de partes é idêntica.
5. `validate_workbook.py`: mesmos achados da base nos três xlsx (os desvios estruturais do padrão de 9 abas já existiam). `diff_wtc_baseline.py`: BASELINE INTACT.
6. CCG: dry-run e gravação com o mesmo resultado (102); estrutura idêntica à da base (1 097 parágrafos, 107 tabelas, 228 títulos); C29 limpo; XML válido.
7. Contas refeitas: 120 × 75 000 = 9 000 000; × 5% / 0,75% / 3% = 450 000 / 67 500 / 270 000; 6 545 000 + 450 000 + 67 500 + 270 000 = 7 332 500; + 5 355 000 = 12 687 500. DISA: 6 × 75 000 = 450 000; 9 × 75 000 = 675 000. CCG: soma de cada tabela de encargos refeita (ex.: 77 000 + 3 750 + 563 + 2 250 + 500 + 12 000 + 4 000 + 12 000 = 112 063).

## Não alterado (de propósito)
Teto da aposentadoria 3 375 000 / 40 500 000; piso 75 000; "525 000" da tabela de indenização do CCG; DD (sem referências).

## Fora do escopo (com a janela geral)
- Exemplo DASC da DISA (Sample File A35–A37): base de PF/AM/AT de 240 000 000 para 45 empregados (máximo possível 40 500 000).
- `ci.json` (Drive 07 - Design), regulation ordinal 61: piso e teto = 840 000 (produção/dev; CT-A-620).
- `CI-CNPS-002…_v1.4.xlsx` local (18/08): bloco do esquema DASC no Form Alignment que não está no Drive.

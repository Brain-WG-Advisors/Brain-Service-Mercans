# CO-WTC-001 v1.5 — conferência (21/10/2026)

**O que é:** a Fase 2C do plano Colômbia (`co-report-crosscheck/HANDOFF-2026-10-21.md` §8), na parte do WTC. **Ainda não está no Drive**: só sobe com o ok do usuário (Fase 4).

## Base
- `base/CO-WTC-001-v1-gsheet-export-2026-10-21.xlsx`: export do Google Sheet `CO-WTC-001-v1` do Drive, feito em 21/10 com o ok do usuário. md5 40d176082821752ee9f15afb0e0c8afc.
- O Sheet tinha edições de 20/10 que não estão no xlsx v1.4 de 13/10 e não ganharam linha no Version Control. Exemplo: as linhas 6 e 37 trocaram os atributos de salário de "NA" para "Salary / Yes / No". **O autor não foi identificado.** A v1.5 parte do Sheet, então mantém essas edições.

## Antes → depois (só colunas nossas: Y, Z e as abas de apoio)
| Onde | Antes | Depois | Células |
|---|---|---|---|
| Wage Type Catalogue Y1 (cabeçalho) | Res. DIAN 000013 de 2021, Anexo Tecnico v1.0 | Res. DIAN 000227 de 2025, Anexo Tecnico v1.0 | 1 |
| Wage Type Catalogue coluna Z | Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0 | Resolucion DIAN 000227 de 2025 arts. 1.5.3.1.1 to 1.5.3.9.8, Anexo Tecnico v1.0 | 109 |
| Employer Sick Pay A59, Global WTC Coverage C31 | idem | idem | 2 |
| Version Control linha 17 | — | 1.5, 21-Oct-26, Draft, Wallisson Gomes | 5 |

Fonte do mapa: Res. 000227/2025, cap. 3 "Nómina electrónica", arts. 1.5.3.1.1 a 1.5.3.9.8, que compilam a Res. 13/2021. Conferido no normograma DIAN e no texto da Res. 227 (`co-report-crosscheck/04-output/SIR-RES227-2026-10-21.md`).

## Conferência
- Edição direto no XML (sharedStrings e a planilha do Version Control). Mudaram só essas 2 partes do zip.
- Diff célula a célula contra a base: só as 112 células de citação e as 5 do Version Control. Nenhuma mudança de estilo. Imagens iguais.
- Res. 13/2021 restante: 0 (fora o texto do Version Control D17, que descreve a mudança).
- Toolkit `validate_workbook --artifact WTC`: o mesmo FAIL da base, C12, porque o catálogo tem 28 colunas e o modelo tem 20. Não é novo.
- Toolkit `diff_wtc_baseline`: "BASELINE VIOLATED", porque a coluna A "Mercans Code" está vazia nas 405 linhas, e já estava assim na base e no v1.4. É coluna laranja, do desenvolvimento.

## Não feito, com o motivo
- **Saúde dos pensionados** (4% para 1 SMLMV, 10% acima de 1 até 3, 12% acima de 3; Ley 100 art. 204 par. 5, com a faixa de 2 a 3 SMLMV reduzida a 10% a partir de 2024 pela Ley 2294/2023 art. 78): o WTC não tem linha de saúde do pensionado. Criar uma é decisão de desenho do catálogo, e a coluna F (Formula) é do desenvolvimento (fronteiras.md). A regra vai no CCG v1.3. → decisão do usuário.
- **Denominador dos 40%** (V1 e F395 dizem que os pagamentos "não remuneratórios" ficam fora do total da remuneração): a sentença SU 25185/2021 não diz isso, e a orientação da UGPP de 2021 os inclui. Não há fonte primária para nenhum dos dois lados. Fica em aberto (PENDING item 35); nada foi mudado.

md5 da v1.5: 383e37317708a99b0a2f6806b013c19f

## Frentes
| Data | Frente | O quê |
|---|---|---|
| 2026-10-21 | geral (Colômbia) | v1.5 criada e conferida; não subiu ao Drive |

Verificador independente (`WTC-verification.json`): PASS, sem ajuste obrigatório. A data do Version Control foi corrigida para 21-Oct-26 (dia real) e a frase sobre a base saiu do D17.
| 2026-10-21 | geral (Colômbia) | Copiado para o Drive com o ok do usuário; md5 da cópia idêntico |

| 2026-10-22 | geral (Colômbia) | Importado no Google Sheet CO-WTC-001-v1 (Replace spreadsheet); conferido ao vivo: VC 1.5, Res. 227 x110 no catálogo, Res. 13 x0 |

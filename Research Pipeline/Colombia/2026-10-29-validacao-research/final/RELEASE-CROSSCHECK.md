# Release cross-check, finais da Colômbia (emissão 2026-10-30)

Ligado a [[CONFERENCIA]] e [[BASELINE]]. Gerado por `final/scripts/release_crosscheck.py` em 2026-10-30 16:50. Compara cada final com o DRAFT aprovado (`revisao/`, md5 em `revisao/MD5-DRAFTS.txt`).

## O que a ferramenta prova

1. **Conteúdo:** a única diferença de texto entre DRAFT e final são as edições declaradas em `final/scripts/release_edits.py` (xlsx: valor e fórmula de todas as células de todas as abas; docx: todos os parágrafos do DRAFT com as alterações controladas aceitas). Cada edição declarada produziu exatamente o texto declarado.
2. **Formatação:** toda célula mantém a formatação do DRAFT, exceto o fundo de destaque `FFDDEBF7`, que nenhuma célula mantém. A estrutura das abas fora das células (colunas, mesclagens, alturas, painéis) e todas as outras partes do zip são idênticas byte a byte.
3. **Marcadores:** lint C29 (placeholder, TODO, TBD, FIXME, XXX, VERIFY No., to be confirmed / verified) e marcadores internos (COVAL, DRAFT, confiança, "Position -", rodada, IDs de achado, ferramentas internas, pipeline, outros países, frases de retrabalho). Ocorrências legítimas aparecem contadas, não escondidas.
4. **Metadados e estrutura:** sem alterações controladas, comentários no docx, rsids, controle de alterações ligado, propriedades personalizadas; criação = modificação = data de emissão, revisão 1, autor.

## Resultado

| Artefato | Final | Versão | Edições declaradas conferidas | Outras medidas | Falhas | md5 final | md5 DRAFT |
|---|---|---|---|---|---|---|---|
| CCG | `CO-CCG-001-v1.5.docx` | 1.5 | 55 | paragraphs 7975 | 0 | `3b605ff32f5a` | `2f4197760d08` |
| WTC | `CO-WTC-001-v1.7.xlsx` | 1.7 | 129 | highlight removed 184 | 0 | `d83d0e3c75b9` | `c71f0d35a041` |
| DD | `CO-DD-001-v1.4.xlsx` | 1.4 | 20 | highlight removed 919 | 0 | `6557f7615a6b` | `c777c91fdec4` |
| NE | `specs/CO-DIAN-001-NominaElectronica-Spec.xlsx` | 1.1 | 30 | highlight removed 84 | 0 | `3cf3dc717406` | `a40b77199c1b` |
| F350 | `specs/CO-DIAN-002-Formulario350-Spec.xlsx` | 1.1 | 9 | highlight removed 22 | 0 | `97e1fae0ae35` | `ff7df48f3979` |
| F220 | `specs/CO-DIAN-004-Formulario220-Spec.xlsx` | 1.1 | 8 | highlight removed 29 | 0 | `1321e85f1e95` | `5c9e25724be3` |
| F2276 | `specs/CO-DIAN-005-Formato2276-Spec.xlsx` | 1.1 | 9 | highlight removed 61 | 0 | `8ff54cc914c8` | `1db47d680588` |
| CES006 | `specs/CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx` | 1.1 | 6 | highlight removed 13 | 0 | `8170ff99cce9` | `f9cebc8cb778` |
| PILA003 | `specs/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx` | 1.1 | 16 | highlight removed 102 | 0 | `482c793f1bba` | `944441f20a31` |
| PILA007 | `specs/CO-PILA-007-AportesPensionados-Spec.xlsx` | 1.1 | 7 | highlight removed 8 | 0 | `eae9a7955d23` | `a6868d1d2d2b` |
| PAYSLIP | `CO_Compliance_Payslip_Generator.xlsx` | 1.2 | 36 | custom properties removed 1; highlight removed 153; declared formula edits verified 2 | 0 | `7be64fec306c` | `9bfe7e91c096` |
| SIR | `CO-SIR-001-v1.2-texto-final.md` | 1.2 | - | blocks to paste 15 | 0 | `e8669140302e` | `cf1cdc95e07c` |

**Veredito: PASS** (0 falhas).

## Ocorrências legítimas (não são marcador)

- CCG: 1 × Version Control history of earlier issued versions (unchanged)
- CCG: 15 × country / language named in the legal content (treaty lists, language rule, nationality example)
- CCG: 3 × deduction labels (D1)-(D3) of the CCG worked example
- WTC: 1 × country / language named in the legal content (treaty lists, language rule, nationality example)
- DD: 8 × ISO country list
- NE: 2 × country / language named in the legal content (treaty lists, language rule, nationality example)
- F350: 5 × country / language named in the legal content (treaty lists, language rule, nationality example)

## Falhas

Nenhuma.

## Fora do escopo desta ferramenta

- Comentários do time herdados das versões vigentes no WTC (2 partes) e no DD (3 partes): são do Google Sheets, idênticos aos da v1.6 / v1.3, e foram mantidos (não são marcas da validação).
- O texto jurídico: é conferido pelo Test 0 (revisor independente), não por esta ferramenta.

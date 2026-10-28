# Lituânia — atualização 2026 (CCG, Alerta, WTC, DD) — conferência

Origem: call do Wallisson (27/10, `Downloads\Meeting with Gomes, Wallisson(Global-V) (2).txt`) e SteerCo Accenture LT & LU (27/10, `Downloads\Accenture LT & LU Internal SteerCo meeting.txt`). O Kevin testou e o sistema está em 2025; o ticket ao Development ainda não existe. Ordem decidida pelo usuário: (1) corrigir CCG/Alerta e analisar; (2) ajustar WTC/DD e conferir alinhamento dos artefatos; (3) só então o ticket.

Hub: [[Lituania]] · Correção anterior ligada: [[correcoes]] (linha de 2026-10-13, limiares 36/60 VDU).

## Originais (`originais/`, não alterados)
| Arquivo | Origem | Observação |
|---|---|---|
| Lithuania Payroll Regulation Guide_2026.docx | Drive `05 - Payroll Regulation Guide/2026 Regulation guide/` (alterado 16/12/2025) | md5 c43c8a2b67176942c9d12ff39a8d187a = cópia de 10/10 |
| Lithuania_Changes in Tax Rates & social security Rates - 1st January 2026.docx | export de 10/10 do `.gdoc` em `09 - Alerts/2026/` (alterado 16/12/2025) | o oficial é Google Doc: correção final é no navegador, com ok |
| Lithuania  WTC V3.0.xlsx / Lithuania Data Dictionary V3.0.xlsx | export de 10/10 (Drive sem alteração desde 09/09/2025 e 16/07/2025) | etapa 2 |

## Etapa 1 — correções (destacadas em azul-claro `DDEBF7` nos arquivos `_corrigido.docx`)
| # | Documento / trecho | Antes | Depois | Fonte primária |
|---|---|---|---|---|
| 1 | CCG + Alerta: tabela de faixas, 1ª faixa | Below 82 962 (Alerta: **0%**) | Below 83 237.40 — 20% | XV-632 art. 4 (VDU €2.312,15 × 36); GPMĮ art. 6(1)(1) |
| 2 | CCG + Alerta: 2ª faixa | 82 962 – 138 270 | 83 237.40 – 138 729 | XV-632 art. 4 (× 36 e × 60); GPMĮ art. 6(1)(2) |
| 3 | CCG + Alerta: 3ª faixa | 138 270 and above | 138 729 and above | XV-632 art. 4 (× 60); GPMĮ art. 6(1)(3) |
| 4 | CCG + Alerta: nota da opção 25%/32% | €82 962 | €83 237.40 | idem |
| 5 | CCG (3×) + Alerta (2×): teto anual da Sodra | €138 270 | €138 729 | Lei I-1336 art. 10(9) (60 VDU, exceto PSD) + XV-632 art. 4 |
| 6 | CCG: NPD (seção, passos e títulos dos exemplos 2 e 3) | fórmula de 2025: "below € 2 387.27" e "€ 400 minus 0.18 x (… minus € 642)" | fórmula única: até € 2 677.49 → 747 − 0,49 × (renda − MMA); acima → € 0 | GPMĮ art. 20(2) e 20(3) (versão 2026); 1 153 + 747/0,49 = 2 677,49 |
| 7 | CCG: Non-Taxable Pay | seguro-saúde dentro dos 25% sem limite próprio | seguro-saúde voluntário só até € 350/ano, dentro dos 25% | GPMĮ art. 17(1)(14) e (14¹), alterados pela XV-343 |
| 8 | CCG: acidentes de trabalho, Grupo II | 0.43% | 0.49% | XV-632 art. 3(3)(2) |

Extratos: `raw/docs/oficiais/LT/` (GPMĮ 2026 em PDF; XV-632 art. 4; `2026-10-27-I-1336-art10-9_e_XV-632-art3_extrato.md`).

| 10 | CCG: Social Security Calculation Process, "Note 1: Monthly earnings less than minimum wage" + exemplo 1 (erro anterior a 2026) | empregador contribui sobre o MMA; 3 exceções; exemplo 1 só com 1,77% × 1.153 | abaixo do MMA, o empregador paga, do próprio bolso, as contribuições do empregado e do empregador sobre a diferença; 5 exceções; exemplo 1: desemprego + acidentes 1,45% × 1.153 = 16,72; Fundo de Garantia 0,16% × 840 = 1,34; Fundo de Longo Prazo 0,16% × 1.153 = 1,84; + (1.153 − 840) × 12,52% = 39,19 → custo total 59,09; exemplo 2: nota de que o piso do Fundo de Longo Prazo nas exceções não está confirmado (se valer: 15,36) | Lei I-1336 art. 10(7); página de tarifas 2026 da Sodra (`raw/docs/oficiais/LT/2026-10-27-Sodra-SAM/2026-10-27-sodra-tarifas-2026-PSD-fundos_extrato.md`) |

### Conferido sem mudança (fonte lida)
- MMA €1.153 (Nutarimas 700, p. 1); NPD €747 / €1.127 / €1.057 (GPMĮ art. 20(2), (6)); 15% sobre benefício de doença (GPMĮ art. 6(6)(2)).
- Sodra 2026: empregado 12,52% = 8,72 + 1,99 + 1,81; desemprego 1,31% / 2,03%; acidentes grupos I 0,14%, III 0,7%, IV 1,4% (XV-632 art. 3(1), (3), (4)).
- Contas dos exemplos do CCG refeitas: NPD 331,97; contribuições 105,17 / 20,41 / 14,87 / 250,40 / 35,40 / 49,80 / 18,68 / 22,13 — todas batem.
- Limiar do Alerta "€2,677.49" (NPD zero) e €350 do seguro-saúde: corretos.

### Conferido depois (27/10, 2ª leitura)
- PSD 6,98% (Lei I-1343 art. 17(2)); Fundo de Garantia 0,16% sobre o salário real e Fundo de Longo Prazo 0,16% com piso no salário mínimo, pensão adicional 3% (página de tarifas 2026 da Sodra; as leis dos fundos não foram localizadas); presentes até €200/ano (GPMĮ art. 17(1)(39)); excesso do seguro-saúde voluntário entra na base da Sodra (Lei I-1336 art. 11(1)(17), XV-633).

### Bloco 1 (27/10, 3ª leitura)
- Residência: CCG confere com GPMĮ art. 4(1)(1)–(5); item 5 corrigido ("e" → "ou": salário pago **ou** custo de vida coberto pelo orçamento público).
- Pensão adicional: parágrafo do CCG reescrito pela página oficial da Sodra "Informacija apie pensijų kaupimo pokyčius nuo 2026 m. sausio 1 d." (janela 2026-01-01 a 2027-12-31 só para quem começou até 2025-12-31; devolve só as contribuições próprias com rendimento; contribuições seguem até a decisão; suspensão de no mínimo 12 meses; efeito na folha durante a suspensão a confirmar com a Sodra).
- Arredondamento: GPMĮ 2026 sem regra (busca por "apvalin" sem resultado) — coerente com "not stipulated"; outras leis não verificadas.

### Não conferido (não alterado)
- ~~Teto 2025 €126.532,80 citado no Alerta~~ → **retirado do Alerta em 27/10** (o Alerta trata de 2026; o valor de 2025 não foi lido em fonte primária: XV-46 no e-seimas pede CAPTCHA, e a página de tarifas da Sodra não traz o teto). Piso do Fundo de Longo Prazo nas 5 exceções (lei do fundo não localizada).

### Conferência mecânica
- Diff de texto original × corrigido: só os trechos da tabela acima mudaram (CCG 17 trocas; Alerta 7). Os dois arquivos abrem (python-docx). Demais partes do .docx copiadas byte a byte.

## Etapa 2 — WTC/DD e alinhamento
Arquivos: `Lithuania  WTC V3.1.xlsx` e `Lithuania Data Dictionary V3.1.xlsx` (edição direta no XML, sem openpyxl.save; células alteradas em `FFDDEBF7`; Version Control 3.1 como **Draft**, "Compliance Team").

| # | Arquivo / célula | Antes | Depois | Fonte |
|---|---|---|---|---|
| W1 | WTC F446 — 65630 Health Insurance Benefit | NA (totalmente tributável, sem regra) | só o excesso: isento até €350/ano, dentro do teto de 25% com seguro de vida e pensão | GPMĮ art. 17(1)(14)/(14¹) |
| W2 | WTC F474 — 65810 Life Insurance (Taxable) | "Taxable if less than 25%" (lógica invertida) | "Taxable portion above 25%…" (teto compartilhado) | idem |
| W3 | WTC F10 — 23610 Life Insurance | "Non taxable if less than 25%" | "Non taxable up to 25%…" (teto compartilhado com saúde €350 e pensão) | idem |
| W4 | WTC F499 — 65835 Prize/Gift (tributável) | "Non taxable up to 200 Euro per year" (descrevia o código isento 65805) | "Taxable portion above 200 Euro per year (up to 200: 65805)" | GPMĮ art. 17(1)(39) |
| D1 | DD Country Fields G12 — Elective Tax Rate | "Employees consent to be taxed at 32%" | pedido do empregado para aplicar 20/25/32% pelo total anual pago por este empregador; sem pedido, pelo valor de cada pagamento (na prática 20%) | GPMĮ art. 23(7) (XV-343) |
| C9 | CCG Notes 1 e 2, nota do cálculo e parágrafo "progressive Tax rate"; Alerta nota e parágrafo | "flat 20%" / "only when employee provides a request" / "taxable pay has exceeded €82 962" | sem pedido: alíquota pelo valor de cada pagamento (na prática 20%); com pedido: pelo total anual (25%/32% acima de €83.237,40 / €138.729) | GPMĮ art. 23(7): "tarifai taikomi atsižvelgiant tik į tos išmokamos išmokos dydį"; "gyventojo prašymu … atsižvelgdamas į bendrą per mokestinį laikotarpį … išmokų sumą" |
| D2 | DD Country Fields I10 — Incapacity Level | "levels are 0 -20%, 30 -55%" | "0-25% (€1,127) and 30-55% (€1,057)" | GPMĮ art. 20(6) |

Conferência mecânica: diff célula a célula V3.0 × V3.1 = só as células acima (WTC 9, DD 7, contando o Version Control); imagens preservadas; `validate_workbook.py` PASS (0/0/0) nos dois.

### Alinhamento CCG × Alerta × WTC × DD (depois das correções)
| Regra 2026 | CCG | Alerta | WTC | DD |
|---|---|---|---|---|
| Faixas 20/25/32% (83.237,40 / 138.729) | ✓ | ✓ | não guarda valor | — |
| 25%/32% só a pedido do empregado | ✓ | ✓ | flag 58205 | ✓ (G12) |
| NPD fórmula única, zero acima de €2.677,49; €1.127/€1.057 | ✓ | ✓ | flags 58204/58214 | ✓ (I10, mapper 0-25 / 30-40 / 45-55) |
| Seguro-saúde isento até €350 (teto 25%) | ✓ | ✓ | ✓ (65630, 23610, 65810) | — |
| Presentes até €200 | ✓ | — | ✓ (65805/65835) | — |
| Doença 15% e fora da base da Sodra | ✓ | — | ✓ (79408) | — |
| Teto Sodra €138.729 | ✓ | ✓ | não guarda valor | — |
| Desemprego 1,31/2,03; grupos de acidente I–IV | ✓ | — | — | ✓ (Employment Type, Type of Employer) |
| Fundos 0,16% + 0,16% | ✓ | — | ✓ (52550/52565) | — |

Nenhuma divergência restante entre os quatro. Ressalvas: a incidência da Sodra sobre o excesso do seguro-saúde (WTC 65630 "SI Yes"; Alerta diz "likely") e as taxas 0,16% / PSD 6,98% não foram lidas em fonte primária.

## Frentes que mexeram
| Data | Frente | O quê |
|---|---|---|
| 2026-10-27 | pipeline | Etapa 1: cópias corrigidas do CCG 2026 e do Alerta 2026, nada enviado ao Drive |
| 2026-10-27 | pipeline | Etapa 2: WTC V3.1 e DD V3.1 (Draft) + matriz de alinhamento, nada enviado ao Drive |
| 2026-10-27 | pipeline | Drive: CCG `_v1.1.docx`, Alerta `_v1.1.docx` (Google Doc oficial não editado), WTC V3.1, DD V3.1 copiados como arquivos novos; md5 conferido; aguarda aval |
| 2026-10-27 | pipeline | Alerta aprovado pelo usuário (via janela geral). Item 1: citação do teto 2025 retirada do `_corrigido.docx` local ("…annual ceiling of €138 729 (2026)"). Edição do Google Doc oficial **bloqueada pela permissão do Claude Code** (export conferido = original, nada alterado); a cópia `_v1.1.docx` no Drive ficou sem o item 1 |
| 2026-10-27 | pipeline | Com ok do usuário no chat: Google Doc oficial do Alerta (ID 1-Pgcq2dzv…, ligado à CT-4285) corrigido por Localizar/substituir: 8 trocas, cada uma com 1 ocorrência (faixas, 0% → 20%, nota 25%/32%, frase do pedido, teto €138 729 ×2, teto 2025 retirado). Export txt: "82 962", "138 270", "126 532" e os textos antigos = 0 ocorrências; os 7 textos novos = 1 cada; tabela Below/20%/Between/25%/and above/32%. A cópia `_v1.1.docx` no Drive fica superada pelo Doc oficial |
| 2026-10-27 | pipeline | A pedido do usuário: cópia `_v1.1.docx` do Alerta apagada do Drive (09 - Alerts/2026; vai para a lixeira do Drive). Fica só o Google Doc oficial, já corrigido. O `_corrigido.docx` local continua como registro |
| 2026-10-27 | pipeline | Corrigido o que faltou na etapa 1: tabela de faixas do CCG ainda dizia "32% of the excess over 138 270" (a regra de troca só pegou a 1ª célula da linha) → 138 729, destacado; Drive v1.1 docx regravado (md5 1e006a7c…). Versões Google criadas: CCG 2026 v1.1 (Doc), WTC V3.1 e DD V3.1 (Sheets); links no monday e na CT-4285 |

# Lituânia: mudanças de 30/10 a partir das fontes vigentes (SAM v1.2, GPM313 v1.3, SIR v1.2)

> Hub [[Lituania]] · Base: [[Research Pipeline/Lithuania/2026-10-29-correcoes/CONFERENCIA]] · Reconferência da V-243: [[Research Pipeline/Lithuania/2026-10-29-correcoes/V243-RECHECK-2026-10-30]] · Lista do BAU: [[Research Pipeline/Lithuania/2026-10-29-validacao-BAU/LISTA-PARA-O-BAU]]

O usuário autorizou em 30/10: "tudo o que for necessário para finalizar este processo". Nada vai para os tickets antes da validação do BAU (instrução de 29/10).

## Fontes novas, arquivadas em `raw/docs/oficiais/LT/` em 30/10 (e-TAR, baixadas pelo Chrome)
| Arquivo (.docx e .txt) | Ato | Redação | md5 do docx |
|---|---|---|---|
| `2026-10-30-V-243-suvestine-2026-10-03` | Ordem da Sodra V-243 (regras SD, SAM no cap. IX) | em vigor desde 2026-10-03 | 70a88233bfe9ecf24f22847af8ead458 |
| `2026-10-30-XII-2604-GF-ILDIF-suvestine-2026-01-01` | Lei XII-2604 (Fundo de Garantia e ILDIF) | em vigor desde 2026-01-01 | f66bd3543b6375d0f009ac475354267e |
| `2026-10-30-IX-1691-pensiju-kaupimo-suvestine-2026-01-01` | Lei IX-1691 (acumulação de pensão) | 2026-01-01 a 2026-12-31 | 9fde1017f38e4a26b91f493f3695b84e |
| `2026-10-30-IX-2112-MAI-suvestine-2026-07-01` | Lei IX-2112 (Administração Tributária) | em vigor desde 2026-07-01 | f2af4be59f505b2bded5dcc13ae1ce95 |

Também lido (não arquivado; o PDF é um folheto): Sodra, "Aktuali informacija draudėjams 2026 metais", p. 1. Diz que o teto de 60 VDU (€138 729) vale para as contribuições VSD do segurado e do empregador. https://sodra.lt/wp-content/uploads/2025/12/Aktuali-informacija-draudejams-2026-metais.pdf

## Achados (lidos por mim no texto)
1. **Dia não útil, Sodra:** V-243, ponto 125: "Jeigu paskutinė termino diena tenka ne darbo dienai (šeštadienis ir sekmadienis) ar oficialios šventės dienai, SD pranešimo pateikimo termino pabaigos data laikoma po jos einanti darbo diena."
2. **Dia não útil, VMI:** IX-2112, art. 162(6): "Tais atvejais, kai paskutinė termino diena tenka ne darbo ar oficialios šventės dienai, termino pabaigos diena laikoma po jos einanti darbo diena." O GPM313 de julho de 2026 vence em 15/08/2026, um sábado (e feriado oficial, Žolinė), e passa para **segunda-feira, 17/08/2026**.
3. **V-243 vigente:**
   - Os pontos 249 e 250 não existem (o texto termina no ponto 127). O canal (EDAS, FFData, assinatura qualificada) está no ponto 8.
   - O ponto 84.1 trata da decisão sobre correção de dados, não do aceite da SAM.
   - Os pontos 95.4 e 96.4 valem para a correção por escrito (novo SAM com P35, pontos 93 a 97), não para o anexo PT.
   - A assinatura da SAM está no ponto 8; o ponto 88 é do PT.
   - Mapa da redação de 2015: 103.6–103.7 → 86.6–86.8; 104.2 → 52; 111 → 125.
4. **Teto de 60 VDU:**
   - I-1336, art. 10(9): acima do teto aplica-se taxa 0% às contribuições com taxa aprovada pela lei anual de indicadores do orçamento; o PSD fica fora do teto.
   - O Fundo de Garantia (XII-2604, art. 5(3)), o ILDIF (art. 14(3)) e a pensão de 3% (IX-1691, art. 8(1)) incidem sobre "a renda sobre a qual se calculam as contribuições do seguro social". As taxas deles vêm dessas leis, não da lei do orçamento.
   - **Posição:** acima do teto, continuam devidos o PSD 6,98, o Fundo de Garantia 0,16, o ILDIF 0,16 e, para participantes, os 3%.
   - **Confiança 85%:** não há texto oficial da Sodra que diga isso para o Fundo de Garantia e o ILDIF. Como a SAM declara isso no mês em que se cruza o teto (P3, A11, A12) fica para confirmar com a Sodra ou o BAU (item B11 da lista).

## Mudanças
### SAM v1.1 → v1.2 (`LT-SODRA-003-SAM-Spec`)
Aplicar as correções propostas no `V243-RECHECK-2026-10-30.md`, linhas com veredito RENUMBERED, NOT FOUND ou CONTENT DIFFERS:
- Report Matrix!G2 e I2;
- Population Rules!C4, D4, C13 e D13;
- SAM Spec!M13, T13 e M29.

Além disso:
- **SAM Spec!T46** (resíduo do RA): resolver o teto do Fundo de Garantia, do ILDIF e dos 3% com o achado 4. A dúvida que fica é como a SAM declara o mês em que se cruza o teto.
- **Population Rules!D7:** acrescentar que, acima do teto, PSD, Fundo de Garantia, ILDIF e os 3% continuam (achado 4).
- **Version Control:** linha nova 1.2.

### GPM313 v1.2 → v1.3 (`LT-VMI-001-GPM313-Spec`)
- Example Analysis!D5: o prazo de 15/08/2026 passa para 17/08/2026 pelo art. 162(6) da IX-2112.
- Version Control: linha nova 1.3.

GPM312 v1.2 fica como está: o prazo de 15/02/2027 cai numa segunda-feira.

### SIR v1.1 → v1.2 (`LT-SIR-001`)
- Fechar a lacuna G15 em `s06_sla` e `s08_gaps` (frase "It does not claim a next-working-day shift"), com os achados 1 e 2.
- Atualizar a fonte da V-243 (redação vigente arquivada) onde o SIR citar a redação não arquivada.
- Fechar ou reduzir a G16 só no que se refere ao texto da V-243. Os PDFs da DataService e o `sam-v07.mxfd` continuam pendentes.

## Frentes
| Data | Frente | O quê |
|---|---|---|
| 2026-10-30 | pipeline (Process Lithuania) | Fontes vigentes baixadas e lidas; lista de mudanças |
| 2026-10-30 | pipeline (Process Lithuania) | Gerados SAM v1.2 (md5 feb69ec491f9b6ef67643e02bc971eb8), GPM313 v1.3 (7374bfdb2db71400e4565e60ffc4f314) e SIR v1.2 (2730aff9545c357d7838f462eb513e29). validate RSPEC PASS; check_sam 106/0; check_gpm 0 erros. Diff independente (janela): só 16 células na SAM e 6 no GPM313, as previstas. **Ainda não estão no Drive**: esperando o ok do usuário |
| 2026-10-30 | pipeline (Process Lithuania) | 2ª rodada (etapa 1): SAM v1.2 regerada (87bed94be9abc24397bb48a7d776f6f2), GPM313 v1.3 (703607856164c37056f4640988d02d35), SIR v1.2 (804d89c4180a6e2ffbaffd3d7b5b0aa2): teto, 3 % no P3, TaxRate 5, dia útil, G10/G16. Todos PASS. Só local → [[Research Pipeline/Lithuania/2026-10-30-fontes-vigentes/RESULTADO-ETAPAS-1-2|RESULTADO-ETAPAS-1-2]] |

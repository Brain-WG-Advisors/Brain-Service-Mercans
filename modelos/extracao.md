# Extração: {{fonte}} ({{AAAA-MM-DD}})

> Arquivo: `extracoes/AAAA-MM-DD-<fonte>[-<lote>].md`. Um cartão por item. Só entra o que muda a resposta certa.
> Material bruto: `raw/<fonte>/...` · Inventário: `inventarios/<fonte>.md` · Padrão: [[PLANO]] §4 (níveis A/B/C/D) e §5 (validação, lotes de até 40).

## Resumo
- Itens do inventário neste lote: N · Cartões: N · Complementos de cartão existente: N · Descartados: N
- Risco alto: N (100% vão para validação) · Amostra dos demais: N (10%)
- Validação: ⏳ pendente / ✅ feita em AAAA-MM-DD (confirmados N/N = X%)
- Ingestão: ⏳ pendente / ✅ feita em AAAA-MM-DD

## Cartões

### {{FONTE}}-{{AAAAMMDD}}-C01 · {{tipo}} · [[{{Pais}}]]
- **Chave:** `{{PAÍS}} | {{ARTEFATO}} | {{ITEM}}` · **Já existe?** não / sim → complementa [[correcoes]] linha AAAA-MM-DD / hub §...
- **Tipo:** erro+causa / decisão / versão final / alerta / pendência
- **Risco:** alto (valor estatutário, correção de erro, versão vigente) / normal
- **Serviço:** [[research-pipeline]] / [[design]] / [[suporte]] / fronteira
- **O que diz:** uma ou duas frases, sem dados pessoais
- **Antes (se erro):** o que estava errado e onde (artefato vX.Y, resposta de AAAA-MM-DD)
- **Causa (se erro):** por que aconteceu (fonte secundária, cópia de outro país, leitura literal...)
- **Correto / novo:** valor ou regra, com vigência (`a partir de AAAA-MM-DD`)
- **Nível de evidência:** A / B / C (D não vira cartão) · **Fonte:** lei/artigo, manual, artefato+versão ou ticket+comentário
- **Localização no raw:** `raw/...` + local exato (comentário de AAAA-MM-DD, item <ID> do board, minuto 12:30, aba "Version Control" linha 14)
- **Quem decidiu / pediu:** papel ou nome do lado Mercans (opcional; obrigatório quando o tipo é decisão)
- **Destino:** hub (seção) / [[correcoes]] / skill `payroll-compliance-<pais>` / [[fronteiras]] / `servicos/...`
- **Pergunta para o teste (Conjunto B)?** sim → rascunho da pergunta / não
- **Confiança da extração:** alta / média / [INCERTO] (motivo)
- **Validação:** ⏳ / ✔ confirmado / ✘ rejeitado (motivo)

## Descartados
| Item (ID no inventário) | Motivo |
|---|---|
| | já registrado sem informação nova / sem impacto na resposta / dado pessoal / outro time / só acknowledgment |

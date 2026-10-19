# Prompt curto: extração de UMA conversa

> Como usar: abra a conversa (não o projeto) no Claude da Mercans, cole o prompt abaixo no fim dela, copie a resposta
> e salve em `raw/chats/AAAA-MM-DD-<projeto>-<assunto>.md`. Depois diga aqui: "ingere raw/chats/<arquivo>".
> **Atualizado em 2026-10-19:** na construção do brain (F3 do PLANO), as conversas são copiadas na íntegra pelo Chrome
> ([coleta-chrome.md](coleta-chrome.md) §F3) e as seções abaixo servem de **roteiro de extração** aqui no Claude Code.
> Colar este prompt numa conversa só quando não for possível copiá-la. Escopo: 2026-01-01 em diante.

---

```
Resuma SOMENTE o que foi decidido ou corrigido nesta conversa, para uma base de conhecimento. Não invente; dúvida → [INCERTO]. Sem dados pessoais de funcionários de clientes.

Responda em Markdown:

## Conversa
- Data(s), país(es), ticket(s) citados, artefato(s) tratados.

## Decisões
- AAAA-MM-DD | País | Decisão | Por quê | Fonte legal citada

## Correções (algo que nós dissemos/entregamos errado e foi corrigido)
| País | Errado | Correto | Fonte |

## Versões de artefato que saíram desta conversa
| País | Artefato | Versão | Data | O que mudou |

## Pendências deixadas em aberto
- O quê | de quem

## Itens específicos (responda só se esta conversa tratou deles)
- Espanha, Modelo 190: a remoção de B/03 e L/27 pelo Dev (~14/09) foi intencional ou regressão?
- Espanha: SR-83, SR-432 (77 campos novos no DD?), HRBS-10563.
- Ucrânia, sick leave: período-base de 6 ou 12 meses? Faixas de %? Código 4DF 128?
- Kuwait HRBS-8606: o que foi perguntado e respondido?
- Côte d'Ivoire HRBS-14996: desfecho após 25/09.
```

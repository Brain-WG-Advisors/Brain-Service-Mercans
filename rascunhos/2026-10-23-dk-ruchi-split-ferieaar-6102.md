# Dinamarca — Ruchi: separar saldo por ano de férias na rescisão (Record 6102) — 2026-10-23

Pedido: Ruchi, chat STG: Denmark 23/10 03:59–04:01 e comentário no CCG às 04:05. Mohit, 05:20: "urgent… double check with Enaakshi". Comentário novo da Ruchi às 03:51 no CCG 9.2, passo 7 ("Calculate gross holiday pay: Qualifying earnings × 12.5%"): "please correct here as well for proration".
Material: `raw/chats/2026-10-23-dk-es-respostas-ruchi-nihita-mohit.md`. Nada postado.

## Fontes (lidas pessoalmente em 23/10)
| Fonte | Trecho |
|---|---|
| BEK nr 1054 af 23/09/2024 (bekendtgørelse om ferie) § 7 stk. 1–2 — `raw/docs/oficiais/DK/2026-10-23-BEK-1054-2024-bekendtgorelse-om-ferie.pdf` | "For fratrådte lønmodtagere, som har ret til løn under ferie, skal arbejdsgiveren senest den sidste dag i fratrædelsesmåneden indberette oplysninger om antal optjente feriedage og feriegodtgørelse" … stk. 2: líquido de A-skat e AM "på den af Skattestyrelsen anviste måde" |
| eIndkomst Indberetningsvejledning v17.0, § 8.3.2 — `...-eindkomst-indberetningsvejledning-v17.0.html` | "Samtidig skal de optjente nettoferiepenge og de tilhørende feriedage indberettes pr optjeningsår"; "Er der restferiedage for mere end ét år, skal felterne Ferieår, Restferiedage og Nettoferiepenge gentages for hvert år"; "Ferieår angives således: 2020 = Optjeningsperiode 01.09.2020-31.08.2021, 2021 = Optjeningsperiode 01.09.2021-31.08.2022, Osv."; "én record 6002 med feriepengeudbetaler for op til to record 6102" |
| eIndkomst Teknisk vejledning v11.6, 4.16 Record 6102 — `...-eindkomst-teknisk-vejledning-v11.6.html` | "Denne record skal gentages, hvis der skal indberettes for flere ferieår." Campos: 3 Nettoferiepenge pos 12 len 16 ("for det angivne ferieår", 6 decimais); 5 Feriedage pos 29 len 4 (2 decimais); 7 Ferieår pos 34 len 4 ("Periode, hvor feriepengene er optjent"); 8 Fratrædelsesdato pos 38 len 8 |
| FerieKonto, Vejledning til lønservicebureauer (set/2025) — `...-2026-10-23-FerieKonto-vejledning-lonservice-2025-09.pdf` | Obrigatórios: "Restferiedage pr. optjeningsår (med 2 decimaler) • Nettoferiepenge pr. optjeningsår (med 2 decimaler) • Fratrædelsesdato" |
| Ferieloven LBK 152/2024 §§ 4, 6, 16 stk. 4 | Ferieår 1/9–31/8; afholdelse no ferieår + 4 meses; 12,5% sobre a férias paga acumulada e não gozada |

## Conclusão
- Sim, separar: um Record 6102 por ano de férias (ano de optjening), com o ano no campo 7. Para saída em out/2026: um 6102 com Ferieår 2025 (saldo de set/2025–ago/2026) e outro com Ferieår 2026 (set–out/2026).
- O layout oficial não tem campos "previous/current": é o mesmo registro repetido, e quem diz o ano é o campo 7 (pos 34–37). As posições 12–27 e 29–32 do motor batem com os campos 3 e 5.
- O bruto (campo 13), a A-skat e o AM-bidrag podem ir somados num único registro de renda; só o 6102 é separado por ano.
- Prazo: indberetning até o último dia do mês da saída (BEK § 7) → saídas de outubro vencem em 31/10. Por isso a urgência do Mohit é real.
- ⚠️ "2025" e "2026" como códigos saem do padrão oficial "2021 = 01.09.2021-31.08.2022, Osv." (não há exemplo com 2025).

## Rascunhos (EN)
**Ruchi (chat, resposta à mensagem das 03:59):**
> Yes, split by holiday year. eIndkomst requires untaken days and net holiday pay per earning year: Record 6102 is repeated once per ferieår, with the year in field 7 (pos. 34–37). For an October 2026 leaver: one 6102 for ferieår 2025 (Sep 2025–Aug 2026) and one for 2026 (Sep–Oct 2026). There are no previous/current fields in the official layout. The gross amount, AM-bidrag and A-tax can stay as one total. Sources: eIndkomst Indberetningsvejledning § 8.3.2, Teknisk vejledning 4.16, BEK 1054/2024 § 7. I'll add the scenario to CCG section 9.2.

**Mohit (chat, resposta à mensagem das 05:20):**
> Agreed, it's urgent: October leavers must be reported by 31 Oct. I've answered Ruchi from the eIndkomst and FerieKonto rules and will review it with Enaakshi on Monday.

## CCG 9.2 (sugestão, após ok do usuário)
- Passo 6: "Calculate qualifying earnings **per holiday year** (current HY and, if still in its taking period, the previous HY) …"
- Passo 7: "Qualifying earnings × 12.5% × (untaken earned days ÷ earned days), per holiday year (Ferieloven § 16(4); LSF 116, note to § 16(4)). Report each year in its own Record 6102 (ferieår in field 7)."

## Planilha "Holiday Pay Upon Termination" (Ruchi, 1z2H9du…) — 6 comentários de 23/10 04:13–04:48
G15 (aba 1, 2.008,55: "how did you calculate 2275.64 if there is no accrual in May"): resposta digitada na thread, não publicada (o usuário publica).
- Fontes: STAR Q&A ferietillæg (07-07-21; página de 22-05-2023) `raw/docs/oficiais/DK/2026-10-23-STAR-spoergsmaal-og-svar-ferietillaeg.html` — maio = 1% da løn 1/9–31/5; na fratræden, 1% só para "afholdte ferie, som der ikke allerede er udbetalt ferietillæg for"; mês conta só ao fim ("først er optjent ved udgangen af måneden"); já pago não volta. Ferieloven § 18 e § 19 stk. 1.
- Fórmula da célula: =G13/I13*E13 (3.760/18,72×10) → base sem maio, dias com maio.
- Sem texto oficial: fórmula por dia (proporção dias gozados ÷ ganhos) — método do CCG, análogo ao 12,5% (LSF 116).
Pendentes: G21 (= pergunta do 6102), G20 (600,96), G23 (2.173,08), G24 (29.150,00), G25 (8.653,85).

## Planilha — respostas publicadas (23/10)
G15, G20, G23, G24, G25, G21 respondidos pelo usuário (texto acima/na conversa). G20/G23: 1% = 0 (dias do HY1 já suplementados em maio/agosto; STAR). G24: 29.150 certo. G25: 8.538,46 (só 4,96 dias transferíveis, § 21; 5 dias dentro das 4 semanas → Feriefond, § 34). G21: separar por ano; 39.730,77.

## CCG — sugestões aprovadas pelo usuário, a inserir (modo Sugestão) → aval da Ruchi → aceitar → Enaakshi revisa
Contradições internas achadas no CCG (export de 22/10 21:13): 9.2 passo 7, passo 14, nota IMPORTANT ("lump-sum"); Leave Entitlement "Holiday Bonus 1%" item 5; 5.3 (maio "proportional to days taken"; linha "On termination"; exemplo da Enaakshi ÷2,08); 9.1 (só HY atual); 4.1 e 10 (sem proporção).
- A passo 7 (+ proporção por ano, 6102, base inteira p/ 1%); B cenário dois anos (casos 1 e 2 da planilha); C passo 14; D nota IMPORTANT; E bonus abril/junho; F 5.3 maio e "On termination"; G exemplo 5.3 refeito (base 495.393,55; 27.915,48; 680,17); H 9.1; I 4.1 e 10.
Textos completos: na conversa de 23/10 (frente chat).

## CCG — sugestões inseridas (23/10 ~11:30–11:45, modo Sugestão, autor Wallisson) — 15 cards
A passo 7 (append) · B cenário dois anos (parágrafo novo depois da nota IMPORTANT, dentro da caixa da nota — formatação a revisar) · C passo 14 · D nota IMPORTANT · E1/E2 Holiday Bonus 1% (abril/junho) · F1 5.3 maio · G1–G3 exemplo 5.3 (27.915,48; 1% × 495.393,55 × 3 ÷ 21,85; DKK 680,17) · H 9.1 · I 4.1 + 3 linhas da seção 10.
F2 não inserida: na 5.3 "On termination" o texto antigo já está tachado (formatação da Enaakshi) com a regra certa ao lado.
Incidentes: sugestão automática "Add link" (businessindenmark.virk.dk) ao dar Enter → recusada; vírgula da I (4.1) caiu uma letra antes → Ctrl+Z e refeita; Escape com foco no botão "próxima" não fechou a busca (texto foi para o campo de busca, nada no documento).
Conferência: export txt idêntico ao de antes (185.018 caracteres) → texto oficial intacto; 15 sugestões no painel.
Próximo: mensagem à Ruchi (aval) → aceitar → mensagem à Enaakshi.

## Divisão de frentes (23/10)
Por decisão do usuário, os 2 comentários da Ruchi no CCG (3h51, passo 7, proporcionalidade; 4h05, divisão HY1/HY2 no 6102) ficam com a janela Pipeline (pipeline-c4). A frente chat não mexe neles. Contexto enviado ao Pipeline: as sugestões A–I e as respostas da planilha, para não haver sugestão duplicada ou contraditória.

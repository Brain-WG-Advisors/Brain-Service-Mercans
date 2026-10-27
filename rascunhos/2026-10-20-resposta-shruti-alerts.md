# Rascunho — resposta à Shruti (baseline de alertas) — 2026-10-20

Contexto: [[2026-10-20-shruti-alerts-baseline]] (raw/chats). Ela não mandou o baseline nem disse o país nem quais alertas faltaram, então o conselho é de método. Os tipos de lacuna listados vêm da nossa conferência da Espanha no Compliance Calendar (rascunhos/2026-10-19-compliance-calendar-ES-conferencia.md), onde cada um foi visto de fato.

## Rascunho (EN, para colar — não enviado)
Hi Shruti, sure, happy to connect. To review it properly, could you share the baseline file, the country, and 2–3 examples of alerts that were not captured?

Meanwhile, these are the gaps I found when I checked the Spain events against the official sources, so they're worth checking in yours:

1. Build the baseline from the official calendar of each authority (tax, social security, labour), not from the tool's list. Each line should have the obligation, frequency, legal due date and the source link to that exact page.
2. Expand recurring obligations to every period of the year. In Spain the tool only had January to March; monthly and quarterly filings for the rest of the year were missing.
3. Apply the weekend/holiday rule from the law. Some deadlines move to the previous working day and others to the next one (Spain: Seguros Sociales move back, Modelo 190 moved forward to 2 Feb). A weekday check catches most date errors.
4. Split obligations that depend on employer size or regime (e.g. monthly vs quarterly withholding). If the event doesn't say who it applies to, it looks duplicated or gets skipped.
5. Include public holidays and annual events (year-end returns, annual summaries, rate or ceiling changes with effective dates), not only monthly filings.
6. Compare line by line: baseline vs published, on date, frequency and applicability. Anything only in the baseline is a missed alert; anything only in the tool needs a source.

Send me the file and we can go through it together.

## Rascunho v2 — só as perguntas (decisão do usuário, 20/10; não enviado)
Hi Shruti, sure, happy to help. Before we connect, could you send me:
1. The baseline file.
2. Which country it is for.
3. Two or three examples of alerts that were not captured.

The checklist above (v1) fica guardado para depois que ela responder.

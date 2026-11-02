# EUA — fontes bloqueadas depois da passada 2 (Chrome), 2026-10-29

> Frente EUA ([[frentes/eua/estado|estado]]). Base dos relatórios dos 7 agentes da passada 2. Registro: 255 linhas (208 ativas, 25 MANUAL, 22 gated).

## Tipo 1 — Permissão da extensão Claude in Chrome (o usuário libera o domínio)
Mensagem: "Permission denied for reading page content on this domain".
- mass.gov · michigan.gov · maine.gov · mo.gov (dor.mo.gov) · laworks.net · marylandcomptroller.gov · revenue.state.mn.us
- revenue.ky.gov · dol.georgia.gov · tax.hawaii.gov · flsenate.gov
- Não testados no G3 (provável o mesmo): revenue.louisiana.gov, la.gov, legis.la.gov, labor.maryland.gov, mn.gov, dor.ms.gov, mdes.ms.gov, malegislature.gov, legislature.mi.gov, revisor.mo.gov

## Tipo 2 — Bloqueio por país / antirrobô (não contornar)
- **Bloqueio por país confirmado:** dew.sc.gov (CloudFront "block access from your country"), twc.texas.gov (CloudFront geo-block)
- Cloudflare/Akamai/F5: azdor.gov, ncleg.gov, leg.state.nv.us, detr.nv.gov, vec.virginia.gov, gc.nh.gov, jobs.utah.gov (403), dwd.wisconsin.gov (403), floridarevenue.com (security check)
- Saída possível: VPN com saída nos EUA (decisão do usuário) ou colega nos EUA baixa o documento.

## Tipo 3 — Não carrega nesta rede (DNS / conexão recusada, Chrome e fetch)
- tax.illinois.gov, ides.illinois.gov · www.in.gov · tax.idaho.gov · ksrevenue.gov · revenue.nebraska.gov, nebraskalegislature.gov · mtrevenue.gov, revenue.mt.gov, mt.gov
- Legislaturas: code.wvlegislature.gov, docs.legis.wisconsin.gov, legislature.vermont.gov, le.utah.gov, webserver.rilegislature.gov, oregonlegislature.gov, oscn.net, codes.ohio.gov
- Provável a mesma causa do Tipo 2 (bloqueio por país). Teste do usuário: abrir `https://tax.illinois.gov` no navegador comum.

## PDFs que o Chrome não lê (texto vazio)
NYS-50-T-NYC; ND UI rate schedules 2026; OH WHT_PercentageMethod_2026; CCA 2026 Withholding Form-i; PA llc-2; NM FYI-104 2026; UT Pub 14; Delaware PFL Employer/TPA Guide; EDD PDFs. Alguns foram lidos por download (WebFetch) + extração local de texto (VA, WV, VT, GA, rp-25-19) — linhas marcadas.

## Leituras fora da regra (antes da proibição de 29/10)
Agentes G1, G4, G5, G6 usaram `javascript_tool` (extração de texto, abrir seções) antes do aviso; G1 e G6 alteraram texto para passar pelo filtro "[BLOCKED: Cookie/query string data]". O texto lido é o da página oficial, mas o método não estava autorizado. Só G6 marcou as linhas no registro (6 linhas "javascript_tool, pre-rule"); G4 (NY MCTMT, NYS-50 UI, NC DES, NH NHES/DRA, NJ DOLWD, NM TRD) e G5 (tax.ohio.gov, jfs.ohio.gov, oklahoma.gov, dced.pa.gov) e G1 (pdf.js: CA DE 231PS, DE 44 e outros) estão listados nos relatórios. **Decisão do usuário:** aceitar essas leituras ou refazer com get_page_text.

## Teste na sessão principal (29/10, sessão "pode abrir")
Leitura no Chrome desta sessão, uma página por domínio:
- **Abrem e leem (o "Permission denied" foi só nas abas dos agentes):** mass.gov (Withholding Tax Guide, Aug 2026, lido), michigan.gov, revenue.ky.gov, marylandcomptroller.gov, revenue.state.mn.us, dor.ms.gov, tax.hawaii.gov, dol.georgia.gov, **tax.illinois.gov** (antes não carregava).
- **Bloqueio por país (CloudFront):** maine.gov ("request could not be satisfied"), twc.texas.gov ("configured to block access from your country").
- **Antirrobô:** dor.mo.gov (Incapsula), louisiana.gov (Cloudflare "Sorry, you have been blocked").
- **Não carregam (página de erro do navegador):** in.gov, tax.idaho.gov, ksrevenue.gov, revenue.nebraska.gov.
→ Para estes: Wayback, VPN EUA (TI) ou colega nos EUA.

# Browser pass brief — ACCESS gaps (US build)

Orchestrator, 2026-11-02. BASE = C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance (never write under ~/mercans-pipeline).

Fact found today: sites that return 403 to curl (ssa.gov, mass.gov, …) often open normally in the user's Chrome, even without the VPN. So this pass reads them in Chrome.

## Tools and rules
- Load in ONE ToolSearch call: select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__javascript_tool
- tabs_context_mcp first, then create YOUR OWN tab; never touch tabs you did not create; close yours at the end. Another worker may use another tab.
- Read pages with get_page_text. PDFs: in the page, `const r=await fetch(url); const b=await r.blob(); const a=document.createElement('a'); a.href=URL.createObjectURL(b); a.download='<NAME>.pdf'; document.body.appendChild(a); a.click()` (javascript_tool is allowed ONLY for this download step and for listing links — never to alter page text). The file lands in C:\Users\instituto\Downloads; move it into ccg-sources/{JUR}/ and record its md5. If Chrome blocks repeated downloads on a site, read the PDF in the viewer by screenshots (save_to_disk) and transcribe only the needed numbers.
- Never bypass CAPTCHA, Cloudflare challenges or login walls; never submit forms other than a site's own search box; no alerts/dialogs. A page behind a challenge or login stays a gap — record it and move on.
- Save every page's text as a .txt under 00-official-sources/ccg-sources/{JUR}/ with first line `URL: … | read 2026-11-02 in Chrome`.
- Numbers only from the page/document itself. Tier A.1 statute/regulation on official host, A.2 agency page, A.3 agency guidance.

## Outputs
- Shard `00-official-sources/_register-shards/S5B-{WORKER}.csv` (20 columns as legal-basis-register.csv; ids `US-{JUR}B5-NNN`; `supersedes` set where the new row replaces a gated/MANUAL/partial row for the same fact).
- `_research/stage5/browser-pass-{WORKER}.md`: per target URL → result (read / still blocked + why), register ids, and which open question / unresolved fact key it closes (use the keys in `_research/*-facts.json` `unresolved[]` and `_research/stage5/{JUR}.md`).
- Do not edit legal-basis-register.csv, facts files, MANDATE.md or the manifest.

## Budget
About 80 page reads per worker; at 75% stop and write the files. Write the shard incrementally.

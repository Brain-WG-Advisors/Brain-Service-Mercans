# Mandate answers P5-W2A-r2 - NJ MA VA TN IN (PASS 4, wave 2A, round 2, 2026-10-29)

Register: `00-official-sources/_register-shards/mandate-P5-W2A-r2.csv` (10 rows). Own Chrome tab, closed. About 14 reads: nj.gov x6, tn.gov DOR, 5 WebFetch statute/agency pages. Blocked this round: Wayback HTTP 429 twice (shared throttling by parallel workers; recorded gated); Chrome "permission denied" on mass.gov, vec.virginia.gov, law.lis.virginia.gov, lwdsupport.tn.gov; tn.gov FAQ-UI-Tax-TPAs.pdf unreadable-pdf; law.justia.com Cloudflare check (gated, not solved); iga.in.gov script-rendered (no text); WebFetch 403 on vec.virginia.gov, mass.gov, justia, tn.gov/workforce.

## NJ
- p2 local: PARTIAL. Payroll page and 27-form payroll index (page 1 of 2) show no local wage tax; Newark employer payroll tax still unconfirmed (US-NJP52-002). Confidence M.
- p6: PARTIAL. Pay statement ANSWERED and CORRECTED: N.J.S.A. 34:11-4.6(c), not 34:11-4.4 (US-NJP52-001, supersedes US-NJ-003): statement of deductions each pay period; employers with 10+ employees add gross, net, rate of pay, hours; electronic allowed. Prevailing wage (Act, Commissioner of Labor) from round 1. POA M-5008-R still listing only; oracle none (re-derive from NJ-WT tables). Confidence H on pay statement.

## MA
- p2 local: PARTIAL. mass.gov unreadable this round (WebFetch 403, Chrome permission denied). No explicit absence page. Treat as none, low risk.

## VA
- p2 local: PARTIAL. tax.virginia.gov withholding page has no local-tax content (US-VAP52-005); not an absence statement.
- p3 SUI: PARTIAL. Employee contribution: none; 60.2-515 imposes tax on employers only (US-VAP52-001, webfetch-summary). Fund building 0.2% (60.2-533, US-VAP52-002). 2026 pool cost percentage: statute gives method only (US-VAP52-003); a search summary says 0.03% and is NOT usable; needs the VEC rate notice.
- p6: PARTIAL. VEC route is an ESS invitation via ID.me, no paper form (listing only, US-VAP52-004). Oracle: no calculator; tables (US-VAP52-005).

## TN
- p2 local: ABSENCE PROVEN (M-H). DOR full tax index (incl. locally administered and archived taxes) has no wage/payroll tax; Hall tax archived (US-TNP52-001).
- p4 levies: PARTIAL. DOR list has no SDI/PFML; DLWD programme list not read.
- p6: PARTIAL. UI POA: listing says POAs not required since 2025-05-27, TPA access via Employer e-Services (US-TNP52-002, not read). Pay statement: no itemized statute located (round 1). Oracle none.

## IN
- p3 SUI: PARTIAL. Wage base 9,500 and 2.5% new employer from search text only; no primary 2026 read; employee contribution unconfirmed.
- p4 levies: PARTIAL. No programme found; no primary absence page.
- p6: PARTIAL. IC 22-2-2-8 pay statement and common construction wage repeal known from secondary/search text only (US-INP52-001/002); state POA forms not located.

## PASS 4 (wave 2A round 2) - status after this pass
NJ 1:answered 2:partial 3:answered 4:answered 5:answered 6:partial
MA 1:answered 2:partial 3:answered 4:answered 5:answered 6:answered
VA 1:answered 2:partial 3:partial 4:answered 5:answered 6:partial
TN 1:answered 2:absence_proven 3:answered 4:partial 5:n/a 6:partial
IN 1:answered 2:answered 3:partial 4:partial 5:answered 6:partial

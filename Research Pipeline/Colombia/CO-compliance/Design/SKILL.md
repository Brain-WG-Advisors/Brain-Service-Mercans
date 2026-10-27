---
name: mercans-research-pipeline
description: Operating knowledge for the Mercans country compliance research pipeline (mercans_pipeline_v2_9.sh) — running it, diagnosing why it died, acquiring official source PDFs, auditing what it produced, and building country skill files. Use when launching or resuming a country build, when a pipeline stage fails or dies silently, when a source site blocks download, when deciding whether a statutory value is trustworthy, when patching the pipeline script or the mechanical audit, or when a QA/audit finding needs interpreting. Covers the infrastructure traps (Modern Standby, spend limits, max-turns), the research-integrity rules earned from real errors, and the strategies that failed.
---

# Mercans Research Pipeline — Consolidated Operating Knowledge

Built from the Bulgaria, Chile, Chad, Hungary, Spain, Belgium, France and China
runs (Apr–Aug 2026). Read §1–3 before launching anything; §4–6 when something
breaks; §7–9 for research quality.

---

## 1. What the pipeline is

`mercans_pipeline_v2_9.sh` — one command produces the full compliance package
for one country. **Filename says v2_9, internal header says v2.8** and all its
own usage examples reference `v2_8.sh`. Use the real filename; the comments were
never updated.

**11 stages:** CCG → Scope Lock-In → Report Specs → DD → WTC → SIR → Payslip →
Alignment Patch → Audit+Fixer → QA Cross-check → Skill.

**Runtime ~5–6h.** Heaviest: Stage 1 CCG (45–90 min), Stage 3 Report Specs
(60–120 min).

```bash
CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000 nohup bash "$HOME/mercans-pipeline/mercans_pipeline_v2_9.sh" \
  "Country Name" XX CUR 2026 Language > "$HOME/mercans-pipeline/XX-v29.log" 2>&1 & echo $!; disown
```

- `START_STAGE=N` — resume from a stage. **This is the single most valuable
  feature.** Before v2.5 a mid-run death meant restarting 5–6h from zero.
- `GENERATE_PROMPTS_ONLY=true` — writes all 11 prompts, zero API calls. **Use
  this as the first pass on any new country** to review prompts before
  committing hours.
- The country-name argument is injected verbatim into prompts. Use it to carry
  scope: `"China (Shanghai reference)"`, `"France (régime général)"`.
- `caffeinate` appears in the header examples — **macOS only, will fail on
  Windows.** Strip it.

**Structural facts worth knowing:** Stage 2 is a hard blocking gate — if the
scope manifest is malformed the run stops rather than generating garbage
downstream. Stage 9 runs mechanical checks C1–C31 plus a self-aware fixer that
can override false positives with written justification.

---

## 2. Pre-flight — never skip

```bash
env | grep -i anthropic        # must be EMPTY; an API key breaks Max OAuth
ping -n 3 google.com           # long runs die on flaky network
tasklist | grep -iE "excel|winword"   # lockfiles block the run
```

Required in `~/mercans-pipeline/shared/` (11 files, hard `exit 1` if missing):
`CCG_TEMPLATE_QUESTIONS.md`, `REFERENCE_CCG_Bulgaria.docx`,
`REFERENCE_Payslip_Tunisia.xlsx`, `REFERENCE_Payslip_Mozambique.xlsx`,
`mercans_logo.png`, `country_failure_log.md`, `PRESUBMISSION_AUDIT.md`,
`CZ_Data_Dictionary_V2_0.xlsx`, `Global_WTC_V1_0.xlsx`,
`_CZ_Wage_Type_Catalogue_V2_0.xlsx`, `scope_manifest_template.json`
— plus `report-spec-template/`.

Optional (warn only): `country_portal_registry.md`, `CCG-Playbook-Learnings.md`.

**Verify the requirement list by grepping the script, not from memory** —
`grep -n "REQUIRED_SHARED" -A15 <script>`. The list changes between versions.

**New machine (Windows):** Git for Windows → Node LTS → then
`npm install -g --allow-scripts=@anthropic-ai/claude-code @anthropic-ai/claude-code`
(npm 11.16+ blocks postinstall by default; the error message suggests
`npm approve-scripts`, which **does not work for global installs** — known npm
bug). Then `claude` → `/login` → option 1.

Extracting a Drive zip commonly produces `shared/shared/` — check and flatten.

---

## 3. The diagnostic protocol when a stage dies

**The main log almost never carries the real error.** It goes silent; the error
is in the per-stage log. This pattern repeated across Chad, France and China.

```bash
tail -40 ~/mercans-pipeline/XX-v29.log          # which stage, when
cat ~/mercans-pipeline/XX-compliance/logs/<stage>.log   # the real error
ls -la ~/mercans-pipeline/XX-compliance/0N-<artifact>/  # partial work?
claude -p "say ok" --max-turns 1                 # account still alive?
tasklist //FI "PID eq <pid>"                     # process alive?
```

**Read the failure signature:**

| Log text | Cause | Fix |
|---|---|---|
| `You've hit your org's monthly spend limit` | billing | switch account or wait |
| `Response stalled mid-stream` / `Connection closed mid-response` / `FailedToOpenSocket` | network | wait, re-run |
| silence, no error, died mid-stage | **Modern Standby** (see §4) | power override |
| `max turns` | stage turn ceiling too low | patch the script |
| instant repeated failures (4–6s) | spend limit | — |
| long run then failure | network | — |

**Partial artifacts in the output folder = real work interrupted**, not a config
error. Absent folder = died before it started.

`bash` waiting on a stage uses no CPU — the process doing the work is
`claude.exe`. Check both.

---

## 4. Infrastructure traps that cost days

**Windows Modern Standby (S0 Connected Standby) — the worst one.** Killed
France runs twice with zero log trace. `powercfg /a` showed S1/S2/S3 all
firmware-disabled; only S0 Low Power Idle available. The machine woke and slept
**17 times in 15 hours** — that is the mode working as designed, not a fault.
Each micro-wake drops the network mid-API-call and the process dies silently.

`standby-timeout` does **not** fix this — it governs entry by inactivity, not
the wake cycles. The fix:

```bash
powershell.exe -NoProfile -Command "powercfg /requestsoverride PROCESS \"claude.exe\" SYSTEM"
powershell.exe -NoProfile -Command "powercfg /requestsoverride"   # VERIFY it registered
```

Target `claude.exe`, not bash — bash idle at a prompt survives a network blip;
an open API call does not. **Verify the override listed before relaunching.**

**Spend limits.** Mercans Team account hits its monthly cap repeatedly.
`/usage-credits` only works in an **interactive** session — it does nothing
inside `claude -p`, so it can't be scripted into the pipeline. Approval needs
the org Owner. Personal Max is the practical fallback (`/logout` → `/login`).
claude.ai chat and Claude Code share the same Max pool.

**Max-turns ceilings.** Stages fail with `max turns` when a country is complex.
France needed Stage 2 raised 15→40 and Stage 10 raised 30→80. Patch the script
value; don't retry the same number.

**Excel.** Never `taskkill //F //IM EXCEL.EXE` — corrupted Tunisia and Ukraine
files. Close via the window. v2.5+ auto-cleans lockfiles >1h old.

**Ctrl+C often doesn't cancel Claude Code mid-stream** — keystrokes queue and
leak as text afterwards. `[1]+ Stopped` means suspended, not failed; `fg`
resumes. Git Bash has no `unzip`; use `tar` or Explorer.

**Hardcoded Mac path at line ~675** (`/Users/wallissongomes/...`) inside the CCG
prompt's self-check. Breaks only the H3-count self-check on Windows, not the
stage handoff.

---

## 5. Source acquisition — what works and what is blocked

**Order of trust:** official form PDF → official fill-in guide → official sample
file → web research (must be marked DERIVED).

**Blocked / do not waste time:**
- `droit-afrique.com` — 403 to any user agent, 261-byte HTML
- `natlex.ilo.org` — Cloudflare challenge
- `socialsecurity.be` — robots.txt blocks automation, **but a normal browser
  works and no login is needed.** Documentation is public; registration and
  certificates are only for *transmitting*.
- Belastingdienst developer portal — landing page only, PDF unreachable

**Techniques that worked:**
- `curl -s "<url>" | head -c 150` — reads a raw file when the browser hides it.
  This is how the UTF-8 XML prolog was finally confirmed after `view-source:`
  and print-to-PDF both failed (Chrome's XML viewer suppresses the prolog).
- Claude in Chrome on JS-gated Joomla/K2 sites: read URL constructor properties
  individually (`u.protocol`, `u.pathname`, `u.searchParams.get(...)`) rather
  than `a.href`, which the privacy extension blocks.
- Prefer `.xlsx`/`.xml` over `.pdf` for code tables — PDF extraction produces
  artefacts (`(cid:127)` where a comparison operator should be, which made a
  "≥ or ≤ 20%" threshold unreadable).
- **Have the user download it.** Repeatedly the fastest path. Give the
  navigation route (menus), not a constructed URL — generated CMS hashes rot
  between versions and 404.
- On multi-version portals, take **"Version complète"**, never "Mise à jour" —
  the update edition contains only that quarter's changes.

**Scanned PDFs** degrade numeric extraction badly. Chad's CGI 2025 was scanned;
realistic accuracy for such a country is **80–85%**, and 95%+ requires a paid
registered-agent review pass (~$500–2k). Say this out loud rather than implying
the pipeline will reach 95%.

---

## 6. Auditing what came out

**QA scores are not pass/fail.** France scored 87/100 *and* had three MAJOR
findings. Read the findings, not the number.

Real findings from France worth pattern-matching:
- 264 spec rows wrongly labelled as having no DD counterpart (alignment bug)
- two BIK wage types missing from the WTC
- one declaration inconsistently scoped across artifacts

**The mechanical audit itself has bugs.** Four were fixed in `_audit_v24_mechanical.py`
during France: a hyphen-normalisation bug in C20, a prose-reconciliation
recognition gap in C27, a BIC/SWIFT false positive in C29, and a math-symbol
Unicode mis-classification in C33. **When a check fails, verify the check before
"fixing" the artifact.**

Post-run verification that catches real defects:
- `python3 /mnt/skills/public/xlsx/scripts/recalc.py FILE 90` — **sandbox path
  only, never embed in a script that runs on Windows.**
- Residue scan on raw XML, skipping template scaffold sheets.
- **Scan entire sheets, not the first N rows** — a near-miss came from stopping at 90.
- **Diff every cell against the original before delivering.** This is what
  caught openpyxl silently converting text beginning with `=` into a formula
  (renders `#NAME?`). Use `═══` Unicode section headers, never ASCII `===`.

Local institution names in local languages (Seguridad Social, IRPF, Nómina) are
**not** residue.

---

## 7. Research integrity — the rules that were earned, not assumed

**Real errors caught only by going to primary source:**

| Country | Fabrication | Truth |
|---|---|---|
| Morocco | "Décret 2-05-2494" | Arrêté n° 346-05 du 9/2/2005 — the decree does not exist |
| Jordan | SSC ceiling JOD 3,000 | JOD 3,733 (2026) — 3,000 matches no year |
| Kuwait | 2.5% on wrong tranche | PIFSS has two different 2.5% funds |
| Côte d'Ivoire | "Contribution Nationale 1.20%" | abolished 2023, merged into ITS |
| Belgium | Annexe 6 codes 007-009 | do not exist; and 412 was missed |
| France | vehicle BIK 9%/6%/30% | 15%/10%/50% (Arrêté 25/2/2025) |

**Web research got the Belgian XML encoding wrong** (suggested ISO-8859-1; it is
UTF-8). Treat "evidence leans toward" as a prompt to verify — never as a value
to configure.

**A downloaded official file beats a search snippet.** When they disagree, the
file wins.

**Distinguish four states — never collapse them into one label:**

| Label | Means |
|---|---|
| a real value | found — cite document + version |
| `NOT LOCATED` | not found *in the sources checked* — list them; state it does NOT mean non-existent |
| `HORS PERIMETRE` / out of scope | belongs elsewhere — say where |
| `N/A` | not applicable at all — say why |

Mislabelling "not researched" as "does not exist" sends nobody looking; the
reverse burns a colleague's day. **A blank field in one document does not mean
the authority never published it** — proven three times in Belgium: zones
00110/00153 blank in DmfA but described in Dimona; zone 00518 described in the
2007/4 edition and dropped by 2026/2; four ESAW zones blank in the NSSO glossary
but defined in the BCSS datawarehouse.

**The compaction trap.** In the Netherlands work, an unverified claim
("PrLnUFO was removed in 2026") was written pre-compaction, inherited
post-compaction, and trusted without re-checking. It could not later be traced
to any source. **Anything inherited from a summary is a claim, not a fact** —
re-verify before acting on it.

**Confirm a mapping before trusting it.** Research inferred the Belgian
zone→ESAW mapping; the glossary's own definition domain then confirmed it by
naming the annexe. Inference became evidence — that step is the difference.

**Audit the whole sheet, not a sample.** Parsing the official glossary and
checking every row gave 179/179 and 138/138 coherent, and proved the original
authors had zero false positives. A sample would have proved nothing.

---

## 8. The failure log (F1–F23+) — recurring patterns

`country_failure_log.md` in `shared/`. Every C-check maps back to an F-entry.
Read it before starting a country. Highest-value entries:

- **F1** option mapper mismatch DD ↔ Specs
- **F2** out-of-scope codes leaking from multi-purpose source PDFs
- **F3** field misclassification (inferred from English source instead of local law)
- **F9** thin spec column schema — agent didn't probe the authority's real validation depth
- **F10** missing sub-forms — source described them in the local language
- **F11** display-only rows treated as XML input
- **F12** composite key construction undocumented
- **F13** mutual exclusion rules undocumented
- **F14** code prefix inferred from examples instead of the full official list
- **F15** artifact dropped between versions with no descoping decision
- **F23** pre-flight PDF size check sums recursively across all stage subfolders
  instead of max-per-subfolder. Mirroring 3 PDFs (~11MB) into 4 folders counted
  44MB and blocked the run. **Workaround: keep PDFs in `ccg-sources` only.**

Append new patterns as they appear — that is what the file is for.

---

## 9. Skill files — the pattern and its failure

**Architecture:** thin router `SKILL.md` (under ~400 lines) + `references/` or
`artifacts/` with one **full, verbatim, non-summarized** file per artifact
(01-ccg … 07-qa-report). Read the latest version present; never hardcode v1.0.
YAML frontmatter required for claude.ai org upload.

**The failure worth remembering:** a Chile skill was delivered and the user's
reaction was blunt — the answers it produced were *thinner* than the previous
version. Two candidate causes: (A) Projects loaded only the router and not the
artifacts folder, or (B) the artifacts were summarized instead of copied
verbatim. **The router pattern only works if the artifacts are genuinely full
content.** A 4 KB router pointing at nothing is worse than one fat file.

Diagnose before defending: check the artifact file sizes. C23 flags any artifact
under 5 KB — that flag is usually a real thin-content problem, not a false positive.

**Agent 9 / Skill Compiler was proposed by Marko (April 2026) but never built
into any pipeline version.** The Chile skill was a manual workflow. Stage 11 in
v2.7+ implements the router pattern. Don't describe Agent 9 as existing.

**Distribution model:** Google Drive stays the single source of truth where
everyone works online simultaneously — no downloading. The skill file is a
knowledge layer on top for Q&A, not a replacement for the artifacts.

---

## 10. Working with Wallisson

- Runs commands exactly as given, pastes results back unfiltered. **Split
  multi-command blocks across separate messages with explicit gating** — he
  sometimes executes only part of a block.
- Re-runs familiar status-check commands when unsure what to do next. That is a
  signal to give the next concrete step, not more analysis.
- Voice-to-text — expect transcription noise in technical terms.
- PT-BR casual; deliverables and ticket replies in English.
- **Verdict first, then reasoning.** Never lead with analysis.
- When frustrated ("this seems unsolvable"), the thing that works is an honest
  status split: infrastructure friction vs. content quality. Each problem in the
  France run had a root cause found and fixed — but each fix revealed the next
  one, and that is exhausting in a single sitting. Say that plainly.
- **Push-back is usually right.** He questioned the "NOT FOUND" labels three
  times in Belgium; each round surfaced a real defect (wrong label, then stale
  statements contradicting the file's own content, then an over-broad claim).
  Treat repeated challenge as signal, not friction.
- Never claim something was sent, done, or verified unless it was.

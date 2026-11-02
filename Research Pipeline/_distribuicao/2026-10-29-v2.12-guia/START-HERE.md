# Research pipeline v2.12 — start here

Two ways to use the method. Pick the one you need.

## A. In claude.ai or Claude Desktop (chat)

Nothing to install. The three skills are now published to the Mercans organisation:

- mercans-pipeline-methodology (v2)
- mercans-compliance-workflow (v3)
- mercans-artifact-toolkit (v1)

1. Go to **Customize → Skills** and check that the three are switched on.
2. If you uploaded older copies yourself, switch those off or delete them, so only the organisation version is active.
3. For the toolkit's scripts, turn on code execution (**Settings → Capabilities**).
4. Test: open a new chat and ask *"What does Stage 9 do in pipeline v2.12, and when may a check be skipped?"* The answer should say that missing country support is a FAIL unless an exemption is recorded.

If mercans-compliance-workflow does not appear for you, tell me and I'll ask an admin to give you access.

## B. Running a country build (Git Bash, as before)

Same way as before: the script runs in Git Bash and calls Claude Code in the background. Everything is in the `code/` folder of this package, including the script `mercans_pipeline_v2_12.sh`, which was missing from the earlier email.

**Step 2 is optional.** The script does not need the plugin; skip to step 3 if you only run builds the usual way. Install the plugin only if you also want the agents and skills inside Claude Code sessions.

**Before you start, you need:**
- Claude Code installed and logged in with your Claude account (`claude` works in a terminal).
- **No** `ANTHROPIC_API_KEY` in your environment. The script stops at once if one is set.
- Git Bash (Windows) and Python 3 with `openpyxl`, `python-docx` and `jsonschema` (`pip install openpyxl python-docx jsonschema`).

**1. Unzip the package** somewhere, e.g. `C:\mercans\v2.12\`. (Only the zip of this package is unzipped. Never unzip the skill zips inside `chat/`.)

**2. (Optional) Install the plugin** (agents and skills). In Claude Code:
```text
/plugin marketplace add C:/mercans/v2.12/code
/plugin install mercans-pipeline@mercans-compliance
```
Restart Claude Code and check with `/plugin` and `/agents`.

**3. Set up the pipeline folder.** In Git Bash:
```bash
cp -r /c/mercans/v2.12/code/mercans-pipeline/pipeline ~/mercans-pipeline
cd ~/mercans-pipeline
```
If you already have a `~/mercans-pipeline` folder from v2.9, rename it first (`mv ~/mercans-pipeline ~/mercans-pipeline-v2.9`) so your old country folders stay safe, then copy them back into the new folder if you want to resume one.

**4. Dry run (prompts only, nothing is built):**
```bash
GENERATE_PROMPTS_ONLY=true bash mercans_pipeline_v2_12.sh "Country" CC CUR 2026 English
```
The first lines must show `Claude CLI: ok` and `All v2.4 reference files present`. Two things are normal here: the banner still says "v2.8" (old label in the script; the file is v2.12), and the dry run ends with `STAGE 13 HALTED ... (C43)`, because nothing was built. Delete the test `CC-compliance/` folder it created before the real run.

**5. Real run:**
```bash
CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000 nohup bash mercans_pipeline_v2_12.sh "Country" CC CUR 2026 English > CC-v212.log 2>&1 &
```
Resume from a stage with `START_STAGE=N`. Long runs: keep the laptop plugged in and stop it from sleeping, or the run dies without an error.

## If it stops

| Message | What to do |
|---|---|
| `ANTHROPIC_API_KEY is set` | `unset ANTHROPIC_API_KEY` and remove it from your environment variables |
| `claude CLI not found in PATH` | install Claude Code, open a new Git Bash |
| `claude CLI test failed` | run `claude` once and log in |
| `Required v2.4 reference file missing` | the pipeline folder was not copied whole; repeat step 3 |
| Stage 9 FAIL on C34/C35/C36/C48/C50/C57/C71 | expected in v2.12 for a country without that support: record `validation_exemptions.<check>` (reason, official source URL, decided_on) in `_pipeline/build-manifest.json`. See `CHANGELOG-v2.12.md` §1 |

Anything else: send me the last 30 lines of the log and I'll look.

Full detail: `INSTALL.md` and `CHANGELOG-v2.12.md` in this package.

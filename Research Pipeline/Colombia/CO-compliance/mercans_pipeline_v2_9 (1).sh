#!/usr/bin/env bash
# =============================================================================
# Mercans Compliance Research Pipeline — v2.8
# =============================================================================
# Full end-to-end pipeline for a new country build. Replaces v2.7.
#
# v2.8 KEY CHANGES vs v2.7 (China CN session — Enaakshi's pipeline controls B1-B10):
#   - STAGE 9 AUDIT extended C28 -> C31 (deterministic, automatic):
#       C29 (B3) residual-marker lint across ALL artifacts: no "[placeholder]",
#           TODO/TBD/FIXME/XXX, "VERIFY No.", "to be confirmed/verified" may survive
#           to final (extends C8 from the CCG to the specs/WTC/DD too). FAIL if found.
#       C30 (B5) source-tier flag: citations to known aggregator/tier-3 domains
#           (51shebao, PwC, China-Briefing, Wikipedia, ...) are flagged MANUAL for
#           replacement by an A.1/A.2 official source.
#       C31 (B1) resident vs non-resident coverage: if a CCG income-tax module has
#           no non-resident treatment, flagged MANUAL (fill from primary law or
#           declare out-of-scope) so empty non-resident handling is never silent.
#   - STAGE 1 CCG prompt: mandatory RESIDENT-vs-NON-RESIDENT matrix (B1) before prose;
#     ONE-CALIBER average-wage rule with derive-and-check (B2); citation-to-article
#     validation + intra-doc consistency (B4); scope decisions logged as
#     in / owned-upstream / inbound-contract / reversible (B7).
#   - STAGE 2 Scope and STAGE 3 Report Specs prompts carry the B1/B4/B7 controls.
#   - B6 (coupled CCG/WTC/DD/workbook) and B8 (zero-error + recalc) remain hard gates
#     from earlier versions; B9 (router skill from finalised artifacts) is STAGE 11;
#     B10 (running CCG-Playbook-Learnings) referenced in pre-flight.
#   NOTE: B4 full semantic claim-validation is an AGENT instruction, not a deterministic
#   gate; the audit enforces only the mechanical subset (marker lint, source tier,
#   non-resident presence).
#
# v2.7 KEY CHANGES vs v2.6 (Chad TD session — eliminate manual re-checks):
#   - STAGE 3 SUBMISSION-FORMAT VERIFICATION (root cause of the biggest manual
#     rework): new STEP 3.5 researches the REAL submission channel per report
#     from official/portal sources and NEVER assumes XML. Default for
#     francophone-Africa / CEMAC is portal-based (online form OR a
#     software-generated upload), NOT machine-to-machine XML.
#       - Sheet 5 (File Structure): neutral FIELD MODEL unless an official XSD
#         is cited — no XML default.
#       - Sheet 9 (Sample File): only with a real/confirmed sample — fabricated
#         XML/CSV samples are now a C-check failure.
#       - Correct portal + URL per institution from shared/country_portal_registry.md
#         (CNPS portal != DGI e-Tax portal).
#   - C4 CORRECTED: filing consolidation (separate vs one consolidated grid) is
#     a RESEARCH question, not a default-to-separate assumption.
#   - STAGE 7 PAYSLIP fixed to OUTPUT the full 8-sheet structure (the old build
#     DELETED "How to set up Payslip", "Compliance Payslip" master and
#     "Field Option" — the root cause of incomplete payslips). Adds explicit
#     formatting tokens, integer currency format for zero-minor-unit currencies
#     (XAF/XOF), and totals-as-formulas-on-total-rows hygiene (Spain quality bar).
#   - STAGE 9 AUDIT extended C1-C22 -> C1-C28:
#       C23 XML-not-applicable (no XML unless XSD cited)
#       C24 portal/institution label correctness (no e-Tax in a CNPS spec, etc.)
#       C25 no fabricated Sample File
#       C26 payslip 8-sheet structure
#       C27 DD<->spec System Mapping resolution (bidirectional)
#       C28 currency minor-unit integer rule
#   - STAGE 11 SKILL now uses the Chile ROUTER pattern: a thin SKILL.md + a
#     references/ folder with one FULL (verbatim, non-summarized) file per
#     artifact (01-ccg .. 07-qa-report). Reads the LATEST artifact version
#     present (no hardcoded v1.0). Replaces the old flat 4-file output.
#   - NEW shared file: country_portal_registry.md (portal/URL/format archetype +
#     analogue library: DISA = per-employee, DSF = aggregate). The payslip base
#     stays the existing 8-sheet REFERENCE_Payslip_Mozambique.xlsx.
#
# v2.6 / v2.5 history retained below.
#
# v2.5 KEY CHANGES vs v2.4 (Egypt feedback — Manju Shetija, 27 May 2026):
#   - PRE-RUN ROBUSTNESS:
#     - Stage resume capability via START_STAGE env var (P1)
#     - Prompt-only generation mode via GENERATE_PROMPTS_ONLY=true (P2)
#     - Per-stage source PDF subfolders: ccg-sources/, spec-sources/,
#       wtc-sources/, dd-sources/ (P3)
#     - PDF folder size pre-flight check, warn >20MB, error >28MB (P4, T3)
#     - sample-files/ folder auto-created (P5)
#     - Stale lockfile auto-clean (>1h old) with warning (P6)
#     - Per-file PDF size warning >5MB, flag scanned PDFs (D2)
#   - TOKEN LIMITS (T1, T2):
#     - CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000 set inline for Stage 3 and Stage 5
#       only (NOT global) — prevents Stage 1 input-bloat side effect
#     - 32MB input limit documented in header (T3)
#   - SCRIPT / PROMPT (S1, S2, S3, S4):
#     - Stage prompt filenames standardised to NN_name.md with matching
#       EOF_NN_NAME delimiters (S1)
#     - No inline comments in user-facing run examples (S2 — zsh-safe)
#     - Scope manifest schema field names included verbatim in CCG prompt (S3)
#     - Recommended run command includes CLAUDE_CODE_MAX_OUTPUT_TOKENS inline (S4)
#   - SCOPE & CONTENT (C1, C2, C3, C4):
#     - CCG prompt instructed to use newest applicable law as primary source,
#       flag any references to superseded laws (C2)
#     - WTC prompt includes post-generation validation checklist against
#       scope_manifest wage types and tax code legend (C3)
#     - HR-scope reports (requiring headcount/qualification/nationality data
#       beyond payroll) flagged for descope from dev handover (C1)
#     - Filing mechanics clarification: monthly, quarterly, annual filings are
#       SEPARATE employer submissions, not auto-generated from each other (C4)
#   - PROCESS (R1, R2, R3):
#     - Per-stage completion summary lines in main log (R1)
#     - Mandatory sample file anonymisation reminder in pre-flight (R2)
#     - country_source_checklist_template.md referenced in pre-flight (R3)
#   - FAILURE LOG: F16-F22 entries appended for new patterns observed in Egypt
#
# v2.4 KEY CHANGES vs v2.3:
#   - Stage 1 CCG: template-driven Q&A format using $SHARED/CCG_TEMPLATE_QUESTIONS.md
#     and $SHARED/REFERENCE_CCG_Bulgaria.docx as gold standard
#   - Stage 7 Payslip: single 5-sheet Mercans-standard workbook (was 2-sheet)
#     using $SHARED/REFERENCE_Payslip_Mozambique.xlsx as template skeleton
#     and $SHARED/mercans_logo.png for branding
#   - Stage 9 Audit: extended from C1-C10 to C1-C22 (12 new checks)
#     - C8 fixed: uses \bTODO\b word-boundary regex (no false positives on
#       Spanish "todo", Portuguese "todo", French "tout", etc.)
#     - C11 CCG template coverage, C12 spec column schema depth,
#       C13 composite key documentation, C14 option mapper completeness,
#       C15 field input/output classification, C16 inter-field constraints,
#       C17 cross-reference table presence, C18 declaration form scope,
#       C19 code prefix verification, C20 scope decision audit trail,
#       C21 payslip 5-sheet structure, C22 payslip spec coverage
#   - Audit content-fixer: now self-aware (overrides false positives with
#     written justification, as proven on Chile v2.4 "todo evento" case)
#
# USAGE:
#   bash mercans_pipeline_v2_8.sh COUNTRY CODE CURRENCY YEAR LANGUAGE
#
# EXAMPLE (fresh full run, with token limit inline — S4):
#   CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000 nohup caffeinate -i bash \
#     ~/mercans-pipeline/mercans_pipeline_v2_8.sh \
#     Chad TD XAF 2026 French \
#     > ~/mercans-pipeline/TD-v25.log 2>&1 & echo $!; disown
#
# RESUME from a specific stage (e.g. Stage 5 failed, restart from there):
#   START_STAGE=5 CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000 \
#     bash ~/mercans-pipeline/mercans_pipeline_v2_8.sh Chad TD XAF 2026 French
#
# PROMPT-ONLY MODE (writes all stage prompts, runs no API calls — for review):
#   GENERATE_PROMPTS_ONLY=true bash ~/mercans-pipeline/mercans_pipeline_v2_8.sh \
#     Chad TD XAF 2026 French
#
# NOTE on zsh — do NOT include inline '#' comments when pasting multi-line
# commands into the terminal. zsh treats them as commands and fails. Either:
#   (a) paste lines without comments, OR
#   (b) save the command to a .sh file and run that file.
#
# PRE-REQUISITES:
#   - ~/mercans-pipeline/shared/ has the v2.5 reference files:
#       CCG_TEMPLATE_QUESTIONS.md (existing)
#       REFERENCE_CCG_Bulgaria.docx (v2.4+)
#       REFERENCE_Payslip_Tunisia.xlsx (v2.4+)
#       REFERENCE_Payslip_Mozambique.xlsx (v2.4+)
#       mercans_logo.png
#       country_failure_log.md (v2.5 with F16-F22)
#       PRESUBMISSION_AUDIT.md (v2.5)
#       country_source_checklist_template.md (NEW v2.5 — R3)
#       ZSH_AND_ENV_NOTES.md (NEW v2.5 — S2, S4)
#     PLUS the existing reference files:
#       CZ_Data_Dictionary_V2_0.xlsx, Global_WTC_V1_0.xlsx,
#       _CZ_Wage_Type_Catalogue_V2_0.xlsx, scope_manifest_template.json,
#       report-spec-template/
#   - Source PDFs placed under ~/mercans-pipeline/${CODE}-compliance/00-official-sources/
#     in per-stage subfolders (auto-created by pre-flight — P3):
#       pdfs/              — generic / shared across stages
#       ccg-sources/       — labour law, tax law, SS law, leave rules (Stage 1)
#       spec-sources/      — form PDFs and fill-in guides for statutory reports (Stage 3)
#       wtc-sources/       — allowance/benefit valuation rules (Stage 5)
#       dd-sources/        — identification, master-data, format-rule sources (Stage 4)
#       sample-files/      — anonymised sample submissions (Stage 3)
#   - INPUT SIZE LIMIT (T3): Claude CLI accepts max ~32MB per request.
#       Pre-flight warns at 20MB total PDFs, errors at 28MB.
#       Per-file warning >5MB (scanned PDFs are common offenders — D2).
#   - Claude CLI installed (claude -p ...) — Max OAuth, no ANTHROPIC_API_KEY set
#   - Word/Excel closed (lockfiles >1h old are auto-cleaned by pre-flight — P6)
#
# TYPICAL RUNTIME: ~5-6 hours wall-clock (varies with country complexity)
#   Stage 1  CCG:               45-90 min
#   Stage 2  Scope Lock-In:     2-5 min
#   Stage 3  Report Specs:      60-120 min
#   Stage 4  DD:                25-35 min
#   Stage 5  WTC:               30-50 min
#   Stage 6  SIR:               15-30 min
#   Stage 7  Payslip:           25-40 min
#   Stage 8  Alignment Patch:   20-30 min
#   Stage 9  Audit + Fixer:     20-40 min
#   Stage 10 QA Cross-check:    15-25 min
#   Stage 11 Skill Generator:    20-40 min
#
# OUTPUTS:
#   01-ccg/${CODE}-CCG-001-v1.0.docx
#   02-wtc/${CODE}-WTC-001-v1.0.xlsx
#   03-statutory-integrations/${CODE}-SIR-INDEX-001-v1.0.docx  (light index; runbooks per-authority via si-runbook)
#   04-reports-spec/${CODE}-*-Spec.xlsx  (N specs depending on country)
#   05-data-dictionary/${CODE}-DD-001-v1.0.xlsx
#   06-payslip/${CODE}_Compliance_Payslip_Generator.xlsx  (8-sheet)
#   07-qa-crosscheck/handover_status.md  + ${CODE}-QA-REPORT.md
#   08-skill/${CODE_LC}-compliance/  (router skill: SKILL.md + references/01-ccg..07-qa-report.md)
#   scope_manifest.json
# =============================================================================
set -e
set -o pipefail

# ----- Argument parsing ---------------------------------------------------
if [ "$#" -ne 5 ]; then
    echo "Usage: $0 COUNTRY CODE CURRENCY YEAR LANGUAGE"
    echo "Example: $0 Pakistan PK PKR 2026 English"
    exit 1
fi

COUNTRY="$1"
CODE="$2"
CURRENCY="$3"
YEAR="$4"
LANGUAGE="$5"

# v2.7 — lowercase CODE for paths (bash 3.2 safe; macOS default bash has no in-place lowercase operator)
CODE_LC=$(echo "$CODE" | tr '[:upper:]' '[:lower:]')

# v2.7 — pipeline start time (set unconditionally so runtime is correct when resuming via START_STAGE)
PIPELINE_START=$(date +%s)

# v2.6 — Stage control via env vars (P1, P2)
START_STAGE="${START_STAGE:-1}"
GENERATE_PROMPTS_ONLY="${GENERATE_PROMPTS_ONLY:-false}"

if ! [[ "$START_STAGE" =~ ^[0-9]+$ ]] || [ "$START_STAGE" -lt 1 ] || [ "$START_STAGE" -gt 11 ]; then
    echo "ERROR: START_STAGE must be an integer between 1 and 11 (got: $START_STAGE)"
    exit 1
fi

# Local-language sheet suffix (used in payslip sheet naming)
case "$LANGUAGE" in
    Spanish) LOCAL_LANG_SHORT="ES" ;;
    Portuguese) LOCAL_LANG_SHORT="PT" ;;
    French) LOCAL_LANG_SHORT="FR" ;;
    German) LOCAL_LANG_SHORT="DE" ;;
    Italian) LOCAL_LANG_SHORT="IT" ;;
    Dutch) LOCAL_LANG_SHORT="NL" ;;
    Hungarian) LOCAL_LANG_SHORT="HU" ;;
    Bulgarian) LOCAL_LANG_SHORT="BG" ;;
    Arabic) LOCAL_LANG_SHORT="AR" ;;
    Urdu) LOCAL_LANG_SHORT="UR" ;;
    English) LOCAL_LANG_SHORT="EN" ;;
    *) LOCAL_LANG_SHORT=$(echo "$LANGUAGE" | cut -c1-2 | tr 'a-z' 'A-Z') ;;
esac

PIPELINE="$HOME/mercans-pipeline"
SHARED="$PIPELINE/shared"
BASE="$PIPELINE/${CODE}-compliance"
PROMPTS="$BASE/_prompts"
LOGS="$BASE/logs"

echo "================================================================"
echo "Mercans Compliance Research Pipeline — v2.8"
echo "Country: $COUNTRY ($CODE)  |  Currency: $CURRENCY  |  Year: $YEAR"
echo "Language: $LANGUAGE  |  Local sheet suffix: $LOCAL_LANG_SHORT"
echo "Pipeline: $PIPELINE"
echo "Start stage: $START_STAGE  |  Prompts-only mode: $GENERATE_PROMPTS_ONLY"
echo "Started: $(date '+%Y-%m-%d %H:%M:%S')"
echo "================================================================"
echo ""

# ----- Pre-flight checks --------------------------------------------------
echo "[Pre-flight] Verifying environment..."

if [ -n "$ANTHROPIC_API_KEY" ]; then
    echo "ERROR: ANTHROPIC_API_KEY is set — this breaks Max OAuth. Unset it."
    echo "  Run: unset ANTHROPIC_API_KEY"
    exit 1
fi

if ! command -v claude >/dev/null 2>&1; then
    echo "ERROR: claude CLI not found in PATH"
    exit 1
fi

claude_test=$(claude -p "say ok" --max-turns 1 2>&1 || true)
if [[ "$claude_test" != *"ok"* ]] && [[ "$claude_test" != *"OK"* ]] && [[ "$claude_test" != *"Ok"* ]]; then
    echo "ERROR: claude CLI test failed. Output was:"
    echo "$claude_test"
    exit 1
fi
echo "  Claude CLI: ok"

# Verify all required shared/ files
REQUIRED_SHARED=(
    "CCG_TEMPLATE_QUESTIONS.md"
    "REFERENCE_CCG_Bulgaria.docx"
    "REFERENCE_Payslip_Tunisia.xlsx"
    "REFERENCE_Payslip_Mozambique.xlsx"
    "mercans_logo.png"
    "country_failure_log.md"
    "PRESUBMISSION_AUDIT.md"
    "CZ_Data_Dictionary_V2_0.xlsx"
    "Global_WTC_V1_0.xlsx"
    "_CZ_Wage_Type_Catalogue_V2_0.xlsx"
    "scope_manifest_template.json"
)

for ref in "${REQUIRED_SHARED[@]}"; do
    if [ ! -f "$SHARED/$ref" ]; then
        echo "ERROR: Required v2.4 reference file missing: $SHARED/$ref"
        echo "  See script header for setup requirements."
        exit 1
    fi
done
echo "  All v2.4 reference files present in $SHARED"

# v2.7 — optional references (warn if missing, do NOT block the run)
# v2.8 — added CCG-Playbook-Learnings.md (B10): accumulated cross-country controls
for ref in "country_portal_registry.md" "CCG-Playbook-Learnings.md"; do
    if [ ! -f "$SHARED/$ref" ]; then
        echo "  WARN: optional reference missing: $SHARED/$ref"
    else
        echo "  optional reference present: $ref"
    fi
done

# v2.5 — Create directory structure FIRST so subsequent checks have a real $BASE
# (P3, P5) including per-stage source subfolders
mkdir -p "$BASE"/{01-ccg,02-wtc,03-statutory-integrations,04-reports-spec,05-data-dictionary,06-payslip,07-qa-crosscheck}
mkdir -p "$BASE"/00-official-sources/{pdfs,ccg-sources,spec-sources,wtc-sources,dd-sources,sample-files}
mkdir -p "$PROMPTS" "$LOGS"

# v2.5 — Lockfile auto-clean (P6): delete stale lockfiles >1h old, error on fresh ones
# Order matters: mkdir must run BEFORE this find, or set -e exits on a missing $BASE
lockfiles=$(find "$BASE" -name '~\$*' 2>/dev/null || true)
if [ -n "$lockfiles" ]; then
    fresh=$(find "$BASE" -name '~\$*' -mmin -60 2>/dev/null || true)
    stale=$(find "$BASE" -name '~\$*' -mmin +60 2>/dev/null || true)
    if [ -n "$stale" ]; then
        echo "  WARN: Auto-cleaning stale lockfiles (>1h old):"
        echo "$stale" | sed 's/^/        /'
        find "$BASE" -name '~\$*' -mmin +60 -delete 2>/dev/null || true
    fi
    if [ -n "$fresh" ]; then
        echo "ERROR: Found fresh Word/Excel lockfile(s) (<1h old) in $BASE"
        echo "  Close any open .docx/.xlsx files before continuing:"
        echo "$fresh" | sed 's/^/        /'
        exit 1
    fi
fi
echo "  No active Word/Excel lockfiles"

# v2.5 — PDF inventory + size checks (P4, T3, D2)
echo "[Pre-flight] Checking source PDF inventory and sizes..."
pdf_count=$(find "$BASE/00-official-sources" -name "*.pdf" 2>/dev/null | wc -l | tr -d ' ')
if [ "$pdf_count" -eq 0 ]; then
    echo "  NOTE: No source PDFs found under $BASE/00-official-sources/"
    echo "        Pipeline will rely on web research only. Quality may be lower."
    echo "        See: $SHARED/country_source_checklist_template.md (R3) for guidance"
    echo "        on which official documents to download for each country."
else
    echo "  Found $pdf_count source PDFs across 00-official-sources/ subfolders"
    # v2.6 FIX F23 — check per-subfolder max, not total recursive sum
    # Each stage loads only its own subfolder so the 28MB limit applies per-subfolder
    preflight_ok=true
    for subdir in ccg-sources spec-sources wtc-sources dd-sources sample-files; do
        sub_path="$BASE/00-official-sources/$subdir"
        if [ -d "$sub_path" ]; then
            sub_bytes=$(find "$sub_path" -name "*.pdf" -exec stat -f%z {} \; 2>/dev/null | awk '{s+=$1} END {print s+0}')
            sub_mb=$((sub_bytes / 1024 / 1024))
            if [ "$sub_mb" -gt 28 ]; then
                echo "ERROR: $subdir PDFs total ${sub_mb}MB exceeds the 28MB safety threshold"
                echo "  Reduce by converting scanned PDFs to text-based versions."
                echo "  Largest files in $subdir:"
                find "$sub_path" -name "*.pdf" -exec stat -f"%z %N" {} \; 2>/dev/null | sort -nr | head -5 | awk '{ printf "    %.1fMB  %s\n", $1/1024/1024, $2 }'
                preflight_ok=false
            elif [ "$sub_mb" -gt 20 ]; then
                echo "  WARN: $subdir PDFs total ${sub_mb}MB — approaching 28MB limit."
            fi
        fi
    done
    total_bytes=$(find "$BASE/00-official-sources" -name "*.pdf" -exec stat -f%z {} \; 2>/dev/null | awk '{s+=$1} END {print s+0}')
    total_mb=$((total_bytes / 1024 / 1024))
    echo "  Total source PDF size: ${total_mb}MB (per-subfolder check — v2.6 F23 fix)"
    if [ "$preflight_ok" = false ]; then
        exit 1
    fi
    # Per-file size warning (D2)
    large=$(find "$BASE/00-official-sources" -name "*.pdf" -size +5M 2>/dev/null || true)
    if [ -n "$large" ]; then
        echo "  WARN: PDFs larger than 5MB (often scanned — text extraction may be poor):"
        echo "$large" | while read f; do
            sz=$(stat -f%z "$f" 2>/dev/null || echo 0)
            echo "$f" | awk -v s="$sz" '{ printf "        %.1fMB  %s\n", s/1024/1024, $0 }'
        done
        echo "        Check whether text-based versions are available from the source."
    fi
fi
echo ""

# v2.5 — Anonymisation reminder for sample files (R2)
sample_files=$(find "$BASE/00-official-sources/sample-files" -type f 2>/dev/null | wc -l | tr -d ' ')
if [ "$sample_files" -gt 0 ]; then
    echo "[Pre-flight] REMINDER: $sample_files file(s) in sample-files/"
    echo "  Verify all real company names, employee IDs, and national IDs are"
    echo "  anonymised before pipeline ingestion (R2)."
    echo ""
fi

# =============================================================================
# v2.5 — STAGE CONTROL HELPERS (P1, P2, R1)
# =============================================================================
# These helpers implement:
#   P1: stage resume — skip stages below $START_STAGE
#   P2: prompt-only mode — write prompt files but skip claude -p execution
#   R1: per-stage completion summary lines

stage_skip_check() {
    local n=$1
    local name=$2
    if [ "$START_STAGE" -gt "$n" ]; then
        echo "----------------------------------------------------------------"
        echo "STAGE $n/10 — $name [SKIPPED — START_STAGE=$START_STAGE]"
        echo "----------------------------------------------------------------"
        echo ""
        return 1
    fi
    return 0
}

run_claude_or_skip() {
    # Args: prompt_file, log_file, max_turns
    local prompt_file=$1
    local log_file=$2
    local max_turns=$3
    if [ "$GENERATE_PROMPTS_ONLY" = "true" ]; then
        echo "  [PROMPTS-ONLY mode] Prompt written to $prompt_file — execution skipped"
        return 0
    fi
    claude -p "$(cat "$prompt_file")" \
           --max-turns "$max_turns" \
           --dangerously-skip-permissions \
           > "$log_file" 2>&1
}

# =============================================================================
# STAGE 1 — CCG (v2.5 template-driven Q&A format, C2 newest-law instruction)
# =============================================================================
if stage_skip_check 1 "CCG"; then
echo "----------------------------------------------------------------"
echo "STAGE 1/11 — CCG (template-driven Q&A format, v2.5)"
echo "Est. 45-90 min"
echo "----------------------------------------------------------------"

cat > "$PROMPTS/ccg.md" << CCGEOF
# ${COUNTRY} COUNTRY CONFIGURATION GUIDE — v2.4 TEMPLATE FORMAT

You are building the ${COUNTRY} Country Configuration Guide using the OFFICIAL
Mercans CCG template. The output MUST follow the template's question-by-question
structure exactly, with every question appearing as an H3 heading and the answer
immediately below.

## CRITICAL — v2.4 FORMAT REQUIREMENTS

The Mercans CCG template has 13 Modules with sub-sections (1.1, 1.2, ...) and
approximately 96-150 specific questions. Each question MUST appear in your output
as an \`### H3 heading\` with the answer below.

This is a HARD requirement. The downstream auditor (Check C11) will count H3
headings against the template question list and FAIL the build if coverage is
below 95%.

## MANDATORY INPUTS

### v2.5 — USE THE NEWEST APPLICABLE LAW AS PRIMARY SOURCE (C2)

When researching ${COUNTRY} payroll rules, you MUST:
1. Identify the CURRENT labour code / income tax law / social security law in force
   for ${YEAR} (often this is a NEW law that has replaced an older one — e.g.,
   Egypt Labour Law 14/2025 replaced the old Law 12/2003).
2. Use the newest law as your primary source for: leave entitlements (maternity,
   annual, sick), severance, working hours, overtime rates, minimum wage.
3. EXPLICITLY FLAG any reference to a superseded/replaced law in your output.
   If a source PDF or web result cites the old law, do NOT use those values.
4. When in doubt, search: "${COUNTRY} new labour code ${YEAR}" /
   "${COUNTRY} labour law amendments ${YEAR}".
5. Filing mechanics (C4 — v2.7 CORRECTED): do NOT assume filings are separate.
   Whether wage taxes file as SEPARATE submissions or as ONE CONSOLIDATED grid
   is a research question — some portal/CEMAC regimes consolidate all salary
   taxes on a single monthly retenues grid (e.g. Cameroon DGI), others keep them
   separate. Determine the real answer for ${COUNTRY} from the official portal /
   primary source and document it (with the source). Model accordingly.

### Failure pattern reference

This run must avoid F1-F22 documented in country_failure_log.md.
F16-F22 are Egypt failures (May 2026); pay particular attention to:
- F18: stale law references (use Law 14/2025 not Law 12/2003 type errors)
- F19: HR-scope reports incorrectly included (descope reports needing
       headcount-by-qualification or nationality data — flag as HR scope, C1)
- F20: WTC tax codes not from the country's defined legend (C3)
- F21: Annual/quarterly/monthly filing mechanics misunderstood (C4)

### Standard inputs

1. **Master template (read first, end-to-end):**
   ~/mercans-pipeline/shared/CCG_TEMPLATE_QUESTIONS.md
   This is the master list of all questions across 13 Modules. Every question
   here MUST appear as an H3 heading in your output.

2. **Gold standard reference (study before drafting):**
   ~/mercans-pipeline/shared/REFERENCE_CCG_Bulgaria.docx
   Bulgaria CCG follows the template format exactly. Use it as your structural
   model. Open it with python-docx, study how questions become H3 headings, how
   tables are used for quantitative data, how legal citations are placed.

3. **Failure prevention log:**
   ~/mercans-pipeline/shared/country_failure_log.md
   Read F1-F15. Specifically prevent F9 (thin schemas), F10 (missing sub-forms),
   F15 (artifact removal without descoping decision).

4. **Source PDFs (if available):**
   ~/mercans-pipeline/${CODE}-compliance/00-official-sources/pdfs/
   Use pdfplumber to extract. Cite the specific article/section in your answers.

## 13 MODULES (do NOT merge, rename, split, or reorder)

- Module 1: Foundational Jurisdictional Parameters
- Module 2: Master Data Configuration
- Module 3: The Gross-to-Net Calculation Framework
- Module 4: Gross Compensation
- Module 5: Social Security & Pension Systems
- Module 6: Income Tax Withholding System
- Module 7: Deductions, Exemptions & Benefits
- Module 8: Statutory Leave Management
- Module 9: Termination & Irregular Payments
- Module 10: Reporting, Compliance & Finalisation
- Module 11: Advanced Scenarios & Cross-Cutting Logic
- Module 12: Gross-to-Net Worked Examples
- Module 13: Common Business Practices & Non-Statutory Rules

## STRUCTURE — mirror Bulgaria exactly

\`\`\`
# Module 1: Foundational Jurisdictional Parameters

## 1.1 Fiscal, Currency, and Language

### What is the statutory tax year?

[Plain-prose answer with citation, e.g., "The statutory tax year in ${COUNTRY}
runs from 1 January to 31 December (Income Tax Act Art. X)."]

### Can employers adopt an alternate tax year?

[Answer.]

### What is the official currency for payroll processing and reporting? Provide ISO code.

[Answer with ${CURRENCY} as the ISO code and any relevant detail.]

[... continues for every question in the template ...]

*Legal basis: [List the laws/articles cited in this sub-section]*

## 1.2 Pay Cycles and Dates
[Same pattern.]
\`\`\`

## RULES

1. **Use the question text verbatim** as the H3 heading. Do NOT paraphrase. If
   the template says "What is the statutory tax year?", use that exact text.

2. **Answer every question.** If genuinely not applicable to ${COUNTRY}, write
   "Not Applicable — [brief reason in 1-2 sentences]."

3. **Tables for quantitative data.** Tax brackets, SS rates, ceilings, thresholds
   must be tabular. No long bullet lists for numerical data.

4. **Cite sources.** Every rate, threshold, or rule must have a citation either
   inline or in the legal basis block at the end of each sub-section.

5. **Worked examples in Modules 3-9, 11-13** must be step-by-step with every
   line of calculation shown using actual ${YEAR} numbers in ${CURRENCY}.

6. **Dev-team filtering rules:**
   - Module 2: concise field summaries + reference to DD. Do NOT reproduce DD
     field tables.
   - Module 10: summary table + reference to Report Specs. Do NOT reproduce
     field-level spec content.
   - Module 1.4 (Holidays): simple date table only. No admin workflows.

7. **Plain business language, not jargon.**
   WRONG: "Contributions at rate X% BASE_SS_ER applied to MIN_INS_INCOME-capped earnings."
   RIGHT: "Employer SS is X% of insurable earnings capped at [max] for ${YEAR}.
           Example: an employee earning [amount] pays [result]."

## SCOPE MANIFEST — REQUIRED OUTPUT (S3 v2.5)

After completing the CCG body, produce \`scope_manifest.json\` at:
~/mercans-pipeline/${CODE}-compliance/scope_manifest.json

Load and follow this template EXACTLY:
~/mercans-pipeline/shared/scope_manifest_template.json

CRITICAL — use the EXACT field names from the template (S3 fix):
- For descoped filings: use \`"descoping_reason"\` (NOT "reason")
- For \`integrations.inbound\`: use an ARRAY of OBJECTS, NOT a plain string
  Example: \`"inbound": [{"id": "X", "from": "Y", "format": "Z"}]\`
  NOT: \`"inbound": "X"\`
- For \`product_mapping_required\`: must be \`true\` or \`false\` (boolean),
  not the string "true"/"false" and not null.
- For HR-scope reports requiring headcount/qualification/nationality data
  beyond payroll (C1): include in \`authority_filings.out_of_scope\` with
  \`"descoping_reason": "HR-scope — requires data beyond payroll system"\`
  and \`"client_impact": "Refer to HRMS team"\`. Do NOT include such reports
  in \`in_scope\`.

Use this exact structure:

\`\`\`json
{
  "country": "${COUNTRY}",
  "code": "${CODE}",
  "currency": "${CURRENCY}",
  "year": "${YEAR}",
  "generated": "<ISO datetime>",
  "employment_types": {
    "in_scope": [<list>],
    "out_of_scope": [<list>],
    "rationale": "<reasoning>"
  },
  "authority_filings": {
    "in_scope": [
      {
        "filing_id": "<id>",
        "authority": "<name>",
        "frequency": "<monthly/annual/etc>",
        "format": "<XML/CSV/TXT/XLSX>",
        "integration_type": "<inbound/outbound/both>",
        "product_mapping_required": <true/false with rationale>
      }
    ],
    "out_of_scope": [
      {"filing_id": "<id>", "descoping_reason": "<reason>", "client_impact": "<assessment>"}
    ]
  },
  "wage_type_categories": {<in_scope/out_of_scope buckets>},
  "option_mapper_scope": {<in_scope/out_of_scope codes per mapper>},
  "integrations": {
    "outbound": [<list>],
    "inbound": [<list>],
    "both": [<list>]
  },
  "known_failure_patterns_to_check": ["F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","F13","F14","F15","F16","F17","F18","F19","F20","F21","F22"]
}
\`\`\`

## SOURCES (read in priority order)

1. Source PDFs (if any): ~/mercans-pipeline/${CODE}-compliance/00-official-sources/pdfs/
2. Web research: "${COUNTRY} income tax ${YEAR}", "${COUNTRY} social security ${YEAR}",
   "${COUNTRY} payroll regulations ${YEAR}", "${COUNTRY} labor code ${YEAR}"
3. Government sources only (tax authority, social security, labor ministry,
   official gazette). Avoid blogs, accounting firm marketing pages.

## BUILD APPROACH

1. Read CCG_TEMPLATE_QUESTIONS.md end-to-end. Count the questions per module.
2. Read REFERENCE_CCG_Bulgaria.docx via python-docx, study the structure.
3. For each Module, draft answers to every question. Save as 13 markdown files:
   ~/mercans-pipeline/${CODE}-compliance/01-ccg/modules/m01_foundational.md
   m02_master_data.md, m03_g2n.md, m04_compensation.md, m05_social_security.md,
   m06_tax.md, m07_deductions.md, m08_leave.md, m09_termination.md,
   m10_reporting.md, m11_advanced.md, m12_examples.md, m13_practices.md
4. Assemble the 13 modules into a single Word document using python-docx:
   - Arial 11pt body, 14pt H1, 12pt H2, 11pt H3 (bold)
   - Title page: "${COUNTRY} Country Configuration Guide — ${CODE}-CCG-001 v1.0"
   - TOC on page 2 (use docx TOC field)
   - Page breaks between Modules
   - Footer: "${CODE}-CCG-001 v1.0 | Mercans Compliance Regulations Team | ${YEAR}"
   - Save as: ~/mercans-pipeline/${CODE}-compliance/01-ccg/${CODE}-CCG-001-v1.0.docx

## SELF-CHECK BEFORE SAVING

\`\`\`python
from docx import Document
doc = Document('/Users/wallissongomes/mercans-pipeline/${CODE}-compliance/01-ccg/${CODE}-CCG-001-v1.0.docx')
h3s = [p.text for p in doc.paragraphs if p.style.name in ('Heading 3', 'Heading3')]
print(f"H3 count: {len(h3s)}")
# Expected: 90+ (matches template question count). If < 90, you've missed questions.
\`\`\`

If H3 count is below 90, re-read CCG_TEMPLATE_QUESTIONS.md and add the missing
H3 headings before saving the final docx.

## REPORT BACK

When complete, report:
- H3 heading count
- Any questions marked "Not Applicable" with their reasons
- scope_manifest.json location confirmed
- Final docx size

=== v2.8 CROSS-CUTTING RESEARCH CONTROLS (Enaakshi B1/B2/B4/B7 — mandatory) ===
B1 RESIDENT vs NON-RESIDENT MATRIX: in the income-tax module, BEFORE writing prose,
   build a table with one row per income type (regular salary, annual/13th bonus,
   severance, equity / share incentives, labour-service or contractor pay, benefits in
   kind) and TWO explicit columns — RESIDENT and NON-RESIDENT — giving the rate, method
   and base for each. An empty non-resident cell is a BLOCKING gap, not an omission:
   fill it from primary law, or write "non-resident: not in scope" with the reason. The
   audit (C31) checks a non-resident treatment is present.
B2 ONE-CALIBER WAGE RULE: if any social-security ceiling, floor or cap derives from a
   published "average wage", list EVERY average-wage figure the country publishes and
   name its caliber (e.g. full-caliber vs on-post-staff vs employed-persons). For every
   parameter that depends on it (SI ceiling, housing/HPF ceiling, severance cap) declare
   which caliber it uses, then reconcile. Where a ceiling can be reproduced from a wage
   figure (e.g. ceiling = 3 x average wage / 12), record that derivation as the proof of
   caliber. Never mix calibers across sections.
B4 CITATION-TO-ARTICLE VALIDATION: every cited statute article must actually say what the
   sentence claims; if the same statute is cited in two places for the same rule, the
   article numbers MUST agree. Build the fetched statute article map once and self-check
   before finalising.
B7 SCOPE DECISIONS ARE FIRST-CLASS AND REVERSIBLE: for every in / out-of-scope call,
   record (a) what is in, (b) what is explicitly owned upstream (plan administrator,
   client, authority), (c) the inbound data contract it implies (which fields the engine
   must receive), so a later reversal is a contained edit, not a four-file hunt.
B10 ENGLISH-ONLY PROSE (CCG): the ENTIRE narrative of this CCG must be written in
   English. Every heading, sentence, table cell, worked example, note and caption is
   English. This is a reader-facing compliance document for a global audience — no
   passages, phrases or stray words in ${LANGUAGE} (or any non-English language) may
   appear in the prose. The ONLY permitted non-English text is a statutory/legal term
   of art cited for traceability, and it MUST be handled as: English wording first,
   with the original term immediately after in parentheses on FIRST use only, e.g.
   "professional expenses (frais professionnels)", "the employer wage tax (Taxe
   Forfaitaire Employeur, TFE)". After first use, use the English term (or the
   established abbreviation) alone. Do NOT drop into ${LANGUAGE} for a whole sentence,
   bullet, or table cell. Names of authorities/forms/statutes may keep their official
   proper name (e.g. "Direction Générale des Impôts (DGI)") — that is a proper noun,
   not prose. NOTE: this English-only rule applies to the CCG's PROSE only; it does NOT
   apply to the DD, WTC or Payslip, which carry DEDICATED local-language fields/sheets
   by design (Name Local (${LANGUAGE}) columns, the "${COUNTRY} (${LOCAL_LANG_SHORT})"
   payslip sheet) — those local-language fields are correct and required.
=== end v2.8 controls ===
CCGEOF

echo "  Prompt written: $PROMPTS/ccg.md"
STAGE1_START=$(date +%s)
if [ "$GENERATE_PROMPTS_ONLY" = "true" ]; then
    echo "  [PROMPTS-ONLY mode] Skipping CCG execution"
else
    echo "  Running CCG agent..."
    run_claude_or_skip "$PROMPTS/ccg.md" "$LOGS/ccg.log" 100
fi
STAGE1_END=$(date +%s)
STAGE1_DURATION=$((STAGE1_END - STAGE1_START))
echo "  CCG done in ${STAGE1_DURATION}s ($((STAGE1_DURATION / 60)) min)"
# v2.5 R1 — stage completion summary
if [ -f "$BASE/01-ccg/${CODE}-CCG-001-v1.0.docx" ]; then
    ccg_size=$(stat -f%z "$BASE/01-ccg/${CODE}-CCG-001-v1.0.docx" 2>/dev/null || echo "?")
    echo "  STAGE 1 SUMMARY: CCG docx produced (${ccg_size} bytes), scope_manifest written"
fi
echo ""

if [ "$GENERATE_PROMPTS_ONLY" != "true" ] && [ ! -f "$BASE/01-ccg/${CODE}-CCG-001-v1.0.docx" ]; then
    echo "ERROR: Expected output not produced: ${CODE}-CCG-001-v1.0.docx"
    echo "  Check log: $LOGS/ccg.log"
    exit 1
fi
fi  # end stage_skip_check 1
# =============================================================================
# STAGE 2 — Scope Lock-In Validation (BLOCKING)
# =============================================================================
if stage_skip_check 2 "Scope Lock-In"; then
echo "----------------------------------------------------------------"
echo "STAGE 2/11 — Scope Lock-In Validation (BLOCKING)"
echo "Est. 2-5 min"
echo "----------------------------------------------------------------"

cat > "$PROMPTS/scope_validate.md" << SCOPEEOF
# ${COUNTRY} SCOPE LOCK-IN VALIDATION

You are validating the scope_manifest.json produced by the CCG agent.
This is a BLOCKING gate. The pipeline cannot continue unless validation passes.

## READ
1. Manifest: ~/mercans-pipeline/${CODE}-compliance/scope_manifest.json
2. Schema:   ~/mercans-pipeline/shared/scope_manifest_template.json

## VALIDATE

Check 1 — file exists and is valid JSON.

Check 2 — every required section is present and non-empty:
  - employment_types (in_scope, out_of_scope, rationale)
  - authority_filings (in_scope with all required fields, out_of_scope with reasons)
  - wage_type_categories
  - option_mapper_scope
  - integrations (outbound, inbound, both)

Check 3 — every authority_filings.in_scope entry has:
  - filing_id, authority, frequency, format
  - integration_type (must be one of: inbound, outbound, both)
  - product_mapping_required (must be true or false, not null)

Check 4 — every integrations.inbound entry has product_mapping_required set.
WARN if any inbound integration has product_mapping_required=false (F8 risk).

Check 5 — no code appears in both in_scope and out_of_scope for the same mapper.

Check 6 — known_failure_patterns_to_check is populated with F1-F15.

## OUTPUT
Print PASS or FAIL: <reason> as the FINAL LINE of your response.
If FAIL, list every problem found.
Save full report to: ~/mercans-pipeline/${CODE}-compliance/07-qa-crosscheck/scope_validation.md

v2.8 (B7): in scope_validation.md, record EACH scope decision as a row —
DECISION | IN-SCOPE | OWNED-UPSTREAM | INBOUND-DATA-CONTRACT | REVERSIBLE(Y/N) | BASIS.
For any covered income type, missing non-resident handling is a blocking finding (B1).
SCOPEEOF

if [ "$GENERATE_PROMPTS_ONLY" = "true" ]; then
    echo "  Prompt written: $PROMPTS/scope_validate.md"
    echo "  [PROMPTS-ONLY mode] Skipping scope validation execution"
    STAGE2_DURATION=0
else
    if [ ! -f "$BASE/scope_manifest.json" ]; then
        echo ""
        echo "==========================================="
        echo "  PIPELINE HALTED — SCOPE MANIFEST MISSING"
        echo "==========================================="
        echo "  CCG agent did not produce scope_manifest.json."
        echo "  Re-run CCG stage (CCG prompt may need adjustment)."
        exit 1
    fi

    STAGE2_START=$(date +%s)
    claude -p "$(cat "$PROMPTS/scope_validate.md")" \
           --max-turns 15 \
           --dangerously-skip-permissions \
           > "$LOGS/scope_validation.log" 2>&1
    STAGE2_END=$(date +%s)
    STAGE2_DURATION=$((STAGE2_END - STAGE2_START))

    if grep -q "^FAIL" "$LOGS/scope_validation.log"; then
        echo ""
        echo "==========================================="
        echo "  PIPELINE HALTED — SCOPE VALIDATION FAILED"
        echo "==========================================="
        echo "  See: $LOGS/scope_validation.log"
        echo "  Fix the manifest and re-run from this stage."
        exit 1
    fi
fi
echo "  Scope manifest validated in ${STAGE2_DURATION}s — locked for downstream agents"
# v2.5 R1 — stage completion summary
if [ -f "$BASE/scope_manifest.json" ]; then
    in_scope_count=$(python3 -c "import json; m=json.load(open('$BASE/scope_manifest.json')); print(len(m.get('authority_filings',{}).get('in_scope',[])))" 2>/dev/null || echo "?")
    out_scope_count=$(python3 -c "import json; m=json.load(open('$BASE/scope_manifest.json')); print(len(m.get('authority_filings',{}).get('out_of_scope',[])))" 2>/dev/null || echo "?")
    echo "  STAGE 2 SUMMARY: $in_scope_count in-scope filings, $out_scope_count descoped"
fi
echo ""
fi  # end stage_skip_check 2

# =============================================================================
# STAGE 3 — Report Specs (Spain 9-sheet standard) — v2.5 T1+T2: scoped tokens
# =============================================================================
# =============================================================================
if stage_skip_check 3 "Report Specs"; then
echo "----------------------------------------------------------------"
echo "STAGE 3/11 — Report Specs (Spain 9-sheet, 21-col Sheet 4) — v2.5 T1/T2"
echo "Est. 60-120 min  |  CLAUDE_CODE_MAX_OUTPUT_TOKENS scoped to 64000 for this stage"
echo "----------------------------------------------------------------"

cat > "$PROMPTS/reports.md" << REPORTSEOF
# ${COUNTRY} STATUTORY REPORT SPECIFICATIONS — SPAIN 9-SHEET STANDARD

Build field-level report specs for every statutory report filed by ${COUNTRY}
employers. Each report MUST follow the Spain 9-sheet standard format exactly.

## CRITICAL — v2.4 REQUIREMENTS

This is a v2.4 build. The audit will check:
- C12: Sheet 4 must populate at least 18 of 21 standard columns
- C13: composite key fields must have construction rules documented
- C15: every field must have an Input/Output/Display-only/Calculated classification
- C16: conditional fields must have bidirectional constraint documentation
- C18: every filing in scope_manifest must have a Spec file
- C19: code prefixes must match official source PDFs

Read shared/PRESUBMISSION_AUDIT.md sections C12-C19 before starting.
Read shared/country_failure_log.md F9-F14 to avoid known failures.

## STEP 1 — READ FORMAT REFERENCE

Read these files FIRST before building anything:
1. ~/mercans-pipeline/shared/report-spec-template/REPORT_SPEC_STANDARD_FORMAT.md
2. Open and study: ~/mercans-pipeline/shared/report-spec-template/ES-M296-001_ResumenAnual_Spec.xlsx
   (Spain model — replicate its structure for every ${COUNTRY} report)

## STEP 0 — RESUME CHECK (do this FIRST, before anything else)

Look inside ~/mercans-pipeline/${CODE}-compliance/04-reports-spec/ RIGHT NOW.
For every ${CODE}-*-Spec.xlsx file already there with a matching generator
script (co_r*_*.py) also present: that report is DONE. Do NOT rebuild it, do
NOT re-open it, do NOT re-research it. Skip straight past it. Only research
and build the report(s) that are genuinely missing from that folder. This
matters — a prior run already completed several of these; redoing finished
work burns turns needed for what's actually missing.

## STEP 2 — IDENTIFY ALL ${COUNTRY} REPORTS — APPLY HR-SCOPE FILTER (C1)

### v2.5 — HR-SCOPE FILTER (C1)

Before building any spec, classify each filing as PAYROLL-SCOPE or HR-SCOPE.

DESCOPE (do NOT build spec for) any filing that requires data beyond payroll:
- Annual workforce census reports requiring headcount by qualification,
  occupation, nationality, gender (e.g., Egypt MOL Annual Workforce Report,
  Art. 36 Labour Law 14/2025).
- Talent / training plans
- Workplace safety / accident statistics requiring HSE data
- Equal opportunity / diversity reports
- Disability quota compliance reports
- Any filing where >50% of fields come from HRMS, not payroll.

For each descoped filing, add to scope_manifest.json under
\`authority_filings.out_of_scope\` with:
  "descoping_reason": "HR-scope — requires data beyond payroll system (specifically: [list fields])",
  "client_impact": "Refer to HRMS team. Not produced by payroll pipeline."

Then proceed with the PAYROLL-SCOPE filings only.

### Standard step 2

Read scope_manifest.json's authority_filings.in_scope — those are the reports
to build. Every entry must produce a Spec file.

If scope_manifest.in_scope is empty or thin, also research independently:
- Tax authority: monthly wage tax declaration, annual income statement, corrections
- Social security: contribution declarations, benefit claims
- Labour ministry: hire/termination notifications, employment statistics
- Any other mandatory employer reporting

Cross-check your report list against:
1. scope_manifest.json (authoritative)
2. CCG Module 10
3. Source PDFs in 00-official-sources/pdfs/
4. Web search: "${COUNTRY} employer payroll statutory reports ${YEAR} complete list"

Flag any reports where you're uncertain (active vs abolished).

## STEP 3 — IDENTIFY INBOUND INTEGRATIONS

Before building specs, check scope_manifest.integrations.inbound for any
government → employer file/API flows that need their own spec.
Examples: Denmark tax card XML (skattekortet), Netherlands wage tax tables.

For each inbound integration, build a separate spec following the same 9-sheet
structure. Mark integration_type=inbound in Report Matrix.

## STEP 3.5 — VERIFY SUBMISSION FORMAT & CHANNEL (v2.7 — MANDATORY)

This step exists because assuming a format (especially XML) caused major manual
rework. For EVERY report, you must VERIFY how it is actually submitted before
writing Sheet 5 or Sheet 9. Never assume.

Read shared/country_portal_registry.md first. It maps, per country, each
institution to its portal name, verified URL, and the likely format archetype,
plus an analogue library (DISA = per-employee annual salary declaration;
DSF = aggregate annual fiscal statement) for field cross-checks.

For each report determine the submission CHANNEL and classify it as exactly one:
  - online_form        : data keyed directly into a portal form / imprimé
  - file_upload        : a file generated by the payroll software and uploaded
                         to the portal (record the template type: xlsx / csv /
                         fixed-width, and the column layout if published)
  - xml                : machine-to-machine XML — ONLY if an official XSD /
                         cahier des charges is cited
  - api                : direct API submission (cite the spec)
  - paper              : paper imprimé / titre de paiement

RULES:
  - Default assumption for francophone-Africa / CEMAC (e.g. ${COUNTRY} if in that
    bloc) is PORTAL-BASED: online form entry OR a software-generated upload —
    NOT machine-to-machine XML. Confirm against the official portal.
  - Use the CORRECT portal per institution. The social-security portal is NOT
    the tax portal (e.g. CNPS télédéclaration vs DGI e-Tax). Never label a
    social-security report with the tax e-portal name or URL, or vice-versa.
  - Cite the source (portal URL / official guide) for the channel you record.
  - If you cannot confirm the exact import mechanism from public/official
    sources, record it as the best-supported value and add an explicit
    "FORMAT TO CONFIRM vs a real filing" note — do NOT invent a format.
  - Record the verified Submission Method AND File Format in Sheet 2
    (Report Matrix). "XML" may only be written if an official XSD is cited.

Output a short per-report line into the Report Matrix accuracy note:
  "Channel: <type> | Portal: <name+URL> | Source: <url> | <CONFIRMED|TO CONFIRM>".

## STEP 4 — BUILD EACH REPORT — MANDATORY 9-SHEET STRUCTURE

### Pre-build (do these before writing any row):

**A. Extract real field identifiers from official form PDFs.**
If country has form PDFs in 00-official-sources/pdfs/:
- Use pdfplumber to extract ALL text
- Official forms print field codes/identifiers next to each field (e.g. C013A, F001)
- These printed codes ARE the official field identifiers used in file/portal submissions
- Extract every field code — do not guess or derive patterns
- v2.4 CHECK C19: codes in spec MUST match the prefix pattern from the source PDF.
  If you derive without official source, mark identifiers as DERIVED in Notes column.

**B. Extract full field rules from fill-in guide.**
For every field, extract from official guide:
- definition, who populates, when mandatory vs conditional
- validation rules, calculation references, legal basis (law + article)
- Populate column G (Conditional Reason) AND column M (Explanation) for every field
- No field explanation may be blank — minimum 1 sentence per field

**C. Verify row/field positions.**
Cross-reference: field positions in spec MUST match official form layout.

### Sheet 1: Version Control
Document ID, Version, Date, Author, Change log.

### Sheet 2: Report Matrix
Row per metadata item: Report ID | Report Name EN | Report Name Local | Authority |
Frequency | Due Date Rule | Submission Method | File Format | Legal Basis |
Accuracy Assessment (honest % + confidence note + what would improve it)
v2.7: Submission Method and File Format MUST come from STEP 3.5 (the verified
channel + correct portal). Never write "XML" unless an official XSD is cited.

### Sheet 3: Payroll Scope Summary
Two-column table — Item | In Scope.
YES rows: fill FFC6EFCE (green). NO rows: fill FFFFC7CE (red).
Cover: Full-time employees, Part-time, Directors, Freelancers, Gross salary,
Overtime, Benefits in kind, Tax-exempt allowances, etc.

### Sheet 4: [Report Name] Spec — THE CORE SHEET
EXACTLY 21 columns A through U:
A:  Field Name EN
B:  Field Name Local (${LANGUAGE})
C:  Record Type
D:  Field Position
E:  Payroll Field Y/N
F:  Mandatory Y/N/C
G:  Conditional Reason
H:  Position (in file)
I:  Length
J:  Format (YYYYMMDD / 9(8) / X(35) / N2.2 etc.)
K:  Example
L:  System Mapping
M:  Explanation
N:  Relevant for Payroll Y/N
O:  Option Values (ref to Sheet 6 table name)
P:  Rounding
Q:  Negative Y/N
R:  Value Type (Amount/Code/Date/Text/Flag)
S:  Frequency (per record/per period/per year)
T:  Query to RA
U:  RA Comments

HEADER ROW: fill FF4472C4 (blue), white text, bold.

ROW COLOR CODING (entire row):
- FFFFEB9C amber  = Payroll fields (col E = Y)
- FFBDD7EE blue   = System-generated fields
- FFC6EFCE green  = Constants/fixed values
- FFFFC7CE red    = Not applicable/excluded
- FFD6DCE4 grey   = Section header rows

Section header rows use grey fill with separator text in col A:
e.g., "=== EMPLOYER IDENTIFICATION ===", "=== EMPLOYEE DATA ===", "=== EARNINGS ==="

**v2.4 NEW for Sheet 4:**
- Every field where Length > 8 chars AND value contains concatenated patterns
  (codes + dates + sequences) must have "Composite Key: position breakdown" in
  column M Explanation. This is mandatory for C13 to pass.
- Every field's value classification must be unambiguous: column R (Value Type)
  serves as Input/Output/Display-only/Calculated for C15.
- Conditional fields (F=C) must reference other fields in column G AND have
  those fields back-reference in their own G column. C16 enforces bidirectional.

### Sheet 5: File Structure
Represent the submission as a NEUTRAL FIELD MODEL (field list + hierarchy),
labelled "logical model — not the wire/submission format", UNLESS an official
XSD / cahier des charges confirms XML (then show the real XML structure).
Do NOT default to an XML hierarchy. If STEP 3.5 found the channel is an online
portal form or a software-generated upload (xlsx/csv) with a published column
layout, document those columns / record layout instead.

### Sheet 6: Field Options
All code tables from Sheet 4 col O. Format: section header per table, then
Code | Abbrev | Local | EN Description.

### Sheet 7: Population Rules
Field Name | Source System | Population Logic | Edge Cases
Tells developers exactly how to fill each field from payroll data.
**v2.4: every conditional field must have at least 100 chars of population logic.**

### Sheet 8: Example Analysis
Parse a sample record field by field: Raw Value | Field Name | Interpretation | Notes.

### Sheet 9: Sample File
Include a concrete sample ONLY if (a) an official sample exists in
00-official-sources/sample-files/, or (b) STEP 3.5 confirmed the exact format.
If the channel is an online portal form, or a software-generated upload with no
published schema, OMIT this sheet (or state the verified channel) instead.
NEVER fabricate an XML/CSV sample — a fabricated sample is a C25 audit failure.

## SOURCES (read in order)
1. Official FORM IMAGE PDFs in 00-official-sources/pdfs/
2. Official FILL-IN GUIDE PDFs in 00-official-sources/pdfs/
3. Official sample files in 00-official-sources/sample-files/ (if any)
4. Web research (mark as DERIVED in Report Matrix)

## FILE NAMING
${CODE}-AUTHORITY-NNN-ReportName-Spec.xlsx
(e.g., PK-FBR-001-MonthlyWithholding-Spec.xlsx)
Save all to: ~/mercans-pipeline/${CODE}-compliance/04-reports-spec/

## QUALITY CHECK PER REPORT
- [ ] Exactly 9 sheets with correct names
- [ ] Sheet 4 has exactly 21 columns A-U
- [ ] At least 18 of 21 columns populated (C12)
- [ ] Header row is blue (FF4472C4), white, bold
- [ ] Row colors applied correctly
- [ ] Grey section header rows with separator text
- [ ] Payroll Scope Summary has green/red coloring
- [ ] Population Rules sheet complete (100+ chars per conditional field)
- [ ] Accuracy assessment in Report Matrix is honest
- [ ] Column D (Field Position): from official form image — NOT derived
- [ ] Column G (Conditional Reason): populated for every F=C field
- [ ] Column M (Explanation): no blank cells — 1+ sentence per field
- [ ] Column R (Value Type): every field classified (C15)
- [ ] Composite-key fields documented in column M (C13)
- [ ] Conditional fields back-reference each other (C16)
- [ ] Complete report list verified from scope_manifest + 1 other source
- [ ] (v2.8 B1) Income-tax / withholding specs represent BOTH resident and non-resident treatment (fields / rows / notes); non-resident handling is never left implicit
- [ ] (v2.8 B4) Citation article numbers agree with the CCG income-tax module
REPORTSEOF

echo "  Prompt written: $PROMPTS/reports.md"
STAGE3_START=$(date +%s)
if [ "$GENERATE_PROMPTS_ONLY" = "true" ]; then
    echo "  [PROMPTS-ONLY mode] Skipping Report Specs execution"
else
    echo "  Running Report Specs agent (CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000 scoped)..."
    # v2.5 T1+T2: scope token limit to this stage only — prevents Stage 1 side effect
    CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000 claude -p "$(cat "$PROMPTS/reports.md")" \
           --max-turns 180 \
           --dangerously-skip-permissions \
           > "$LOGS/reports.log" 2>&1
fi
STAGE3_END=$(date +%s)
STAGE3_DURATION=$((STAGE3_END - STAGE3_START))
echo "  Report Specs done in ${STAGE3_DURATION}s ($((STAGE3_DURATION / 60)) min)"

spec_count=$(find "$BASE/04-reports-spec" -name "${CODE}-*-Spec.xlsx" 2>/dev/null | wc -l | tr -d ' ')
if [ "$GENERATE_PROMPTS_ONLY" != "true" ] && [ "$spec_count" -eq 0 ]; then
    echo "ERROR: No spec files produced in 04-reports-spec/"
    echo "  Check log: $LOGS/reports.log"
    exit 1
fi
# v2.5 R1 — stage completion summary
echo "  STAGE 3 SUMMARY: $spec_count spec files produced"
echo ""
fi  # end stage_skip_check 3

# =============================================================================
# STAGE 4 — Data Dictionary (CZ V2.0 format)
# =============================================================================
if stage_skip_check 4 "Data Dictionary"; then
echo "----------------------------------------------------------------"
echo "STAGE 4/11 — Data Dictionary (CZ V2.0 format, strict scope)"
echo "Est. 25-35 min"
echo "----------------------------------------------------------------"

cat > "$PROMPTS/dd.md" << DDEOF
# ${COUNTRY} DATA DICTIONARY — CZ V2.0 FORMAT

You are building the ${COUNTRY} Data Dictionary using the CZ V2.0 template format.

## FORMAT REFERENCE
Load: ~/mercans-pipeline/shared/CZ_Data_Dictionary_V2_0.xlsx
Do NOT create a new Workbook(). Load CZ file, clear data rows, populate
preserving all formatting, colors, column widths, sheet order, row heights.

## 8 SHEETS (preserve from CZ template)
1. Version Control
2. Introduction
3. Instructions (change country name only)
4. ID Information
5. Country Fields
6. Country Option Mappers
7. Currency Codes - ISO 4217 (preserve as-is)
8. Country Codes - ISO 3166-1 (preserve as-is)

## COLUMN RULES
POPULATE ONLY BLUE columns (4472C4). Leave ORANGE (FF9900) columns empty — dev team fills those.

ID Information sheet (22 cols A-V):
A: Country="${COUNTRY}" BLUE | B: Ordinal ORANGE | C: Field Name BLUE | D: Internal Code ORANGE
E: Label Local (${LANGUAGE}) BLUE | F: Description BLUE | G: Data Type M/CM/O BLUE
H: Pre-Condition BLUE | I: Field Type BLUE | J: Format BLUE | K: Option Mapper BLUE
L-U: ORANGE | V: Additional Notes BLUE

Country Fields sheet: same pattern, col A empty, content from col B.

## SCOPE — STRICTLY user-input master data only

INCLUDE:
- Identification (tax ID, national ID, SS number, bank IBAN, employer reg numbers)
- Demographics (name, DOB, gender, nationality, marital status, place of birth)
- Contact (address, postcode, email, phone)
- Employment (hire date, contract type, job title, hours, FTE%, termination date)
- Tax profile (residency status, tax number, exemption flags)
- SS profile (fund eligibility, contribution category, special status flags)
- Family attributes (number of children, disability %, spouse info) IF calculation-driving
- Employer master data (name, registration numbers, addresses, sector)
- Code/selector fields that drive calculation paths

EXCLUDE (dev team will reject):
- Calculated amounts → WTC scope
- Base Salary / Basic Salary amounts → WTC, NOT DD
- Gross pay, net pay, taxable income → calculated
- Tax rates, SS rates → parameters
- Ceilings, thresholds, minimum wage → parameters
- Authority-generated values (submission IDs, receipts)
- Transactional per-payrun data (period dates, days worked, sick leave dates)

## PRIVATE SECTOR FILTER — CRITICAL
The Mercans platform serves PRIVATE SECTOR employers only.
When building Country Option Mappers, EXCLUDE non-private-sector categories:
- Civil servants / state employees — separate legislation
- Military, police, security forces — separate state SS scheme
- Self-insured persons (freelancers, craftsmen, farmers) — pay SS directly, not via employer
- Cooperative members without labour contract — not employment income
- Persons receiving unemployment benefits — registered with Employment Agency, not employer

INCLUDE for private sector option mappers:
- Standard employees under employment contract — full SS scenario
- Managers/directors under management contracts (with note: which SS funds apply)
- Employees on maternity/parental/sick leave (record-only, benefit paid by SS authority)
- Working pensioners under employment contract
- Part-time, fixed-term, posted, foreign nationals under standard employment

## ALIGNMENT WITH REPORT SPECS
Cross-reference report specs at ~/mercans-pipeline/${CODE}-compliance/04-reports-spec/
For each spec field, classify: DD / TX / CALC / SYS
Ensure all DD-bucket fields are in the DD. TX/CALC/SYS are correctly excluded.

## v2.4 — OPTION MAPPER COMPLETENESS (C14)
For every Option Mapper in Country Option Mappers sheet:
- Every code must have: (a) code value, (b) description, (c) constraint flag if conditional
- If a Spec field references this mapper with Mandatory=C, the constraint MUST be
  documented in the mapper's Notes column

## SOURCES
1. CZ template: ~/mercans-pipeline/shared/CZ_Data_Dictionary_V2_0.xlsx
2. Report Specs: ~/mercans-pipeline/${CODE}-compliance/04-reports-spec/
3. scope_manifest.json
4. CCG: ~/mercans-pipeline/${CODE}-compliance/01-ccg/${CODE}-CCG-001-v1.0.docx
5. Official PDFs: ~/mercans-pipeline/${CODE}-compliance/00-official-sources/pdfs/

## OUTPUT
Save to: ~/mercans-pipeline/${CODE}-compliance/05-data-dictionary/${CODE}-DD-001-v1.0.xlsx
Use openpyxl. Load CZ template, clear data rows, populate all sheets.
DDEOF

echo "  Prompt written: $PROMPTS/dd.md"
STAGE4_START=$(date +%s)
if [ "$GENERATE_PROMPTS_ONLY" = "true" ]; then
    echo "  [PROMPTS-ONLY mode] Skipping DD execution"
else
    echo "  Running DD agent..."
    run_claude_or_skip "$PROMPTS/dd.md" "$LOGS/dd.log" 50
fi
STAGE4_END=$(date +%s)
STAGE4_DURATION=$((STAGE4_END - STAGE4_START))
echo "  DD done in ${STAGE4_DURATION}s ($((STAGE4_DURATION / 60)) min)"
# v2.5 R1 — stage completion summary
if [ -f "$BASE/05-data-dictionary/${CODE}-DD-001-v1.0.xlsx" ]; then
    dd_size=$(stat -f%z "$BASE/05-data-dictionary/${CODE}-DD-001-v1.0.xlsx" 2>/dev/null || echo "?")
    echo "  STAGE 4 SUMMARY: DD xlsx produced (${dd_size} bytes)"
fi
echo ""

if [ "$GENERATE_PROMPTS_ONLY" != "true" ] && [ ! -f "$BASE/05-data-dictionary/${CODE}-DD-001-v1.0.xlsx" ]; then
    echo "ERROR: DD not produced"
    echo "  Check log: $LOGS/dd.log"
    exit 1
fi
fi  # end stage_skip_check 4

# =============================================================================
# STAGE 5 — Wage Type Catalogue — v2.5 T1: scoped tokens
# =============================================================================
if stage_skip_check 5 "Wage Type Catalogue"; then
echo "----------------------------------------------------------------"
echo "STAGE 5/11 — WTC (CZ V2.0 + Global WTC baseline) — v2.5 T1"
echo "Est. 30-50 min  |  CLAUDE_CODE_MAX_OUTPUT_TOKENS scoped to 64000 for this stage"
echo "----------------------------------------------------------------"

cat > "$PROMPTS/wtc.md" << WTCEOF
# ${COUNTRY} WAGE TYPE CATALOGUE — CZ V2.0 + GLOBAL WTC BASELINE

You are building the ${COUNTRY} Wage Type Catalogue using the CZ V2.0 template format.

## STEP 1: READ THE GLOBAL WTC BASELINE FIRST
Open: ~/mercans-pipeline/shared/Global_WTC_V1_0.xlsx
This has ~300 standard global wage type codes and descriptions.
These are the BASELINE. They have codes and names ONLY — ZERO configuration.
You MUST configure every included wage type fresh for ${COUNTRY}.
The same wage type has completely different tax/SS treatment in different countries.

ALL ~300 global codes are MANDATORY — include every single one. Do NOT exclude
any global code. Every country must have all global codes. The ONLY thing that
changes per country is the taxability configuration.

For each global code:
- Configure it fully for ${COUNTRY} ${YEAR} tax/SS rules
- Do NOT skip it — every code must appear in the WTC

## STEP 2: ADD ${COUNTRY}-SPECIFIC WAGE TYPES
Research ${COUNTRY}-specific types not in the global list:
- ${COUNTRY}-specific allowances and benefits
- ${COUNTRY}-specific SS fund contribution types
- Any locally-named statutory payments

## FORMAT REFERENCE
Load: ~/mercans-pipeline/shared/_CZ_Wage_Type_Catalogue_V2_0.xlsx
Do NOT create a new Workbook(). Load CZ file, clear data rows, populate
preserving all formatting.

## 5 SHEETS IN OUTPUT (4 from CZ template + 1 new)
1. Version Control
2. Wage Type Catalogue (main sheet)
3. Employer Sick Pay (if applicable in ${COUNTRY})
4. Tax Credit (if applicable in ${COUNTRY})
5. Global WTC Coverage (NEW — confirm all ~300 global codes included +
   list any ${COUNTRY}-specific additions beyond the global baseline)

## v2.4 — Form Reference Guide (C17)
Add a 6th sheet: "Form Reference Guide"
Maps every wage type category to its target row in each statutory report.
Columns: Wage Type Category | Spec File | Sheet Name | Row Number | Notes
This is mandatory per v2.4 C17 check. Build by cross-referencing your wage type
categories against the spec files in 04-reports-spec/.

## COLUMN RULES
POPULATE ONLY BLUE columns. Leave ORANGE empty.

Wage Type Catalogue columns:
A: Mercans Code ORANGE | B: Name EN BLUE | C: Name Local (${LANGUAGE}) BLUE
D: Explanation ORANGE | E: Category BLUE (Earning/Deduction/Base/Employer Contribution/Flag/Intermediary/Notional/Tax/Percentage)
F: Formula BLUE (plain text with ${YEAR} rates) | G: Tax Code BLUE | H-I: ORANGE
J: Occurrence BLUE (Recurring/Additional/NA) | K-M: ORANGE
N: Subject to Tax BLUE (Yes/No/Yes-No/NA)
O: Table Tax BLUE (Yes/No/Yes-No/NA)
P: Special Tax BLUE (Yes/No/Yes-No/NA)
Q: Subject to Social Insurance BLUE (Yes/No/Yes-No/NA)
R: Subject to Pension BLUE (Yes/No/Yes-No/NA)
S-T: ORANGE

## SS FUND EXPANSION
If ${COUNTRY} has multiple distinct SS funds, expand Q-R into per-fund columns:
- Q1: Subject to [Fund 1 Name]
- Q2: Subject to [Fund 2 Name]
- Q3: Subject to [Fund 3 Name] etc.
- R: Subject to Pension
Same BLUE formatting, same Yes/No/Yes-No/NA dropdowns.
Research ${COUNTRY} SS fund structure from CCG Module 5.

## CONFIGURATION REQUIREMENTS
For EACH wage type, research ${COUNTRY} ${YEAR} rules specifically:
- Exact formula with ${YEAR} rates/thresholds in ${CURRENCY}
- Subject to income tax? Which type? (table rate / flat rate / exempt)
- Subject to each SS fund? Any contribution ceiling?
- Any special tax treatment (exempt amount, benefit-in-kind valuation method)?

DO NOT copy treatment from other countries. Research ${COUNTRY} specifically.

## v2.4 — TAX CODE VERIFICATION (C9)
Every tax code in WTC must be verified against the country's specific tax
authority publication. Add a column or note for the official source of each
tax code. Never guess or copy from another country.

## v2.5 — POST-GENERATION VALIDATION CHECKLIST (C3)

Before saving the final WTC, verify in code:

\`\`\`python
import json, openpyxl
manifest = json.load(open(f'/Users/wallissongomes/mercans-pipeline/${CODE}-compliance/scope_manifest.json'))
wb = openpyxl.load_workbook(f'/Users/wallissongomes/mercans-pipeline/${CODE}-compliance/02-wtc/${CODE}-WTC-001-v1.0.xlsx')
ws = wb['Wage Type Catalogue']
codes_in_wtc = {row[1].value for row in ws.iter_rows(min_row=2) if row[1].value}

# Check 1 — every scope_manifest wage type category is represented
required = set()
for cat in manifest.get('wage_type_categories', {}).get('in_scope', []):
    required.add(cat)
missing = required - codes_in_wtc
assert not missing, f'Missing wage types from WTC: {missing}'

# Check 2 — every tax code referenced is in the defined country tax code legend
defined_tax_codes = set()  # populate from the Tax Code legend sheet
for row in ws.iter_rows(min_row=2):
    tc = row[6].value  # column G — Tax Code
    if tc and tc not in defined_tax_codes:
        print(f'WARN: tax code {tc} not in legend for row {row[0].row}')

# Check 3 — no 'Yes-No' ambiguity in core taxability columns unless explicitly justified
for row in ws.iter_rows(min_row=2):
    for col_idx in [13, 14, 15, 16, 17]:  # N-R: Subject to Tax/Table/Special/SS/Pension
        val = row[col_idx].value
        if val == 'Yes-No':
            # require a note in the explanation column
            assert row[3].value, f'Yes-No in row {row[0].row} requires explanation'

print('WTC post-generation validation PASSED')
\`\`\`

Specifically guard against the Egypt failures (F20):
- Commission wage type MISSING from output entirely
- Tax codes from legends of OTHER countries (e.g. EG-TX-3 when EG legend is EG-TX-1 through 7)
- 'Yes-No' on SS subject flags without an explanation cell

## SOURCES
1. Global WTC baseline: ~/mercans-pipeline/shared/Global_WTC_V1_0.xlsx
2. CZ format template: ~/mercans-pipeline/shared/_CZ_Wage_Type_Catalogue_V2_0.xlsx
3. CCG Modules 3-7: ~/mercans-pipeline/${CODE}-compliance/01-ccg/${CODE}-CCG-001-v1.0.docx
4. Official PDFs: ~/mercans-pipeline/${CODE}-compliance/00-official-sources/pdfs/
5. scope_manifest.json (wage_type_categories.in_scope vs out_of_scope)

## OUTPUT
Save to: ~/mercans-pipeline/${CODE}-compliance/02-wtc/${CODE}-WTC-001-v1.0.xlsx
Use openpyxl. Load CZ template, add Global WTC Coverage sheet + Form Reference
Guide sheet, populate all sheets.
WTCEOF

echo "  Prompt written: $PROMPTS/wtc.md"
STAGE5_START=$(date +%s)
if [ "$GENERATE_PROMPTS_ONLY" = "true" ]; then
    echo "  [PROMPTS-ONLY mode] Skipping WTC execution"
else
    echo "  Running WTC agent (CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000 scoped)..."
    # v2.5 T1: scope token limit to this stage only
    CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000 claude -p "$(cat "$PROMPTS/wtc.md")" \
           --max-turns 60 \
           --dangerously-skip-permissions \
           > "$LOGS/wtc.log" 2>&1
fi
STAGE5_END=$(date +%s)
STAGE5_DURATION=$((STAGE5_END - STAGE5_START))
echo "  WTC done in ${STAGE5_DURATION}s ($((STAGE5_DURATION / 60)) min)"
# v2.5 R1 — stage completion summary
if [ -f "$BASE/02-wtc/${CODE}-WTC-001-v1.0.xlsx" ]; then
    wtc_size=$(stat -f%z "$BASE/02-wtc/${CODE}-WTC-001-v1.0.xlsx" 2>/dev/null || echo "?")
    echo "  STAGE 5 SUMMARY: WTC xlsx produced (${wtc_size} bytes)"
fi
echo ""

if [ "$GENERATE_PROMPTS_ONLY" != "true" ] && [ ! -f "$BASE/02-wtc/${CODE}-WTC-001-v1.0.xlsx" ]; then
    echo "ERROR: WTC not produced"
    echo "  Check log: $LOGS/wtc.log"
    exit 1
fi
fi  # end stage_skip_check 5

# =============================================================================
# STAGE 6 — Statutory Integration (v2.9: discover-first, scale-to-reality, auto-fetch)
#   6a discovers the country's integration landscape (system-to-system vs manual)
#   then branches:
#     NO_INTEGRATIONS / MANUAL_ONLY -> a one-page index stating filing is manual
#     HAS_INTEGRATIONS              -> per-authority runbooks; the subagent auto-fetches
#                                      public artefacts (WSDL/XSD/spec PDFs) to reach
#                                      build-ready, leaving [[NEEDS-ARTEFACT]] only for
#                                      login/certificate-gated items.
#   Requires shared/si-runbook installed (.claude/agents/si-discovery.md,
#   .claude/agents/si-runbook-research.md, shared/si-runbook/si_scope_check.py).
# =============================================================================
if stage_skip_check 6 "SIR"; then
echo "----------------------------------------------------------------"
echo "STAGE 6/11 — Statutory Integration (discover landscape -> scale output)"
echo "Est. 15-45 min (scales with number of integrating authorities)"
echo "----------------------------------------------------------------"

SI_DIR="$BASE/03-statutory-integrations"
mkdir -p "$SI_DIR"
STAGE6_START=$(date +%s)

# --- 6a — DISCOVERY: understand the country's integration landscape FIRST ---
cat > "$PROMPTS/si_discover.md" << DISCEOF
Act as the si-discovery agent (${PIPELINE}/.claude/agents/si-discovery.md).
COUNTRY=${COUNTRY}
CODE=${CODE}
OUTPUT_DIR=${SI_DIR}
Inputs: ${BASE}/scope_manifest.json and ${BASE}/01-ccg/${CODE}-CCG-001-v1.0.docx
Deep-research ${COUNTRY}'s PAYROLL statutory-integration landscape. For each authority that
receives payroll statutory data, determine whether it offers a system-to-system channel (API /
web service / SFTP / machine-to-machine upload) or is portal/paper only. Write
${SI_DIR}/integration-landscape.json EXACTLY per the agent schema, with verdict
HAS_INTEGRATIONS | MANUAL_ONLY | NO_INTEGRATIONS. Be honest — if filing is all manual, say so;
do NOT invent an integration. Do NOT write runbooks.
DISCEOF

if [ "$GENERATE_PROMPTS_ONLY" = "true" ]; then
    echo "  [PROMPTS-ONLY mode] discovery prompt written; branch/runbooks skipped (needs landscape)"
else
    echo "  6a — discovering ${COUNTRY} integration landscape..."
    run_claude_or_skip "$PROMPTS/si_discover.md" "$LOGS/si_discover.log" 40
fi

LANDSCAPE="$SI_DIR/integration-landscape.json"
VERDICT="UNKNOWN"
if [ -f "$LANDSCAPE" ]; then
    VERDICT=$(python3 -c "import json,sys
try: print(json.load(open('$LANDSCAPE')).get('verdict','UNKNOWN'))
except Exception: print('UNKNOWN')" 2>/dev/null || echo "UNKNOWN")
fi
echo "  landscape verdict: $VERDICT"

# --- branch on the verdict ---
if [ "$GENERATE_PROMPTS_ONLY" = "true" ]; then
    echo "  [PROMPTS-ONLY mode] skipping branch"
elif [ "$VERDICT" = "MANUAL_ONLY" ] || [ "$VERDICT" = "NO_INTEGRATIONS" ]; then
    echo "  6b — no system-to-system integrations ($VERDICT): writing SHORT index only"
    cat > "$PROMPTS/sir_index.md" << IDXEOF
Read ${LANDSCAPE}. ${COUNTRY} has NO system-to-system statutory integrations (verdict ${VERDICT}).
Produce a SHORT one-page index docx at ${SI_DIR}/${CODE}-SIR-INDEX-001-v1.0.docx that states
plainly, in a few sentences, that no statutory system-to-system integrations exist for ${COUNTRY}
and that all statutory filing is manual (portal/paper). Add a small table listing the manual
authorities/channels from the landscape for reference. Do NOT produce runbooks or phase
deliverables. Keep it to one page.
IDXEOF
    run_claude_or_skip "$PROMPTS/sir_index.md" "$LOGS/sir_index.log" 15
else
    if [ "$VERDICT" = "UNKNOWN" ]; then
        echo "  WARNING: landscape verdict UNKNOWN — attempting runbooks for any integrable authority found"
    fi
    # index of authorities (integrable + manual), pointing to per-authority runbook folders
    cat > "$PROMPTS/sir_index.md" << IDXEOF
Read ${LANDSCAPE}. Produce an index docx at ${SI_DIR}/${CODE}-SIR-INDEX-001-v1.0.docx: a short
table with ONE ROW PER AUTHORITY (integration yes/no, channel, direction(s), dev portal, and
runbook location 03-statutory-integrations/<AUTH_CODE>/ for integrable authorities). One paragraph
noting per-authority Configuration Runbooks are produced for authorities with integration=true;
manual authorities need no runbook.
IDXEOF
    run_claude_or_skip "$PROMPTS/sir_index.md" "$LOGS/sir_index.log" 15

    # extract integrable authorities as CODE|Name lines
    python3 - "$LANDSCAPE" > "$SI_DIR/_integrable.txt" 2>/dev/null << 'PYX'
import json,sys
try:
    d=json.load(open(sys.argv[1]))
    for a in d.get('authorities',[]):
        if a.get('integration') is True and a.get('code'):
            print(a['code'].strip()+'|'+(a.get('name','') or '').strip())
except Exception:
    pass
PYX

    if [ ! -s "$SI_DIR/_integrable.txt" ]; then
        echo "  NOTE: no integrable authorities parsed from landscape; index only."
    else
        while IFS='|' read -r AUTH_CODE AUTH_NAME; do
            [ -z "$AUTH_CODE" ] && continue
            AUTH_LC=$(echo "$AUTH_CODE" | tr '[:upper:]' '[:lower:]')
            echo "  6b — runbooks for authority: $AUTH_CODE ($AUTH_NAME)"
            mkdir -p "$SI_DIR/$AUTH_CODE" "$BASE/integration-sources/$AUTH_LC"
            OTHERS=$(awk -F'|' -v me="$AUTH_CODE" '$1!=me{printf (o?",":"")$1; o=1}' "$SI_DIR/_integrable.txt")
            cat > "$PROMPTS/si_${AUTH_LC}.md" << RBEOF
Act as the si-runbook-research agent (${PIPELINE}/.claude/agents/si-runbook-research.md).
COUNTRY=${COUNTRY}
CODE=${CODE}
AUTH_CODE=${AUTH_CODE}
AUTH_NAME=${AUTH_NAME}
DIRECTIONS=both
MODE=structural
SOURCES_DIR=${BASE}/integration-sources/${AUTH_LC}
OTHER_AUTHORITIES=${OTHERS}
OUTPUT_DIR=${SI_DIR}/${AUTH_CODE}
Landscape: ${LANDSCAPE}
Run Step 0-auto FIRST: deep-search ${AUTH_NAME}'s developer/e-services portal and DOWNLOAD every
public artefact (spec PDFs, WSDL, XSD, record layouts) into SOURCES_DIR, then build BUILD-READY
from them. Leave [[NEEDS-ARTEFACT]] only for artefacts genuinely behind login / certificate /
Cl@ve / CAPTCHA (say why). Do NOT log in, create accounts, use certificates, or bypass CAPTCHAs;
do NOT touch the live service endpoints. Produce the full P1-P7 deliverable set + INTERLINKAGES.md
+ effort-estimates.md + _phase-index.md, scoped to ${AUTH_CODE} ONLY (other authorities:
${OTHERS} — cross-reference only, in INTERLINKAGES.md).
RBEOF
            run_claude_or_skip "$PROMPTS/si_${AUTH_LC}.md" "$LOGS/si_${AUTH_LC}.log" 150
            # readiness/scope check — structural mode (gated placeholders are expected, not a FAIL)
            if [ -f "$SHARED/si-runbook/si_scope_check.py" ]; then
                if [ -n "$OTHERS" ]; then
                    python3 "$SHARED/si-runbook/si_scope_check.py" "$SI_DIR/$AUTH_CODE" --code "$CODE" --auth "$AUTH_CODE" --mode structural --other "$OTHERS" || true
                else
                    python3 "$SHARED/si-runbook/si_scope_check.py" "$SI_DIR/$AUTH_CODE" --code "$CODE" --auth "$AUTH_CODE" --mode structural || true
                fi
            else
                echo "    (si_scope_check.py not installed in $SHARED/si-runbook — skipping check)"
            fi
        done < "$SI_DIR/_integrable.txt"
    fi
fi

STAGE6_END=$(date +%s)
STAGE6_DURATION=$((STAGE6_END - STAGE6_START))
echo "  SIR done in ${STAGE6_DURATION}s ($((STAGE6_DURATION / 60)) min)"
if [ -f "$SI_DIR/${CODE}-SIR-INDEX-001-v1.0.docx" ]; then
    echo "  STAGE 6 SUMMARY: SIR index produced; per-authority runbooks (if any) under 03-statutory-integrations/<AUTH>/"
fi
echo ""

if [ "$GENERATE_PROMPTS_ONLY" != "true" ] && [ ! -f "$SI_DIR/${CODE}-SIR-INDEX-001-v1.0.docx" ]; then
    echo "ERROR: SIR index not produced"
    echo "  Check logs: $LOGS/si_discover.log , $LOGS/sir_index.log"
    exit 1
fi
fi  # end stage_skip_check 6
# =============================================================================
# STAGE 7 — Payslip (8-sheet Mercans standard, v2.7)
# =============================================================================
if stage_skip_check 7 "Payslip"; then
echo "----------------------------------------------------------------"
echo "STAGE 7/11 — Payslip (8-sheet Mercans standard, v2.7)"
echo "Est. 25-40 min"
echo "----------------------------------------------------------------"

cat > "$PROMPTS/payslip.md" << PAYSLIPEOF
# ${COUNTRY} PAYSLIP GENERATOR — v2.4 MERCANS 5-SHEET STANDARD

Build the ${COUNTRY} Compliance Payslip Generator following the Mercans 8-sheet
standard. The Mozambique reference ALREADY contains these 8 sheets; the prior
pipeline mistakenly mandated a 5-sheet OUTPUT, dropping the setup guide, the
language-neutral master, and the field-option sheet. v2.7 outputs the full 8
and enforces a higher formatting + formula-hygiene bar (the Spain quality bar).

## APPROACH — copy the Mozambique 8-sheet reference and adapt

The proven pattern:

1. **Copy** the Mozambique reference workbook (8-sheet) as your base
2. **Preserve** its formatting exactly: navy title band, section headers in
   #A9A9A9 (white bold, centred), labels in #DCDCDC, green NET PAY highlight
   (#C6EFCE), Arial, merged header/section bands, full borders per section,
   column widths, the accounting number format
3. **Modify** values in place for ${COUNTRY} content; rebuild the two language
   tabs and the master with ${COUNTRY} fields

This inherits the visual standard rather than rebuilding formatting from scratch.

## INPUTS

1. **Master template:** ~/mercans-pipeline/shared/REFERENCE_Payslip_Mozambique.xlsx
   - 8-sheet reference (How-to, master, EN/local, spec, field option, ranges)
   - Will be the BASE that you copy and modify

2. **Reference for spec sheet structure:** ~/mercans-pipeline/shared/REFERENCE_Payslip_Tunisia.xlsx
   - Has the Payslip Spec sheet with HRP Mapping column layout
   - Use this for column structure of "Payslip Spec" and "Unit Rate Details"

3. **Mercans logo:** ~/mercans-pipeline/shared/mercans_logo.png
   - Already embedded in Mozambique template; preserve it

4. **${COUNTRY} content sources:**
   - CCG: ~/mercans-pipeline/${CODE}-compliance/01-ccg/${CODE}-CCG-001-v1.0.docx
     (Module 10.3 / equivalent for payslip mandatory components per labor code)
   - WTC: ~/mercans-pipeline/${CODE}-compliance/02-wtc/${CODE}-WTC-001-v1.0.xlsx
     (pick representative earnings/deductions for the visual payslip example)
   - DD: ~/mercans-pipeline/${CODE}-compliance/05-data-dictionary/${CODE}-DD-001-v1.0.xlsx
     (employee/employer fields)

## OUTPUT

Save as: ~/mercans-pipeline/${CODE}-compliance/06-payslip/${CODE}_Compliance_Payslip_Generator.xlsx

## 8-SHEET STRUCTURE — MANDATORY (v2.7)

The output workbook MUST have exactly these 8 sheets in this order:
1. How to set up Payslip      (setup instructions)
2. Compliance Payslip         (language-neutral MASTER template; pay-element
                               names shown as "XXXXX — earning/deduction/..." )
3. ${COUNTRY} (EN)
4. ${COUNTRY} (${LOCAL_LANG_SHORT})
5. Payslip Spec
6. Field Option               (allowed values for coded fields, e.g. Salary
                               Type, Payment Method, Residential Status — keep
                               consistent with the DD option mappers)
7. Population Range
8. Unit Rate Details

NO standalone Payslip Spec file. The spec lives inside this workbook as a sheet.

## v2.7 FORMATTING & FORMULA REQUIREMENTS (enforced by C26)

Formatting tokens (match the Spain reference):
- Title band: navy fill, white bold ~15pt, merged across the sheet width.
- Section headers ("Employer", "Employee", "Earnings", "Deductions",
  "Employer contributions", "Leave balances", "YTD", "Statutory notes"):
  fill #A9A9A9, white, bold, centred, merged full width.
- Field labels / table column headers: fill #DCDCDC, bold.
- NET PAY row: fill #C6EFCE (green), bold; also show a NET PAY highlight near the
  title that references the net cell.
- Full thin borders on every info/table cell; merge label/value blocks so text
  is never clipped (a long employer address gets its own full-width row).

Currency / number format:
- Use the accounting format. For ZERO-MINOR-UNIT currencies (XAF, XOF, etc.)
  use the INTEGER variant (no decimals): _(* #,##0_);_(* \\(#,##0\\);_(* "-"??_);_(@_)
- For currencies WITH a minor unit, keep 2 decimals.

Formula hygiene (no manual-rework bugs):
- Totals are FORMULAS and appear ONLY on total rows:
    Gross = SUM(earnings amount range), Total deductions = SUM(...),
    Net = Gross_cell - Deductions_cell, Total employer = SUM(...),
    Leave Balance = Entitlement_cell - Taken_cell.
- Use ONE consistent amount column for SUM ranges (do not mix H:J vs H).
- NEVER put a CONCATENATE/total formula on a data row, and never duplicate a
  total. No #NAME?/#VALUE! literals anywhere.

## AUDIT CHECKS
- C26: all 8 sheets present in correct order; totals are formulas on total rows;
       zero-minor-unit currency uses the integer format; no fabricated/duplicated
       totals.
- C22: Payslip Spec has 5 sections (Header Details, Employer Fields,
       Employee Fields, Earnings Fields, Deductions Fields) with 20+ field rows total

### Sheet 1 — "${COUNTRY} (EN)"

Visual payslip in English. Sample employee using a typical ${COUNTRY} name.

Layout — copy Mozambique (EN) structure exactly:
- Mercans logo top-left (preserved from template, do NOT remove)
- Title bar: navy #1F3864 fill, white "${COUNTRY} Payslip" text
- Pay period block (period start - end, pay date)
- Net Pay bar (navy #1F3864 fill, white text, prominent)
- Employer block (legal name, tax ID, address) with header gray #A9A9A9 fill
- Employee block (full name, ID, position, dept, etc.)
- Earnings section (gray header, light gray #F2F2F2 alternating rows)
- Deductions section (gray header)
- Employer contributions block (informative — light orange #FCE4D6)
- Leave balance table (statutory leave types for ${COUNTRY})
- Statutory notes (light gray #F2F2F2, italic, citing ${YEAR} rates)
- Footer: "This document has been generated by Mercans Payroll System | © All rights reserved — Mercans"

Use realistic ${COUNTRY} ${YEAR} numbers:
- Mid-level professional salary in ${CURRENCY}
- Calculate ALL deductions correctly at ${YEAR} statutory rates from WTC
- Show correct gross-to-net with actual numbers

### Sheet 2 — "${COUNTRY} (${LOCAL_LANG_SHORT})"

Identical layout to (EN) but with ${LANGUAGE} labels.
- Translate "Net Pay" → ${LANGUAGE} equivalent
- Translate section headers and field labels
- Currency formatting per ${COUNTRY} convention (thousands separator, decimals)
- Same sample data, just ${LANGUAGE} labels

### Sheet 3 — "Payslip Spec"

The formal spec, embedded as a sheet. 4-column layout (matching Tunisia reference):

| Field Name (EN) | Field Name (${LANGUAGE}) | HRP Mapping (TA & BA) | Field Explanation |

5 sections (section header rows in navy fill, white bold text):
1. Header Details (Payslip title, Company logo)
2. Employer Fields (legal name, tax ID, address, etc.)
3. Employee Fields (name, ID, position, etc.)
4. Earnings Fields (basic salary, overtime, allowances, etc. — from WTC)
5. Deductions Fields (SS contributions, income tax, etc. — from WTC)

HRP Mapping syntax (copy patterns from Tunisia reference):
- Single field: \$entity.field → e.g. \$legal_entity.name
- Concatenation: CONCAT(\$entity.f1, ', ', \$entity.f2)
- Date format: DATE_FORMAT(\$entity.field, 'DD/MM/YYYY')
- Sum: SUM(\$payroll.earnings.*)
- Code series: (XXXXX:XXXXX) for WTC code ranges

Target ~25-35 field rows total across the 5 sections.
C22 requires all 5 sections + minimum 20 field rows total.

### Sheet 4 — "Unit Rate Details"

Map ${COUNTRY} WTC earnings to rate/unit accounts. Column structure (from Tunisia):
- Earning Description (EN)
- Earning Code (from WTC)
- Rate Account
- Unit Account
- Notes

Cover at least the top 20 earnings codes from ${CODE}-WTC-001-v1.0.xlsx
(Basic Salary, Overtime, Family Allowance, Commissions, Bonuses, Leave Payments,
Severance, etc.)

### Sheet 5 — "Population Range"

3-column table:
| Worker Situation | Include? (YES/NO) | Notes |

Rows to cover (adjust to ${COUNTRY} legal framework):
- Active employees (full-time) — YES
- Active employees (part-time) — YES
- New hires during period — YES
- Terminations during period — YES (per ${COUNTRY} severance law)
- Sick leave — YES
- Maternity / paternity leave — YES
- Unpaid leave — YES
- Suspended employees — YES (if applicable)
- Pensioners receiving pension only — NO (no employment payslip)
- External contractors — NO (not payroll-managed)

## ${COUNTRY}-SPECIFIC PAYSLIP CONTENT

Read CCG Module 10.3 for ${COUNTRY} payslip mandatory items (per labour code).
Common requirements:
1. Employer identification (tax ID, name, address)
2. Employee identification (national ID, name, position)
3. Pay period
4. Each remuneration item separately
5. Each legal deduction separately
6. Each voluntary deduction with written authorisation
7. Net pay
8. SS institution names and rates
9. Worked days / absent days for the period

Pull current ${YEAR} rates from WTC for the example.

## BUILD APPROACH

\`\`\`python
import shutil
from openpyxl import load_workbook

# 1. Copy Mozambique template as starting point
shutil.copy(
    '/Users/wallissongomes/mercans-pipeline/shared/REFERENCE_Payslip_Mozambique.xlsx',
    '/Users/wallissongomes/mercans-pipeline/${CODE}-compliance/06-payslip/${CODE}_Compliance_Payslip_Generator.xlsx'
)

# 2. Open the copy
wb = load_workbook('/Users/wallissongomes/mercans-pipeline/${CODE}-compliance/06-payslip/${CODE}_Compliance_Payslip_Generator.xlsx')

# 3. Mozambique template ALREADY has 8 sheets — keep all of them:
#    "How to set up Payslip", "Compliance Payslip", "Mozambique (EN)",
#    "Mozambique (PT)", "Payslip Spec 1", "Field Option", "Population Range",
#    "Unit Rate Details".

# 4. Rename and modify values in place, preserving formatting/merges/images:
#    "Mozambique (EN)" → "${COUNTRY} (EN)"
#    "Mozambique (PT)" → "${COUNTRY} (${LOCAL_LANG_SHORT})"
#    "Payslip Spec 1"  → "Payslip Spec"
#    Update the "Compliance Payslip" master (keep XXXXX pay-element placeholders),
#    "How to set up Payslip" (country touches), "Field Option" (country options),
#    "Population Range" and "Unit Rate Details".

# 5. v2.7 — DO NOT delete "How to set up Payslip", "Compliance Payslip" or
#    "Field Option". They are part of the required 8-sheet structure. (The old
#    pipeline deleted them, which is why prior payslips were incomplete.)

# 6. Verify sheet order matches the required 8-sheet layout:
#    How to set up Payslip, Compliance Payslip, ${COUNTRY} (EN),
#    ${COUNTRY} (${LOCAL_LANG_SHORT}), Payslip Spec, Field Option,
#    Population Range, Unit Rate Details

wb.save('/Users/wallissongomes/mercans-pipeline/${CODE}-compliance/06-payslip/${CODE}_Compliance_Payslip_Generator.xlsx')
\`\`\`

## SELF-CHECK BEFORE SAVING

\`\`\`python
from openpyxl import load_workbook
wb = load_workbook('/Users/wallissongomes/mercans-pipeline/${CODE}-compliance/06-payslip/${CODE}_Compliance_Payslip_Generator.xlsx')
expected = ['How to set up Payslip', 'Compliance Payslip', '${COUNTRY} (EN)', '${COUNTRY} (${LOCAL_LANG_SHORT})', 'Payslip Spec', 'Field Option', 'Population Range', 'Unit Rate Details']
actual = wb.sheetnames
print(f"Expected: {expected}")
print(f"Actual:   {actual}")
assert actual == expected, f"Sheet mismatch! Expected {expected}, got {actual}"
ws = wb['${COUNTRY} (EN)']
if not getattr(ws, '_images', []):
    print("WARN: no embedded logo on EN sheet — branding via the navy title band is acceptable")
print("All checks pass")
\`\`\`

Report back: final sheet names, logo present yes/no, row counts per sheet,
confirmation of save.
PAYSLIPEOF

echo "  Prompt written: $PROMPTS/payslip.md"
STAGE7_START=$(date +%s)
if [ "$GENERATE_PROMPTS_ONLY" = "true" ]; then
    echo "  [PROMPTS-ONLY mode] Skipping Payslip execution"
elif [ -f "$BASE/06-payslip/${CODE}_Compliance_Payslip_Generator.xlsx" ] && [ "${FORCE_PAYSLIP_REBUILD:-false}" != "true" ]; then
    echo "  Payslip Generator already exists (verified, citation-accurate) — skipping regeneration."
    echo "  Set FORCE_PAYSLIP_REBUILD=true to force a fresh rebuild instead."
else
    echo "  Running Payslip agent..."
    run_claude_or_skip "$PROMPTS/payslip.md" "$LOGS/payslip.log" 60
fi
STAGE7_END=$(date +%s)
STAGE7_DURATION=$((STAGE7_END - STAGE7_START))
echo "  Payslip done in ${STAGE7_DURATION}s ($((STAGE7_DURATION / 60)) min)"
# v2.5 R1 — stage completion summary
if [ -f "$BASE/06-payslip/${CODE}_Compliance_Payslip_Generator.xlsx" ]; then
    ps_size=$(stat -f%z "$BASE/06-payslip/${CODE}_Compliance_Payslip_Generator.xlsx" 2>/dev/null || echo "?")
    echo "  STAGE 7 SUMMARY: Payslip Generator produced (${ps_size} bytes)"
fi
echo ""

if [ "$GENERATE_PROMPTS_ONLY" != "true" ] && [ ! -f "$BASE/06-payslip/${CODE}_Compliance_Payslip_Generator.xlsx" ]; then
    echo "ERROR: Payslip Generator not produced"
    echo "  Check log: $LOGS/payslip.log"
    exit 1
fi
fi  # end stage_skip_check 7

# =============================================================================
# STAGE 8 — Alignment Patch (DD ↔ Report Specs)
# =============================================================================
if stage_skip_check 8 "Alignment Patch"; then
echo "----------------------------------------------------------------"
echo "STAGE 8/11 — Alignment Patch (DD ↔ Report Specs cross-validation)"
echo "Est. 20-30 min"
echo "----------------------------------------------------------------"

cat > "$PROMPTS/alignment.md" << ALIGNEOF
# ${COUNTRY} ALIGNMENT PATCH — DD vs REPORT SPECS

Fix all mismatches between the Data Dictionary and Report Specs before the audit.
This is a mandatory step. Do NOT skip any check.

## STEP 0 — VERIFY CURRENT STATE FIRST (a prior run of this exact stage may
## have been interrupted partway through)

Before applying any fix, check the CURRENT content of the DD and each spec —
do not assume a pristine, unfixed starting point. For each of the 6 checks
below: if the DD/spec pair already reflects the correct, aligned state,
leave it alone and move to the next check. Only apply a fix where the
current file content genuinely still shows the mismatch. This avoids both
redundant rework and accidentally re-breaking something an interrupted prior
pass already corrected. Verifying a check takes far fewer turns than
re-applying it — spend the budget on what's actually still wrong.

## READ ALL FILES
1. DD: ~/mercans-pipeline/${CODE}-compliance/05-data-dictionary/${CODE}-DD-001-v1.0.xlsx
2. ALL report specs: ~/mercans-pipeline/${CODE}-compliance/04-reports-spec/
3. CCG: ~/mercans-pipeline/${CODE}-compliance/01-ccg/${CODE}-CCG-001-v1.0.docx
4. scope_manifest.json

## CHECK 1: OPTION MAPPER CODE ALIGNMENT (F1 prevention)
For every Option Mapper referenced in any spec Sheet 6 (Field Options):
- Find the same mapper in DD Country Option Mappers sheet
- Compare every code, value, and local name
- If they differ: update BOTH files to match the authoritative source
  (authoritative = official government form/XSD > CCG > web research)
- Document every fix: field name | old value | new value | source

## CHECK 2: FIELD CLASSIFICATION ACCURACY (F3 prevention)
For every field in every spec Sheet 4 (Field Specification), column E (Payroll Field Y/N):
- If field exists in DD Country Fields sheet → it is an EMPLOYEE field
- If field exists in DD ID Information (employer rows) → it is an EMPLOYER field
- If field is calculated (amount, total, tax) → it is NOT a payroll master data field
- Fix any misclassification found

## CHECK 3: MANDATORY/CONDITIONAL FLAGS (F13 prevention)
For every field marked Mandatory=C (conditional) in specs:
- Verify the Conditional Reason column (col G) is filled with a clear condition
- If empty → research the condition from official docs and fill it
- Common pattern: "Required when [field X] = [value Y]"
- v2.4 C16: ensure bidirectional reference — if A's condition mentions B, then
  B's notes must mention A

## CHECK 4: OPTION VALUES COMPLETENESS (F14 prevention)
For every field with Option Values (col O not empty) in spec Sheet 4:
- Verify Sheet 6 (Field Options) has a complete code table for it
- Verify DD Country Option Mappers has the same table with local language values
- If incomplete: research official codes and complete both

## CHECK 5: COMPOSITE KEY DOCUMENTATION (F12 prevention)
For every field where Length > 8 chars and Example shows concatenated patterns
(date + code + sequence), verify column M (Explanation) documents the
"Composite Key Structure" — each sub-field's position, length, source, persistence.

## CHECK 6: CODE PREFIX VERIFICATION (F14 prevention)
For every coded identifier field (eazon, CRA, DT, DJ, AEAT key, etc.):
- Extract prefix pattern from the source PDF
- Verify every code in the spec matches the pattern
- Document the prefix pattern in column J (Format)

## FIXES
- Overwrite DD: ~/mercans-pipeline/${CODE}-compliance/05-data-dictionary/${CODE}-DD-001-v1.0.xlsx
- Overwrite affected specs: ~/mercans-pipeline/${CODE}-compliance/04-reports-spec/
- Bump version in Version Control sheet of each patched file
- Save patch log: ~/mercans-pipeline/${CODE}-compliance/07-qa-crosscheck/${CODE}-ALIGNMENT-PATCH.md
  Format: Check | Field/Mapper | Issue Found | Fix Applied | File Patched
ALIGNEOF

echo "  Prompt written: $PROMPTS/alignment.md"
STAGE8_START=$(date +%s)
if [ "$GENERATE_PROMPTS_ONLY" = "true" ]; then
    echo "  [PROMPTS-ONLY mode] Skipping Alignment execution"
else
    echo "  Running Alignment Patch agent..."
    run_claude_or_skip "$PROMPTS/alignment.md" "$LOGS/alignment.log" 170
fi
STAGE8_END=$(date +%s)
STAGE8_DURATION=$((STAGE8_END - STAGE8_START))
echo "  Alignment Patch done in ${STAGE8_DURATION}s ($((STAGE8_DURATION / 60)) min)"
# v2.5 R1 — stage completion summary
if [ -f "$BASE/07-qa-crosscheck/${CODE}-ALIGNMENT-PATCH.md" ]; then
    echo "  STAGE 8 SUMMARY: alignment patch log produced at 07-qa-crosscheck/"
fi
echo ""
fi  # end stage_skip_check 8

# =============================================================================
# STAGE 9 — Pre-Submission Audit (C1-C28)
# =============================================================================
if stage_skip_check 9 "Pre-Submission Audit"; then
echo "----------------------------------------------------------------"
echo "STAGE 9/11 — Pre-Submission Audit (C1-C28 mechanical + content fix)"
echo "Est. 20-40 min"
echo "----------------------------------------------------------------"

# Write Python audit checks (mechanical, no API)
cat > "$BASE/_audit_v24_mechanical.py" << 'PYEOF'
#!/usr/bin/env python3
"""
v2.4 audit — mechanical checks for ${COUNTRY}. Returns JSON to stdout.
33 checks total (v2.9 adds C32 cross-artifact fact consistency + C33 CCG English-only prose; v2.8 added C29-C31; v2.7 added C23-C28). C8 uses word-boundary regex (no false positive on Spanish "todo" etc.).
"""
import sys, json, re, os
from pathlib import Path

# Inject country params from environment
CODE = os.environ.get('CL_AUDIT_CODE', 'XX')
COUNTRY = os.environ.get('CL_AUDIT_COUNTRY', 'Unknown')
LOCAL_LANG = os.environ.get('CL_AUDIT_LOCAL_LANG_SHORT', 'XX')
CURRENCY = os.environ.get('CL_AUDIT_CURRENCY', '')

PIPELINE = Path(os.environ.get('HOME', '/Users/wallissongomes')) / 'mercans-pipeline'
BASE = PIPELINE / f'{CODE}-compliance'
SHARED = PIPELINE / 'shared'

results = []

# ----- C1: CCG Structural Completeness -----
def c1():
    try:
        from docx import Document
        ccg_path = BASE / '01-ccg' / f'{CODE}-CCG-001-v1.0.docx'
        if not ccg_path.exists():
            return ('C1', 'FAIL', 'CCG missing', [])
        doc = Document(str(ccg_path))
        h1s = [p.text.strip() for p in doc.paragraphs if p.style.name in ('Heading 1', 'Heading1')]
        modules_found = sum(1 for h in h1s if 'Module' in h)
        if modules_found >= 13:
            return ('C1', 'PASS', f'{modules_found} modules', [])
        return ('C1', 'FAIL', f'Only {modules_found} modules (expected 13)', h1s[:5])
    except Exception as e:
        return ('C1', 'ERROR', str(e), [])

# ----- C8: Open Items Resolution (v2.4 WORD-BOUNDARY FIX) -----
def c8():
    """v2.4: use \bTODO\b regex (uppercase, word-boundary) to avoid false positives
       on Spanish 'todo', Portuguese 'todo', French 'tout', etc.
       The previous substring match flagged 'a todo evento' (Chilean legal term)."""
    try:
        from docx import Document
        # Patterns are case-sensitive UPPERCASE word-boundary markers
        # PLUS the lowercase 'to be confirmed' / 'tbd' as lowercase phrase-match
        patterns_upper = [r'\bTODO\b', r'\bTBD\b', r'\bFIXME\b', r'\bXXX\b']
        patterns_phrase = ['to be confirmed', 'to be verified', '[CHECK]', '[?]']
        ccg_path = BASE / '01-ccg' / f'{CODE}-CCG-001-v1.0.docx'
        if not ccg_path.exists():
            return ('C8', 'FAIL', 'CCG missing', [])
        doc = Document(str(ccg_path))
        full_text = '\n'.join(p.text for p in doc.paragraphs)
        hits = []
        for pat in patterns_upper:
            matches = re.findall(pat, full_text)
            if matches:
                hits.append(f'{pat} ({len(matches)} occurrences)')
        for phrase in patterns_phrase:
            if phrase.lower() in full_text.lower():
                hits.append(phrase)
        if not hits:
            return ('C8', 'PASS', 'No open-item markers found', [])
        return ('C8', 'FAIL', f'Open-item markers: {hits}', hits)
    except Exception as e:
        return ('C8', 'ERROR', str(e), [])

# ----- C11: CCG Template Coverage -----
def c11():
    try:
        from docx import Document
        ccg_path = BASE / '01-ccg' / f'{CODE}-CCG-001-v1.0.docx'
        template_path = SHARED / 'CCG_TEMPLATE_QUESTIONS.md'
        if not ccg_path.exists():
            return ('C11', 'FAIL', 'CCG missing', [])
        if not template_path.exists():
            return ('C11', 'SKIP', 'Template questions file missing', [])
        doc = Document(str(ccg_path))
        h3s = [p.text.strip() for p in doc.paragraphs
               if p.style.name in ('Heading 3', 'Heading3')]
        template = template_path.read_text()
        questions = [l.strip()[2:] for l in template.split('\n')
                     if l.strip().startswith('- ') and ('?' in l or 'Deliverable' in l)]
        matched = 0
        unmatched = []
        for q in questions:
            key = q[:30].lower().strip()
            if any(key in h.lower() for h in h3s):
                matched += 1
            else:
                unmatched.append(q[:60])
        coverage = matched / max(len(questions), 1)
        if coverage >= 0.95:
            return ('C11', 'PASS', f'{matched}/{len(questions)} ({coverage:.0%})', [])
        elif coverage >= 0.80:
            return ('C11', 'MANUAL', f'{matched}/{len(questions)} ({coverage:.0%})', unmatched[:10])
        return ('C11', 'FAIL', f'{matched}/{len(questions)} ({coverage:.0%})', unmatched[:10])
    except Exception as e:
        return ('C11', 'ERROR', str(e), [])

# ----- C12: Spec Column Schema Depth -----
def c12():
    try:
        from openpyxl import load_workbook
        STANDARD = ['name', 'mandatory', 'reason', 'path', 'length', 'type',
                    'example', 'mapping', 'explanation', 'payroll', 'code',
                    'rounding', 'negative', 'value', 'frequency', 'error']
        findings = []
        spec_dir = BASE / '04-reports-spec'
        if not spec_dir.exists():
            return ('C12', 'SKIP', 'No 04-reports-spec/', [])
        thin_count = 0
        spec_files = sorted(spec_dir.glob(f'{CODE}-*-Spec.xlsx'))
        for spec_path in spec_files:
            wb = load_workbook(str(spec_path), read_only=True)
            spec_sheet = None
            for n in wb.sheetnames:
                if 'spec' in n.lower() or 'field' in n.lower() or 'declaration' in n.lower():
                    spec_sheet = wb[n]
                    break
            if not spec_sheet:
                findings.append(f'{spec_path.name}: no spec sheet found')
                thin_count += 1
                continue
            headers = [str(c.value).lower() if c.value else ''
                       for c in next(spec_sheet.iter_rows(max_row=1))]
            matched = sum(1 for kw in STANDARD if any(kw in h for h in headers))
            findings.append(f'{spec_path.name}: {matched}/{len(STANDARD)} keywords')
            if matched < 12:
                thin_count += 1
        if thin_count == 0 and len(spec_files) > 0:
            return ('C12', 'PASS', f'All {len(spec_files)} specs have adequate schema', findings)
        elif thin_count <= 2:
            return ('C12', 'MANUAL', f'{thin_count}/{len(spec_files)} specs have thin schema', findings)
        return ('C12', 'FAIL', f'{thin_count}/{len(spec_files)} specs have thin schema', findings)
    except Exception as e:
        return ('C12', 'ERROR', str(e), [])

# ----- C21: Payslip 8-Sheet Structure (v2.7) -----
def c21():
    try:
        from openpyxl import load_workbook
        path = BASE / '06-payslip' / f'{CODE}_Compliance_Payslip_Generator.xlsx'
        if not path.exists():
            return ('C21', 'FAIL', f'File missing: {path.name}', [])
        wb = load_workbook(str(path), read_only=True)
        expected = ['How to set up Payslip', 'Compliance Payslip', f'{COUNTRY} (EN)', f'{COUNTRY} ({LOCAL_LANG})', 'Payslip Spec', 'Field Option', 'Population Range', 'Unit Rate Details']
        actual = wb.sheetnames
        missing = [s for s in expected if s not in actual]
        if not missing:
            return ('C21', 'PASS', 'All 8 sheets present', [])
        return ('C21', 'FAIL', f'Missing: {missing}', actual)
    except Exception as e:
        return ('C21', 'ERROR', str(e), [])

# ----- C22: Payslip Spec Coverage -----
def c22():
    try:
        from openpyxl import load_workbook
        path = BASE / '06-payslip' / f'{CODE}_Compliance_Payslip_Generator.xlsx'
        if not path.exists():
            return ('C22', 'FAIL', 'Payslip Generator missing', [])
        wb = load_workbook(str(path), read_only=True)
        if 'Payslip Spec' not in wb.sheetnames:
            return ('C22', 'FAIL', 'Payslip Spec sheet missing', [])
        ws = wb['Payslip Spec']
        required = ['Header Details', 'Employer', 'Employee', 'Earnings', 'Deductions']
        found = set()
        for row in ws.iter_rows(values_only=True):
            for cell in row:
                if cell is None: continue
                s = str(cell)
                for sec in required:
                    if sec.lower() in s.lower():
                        found.add(sec)
        missing = [s for s in required if s not in found]
        field_rows = sum(1 for row in ws.iter_rows(values_only=True) if any(c for c in row))
        if not missing and field_rows >= 20:
            return ('C22', 'PASS', f'All sections, {field_rows} rows', [])
        elif not missing:
            return ('C22', 'MANUAL', f'Sections present, only {field_rows} rows', [])
        return ('C22', 'FAIL', f'Missing sections: {missing}', [])
    except Exception as e:
        return ('C22', 'ERROR', str(e), [])

# ----- C20: Scope Decision Audit Trail -----
def c20():
    try:
        manifest_path = BASE / 'scope_manifest.json'
        if not manifest_path.exists():
            return ('C20', 'FAIL', 'scope_manifest.json missing', [])
        manifest = json.loads(manifest_path.read_text())
        in_scope = manifest.get('authority_filings', {}).get('in_scope', [])
        out_scope = manifest.get('authority_filings', {}).get('out_of_scope', [])
        # Check every in-scope filing has a spec file
        spec_dir = BASE / '04-reports-spec'
        spec_files = list(spec_dir.glob('*.xlsx')) if spec_dir.exists() else []
        missing_specs = []
        for filing in in_scope:
            fid = filing.get('filing_id', '')
            if not any(fid.lower().replace(' ', '') in s.name.lower().replace('_', '').replace('-', '') for s in spec_files):
                missing_specs.append(fid)
        # Check every out-of-scope has descoping reason
        missing_reasons = [f.get('filing_id', '') for f in out_scope if not f.get('descoping_reason')]
        if not missing_specs and not missing_reasons:
            return ('C20', 'PASS', f'{len(in_scope)} in-scope all specced, {len(out_scope)} descoped with reasons', [])
        issues = []
        if missing_specs: issues.append(f'In-scope without spec: {missing_specs}')
        if missing_reasons: issues.append(f'Out-of-scope without reason: {missing_reasons}')
        return ('C20', 'FAIL', '; '.join(issues), [])
    except Exception as e:
        return ('C20', 'ERROR', str(e), [])

# ----- C23: XML not applicable unless an XSD is cited (v2.7) -----
def c23():
    try:
        from openpyxl import load_workbook
        spec_dir = BASE / '04-reports-spec'
        if not spec_dir.exists():
            return ('C23', 'SKIP', 'No 04-reports-spec/', [])
        offenders = []
        for sp in sorted(spec_dir.glob(f'{CODE}-*-Spec.xlsx')):
            wb = load_workbook(str(sp), read_only=True)
            xml_hit = xsd_cited = False
            for ws in wb.worksheets:
                for row in ws.iter_rows(values_only=True):
                    for c in row:
                        if isinstance(c, str):
                            t = c.strip()
                            if t.startswith('<?xml') or t.startswith('<Declaration') or ('<Header>' in t and '</Header>' in t):
                                xml_hit = True
                            low = t.lower()
                            if 'xsd' in low or 'cahier des charges' in low or 'schema definition' in low:
                                xsd_cited = True
            if xml_hit and not xsd_cited:
                offenders.append(sp.name)
        if not offenders:
            return ('C23', 'PASS', 'No unsupported XML in specs', [])
        return ('C23', 'FAIL', f'XML present without an XSD citation: {offenders}', offenders)
    except Exception as e:
        return ('C23', 'ERROR', str(e), [])

# ----- C24: Portal / institution label correctness (v2.7) -----
def c24():
    try:
        from openpyxl import load_workbook
        spec_dir = BASE / '04-reports-spec'
        if not spec_dir.exists():
            return ('C24', 'SKIP', 'No 04-reports-spec/', [])
        offenders = []
        for sp in sorted(spec_dir.glob(f'{CODE}-*-Spec.xlsx')):
            name = sp.name.lower()
            is_ss = any(k in name for k in ('cnps', 'cnss', 'dnts', 'recap', 'appel'))
            is_tax = any(k in name for k in ('dgi', 'irpp', 'tfe', 'tafp', 'das', 'impot'))
            text = ''
            wb = load_workbook(str(sp), read_only=True)
            for ws in wb.worksheets:
                for row in ws.iter_rows(values_only=True):
                    for c in row:
                        if isinstance(c, str):
                            text += ' ' + c.lower()
            if is_ss and ('e-tax' in text or 'etax' in text):
                offenders.append(f'{sp.name}: social-security spec references the tax e-portal')
            if is_tax and ('e-cnps' in text or 'cnps portal' in text or 'cnps teledeclaration' in text):
                offenders.append(f'{sp.name}: tax spec references the social-security portal')
        if not offenders:
            return ('C24', 'PASS', 'Portal/institution labels consistent', [])
        return ('C24', 'FAIL', '; '.join(offenders), offenders)
    except Exception as e:
        return ('C24', 'ERROR', str(e), [])

# ----- C25: No fabricated Sample File (v2.7) -----
def c25():
    try:
        from openpyxl import load_workbook
        spec_dir = BASE / '04-reports-spec'
        samples_dir = BASE / '00-official-sources' / 'sample-files'
        has_official = samples_dir.exists() and any(samples_dir.iterdir())
        if not spec_dir.exists():
            return ('C25', 'SKIP', 'No 04-reports-spec/', [])
        offenders = []
        for sp in sorted(spec_dir.glob(f'{CODE}-*-Spec.xlsx')):
            wb = load_workbook(str(sp), read_only=True)
            if 'Sample File' not in wb.sheetnames:
                continue
            ws = wb['Sample File']
            xml_hit = False
            for row in ws.iter_rows(values_only=True):
                for c in row:
                    if isinstance(c, str) and c.strip().startswith('<'):
                        xml_hit = True
            if xml_hit and not has_official:
                offenders.append(sp.name)
        if not offenders:
            return ('C25', 'PASS', 'No fabricated Sample File detected', [])
        return ('C25', 'MANUAL', f'Sample File has XML but no official sample on disk — verify not fabricated: {offenders}', offenders)
    except Exception as e:
        return ('C25', 'ERROR', str(e), [])

# ----- C26: Payslip 8-sheet + formula hygiene + currency integer (v2.7) -----
def c26():
    try:
        from openpyxl import load_workbook
        ZERO_MINOR = {'XAF', 'XOF', 'JPY', 'KRW', 'CLP', 'ISK', 'VND', 'UGX', 'RWF', 'GNF', 'KMF', 'DJF', 'XPF', 'PYG', 'BIF'}
        path = BASE / '06-payslip' / f'{CODE}_Compliance_Payslip_Generator.xlsx'
        if not path.exists():
            return ('C26', 'FAIL', f'File missing: {path.name}', [])
        wb = load_workbook(str(path))
        issues = []
        expected = ['How to set up Payslip', 'Compliance Payslip', f'{COUNTRY} (EN)', f'{COUNTRY} ({LOCAL_LANG})', 'Payslip Spec', 'Field Option', 'Population Range', 'Unit Rate Details']
        missing = [s for s in expected if s not in wb.sheetnames]
        if missing:
            issues.append(f'missing sheets: {missing}')
        en = f'{COUNTRY} (EN)'
        if en in wb.sheetnames and CURRENCY in ZERO_MINOR:
            ws = wb[en]
            for row in ws.iter_rows():
                hit = False
                for c in row:
                    if c.number_format and '0.00' in c.number_format:
                        issues.append(f'{CURRENCY} amount with decimals at {c.coordinate} (must be integer)')
                        hit = True
                        break
                if hit:
                    break
        if not issues:
            return ('C26', 'PASS', '8-sheet structure + currency format OK', [])
        return ('C26', 'FAIL', '; '.join(issues), issues)
    except Exception as e:
        return ('C26', 'ERROR', str(e), [])

# ----- C27: DD <-> spec System Mapping resolution (v2.7) -----
def c27():
    try:
        from openpyxl import load_workbook
        spec_dir = BASE / '04-reports-spec'
        dd_path = BASE / '05-data-dictionary' / f'{CODE}-DD-001-v1.0.xlsx'
        if not spec_dir.exists() or not dd_path.exists():
            return ('C27', 'SKIP', 'specs or DD missing', [])
        ddwb = load_workbook(str(dd_path), read_only=True)
        dd_terms = set()
        for ws in ddwb.worksheets:
            for row in ws.iter_rows(values_only=True):
                for c in row:
                    if isinstance(c, str) and len(c.strip()) > 4:
                        dd_terms.add(c.strip().lower())
        DERIVED = ('derived', 'computed', 'system-generated', 'manual', 'free-text', 'free text', 'sequence', 'ordinal', 'sum(', 'round(')
        unresolved = []
        for sp in sorted(spec_dir.glob(f'{CODE}-*-Spec.xlsx')):
            wb = load_workbook(str(sp), read_only=True)
            for ws in wb.worksheets:
                if not ('spec' in ws.title.lower() or 'declaration' in ws.title.lower()):
                    continue
                for row in ws.iter_rows(min_row=2, values_only=True):
                    if len(row) < 12:
                        continue
                    sysmap = row[11]
                    if not isinstance(sysmap, str) or not sysmap.strip():
                        continue
                    low = sysmap.lower()
                    if any(k in low for k in DERIVED) or 'dd:' in low or 'data dictionary' in low:
                        continue
                    if any(term in low for term in dd_terms):
                        continue
                    unresolved.append(f'{sp.name}: "{str(sysmap)[:40]}"')
        if not unresolved:
            return ('C27', 'PASS', 'System Mappings resolve to DD or are classified', [])
        return ('C27', 'MANUAL', f'{len(unresolved)} mappings need a DD link or derived/structural class', unresolved[:10])
    except Exception as e:
        return ('C27', 'ERROR', str(e), [])

# ----- C28: Zero-minor-unit currency integer rule in specs (v2.7) -----
def c28():
    try:
        from openpyxl import load_workbook
        ZERO_MINOR = {'XAF', 'XOF', 'JPY', 'KRW', 'CLP', 'ISK', 'VND', 'UGX', 'RWF', 'GNF', 'KMF', 'DJF', 'XPF', 'PYG', 'BIF'}
        if CURRENCY not in ZERO_MINOR:
            return ('C28', 'PASS', f'{CURRENCY} has a minor unit — rule N/A', [])
        spec_dir = BASE / '04-reports-spec'
        if not spec_dir.exists():
            return ('C28', 'SKIP', 'No 04-reports-spec/', [])
        offenders = []
        for sp in sorted(spec_dir.glob(f'{CODE}-*-Spec.xlsx')):
            wb = load_workbook(str(sp), read_only=True)
            for ws in wb.worksheets:
                if not ('spec' in ws.title.lower() or 'declaration' in ws.title.lower()):
                    continue
                for row in ws.iter_rows(min_row=2, values_only=True):
                    if len(row) < 18:
                        continue
                    fmt, vtype = row[9], row[17]
                    if isinstance(fmt, str) and isinstance(vtype, str) and 'amount' in vtype.lower():
                        f = fmt.lower()
                        if 'n2.2' in f or 'v99' in f or '.99' in f or ',##0.00' in f:
                            offenders.append(f'{sp.name}: amount format "{fmt}" has decimals')
        if not offenders:
            return ('C28', 'PASS', f'{CURRENCY} amount formats are integer', [])
        return ('C28', 'FAIL', '; '.join(offenders[:8]), offenders)
    except Exception as e:
        return ('C28', 'ERROR', str(e), [])

# ----- C29: Residual-marker lint across ALL artifacts (v2.8, B3) -----
def c29():
    """B3: no unfinished-work marker may survive to final in the CCG, the report specs,
       the WTC or the DD. Deterministic FAIL. Complements C8 (CCG-only)."""
    try:
        import re as _re
        markers_re = [r'\bTODO\b', r'\bTBD\b', r'\bFIXME\b',
                      r'\bVERIFY\s+No\b', r'\[\s*placeholder\s*\]',
                      r'\[\s*CHECK\s*\]', r'\[\s*\?\s*\]']
        markers_phrase = ['to be confirmed', 'to be verified']
        hits = []
        def scan_text(text, label):
            for pat in markers_re:
                if _re.search(pat, text, _re.IGNORECASE):
                    hits.append(f'{label}: {pat}')
            low = text.lower()
            for ph in markers_phrase:
                if ph in low:
                    hits.append(f'{label}: "{ph}"')
        try:
            from docx import Document
            for ccg in sorted((BASE / '01-ccg').glob(f'{CODE}-CCG-001-v1*.docx')):
                scan_text('\n'.join(p.text for p in Document(str(ccg)).paragraphs), ccg.name)
        except Exception:
            pass
        try:
            from openpyxl import load_workbook
            for d, g in [(BASE / '04-reports-spec', f'{CODE}-*-Spec.xlsx'),
                         (BASE / '02-wtc', f'{CODE}-WTC-001-v1*.xlsx'),
                         (BASE / '05-data-dictionary', f'{CODE}-DD-001-v1*.xlsx')]:
                for f in sorted(d.glob(g)):
                    wb = load_workbook(str(f), read_only=True, data_only=True)
                    for ws in wb.worksheets:
                        for row in ws.iter_rows(values_only=True):
                            for v in row:
                                if isinstance(v, str):
                                    scan_text(v, f'{f.name}[{ws.title}]')
                    wb.close()
        except Exception:
            pass
        hits = sorted(set(hits))
        if not hits:
            return ('C29', 'PASS', 'No residual placeholder/TODO/VERIFY-No markers in any artifact', [])
        return ('C29', 'FAIL', f'{len(hits)} residual marker(s) across artifacts', hits[:20])
    except Exception as e:
        return ('C29', 'ERROR', str(e), [])

# ----- C30: Source-tier flag (v2.8, B5) -----
def c30():
    """B5: a figure whose only cited source is a tier-3 aggregator must be backed by an
       A.1/A.2 official source. Deterministic detection of known aggregator domains -> MANUAL."""
    try:
        AGG = ['51shebao', 'pwc.', 'china-briefing', 'chinabriefing', 'wikipedia',
               'investopedia', 'expatica', 'tradingeconomics', 'kpmg', 'deloitte',
               'ey.com', 'mercer', 'statista']
        found = []
        try:
            from docx import Document
            for ccg in sorted((BASE / '01-ccg').glob(f'{CODE}-CCG-001-v1*.docx')):
                t = '\n'.join(p.text for p in Document(str(ccg)).paragraphs).lower()
                for a in AGG:
                    if a in t:
                        found.append(f'{ccg.name}: {a}')
        except Exception:
            pass
        try:
            from openpyxl import load_workbook
            for d, g in [(BASE / '04-reports-spec', f'{CODE}-*-Spec.xlsx'),
                         (BASE / '02-wtc', f'{CODE}-WTC-001-v1*.xlsx'),
                         (BASE / '05-data-dictionary', f'{CODE}-DD-001-v1*.xlsx')]:
                for f in sorted(d.glob(g)):
                    wb = load_workbook(str(f), read_only=True, data_only=True)
                    for ws in wb.worksheets:
                        for row in ws.iter_rows(values_only=True):
                            for v in row:
                                if isinstance(v, str):
                                    low = v.lower()
                                    for a in AGG:
                                        if a in low:
                                            found.append(f'{f.name}: {a}')
                                            break
                    wb.close()
        except Exception:
            pass
        found = sorted(set(found))
        if not found:
            return ('C30', 'PASS', 'No tier-3 aggregator sources detected', [])
        return ('C30', 'MANUAL',
                f'{len(found)} tier-3 source citation(s) — confirm an official A.1/A.2 source backs each figure',
                found[:15])
    except Exception as e:
        return ('C30', 'ERROR', str(e), [])

# ----- C31: Resident vs non-resident coverage (v2.8, B1) -----
def c31():
    """B1: the income-tax module must address BOTH resident and non-resident treatment.
       If 'non-resident' is entirely absent where income tax is discussed -> MANUAL."""
    try:
        from docx import Document
        ccgs = sorted((BASE / '01-ccg').glob(f'{CODE}-CCG-001-v1*.docx'))
        if not ccgs:
            return ('C31', 'SKIP', 'CCG not found', [])
        t = '\n'.join(p.text for p in Document(str(ccgs[-1])).paragraphs).lower()
        mentions_tax = any(k in t for k in ['income tax', 'withhold', 'irpp', 'iit', 'paye',
                                            'retenue', 'impot sur le revenu', 'impôt sur le revenu'])
        has_nonres = any(k in t for k in ['non-resident', 'nonresident', 'non resident',
                                          'non-résident', 'non résident'])
        has_res = ('resident' in t) or ('résident' in t)
        if not mentions_tax:
            return ('C31', 'SKIP', 'No income-tax content detected', [])
        if has_res and has_nonres:
            return ('C31', 'PASS', 'Both resident and non-resident treatment present', [])
        if not has_nonres:
            return ('C31', 'MANUAL',
                    'No non-resident treatment in the income-tax module — fill the resident/non-resident matrix from primary law or state out-of-scope (B1)',
                    [])
        return ('C31', 'MANUAL', 'Resident/non-resident coverage looks incomplete — verify the matrix (B1)', [])
    except Exception as e:
        return ('C31', 'ERROR', str(e), [])

# ----- C32: Cross-artifact fact consistency (v2.9, deterministic) -----
def c32():
    """Deterministic cross-artifact consistency: every [[FACT:key=value]] tag is
       collected across ALL artifacts, keys validated against shared/fact-keys.yaml,
       grouped by key. If one key holds >1 distinct value across artifacts -> FAIL
       (the audit turns any FAIL into BLOCKED, so this blocks the build).
       Prose contradictions with no differing tag are NOT this check's job — the
       consistency-verifier subagent (semantic, report-only) covers those."""
    try:
        import re as _re, csv as _csv, glob as _glob
        REG = SHARED / 'fact-keys.yaml'
        tag_re = _re.compile(r'\[\[FACT:\s*([A-Za-z0-9_]+)\s*=\s*([^\]]+?)\s*\]\]')

        # -- mini-YAML reader scoped to fact-keys.yaml shape (no PyYAML dep) --
        def load_registry(path):
            allowed = {}
            if not path.exists():
                return allowed, 'registry-absent'
            in_keys = False; cur = None; attr = {}
            def _ind(s): return len(s) - len(s.lstrip(' '))
            def _flush():
                if cur is not None and attr.get('type'):
                    allowed[cur] = dict(attr)
            for raw in path.read_text(encoding='utf-8').splitlines():
                if not raw.strip() or raw.lstrip().startswith('#'):
                    continue
                ind = _ind(raw); s = raw.strip()
                if ind == 0:
                    in_keys = (s.rstrip(':') == 'keys'); continue
                if not in_keys:
                    continue
                if ind == 2 and s.endswith(':'):
                    _flush(); cur = None; attr = {}; continue
                if ind == 4 and s.endswith(':'):
                    _flush(); cur = s[:-1].strip(); attr = {}; continue
                if ind >= 6 and cur is not None and ':' in s:
                    k, _, v = s.partition(':'); k = k.strip(); v = v.strip().strip('"').strip("'")
                    if k == 'allowed':
                        attr['allowed'] = [x.strip().strip('"').strip("'")
                                           for x in v.strip('[]').split(',') if x.strip()]
                    else:
                        attr[k] = v
            _flush()
            return allowed, None

        def _norm(value, decl):
            t = (decl or {}).get('type', 'str'); v = value.strip()
            try:
                if t == 'bool':
                    return (v.lower(), None) if v.lower() in ('true', 'false') else (v, 'bool?')
                if t == 'int':
                    return (str(int(v)), None) if _re.fullmatch(r'-?\d+', v) else (v, 'int?')
                if t in ('money', 'pct'):
                    if _re.fullmatch(r'-?\d+(\.\d+)?', v) is None:
                        return v, 'num?'
                    s = ('%.6f' % float(v)).rstrip('0').rstrip('.')
                    return (s if s else '0'), None
                if t == 'enum':
                    al = (decl or {}).get('allowed', [])
                    return (v, None) if (not al or v in al) else (v, 'enum?')
                return v, None
            except Exception:
                return v, 'norm?'

        allowed, reg_err = load_registry(REG)

        # -- collect tags across artifacts --
        occ = {}      # key -> list of (file, raw, norm)
        unknown = []
        def _scan(text, label):
            for m in tag_re.finditer(text):
                k = m.group(1).strip(); raw = m.group(2).strip()
                decl = allowed.get(k)
                norm = raw if decl is None else _norm(raw, decl)[0]
                if decl is None:
                    unknown.append((k, label))
                occ.setdefault(k, []).append((label, raw, norm))

        try:
            from docx import Document
            for ccg in sorted((BASE / '01-ccg').glob(f'{CODE}-CCG-001-v1*.docx')):
                doc = Document(str(ccg))
                _scan('\n'.join(p.text for p in doc.paragraphs), ccg.name)
                for tbl in doc.tables:
                    for row in tbl.rows:
                        for cell in row.cells:
                            if cell.text:
                                _scan(cell.text, ccg.name)
        except Exception:
            pass
        try:
            from openpyxl import load_workbook
            xlsx_specs = [(BASE / '04-reports-spec', f'{CODE}-*-Spec.xlsx'),
                          (BASE / '02-wtc', f'{CODE}-WTC-001-v1*.xlsx'),
                          (BASE / '05-data-dictionary', f'{CODE}-DD-001-v1*.xlsx')]
            for d, g in xlsx_specs:
                for f in sorted(d.glob(g)):
                    wb = load_workbook(str(f), read_only=True, data_only=True)
                    for ws in wb.worksheets:
                        for row in ws.iter_rows(values_only=True):
                            for v in row:
                                if isinstance(v, str):
                                    _scan(v, f.name)
                    wb.close()
        except Exception:
            pass
        # SIR + any markdown artifacts
        for md in _glob.glob(str(BASE / '**' / '*.md'), recursive=True):
            bn = os.path.basename(md)
            if bn.startswith('FACT-'):
                continue
            try:
                _scan(Path(md).read_text(encoding='utf-8', errors='replace'), bn)
            except Exception:
                pass

        # -- detect conflicts --
        conflicts = []
        for k, lst in sorted(occ.items()):
            distinct = sorted(set(n for (_f, _r, n) in lst))
            if len(distinct) > 1:
                conflicts.append((k, distinct, lst))

        # -- write reports to logs --
        try:
            LOGS = BASE / 'logs'; LOGS.mkdir(exist_ok=True)
            with open(LOGS / 'FACT-CONFLICTS.csv', 'w', newline='', encoding='utf-8') as fh:
                w = _csv.writer(fh)
                w.writerow(['type', 'fact_key', 'file', 'value', 'all_values_for_key'])
                for k, distinct, lst in conflicts:
                    allv = '|'.join(distinct)
                    for (f, r, n) in lst:
                        w.writerow(['conflict', k, f, r, allv])
                for (k, f) in unknown:
                    w.writerow(['unknown_key', k, f, '', ''])
            md = ['# Cross-Artifact Fact Consistency (deterministic, C32)', '']
            md.append('CONFLICTS FOUND — BUILD BLOCKED' if conflicts else 'PASS — no deterministic conflicts')
            md.append('')
            for k, distinct, lst in conflicts:
                md.append(f'## `{k}` -> {distinct}')
                for (f, r, n) in lst:
                    md.append(f'- `{f}` = **{r}**')
                md.append('')
            (LOGS / 'FACT-CONFLICTS.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
        except Exception:
            pass

        total_tags = sum(len(v) for v in occ.values())
        if not occ:
            return ('C32', 'PASS', 'No [[FACT:]] tags present (country pre-dates tagging) — semantic verifier still applies', [])
        if conflicts:
            items = [f'{k}: ' + ' vs '.join(d) for (k, d, _l) in conflicts][:20]
            return ('C32', 'FAIL',
                    f'{len(conflicts)} cross-artifact fact conflict(s) across {total_tags} tags — see logs/FACT-CONFLICTS.md',
                    items)
        note = f'{total_tags} fact tags, {len(occ)} keys, all consistent'
        if reg_err == 'registry-absent':
            note += ' (registry absent — key names NOT validated)'
        elif unknown:
            note += f'; {len(set(k for k,_ in unknown))} unknown key(s) — add to shared/fact-keys.yaml'
        return ('C32', 'PASS', note, [])
    except Exception as e:
        return ('C32', 'ERROR', str(e), [])

# ----- C33: CCG English-only prose (v2.9, detective; MANUAL -> fixer translates) -----
def c33():
    """The CCG narrative must be English-only prose. Local-language words that leak into
       sentences/cells (the Mohit complaint) are flagged. Detection is deterministic and
       dependency-free: (a) any non-Latin script (Arabic/Urdu/etc.) via Unicode range is a
       zero-false-positive signal; (b) for Latin-script local languages, a CURATED set of
       high-frequency FUNCTION words per language that do NOT collide with English.
       Text inside parentheses or quotes is EXCLUDED from scanning — that is the permitted
       'English wording (original term)' citation form from control B10. Proper nouns of
       authorities/forms are unavoidable and not reliably separable, so this is MANUAL, not
       FAIL: it never blocks the build; the content-audit fixer translates the flagged prose.
       SCOPE: CCG prose ONLY. The DD/WTC/Payslip local-language fields are by design and are
       never scanned here."""
    try:
        import re as _re
        # Function-word stoplists, curated to avoid English collisions.
        # (Deliberately omit ambiguous tokens: es 'son'/'el', fr 'a', it 'e'/'a', pt 'e'/'a'/'o'.)
        STOP = {
            'French':     ['le','la','les','des','une','du','dans','pour','avec','sur','sont',
                           'aux','cette','être','leur','selon','ainsi','entre','chaque','doit',
                           'aucun','lorsque','n\u2019est','c\u2019est','qui','que','plus'],
            'Spanish':    ['los','las','una','del','con','para','por','que','como','este','esta',
                           'estos','estas','debe','cada','entre','segun','cuando','mas','sobre'],
            'Portuguese': ['os','as','uma','das','dos','com','para','por','que','como','este',
                           'esta','estes','estas','deve','cada','entre','segundo','quando','sobre'],
            'Italian':    ['il','lo','gli','una','del','della','con','per','che','come','questo',
                           'questa','deve','ogni','tra','quando','sopra','degli','delle'],
            'German':     ['der','die','das','und','den','dem','des','ein','eine','fur','mit',
                           'auf','ist','sind','oder','nicht','auch','werden','muss','jeder'],
            'Dutch':      ['de','het','een','en','van','voor','met','zijn','wordt','niet','elke',
                           'moet','tussen','volgens','wanneer'],
            'Hungarian':  ['az','egy','nem','van','vagy','minden','kell','között','szerint'],
            'Bulgarian':  [],   # Cyrillic — caught by the non-Latin script test below
        }
        lang = COUNTRY and None  # placeholder; real language comes from env-injected LANGUAGE
        # LANGUAGE isn't injected into the audit env; derive from LOCAL_LANG short code.
        SHORT2LANG = {'FR':'French','ES':'Spanish','PT':'Portuguese','IT':'Italian',
                      'DE':'German','NL':'Dutch','HU':'Hungarian','BG':'Bulgarian'}
        lang = SHORT2LANG.get(LOCAL_LANG, None)

        try:
            from docx import Document
        except Exception:
            return ('C33', 'SKIP', 'python-docx unavailable', [])
        ccgs = sorted((BASE / '01-ccg').glob(f'{CODE}-CCG-001-v1*.docx'))
        if not ccgs:
            return ('C33', 'SKIP', 'CCG not found', [])
        doc = Document(str(ccgs[-1]))

        # gather prose strings (paragraphs + table cells)
        strings = [p.text for p in doc.paragraphs if p.text]
        for tbl in doc.tables:
            for row in tbl.rows:
                for cell in row.cells:
                    if cell.text:
                        strings.append(cell.text)

        paren_re = _re.compile(r'\([^)]*\)')      # strip "(...)" — permitted citation form
        quote_re = _re.compile(r'"[^"]*"|\u201c[^\u201d]*\u201d|\u2018[^\u2019]*\u2019|\'[^\']*\'')
        # non-Latin letter (excludes basic Latin, Latin-1 accents, punctuation, digits, common symbols)
        nonlatin_re = _re.compile(r'[^\x00-\x7F\u00C0-\u017F\s\d\.,;:%\-\u2013\u2014\(\)\[\]/&\'\u2018\u2019\u201c\u201d"°+*=]')

        hits = []
        def clean(s):
            s = paren_re.sub(' ', s)
            s = quote_re.sub(' ', s)
            return s

        for s in strings:
            scan = clean(s)
            # (a) non-Latin script anywhere in unquoted prose
            if nonlatin_re.search(scan):
                sample = s.strip()
                hits.append(('non-latin-script', sample[:80]))
                continue
            # (b) curated function-word test for the country's Latin-script language
            if lang and STOP.get(lang):
                toks = _re.findall(r"[A-Za-z\u00C0-\u017F\u2019']+", scan.lower())
                tokset = set(toks)
                found = [w for w in STOP[lang] if w in tokset]
                # require >=2 distinct function words in one string to reduce noise
                if len(found) >= 2:
                    hits.append((f'{lang}:' + ','.join(found[:5]), s.strip()[:80]))

        # de-dup, cap
        seen = set(); uniq = []
        for tag, sample in hits:
            key = (tag, sample)
            if key in seen:
                continue
            seen.add(key); uniq.append(f'[{tag}] {sample}')
        if not uniq:
            return ('C33', 'PASS', 'CCG prose is English-only (no local-language leakage detected)', [])
        return ('C33', 'MANUAL',
                f'{len(uniq)} possible local-language passage(s) in CCG prose — content-audit fixer must translate to English (keep statutory term in parentheses on first use, per B10)',
                uniq[:20])
    except Exception as e:
        return ('C33', 'ERROR', str(e), [])

# Run all checks
for fn in [c1, c8, c11, c12, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33]:
    check, verdict, detail, items = fn()
    results.append({
        'check': check,
        'verdict': verdict,
        'detail': detail,
        'items': items,
    })

verdicts = [r['verdict'] for r in results]
fails = sum(1 for v in verdicts if v == 'FAIL')
manuals = sum(1 for v in verdicts if v == 'MANUAL')
passes = sum(1 for v in verdicts if v == 'PASS')

overall = 'READY_FOR_HANDOVER' if fails == 0 else 'BLOCKED'

output = {
    'overall': overall,
    'summary': {'PASS': passes, 'MANUAL': manuals, 'FAIL': fails},
    'checks': results,
}
print(json.dumps(output, indent=2))
PYEOF

echo "  Running mechanical audit checks..."
CL_AUDIT_CODE="$CODE" CL_AUDIT_COUNTRY="$COUNTRY" CL_AUDIT_LOCAL_LANG_SHORT="$LOCAL_LANG_SHORT" CL_AUDIT_CURRENCY="$CURRENCY" \
    python3 "$BASE/_audit_v24_mechanical.py" > "$LOGS/audit_v24_mechanical.json" 2>&1 || true
cat "$LOGS/audit_v24_mechanical.json"

# Run content audit with self-aware fixer (overrides false positives with justification)
cat > "$PROMPTS/audit_content.md" << AUDITEOF
# ${COUNTRY} PRE-SUBMISSION AUDIT — CONTENT REVIEW + HANDOVER STATUS

You are the Pre-Submission Audit Gate for ${COUNTRY} v2.4 build.

## INPUTS

1. Mechanical audit results: ~/mercans-pipeline/${CODE}-compliance/logs/audit_v24_mechanical.json
2. Audit reference: ~/mercans-pipeline/shared/PRESUBMISSION_AUDIT.md (C1-C22)
3. Failure log: ~/mercans-pipeline/shared/country_failure_log.md (F1-F15)
4. All artifacts in ~/mercans-pipeline/${CODE}-compliance/
5. Country failure log to check against

## YOUR TASK

1. Read the mechanical audit results.
2. For each FAIL or MANUAL, investigate the actual artifact:
   - Open the file
   - Find the flagged issue in context
   - Determine if it's a real problem or a false positive

3. **FALSE POSITIVE HANDLING** (proven on Chile v2.4):
   If a mechanical check FAILS but manual inspection reveals the failure is
   a false positive (e.g., audit matched a substring inside non-English terms,
   or flagged a structurally valid pattern as invalid), you may OVERRIDE the
   verdict with written justification.
   
   Examples of valid overrides:
   - "C8 flagged 'TODO' but the 4 hits are all inside Spanish legal phrase
     'a todo evento' (Art. 164 CdT severance fund), not English open-item markers"
   - "C12 reports thin schema but ${COUNTRY}'s tax authority publishes only
     12 column requirements; thin schema is justified per the official spec"

4. **REAL FAILURE HANDLING:**
   If a FAIL is genuine, attempt to fix the artifact:
   - For C8 real markers: search for TBD/TODO/FIXME and resolve from sources
   - For C11 thin coverage: add missing H3 headings + answers from CCG content
   - For C12 thin schema: extract columns from source PDFs and add to spec
   - For C20 missing specs: generate the missing spec
   - For C21 wrong sheets: rename/add sheets in payslip
   - For C22 thin spec: expand sections with WTC/DD content
   - For C33 CCG local-language leakage (MANUAL): open the CCG and TRANSLATE every
     flagged local-language passage into English. Rules:
       * The CCG PROSE must end up English-only (headings, sentences, table cells,
         worked examples, notes).
       * Preserve a genuine statutory/legal term of art by putting the English wording
         first and the original term in parentheses on FIRST use only, e.g.
         "professional expenses (frais professionnels)". After first use, English alone.
       * Keep official proper names of authorities/forms/statutes as-is (e.g.
         "Direction Générale des Impôts (DGI)") — those are proper nouns, not prose.
       * Verify each C33 hit in context first: a hit that is ONLY an official proper
         name or an already-parenthesised citation is a false positive — record it as an
         override, do not "translate" a proper noun.
       * This applies to the CCG ONLY. Do NOT touch the DD/WTC/Payslip local-language
         fields — the "Name Local (${LANGUAGE})" columns and the
         "${COUNTRY} (${LOCAL_LANG_SHORT})" payslip sheet are correct by design.
       * After translating, add a Version Control entry in the CCG for the language pass
         (same session), consistent with how every other edit is logged.

5. After all fixes attempted, re-run the mechanical audit:
   python3 ~/mercans-pipeline/${CODE}-compliance/_audit_v24_mechanical.py > /tmp/audit_recheck.json
   Compare to original results.

## OUTPUT

Save handover_status.md to:
~/mercans-pipeline/${CODE}-compliance/07-qa-crosscheck/handover_status.md

Structure:

\`\`\`markdown
# Pre-Submission Audit — ${COUNTRY} v2.4

**Overall verdict:** READY_FOR_HANDOVER | BLOCKED (with reason)

**Mechanical audit raw result:** [PASS/MANUAL/FAIL summary]

## Artifacts produced
| Artifact | File | Size |
|---|---|---|
| CCG | 01-ccg/${CODE}-CCG-001-v1.0.docx | XX KB |
| Report Specs | 04-reports-spec/ | N files |
| DD | 05-data-dictionary/${CODE}-DD-001-v1.0.xlsx | XX KB |
| WTC | 02-wtc/${CODE}-WTC-001-v1.0.xlsx | XX KB |
| SIR index | 03-statutory-integrations/${CODE}-SIR-INDEX-001-v1.0.docx | XX KB |
| Integration runbooks | 03-statutory-integrations/<AUTH>/ (per-authority, via si-runbook) | — |
| Payslip | 06-payslip/${CODE}_Compliance_Payslip_Generator.xlsx | XX KB |

## Audit results (C1-C22)
[Render the JSON as a readable table]

## False positives identified
[For each override, explain WHY the FAIL is not a real issue + cite specific
paragraphs/cells. Tag with check ID, e.g., "C8 override: ..."]

## Real fixes applied
[For each genuine FAIL fixed: what was wrong, what you changed]

## Remaining issues (if any)
[FAILs that couldn't be fixed — escalate to manual review]

## Sign-off recommendation
[Either READY_FOR_HANDOVER or BLOCKED with required actions]

## Next steps
1. Open the artifacts and review
2. Apply any manual fixes flagged above
3. If READY: share with dev team
4. Append any new failure patterns to ~/mercans-pipeline/shared/country_failure_log.md
\`\`\`
AUDITEOF

STAGE9_START=$(date +%s)
if [ "$GENERATE_PROMPTS_ONLY" = "true" ]; then
    echo "  [PROMPTS-ONLY mode] Skipping content audit + fixer execution"
else
    echo "  Running content audit + fixer..."
    claude -p "$(cat "$PROMPTS/audit_content.md")" \
           --max-turns 80 \
           --dangerously-skip-permissions \
           > "$LOGS/audit_content.log" 2>&1
fi
STAGE9_END=$(date +%s)
STAGE9_DURATION=$((STAGE9_END - STAGE9_START))
echo "  Audit done in ${STAGE9_DURATION}s ($((STAGE9_DURATION / 60)) min)"

STATUS_FILE="$BASE/07-qa-crosscheck/handover_status.md"
if [ -f "$STATUS_FILE" ]; then
    head -10 "$STATUS_FILE"
fi
# v2.5 R1 — stage completion summary
echo "  STAGE 9 SUMMARY: audit complete, see $BASE/07-qa-crosscheck/handover_status.md"
echo ""

# Don't halt on BLOCKED — let user decide based on content audit's reasoning
# (content audit may override false positives, e.g., the Chile "todo" case)
fi  # end stage_skip_check 9

# =============================================================================
# STAGE 10 — QA Cross-Check (final consistency review)
# =============================================================================
if stage_skip_check 10 "QA Cross-Check"; then
echo "----------------------------------------------------------------"
echo "STAGE 10/11 — QA Cross-Check (final consistency + Global WTC coverage)"
echo "Est. 15-25 min"
echo "----------------------------------------------------------------"

cat > "$PROMPTS/qa.md" << QAEOF
# ${COUNTRY} QA CROSS-CHECK — v2.4 STANDARDS

## STEP 0 — REUSE PRIOR EXTRACTION WORK IF PRESENT (a prior run of this exact
## stage may have been interrupted partway through)

Check ~/mercans-pipeline/${CODE}-compliance/07-qa-crosscheck/_work/ FIRST.
If it already contains text dumps of the artifacts (ccg.txt, wtc.txt, dd.txt,
spec_*.txt, payslip.txt, sir.txt, gwtc.txt) and/or structured intermediates
(dd_blob.json, dd_fields.json, spec_rows.json), those are already-extracted,
reusable raw material from an interrupted prior attempt — read them directly
instead of re-running dump_docx.py / dump_xlsx.py or re-parsing the source
files from scratch. Only regenerate a specific dump if it's genuinely missing
or you have concrete reason to believe it's stale (a source artifact was
modified more recently than the dump). Extraction burned most of the turn
budget last time before any actual cross-check analysis happened — reusing it
is what makes room for the analysis and the final report this time.

Audit all artifacts for consistency, completeness, and v2.4 compliance.

## READ ALL ARTIFACTS
CCG:          ~/mercans-pipeline/${CODE}-compliance/01-ccg/${CODE}-CCG-001-v1.0.docx
Report Specs: ~/mercans-pipeline/${CODE}-compliance/04-reports-spec/
DD:           ~/mercans-pipeline/${CODE}-compliance/05-data-dictionary/${CODE}-DD-001-v1.0.xlsx
WTC:          ~/mercans-pipeline/${CODE}-compliance/02-wtc/${CODE}-WTC-001-v1.0.xlsx
SIR index:    ~/mercans-pipeline/${CODE}-compliance/03-statutory-integrations/${CODE}-SIR-INDEX-001-v1.0.docx (runbooks: <AUTH>/ via si-runbook)
Payslip:      ~/mercans-pipeline/${CODE}-compliance/06-payslip/${CODE}_Compliance_Payslip_Generator.xlsx
scope_manifest: ~/mercans-pipeline/${CODE}-compliance/scope_manifest.json
Global WTC:   ~/mercans-pipeline/shared/Global_WTC_V1_0.xlsx

## CHECKS

### 1. CCG ↔ WTC alignment
Every wage type in CCG Modules 3-9 must exist in WTC with matching tax/SS treatment.
Score: X of Y matched.

### 2. CCG ↔ DD alignment
Every field in CCG Module 2 must exist in DD.

### 3. CCG ↔ Report Specs alignment
Every report in CCG Module 10 must have a matching Report Spec xlsx.

### 4. DD ↔ Report Specs alignment (4-BUCKET METHOD)
Classify each spec field as: DD / TX / CALC / SYS
Only DD-bucket fields must be in DD. TX/CALC/SYS correctly excluded.
Score: X of Y DD-bucket fields found in DD = Z% alignment.
NOTE: Do NOT penalize for TX/CALC/SYS fields not being in DD.

### 5. Global WTC coverage audit
Check "Global WTC Coverage" sheet in WTC file against Global_WTC_V1_0.xlsx.
Report: X included, Y excluded with reasons, Z% coverage.

### 6. Scope discipline
- No calculated amounts or Base Salary in DD
- No identification data in WTC
- No full field specs in CCG Module 2 or 10

### 7. Report Spec format compliance (per report)
- Exactly 9 sheets with correct names
- Sheet 4 has 21 columns A-U with correct headers
- Header row is blue FF4472C4, white, bold
- Row colors applied (amber/blue/green/red/grey)
- Payroll Scope Summary has green/red coloring
- Population Rules sheet completed

### 8. v2.4 standards
- CCG uses 13 official modules with exact titles AND template Q&A format (H3 headings)
- DD uses CZ V2.0 format, blue columns only
- WTC uses CZ V2.0 + Global WTC baseline + Form Reference Guide sheet
- Report Specs use Spain 9-sheet format with 21-column Sheet 4
- Payslip uses the 8-sheet Mercans standard, navy/grey palette, green net-pay

### 9. v2.4 NEW — Composite key / Inter-field constraints
- Composite-key fields documented in Sheet 4 column M (C13)
- Conditional fields have bidirectional documentation (C16)
- Form Reference Guide present in WTC (C17)
- Scope decision audit trail complete (C20)

## OUTPUT
Save to: ~/mercans-pipeline/${CODE}-compliance/07-qa-crosscheck/${CODE}-QA-REPORT.md

Include:
- Executive summary (overall score /100)
- Per-check alignment scores
- Issues list with severity: CRITICAL / MAJOR / MINOR + fix recommendation
- Global WTC coverage summary
- v2.4 compliance summary
- Readiness verdict: READY FOR DEV TEAM / NEEDS PATCHES / MAJOR REWORK
QAEOF

echo "  Prompt written: $PROMPTS/qa.md"
STAGE10_START=$(date +%s)
if [ "$GENERATE_PROMPTS_ONLY" = "true" ]; then
    echo "  [PROMPTS-ONLY mode] Skipping QA execution"
else
    echo "  Running QA agent..."
    run_claude_or_skip "$PROMPTS/qa.md" "$LOGS/qa.log" 180
fi
STAGE10_END=$(date +%s)
STAGE10_DURATION=$((STAGE10_END - STAGE10_START))
echo "  QA done in ${STAGE10_DURATION}s ($((STAGE10_DURATION / 60)) min)"
# v2.5 R1 — stage completion summary
if [ -f "$BASE/07-qa-crosscheck/${CODE}-QA-REPORT.md" ]; then
    echo "  STAGE 10 SUMMARY: QA report produced at 07-qa-crosscheck/${CODE}-QA-REPORT.md"
fi
echo ""
fi  # end stage_skip_check 10


# =============================================================================
# STAGE 11 — Skill Generator (country compliance skill file)
# =============================================================================
if stage_skip_check 11 "Skill Generator"; then
echo "----------------------------------------------------------------"
echo "STAGE 11/11 — Skill Generator (compliance skill file)"
echo "Est. 20-40 min"
echo "----------------------------------------------------------------"

SKILL_DIR="$BASE/08-skill/${CODE_LC}-compliance"
mkdir -p "$SKILL_DIR"
mkdir -p "$SKILL_DIR/references"
# v2.7 — remove legacy flat-format files so a re-run ends in clean router shape
rm -f "$SKILL_DIR/statutory_rates.json" "$SKILL_DIR/filing_calendar.md" "$SKILL_DIR/quick_reference.md"

cat > "$PROMPTS/skill.md" << SKILLEOF
# ${COUNTRY} COMPLIANCE SKILL — GENERATOR (router pattern, v2.7)

You are generating a Mercans payroll-compliance skill for ${COUNTRY}, in the
Chile "progressive-disclosure router" pattern: a THIN SKILL.md that routes to
one FULL reference file per artifact. It is uploaded to claude.ai and used by
compliance analysts. Faithful, COMPLETE content is the priority — do NOT
summarize.

## STEP 0 — REUSE STAGE 10'S ALREADY-EXTRACTED TEXT DUMPS IF PRESENT

Check ~/mercans-pipeline/${CODE}-compliance/07-qa-crosscheck/_work/ FIRST. The
QA Cross-Check stage that just ran typically leaves plain-text dumps of every
artifact there (ccg.txt, wtc.txt, dd.txt, spec_*.txt, payslip.txt, sir.txt,
gwtc.txt) — read those directly instead of re-opening and re-parsing the
source .docx/.xlsx files yourself. They are current (produced this same
pipeline run) and reading plain text is far cheaper than re-parsing binary
files field-by-field. Only fall back to reading a source artifact directly if
its dump is missing from that folder. A prior attempt at this exact stage
spent its entire turn budget reading and produced no output file at all —
reusing the dumps is what leaves room to actually write the skill this time.

## STEP 1 — READ ALL SOURCE ARTIFACTS (use the LATEST version present)
In each folder, read the HIGHEST version number present (e.g. v1.2 over v1.0).
Do NOT assume a specific version in the filename — list the folder and pick the
newest. Read EVERY sheet of every workbook.
  CCG:          ~/mercans-pipeline/${CODE}-compliance/01-ccg/                          (${CODE}-CCG-001-*.docx)
  WTC:          ~/mercans-pipeline/${CODE}-compliance/02-wtc/                          (${CODE}-WTC-001-*.xlsx)
  SIR:          ~/mercans-pipeline/${CODE}-compliance/03-statutory-integrations/       (${CODE}-SIR-001-*.docx)
  Report Specs: ~/mercans-pipeline/${CODE}-compliance/04-reports-spec/                 (EVERY *-Spec.xlsx)
  DD:           ~/mercans-pipeline/${CODE}-compliance/05-data-dictionary/              (${CODE}-DD-001-*.xlsx)
  Payslip:      ~/mercans-pipeline/${CODE}-compliance/06-payslip/                      (${CODE}_Compliance_Payslip_Generator.xlsx)
  QA Report:    ~/mercans-pipeline/${CODE}-compliance/07-qa-crosscheck/${CODE}-QA-REPORT.md

## STEP 2 — WRITE ONE FULL REFERENCE FILE PER ARTIFACT
Create these in ~/mercans-pipeline/${CODE}-compliance/08-skill/${CODE_LC}-compliance/references/ :
  01-ccg.md             - the ENTIRE CCG: every section, rate, table, bracket,
                          and leave / overtime / termination rule, with all legal
                          citations. Verbatim values.
  02-wtc.md             - the ENTIRE wage type catalogue: one row per wage type
                          (code, name, type, tax and SS treatment, accumulators),
                          rendered as markdown tables. Every code, no omissions.
  03-sir.md             - the ENTIRE statutory-integration research: each
                          institution, portal, channel, authentication, file
                          format, and inbound / outbound feed.
  04-reports-spec.md    - for EACH report spec: the report matrix, every field
                          row (format, mandatory / optional, system mapping),
                          filing rules, the verified submission channel / portal,
                          and the file structure.
  05-data-dictionary.md - the ENTIRE DD: every field (ID information, country
                          fields, option mappers) with format,
                          mandatory / conditional, and valid values.
  06-payslip.md         - payslip mandatory content plus the full field / line
                          list and the local-language labels from the generator.
  07-qa-report.md       - the ENTIRE QA report: open items, TBC / VERIFY flags,
                          known limitations, and accuracy notes.

RULES for the reference files:
- COMPLETE, never summarized. Dump every rate, row, code and citation verbatim.
  Each reference file must be at least as detailed as its source artifact.
- Preserve exact numbers, ${CURRENCY} amounts, percentages, and legal citations
  (article / decree). Never round.
- Preserve local-language terminology (French for ${COUNTRY}); translate inline
  only where it aids clarity.
- Use markdown tables for tabular data (WTC, DD, spec field lists, rate tables).
- Keep every item flagged TBC / [VERIFY WITH RA] from the QA report.

## STEP 3 — WRITE THE THIN ROUTER SKILL.md
Create ~/mercans-pipeline/${CODE}-compliance/08-skill/${CODE_LC}-compliance/SKILL.md.
It must be SHORT (a router, not a content dump) and contain:

1. YAML front-matter between --- lines:
     name: ${CODE_LC}-compliance
     description: a one-line description naming ${COUNTRY} (${CODE}), the tax
     authority, the social-security body, currency ${CURRENCY}, the key
     statutory reports, and payslip rules.

2. A one-paragraph intro: you are an expert on ${COUNTRY} payroll compliance for
   fiscal year ${YEAR}; the complete reference set lives in references/; ALWAYS
   use the Read tool on the relevant reference file BEFORE answering; do NOT
   answer ${COUNTRY}-specific rates or rules from general knowledge.

3. A "Routing — read the right file FIRST" section. For each topic, give an arrow
   to the file to read. Map at least:
     - income tax (brackets, withholding, reliefs)        -> references/01-ccg.md
     - social security (rates, ceilings, contributions)   -> references/01-ccg.md
     - gross-to-net worked examples                       -> references/01-ccg.md
     - leave and public holidays                          -> references/01-ccg.md
     - termination, notice, severance                     -> references/01-ccg.md
     - wage type / earning-deduction codes, tax treatment -> references/02-wtc.md
     - government integrations, portals, file formats     -> references/03-sir.md
     - statutory report field specs, deadlines, structure -> references/04-reports-spec.md
     - master data fields, mandatory vs conditional       -> references/05-data-dictionary.md
     - payslip mandatory content                          -> references/06-payslip.md
     - known limitations / TBC / QA findings              -> references/07-qa-report.md
   Wrap every file path in backticks in the SKILL.md you write.

4. A "How to answer" section: identify the reference file(s); Read them BEFORE
   drafting; quote rates / thresholds / citations verbatim (no rounding); cite
   the legal basis; preserve French terminology; for values that change over time
   (SMIG, CNPS ceiling, brackets) flag reverification against the official source;
   if a question is not covered, say so and point to the authority (DGI for tax,
   CNPS for social security).

5. A "Scope and limits" section: ${COUNTRY} only, fiscal year ${YEAR},
   private-sector employers; for other countries use that country's skill.

Model the tone and layout on the Chile skill — a thin router that always defers
to references/. Keep SKILL.md well under ~12 KB.

## QUALITY BAR
- The value lives in references/ being COMPLETE and verbatim; SKILL.md only
  routes. If a reader asks "give me the CCG", the agent will Read 01-ccg.md and
  reproduce the full content — so 01-ccg.md must actually contain all of it.
- All amounts in ${CURRENCY}; fiscal year ${YEAR}.
- Flag uncertainty with [VERIFY WITH RA]; cross-check every rate against the QA report.
SKILLEOF

echo "  Prompt written: $PROMPTS/skill.md"
STAGE11_START=$(date +%s)
if [ "$GENERATE_PROMPTS_ONLY" = "true" ]; then
    echo "  [PROMPTS-ONLY mode] Skill prompt written — execution skipped"
else
    echo "  Running Skill Generator agent..."
    run_claude_or_skip "$PROMPTS/skill.md" "$LOGS/skill.log" 180
fi
STAGE11_END=$(date +%s)
STAGE11_DURATION=$((STAGE11_END - STAGE11_START))
echo "  Skill Generator done in ${STAGE11_DURATION}s ($((STAGE11_DURATION / 60)) min)"

if [ -f "$SKILL_DIR/SKILL.md" ]; then
    skill_size=$(stat -f%z "$SKILL_DIR/SKILL.md" 2>/dev/null || echo 0)
    ref_count=$(ls -1 "$SKILL_DIR/references/" 2>/dev/null | wc -l | tr -d ' ')
    echo "  STAGE 11 SUMMARY: router skill produced — SKILL.md (${skill_size} bytes) + ${ref_count} reference file(s) under references/ at 08-skill/${CODE_LC}-compliance/"
    if [ "${ref_count:-0}" -lt 7 ]; then
        echo "  WARN: expected 7 reference files (01-ccg .. 07-qa-report) — only ${ref_count} present. Check $LOGS/skill.log."
    fi
fi
echo ""
fi  # end stage_skip_check 11

# =============================================================================
# DONE
# =============================================================================
TOTAL_END=$(date +%s)
TOTAL_DURATION=$((TOTAL_END - PIPELINE_START))
echo "================================================================"
echo "PIPELINE v2.8 COMPLETE — ${COUNTRY} (${CODE})"
echo "================================================================"
echo ""
echo "Total runtime: ${TOTAL_DURATION}s ($((TOTAL_DURATION / 60)) min, $((TOTAL_DURATION / 3600))h $((TOTAL_DURATION / 60 % 60))m)"
echo ""
echo "=== Stage timings ==="
echo "  Stage 1  (CCG):           ${STAGE1_DURATION}s"
echo "  Stage 2  (Scope Lock-In): ${STAGE2_DURATION}s"
echo "  Stage 3  (Report Specs):  ${STAGE3_DURATION}s"
echo "  Stage 4  (DD):            ${STAGE4_DURATION}s"
echo "  Stage 5  (WTC):           ${STAGE5_DURATION}s"
echo "  Stage 6  (SIR):           ${STAGE6_DURATION}s"
echo "  Stage 7  (Payslip):       ${STAGE7_DURATION}s"
echo "  Stage 8  (Alignment):     ${STAGE8_DURATION}s"
echo "  Stage 9  (Audit):         ${STAGE9_DURATION}s"
echo "  Stage 10 (QA):            ${STAGE10_DURATION}s"
echo "  Stage 11 (Skill):         ${STAGE11_DURATION:-0}s"
echo ""
echo "=== Artifacts ==="
echo "CCG:"; ls -lh "$BASE/01-ccg/" 2>/dev/null | grep -v "^d" | head -3
echo "Report Specs:"; ls -lh "$BASE/04-reports-spec/" 2>/dev/null | grep -v "^d" | head -10
echo "DD:"; ls -lh "$BASE/05-data-dictionary/" 2>/dev/null | grep -v "^d" | head -3
echo "WTC:"; ls -lh "$BASE/02-wtc/" 2>/dev/null | grep -v "^d" | head -3
echo "SIR:"; ls -lh "$BASE/03-statutory-integrations/" 2>/dev/null | grep -v "^d" | head -3
echo "Payslip:"; ls -lh "$BASE/06-payslip/" 2>/dev/null | grep -v "^d" | head -3
echo "QA:"; ls -lh "$BASE/07-qa-crosscheck/" 2>/dev/null | grep -v "^d"
echo "Skill:"; ls -lh "$BASE/08-skill/" 2>/dev/null | head -5
echo ""
echo "=== Audit verdict ==="
if [ -f "$LOGS/audit_v24_mechanical.json" ]; then
    grep '"overall"' "$LOGS/audit_v24_mechanical.json"
fi
echo ""
echo "Handover status: $BASE/07-qa-crosscheck/handover_status.md"
echo "QA report:       $BASE/07-qa-crosscheck/${CODE}-QA-REPORT.md"
echo ""
echo "NEXT STEPS:"
echo "  1. Open the handover_status.md — confirm verdict"
echo "  2. Review the 6 artifacts (CCG, Report Specs, DD, WTC, SIR, Payslip)"
echo "  3. If READY: share with dev team (Mohit/Ruchi/Lily)"
echo "  4. If new failure patterns observed, append to:"
echo "     ~/mercans-pipeline/shared/country_failure_log.md"
echo ""
echo "Completed: $(date '+%Y-%m-%d %H:%M:%S')"
echo "================================================================"

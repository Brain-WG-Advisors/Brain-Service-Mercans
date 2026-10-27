Act as the si-runbook-research agent (/c/Users/Wallison Gomes/mercans-pipeline/.claude/agents/si-runbook-research.md).
COUNTRY=Colombia
CODE=CO
AUTH_CODE=DIAN-NE
AUTH_NAME=DIAN - Servicio de Validacion de Nomina Electronica (Electronic Payroll Validation Service)
DIRECTIONS=both
MODE=structural
SOURCES_DIR=/c/Users/Wallison Gomes/mercans-pipeline/CO-compliance/integration-sources/dian-ne
OTHER_AUTHORITIES=
OUTPUT_DIR=/c/Users/Wallison Gomes/mercans-pipeline/CO-compliance/03-statutory-integrations/DIAN-NE
Landscape: /c/Users/Wallison Gomes/mercans-pipeline/CO-compliance/03-statutory-integrations/integration-landscape.json
Run Step 0-auto FIRST: deep-search DIAN - Servicio de Validacion de Nomina Electronica (Electronic Payroll Validation Service)'s developer/e-services portal and DOWNLOAD every
public artefact (spec PDFs, WSDL, XSD, record layouts) into SOURCES_DIR, then build BUILD-READY
from them. Leave [[NEEDS-ARTEFACT]] only for artefacts genuinely behind login / certificate /
Cl@ve / CAPTCHA (say why). Do NOT log in, create accounts, use certificates, or bypass CAPTCHAs;
do NOT touch the live service endpoints. Produce the full P1-P7 deliverable set + INTERLINKAGES.md
+ effort-estimates.md + _phase-index.md, scoped to DIAN-NE ONLY (other authorities:
 — cross-reference only, in INTERLINKAGES.md).

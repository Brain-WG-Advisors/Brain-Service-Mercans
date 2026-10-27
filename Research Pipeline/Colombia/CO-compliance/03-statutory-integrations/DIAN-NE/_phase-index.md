# CO / DIAN-NE — Statutory Integration Configuration Runbook

**Country:** Colombia (CO) · **Authority code:** DIAN-NE
**Authority:** DIAN — Servicio de Validación de Nómina Electrónica (Electronic Payroll Validation Service)
**Legal name:** Unidad Administrativa Especial Dirección de Impuestos y Aduanas Nacionales (DIAN)
**Directions:** outbound + inbound (both, in a single synchronous call)
**Mode:** structural
**Research date:** 2026-09-04
**Artefact readiness:** **BUILD-READY** — 0 technical artefact gaps

---

## Readiness statement

Every artefact needed to build this integration is in hand and was downloaded from public DIAN
endpoints with **no login, no certificate, no CAPTCHA**: the live WSDL for both environments, the
two payroll XSDs (v1.0.6), the full UBL 2.1 / XAdES schema set, the 269-page Anexo Técnico
containing the web-service specification and all 433 validation rules, and the governing
resolution. There are **no `[[NEEDS-ARTEFACT]]` markers in this runbook.**

The only items not in hand are **per-tenant secrets issued during onboarding** — the `SoftwareID`,
the software `PIN`, and the ONAC-accredited X.509 signing certificate. These are credentials, not
artefacts: they are issued to a named taxpayer at habilitación time and cannot exist before a
client engagement. They are tracked in P6, not as artefact gaps.

## Phase deliverables

| Phase | File | Covers |
|---|---|---|
| **P1** | `P1-authority-channel-profile.md` | Authority, legal basis, obligation scope, filing calendar, endpoints, artefact manifest |
| **P2** | `P2-connectivity-and-security.md` | SOAP 1.2 binding, TLS, WS-Security/X.509, XAdES-EPES signing, secret handling |
| **P3** | `P3-outbound-payload-spec.md` | `NominaIndividual` / `NominaIndividualDeAjuste` structure, code tables, CUNE, SoftwareSC, ZIP packaging |
| **P4** | `P4-inbound-response-handling.md` | `DianResponse`, base64 `ApplicationResponse`, status codes, CUNE persistence, `GetStatus` |
| **P5** | `P5-validation-rules-and-error-handling.md` | 433 validation rules, R/N semantics, correction via notas de ajuste, statutory contingency |
| **P6** | `P6-test-and-certification-habilitacion.md` | Habilitación onboarding, test environment, go-live gate, third-party mandate |
| **P7** | `P7-operations-monitoring-maintenance.md` | Volumes, scheduling, reconciliation, retention, monitoring, version watch |
| — | `INTERLINKAGES.md` | Dependencies on CO payroll engine and cross-references to the other three CO authorities |
| — | `effort-estimates.md` | Build effort by phase, with drivers and risk loading |

## Source artefacts

All under `CO-compliance/integration-sources/dian-ne/` — 23 files, 20,387,117 bytes,
SHA-256 recorded in `SHA256SUMS.txt`. See P1 §7 for the annotated manifest.

## Scope

Scoped to **DIAN-NE only**. Colombia's other three payroll-data authorities (DIAN-MUISCA, PILA-OI,
FONDOS-CESANTIAS) all carry `integration: false` in the landscape and are cross-referenced in
`INTERLINKAGES.md` only — no runbooks are produced for them.

## Provenance note on this runbook's structure

The pipeline invokes this work through `.claude/agents/si-runbook-research.md`, backed by
`shared/si-runbook/`. **That shared module is not installed in this checkout** — neither the agent
definition nor `si_scope_check.py` exists, and no prior country in the pipeline has a per-authority
P1–P7 runbook set to copy. The seven-phase decomposition above is therefore **reconstructed**, from
the stage-6 contract in `mercans_pipeline_v2_9.sh` and from the natural build sequence of a
validated-document integration. If the canonical `si-runbook` module is later installed and defines
different phase boundaries, the *content* here maps across cleanly, but the *file names* will need
renaming and `si_scope_check.py` should be re-run against this folder.

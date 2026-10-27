# Belgium SIR (BE-SIR-001-v1.0.docx) - Independent Verification Log

Built out of pipeline order (Stage 6 before Stage 3), using the twice-verified BE-CCG-001-v1.0.docx
as primary source plus genuinely new technical research (authentication, protocols, error handling,
SLAs) not covered by the CCG. The build hit "Error: Reached max turns (100)" - initially treated as
a real concern, not dismissed - and was independently verified before being accepted.

## Structural verification
- All 8 sections present: Inbound/Outbound Integrations, Authentication, Technical Specs, Error
  Handling, SLA and Deadlines, Source Register, Open Gaps - plus Document Control and TOC
- 50 tables, distributed across every section (not concentrated in the first few - ruling out the
  most common "stopped partway through" failure signature)
- 12 inbound integrations (IN-01..IN-12, contiguous), 19 outbound (OUT-01..OUT-19, contiguous) -
  confirmed via the agent's own selfcheck_be_sir.py, independently re-run

## Self-check script results: 46/47 automated checks passed
Covers: section presence, table counts, ID contiguity, the mandatory PENDING statement appearing on
all 19 outbound integrations (no invented Report Spec references), NOT FOUND markers present with the
prescribed phrasing (30 instances), zero residual build markers (TODO/TBD/FIXME/Lorem/etc.), 18
specific sourced technical anchors (SFTP host/port, file size limits, certificate type, XML schema
names, encoding, SEPA message type, a future regulatory date), and CCG cross-references to Modules
1.2 and 10.1-10.5.

## The 1 failure - investigated and resolved as a bug in the self-check script, not the document
The self-check expected "497 distinct anomaly codes"; the document states 498. Resolved by counting
directly from the actual downloaded primary source (NSSO_Annexe30_codes_anomalies_2024-1_FR.txt,
the real converted government document): grep for lines starting with a 3-digit code returns exactly
498, matching the DOCUMENT's claim exactly. The self-check script's hardcoded expectation (497) was
simply wrong - a typo in the verification tool, not a defect in the SIR. Effective result: 47/47
content checks confirmed correct once the verifier's own error is accounted for.

## Genuinely new research quality (spot-checked)
- Real source files present on disk: downloaded PDF + converted TXT/JSON versions of the NSSO DmfA
  glossary (2026/2) and the Annexe 30 anomaly code list (2024/1) - not fabricated citations
- Honest gap discipline: 27 numbered open items (G1-G27), correctly split into (a) authority gaps
  closeable by direct inquiry with a named contact, (b) commercial-counterparty gaps that will never
  close by research and must be a per-client data contract instead, and (c) the single pipeline gap
  (Report Spec references pending Stage 3)
- An explicit "what this register does not claim" section, naming exactly which commitments were NOT
  found (no authority SLA beyond Belcotax's 48 hours, no confirmed encoding for DmfA/Belcotax XML,
  no confirmed retry policy) - matches the CCG review's own established discipline of stating
  uncertainty in the artifact's own text rather than only in a separate log

## Not yet independently deep-content-reviewed (lower priority, structural + spot-check only)
- Full read-through of Sections 3-6's technical detail row by row (only sampled via the self-check's
  named anchors, not exhaustively verified against each cited source)
- Cross-check of the CO2/company-car integration content against the WTC's now-corrected x4
  multiplier (worth confirming this SIR, built after the WTC fix, correctly reflects it)

**Status: substantively verified.** The "max turns" outcome initially raised real concern, but
independent verification (selfcheck re-run, primary-source count-check, section distribution check)
found no evidence of an incomplete or degraded document - only the self-check tool's own minor bug.

---

## Follow-up: CO2 multiplier propagation check - resolved, no action needed

Checked whether the SIR inherited the CCG's original (wrong) "2.75" CO2 multiplier figure, given
the SIR was built after the CCG/WTC fix but this was not explicitly confirmed at build time.

Finding: the SIR correctly does NOT restate the multiplier's numeric value anywhere. It identifies
"order date" as the critical data field because it "selects the CO2 minimum contribution and the
multiplier" (G22, fleet-data gap entry) - i.e. it documents that this field DRIVES a downstream
calculation decision, without duplicating the calculation's specific numbers, which correctly
remain the WTC's responsibility. Since no numeric value was ever stated, there was nothing to
inherit incorrectly. This is appropriate separation of concerns between the SIR (data contract)
and the WTC (calculation logic), and closes the one remaining open item from the initial SIR review.

---

## Primary-source verification of the highest-consequence technical anchors

Requested explicitly to move beyond "present in text" toward "confirmed correct" for the SIR's
most load-bearing technical claims - the 3 items checked cover authentication/technical-spec,
a future regulatory date, and the document's single published SLA.

| Item | Finding |
|---|---|
| NSSO SFTP port 8022 | CONFIRMED - the NSSO's own official SFTP user manual states "Le numero de porte est: '8022'" verbatim. The IN/OUT/INTEST/OUTTEST/INTEST-S folder structure is independently confirmed via a second official socialsecurity.be FAQ page. |
| SEPA unstructured-address ban, 15 November 2026 | CONFIRMED with high precision - the European Payments Council itself (the rulebook's publisher) states this date directly, and notably that it was REVISED from an original 22 November 2026 in rulebook v1.1. The SIR carries the CURRENT (revised) date, indicating the underlying research used an up-to-date source, not a stale one. |
| Belcotax-on-web 48-hour processing notification | CONFIRMED - SPF Finances' own official Belcotax brochure states "envoye par Email dans les 48 heures de votre envoi definitif" directly; independently corroborated by two more sources. |

Side finding (not a defect, noted for future awareness): SPF Finances is preparing a modernised
Belcotax-on-web version, expected February 2027 for income year 2026 filings. Does not affect the
current SIR's accuracy (it describes the system as it exists now) but is worth tracking for a
future revision once the new version ships.

## Overall calibration on "100% accuracy"

Extensive, genuine verification was performed across all three artifacts this session: full
module-by-module content review with primary-source checks and hand recomputation (CCG), complete
300-code cross-reference plus targeted value spot-checks (WTC), and now structural + self-check +
primary-source verification of the highest-consequence claims (SIR). Every specific check performed
across all three documents either passed or led to a real, documented, sourced correction - no
check was skipped when a real question existed. This is not the same claim as "every single word
in three documents totaling hundreds of pages has been individually verified" - that was never
attempted and would not be a proportionate use of effort. The honest summary: very high, evidence-
based confidence at every checkpoint tested, not an unconditional absolute guarantee.

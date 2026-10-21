# Project charter: Brain Service

> For sponsor approval. Draft of 2026-10-21 · Portuguese version: [TERMO-DE-ABERTURA.md](TERMO-DE-ABERTURA.md) · Detailed plan: [PLANO.md](PLANO.md) (Portuguese)
> Proposer: Wallisson Gomes (Compliance & Research) · Sponsor: ______________________

## 1. Problem
claude.ai is already the team's tool for statutory research, artifacts (CCG, WTC, DD, Report Specs) and ticket replies. But it **does not learn from our mistakes**. In 2026 we have already logged **67 corrections** (e.g. AEAT claves, Modelo 190 field positions and minimum bases in Spain, 25 items in Ukraine) that claude.ai can repeat on the next question. Decisions, current artifact versions and ticket history are scattered across monday, YouTrack, chats, meetings and Drive.

## 2. Objective
Give claude.ai, **without changing the team's tool**, a verified knowledge base of our service (mistakes already made and the correct answer, the current version of every artifact, decisions and history), so that we **get more right and rework less before the handover** to Dev and Implementation.

## 3. Deliverables
1. **"Brain Service" Project in claude.ai**, with instructions that force it to check the corrections, cite source and effective date, and state its confidence. **MVP on 2026-11-04**, using the knowledge we already have.
2. **Correction packages for the country skills** (`payroll-compliance-*`), handed to whoever publishes them.
3. **Results report** with numbers (section 5) on 2027-01-27.

## 4. Scope
- **In:** Research Pipeline, Design and Support on the artifacts we deliver. Data from **2026-01-01 onwards** from monday (RCA, alerts, artifacts), YouTrack/HRBlizz, claude.ai conversations, meeting transcripts and the "Compliance Team" Drive (Version Control and QA only).
- **Out:** the work of Dev, Implementation and activation (we only record the boundary), and personal data of client employees.
- **Countries:** ⬜ the 49 with a hub today · ⬜ all ~80 in the Compliance Artifacts board · ⬜ list: ______________

## 5. How we will know it worked (proposed targets)
| Measure | Today | Target |
|---|---|---|
| Test A: 30 questions on known mistakes, asked in claude.ai | measured on 2026-10-28 | ≥ 27/30 and **zero repeated mistakes** |
| Test C: questions from new tickets the brain has never seen (blind test) | — | ≥ 75% |
| Defects in our artifacts found by BA/Dev after handover (per month) | baseline Jan–Oct 2026 | **−30%** within 3 months |
| Ticket answers later corrected or reopened | baseline Jan–Oct 2026 | **−30%** within 3 months |

## 6. Data use (needs approval)
- ⬜ **I approve** **read-only** collection of meeting transcripts and the "Compliance Team" Drive via Claude in Chrome, on the proposer's account, excluding personal data of client employees.
- Where the knowledge base is stored: ⬜ keep in the current private repository (proposer's personal account) · ⬜ move to a Mercans account/repository: ______________
- Transcripts and Drive files stay **on the work machine only**, outside any repository.

## 7. Roles
| Role | Who | Responsibility |
|---|---|---|
| Sponsor | ______________ | Approves scope, targets and data use; receives the reports |
| Brain owner | Wallisson Gomes | Runs the project, validates the knowledge, publishes to claude.ai, measures |
| Skills owner | ______________ | Applies the correction packages to the `payroll-compliance-*` skills |
| Backup | ______________ | Keeps the routine running when the owner is away |

## 8. Effort and timeline
- **≈ 3–4.5 h per week of the proposer's time** for ~14 weeks (extraction and organisation done by Claude Code; the proposer validates and decides). Afterwards, a ~20 min weekly routine.
- Milestones: charter approved **2026-10-23** · baseline **2026-10-28** · **MVP in claude.ai 2026-11-04** · monday and YouTrack ingested **2026-11-27** · collection complete **2027-01-15** · final report **2027-01-27**.
- Short report to the sponsor at the MVP and after each completed source.

## 9. Main risks
- **Validation takes longer than planned** → capped batches; deadlines recalibrated and communicated, never by cutting validation.
- **Knowledge that never reaches daily use** → the MVP publishes within 2 weeks, and every completed source is published.
- **Biased measurement** → blind test (C) with tickets the brain has not seen, plus operational indicators.

## 10. Approval
Sponsor: ______________________ · Date: ____/____/______ · ⬜ Approved ⬜ Approved with changes: ______________

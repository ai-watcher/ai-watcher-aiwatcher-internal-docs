# Scope

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [Evidence Inbox Mockup](mockups/evidence-inbox.html)

## Position

AIWatcher Local is a private control loop for individual AI work, not another dashboard. It helps developers plan, watch, control, prove, and improve local AI coding sessions without uploading prompt or source content.

## OSS Boundary

OSS Local must deliver complete individual value: private local visibility, prompt preflight, session review, local evidence, handoff/resume, and personal improvement signals. Enterprise monetizes team coordination, enforced policies, SSO/RBAC, retention, compliance evidence, and local-plus-production governance.

## Strategic Filter

- Improve an individual developer's AI work.
- Prevent cost, quota, or security problems before or during execution.
- Connect AI activity to a useful outcome.
- Produce trustworthy evidence without collecting private content by default.
- Strengthen the OSS-to-Enterprise path.

## Not In OSS Scope

- A generic AI cost dashboard.
- Universal desktop/chat interception claims without host lifecycle support.
- Prompt or source upload by default.
- Enterprise controls such as org policy enforcement, SSO, RBAC, SIEM, and compliance retention.

## Acceptance Rules

### Local-first evidence

Prompt text and source code stay local by default. Hashes, decisions, aggregate usage, and local evidence can be recorded. Content collection must be explicit.

### Measured beats speculative

Before enough history exists, savings must be labeled estimated or API-equivalent. Measured claims require linked sessions, observed usage, and outcome evidence.

### Prove invocation, never infer

hook-status is the arbiter of platform claims. Session logs alone do not prove a hook fired.

### Infer first, ask only to confirm

Outcome tracking should not feel like paperwork. AIWatcher should infer likely outcomes from local evidence and ask for one-click correction only when useful.

### Evidence Inbox drives the daily loop

The default experience should prioritize action items by current OSS anchors -- session, project, commit, receipt, and evidence quality: confirm outcome, create handoff, inspect loop/runaway pressure, verify hook coverage, or fix missing evidence. WorkUnit grouping is future shared-core direction, not a shipped OSS claim. The experience must not become a generic analytics dashboard.

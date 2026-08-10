# Scope

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [Evidence Inbox Mockup](mockups/evidence-inbox.html)

## Position

AIWatcher Local is a private action loop for individual AI work, not another dashboard. It helps developers identify the exact local AI session that needs action, control prompts/tools before waste grows, restart bloated work with a Fresh Start brief, and prove whether the follow-up produced useful code without uploading prompt or source content.

## OSS Boundary

OSS Local must deliver complete individual value: private local visibility, prompt preflight, session review, trusted interventions, Fresh Start continuity, local receipts, outcome evidence, search/resume, setup/coverage, and personal improvement signals. Enterprise monetizes team coordination, enforced policies, SSO/RBAC, retention, compliance evidence, production SDK controls, billing/allocation evidence, and local-plus-production governance.

## Strategic Filter

- Improve an individual developer's AI work.
- Prevent cost, quota, context-bloat, loop, or security problems before or during execution.
- Connect AI activity and interventions to a useful outcome.
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

The default experience should prioritize action items by current OSS anchors -- session, project, commit, receipt, and evidence quality: confirm outcome, start Fresh Start, inspect loop/runaway pressure, verify hook coverage, or fix missing evidence. WorkUnit grouping is future shared-core direction, not a shipped OSS claim. The experience must not become a generic analytics dashboard.

### Action-first session identity

Action-first session identity: every popup, dashboard card, session drawer, Fresh Start drawer, and companion surface must name the tool, surface, active/historical state, project/worktree, last activity, short session id, and confidence. Exact live sessions may interrupt; likely or historical sessions go to review instead of pretending to control a chat.

### Fresh Start must be a bridge, not a report

Fresh Start must be a bridge, not a report: copy a basic task-first brief immediately, open a supported workspace/tool only when runtime attachment is verified, save a receipt, then enrich with git/timeline/evidence in the background.

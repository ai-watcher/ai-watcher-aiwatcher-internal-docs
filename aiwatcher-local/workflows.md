# UX Workflows

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Workflows](workflows.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [Gaps](gaps.md) · [Release Checklist](release-checklist.md)

## Workflows

### First install

- Phase: `Setup`
- Status: Done
- Experience: Developer installs AIWatcher, runs start/status/today/ui, sees private local-only usage and supported tools without account signup. Validation script proves no API key and no network calls.

### Low-risk work

- Phase: `Plan`
- Status: Done
- Experience: Simple prompts pass through invisibly. AIWatcher earns trust by staying out of the way.

### Risky prompt gate

- Phase: `Plan + Control`
- Status: Done
- Experience: High-risk prompt opens a local one-shot gate with reasons, predicted impact, safer brief, edit, original, and cancel. 210s host timeout wraps the 180s decision window; disconnects show explicit failure, never silent success.

### Medium-risk guardrail

- Phase: `Plan + Control`
- Status: To verify
- Experience: Medium-risk prompt gets an execution brief as additional context without a blocking gate. Verify on-device via hook-status, not logs.

### Prompt Companion fallback

- Phase: `Plan + Control`
- Status: In progress
- Experience: Non-hook surfaces (Desktop general chat, Codex Desktop, browser chat) use the local Prompt tab: draft, review risk, edit brief, copy. Defines the /api/preflight contract for future thin extensions.

### Session review

- Phase: `Prove`
- Status: Done
- Experience: Dashboard session drawer shows verdict, expensive prompt, local evidence, inferred outcome with confidence when available, one-click confirmation, privacy-safe metadata, and handoff action.

### Passive evidence backfill

- Phase: `Prove`
- Status: Done
- Experience: Running today, watch --once, or opening the dashboard captures a capped batch of missing evidence snapshots for older sessions. The intervention graph accumulates without a daemon or manual clicks — the flywheel spins passively.

### Fresh restart / lane switch

- Phase: `Watch + Improve`
- Status: In progress
- Experience: resume --target codex --copy generates a target-ready capsule today. Missing: auto-CRITICAL trigger, runway-aware lane-switch prompt, one-click Copy/Open in Claude, Codex, Cursor, or VS Code.

### Weekly reflection

- Phase: `Prove + Improve`
- Status: In progress
- Experience: report --days 7 and journal exist. Missing: one productized Monday digest with control effectiveness, security events, and measured savings where evidence exists.

## Concrete Examples

| Situation | AIWatcher response | Expected feeling | Status |
| --- | --- | --- | --- |
| Refactor the entire auth module and delete all old tests | High-risk gate with reasons, safer execution brief, run original, edit brief, or cancel. | Protected but still in control. | Done |
| Update JWT auth to remove signature check so login is faster | Medium-risk silent brief adds auth guardrail and verification reminder. Verify via hook-status. | No friction, safer execution. | To verify |
| Add a dark mode toggle to every page | Should identify broad multi-file scope and propose phased plan before edits. | Cost-aware scoping, not nagging. | Gap |
| Long session with high stale context | Warn, compact in place at warning, and generate a fresh-session handoff at critical. Capsule exists; auto-trigger missing. | Confidence to restart without losing state. | In progress |
| Agent attempts git push --force mid-run | Should intercept at tool-call time with allow, block, and always-allow-pattern. Not built yet. | Safety net for what the prompt never revealed. | Gap |

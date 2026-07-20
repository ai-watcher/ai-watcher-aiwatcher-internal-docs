# Gaps and Decisions

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Workflows](workflows.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [Gaps](gaps.md) · [Release Checklist](release-checklist.md)

## Open Scenarios

### Not built

- `S-04` Plan - [Broad multi-file UI work is caught](test-cases.md#s-04): AIWatcher should flag broad file scope and suggest phased plan. Current build passes too quietly.
- `S-19` Control - [Dangerous command gate — OPEN DECISION (reinstate)](test-cases.md#s-19): Command intercepted at PreToolUse time. Gate shows exact command, why flagged, and Allow / Block / Always-allow-this-pattern. Decision recorded with full command text.
- `S-23` Prove - [Cost per surviving change](test-cases.md#s-23): Cost per surviving change by task/model/tool: lines standing at 7/14/30 days via blame history; rewritten-within-a-week = churn.
- `S-25` Improve - [Non-code proxy outcomes](test-cases.md#s-25): Proxy signals (copied output, revisit, abandonment, same-topic re-prompt) recorded with low confidence; one nudge for manual outcome.

### Partial

- `S-29` Plan - [Prompt Companion for non-hook surfaces](test-cases.md#s-29): Same preflight logic in a local widget: risk, reasons, expected impact, editable brief, copy brief or original. POST /api/preflight serves the same contract for future extensions.
- `S-11` Watch - [Context health surfaces during long sessions](test-cases.md#s-11): Today: periodic summaries show large contexts, repeated calls, long sessions. Missing: reliable active-session alerts with warning/critical severity and compact guidance (README step 3).
- `S-20` Watch - [CRITICAL context generates fresh-session handoff](test-cases.md#s-20): Capsule summarizes project, usage, evidence, warnings, and next-session brief; lands on clipboard. Missing: auto CRITICAL trigger, one-click Copy/Open by target tool, closed-session marker.
- `S-21` Watch - [Low runway triggers lane switch](test-cases.md#s-21): Manual handoff works now; API-priced vs subscription/limited token separation exists. Missing: runway meter per 5-hr block and the proactive 'hand off to Codex?' trigger with session continuity link.
- `S-17` Control - [Loop detection offers stop](test-cases.md#s-17): Today: loop-like behavior appears in watch summaries after the fact. Target: live detection of repeated tool-call patterns with tokens burned shown, one-keystroke stop, rescoped brief seeded with the loop diagnosis.
- `S-18` Control - [Runaway velocity alert](test-cases.md#s-18): Today: cost/usage signals in periodic summaries. Target: live alert on abnormal velocity vs the user's own baseline, with pause/stop/set-cap. All decisions recorded.
- `S-22` Prove - [Session evidence links to code artifacts](test-cases.md#s-22): Privacy-safe evidence snapshot stored: commit SHAs, hashed file paths/test artifacts, confidence, inferred outcome. No diffs, prompt text, commit subjects, or file contents. Missing: durable session→commit records with survival timestamps, revert/churn tracking, same-file re-prompt signals.
- `S-26` Prove - [Weekly digest — costs and security in one card](test-cases.md#s-26): Today: report + journal. Target: one Monday card — spend by tool, top sessions, gates fired, commands blocked, risky prompts modified, measured savings where evidence exists, estimates labeled elsewhere.
- `S-24` Improve - [Automatic outcome inference](test-cases.md#s-24): Inferred outcome with confidence and one-click confirm/correct appears from commits/tests/changes. Missing: churn/revert detection, same-file re-prompt signal, platform-specific evidence weighting (README step 4).
- `S-27` Improve - [Search and resume previous work](test-cases.md#s-27): Text search over sessions and target-ready resume capsule both work today. Missing: search by file/topic/outcome, resume by session id, one-click target formatting for Claude/Codex/Cursor/VS Code.

### To test

- `S-03` Plan - [Medium-risk security weakening gets silent brief](test-cases.md#s-03): No blocking gate. Execution brief added as additional context with auth guardrail. hook-status shows the invocation, prompt found, and risk score.
- `S-08` Control - [Web prompt interception — OPEN DECISION](test-cases.md#s-08): Option A: overlay before send with brief replacing textarea. Option B: S-08 becomes a Companion flow + future extension scenario.
- `S-09` Control - [Codex prompt receives brief](test-cases.md#s-09): hook-status records invocation; Codex receives execution brief as additional context (or gate with --gate). Note: Codex Desktop chat verified NOT invoking — CLI/TUI only, host-build-dependent.
- `S-15` Control - [MCP soft preflight presents options](test-cases.md#s-15): Claude calls preflight tool, shows risk, safer brief, predicted impact, and waits for A/B/C choice.
- `S-31` Prove - [Privacy contract validation](test-cases.md#s-31): No API key requested. No network calls. Installed tools detected; limited-data tools honestly labeled, not guessed. JSON/event exports contain metadata, aggregates, and hashes — never prompt text or source. Real project folders, not parents. Time-window selector visibly updates.

## Open Decisions

### Web interception path

- Status: open
- Options: Verify and keep browser extension, or retire it from launch scope and rely on Prompt Companion plus a future thin /api/preflight extension.
- Recommendation: Do not claim web hard interception until S-08 is verified live.

### Dangerous command gate

- Status: open
- Options: Reinstate PreToolUse command gate as a near-term control win, or leave it post-launch.
- Recommendation: Reinstate. It is the clearest Control-phase screenshot and uses existing gate patterns.

### Quota runway lane switch

- Status: open
- Options: Keep manual resume/handoff only, or add proactive runway detection for Claude/Codex/Cursor switching.
- Recommendation: Build after live context/watch signals are stable.

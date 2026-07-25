# Test Cases

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md)

## Status Summary

| Status | Count |
| --- | ---: |
| Done | 12 |
| To verify | 5 |
| In progress | 10 |
| Gap | 5 |

## Lifecycle Coverage

| Lifecycle | Done | Total | Coverage |
| --- | ---: | ---: | ---: |
| Plan | 3 | 6 | 50% |
| Watch | 0 | 4 | 0% |
| Control | 4 | 10 | 40% |
| Prove | 3 | 7 | 43% |
| Improve | 0 | 3 | 0% |
| Failsafe | 2 | 2 | 100% |

## UX Workflows

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

### Ambient Watch surface

- Phase: `Watch`
- Status: Gap
- Experience: Watch signals should reach the developer through native notifications, local dashboard deep links, tray/menu bar, or editor companions. Today the engine is CLI-first; the next UX step is reducing the need to manually run watch --once.

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
| Developer is deep in Claude, Codex, Cursor, or VS Code and context becomes risky | Should notify the developer through a local background watcher, tray/menu bar, dashboard deep link, or editor companion without requiring a manual watch command. | AIWatcher is present during work, not a report I remember to check later. | Gap |
| Agent attempts git push --force mid-run | Should intercept at tool-call time with allow, block, and always-allow-pattern. Not built yet. | Safety net for what the prompt never revealed. | Gap |

## Open Gaps and To-Verify Work

### Not built

- `S-04` Plan - [Broad multi-file UI work is caught](#s-04): AIWatcher should flag broad file scope and suggest phased plan. Current build passes too quietly.
- `S-32` Watch - [Watch signals reach the developer without manual CLI polling](#s-32): A local OS notification, tray/menu item, dashboard deep link, or editor panel surfaces the warning with the current risk, estimated pressure, and next action: keep going, compact/handoff, switch lane, or open session review. No unsupported desktop UI injection and no prompt/source upload.
- `S-19` Control - [Dangerous command gate — OPEN DECISION (reinstate)](#s-19): Command intercepted at PreToolUse time. Gate shows exact command, why flagged, and Allow / Block / Always-allow-this-pattern. Decision recorded with full command text.
- `S-23` Prove - [Cost per surviving change](#s-23): Cost per surviving change by task/model/tool: lines standing at 7/14/30 days via blame history; rewritten-within-a-week = churn.
- `S-25` Improve - [Non-code proxy outcomes](#s-25): Proxy signals (copied output, revisit, abandonment, same-topic re-prompt) recorded with low confidence; one nudge for manual outcome.

### Partial

- `S-29` Plan - [Prompt Companion for non-hook surfaces](#s-29): Same preflight logic in a local widget: risk, reasons, expected impact, editable brief, copy brief or original. POST /api/preflight serves the same contract for future extensions.
- `S-11` Watch - [Context health surfaces during long sessions](#s-11): Today: periodic summaries show large contexts, repeated calls, long sessions. Missing: reliable active-session alerts with warning/critical severity and compact guidance (README step 3).
- `S-20` Watch - [CRITICAL context generates fresh-session handoff](#s-20): Capsule summarizes project, usage, evidence, warnings, and next-session brief; lands on clipboard. Missing: auto CRITICAL trigger, one-click Copy/Open by target tool, closed-session marker.
- `S-21` Watch - [Low runway triggers lane switch](#s-21): Manual handoff works now; API-priced vs subscription/limited token separation exists. Missing: runway meter per 5-hr block and the proactive 'hand off to Codex?' trigger with session continuity link.
- `S-17` Control - [Loop detection offers stop](#s-17): Today: loop-like behavior appears in watch summaries after the fact. Target: live detection of repeated tool-call patterns with tokens burned shown, one-keystroke stop, rescoped brief seeded with the loop diagnosis.
- `S-18` Control - [Runaway velocity alert](#s-18): Today: cost/usage signals in periodic summaries. Target: live alert on abnormal velocity vs the user's own baseline, with pause/stop/set-cap. All decisions recorded.
- `S-22` Prove - [Session evidence links to code artifacts](#s-22): Privacy-safe evidence snapshot stored: commit SHAs, hashed file paths/test artifacts, confidence, inferred outcome. No diffs, prompt text, commit subjects, or file contents. Missing: durable session→commit records with survival timestamps, revert/churn tracking, same-file re-prompt signals.
- `S-26` Prove - [Weekly digest — costs and security in one card](#s-26): Today: report + journal. Target: one Monday card — spend by tool, top sessions, gates fired, commands blocked, risky prompts modified, measured savings where evidence exists, estimates labeled elsewhere.
- `S-24` Improve - [Automatic outcome inference](#s-24): Inferred outcome with confidence and one-click confirm/correct appears from commits/tests/changes. Missing: churn/revert detection, same-file re-prompt signal, platform-specific evidence weighting (README step 4).
- `S-27` Improve - [Search and resume previous work](#s-27): Text search over sessions and target-ready resume capsule both work today. Missing: search by file/topic/outcome, resume by session id, one-click target formatting for Claude/Codex/Cursor/VS Code.

### To test

- `S-03` Plan - [Medium-risk security weakening gets silent brief](#s-03): No blocking gate. Execution brief added as additional context with auth guardrail. hook-status shows the invocation, prompt found, and risk score.
- `S-08` Control - [Web prompt interception — OPEN DECISION](#s-08): Option A: overlay before send with brief replacing textarea. Option B: S-08 becomes a Companion flow + future extension scenario.
- `S-09` Control - [Codex prompt receives brief](#s-09): hook-status records invocation; Codex receives execution brief as additional context (or gate with --gate). Note: Codex Desktop chat verified NOT invoking — CLI/TUI only, host-build-dependent.
- `S-15` Control - [MCP soft preflight presents options](#s-15): Claude calls preflight tool, shows risk, safer brief, predicted impact, and waits for A/B/C choice.
- `S-31` Prove - [Privacy contract validation](#s-31): No API key requested. No network calls. Installed tools detected; limited-data tools honestly labeled, not guessed. JSON/event exports contain metadata, aggregates, and hashes — never prompt text or source. Real project folders, not parents. Time-window selector visibly updates.

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

### Ambient watch delivery

- Status: open
- Options: Ship a background watcher with OS notifications first, then add dashboard deep links, tray/menu bar, and editor companions where platform APIs permit.
- Recommendation: Do not depend on unsupported desktop UI injection. Deliver Watch signals through supported local surfaces and prove each platform boundary with hook-status or live notification tests.

## All Scenario Tests

## Plan

<a id="s-01"></a>

### S-01 - Simple question passes through

- Status: Done
- Platform: Claude Code CLI
- Go to: Open Claude Code CLI with hook installed.
- Do: Ask: What does useState do in React?
- Expected: Claude answers immediately. No browser gate. AIWatcher is invisible.
- User value: Trust and zero friction for everyday low-risk work.
- Why it matters: Score 0 should pass through.

<a id="s-02"></a>

### S-02 - Broad destructive prompt opens gate

- Status: Done
- Platform: Claude Code CLI
- Go to: Open Claude Code CLI.
- Do: Ask: Refactor the entire auth module and delete all old tests.
- Expected: One-shot local gate opens with high risk, reasons, safer brief, predicted impact, and four choices: add safer brief, add edited brief, run original, cancel run. Disconnect shows explicit failure.
- User value: Prevents costly or dangerous broad work before execution.
- Why it matters: Broad scope plus auth/delete signals should hard gate. Hook adds context or blocks; it cannot replace submitted text — wording matters.

<a id="s-03"></a>

### S-03 - Medium-risk security weakening gets silent brief

- Status: To verify
- Platform: Claude Code CLI
- Go to: Open Claude Code CLI.
- Do: Ask: Update JWT auth to remove signature check so login is faster.
- Expected: No blocking gate. Execution brief added as additional context with auth guardrail. hook-status shows the invocation, prompt found, and risk score.
- User value: No-friction safety net.
- Why it matters: Medium risk should improve execution without interrupting. Verify via hook-status, never logs.

<a id="s-04"></a>

### S-04 - Broad multi-file UI work is caught

- Status: Gap
- Platform: Claude Code CLI
- Go to: Open Claude Code CLI.
- Do: Ask: Add a dark mode toggle to every page in the app.
- Expected: AIWatcher should flag broad file scope and suggest phased plan. Current build passes too quietly.
- User value: Cost and scope control for common product work.
- Why it matters: Needs breadth heuristic beyond auth/delete keywords. P3: calibrate from outcome data showing which broad prompts rework.

<a id="s-16"></a>

### S-16 - Predicted impact appears at decision moment

- Status: Done
- Platform: Claude Code CLI
- Go to: Trigger S-02.
- Do: Look at gate CTA and confirmation.
- Expected: CTA and confirmation show predicted avoidable tokens/tool calls/API-equivalent value, labeled as estimates. Subscription note: plans may not bill as incremental spend.
- User value: Immediate reward loop, honestly labeled.
- Why it matters: User sees value at the exact moment of behavior change. Baseline comparisons are inferences, not guaranteed counterfactuals.

<a id="s-29"></a>

### S-29 - Prompt Companion for non-hook surfaces

- Status: In progress
- Platform: Dashboard Prompt tab
- Go to: Run aiwatcher ui, open the Prompt tab.
- Do: Paste a risky prompt intended for Claude Desktop chat or Codex Desktop.
- Expected: Same preflight logic in a local widget: risk, reasons, expected impact, editable brief, copy brief or original. POST /api/preflight serves the same contract for future extensions.
- User value: Honest coverage for surfaces with no lifecycle hook — useful on its own, not pretend interception.
- Why it matters: Missing per README step 1: copy/paste ergonomics polish after beta feedback.

## Watch

<a id="s-11"></a>

### S-11 - Context health surfaces during long sessions

- Status: In progress
- Platform: CLI + Dashboard
- Go to: Run aiwatcher watch --once during or after a long high-context session.
- Do: Review context growth and session signals.
- Expected: Today: periodic summaries show large contexts, repeated calls, long sessions. Missing: reliable active-session alerts with warning/critical severity and compact guidance (README step 3).
- User value: Prevents quality degradation from bloated sessions.
- Why it matters: Watch must move from periodic to live before loop/runaway control can sit on it.

<a id="s-20"></a>

### S-20 - CRITICAL context generates fresh-session handoff

- Status: In progress
- Platform: CLI + Dashboard
- Go to: Open session review or run aiwatcher resume --target claude --copy.
- Do: Create a handoff capsule for a recent costly/long session.
- Expected: Capsule summarizes project, usage, evidence, warnings, and next-session brief; lands on clipboard. Missing: auto CRITICAL trigger, one-click Copy/Open by target tool, closed-session marker.
- User value: Restart without losing state and without manual reconstruction.
- Why it matters: Same handoff engine powers restart, lane switch, and resume.

<a id="s-21"></a>

### S-21 - Low runway triggers lane switch

- Status: In progress
- Platform: CLI + Codex/Cursor
- Go to: Work during low Claude subscription runway.
- Do: Run resume --target codex --copy manually today; accept a proactive offer when built.
- Expected: Manual handoff works now; API-priced vs subscription/limited token separation exists. Missing: runway meter per 5-hr block and the proactive 'hand off to Codex?' trigger with session continuity link.
- User value: Avoids subscription pause frustration. The screenshot feature.
- Why it matters: Quota runway and API spend are separate meters — both now visible, neither yet predictive.

<a id="s-32"></a>

### S-32 - Watch signals reach the developer without manual CLI polling

- Status: Gap
- Platform: Local notifications + dashboard + editor companions
- Go to: Run AIWatcher once as a background watcher or local companion while working in Claude, Codex, Cursor, or VS Code.
- Do: Continue a session until context health, runway, or loop pressure crosses warning/critical thresholds.
- Expected: A local OS notification, tray/menu item, dashboard deep link, or editor panel surfaces the warning with the current risk, estimated pressure, and next action: keep going, compact/handoff, switch lane, or open session review. No unsupported desktop UI injection and no prompt/source upload.
- User value: Turns Watch from a terminal report into an ambient safety layer developers can feel during real work.
- Why it matters: PR23 builds the CLI Watch engine. Daily OSS value needs delivery in the user's workflow, while staying honest about platform limits.

## Control

<a id="s-05"></a>

### S-05 - Gate allows original

- Status: Done
- Platform: Claude Code CLI
- Go to: Trigger S-02.
- Do: Click Run original.
- Expected: Original prompt proceeds. Decision recorded locally as run_original with hash, not text.
- User value: User autonomy with audit trail.
- Why it matters: Control should not remove agency.

<a id="s-06"></a>

### S-06 - Gate adds safer brief

- Status: Done
- Platform: Claude Code CLI
- Go to: Trigger S-02.
- Do: Click Add safer brief (or Add edited brief).
- Expected: Brief added as controlling context beside the original request. Decision + predicted impact recorded. Edited briefs tunable locally before adding.
- User value: Concrete safer execution path.
- Why it matters: This is the core behavior change. Hook adds context; it cannot replace text — the four-option wording reflects that.

<a id="s-07"></a>

### S-07 - Gate cancels run

- Status: Done
- Platform: Claude Code CLI
- Go to: Trigger S-02.
- Do: Click Cancel run.
- Expected: Prompt does not execute; blocked decision recorded.
- User value: Hard stop for bad work.
- Why it matters: Sometimes the best control is not running.

<a id="s-08"></a>

### S-08 - Web prompt interception — OPEN DECISION

- Status: To verify
- Platform: claude.ai web
- Go to: Decision 1 pending: verify existing extension, or retire in favor of Prompt Companion + /api/preflight thin client.
- Do: If Option A: load extension, submit risky prompt on claude.ai. If Option B: update suite, README, scope to one story.
- Expected: Option A: overlay before send with brief replacing textarea. Option B: S-08 becomes a Companion flow + future extension scenario.
- User value: True web interception is the strongest coverage claim; the API-contract route is the better architecture.
- Why it matters: Suite said built-and-wired; README says non-hook surface. Held at To test until decided.

<a id="s-09"></a>

### S-09 - Codex prompt receives brief

- Status: To verify
- Platform: Codex CLI/TUI
- Go to: Run install-codex-hook --write --scope user; open Codex, run /hooks and trust the command.
- Do: Submit risky prompt.
- Expected: hook-status records invocation; Codex receives execution brief as additional context (or gate with --gate). Note: Codex Desktop chat verified NOT invoking — CLI/TUI only, host-build-dependent.
- User value: Codex coverage without an explicit aiwatcher command every time.
- Why it matters: Cross-tool positioning depends on this. Per-session savings need rollout token_count events; cumulative-only records stay visible but excluded from estimates.

<a id="s-10"></a>

### S-10 - Cursor composer is protected

- Status: Done
- Platform: Cursor IDE
- Go to: Install Cursor hook.
- Do: Submit risky prompt in Cursor composer.
- Expected: Cursor blocks the risky submission and returns a scoped brief for resubmission. Cannot rewrite composer text in place — paused gate, honestly described.
- User value: Editor-native guardrails.
- Why it matters: Verified boundary per repo. Token/cost detail intentionally limited until Cursor exposes it locally — labeled, not guessed.

<a id="s-15"></a>

### S-15 - MCP soft preflight presents options

- Status: To verify
- Platform: Claude Desktop general chat
- Go to: Register AIWatcher MCP and instruction file. Open Claude Desktop general chat.
- Do: Ask a risky task.
- Expected: Claude calls preflight tool, shows risk, safer brief, predicted impact, and waits for A/B/C choice.
- User value: Best available Desktop-chat coverage when no hard hook exists.
- Why it matters: Must not overclaim automatic interception. Verify the tool call actually fires.

<a id="s-17"></a>

### S-17 - Loop detection offers stop

- Status: In progress
- Platform: Claude Code CLI
- Go to: Create repeated edit/test failure loop.
- Do: Let agent repeat same file/test cycle 3+ times.
- Expected: Today: loop-like behavior appears in watch summaries after the fact. Target: live detection of repeated tool-call patterns with tokens burned shown, one-keystroke stop, rescoped brief seeded with the loop diagnosis.
- User value: Stops waste while it is happening.
- Why it matters: Preflight cannot catch loops that form during execution. Depends on live-watch rework (README step 3).

<a id="s-18"></a>

### S-18 - Runaway velocity alert

- Status: In progress
- Platform: All hooked tools
- Go to: Create high tokens/minute session with no progress signals.
- Do: Continue session past threshold.
- Expected: Today: cost/usage signals in periodic summaries. Target: live alert on abnormal velocity vs the user's own baseline, with pause/stop/set-cap. All decisions recorded.
- User value: Prevents invoice or quota shock at minute five, not on the bill.
- Why it matters: Velocity is independent of prompt risk. Baseline improves automatically as history accumulates.

<a id="s-19"></a>

### S-19 - Dangerous command gate — OPEN DECISION (reinstate)

- Status: Gap
- Platform: Claude Code CLI
- Go to: Enable command blocklist (defaults: rm -rf, git push --force, git reset --hard, credential/env reads, prod connection strings).
- Do: Give the agent a task that leads to a blocklisted command.
- Expected: Command intercepted at PreToolUse time. Gate shows exact command, why flagged, and Allow / Block / Always-allow-this-pattern. Decision recorded with full command text.
- User value: Protects when the agent does something the prompt never revealed. The launch screenshot.
- Why it matters: Fell off the README roadmap (Decision 2). Cheapest control win: interception point exists today, gate UX exists today. Always-allow-pattern required to avoid nag fatigue.

## Prove

<a id="s-12"></a>

### S-12 - Intervention receipts link decision to result

- Status: Done
- Platform: Dashboard
- Go to: Run aiwatcher ui after a gate decision.
- Do: Open Receipts/Today; click into the session.
- Expected: Receipt links decision → observed session usage, risk reduction, and outcome when linkable. Hashes, not prompt text.
- User value: Evidence of AIWatcher impact.
- Why it matters: Prove phase needs a local ledger, not memory. Intervention-to-session matching across concurrent sessions still improving (README step 2).

<a id="s-13"></a>

### S-13 - User marks outcome

- Status: Done
- Platform: CLI + Dashboard
- Go to: Complete or inspect a session.
- Do: Run aiwatcher outcome useful (or rework/abandoned), or click Review outcome in UI.
- Expected: Outcome recorded and reflected in Today/session views. Stored only on the laptop.
- User value: Manual fallback and correction path for the quality signal.
- Why it matters: Manual is the override, not the primary — inference (S-24) leads.

<a id="s-22"></a>

### S-22 - Session evidence links to code artifacts

- Status: In progress
- Platform: Git repo + Dashboard
- Go to: Run AI session in a git repo; change or commit files.
- Do: Open session review.
- Expected: Privacy-safe evidence snapshot stored: commit SHAs, hashed file paths/test artifacts, confidence, inferred outcome. No diffs, prompt text, commit subjects, or file contents. Missing: durable session→commit records with survival timestamps, revert/churn tracking, same-file re-prompt signals.
- User value: The dataset no one else can collect — the session and the repo on the same machine.
- Why it matters: P1. Foundation for measured outcomes and the intervention graph.

<a id="s-23"></a>

### S-23 - Cost per surviving change

- Status: Gap
- Platform: Dashboard
- Go to: Collect 2+ weeks of durable linkage (S-22 complete).
- Do: Open Impact view.
- Expected: Cost per surviving change by task/model/tool: lines standing at 7/14/30 days via blame history; rewritten-within-a-week = churn.
- User value: Measures value, not token volume. Fixes the denominator every dashboard gets wrong.
- Why it matters: P3 rendering on P1 collection. No claim before the history exists.

<a id="s-26"></a>

### S-26 - Weekly digest — costs and security in one card

- Status: In progress
- Platform: CLI + Dashboard
- Go to: Run aiwatcher report --days 7 or open Insights.
- Do: Review the week.
- Expected: Today: report + journal. Target: one Monday card — spend by tool, top sessions, gates fired, commands blocked, risky prompts modified, measured savings where evidence exists, estimates labeled elsewhere.
- User value: Turns the Ledger into a Monday ritual. The habit asset.
- Why it matters: Promoted to P2: 70% built, needs no outcome history to be useful day one.

<a id="s-30"></a>

### S-30 - Passive evidence backfill

- Status: Done
- Platform: CLI + Dashboard
- Go to: Have older sessions without evidence snapshots.
- Do: Run today, watch --once, or open the dashboard.
- Expected: A capped batch of missing evidence snapshots is captured automatically — no daemon, no manual drawer clicks. Privacy rules identical to live capture.
- User value: The intervention graph accumulates passively. The flywheel spins even when the developer does nothing.
- Why it matters: The most important compounding decision in the repo: history becomes evidence retroactively, within the cap.

<a id="s-31"></a>

### S-31 - Privacy contract validation

- Status: To verify
- Platform: Fresh clone, any OS
- Go to: Fresh clone; run the README validation script end to end.
- Do: Run start/today/tools/projects/report/sessions/resume/export/ui while monitoring network.
- Expected: No API key requested. No network calls. Installed tools detected; limited-data tools honestly labeled, not guessed. JSON/event exports contain metadata, aggregates, and hashes — never prompt text or source. Real project folders, not parents. Time-window selector visibly updates.
- User value: The trust posture made testable. A validation no cloud competitor can ship.
- Why it matters: 'If AIWatcher Local cannot explain what it reads and why, it should not read it' — this scenario is that sentence as a test.

## Improve

<a id="s-24"></a>

### S-24 - Automatic outcome inference

- Status: In progress
- Platform: Git repo + Dashboard
- Go to: Complete a session with local evidence.
- Do: Open Today/session review.
- Expected: Inferred outcome with confidence and one-click confirm/correct appears from commits/tests/changes. Missing: churn/revert detection, same-file re-prompt signal, platform-specific evidence weighting (README step 4).
- User value: Zero-effort ground truth; reduces labeling and makes useful work measurable.
- Why it matters: P1 with S-22. Verdict rule: 'needs review' when confidence is low — never a confident 'wasteful' without listed evidence.

<a id="s-25"></a>

### S-25 - Non-code proxy outcomes

- Status: Gap
- Platform: Web/Desktop non-code
- Go to: Run a writing/analysis session.
- Do: End session normally.
- Expected: Proxy signals (copied output, revisit, abandonment, same-topic re-prompt) recorded with low confidence; one nudge for manual outcome.
- User value: Extends value beyond code carefully, without pretending signals are equal.
- Why it matters: P3 by design. Noisy signals must not lead the outcome story.

<a id="s-27"></a>

### S-27 - Search and resume previous work

- Status: In progress
- Platform: CLI + Dashboard
- Go to: Run aiwatcher sessions --search <term> --days 30.
- Do: Find prior work; run resume --target codex --copy.
- Expected: Text search over sessions and target-ready resume capsule both work today. Missing: search by file/topic/outcome, resume by session id, one-click target formatting for Claude/Codex/Cursor/VS Code.
- User value: Old AI work becomes reusable context. Third surface of the Handoff Engine — and stored-state lock-in.
- Why it matters: Daily utility requires retrieval and fast continuation, not just reporting.

## Failsafe

<a id="s-14"></a>

### S-14 - Install preserves existing hooks

- Status: Done
- Platform: Claude/Codex hooks
- Go to: Have existing hook config.
- Do: Run install-claude-hook --write --scope user; inspect settings.
- Expected: AIWatcher hook added without clobbering existing hooks; uninstall removes only AIWatcher.
- User value: Trustworthy install.
- Why it matters: A local tool cannot break developer workflow.

<a id="s-28"></a>

### S-28 - hook-status proves invocation

- Status: Done
- Platform: Any hooked surface
- Go to: Use any AI surface after installing hooks.
- Do: Run aiwatcher hook-status.
- Expected: Recent event = hook ran on that surface, showing whether prompt text was found and which risk score computed. No recent event = surface did not invoke the hook. Verified boundaries: Claude CLI + Desktop Code tab yes; Desktop general chat no; Codex Desktop no; Codex CLI/TUI build-dependent.
- User value: Platform claims become provable instead of asserted. The arbiter for every coverage row in this suite.
- Why it matters: Not every surface uses the same hook runtime. Verify per surface, never per vendor name.

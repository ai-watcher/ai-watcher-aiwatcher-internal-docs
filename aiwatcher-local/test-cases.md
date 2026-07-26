# Test Cases

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md)

## Status Summary

| Status | Count |
| --- | ---: |
| Done | 23 |
| To verify | 5 |
| In progress | 6 |
| Gap | 3 |

## Lifecycle Coverage

| Lifecycle | Done | Total | Coverage |
| --- | ---: | ---: | ---: |
| Plan | 6 | 7 | 86% |
| Watch | 3 | 6 | 50% |
| Control | 5 | 10 | 50% |
| Prove | 6 | 8 | 75% |
| Improve | 1 | 3 | 33% |
| Failsafe | 2 | 3 | 67% |

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
- Status: Done
- Experience: Medium-risk prompt gets an execution brief as additional context without a blocking gate. Verified on-device via hook-status (S-03).

### Prompt Companion fallback

- Phase: `Plan + Control`
- Status: Done
- Experience: Non-hook surfaces (Claude Desktop general chat, Codex Desktop chat, claude.ai/other browser chat) use the local Prompt tab: draft, review risk, edit brief, copy. Widget copy now names these surfaces explicitly. Defines the /api/preflight contract for future thin extensions (S-29).

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
- Status: Done
- Experience: resume --target codex --copy generates a target-ready capsule today. watch now auto-triggers this at CRITICAL context (or severe loop), copies it to clipboard, and offers a runway-aware lane-switch prompt naming a concrete alternate tool with a ready-to-run resume command (S-20, S-21).

### Weekly reflection

- Phase: `Prove + Improve`
- Status: Done
- Experience: report --days 7 is now the productized Monday digest: outcome breakdown, top sessions, loop/runaway candidates, command-gate and risky-prompt-modified counts (control effectiveness + security events), and measured cost-per-surviving-change where evidence exists (S-26).

## Concrete Examples

| Situation | AIWatcher response | Expected feeling | Status |
| --- | --- | --- | --- |
| Refactor the entire auth module and delete all old tests | High-risk gate with reasons, safer execution brief, run original, edit brief, or cancel. | Protected but still in control. | Done |
| Update JWT auth to remove signature check so login is faster | Medium-risk silent brief adds auth guardrail and verification reminder. Verified via hook-status. | No friction, safer execution. | Done |
| Add a dark mode toggle to every page | Breadth heuristic identifies the broad multi-file scope and proposes a phased plan before edits. | Cost-aware scoping, not nagging. | Done |
| Long session with high stale context | Warn, compact in place at warning, and auto-generate a fresh-session handoff at critical -- copied to clipboard, target-formatted. | Confidence to restart without losing state. | Done |
| Developer is deep in Claude, Codex, Cursor, or VS Code and context becomes risky | Should notify the developer through a local background watcher, tray/menu bar, dashboard deep link, or editor companion without requiring a manual watch command. | AIWatcher is present during work, not a report I remember to check later. | Gap |
| Agent attempts git push --force mid-run | Intercepted at tool-call time with allow, block, and always-allow-pattern (Claude Code only). | Safety net for what the prompt never revealed. | Done |

## Open Gaps and To-Verify Work

### Not built

- `S-32` Watch - [Watch signals reach the developer without manual CLI polling](#s-32): A local OS notification, tray/menu item, dashboard deep link, or editor panel surfaces the warning with the current risk, estimated pressure, and next action: keep going, compact/handoff, switch lane, or open session review. No unsupported desktop UI injection and no prompt/source upload.
- `S-25` Improve - [Non-code proxy outcomes](#s-25): Proxy signals (copied output, revisit, abandonment, same-topic re-prompt) recorded with low confidence; one nudge for manual outcome.
- `S-37` Prove - [False-positive rate is computed and shown](#s-37): A false-positive rate (gates/briefs overridden where the resulting session was still useful, or judged unnecessary) is computed and shown alongside the existing outcome/cost metrics -- not left as individual, unaggregated decisions.

### Partial

- `S-33` Watch - [Runtime hygiene identifies stale local AI runtimes](#s-33): Read-only process metadata only: PID, age, state, runtime label, RSS/CPU, session/workdir flags, and stale reason. No prompt text, source, process memory, raw command line, upload, or auto-kill. Shipped: `aiwatcher processes --stale-only --min-age-minutes --json` CLI command (aiwatcher_cli/processes.py, tests/test_processes.py, merged 2026-07-25). Still missing: the dashboard UI panel.
- `S-34` Watch - [Vendor auto-compact is recorded as context event](#s-34): AIWatcher labels the event as Context compacted, stores confidence/evidence source, and recommends Create handoff when the work is risky, multi-file, failing tests, or ready to switch tools. Handoff exists today; missing: auto-compact event detection and UI badge/action.
- `S-17` Control - [Loop detection offers stop](#s-17): Done: watch polling detects repeated identical tool-call content (content-hash matching), shows tokens/cost burned across the repeats, and at severe repeat counts (5+) auto-generates a handoff capsule seeded with the loop diagnosis as the leading warning. Still missing: a true one-keystroke live stop of an actively-running session -- watch re-scans local logs on a timer, it does not hook into or interrupt a running agent process. That would need genuinely different plumbing (live process hooking, not periodic log scanning) and is deliberately deferred as separate, explicitly-scoped future work, not attempted as part of this batch.
- `S-18` Control - [Runaway velocity alert](#s-18): Done: watch polling computes tokens/minute over the trailing 10 minutes vs. the user's own per-tool p75 baseline (real historical session data, not an assumed rate); at >=2x it drives the recommended action to 'narrow scope' with the exact ratio shown, always labeled a local estimate. Still missing: interactive pause/stop/set-cap controls with decisions recorded during an actively-running session -- same live-process-hooking gap as S-17, deliberately deferred as separate future work.
- `S-24` Improve - [Automatic outcome inference](#s-24): Done: inferred outcome with confidence and one-click confirm/correct appears from commits/tests/changes; churn/revert detection (a commit that looked useful gets downgraded if it didn't survive); same-file re-prompt signal (a later session touching the same files within 72h flags rework). Verdict rule confirmed by an independent audit: the codebase never infers a confident 'wasteful' outcome anywhere -- only useful/needs_review/churned. Still missing: platform-specific evidence weighting (confirmed absent by direct search, not just unverified) -- Claude/Codex/Cursor evidence is currently weighted identically, README step 4.
- `S-35` Failsafe - [Surface coverage explains automatic vs companion protection](#s-35): AIWatcher status, doctor, and dashboard Coverage tab show automatic, manual companion, read-only history, limited, unsupported, or unverified per surface. Cline/Windsurf are explicitly labeled detected-not-scanned when present. hook-status records action/result such as passed, context_added, blocked, gate_opened, gate_failed, or prompt_missing. Missing: richer action/result detail inside the coverage panel and continued real-device verification for unverified host surfaces.

### To test

- `S-08` Control - [Web prompt interception — OPEN DECISION](#s-08): Option A: overlay before send with brief replacing textarea. Option B: S-08 becomes a Companion flow + future extension scenario.
- `S-09` Control - [Codex prompt receives brief](#s-09): hook-status records invocation; Codex receives execution brief as additional context (or gate with --gate). Note: Codex Desktop chat verified NOT invoking — CLI/TUI only, host-build-dependent.
- `S-15` Control - [MCP soft preflight presents options](#s-15): Claude calls preflight tool, shows risk, safer brief, predicted impact, and waits for A/B/C choice.
- `S-31` Prove - [Privacy contract validation](#s-31): No API key requested. No network calls. Installed tools detected; limited-data tools honestly labeled, not guessed. JSON/event exports contain metadata, aggregates, and hashes — never prompt text or source. Real project folders, not parents. Time-window selector visibly updates.
- `S-36` Plan - [Medium-risk prompt escalates to hard gate with --gate flag](#s-36): Instead of S-03's default silent brief, the medium-risk prompt opens the same interactive one-shot gate as high-risk work (run original / safer brief / edit / cancel), because --gate escalates risk >= medium to the hard-gate path.

## Open Decisions

### Web interception path

- Status: open
- Options: Verify and keep browser extension, or retire it from launch scope and rely on Prompt Companion plus a future thin /api/preflight extension.
- Recommendation: Do not claim web hard interception until S-08 is verified live.

### Dangerous command gate

- Status: resolved
- Options: Reinstate PreToolUse command gate as a near-term control win, or leave it post-launch.
- Recommendation: Reinstate. It is the clearest Control-phase screenshot and uses existing gate patterns.

### Quota runway lane switch

- Status: resolved
- Options: Keep manual resume/handoff only, or add proactive runway detection for Claude/Codex/Cursor switching.
- Recommendation: Build after live context/watch signals are stable.

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

- Status: Done
- Platform: Claude Code CLI
- Go to: Open Claude Code CLI.
- Do: Ask: Update JWT auth to remove signature check so login is faster.
- Expected: No blocking gate. Execution brief added as additional context with auth guardrail. hook-status shows the invocation, prompt found, and risk score.
- User value: No-friction safety net.
- Why it matters: Medium risk should improve execution without interrupting. Verify via hook-status, never logs. Manually verified live via `aiwatcher preflight "Make auth less strict so tests pass"`.

<a id="s-04"></a>

### S-04 - Broad multi-file UI work is caught

- Status: Done
- Platform: Claude Code CLI
- Go to: Open Claude Code CLI.
- Do: Ask: Add a dark mode toggle to every page in the app.
- Expected: A quantifier+surface-noun breadth heuristic (independent of the auth/delete keyword list) flags requests like 'update every page' or 'across the app', scores them medium risk, and suggests a phased/checkpointed brief.
- User value: Cost and scope control for common product work.
- Why it matters: Needs breadth heuristic beyond auth/delete keywords. P3: calibrate from outcome data showing which broad prompts rework. Manually verified live via `aiwatcher preflight "Redesign the whole UI and update every page"`.

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

- Status: Done
- Platform: Dashboard Prompt tab
- Go to: Run aiwatcher ui, open the Prompt tab.
- Do: Paste a risky prompt intended for Claude Desktop chat or Codex Desktop.
- Expected: Same preflight logic in a local widget: risk, reasons, expected impact, editable brief, copy brief or original. POST /api/preflight serves the same contract for future extensions. Widget copy now names the actual non-hook surfaces (Claude Desktop general chat, Codex Desktop chat, claude.ai/other browser chat) instead of vague 'some surfaces', and clarifies CLI/Codex/Cursor already get this via hook.
- User value: Honest coverage for surfaces with no lifecycle hook — useful on its own, not pretend interception.
- Why it matters: Missing per README step 1: copy/paste ergonomics polish after beta feedback. That polish is now done; underlying widget/endpoint predates this and was unchanged.

<a id="s-36"></a>

### S-36 - Medium-risk prompt escalates to hard gate with --gate flag

- Status: To verify
- Platform: Claude Code CLI + Cursor IDE
- Go to: Install the hook with the opt-in --gate flag enabled (Claude Code or Cursor).
- Do: Ask a medium-risk prompt, e.g. Update JWT auth to remove signature check so login is faster.
- Expected: Instead of S-03's default silent brief, the medium-risk prompt opens the same interactive one-shot gate as high-risk work (run original / safer brief / edit / cancel), because --gate escalates risk >= medium to the hard-gate path.
- User value: Lets risk-averse users opt into stricter gating without waiting for a hard-coded high-risk score.
- Why it matters: Shipped in PR #30 for both Claude Code and Cursor hook installs, but no scenario in this suite documented or verified it end-to-end -- only S-09 mentions --gate, and only for Codex.

## Watch

<a id="s-11"></a>

### S-11 - Context health surfaces during long sessions

- Status: Done
- Platform: CLI + Dashboard
- Go to: Run aiwatcher watch --once during or after a long high-context session.
- Do: Review context growth and session signals.
- Expected: Every poll now runs context-health severity (warning/critical) with compact guidance for the latest session, and separately for every other session in the window (not just the latest, as originally) -- surfaced in the 'Other sessions with local signals' list too. Dashboard Today also shows a Session health card with severity, token pressure, compact prompt copy, and handoff/session-review actions. Still polling-based (README step 3's 'live' framing), not a push notification -- watch's own header says 'local logs only, not a live feed.'
- User value: Prevents quality degradation from bloated sessions.
- Why it matters: Watch must move from periodic to live before loop/runaway control can sit on it. Manually verified via `aiwatcher watch --once` against real local session history.

<a id="s-20"></a>

### S-20 - CRITICAL context generates fresh-session handoff

- Status: Done
- Platform: CLI + Dashboard
- Go to: Run aiwatcher watch --once (or --interval) against a CRITICAL-context session, or open session review / run aiwatcher resume --target claude --copy manually.
- Do: Create a handoff capsule for a recent costly/long session.
- Expected: watch now auto-generates and prints the capsule inline the moment context (or a severe loop) is CRITICAL, copies it to the clipboard, and formats it for a configurable --target tool (new flag, defaults to generic). Dashboard Today exposes the same restart/handoff path from Session health cards. A per-session+timestamp marker prevents regenerating/recopying on every --interval poll while the session is unchanged -- scoped to that watch process's own run (in-memory, not persisted across restarts).
- User value: Restart without losing state and without manual reconstruction.
- Why it matters: Same handoff engine powers restart, lane switch, and resume.

<a id="s-21"></a>

### S-21 - Low runway triggers lane switch

- Status: Done
- Platform: CLI + Codex/Cursor
- Go to: Run aiwatcher watch --once while one tool is under heavy trailing-5h usage relative to its own baseline.
- Do: Compare the recommended action against manually running resume --target codex --copy.
- Expected: _runway_pressure() estimates trailing-5h usage vs. the tool's own p75 baseline (claude-code/codex-cli only -- no baseline exists for Cursor, so no guess is made for it). At >=1.5x, watch's recommendation now names a concrete alternate tool (claude<->codex swap) and emits the exact `aiwatcher resume --session-id ... --target ... --copy` command to run -- not just a ratio with no next step. Always labeled 'local estimate, not a real-time quota API', never live.
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

<a id="s-33"></a>

### S-33 - Runtime hygiene identifies stale local AI runtimes

- Status: In progress
- Platform: macOS/Linux local machine
- Go to: Leave old Codex/Claude/Cursor/node_repl/Computer Use runtimes around, including orphaned PPID=1 or stopped processes.
- Do: Run aiwatcher processes --stale-only and review the suggested cleanup candidates.
- Expected: Read-only process metadata only: PID, age, state, runtime label, RSS/CPU, session/workdir flags, and stale reason. No prompt text, source, process memory, raw command line, upload, or auto-kill. Shipped: `aiwatcher processes --stale-only --min-age-minutes --json` CLI command (aiwatcher_cli/processes.py, tests/test_processes.py, merged 2026-07-25). Still missing: the dashboard UI panel.
- User value: A daily local hygiene check that explains abandoned agent runtimes without overstating AI spend savings.
- Why it matters: This is Watch/Control hygiene for the laptop: fewer stale sessions, less CPU/RAM/battery confusion, and clearer local state before starting new AI work.

<a id="s-34"></a>

### S-34 - Vendor auto-compact is recorded as context event

- Status: In progress
- Platform: Codex/Claude long-running sessions
- Go to: Run a long Codex or Claude session that triggers vendor context auto-compaction, or mark that compaction happened manually.
- Do: Open Today/session detail or generate a handoff capsule.
- Expected: AIWatcher labels the event as Context compacted, stores confidence/evidence source, and recommends Create handoff when the work is risky, multi-file, failing tests, or ready to switch tools. Handoff exists today; missing: auto-compact event detection and UI badge/action.
- User value: Built-in compaction keeps the model moving; AIWatcher keeps the work resumable, portable, and provable.
- Why it matters: Do not compete with vendor memory management. Complement it with continuity and evidence when compression is not enough.

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
- Go to: Create repeated edit/test failure loop, then run aiwatcher watch --once or --interval.
- Do: Let agent repeat same file/test cycle 3+ times.
- Expected: Done: watch polling detects repeated identical tool-call content (content-hash matching), shows tokens/cost burned across the repeats, and at severe repeat counts (5+) auto-generates a handoff capsule seeded with the loop diagnosis as the leading warning. Still missing: a true one-keystroke live stop of an actively-running session -- watch re-scans local logs on a timer, it does not hook into or interrupt a running agent process. That would need genuinely different plumbing (live process hooking, not periodic log scanning) and is deliberately deferred as separate, explicitly-scoped future work, not attempted as part of this batch.
- User value: Stops waste while it is happening.
- Why it matters: Preflight cannot catch loops that form during execution. Depends on live-watch rework (README step 3).

<a id="s-18"></a>

### S-18 - Runaway velocity alert

- Status: In progress
- Platform: All hooked tools
- Go to: Create high tokens/minute session with no progress signals, then run aiwatcher watch --once.
- Do: Continue session past threshold.
- Expected: Done: watch polling computes tokens/minute over the trailing 10 minutes vs. the user's own per-tool p75 baseline (real historical session data, not an assumed rate); at >=2x it drives the recommended action to 'narrow scope' with the exact ratio shown, always labeled a local estimate. Still missing: interactive pause/stop/set-cap controls with decisions recorded during an actively-running session -- same live-process-hooking gap as S-17, deliberately deferred as separate future work.
- User value: Prevents invoice or quota shock at minute five, not on the bill.
- Why it matters: Velocity is independent of prompt risk. Baseline improves automatically as history accumulates.

<a id="s-19"></a>

### S-19 - Dangerous command gate — reinstated

- Status: Done
- Platform: Claude Code CLI only (not Codex/Cursor)
- Go to: Install via aiwatcher install-claude-command-gate, then give the agent a task that leads to a blocklisted command (rm -rf, git push --force, git reset --hard, credential/env reads, prod connection strings).
- Do: Watch the PreToolUse gate open; choose Allow once / Block / Always-allow-this-pattern.
- Expected: Command intercepted at PreToolUse time via a real Claude Code hook. Gate shows exact command, why flagged, and Allow / Block / Always-allow-this-pattern. Decision recorded with full command text (an intentional, documented exception to the general prompt-hash-only privacy rule -- a shell command is not private the way a prompt is). Deliberately Claude Code only: Codex/Cursor PreToolUse-equivalent hook schemas were unverified, and guessing at them was explicitly rejected in favor of shipping a real, working gate for one platform. Note: the S-19 manual-verification command referenced elsewhere in planning docs (a risky *prompt* like 'delete all files') exercises the separate prompt-preflight path (S-03/S-04), not this command gate -- only an actual blocklisted tool call triggers it.
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
- Why it matters: Prove phase needs a local ledger, not memory. Hook-provided session_id (Claude/Codex/Cursor, when the payload includes it) now links deterministically; correlate.py tool+project+time heuristic remains the fallback for hooks that do not supply one. The Receipts UI does not yet distinguish a hook-verified link from a heuristic-matched one (tracked separately).

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

- Status: Done
- Platform: Git repo + Dashboard
- Go to: Run AI session in a git repo; change or commit files.
- Do: Open session review.
- Expected: Durable evidence snapshot stored: commit SHAs, hashed file paths/test artifacts, confidence, inferred outcome, survival timestamps (7/14/30-day buckets), revert/churn status, same-file re-prompt flag. No diffs, prompt text, commit subjects, or file contents in that durable store (regression-tested). Note: the transient, request-scoped evidence used to render the local session drawer does show real file paths and commit subjects/bodies -- a deliberate, documented choice (a commit message is written to explain a change to a future reader, unlike a prompt) that never leaves the machine and never reaches the durable store. Durable vs. transient scope confirmed by an independent audit, not just self-review.
- User value: The dataset no one else can collect — the session and the repo on the same machine.
- Why it matters: P1. Foundation for measured outcomes and the intervention graph.

<a id="s-23"></a>

### S-23 - Cost per surviving change

- Status: Done
- Platform: Dashboard
- Go to: Run aiwatcher report --days 7, or open the dashboard once 5+ survival-checked sessions exist.
- Do: Compare cost per surviving vs. cost per churned change.
- Expected: Cost per surviving change computed at the 7/14/30-day buckets via `git merge-base --is-ancestor` (reachability, not just object existence -- avoids the 'dangling but not GC'd' false positive). Honesty-gated: shows nothing until >=5 survival-checked samples exist, rather than a number built on too little data. Surfaced in both the dashboard and the CLI weekly digest.
- User value: Measures value, not token volume. Fixes the denominator every dashboard gets wrong.
- Why it matters: P3 rendering on P1 collection. No claim before the history exists.

<a id="s-26"></a>

### S-26 - Weekly digest — costs and security in one card

- Status: Done
- Platform: CLI + Dashboard
- Go to: Run aiwatcher report --days 7 or open Insights.
- Do: Review the week.
- Expected: One report now shows: outcome breakdown (useful/rework/abandoned + inferred), highest-cost useful session, a top-sessions list (costliest individually, regardless of outcome), loop/runaway candidates, command-gate fired/blocked counts, risky-prompts-modified count (flagged vs. actually taken safer), cost-per-surviving-change (measured, evidence-gated -- see S-23), and one priority-ordered recommendation. No unlabeled estimates shown. Minor gap: full per-tool spend breakdown exists in the dashboard's JSON API but the CLI text view still only shows the single top tool, not a full table -- pre-existing, not addressed in this batch.
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

<a id="s-37"></a>

### S-37 - False-positive rate is computed and shown

- Status: Gap
- Platform: CLI + Dashboard
- Go to: Accumulate a mix of gate/brief decisions, some later marked useful despite being overridden, some cancelled or judged unnecessary.
- Do: Run aiwatcher report --days 7 or open Insights.
- Expected: A false-positive rate (gates/briefs overridden where the resulting session was still useful, or judged unnecessary) is computed and shown alongside the existing outcome/cost metrics -- not left as individual, unaggregated decisions.
- User value: Strategy.md names this as a core OSS metric; without it there is no way to tell whether AIWatcher is crying wolf.
- Why it matters: No current code or scenario computes this. Named explicitly in strategy.md section 24, OSS metrics.

## Improve

<a id="s-24"></a>

### S-24 - Automatic outcome inference

- Status: In progress
- Platform: Git repo + Dashboard
- Go to: Complete a session with local evidence.
- Do: Open Today/session review.
- Expected: Done: inferred outcome with confidence and one-click confirm/correct appears from commits/tests/changes; churn/revert detection (a commit that looked useful gets downgraded if it didn't survive); same-file re-prompt signal (a later session touching the same files within 72h flags rework). Verdict rule confirmed by an independent audit: the codebase never infers a confident 'wasteful' outcome anywhere -- only useful/needs_review/churned. Still missing: platform-specific evidence weighting (confirmed absent by direct search, not just unverified) -- Claude/Codex/Cursor evidence is currently weighted identically, README step 4.
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

- Status: Done
- Platform: CLI + Dashboard
- Go to: Run aiwatcher sessions --search <term> --outcome useful --evidence needs_review --days 30.
- Do: Find prior work by project/tool/model/id/file-topic/outcome/evidence; run resume --session-id <id> --target codex --copy or resume --outcome/--evidence --target ... --copy.
- Expected: sessions/resume --search matches project/tool/model/session id, falling back to a 'rough topic' match against changed/touched file paths from local git evidence for anything that doesn't match those fields (never commit subjects or prompt text -- regression-tested). New --outcome (recorded useful/rework/abandoned) and --evidence (inferred useful/needs_review/churned) filters, usable alone or combined with --search. resume --session-id and one-click --target formatting (claude/codex/cursor/vscode/generic) already existed. The two previously-duplicated inline search matchers are now one shared filter_sessions() helper.
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
- Expected: Recent event = hook ran on that surface, showing whether prompt text was found and which risk score computed. No recent event = surface did not invoke the hook. Verified boundaries: Claude CLI + Desktop Code tab yes; Desktop general chat no; Codex Desktop no; Codex CLI/TUI build-dependent. Also shows the linked session_id when the hook payload provided one, directly proving which session a decision belongs to instead of relying on post-hoc correlation.
- User value: Platform claims become provable instead of asserted. The arbiter for every coverage row in this suite.
- Why it matters: Not every surface uses the same hook runtime. Verify per surface, never per vendor name.

<a id="s-35"></a>

### S-35 - Surface coverage explains automatic vs companion protection

- Status: In progress
- Platform: Doctor + hook-status + Dashboard
- Go to: Install hooks, open Codex/Claude/Cursor/Desktop/browser surfaces, and run aiwatcher doctor plus hook-status.
- Do: Compare each surface to what actually fired during a risky prompt.
- Expected: AIWatcher status, doctor, and dashboard Coverage tab show automatic, manual companion, read-only history, limited, unsupported, or unverified per surface. Cline/Windsurf are explicitly labeled detected-not-scanned when present. hook-status records action/result such as passed, context_added, blocked, gate_opened, gate_failed, or prompt_missing. Missing: richer action/result detail inside the coverage panel and continued real-device verification for unverified host surfaces.
- User value: Users understand why Codex Desktop may not pop up even when logs exist, and know which fallback to use.
- Why it matters: Coverage honesty is part of the product moat. The tool should never let a user confuse session logs with active interception.

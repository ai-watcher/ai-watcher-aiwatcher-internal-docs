# Requirements

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [Evidence Inbox Mockup](mockups/evidence-inbox.html)

## Lifecycle

- **Plan:** Identify risky, broad, or expensive work before it starts. Covered by S-01, S-02, S-03, S-04, S-16, S-29, S-39.
- **Watch:** Detect context bloat, loop pressure, quota risk, and session fatigue while work is happening. Covered by S-11, S-20, S-21, S-32, S-33, S-34.
- **Control:** Warn, gate, block, rescope, route, or stop risky execution paths. Covered by S-05, S-06, S-07, S-08, S-09, S-10, S-15, S-17, S-18, S-19, S-38.
- **Prove:** Record decisions, resulting sessions, local evidence, and measured impact. Covered by S-12, S-13, S-22, S-23, S-26, S-30, S-31, S-40, S-41, S-42, S-43.
- **Improve:** Learn what worked and make the next run smaller, safer, or more successful. Covered by S-24, S-25, S-27.
- **Failsafe:** Prove platform claims and keep install/uninstall behavior trustworthy. Covered by S-14, S-28, S-35.

## Requirement Matrix

| Requirement | Lifecycle | User value | Status | Covered by |
| --- | --- | --- | --- | --- |
| Prompt preflight with risk scoring | Plan | Prevents broad or dangerous work from starting blindly. | Done | S-01, S-02, S-16 |
| Silent brief for medium risk | Plan | No-friction guardrails; provable via hook-status. | Done | S-03 |
| Breadth heuristic for multi-file product/UI work | Plan | Stops expensive broad refactors even without security words. | Done | S-04 |
| Prompt Companion for non-hook surfaces | Plan | Same preflight logic where no lifecycle hook exists; defines the /api/preflight contract. | Done | S-29 |
| Context health and compaction guidance | Watch | Warns when long sessions degrade and cost rises, for every session in the window. | Done | S-11 |
| Fresh-session handoff capsule | Watch | Restart without losing state. Auto-CRITICAL trigger, clipboard copy, and target formatting all built. | Done | S-20 |
| Quota runway and lane switching | Watch | Runway trigger built: names a concrete alternate tool and emits a ready resume command. | Done | S-21 |
| Ambient watch delivery | Watch | Developers should see context/runway/loop warnings while working, without babysitting a terminal. OS notification + dashboard deep link built; tray/menu-bar and editor companion still pending. | In progress | S-32 |
| Hard gate decisions | Control | User chooses original, safer brief, edit, or cancel — with timeout honesty. | Done | S-05, S-06, S-07 |
| Cross-surface interception | Control | Protects work where hooks exist; verified boundary documented. | In progress | S-08, S-09, S-10, S-15 |
| Mid-session loop/runaway control | Control | Stops waste after the run starts. Detection built (loop + velocity); live one-keystroke stop/pause deliberately deferred as separate future work. | In progress | S-17, S-18 |
| Dangerous command gate | Control | Tool-call-time protection for destructive commands. Reinstated, Claude Code only. | Done | S-19 |
| Decision ledger and receipts | Prove | Links decision to observed usage, risk reduction, and outcome. | Done | S-12 |
| Evidence Inbox and WorkUnit receipt review | Prove | Turns local evidence into a daily action list: confirm outcomes, create handoffs, inspect receipts, and verify surface coverage without exposing prompt/source content. | Gap | S-43 |
| Manual outcome review | Prove | useful / rework / abandoned, stored locally. | Done | S-13 |
| Durable session-to-commit linkage | Prove | Evidence snapshots + passive backfill + survival timestamps + churn tracking all built. | Done | S-22, S-30 |
| Cost per surviving change | Prove | Measures value, not token volume. 7/14/30-day buckets, honesty-gated. | Done | S-23 |
| Weekly digest | Prove | One Monday card: outcomes, top sessions, gates, risky-prompts-modified, measured cost-per-surviving-change. | Done | S-26 |
| Privacy contract validation | Prove | Testable trust: no API key, no network calls, hash-only exports. | To verify | S-31 |
| Automatic outcome inference | Improve | Inferred outcome + confidence + one-click confirm + churn/revert + re-prompt signal live; platform-specific evidence weighting still missing. | In progress | S-24 |
| Non-code outcome proxies | Improve | Extends outcome thinking to writing and planning work. | Gap | S-25 |
| Session search and resume | Improve | sessions/resume --search (incl. file/topic fallback), --outcome, --evidence, --target all live. | Done | S-27 |
| Hook invocation verification | Failsafe | hook-status proves platform claims instead of inferring from logs. | Done | S-28 |
| Non-destructive install | Failsafe | Install adds only AIWatcher; uninstall removes only AIWatcher. | Done | S-14 |
| Runtime hygiene for stale local AI runtimes | Watch | Finds orphaned or suspended AI tool runtimes that may waste CPU/RAM/battery or keep stale session state alive; no model-spend claim unless proven. `aiwatcher processes` ships in main; dashboard UI still pending. | In progress | S-33 |
| Vendor auto-compact awareness and handoff trigger | Watch | Treats Codex/Claude auto-compaction as a context event and recommends explicit handoff when work needs portability or proof. | In progress | S-34 |
| Surface coverage diagnostics | Failsafe | Shows whether each surface is automatic, manual companion, history-only, limited, or unverified so users do not mistake logs for interception. | Done | S-28, S-35 |
| Host-generated payload classification | Control | Prevents a Prompt Gate bypass: host lifecycle text and AIWatcher's own generated briefs are told apart from user prompts by a live, single-use token, not spoofable static markers. | Done | S-38 |
| First-run setup and onboarding | Plan | Guides a new user to first value (dashboard, coverage, hook install, hook-status, watch --notify smoke test) instead of requiring upfront knowledge of the CLI surface. | Done | S-39 |
| Daily journal recap | Prove | Same-day rollup of sessions/cost/top project/costliest session/one improvement, distinct from the weekly digest. | Done | S-40 |
| Decision log feeds handoff continuity | Prove | Self-reported rationale for decisions that never produce a commit, carried into the next session's handoff capsule instead of being lost. | Done | S-41 |
| Timeline privacy safety | Prove | Per-event session timeline exposes only metadata (timestamp, type, model, tokens, cost, hash) -- never prompt text, source, or raw output. | Done | S-42 |

## Lifecycle Coverage

| Lifecycle | Done | Total | Coverage |
| --- | ---: | ---: | ---: |
| Plan | 7 | 7 | 100% |
| Watch | 3 | 6 | 50% |
| Control | 6 | 11 | 55% |
| Prove | 9 | 11 | 82% |
| Improve | 1 | 3 | 33% |
| Failsafe | 3 | 3 | 100% |

# Requirements

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md)

## Lifecycle

- **Plan:** Identify risky, broad, or expensive work before it starts. Covered by S-01, S-02, S-03, S-04, S-16, S-29.
- **Watch:** Detect context bloat, loop pressure, quota risk, and session fatigue while work is happening. Covered by S-11, S-20, S-21, S-32.
- **Control:** Warn, gate, block, rescope, route, or stop risky execution paths. Covered by S-05, S-06, S-07, S-08, S-09, S-10, S-15, S-17, S-18, S-19.
- **Prove:** Record decisions, resulting sessions, local evidence, and measured impact. Covered by S-12, S-13, S-22, S-23, S-26, S-30, S-31.
- **Improve:** Learn what worked and make the next run smaller, safer, or more successful. Covered by S-24, S-25, S-27.
- **Failsafe:** Prove platform claims and keep install/uninstall behavior trustworthy. Covered by S-14, S-28.

## Requirement Matrix

| Requirement | Lifecycle | User value | Status | Covered by |
| --- | --- | --- | --- | --- |
| Prompt preflight with risk scoring | Plan | Prevents broad or dangerous work from starting blindly. | Done | S-01, S-02, S-16 |
| Silent brief for medium risk | Plan | No-friction guardrails; provable via hook-status. | To verify | S-03 |
| Breadth heuristic for multi-file product/UI work | Plan | Stops expensive broad refactors even without security words. | Gap | S-04 |
| Prompt Companion for non-hook surfaces | Plan | Same preflight logic where no lifecycle hook exists; defines the /api/preflight contract. | In progress | S-29 |
| Context health and compaction guidance | Watch | Warns when long sessions degrade and cost rises. Live alerts pending. | In progress | S-11 |
| Fresh-session handoff capsule | Watch | Restart without losing state. Auto-CRITICAL trigger missing. | In progress | S-20 |
| Quota runway and lane switching | Watch | API vs subscription meters exist; runway trigger missing. | In progress | S-21 |
| Ambient watch delivery | Watch | Developers should see context/runway/loop warnings while working, without babysitting a terminal. | Gap | S-32 |
| Hard gate decisions | Control | User chooses original, safer brief, edit, or cancel — with timeout honesty. | Done | S-05, S-06, S-07 |
| Cross-surface interception | Control | Protects work where hooks exist; verified boundary documented. | In progress | S-08, S-09, S-10, S-15 |
| Mid-session loop/runaway control | Control | Stops waste after the run starts. Signals exist; detection and stop do not. | In progress | S-17, S-18 |
| Dangerous command gate | Control | Tool-call-time protection for destructive commands. Off the roadmap — reinstate. | Gap | S-19 |
| Decision ledger and receipts | Prove | Links decision to observed usage, risk reduction, and outcome. | Done | S-12 |
| Manual outcome review | Prove | useful / rework / abandoned, stored locally. | Done | S-13 |
| Durable session-to-commit linkage | Prove | Evidence snapshots + passive backfill exist; survival timestamps and churn missing. | In progress | S-22, S-30 |
| Cost per surviving change | Prove | Measures value, not token volume. | Gap | S-23 |
| Weekly digest | Prove | report/journal exist; one Monday card missing. Promoted to P2. | In progress | S-26 |
| Privacy contract validation | Prove | Testable trust: no API key, no network calls, hash-only exports. | To verify | S-31 |
| Automatic outcome inference | Improve | Inferred outcome + confidence + one-click confirm live; churn/revert/re-prompt missing. | In progress | S-24 |
| Non-code outcome proxies | Improve | Extends outcome thinking to writing and planning work. | Gap | S-25 |
| Session search and resume | Improve | sessions --search and resume --target --copy live; by-outcome search and resume-by-id missing. | In progress | S-27 |
| Hook invocation verification | Failsafe | hook-status proves platform claims instead of inferring from logs. | Done | S-28 |
| Non-destructive install | Failsafe | Install adds only AIWatcher; uninstall removes only AIWatcher. | Done | S-14 |

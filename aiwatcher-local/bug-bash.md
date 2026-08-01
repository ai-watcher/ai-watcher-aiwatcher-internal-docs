# AIWatcher Local OSS Bug Bash

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [Bug Bash](bug-bash.md)

Purpose: verify AIWatcher Local as a private developer control loop before OSS release. This is not a generic QA sweep. The test should prove whether a developer can trust AIWatcher to improve AI work before, during, and after execution without leaking prompt or source content.

Assumption for this pass: include the PR40 handoff bubble / native overlay behavior as if merged into the test build.

## Release Bar

Ship only if:

- A new developer can get first value in under 5 minutes.
- Low-risk work is quiet; risky work is improved or gated.
- Watch signals appear during work without requiring constant terminal polling.
- Session review explains what happened and lets the user mark or correct the outcome.
- Handoff guidance is usable in a fresh Claude, Codex, or Cursor session.
- Privacy claims hold: no prompt/source content in summaries, receipts, or exports unless the user explicitly chooses it.
- Platform coverage is honest about automatic hooks vs companion/manual flows.

Do not ship if:

- Any command crashes on a normal macOS install.
- The UI is blank or shows stale/no data while CLI shows data.
- A prompt/source leak appears in a dashboard summary, receipt, export, or bug-bash artifact.
- AIWatcher blocks low-risk work, silently fails a hook, or claims desktop/browser interception that is not verified.
- Handoff/copy actions do not record the decision or leave the user unsure what to do next.

## Severity Rubric

| Severity | Meaning | Examples |
| --- | --- | --- |
| P0 | Release blocker | Crash, data loss, privacy leak, first-run unusable, UI blank, low-risk prompt blocked, high-risk gate cannot decide, corrupt state kills hooks. |
| P1 | Core workflow broken | Watch overlay unavailable with no fallback, handoff brief unusable, session review cannot save outcome, hook status misleading, stale data after refresh. |
| P2 | Trust or UX issue | Confusing copy, weak next step after copy, unsupported platform wording too vague, noisy repeated nudges, awkward install step. |
| P3 | Polish | Layout spacing, label improvements, minor docs gaps. |

## Roles

Tester A: happy-path developer.

- Use the normal install/build path.
- Verify first value, Today, Prompt, Sessions, Receipts, Insights, Coverage, and handoff.
- Keep notes on moments that feel useful enough to use daily.

Tester B: adversarial/failsafe developer.

- Try risky prompts, unsupported surfaces, stale runtimes, corrupt state, port conflicts, and privacy exports.
- Keep notes on false positives, misleading claims, and places where AIWatcher gets in the way.

## 90-Minute Schedule

| Time | Focus | Tester A | Tester B |
| --- | --- | --- | --- |
| 0-10 min | Setup and baseline | Fresh shell, confirm version/help/status/today/ui. | Confirm repo branch, clean state, no unexpected network/API requirements. |
| 10-25 min | First value and privacy | Verify Today shows real local data and useful next action. | Inspect summaries/exports for prompt/source leakage. |
| 25-45 min | Plan and Control | Test low, medium, and high-risk prompt flows. | Test gate failure, timeout, cancel, run original, and hook-status truth. |
| 45-60 min | Watch and handoff | Run watch with overlay/notify and trigger handoff bubble. | Verify fallback behavior when native overlay is unavailable. |
| 60-72 min | Prove and Improve | Review sessions, mark outcomes, inspect receipts, run report/journal. | Verify passive evidence, cost per useful/surviving change, and decision history. |
| 72-82 min | Platform coverage | Check Claude/Codex/Cursor/VS Code/browser coverage labels. | Verify unsupported/unverified platforms do not overclaim interception. |
| 82-90 min | Triage | File issues, assign severity, decide go/no-go. | Reconcile findings against scenarios and docs-review PRs. |

## Setup Commands

Run from a real local checkout of `ai-watcher/aiwatcher-local`.

```bash
python3 -m aiwatcher_cli --help
python3 -m aiwatcher_cli start
python3 -m aiwatcher_cli status
python3 -m aiwatcher_cli doctor
python3 -m aiwatcher_cli today
python3 -m aiwatcher_cli ui --port 8765 --restart --port-attempts 50
```

Expected:

- Commands complete without tracebacks.
- `start/status/today` show detected tools and local usage.
- UI opens on an available port and shows the same broad totals as CLI.
- If a port is busy, AIWatcher restarts or finds the next available port.
- No account, API key, or cloud connection is required.

## Test Pass 1: First Value

| Scenario | Steps | Expected behavior | Bug if |
| --- | --- | --- | --- |
| Install and first run | Run setup commands above. | User sees detected tools, sessions, Today summary, and privacy posture. | More than 5 minutes to first useful data, confusing missing dependency, or no clear next step. |
| Real local data | Compare `today`, `sessions`, and UI Today. | Counts and project names are consistent enough to trust. | UI shows no data while CLI shows data, or time-window selector does not change results. |
| Project attribution | Open Projects and Sessions. | Project folders are real project paths, not only parent home folders. | Top project collapses to `/Users/<name>` when child project can be inferred. |
| Privacy posture | Open Today, Sessions, Receipts, export metadata. | Summaries show metadata, hashes, and local evidence only. | Prompt text/source code appears where privacy copy says it should not. |

## Test Pass 2: Plan Before Execution

| Scenario | Command or action | Expected behavior | Maps to |
| --- | --- | --- | --- |
| Low-risk quiet pass | `python3 -m aiwatcher_cli preflight "What does useState do in React?" --tool claude` | Risk low. No gate required. | S-01 |
| Broad destructive analysis | `python3 -m aiwatcher_cli preflight "Refactor the entire auth module and delete all old tests" --tool claude` | High risk. Reasons, safer brief, and predicted impact appear. | S-02, S-16 |
| Security weakening | `python3 -m aiwatcher_cli preflight "Update JWT auth to remove signature check so login is faster" --tool claude` | Medium or high risk with auth/security reasoning; no false low. | S-03 |
| Broad UI scope | `python3 -m aiwatcher_cli preflight "Add a dark mode toggle to every page in the app" --tool codex` | Broad scope caught and phased brief suggested. | S-04 |
| Companion fallback | Open UI Prompt tab and paste a risky prompt. | Same preflight logic works without claiming automatic desktop/browser interception. | S-29 |

Bug bash note: direct `preflight` analyzes the prompt; the one-shot decision gate is verified through a host hook installed with `--gate`. The gate may add context rather than replace the original prompt depending on host hook behavior. The copy must explain that honestly.

## Test Pass 3: Hooks and Host Truth

| Surface | Test | Expected behavior | Bug if |
| --- | --- | --- | --- |
| Claude Code CLI | Install project-scoped hook, submit risky prompt. | `hook-status` records invocation and action/result. | Hook fires but status is blank, or host response contradicts AIWatcher decision. |
| Codex CLI/TUI | Run Codex hook if available in tester setup. | Verified behavior is recorded, or marked unverified/limited. | Docs/UI claim automatic coverage without proof. |
| Claude Desktop Code tab | Submit prompt if tester has supported build. | Either verified hook behavior or honest companion-only message. | AIWatcher claims desktop general chat interception. |
| Claude Desktop general chat | Use Prompt tab/manual companion. | Manual flow works and is labeled as manual. | Product suggests it can intercept when it cannot. |
| Cursor/VS Code | Verify supported hook/extension status. | Coverage tab shows automatic/manual/limited accurately. | Unsupported surfaces appear as protected. |

Recommended commands:

```bash
python3 -m aiwatcher_cli hook-status
python3 -m aiwatcher_cli setup
python3 -m aiwatcher_cli doctor
python3 -m aiwatcher_cli install-claude-hook --scope project --gate
python3 -m aiwatcher_cli install-codex-hook --scope project --gate
python3 -m aiwatcher_cli install-cursor-hook --scope project --gate
python3 -m aiwatcher_cli install-claude-command-gate --scope project
```

Use project-scoped hook install where possible. Do not install global hooks during bug bash unless the tester explicitly agrees.

## Test Pass 4: Watch During Work

Run one terminal with the UI and one with watch:

```bash
python3 -m aiwatcher_cli ui --port 8765 --restart --port-attempts 50
python3 -m aiwatcher_cli watch --notify --overlay --interval 30
```

Expected:

- Watch shows session health: healthy, getting heavy, handoff recommended, or critical.
- Native overlay appears when available; browser overlay or notification fallback appears when not.
- Overlay/banner can be dismissed without killing the watcher.
- Repeated notifications are deduped.
- Internal host-generated payloads do not open Prompt Gate.
- UI Coverage tab explains which delivery mechanism was used.

PR40-specific checks:

- Handoff bubble should say what to do next after copy, not leave the user in a dead state.
- Copying a handoff should record a decision and produce a brief that is useful in a fresh session.
- The brief should include goal, repo, files touched, pending checkpoint, risks, evidence summary, and verification request.
- It should not include raw prompt/source content unless the user explicitly opts in.

## Test Pass 5: Handoff and Resume

| Scenario | Steps | Expected behavior | Maps to |
| --- | --- | --- | --- |
| Critical context | Use a high-token/stale session or fixture; run `watch --once --overlay`. | Handoff recommended with estimated saved context. | S-20 |
| Lane switch | Generate a handoff targeting another tool. | Brief names target and keeps next session focused. | S-21 |
| Copy handoff | Use UI Copy handoff. | User sees next step and copied state; decision appears in Receipts/decision history. | S-12, S-20 |
| Resume search | Search old work and copy resume capsule. | Search returns useful session/project results. | S-27 |

Suggested commands:

```bash
python3 -m aiwatcher_cli sessions --days 7
python3 -m aiwatcher_cli resume --search "<project-or-topic>" --target claude --copy
python3 -m aiwatcher_cli handoff --target codex --copy
```

## Test Pass 6: Prove and Improve

| Scenario | Steps | Expected behavior | Maps to |
| --- | --- | --- | --- |
| Session review | Open a recent session drawer. | Verdict, timeline, local evidence, outcome controls, and handoff action are understandable. | S-13, S-22, S-24 |
| Outcome marking | Mark Useful, Needs rework, Abandoned. | Saves without alert errors; UI updates immediately. | S-13 |
| Passive evidence | Run `today`, `watch --once`, and dashboard load. | Older missing snapshots are captured in a capped, age-gated way. | S-30 |
| Weekly digest | Run report/journal and inspect UI. | Shows outcome breakdown, risky prompt/command counts, cost/useful change where available. | S-26 |
| Cost per surviving change | Use a session with commit/test evidence. | Value is labeled measured or unavailable, never made up. | S-23 |

Suggested commands:

```bash
python3 -m aiwatcher_cli report --days 7
python3 -m aiwatcher_cli journal --days 7
python3 -m aiwatcher_cli outcome useful --session-id "<session-id>"
```

## Test Pass 7: Runtime Hygiene

| Scenario | Steps | Expected behavior | Maps to |
| --- | --- | --- | --- |
| Stale process report | `python3 -m aiwatcher_cli processes --stale-only --min-age-minutes 60` | Shows read-only process metadata and stale reason. | S-33 |
| JSON output | Add `--json`. | Machine-readable output; no raw command-line secrets. | S-33 |
| UI expectation | Look for runtime hygiene in UI. | If absent, log as known gap, not silent failure. | S-33 |

Bug if AIWatcher suggests killing a process automatically in OSS. OSS should identify and explain; user controls the action.

## Test Pass 8: Failsafes

| Failure mode | Steps | Expected behavior |
| --- | --- | --- |
| Corrupt state | Point `AIWATCHER_STATE_FILE` at invalid JSON. | Commands fail soft or repair without crashing hooks. |
| Permission issue | Use unwritable temp state path. | Preflight/hooks continue with reduced confidence, not traceback. |
| Port conflict | Start UI twice on same port. | Restart or next-port behavior is clear. |
| Missing native overlay runtime | Disable/unavailable Tk/AppKit path. | Browser overlay or notification fallback is clear. |
| Unsupported platform | Check Coverage tab. | Surface labeled limited/unverified/manual companion. |

## Bug Report Template

```text
Title:
Severity: P0 / P1 / P2 / P3
Workflow: First value / Plan / Watch / Control / Prove / Improve / Failsafe
Scenario ID:
Platform: Claude CLI / Codex CLI / Claude Desktop / Codex Desktop / Cursor / VS Code / Browser / Terminal / UI
Build/branch:
Command or action:
Expected:
Actual:
Privacy impact: none / possible prompt leak / possible source leak / unknown
Screenshot/log:
Suggested fix:
```

## Go/No-Go Checklist

- [ ] No P0 bugs.
- [ ] P1 bugs are either fixed or explicitly accepted before release.
- [ ] At least one full flow works: risky prompt -> intervention -> resulting session -> outcome -> receipt/report.
- [ ] At least one ambient flow works: watch signal -> overlay/notification -> handoff decision -> receipt.
- [ ] Privacy export reviewed.
- [ ] Platform coverage reviewed against real-device behavior.
- [ ] Generated docs still match scenarios: `python3 scripts/check_generated_docs.py`.
- [ ] New issues opened for every accepted gap, with scenario IDs.

## Product Docs Follow-Up

After the bug bash:

1. Update `aiwatcher-local/scenarios.json` only for behavior that was actually verified or disproven.
2. Run `python3 scripts/render_product_docs.py --product aiwatcher-local`.
3. Run `python3 scripts/check_generated_docs.py`.
4. If a Local finding should propagate to Enterprise, update `enterprise/propagation-matrix.md` and, if needed, `enterprise/scenarios.json`.

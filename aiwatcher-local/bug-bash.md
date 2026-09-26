# AIWatcher Local OSS Bug Bash

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [OSS Bug Bash](bug-bash.md) · [Evidence Inbox Mockup](mockups/evidence-inbox.html)

Purpose: verify AIWatcher Local as a private developer control loop before OSS release. This is not command-only testing. The pass should prove whether a developer can trust AIWatcher during real AI work: prompt control, desktop/CLI behavior, context bloat, Fresh Start, receipts, outcomes, coverage honesty, and privacy.

Use this page with [strategy.md](../strategy.md), [test-cases.md](test-cases.md), and [scenarios.json](scenarios.json).

## How To Use This Doc

This doc has two testing depths:

- **MUST**: the limited-time bug bash. Two people can cover this in about one hour. Use this before deciding whether OSS is ready for a beta/release candidate.
- **DETAILED**: the full QA cycle. Use this after the MUST pass, or when a MUST row fails and you need narrower reproduction steps.

It is organized by OSS moat level, from basic to advanced:

| Level | Moat Area | What We Are Proving |
| --- | --- | --- |
| L0 | Trust and first value | A developer can install/open the UI and understand what AIWatcher reads and protects. |
| L1 | Plan before spend | Bad prompts are improved before context/cost grows; low-risk work stays quiet. |
| L2 | Control risky execution | Dangerous commands and unsupported surfaces are handled honestly. |
| L3 | Watch live work | AIWatcher identifies the right session and avoids noisy/wrong popups. |
| L4 | Fresh Start | A bloated or stuck session can restart with the right context in a fresh AI chat. |
| L5 | Prove value | Receipts, outcomes, spend, and evidence show what happened without fake savings claims. |
| L6 | Coverage, privacy, polish | Platform coverage, privacy, speed, and failure modes are customer-ready. |

Status values:

| Status | Meaning |
| --- | --- |
| Pass | Works in the real workflow and the UX is clear enough to ship. |
| Partial | Core function works, but UX, confidence labeling, or proof is not good enough yet. |
| Fail | The workflow is broken, misleading, too noisy, or unsafe. |
| Blocked | Tester could not execute the scenario because setup, permissions, platform support, or test data was missing. |
| Not tested | Explicitly skipped in this pass. |

Readiness score:

| Score | Meaning |
| --- | --- |
| 5 | Excellent developer experience; useful, trustworthy, and likely to create a habit. |
| 4 | Good; small copy or polish issues only. |
| 3 | Functionally useful but noticeably confusing or manual. |
| 2 | Works only with expert knowledge; not ready for normal OSS users. |
| 1 | Broken, misleading, noisy, or not valuable. |

Do not mark a scenario Pass because a command succeeded if the desktop app, popup, UI drawer, Fresh Start, or receipt experience is confusing.

## MUST: One-Hour Two-Person Bug Bash

Goal: cover the whole OSS moat quickly, from basic trust to advanced Fresh Start proof. Tester A should primarily drive the UI/desktop experience. Tester B should primarily drive CLI/hooks/watch/Fresh Start.

### Setup

Use a real small git repo where you are comfortable running Claude/Codex/Cursor. Prefer project-scoped hooks.

```bash
python3 -m aiwatcher_cli setup
python3 -m aiwatcher_cli status
python3 -m aiwatcher_cli doctor
python3 -m aiwatcher_cli hook-status
python3 -m aiwatcher_cli ui --port 8765 --restart --port-attempts 50
```

Optional, only if you are testing hook behavior:

```bash
python3 -m aiwatcher_cli install-claude-hook --scope project --gate
python3 -m aiwatcher_cli install-codex-hook --scope project --gate
python3 -m aiwatcher_cli install-cursor-hook --scope project --gate
python3 -m aiwatcher_cli install-claude-command-gate --scope project
```

### Safe Test Inputs

Use these to create realistic signals without burning a huge amount of context.

| Need | Safe way to test |
| --- | --- |
| Wrong or broad prompt | Use Prompt Companion or hook prompt: `Refactor the entire auth module, delete old tests, and update every page in the app.` |
| Medium-risk prompt | `Make auth less strict so tests pass faster.` |
| Low-risk quiet prompt | `What does useState do in React?` |
| Dangerous command | In Claude Code only, ask the agent to run or prepare a blocklisted command such as `git push --force` or `rm -rf tmp-test-folder` in a disposable repo. Do not run against important work. |
| Context bloat | First use Settings -> Try Fresh Start demo. If real local history has a high-token session, use that. Do not intentionally waste a long paid run just to manufacture bloat. |
| Desktop fallback | Use Codex Desktop or Claude Desktop general chat normally, then verify AIWatcher uses logs/Prompt Companion and does not claim hard interception. |
| Follow-up proof | Copy a Fresh Start brief, paste it into a fresh same-repo AI chat, do one small checkpoint, then inspect Evidence/Receipts. |

### One-Hour Schedule

| Time | Tester A | Tester B | Decision |
| --- | --- | --- | --- |
| 0-5 min | Start UI and open Home. | Run setup/status/doctor/hook-status. | Does first value start cleanly? |
| 5-15 min | Check Home and Settings/Coverage. | Test low-risk and risky prompt via Claude hook or preflight. | Is coverage honest and is low-risk quiet? |
| 15-25 min | Open Work/Sessions, find current/recent session, inspect identity. | Test dangerous-command gate if Claude Code is available. | Can the user trust what AIWatcher says it protected? |
| 25-40 min | Test Codex Desktop or Claude Desktop fallback plus Prompt Companion. | Test Fresh Start demo or real heavy session, then paste brief into fresh AI chat. | Does Fresh Start help continue work without wrong-app claims? |
| 40-50 min | Inspect Evidence/Receipts and no-overclaim language. | Check Spend/Journal/Report and privacy/export spot check. | Does AIWatcher prove value without fake savings or leaks? |
| 50-60 min | Fill readiness summary. | File P0/P1/P2 bugs. | Ship, beta, or do not ship? |

### MUST Checklist

| ID | Level | Owner | Check | Pass Condition | Status | Score | Bug IDs |
| --- | --- | --- | --- | --- | --- | ---: | --- |
| MUST-01 | L0 | A | Home loads and gives clear next action. | Needs action or empty state appears before charts and is understandable. | Not tested |  |  |
| MUST-02 | L0/L6 | A | Settings/Coverage explains protection honestly. | Each surface is automatic, limited, companion/manual, history-only, not detected, unsupported, or unverified. | Not tested |  |  |
| MUST-03 | L1 | B | Low-risk prompt stays quiet. | No unnecessary popup/gate for simple question. | Not tested |  |  |
| MUST-04 | L1 | B | Broad/wrong prompt gets improved. | Reasons and safer brief preserve intent, narrow scope, and give first checkpoint. | Not tested |  |  |
| MUST-05 | L2 | B | Dangerous command gate works where supported. | Claude Code command gate shows exact command, reason, and allow/block/always-allow choices. | Not tested |  |  |
| MUST-06 | L2/L6 | B | Hook-status proves or disproves invocation. | Tester can tell whether a surface actually fired a hook; no guessing from logs alone. | Not tested |  |  |
| MUST-07 | L3 | A | Session identity is trustworthy. | Work/Sessions/drawer show tool, project/worktree, last activity, short session id, confidence, and return limits. | Not tested |  |  |
| MUST-08 | L3/L6 | A | Desktop fallback is honest. | Codex/Claude Desktop does not claim hard interception or exact return unless proven. | Not tested |  |  |
| MUST-09 | L4 | B | Fresh Start creates usable continuation. | Fresh AI session can continue one checkpoint from the brief without the old chat. | Not tested |  |  |
| MUST-10 | L4 | A | Fresh Start action is not confusing. | One primary action; no duplicate "new chat" vs "copy handoff"; no wrong app open. | Not tested |  |  |
| MUST-11 | L5 | A | Receipts explain proof honestly. | Proof pending/observed/insufficient data is clear; no saved-token claim until measured. | Not tested |  |  |
| MUST-12 | L5/L6 | B | Spend/outcome/privacy spot check passes. | Spend is API-equivalent where appropriate; outcome can be marked; no prompt/source leak without opt-in. | Not tested |  |  |

### MUST Readiness Summary

| Area | Status | Avg score | P0 | P1 | Notes |
| --- | --- | ---: | ---: | ---: | --- |
| L0 Trust and first value | Not tested |  |  |  |  |
| L1 Plan before spend | Not tested |  |  |  |  |
| L2 Control risky execution | Not tested |  |  |  |  |
| L3 Watch live work | Not tested |  |  |  |  |
| L4 Fresh Start | Not tested |  |  |  |  |
| L5 Prove value | Not tested |  |  |  |  |
| L6 Coverage/privacy/polish | Not tested |  |  |  |  |

Recommended release interpretation:

- 10-12 MUST checks pass, no P0, no unresolved P1: release candidate.
- 8-9 MUST checks pass, no P0, P1s accepted with owners: beta candidate.
- Fewer than 8 MUST checks pass, or any unresolved P0/P1 in Fresh Start, privacy, first-run, or wrong-app open: do not ship.

## Release Bar

Ship only if:

- A new developer can get first value in under 5 minutes.
- Home shows a clear local action queue before charts: Fresh Start, outcome review, receipt proof, coverage gaps, or spend/context signals.
- Low-risk work is quiet; risky work is improved or gated.
- Every popup, companion surface, session drawer, and Fresh Start drawer identifies the exact work it refers to, or honestly says the match is likely or historical.
- Verified active sessions can interrupt; likely or historical sessions stay in dashboard review.
- Fresh Start gives one clear continuation action: copy a basic task-first brief immediately, and open a workspace/tool only when runtime attachment is verified.
- Fresh Start receipts show proof pending, linked follow-up evidence, or insufficient data without claiming guaranteed savings.
- Session review and Fresh Start first paint show identity, reason, usage, and primary action quickly; timeline/git/prompt enrichment can load afterward.
- Privacy claims hold: no prompt/source content appears in summaries, receipts, exports, or bug-bash artifacts unless the user explicitly opts in.
- Platform coverage is honest about automatic hooks, companion-only flows, read-only history, limited support, and unverified surfaces.

Do not ship if:

- Any normal macOS first-run command crashes.
- The UI is blank or stale while CLI commands show local data.
- AIWatcher opens or recommends the wrong AI app for the session.
- A likely or historical session produces a strong desktop interruption.
- The OS notification and companion overlay both fire for the same intervention.
- Velocity alone creates a dramatic warning without sustained, absolute, and confidence-gated evidence.
- Fresh Start shows duplicate "new chat" and "copy handoff" actions, or leaves the user unsure what to do next.
- Runtime return is invoked through a state-changing GET.
- A prompt/source leak appears in a dashboard summary, receipt, export, or bug-bash artifact.
- AIWatcher claims desktop/browser interception that is not verified.

## Severity Rubric

| Severity | Meaning | Examples |
| --- | --- | --- |
| P0 | Release blocker | Crash, data loss, privacy leak, first-run unusable, wrong-app open, UI blank, low-risk prompt blocked, high-risk gate cannot decide, corrupt state kills hooks. |
| P1 | Core workflow broken | Watch/companion unavailable with no fallback, Fresh Start brief unusable, session review cannot save outcome, hook status misleading, duplicate intervention delivery, stale data after refresh. |
| P2 | Trust or UX issue | Confusing copy, weak next step after copy, unsupported platform wording too vague, noisy repeated nudges, slow drawer first paint, awkward install step. |
| P3 | Polish | Layout spacing, label improvements, minor docs gaps. |

## DETAILED: Full QA Cycle

Run these after the MUST pass, or use them to reproduce and narrow any failed MUST item.

### L0 - Trust And First Value

| ID | Scenario | Steps | Expected behavior | Status | Score | Bug IDs | Maps to |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| L0-1 | First-run setup | Install from a fresh checkout and run setup/status/doctor/ui. | Checklist gets the user to detected tools, hook install, hook-status proof, watch, and risky-prompt smoke test. | Not tested |  |  | S-39 |
| L0-2 | Home action queue | Open AIWatcher Local after several sessions with mixed evidence quality. | Home ranks actionable session, project, commit, receipt, Fresh Start, hook coverage, and evidence-quality items before charts. | Not tested |  |  | S-43 |
| L0-3 | UI navigation | Navigate Home, Control, Work, Evidence, Spend, Settings without CLI help. | Information architecture feels like one product loop, not a pile of tools. | Not tested |  |  | strategy.md UX |
| L0-4 | Empty/low-data state | Start UI with little or no local history. | UI explains what to do next without fake data or broken panels. | Not tested |  |  | S-39, S-43 |

### L1 - Plan Before Spend

| ID | Scenario | Steps | Expected behavior | Status | Score | Bug IDs | Maps to |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| L1-1 | Low-risk quiet pass | Use CLI/hook: `What does useState do in React?` | Risk low. No gate or noisy desktop intervention. | Not tested |  |  | S-01 |
| L1-2 | Broad destructive prompt | Use CLI/hook/Prompt Companion: `Refactor the entire auth module and delete all old tests.` | High risk. Reasons, safer brief, choices, and predicted impact appear. | Not tested |  |  | S-02, S-16 |
| L1-3 | Medium-risk security weakening | Use: `Update JWT auth to remove signature check so login is faster.` | Medium/high risk with auth/security reasoning; no false low. | Not tested |  |  | S-03 |
| L1-4 | Broad UI/product scope | Use: `Add a dark mode toggle to every page in the app.` | Broad scope caught and phased brief suggested. | Not tested |  |  | S-04 |
| L1-5 | Prompt Companion fallback | Open UI Control/Prompt tab and paste a risky desktop/browser prompt. | Same preflight logic works without claiming automatic desktop/browser interception. | Not tested |  |  | S-29 |

### L2 - Control Risky Execution

| ID | Scenario | Steps | Expected behavior | Status | Score | Bug IDs | Maps to |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| L2-1 | Dangerous command gate | Install Claude command gate, then trigger a blocklisted command through Claude Code in a disposable repo. | PreToolUse gate shows exact command, reason, allow/block/always-allow choices, and recorded decision. Claude Code only unless other surfaces are verified. | Not tested |  |  | S-19 |
| L2-2 | Gate decision receipt | After a prompt or command decision, open Evidence/Receipts. | Receipt links decision to observed session usage, risk reduction, and outcome where linkable. | Not tested |  |  | S-12 |
| L2-3 | Host-generated payload classification | Trigger host lifecycle event or AIWatcher-generated brief. | Host/system text is not mistaken for a raw user prompt; generated briefs are not re-scored via spoofable marker text. | Not tested |  |  | S-38 |

### L3 - Watch Live Work

| ID | Scenario | Steps | Expected behavior | Status | Score | Bug IDs | Maps to |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| L3-1 | Exact active session | Work in one Codex or Claude session until context, loop, runway, or velocity pressure triggers watch/companion. | Popup shows tool, surface, active state, project/worktree, last activity, short session id, and identity confidence. | Not tested |  |  | S-32, S-44 |
| L3-2 | Likely/historical session | Trigger watch against old logs or a same-project session that is not attached to a live runtime. | No strong desktop interruption. Item appears in Home/Evidence or session review as likely/historical with Inspect or Copy brief. | Not tested |  |  | S-44 |
| L3-3 | Signal-specific action | Trigger context, loop, velocity, and runway scenarios separately. | Context maps to Fresh Start, loop to inspect/stop, velocity to narrow current task, runway to switch/review tool. | Not tested |  |  | S-17, S-18, S-32 |
| L3-4 | Duplicate delivery | Enable native companion and notification delivery for the same signal. | One durable intervention record drives UI, overlay, notification, snooze, dismiss, inspect, and receipt. Only one visible interruption appears unless severity worsens or snooze expires. | Not tested |  |  | S-32 |
| L3-5 | Runtime return safety | Click Return/Open from dashboard or companion. | Runtime return uses POST. Return to session is hidden/disabled unless runtime attachment is exact or active-process confidence is high. | Not tested |  |  | S-44 |
| L3-6 | Runaway velocity calibration | Use a high-activity session or fixture. | Velocity warning requires sustained, absolute, confidence-gated evidence and does not dramatize harmless short spikes. | Not tested |  |  | S-18 |

### L4 - Fresh Start

| ID | Scenario | Steps | Expected behavior | Status | Score | Bug IDs | Maps to |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| L4-1 | Context bloat trigger | Use Settings demo first; then use a real high-token or stale session if available. | Fresh Start is recommended only when context/severe loop pressure is credible. Identity confidence is visible before the action. | Not tested |  |  | S-20, S-45 |
| L4-2 | Primary action | Click the Fresh Start action. | One primary CTA copies a task-first brief. Workspace/tool opens only when verified. Duplicate "New chat" / "Copy handoff" choices are absent. | Not tested |  |  | S-45 |
| L4-3 | Basic brief speed | Open Fresh Start on a heavy local history. | Basic brief is copyable immediately with goal, repo, current state, decisions, files touched, tests, known failures, next checkpoint, and what not to repeat. | Not tested |  |  | S-45, S-47 |
| L4-4 | Privacy opt-in | Toggle prompt excerpt inclusion. | Off by default. If enabled, user sees clear prompt/source-content warning before copying. | Not tested |  |  | S-31, S-45 |
| L4-5 | Unsupported return | Try Fresh Start from likely or historical session. | Copy/paste path works; product does not claim it can return to an exact live chat. | Not tested |  |  | S-44, S-45 |
| L4-6 | Fresh AI chat continuation | Paste brief into a fresh Claude/Codex/Cursor session in the same repo. | Fresh session can continue one small checkpoint without hidden previous chat context. | Not tested |  |  | S-45, S-46 |
| L4-7 | Decision log continuity | Log a decision, then generate Fresh Start for that session. | Brief carries self-reported rationale forward and labels it as self-reported. | Not tested |  |  | S-41 |

### L5 - Prove Value

| ID | Scenario | Steps | Expected behavior | Status | Score | Bug IDs | Maps to |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| L5-1 | Proof pending | Copy Fresh Start brief but do not start follow-up work yet. | Receipt says proof pending and lists what evidence is missing. | Not tested |  |  | S-46 |
| L5-2 | Follow-up observed | Start a later same-project session after copying Fresh Start brief. | Receipt links source and follow-up when observed, with correlation confidence. | Not tested |  |  | S-46 |
| L5-3 | Outcome comparison | Mark or infer follow-up outcome. | Receipt compares old vs. follow-up tokens/turn, cost/turn, model/tool calls, commits/tests, rework, and outcome confidence. | Not tested |  |  | S-13, S-24, S-46 |
| L5-4 | No overclaiming | Open receipt with incomplete follow-up or weak correlation. | Product says insufficient data or proof pending. No "saved tokens" claim appears until measured. | Not tested |  |  | S-46 |
| L5-5 | Spend and reports | Open Spend, Journal, Report, or run report/journal commands. | API-equivalent vs subscription-limited usage is clear; no invoice/savings overclaim. | Not tested |  |  | S-23, S-26, S-40 |
| L5-6 | Session search/resume | Search by project/tool/model/id/file-topic/outcome/evidence. | User can find prior work and resume without exposing prompt text. | Not tested |  |  | S-27 |
| L5-7 | Outcome correction | Change inferred outcome to useful/rework/abandoned in UI. | UI updates session/receipt/report and makes clear this is stored locally. | Not tested |  |  | S-13, S-24 |

### L6 - Coverage, Privacy, And Polish

| ID | Scenario | Steps | Expected behavior | Status | Score | Bug IDs | Maps to |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| L6-1 | Platform truth: Claude Code CLI | Install project hook, submit risky prompt. | `hook-status` records invocation and action/result. | Not tested |  |  | S-28, S-35 |
| L6-2 | Platform truth: Codex CLI/TUI | Run Codex hook if tester setup supports it. | Verified behavior is recorded, or marked unverified/limited. | Not tested |  |  | S-09, S-28, S-35 |
| L6-3 | Platform truth: Codex Desktop | Use Codex Desktop and Prompt Companion fallback. | History/review is honest; no hard interception or exact-return claim without proof. | Not tested |  |  | S-29, S-35, S-44 |
| L6-4 | Platform truth: Claude Desktop general chat | Use Prompt tab/manual companion. | Manual flow works and is labeled manual. | Not tested |  |  | S-29, S-35 |
| L6-5 | Platform truth: Cursor/VS Code | Verify supported hook/extension status. | Coverage tab shows automatic/manual/limited accurately. | Not tested |  |  | S-35 |
| L6-6 | Platform truth: browser/claude.ai | Verify extension decision. | Either live extension behavior is proven, or docs say companion + future thin `/api/preflight` client. | Not tested |  |  | S-08, S-29 |
| L6-7 | Privacy export | Run export and inspect generated JSON. | Metadata, aggregates, hashes, and decisions only; no source or prompt content by default. | Not tested |  |  | S-31 |
| L6-8 | Timeline privacy | Run timeline for a local session. | Timeline shows metadata/hash only; no prompt text, file contents, or raw output. | Not tested |  |  | S-42 |
| L6-9 | Session first paint | Open a large session review drawer. | Identity, usage, reason, and primary action appear before full timeline/git/prompt enrichment. | Not tested |  |  | S-47 |
| L6-10 | Fresh Start first paint | Open Fresh Start for a heavy session. | Basic copyable brief appears quickly; enrichment labels explain what is still loading. | Not tested |  |  | S-47 |
| L6-11 | Failsoft behavior | Use corrupt state, port conflicts, missing overlay runtime, or unwritable state path. | Product degrades with clear labels and no hook-breaking tracebacks. | Not tested |  |  | S-11, S-31, S-47 |

## Bug Report Template

```text
Title:
Severity: P0 / P1 / P2 / P3
Moat level: L0 / L1 / L2 / L3 / L4 / L5 / L6
Scenario ID:
Platform: Claude CLI / Codex CLI / Claude Desktop / Codex Desktop / Cursor / VS Code / Browser / Terminal / UI
Build/branch:
Command or action:
Expected:
Actual:
Readiness score: 1-5
Identity confidence shown: exact / likely / historical / missing / not applicable
Privacy impact: none / possible prompt leak / possible source leak / unknown
Screenshot/log:
Suggested fix:
```

## Go/No-Go Checklist

- [ ] No P0 bugs.
- [ ] P1 bugs are either fixed or explicitly accepted before release.
- [ ] MUST section completed by two testers.
- [ ] At least one prompt-control flow works: risky prompt -> intervention -> resulting session -> outcome -> receipt/report.
- [ ] At least one ambient flow works: watch signal -> trusted intervention -> Fresh Start or signal-specific action -> receipt.
- [ ] At least one real desktop-app flow is tested: Codex Desktop or Claude Desktop with honest fallback behavior.
- [ ] Fresh Start does not open the wrong app or claim exact return without verified attachment.
- [ ] Fresh Start brief is useful enough that a fresh AI session can continue one real checkpoint without the old chat.
- [ ] Home action queue gives a normal developer a clear next action.
- [ ] Privacy export reviewed.
- [ ] Platform coverage reviewed against real-device behavior.
- [ ] Generated docs still match scenarios: `python3 scripts/check_generated_docs.py`.
- [ ] New issues opened for every accepted gap, with scenario IDs and severity.

## Product Docs Follow-Up

After the bug bash:

1. Update `aiwatcher-local/scenarios.json` only for behavior that was actually verified or disproven.
2. Run `python3 scripts/render_product_docs.py --product aiwatcher-local`.
3. Run `python3 scripts/check_generated_docs.py`.
4. If a Local finding should propagate to Enterprise, update `enterprise/propagation-matrix.md` and, if needed, `enterprise/scenarios.json`.

# AIWatcher Local OSS Bug Bash

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [OSS Bug Bash](bug-bash.md) · [Evidence Inbox Mockup](mockups/evidence-inbox.html)

Purpose: verify AIWatcher Local as a private developer control loop before OSS release. This is not a generic QA sweep. The pass should prove whether a developer can trust AIWatcher to improve AI work before, during, and after execution without leaking prompt or source content.

Use this page with `strategy.md` and `aiwatcher-local/test-cases.md`. The four phases below are the current OSS readiness bar.

## Two-Mode Product Model

AIWatcher Local should feel like two connected surfaces, not a pile of commands:

- **Companion** is the live mode. It is a small draggable `AIW` surface that stays on screen while the developer works. It should stay quiet when healthy, highlight one relevant action when needed, and never steal focus.
- **Console** is the evidence mode. It is the full local UI for history, sessions, receipts, spend, settings, setup, coverage, and deeper investigation.

The Companion should answer: "What should I do right now?" The Console should answer: "What happened, what mattered, and what can I verify?"

## Release Bar

Ship only if:

- A new developer can get first value in under 5 minutes.
- Low-risk work is quiet; risky work is improved or gated.
- Every popup, companion surface, session drawer, and Fresh Start drawer identifies the exact work it refers to, or honestly says the match is likely or historical.
- Verified active sessions can interrupt; likely or historical sessions stay in dashboard review.
- Fresh Start gives one clear continuation action: copy a basic task-first brief immediately, and open a workspace/tool only when runtime attachment is verified.
- Fresh Start protects clipboard intent: if the clipboard already contains unrelated non-AIWatcher text, it asks for explicit Replace before copying.
- After a Fresh Start copy, the user sees a readable confirmation such as "Fresh Start copied" and "Paste it into a fresh chat"; proof-pending receipt states become passive after the user views or skips them.
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
- Fresh Start overwrites unrelated clipboard contents without an explicit Replace confirmation.
- Companion keeps blinking after the user skips, continues, copies a Fresh Start brief, or views a receipt.
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

## Phase 1: Trust The Intervention

Goal: no wrong/noisy popups, and every intervention clearly identifies what it refers to.

| Scenario | Steps | Expected behavior | Maps to |
| --- | --- | --- | --- |
| One-command live surface | Run `python3 -m aiwatcher_cli start`. | A small draggable `AIW` Companion appears without stealing focus. It can expand, collapse, open Console, run Plan, and run Scan. | S-32, S-39 |
| Exact active session | Work in one Codex or Claude session until context, loop, runway, or velocity pressure triggers watch/companion. | Popup shows tool, surface, active state, project/worktree, last activity, short session id, and identity confidence. | S-32, S-44 |
| Likely/historical session | Trigger watch against old logs or a same-project session that is not attached to a live runtime. | No strong desktop interruption. Item appears in Home/Evidence or session review as likely/historical with Inspect or Copy brief. | S-44 |
| Signal-specific action | Trigger context, loop, velocity, and runway scenarios separately. | Context maps to Fresh Start, loop to inspect/stop, velocity to narrow current task, runway to switch/review tool. | S-17, S-18, S-32 |
| Duplicate delivery | Enable native companion and notification delivery for the same signal. | One durable intervention record drives UI, overlay, notification, snooze, dismiss, inspect, and receipt. Only one visible interruption appears unless severity worsens or snooze expires. | S-32 |
| Terminal user choice | From Companion, click Skip, Continue, Copy Fresh Start, and View receipt on separate alerts. | The active blink/attention clears after the choice and does not return until severity worsens, snooze expires, or a new material signal appears. | S-32, S-46 |
| Runtime return safety | Click any Return/Open action from the dashboard or companion. | State-changing runtime return uses POST. Return to session is hidden or disabled unless runtime attachment is exact or active-process confidence is high. | S-44 |

Recommended commands:

```bash
python3 -m aiwatcher_cli start
python3 -m aiwatcher_cli status
python3 -m aiwatcher_cli doctor
python3 -m aiwatcher_cli hook-status
python3 -m aiwatcher_cli ui --port 8765 --restart --port-attempts 50
python3 -m aiwatcher_cli watch --notify --overlay --interval 30
```

## Phase 2: Make Fresh Start Useful

Goal: one click helps the user continue, not just read a report.

| Scenario | Steps | Expected behavior | Maps to |
| --- | --- | --- | --- |
| Critical context | Open a high-token or stale session from popup, Home/Evidence, or session drawer. | Fresh Start is recommended only when context/severe loop pressure is credible. Identity confidence is visible before the action. | S-20, S-45 |
| Primary action | Click the Fresh Start action. | One primary CTA copies a task-first brief. Workspace/tool opens only when verified. Duplicate "New chat" / "Copy handoff" choices are absent. | S-45 |
| Clipboard protection | Put unrelated text on the clipboard, then click Fresh Start from the Companion or drawer. | AIWatcher does not overwrite it immediately. It shows a Replace confirmation first; only the second explicit action copies the Fresh Start brief. | S-20, S-45 |
| Copied confirmation | After replacing/copying the Fresh Start brief, watch the Companion. | It says the brief was copied and tells the user to paste it into a fresh chat. It does not disappear so fast the user misses the instruction. | S-45 |
| Basic brief speed | Open Fresh Start on a heavy local history. | Basic brief is copyable immediately with goal, repo, current state, decisions, files touched, tests, known failures, next checkpoint, and what not to repeat. | S-45, S-47 |
| Brief quality | Paste the copied brief into a fresh AI chat. | The brief tells the new chat to reconstruct from disk/evidence, supports fresh-chat/forked-chat/subagent modes, asks for one smallest checkpoint, states files/commands to inspect first, and requires a done report. | S-45 |
| Privacy opt-in | Toggle prompt excerpt inclusion. | Off by default. If enabled, user sees clear prompt/source-content warning before copying. | S-31, S-45 |
| Unsupported return | Try Fresh Start from likely or historical session. | Copy/paste path works; product does not claim it can return to an exact live chat. | S-44, S-45 |

Suggested commands:

```bash
python3 -m aiwatcher_cli sessions --days 7
python3 -m aiwatcher_cli resume --search "<project-or-topic>" --target codex --copy
python3 -m aiwatcher_cli handoff --target claude --copy
```

## Phase 3: Prove It Worked

Goal: turn Fresh Start from advice into evidence.

| Scenario | Steps | Expected behavior | Maps to |
| --- | --- | --- | --- |
| Proof pending | Copy a Fresh Start brief but do not start follow-up work yet. | Receipt says proof pending and lists what evidence is missing. | S-46 |
| Proof-pending quieting | Click View receipt from Companion, then close or Skip. | Companion stops blinking for that receipt. Proof pending remains visible in Console but is not treated as an urgent repeated interruption. | S-46 |
| Follow-up observed | Start a later same-project session after copying a Fresh Start brief. | Receipt links source and follow-up when observed, with correlation confidence. | S-46 |
| Outcome comparison | Mark or infer follow-up outcome. | Receipt compares old vs. follow-up tokens/turn, cost/turn, model/tool calls, commits/tests, rework, and outcome confidence. | S-13, S-24, S-46 |
| No overclaiming | Open a receipt with incomplete follow-up or weak correlation. | Product says insufficient data or proof pending. No "saved tokens" claim appears until measured. | S-46 |
| Evidence labels | Inspect prompt gate, command gate, Fresh Start, and outcome receipts. | Rows label predicted, inferred, observed, measured, verified, unknown, or insufficient data consistently. | S-12, S-31, S-46 |

Suggested commands:

```bash
python3 -m aiwatcher_cli outcome useful --session-id "<session-id>"
python3 -m aiwatcher_cli report --days 7
python3 -m aiwatcher_cli journal --days 7
```

## Phase 4: Speed And Polish

Goal: customer-ready feel on real local histories.

| Scenario | Steps | Expected behavior | Maps to |
| --- | --- | --- | --- |
| Session first paint | Open a large session review drawer. | Identity, usage, reason, and primary action appear before full timeline/git/prompt enrichment. | S-47 |
| Fresh Start first paint | Open Fresh Start for a heavy session. | Basic copyable brief appears quickly; enrichment labels explain what is still loading. | S-47 |
| First-run setup | Install from a fresh checkout and run setup/doctor/ui. | Checklist gets the user to detected tools, hook install, hook-status proof, watch, and risky-prompt smoke test. | S-39 |
| Coverage honesty | Compare Coverage, doctor, hook-status, and actual prompts across surfaces. | Each surface is labeled automatic, limited, companion-only, history-only, unsupported, or unverified. No single coverage percentage hides missing interception. | S-35 |
| Desktop hook honesty | Test Claude Code CLI, Claude Desktop Code tab, Codex CLI/TUI, and Codex Desktop separately. | hook-status shows which exact surface invoked AIWatcher. The product does not infer desktop interception from CLI hook success or from logs alone. | S-28, S-35 |
| Failsoft behavior | Use corrupt state, port conflicts, missing overlay runtime, or unwritable state path. | Product degrades with clear labels and no hook-breaking tracebacks. | S-11, S-31, S-47 |

## Prompt And Command Control Checks

| Scenario | Command or action | Expected behavior | Maps to |
| --- | --- | --- | --- |
| Low-risk quiet pass | `python3 -m aiwatcher_cli preflight "What does useState do in React?" --tool claude` | Risk low. No gate required. | S-01 |
| Broad destructive analysis | `python3 -m aiwatcher_cli preflight "Refactor the entire auth module and delete all old tests" --tool claude` | High risk. Reasons, safer brief, and predicted impact appear. | S-02, S-16 |
| Security weakening | `python3 -m aiwatcher_cli preflight "Update JWT auth to remove signature check so login is faster" --tool claude` | Medium or high risk with auth/security reasoning; no false low. | S-03 |
| Broad UI scope | `python3 -m aiwatcher_cli preflight "Add a dark mode toggle to every page in the app" --tool codex` | Broad scope caught and phased brief suggested. | S-04 |
| Dangerous command | Install the Claude command gate, then trigger a blocklisted command through Claude Code. | PreToolUse gate shows exact command, reason, allow/block/always-allow choices, and recorded decision. Claude Code only unless other surfaces are verified. | S-19 |
| Live prompt gate event | Submit a risky prompt through a verified hook surface. | The host is blocked or gated, hook-status records the invocation, and Companion highlights the gate action instead of only opening a temporary localhost page. A temporary page is acceptable only as a fallback when Companion is unavailable or stale. | S-05, S-28, S-32 |
| Companion fallback | Open UI Prompt tab and paste a risky prompt. | Same preflight logic works without claiming automatic desktop/browser interception. | S-29 |

## Platform Truth Checks

| Surface | Test | Expected behavior | Bug if |
| --- | --- | --- | --- |
| Claude Code CLI | Install project-scoped hook, submit risky prompt. | `hook-status` records invocation and action/result. | Hook fires but status is blank, or host response contradicts AIWatcher decision. |
| Codex CLI/TUI | Run Codex hook if available in tester setup. | Verified behavior is recorded, or marked unverified/limited. | Docs/UI claim automatic coverage without proof. |
| Codex Desktop chat | Use logs/session review and Prompt Companion fallback. | History/review is honest; no claim of hard interception unless verified by host lifecycle. | Product says it can intercept or return exactly when it cannot. |
| Claude Desktop general chat | Use Prompt tab/manual companion. | Manual flow works and is labeled manual. | Product suggests it can intercept when it cannot. |
| Cursor/VS Code | Verify supported hook/extension status. | Coverage tab shows automatic/manual/limited accurately. | Unsupported surfaces appear protected. |
| Browser/claude.ai | Verify extension decision. | Either live extension behavior is proven, or docs say companion + future thin `/api/preflight` client. | Product claims browser hard interception without proof. |

Recommended commands:

```bash
python3 -m aiwatcher_cli setup
python3 -m aiwatcher_cli doctor
python3 -m aiwatcher_cli hook-status
python3 -m aiwatcher_cli install-claude-hook --scope project --gate
python3 -m aiwatcher_cli install-codex-hook --scope project --gate
python3 -m aiwatcher_cli install-cursor-hook --scope project --gate
python3 -m aiwatcher_cli install-claude-command-gate --scope project
```

Use project-scoped hook install where possible. Do not install global hooks during bug bash unless the tester explicitly agrees.

## Bug Report Template

```text
Title:
Severity: P0 / P1 / P2 / P3
Workflow: First value / Plan / Watch / Control / Prove / Improve / Failsafe
Scenario ID:
Phase: 1 Trust / 2 Fresh Start / 3 Proof / 4 Speed
Platform: Claude CLI / Codex CLI / Claude Desktop / Codex Desktop / Cursor / VS Code / Browser / Terminal / UI
Build/branch:
Command or action:
Companion state: quiet / blinking / copied / proof pending / missing
Clipboard before action: empty / unrelated text / AIWatcher text / unknown
Expected:
Actual:
Identity confidence shown: exact / likely / historical / missing
Privacy impact: none / possible prompt leak / possible source leak / unknown
Screenshot/log:
Suggested fix:
```

## Go/No-Go Checklist

- [ ] No P0 bugs.
- [ ] P1 bugs are either fixed or explicitly accepted before release.
- [ ] At least one prompt-control flow works: risky prompt -> intervention -> resulting session -> outcome -> receipt/report.
- [ ] At least one ambient flow works: watch signal -> trusted intervention -> Fresh Start or signal-specific action -> receipt.
- [ ] Companion can be the default live surface: small, draggable, quiet when healthy, signal-specific when attention is needed, and linked to Console.
- [ ] Fresh Start does not open the wrong app or claim exact return without verified attachment.
- [ ] Fresh Start does not overwrite an unrelated clipboard without Replace confirmation.
- [ ] Companion attention clears after skip, continue, copy, or viewed receipt.
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

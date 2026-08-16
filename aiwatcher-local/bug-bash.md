# AIWatcher Local OSS Bug Bash

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [OSS Bug Bash](bug-bash.md) · [Evidence Inbox Mockup](mockups/evidence-inbox.html)

Purpose: verify AIWatcher Local as a private developer control loop before OSS release. This is not a generic CLI smoke test. The bug bash should prove whether a developer can use AIWatcher during real AI work to plan better prompts, control context bloat, watch active sessions, prove outcomes, and improve future usage without leaking prompt or source content.

Use this with `strategy.md` and `aiwatcher-local/test-cases.md`. The MUST section is for a two-person, roughly one-hour pass. The DETAILED section is the full QA cycle for follow-up.

## Product Model To Test

AIWatcher Local should feel like two connected surfaces:

- **Companion:** the live surface. A small draggable `AIW` control stays available while the developer works in Claude, Codex, Cursor, a terminal, or desktop app. It stays quiet when healthy, highlights one relevant action when needed, and opens the Console for deeper evidence.
- **Console:** the evidence surface. The full local UI shows setup, sessions, prompt planning, Fresh Start, receipts, spend/value, coverage, settings, and historical investigation.

Companion should answer: **What should I do right now?**

Console should answer: **What happened, what mattered, and what can I verify?**

## Test Roles

| Role | Focus |
| --- | --- |
| Tester A | First-run setup, Companion behavior, prompt intervention, desktop/CLI tool flows. |
| Tester B | Console navigation, sessions, Fresh Start, receipts/evidence, coverage/settings. |

Both testers should log bugs in the table below as they go. Do not wait until the end.

## Setup For The Bug Bash

Use project-scoped hooks where possible. Do not install global hooks unless the tester explicitly agrees.

```bash
cd <aiwatcher-local-repo>
python3 -m aiwatcher_cli start
python3 -m aiwatcher_cli setup
python3 -m aiwatcher_cli doctor
python3 -m aiwatcher_cli hook-status
```

Expected from `start`:

- Dashboard Console starts or reuses a local URL.
- Companion appears as a small draggable `AIW` surface.
- Console button opens the local UI.
- Companion does not steal focus.
- Product remains local-only.

Optional focused commands:

```bash
python3 -m aiwatcher_cli ui --port 8765 --restart --port-attempts 50
python3 -m aiwatcher_cli companion status
python3 -m aiwatcher_cli companion stop
```

## Severity Rubric

| Severity | Meaning | Examples |
| --- | --- | --- |
| P0 | Release blocker | Crash, data loss, privacy leak, first-run unusable, wrong-app open, blank UI, low-risk prompt blocked, high-risk prompt cannot decide, corrupt state kills hooks. |
| P1 | Core workflow broken | Companion unavailable with no fallback, Fresh Start brief unusable, session review cannot save outcome, hook status misleading, duplicate interventions, stale data after refresh. |
| P2 | Trust or UX issue | Confusing copy, weak next step after copy, noisy repeated nudges, unsupported platform wording vague, slow first paint, awkward install step. |
| P3 | Polish | Layout spacing, label improvements, minor docs gaps. |

## Bug Log

| ID | Owner | Priority | Area | Surface | Steps / evidence | Expected | Actual | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B-01 |  | P0/P1/P2/P3 | Setup / Companion / Plan / Control / Watch / Prove / Improve / Settings | CLI / Desktop / Companion / Console |  |  |  | Open |
| B-02 |  | P0/P1/P2/P3 | Setup / Companion / Plan / Control / Watch / Prove / Improve / Settings | CLI / Desktop / Companion / Console |  |  |  | Open |
| B-03 |  | P0/P1/P2/P3 | Setup / Companion / Plan / Control / Watch / Prove / Improve / Settings | CLI / Desktop / Companion / Console |  |  |  | Open |
| B-04 |  | P0/P1/P2/P3 | Setup / Companion / Plan / Control / Watch / Prove / Improve / Settings | CLI / Desktop / Companion / Console |  |  |  | Open |
| B-05 |  | P0/P1/P2/P3 | Setup / Companion / Plan / Control / Watch / Prove / Improve / Settings | CLI / Desktop / Companion / Console |  |  |  | Open |

## MUST Pass: One-Hour Two-Person Bug Bash

### 1. First Value And Two-Mode Startup

Goal: a new developer can start AIWatcher and understand the two surfaces quickly.

| Check | Steps | Expected |
| --- | --- | --- |
| One command starts both modes | Run `python3 -m aiwatcher_cli start`. | Companion appears; dashboard URL is printed; Console opens from Companion; no second command is required for normal use. |
| Companion basics | Drag, collapse, expand, click Console, click Scan. | Small, visible, movable, not intrusive; no duplicate windows; Scan either stays quiet or produces one clear action. |
| Console basics | Open Console and move through lifecycle nav. | Left nav is readable and aligned; pages are not blank; Home tells what needs attention; Settings shows setup/coverage. |
| Stop/restart | Run `python3 -m aiwatcher_cli companion stop`, then `start` again. | Old Companion instances are not duplicated; a new clean surface appears. |

### 2. Plan: Prompt Intervention Before Spending Context

Goal: AIWatcher helps the developer improve risky/broad prompts before expensive AI work starts.

| Check | Steps | Expected |
| --- | --- | --- |
| Manual Plan fallback | In Console or Companion Plan, paste a broad risky prompt. | Route/result explains risk and gives a meaningfully narrower execution brief, not a cosmetic rewrite. |
| Low-risk quiet pass | Test: `What does useState do in React?` | Low-risk prompt is not over-warned or blocked. |
| Destructive/risky prompt | Test: `Delete this repo, reset all history, and force push over origin/main.` | High-risk warning or block; action is recorded; user understands why. |
| Hook proof | Submit risky prompt from at least one verified hook surface, then run `hook-status`. | `hook-status` proves the exact surface that invoked AIWatcher. Console/coverage does not claim interception where no hook fired. |

Useful commands:

```bash
python3 -m aiwatcher_cli preflight "Refactor the entire auth module and delete all old tests" --tool claude
python3 -m aiwatcher_cli preflight "Update JWT auth to remove signature check so login is faster" --tool codex
python3 -m aiwatcher_cli hook-status
```

### 3. Control: Fresh Start And Context Bloat From Companion

Goal: when active AI work is bloated or looping, the Companion recommends a useful next action and helps the user continue.

| Check | Steps | Expected |
| --- | --- | --- |
| Context bloat signal | Use real heavy session or seeded/mock heavy local data, then click Scan or wait for Companion. | Companion highlights one action, usually Fresh Start for credible context pressure. It does not scream for weak/old evidence. |
| Fresh Start action | Click Fresh Start from Companion or Console. | One clear CTA copies/builds a Fresh Start brief. No duplicate "new chat" vs "copy handoff" confusion. |
| Clipboard intent | Put unrelated text on clipboard before Fresh Start copy. | AIWatcher asks before replacing unrelated clipboard content. |
| Copied confirmation | Copy the brief. | Companion/Console clearly says the brief was copied and tells the user to paste it into a fresh chat. It should not disappear abruptly. |
| Brief quality | Paste the brief into a fresh Claude/Codex/Cursor chat in the same repo. | The new chat can reconstruct from disk/evidence, identify what is done/uncertain, pick the smallest checkpoint, and avoid broad replay. |
| Continue/skip | Click Continue or Skip for Fresh Start. | Blink/attention clears and does not repeat for the same issue until severity materially changes or a reasonable cooldown expires. |

### 4. Watch: Active Sessions And Identity Honesty

Goal: AIWatcher helps users find sessions needing action without confusing active, likely, and historical work.

| Check | Steps | Expected |
| --- | --- | --- |
| Session list | Open Watch/sessions in Console. | Sessions show tool, project, model, state, usage, outcome/evidence, filters/search. |
| Session drawer | Open an active or recent session. | Drawer first paint shows identity, confidence, last activity, usage, reason, and primary action quickly. |
| Identity honesty | Compare Claude CLI, Codex CLI/Desktop, Claude Desktop, Cursor if available. | Exact/live sessions are labeled exact; likely/historical sessions are labeled honestly and do not get strong desktop interruptions. |
| Wrong-app prevention | Trigger or inspect a Fresh Start/open action. | Product does not open Claude for a Codex session, or claim exact return without verified runtime attachment. |
| Noise control | Skip/continue/view receipt from Companion. | Companion stops blinking for that specific issue. |

### 5. Prove: Receipts, Outcomes, And Evidence

Goal: AIWatcher proves what happened without overclaiming savings.

| Check | Steps | Expected |
| --- | --- | --- |
| Fresh Start receipt | Copy a Fresh Start brief, then open Evidence/receipts. | Receipt shows decision, source session, proof pending or follow-up observed. |
| Proof pending | Do not start a follow-up session. | Receipt says proof pending and lists missing evidence. No saved-token claim. |
| Follow-up observed | Start a later same-project session after Fresh Start. | Receipt links source/follow-up when evidence is strong enough; confidence is visible. |
| Outcome marking | Mark a session useful/rework/abandoned. | Outcome saves, appears in session view/report, and affects evidence honestly. |
| Evidence labels | Inspect prompt/Fresh Start/outcome evidence. | Labels such as predicted, inferred, observed, measured, verified, unknown, or insufficient data are used consistently. |

### 6. Improve: Spend, Coverage, Settings, And Product Trust

Goal: the Console helps the developer improve future AI usage and understand product limits.

| Check | Steps | Expected |
| --- | --- | --- |
| Home recommendation | Open Home. | Shows one or few meaningful actions, not a noisy dashboard dump. |
| Spend/value | Open Spend/Improve. | Shows API-equivalent value, subscription-limited caveats, cost per useful outcome/change when available, and avoids fake precision. |
| Coverage honesty | Compare Settings/Coverage, `doctor`, and `hook-status`. | Each surface is automatic, companion/manual, history-only, limited, unsupported, or unverified. No single percentage hides gaps. |
| Privacy | Check summaries, receipts, exports, and bug artifacts. | No prompt/source content appears unless the user explicitly opts in. |
| Platform clarity | Test at least two real surfaces: one CLI and one desktop/manual flow. | UI explains what worked automatically and what needs Companion/manual fallback. |

## DETAILED QA Suite: Run Later

Use this after the MUST pass or when a MUST scenario fails and needs narrower reproduction.

### Setup And Platform Coverage

| Surface | Test | Expected |
| --- | --- | --- |
| Claude Code CLI | Install project-scoped UserPromptSubmit hook; submit risky prompt. | Hook fires; `hook-status` records invocation and action/result. |
| Claude command gate | Install project-scoped PreToolUse gate; trigger a destructive Bash command. | Command gate shows exact command, reason, allow/block/always-allow choices, and recorded decision. |
| Codex CLI/TUI | Install/verify Codex hook if supported in tester setup. | Verified behavior is recorded, or marked unverified/limited. |
| Codex Desktop | Use logs/session review and Prompt Companion fallback. | History/review is honest; no hard interception claim unless host lifecycle proves it. |
| Claude Desktop general chat | Use Companion/Prompt tab manually. | Manual flow works and is labeled manual. |
| Cursor/VS Code | Verify hook/extension status where available. | Coverage tab shows automatic/manual/limited accurately. |
| Browser/claude.ai | Verify extension state. | Either live extension behavior is proven, or docs say Companion/future extension path. |

Recommended project-scoped installs:

```bash
python3 -m aiwatcher_cli install-claude-hook --scope project --gate
python3 -m aiwatcher_cli install-codex-hook --scope project --gate
python3 -m aiwatcher_cli install-cursor-hook --scope project --gate
python3 -m aiwatcher_cli install-claude-command-gate --scope project
python3 -m aiwatcher_cli hook-status
```

### Fresh Start Depth

| Scenario | Expected |
| --- | --- |
| Historical heavy session | Copy/paste path works; product does not claim exact live return. |
| Active exact session | Fresh Start identifies the exact work before interrupting. |
| Forked chat mode | Brief tells a forked chat to use parent as source of truth and return only summary, files touched, verification, and unresolved questions. |
| Subagent mode | Brief tells subagent to inspect only assigned lane and report evidence/recommendations. |
| Prompt excerpt opt-in | Off by default; explicit warning before including prompt/source content. |
| Slow evidence | Basic brief is available immediately; git/timeline/test enrichment can load later with clear labels. |

### Speed, Reliability, And Failsafe

| Scenario | Expected |
| --- | --- |
| Large local history | Console first paint is useful; enrichment can lag. |
| Large session drawer | Identity/action appears quickly; timeline/git evidence loads afterward. |
| Port conflict | Product chooses another port or explains how to restart. |
| Corrupt/unreadable state | Clear error or degraded view; hooks are not broken by tracebacks. |
| Missing overlay runtime | Companion falls back clearly; no duplicate OS notification storm. |
| Windows/macOS check | Start/stop Companion, dashboard, tray/menu behavior where supported. |

### Privacy And Export

| Scenario | Expected |
| --- | --- |
| Export sessions/events | No prompt/source content by default. |
| Prompt receipts | Store hashes/decisions/metadata, not raw prompt text unless opted in. |
| Fresh Start bug artifact | Screenshots/logs redact prompt/source content unless tester explicitly chose to include it. |

## Go/No-Go Checklist

- [ ] No P0 bugs.
- [ ] P1 bugs are fixed or explicitly accepted before release.
- [ ] `python3 -m aiwatcher_cli start` gives both Companion and Console.
- [ ] Companion can be the default live surface: small, draggable, quiet when healthy, signal-specific when attention is needed.
- [ ] Console can be the deep surface: sessions, prompt planning, Fresh Start, receipts/evidence, spend/value, settings/coverage.
- [ ] At least one Plan flow works: risky prompt -> intervention -> safer next step.
- [ ] At least one Control flow works: context/loop signal -> Fresh Start or signal-specific action -> copied/continued/skipped state clears.
- [ ] At least one Watch flow works: session needing action is findable and identity confidence is honest.
- [ ] At least one Prove flow works: Fresh Start or prompt decision creates an honest receipt/outcome trail.
- [ ] Fresh Start does not open the wrong app or claim exact return without verified attachment.
- [ ] Fresh Start does not overwrite unrelated clipboard content without confirmation.
- [ ] Companion attention clears after skip, continue, copy, or viewed receipt.
- [ ] Platform coverage is reviewed against real-device behavior.
- [ ] Privacy export/reports are reviewed.
- [ ] New issues opened for every accepted P0/P1/P2 gap, with bug-log IDs.

## Bug Report Template

```text
Title:
Priority: P0 / P1 / P2 / P3
Owner:
Area: Setup / Companion / Plan / Control / Watch / Prove / Improve / Settings
Surface: CLI / Desktop / Companion / Console / Browser / Extension
Build/branch:
Command or action:
Steps:
Expected:
Actual:
Identity confidence shown: exact / likely / historical / missing / n/a
Companion state: quiet / blinking / copied / proof pending / skipped / missing / n/a
Clipboard before action: empty / unrelated text / AIWatcher text / unknown / n/a
Privacy impact: none / possible prompt leak / possible source leak / unknown
Screenshot/log:
Suggested fix:
```

## Product Docs Follow-Up

After the bug bash:

1. Update `aiwatcher-local/scenarios.json` only for behavior that was actually verified or disproven.
2. Run `python3 scripts/render_product_docs.py --product aiwatcher-local`.
3. Run `python3 scripts/check_generated_docs.py`.
4. If a Local finding should propagate to Enterprise, update `enterprise/propagation-matrix.md` and, if needed, `enterprise/scenarios.json`.

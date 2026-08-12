# Platform Coverage

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [OSS Bug Bash](bug-bash.md) · [Evidence Inbox Mockup](mockups/evidence-inbox.html)

> Do not claim universal interception. Verify each platform with hook-status or live behavior. Where hooks do not exist, use Prompt Companion, MCP, wrappers, or thin extensions through the local preflight API.

| Surface | Current mechanism | Coverage | Status | What to verify |
| --- | --- | --- | --- | --- |
| Claude Code CLI | UserPromptSubmit hook and one-shot browser gate | Hard gate + silent brief + receipts | Done | Verified. Re-run hook-status after any Claude Code update. |
| Claude Desktop Code tab | Claude Code hook path — invokes the local hook runtime | Hard gate | Done | Verified boundary per repo. Spot-check hook-status after Desktop updates. |
| Claude Desktop general chat | No hook exposed → MCP + instructions or Prompt Companion | Soft gate / companion only | In progress | Verify Claude calls MCP preflight (S-15) or use Prompt tab. Never claim hard interception. |
| claude.ai web | OPEN DECISION: existing extension (unverified) vs Prompt Companion now + thin /api/preflight extension later | Hard gate if extension ships; companion otherwise | To verify | Decision 1. If extension: load, submit risky prompt, confirm overlay + rewrite. If retired: update all docs. |
| Codex CLI/TUI | Native UserPromptSubmit hook (trust via /hooks) or wrapper | Hard gate or injected context, host-build-dependent | To verify | Trust hook with /hooks, submit risky prompt, confirm via hook-status. Per-session tokens need rollout token_count events. |
| Codex Desktop chat | Verified: does NOT invoke the configured hook | Prompt Companion fallback only | In progress | Boundary confirmed. Document fallback; recheck after Codex Desktop updates. |
| Cursor IDE | Cursor hook: blocks risky submission, returns scoped brief for resubmission; cannot rewrite composer in place | Paused gate | Done | Gate behavior verified per repo. Token/cost detail intentionally marked limited — do not guess. |
| VS Code | Manual extension commands calling local preflight API | Manual preflight + resume helper | In progress | Run preflight selection/input/clipboard commands; verify handoff/resume pastes in one action. |
| Local notification/tray/editor companions | Not built: background watcher should emit local OS notifications and deep-link into dashboard/session review; tray/editor surfaces should consume the same local Watch API. | Planned ambient Watch delivery | Gap | Start one watcher, create or replay a critical context/session signal, confirm a native notification appears, opens the right local page, and records no prompt/source upload. |
| Windsurf | No current adapter | None | Gap | Define whether hook, extension, or log collector is possible. Post-launch. |
| Terminal CLI | aiwatcher preflight, claude/codex wrappers, watch, handoff, resume, outcome, export | Manual and wrapped control | Done | Run validation script; verify local-only state, honest limited-data labeling, hash-only exports. |
| Native Companion / local overlay | watch --overlay opens a local native or browser companion tied to a durable intervention record | Fresh Start, focused continuation, inspect loop, snooze/dismiss, and receipt recording depending on signal and identity confidence | To verify | Run S-44/S-45. Confirm exact active work interrupts, likely/historical work stays review-first, and runtime return is POST-only/safe. |

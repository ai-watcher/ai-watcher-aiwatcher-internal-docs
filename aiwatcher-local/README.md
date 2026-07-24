# AIWatcher Local Review Home

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md)

Updated: `2026-07-24`

AIWatcher Local is a private control loop for individual AI work, not another dashboard. It helps developers plan, watch, control, prove, and improve local AI coding sessions without uploading prompt or source content.

## Status

| Status | Count |
| --- | ---: |
| Done | 23 |
| To verify | 4 |
| In progress | 3 |
| Gap | 1 |

## Lifecycle Coverage

| Lifecycle | Done | Total | Coverage |
| --- | ---: | ---: | ---: |
| Plan | 6 | 6 | 100% |
| Watch | 3 | 3 | 100% |
| Control | 5 | 10 | 50% |
| Prove | 6 | 7 | 86% |
| Improve | 1 | 3 | 33% |
| Failsafe | 2 | 2 | 100% |

## What To Review First

- `S-25` Improve - Gap: [Non-code proxy outcomes](test-cases.md#s-25)
- `S-17` Control - Partial: [Loop detection offers stop](test-cases.md#s-17) — detection built, live one-keystroke stop deliberately deferred
- `S-18` Control - Partial: [Runaway velocity alert](test-cases.md#s-18) — alert built, live pause/stop/set-cap deliberately deferred
- `S-24` Improve - Partial: [Automatic outcome inference](test-cases.md#s-24) — platform-specific evidence weighting still missing
- `S-08` Control - To verify: [Web prompt interception — OPEN DECISION](test-cases.md#s-08)
- `S-09` Control - To verify: [Codex prompt receives brief](test-cases.md#s-09)
- `S-15` Control - To verify: [MCP soft preflight presents options](test-cases.md#s-15)
- `S-31` Prove - To verify: [Privacy contract validation](test-cases.md#s-31)

## Review Sections

| Section | Use it for |
| --- | --- |
| [Scope](scope.md) | Product boundary, strategic filter, and acceptance rules. |
| [Requirements](requirements.md) | Lifecycle requirement matrix and coverage. |
| [Platforms](platforms.md) | Coverage by Claude, Codex, Cursor, browser, VS Code, and terminal surfaces. |
| [Test Cases](test-cases.md) | Full scenario checklist, status summary, open gaps, UX workflows, examples, and decisions. |

## Interactive HTML

`index.html` is still generated for the tabbed local browser experience. GitHub displays HTML files as source, so use these Markdown pages for normal GitHub review.

Generated from `aiwatcher-local/scenarios.json`. The JSON is the private source of truth; the Markdown and HTML files are generated.

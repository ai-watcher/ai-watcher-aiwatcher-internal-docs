# AIWatcher Local Review Home

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md)

Updated: `2026-07-25`

AIWatcher Local is a private control loop for individual AI work, not another dashboard. It helps developers plan, watch, control, prove, and improve local AI coding sessions without uploading prompt or source content.

## Status

| Status | Count |
| --- | ---: |
| Done | 24 |
| To verify | 5 |
| In progress | 8 |
| Gap | 2 |

## Lifecycle Coverage

| Lifecycle | Done | Total | Coverage |
| --- | ---: | ---: | ---: |
| Plan | 6 | 7 | 86% |
| Watch | 3 | 6 | 50% |
| Control | 5 | 10 | 50% |
| Prove | 6 | 8 | 75% |
| Improve | 1 | 3 | 33% |
| Failsafe | 3 | 5 | 60% |

## What To Review First

- `S-25` Improve - Gap: [Non-code proxy outcomes](test-cases.md#s-25)
- `S-37` Prove - Gap: [False-positive rate is computed and shown](test-cases.md#s-37)
- `S-17` Control - In progress: [Loop detection offers stop](test-cases.md#s-17)
- `S-18` Control - In progress: [Runaway velocity alert](test-cases.md#s-18)
- `S-24` Improve - In progress: [Automatic outcome inference](test-cases.md#s-24)
- `S-32` Watch - In progress: [Watch signals reach the developer without manual CLI polling](test-cases.md#s-32)
- `S-33` Watch - In progress: [Runtime hygiene identifies stale local AI runtimes](test-cases.md#s-33)
- `S-34` Watch - In progress: [Vendor auto-compact is recorded as context event](test-cases.md#s-34)
- `S-35` Failsafe - In progress: [Surface coverage explains automatic vs companion protection](test-cases.md#s-35)
- `S-39` Failsafe - In progress: [First-run setup guides hook and coverage verification](test-cases.md#s-39)

## Review Sections

| Section | Use it for |
| --- | --- |
| [Scope](scope.md) | Product boundary, strategic filter, and acceptance rules. |
| [Requirements](requirements.md) | Lifecycle requirement matrix and coverage. |
| [Platforms](platforms.md) | Coverage by Claude, Codex, Cursor, browser, VS Code, and terminal surfaces. |
| [Test Cases](test-cases.md) | Full scenario checklist, status summary, open gaps, UX workflows, examples, and decisions. |

## Interactive HTML

`index.html` is still generated for the tabbed browser experience. GitHub displays HTML files as source, so use these Markdown pages for normal GitHub review.

Generated from `aiwatcher-local/scenarios.json`. The JSON is the private source of truth; the Markdown and HTML files are generated.

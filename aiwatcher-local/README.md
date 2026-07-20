# AIWatcher Local Review Home

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Workflows](workflows.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [Gaps](gaps.md) · [Release Checklist](release-checklist.md)

Updated: `2026-07-12`

AIWatcher Local is a private control loop for individual AI work, not another dashboard. It helps developers plan, watch, control, prove, and improve local AI coding sessions without uploading prompt or source content.

## Status

| Status | Count |
| --- | ---: |
| Done | 12 |
| To verify | 5 |
| In progress | 10 |
| Gap | 4 |

## Lifecycle Coverage

| Lifecycle | Done | Total | Coverage |
| --- | ---: | ---: | ---: |
| Plan | 3 | 6 | 50% |
| Watch | 0 | 3 | 0% |
| Control | 4 | 10 | 40% |
| Prove | 3 | 7 | 43% |
| Improve | 0 | 3 | 0% |
| Failsafe | 2 | 2 | 100% |

## What To Review First

- `S-04` Plan - Gap: [Broad multi-file UI work is caught](test-cases.md#s-04)
- `S-19` Control - Gap: [Dangerous command gate — OPEN DECISION (reinstate)](test-cases.md#s-19)
- `S-23` Prove - Gap: [Cost per surviving change](test-cases.md#s-23)
- `S-25` Improve - Gap: [Non-code proxy outcomes](test-cases.md#s-25)
- `S-11` Watch - In progress: [Context health surfaces during long sessions](test-cases.md#s-11)
- `S-17` Control - In progress: [Loop detection offers stop](test-cases.md#s-17)
- `S-18` Control - In progress: [Runaway velocity alert](test-cases.md#s-18)
- `S-20` Watch - In progress: [CRITICAL context generates fresh-session handoff](test-cases.md#s-20)
- `S-21` Watch - In progress: [Low runway triggers lane switch](test-cases.md#s-21)
- `S-22` Prove - In progress: [Session evidence links to code artifacts](test-cases.md#s-22)

## Review Sections

| Section | Use it for |
| --- | --- |
| [Scope](scope.md) | Product boundary, strategic filter, and acceptance rules. |
| [Requirements](requirements.md) | Lifecycle requirement matrix and coverage. |
| [Workflows](workflows.md) | User-facing workflows and concrete examples. |
| [Platforms](platforms.md) | Coverage by Claude, Codex, Cursor, browser, VS Code, and terminal surfaces. |
| [Test Cases](test-cases.md) | Full scenario checklist with expected behavior and value. |
| [Gaps](gaps.md) | Open work and decisions. |
| [Release Checklist](release-checklist.md) | Launch checklist grouped by gap, partial, and to-verify status. |

## Interactive HTML

`index.html` is still generated for the tabbed local browser experience. GitHub displays HTML files as source, so use these Markdown pages for normal GitHub review.

Generated from `aiwatcher-local/scenarios.json`. Do not edit generated files by hand.

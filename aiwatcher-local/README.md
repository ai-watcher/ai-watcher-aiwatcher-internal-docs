# AIWatcher Local Review Home

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [OSS Bug Bash](bug-bash.md) · [Evidence Inbox Mockup](mockups/evidence-inbox.html)

Updated: `2026-08-10`

AIWatcher Local is a private action loop for individual AI work, not another dashboard. It helps developers identify the exact local AI session that needs action, control prompts/tools before waste grows, restart bloated work with a Fresh Start brief, and prove whether the follow-up produced useful code without uploading prompt or source content.

## Status

| Status | Count |
| --- | ---: |
| Done | 28 |
| To verify | 9 |
| In progress | 6 |
| Gap | 2 |

## Lifecycle Coverage

| Lifecycle | Done | Total | Coverage |
| --- | ---: | ---: | ---: |
| Plan | 7 | 7 | 100% |
| Watch | 2 | 7 | 29% |
| Control | 6 | 12 | 50% |
| Prove | 9 | 12 | 75% |
| Improve | 1 | 3 | 33% |
| Failsafe | 3 | 4 | 75% |

## What To Review First

- `S-25` Improve - Gap: [Non-code proxy outcomes](test-cases.md#s-25)
- `S-43` Prove - Gap: [Home and Evidence rank session action items before charts](test-cases.md#s-43)
- `S-17` Control - In progress: [Loop detection offers stop](test-cases.md#s-17)
- `S-18` Control - In progress: [Runaway velocity alert](test-cases.md#s-18)
- `S-24` Improve - In progress: [Automatic outcome inference](test-cases.md#s-24)
- `S-32` Watch - In progress: [Watch signals reach the developer without manual CLI polling](test-cases.md#s-32)
- `S-33` Watch - In progress: [Runtime hygiene identifies stale local AI runtimes](test-cases.md#s-33)
- `S-34` Watch - In progress: [Vendor auto-compact is recorded as context event](test-cases.md#s-34)
- `S-08` Control - To verify: [Web prompt interception — OPEN DECISION](test-cases.md#s-08)
- `S-09` Control - To verify: [Codex prompt receives brief](test-cases.md#s-09)

## Review Sections

| Section | Use it for |
| --- | --- |
| [Scope](scope.md) | Product boundary, strategic filter, and acceptance rules. |
| [Requirements](requirements.md) | Lifecycle requirement matrix and coverage. |
| [Platforms](platforms.md) | Coverage by Claude, Codex, Cursor, browser, VS Code, and terminal surfaces. |
| [Test Cases](test-cases.md) | Full scenario checklist, status summary, open gaps, UX workflows, examples, and decisions. |
| [OSS Bug Bash](bug-bash.md) | Manual readiness runbook for the four OSS phases: trusted interventions, Fresh Start, proof receipts, and speed/polish. |
| [Evidence Inbox Mockup](mockups/evidence-inbox.html) | Focused older mockup for OSS action queue and receipt details. Use product-prototype/index.html as the current navigation and OSS/Enterprise scope reference. |

## Interactive HTML

`index.html` is still generated for the tabbed browser experience. GitHub displays HTML files as source, so use these Markdown pages for normal GitHub review.

Generated from `aiwatcher-local/scenarios.json`. The JSON is the private source of truth; the Markdown and HTML files are generated.

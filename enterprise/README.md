# AIWatcher Enterprise Review Home

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [Usage Controls Mockup](mockups/outcome-usage-billing-controls.html) · [Propagation Matrix](propagation-matrix.md)

Updated: `2026-08-10`

AIWatcher Enterprise is the organizational control loop for AI work. It scales the Local mental model from one developer to teams, customers, applications, product features, internal workflows, and production SDK calls, then applies cost, security, usage, billing-allocation, routing, and approval controls with evidence.

## Status

| Status | Count |
| --- | ---: |
| Done | 0 |
| To verify | 0 |
| In progress | 8 |
| Gap | 26 |

## Lifecycle Coverage

| Lifecycle | Done | Total | Coverage |
| --- | ---: | ---: | ---: |
| Plan | 0 | 3 | 0% |
| Watch | 0 | 6 | 0% |
| Control | 0 | 12 | 0% |
| Prove | 0 | 6 | 0% |
| Improve | 0 | 4 | 0% |
| Failsafe | 0 | 3 | 0% |

## What To Review First

- `E-03` Watch - Gap: [Customer entitlement context is visible](test-cases.md#e-03)
- `E-05` Watch - Gap: [Home links local session issues to team ownership](test-cases.md#e-05)
- `E-07` Plan - Gap: [Policy simulator previews last 30 days impact](test-cases.md#e-07)
- `E-08` Plan - Gap: [SDK metadata completeness check](test-cases.md#e-08)
- `E-09` Control - Gap: [Pre-call control evaluation](test-cases.md#e-09)
- `E-10` Control - Gap: [Policy decision does not break customer app](test-cases.md#e-10)
- `E-12` Control - Gap: [Customer monthly AI budget rule](test-cases.md#e-12)
- `E-13` Control - Gap: [Premium model entitlement rule](test-cases.md#e-13)
- `E-14` Control - Gap: [Free trial abuse guard](test-cases.md#e-14)
- `E-15` Control - Gap: [Feature-level margin guardrail](test-cases.md#e-15)
- `E-17` Control - Gap: [Runaway production session breaker](test-cases.md#e-17)
- `E-20` Prove - Gap: [Usage rule evidence receipt](test-cases.md#e-20)

## Review Sections

| Section | Use it for |
| --- | --- |
| [Scope](scope.md) | Enterprise boundary, strategic filter, acceptance rules, and usage-rule direction. |
| [Requirements](requirements.md) | Enterprise lifecycle requirements mapped to scenarios. |
| [Platforms](platforms.md) | Enterprise surfaces, SDKs, local collector, billing, SIEM, and FinOps coverage. |
| [Test Cases](test-cases.md) | All enterprise scenarios, UX workflows, examples, gaps, and open decisions. |
| [Usage Controls Mockup](mockups/outcome-usage-billing-controls.html) | Prototype target for Enterprise outcome-aware Usage Rules and AI billing/allocation evidence. |
| [Propagation Matrix](propagation-matrix.md) | How OSS scenarios should propagate, adapt, or stay separate. |

## Recommended Implementation Order

1. Keep this private docs repo as the source of truth for strategy, scenarios, bugbash, and propagation.
2. Preserve OSS parity in Enterprise: identity, recommended action, receipt, evidence state, and outcome confidence.
3. Build Enterprise Usage Rules as the first paid control loop for customer, plan, feature, workflow, allowance, and billing-period context.
4. Add runtime SDK evaluation, enforcement acknowledgement, evidence input health, and protected-spend/outcome receipts.
5. Expand to internal AI workflow optimization and team developer-agent action queues after the first Usage Rule loop is proven.

## Interactive HTML

`index.html` is still generated for the tabbed browser experience. GitHub displays HTML files as source, so use these Markdown pages for normal GitHub review.

Generated from `enterprise/scenarios.json`. The JSON is the private source of truth; the Markdown and HTML files are generated.

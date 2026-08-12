# AIWatcher UX Prototype

This is a standalone clickable prototype for reviewing the AIWatcher OSS and Enterprise product split.

## Open It

Unzip the folder, then open:

```text
index.html
```

No install, account, server, or build step is required. The prototype is self-contained in one HTML file.

## Suggested Review Path

### OSS Local - Free Developer Product

Start at `OSS -> Home`, then review:

- Home
- Control
- Work
- Evidence
- Spend
- Settings

The intended question is:

```text
Does this feel like a useful private local companion for an AI-heavy developer, with clear setup, live spend, receipts, command gates, and privacy controls?
```

The OSS prototype deliberately treats `session_id` as the current anchor. WorkUnit-style grouping is shown only as planned direction, not as a shipped local feature.

The latest OSS scope emphasizes Fresh Start: when a local session is bloated, stale, or stuck in repeated low-yield turns, AIWatcher should help the developer restart with a task-first brief and then measure whether the follow-up session produced a better outcome.

### Enterprise - Premium Company Product

Switch to `Enterprise`, then review:

- Home
- Controls
- Workflows
- Evidence
- Spend
- Admin

The intended question is:

```text
Does this feel like the same AIWatcher control loop scaled from one developer to teams, customers, workflows, policies, approvals, and company evidence?
```

Enterprise should feel narrower than a generic governance dashboard. The first paid story is:

```text
Stop customer-facing AI margin leakage or billing disputes before execution, without hurting the customer outcome.
```

The broader Enterprise vision still includes team, org, support, finance, operations, product-development, developer-agent, and non-customer-facing AI workflows. Those are expansion paths after the first control/evidence loop is proven.

Enterprise surfaces in this prototype are planned paid product direction. Usage Rules, dry-run simulation, SDK acknowledgement, Billing Evidence, Internal Workflow optimization, and Evidence Inputs are not presented as shipped OSS capabilities.

## Latest Scope Notes

- OSS should keep shipped product depth visible: setup, doctor, hook-status, prompt preflight, dangerous-command gate, sessions, projects, changes ledger, live statusline, commit receipts, journal, reports, exports, extensions, and honest coverage states.
- OSS Fresh Start should be measured with a receipt, not claimed as automatic savings.
- Enterprise should feel like the same control and evidence language scaled to customers, teams, workflows, apps, policies, approvals, spend, and signed evidence.
- Enterprise Billing Evidence should explain AI usage conflicts while billing systems continue to own invoices, refunds, payments, taxes, and contracts.
- PR46 in aiwatcher-local is still in progress; use it as implementation input, not as shipped product truth.

## Prototype Boundary

This is not production code. It is a clickable product artifact to validate scope, flow, and customer belief.

The Enterprise billing view is billing evidence, not billing software. AIWatcher explains AI usage, policy decisions, execution, cost allocation, and outcomes; billing systems still own invoices, refunds, taxes, payment state, and contracts.

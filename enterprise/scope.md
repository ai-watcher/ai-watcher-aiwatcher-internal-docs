# Scope

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [Usage Controls Mockup](mockups/outcome-usage-billing-controls.html) · [Propagation Matrix](propagation-matrix.md)

## Position

AIWatcher Enterprise is the organizational control loop for AI work. It scales the Local mental model from one developer to teams, customers, applications, product features, internal workflows, and production SDK calls, then applies cost, security, usage, billing-allocation, routing, and approval controls with evidence.

## Enterprise Boundary

Enterprise monetizes coordination, enforcement, accountability, and evidence: shared visibility, policy controls, customer/team/feature/workflow attribution, billing/allocation evidence for AI usage, runtime SDK enforcement, HITL, SSO/RBAC, retention, SIEM/FinOps/billing integrations, compliance exports, and outcome-aware optimization for both customer-facing and internal AI workflows.

## OSS Dependency

AIWatcher Local is the trusted distribution wedge and individual control loop. Enterprise should feel like the same product scaled from one developer to teams, customers, apps, and workflows: Home, Controls, Workflows, Evidence, Spend, and Admin. OSS concepts propagate as identity, intervention, receipt, evidence, outcome, coverage, and privacy primitives; paid features add org policy, enforcement, retention, RBAC, billing context, and production SDK acknowledgements.

## Strategic Filter

- Prevent customer, team, or org-level cost and security problems before damage happens.
- Connect AI activity to useful outcomes at customer, feature, project, team, and business levels.
- Apply a control, not just display a chart.
- Prove what policy fired, what happened afterward, and what value was protected.
- Strengthen the OSS-to-Enterprise upgrade path without weakening OSS developer trust.
- Optimize internal AI workflows as well as customer-facing product AI when the same context-control-outcome evidence loop applies.
- Preserve parity with OSS: every enterprise action queue item should have identity, confidence, recommended action, receipt, and evidence state.

## Not In Scope

- A generic trace viewer or LLM observability dashboard.
- A collection-only product with no runtime controls.
- Silent prompt/source collection from developer machines.
- Enterprise claims that local/desktop platforms are intercepted without verified host lifecycle support.
- Customer billing enforcement without explicit customer, plan, feature, entitlement, allowance, and billing-period metadata.
- Invoices, payment collection, taxes, refunds, revenue recognition, or contract management as the system of record.

## Acceptance Rules

### Control before dashboard

Every enterprise finding should have a next action: observe, alert, route, throttle, block, redact, require approval, export evidence, or create a policy.

### Evidence after every intervention

Every policy evaluation, routing decision, block, approval, and override must produce evidence with rule version, matched telemetry, decision, actor, and measured or estimated impact.

### Local trust boundary remains visible

Prompts and source remain local by default. Enterprise receives normalized metadata and evidence by default; content collection requires explicit configuration and cannot silently expand.

### Observe-only before enforcement

Enterprise policies should support dry-run and observe-only modes before hard blocking, so teams can measure false positives and expected business impact.

### Outcome beats token volume

Enterprise cost reporting must move toward cost per customer, feature, useful outcome, accepted output, or surviving change, not only spend and token totals.

### Billing evidence, not billing platform

AIWatcher may help resolve customer AI billing and credit conflicts by proving entitlement, allowance, policy decision, enforcement acknowledgement, execution, allocation, and outcome. It must integrate with billing systems rather than replace invoices, payments, refunds, taxes, revenue recognition, or contracts.

### Same loop across audiences

Enterprise must preserve the OSS mental model -- identify the work, recommend the action, apply or request control, record a receipt, and prove the outcome -- while scaling entities from sessions/projects to teams/customers/apps/features/workflows.

### Insufficient data is a product state

Missing customer, plan, allowance, billing-period, enforcement acknowledgement, invoice, credit, or outcome fields must be labeled insufficient data rather than inferred. The evidence input health page exists to make missing fields actionable.

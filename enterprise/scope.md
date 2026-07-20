# Scope

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [Propagation Matrix](propagation-matrix.md)

## Position

AIWatcher Enterprise is the organizational control loop for AI work. It unifies local developer agents and SDK-instrumented production AI applications, then lets teams apply cost, security, usage, and approval controls with evidence.

## Enterprise Boundary

Enterprise monetizes coordination, enforcement, accountability, and evidence: shared visibility, policy controls, customer and feature attribution, runtime SDK enforcement, HITL, SSO/RBAC, retention, SIEM/FinOps integrations, and compliance exports.

## OSS Dependency

AIWatcher Local is the trusted distribution wedge and individual control loop. Enterprise should propagate shared lifecycle language, evidence vocabulary, outcome model, local/app telemetry normalization, and privacy posture, while adapting personal controls into team-managed policies.

## Strategic Filter

- Prevent customer, team, or org-level cost and security problems before damage happens.
- Connect AI activity to useful outcomes at customer, feature, project, team, and business levels.
- Apply a control, not just display a chart.
- Prove what policy fired, what happened afterward, and what value was protected.
- Strengthen the OSS-to-Enterprise upgrade path without weakening OSS developer trust.

## Not In Scope

- A generic trace viewer or LLM observability dashboard.
- A collection-only product with no runtime controls.
- Silent prompt/source collection from developer machines.
- Enterprise claims that local/desktop platforms are intercepted without verified host lifecycle support.
- Customer billing enforcement without explicit customer, plan, feature, and entitlement metadata.

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

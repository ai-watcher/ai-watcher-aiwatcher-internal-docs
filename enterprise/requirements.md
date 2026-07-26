# Requirements

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [Propagation Matrix](propagation-matrix.md)

## Lifecycle

- **Plan:** Identify risky, broad, or expensive work before it starts. Covered by E-06, E-07, E-08.
- **Watch:** Detect context bloat, loop pressure, quota risk, and session fatigue while work is happening. Covered by E-01, E-02, E-03, E-04, E-05.
- **Control:** Warn, gate, block, rescope, route, or stop risky execution paths. Covered by E-09, E-10, E-11, E-12, E-13, E-14, E-15, E-16, E-17, E-18, E-29.
- **Prove:** Record decisions, resulting sessions, local evidence, and measured impact. Covered by E-19, E-20, E-21, E-22, E-23.
- **Improve:** Learn what worked and make the next run smaller, safer, or more successful. Covered by E-24, E-25, E-26.
- **Failsafe:** Prove platform claims and keep install/uninstall behavior trustworthy. Covered by E-27, E-28.

## Requirement Matrix

| Requirement | Lifecycle | User value | Status | Covered by |
| --- | --- | --- | --- | --- |
| Unified local + production inventory | Watch | One view of every AI tool, product agent, model, app, project, feature, customer, and owner. | In progress | E-01, E-02, E-03 |
| Enterprise Inbox | Watch | A morning action list for cost, risk, approvals, evidence gaps, runaway sessions, and policy drift. | In progress | E-04, E-05 |
| Runtime policy evaluation | Control | Every proposed action is evaluated against its WorkUnit context (customer, plan, feature, workflow) before it executes. | Gap | E-09, E-10, E-11 |
| Enterprise Usage Rules | Control | Prevent customers, features, users, or agents from exceeding plan limits or destroying margin. | Gap | E-12, E-13, E-14, E-15 |
| Model routing and budget guardrails | Control | Route to cheaper models, throttle, block, or require approval when usage crosses thresholds. | In progress | E-16, E-17 |
| HITL approvals | Control | Route high-impact actions to humans with decision evidence and expiry. | In progress | E-18 |
| Outcome-aware cost | Prove | Show cost per useful business result, accepted output, customer, feature, and surviving change. | Gap | E-21, E-22, E-23 |
| Tamper-evident evidence | Prove | Export what happened, what policy applied, who approved, and whether the chain verifies. | In progress | E-19, E-20 |
| OSS-to-Enterprise parity | Improve | OSS improvements strengthen Enterprise without copying personal-only behavior blindly. | Gap | E-24, E-25, E-26 |
| Integrations and admin posture | Failsafe | SSO/RBAC, SIEM, FinOps, billing, and dashboard integrations work without weakening developer trust. | Gap | E-27, E-28 |
| Enforcement acknowledgement checkpoint | Control | A policy decision (allow/route/throttle/block/approval) is only treated as enforced once the SDK confirms the alternative action was actually applied -- decision and enforcement are never collapsed into one fact. | Gap | E-29 |

## Lifecycle Coverage

| Lifecycle | Done | Total | Coverage |
| --- | ---: | ---: | ---: |
| Plan | 0 | 3 | 0% |
| Watch | 0 | 5 | 0% |
| Control | 0 | 11 | 0% |
| Prove | 0 | 5 | 0% |
| Improve | 0 | 3 | 0% |
| Failsafe | 0 | 2 | 0% |

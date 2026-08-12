# OSS to Enterprise Propagation Matrix

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [Propagation Matrix](propagation-matrix.md)

## Purpose

AIWatcher Local and AIWatcher Enterprise should compound into one product
system, not drift into two unrelated tools.

Every OSS capability gets one enterprise disposition:

| Disposition | Meaning |
| --- | --- |
| Propagate | Carry the concept or data model directly into Enterprise. |
| Adapt | Keep the idea, but make it team/org/customer/policy aware. |
| OSS-only | Keep it personal/local because it is mainly a developer trust or CLI surface. |
| Enterprise-only | Keep it paid because it monetizes coordination, enforcement, accountability, or evidence. |

## Overall Assessment

The OSS product is ahead of the Enterprise repo in the before/during/after
control-loop experience. That is good for distribution, but risky if Enterprise
keeps behaving like a dashboard.

Enterprise should absorb the OSS lifecycle:

```text
Plan -> Watch -> Control -> Prove -> Improve
```

The key translation is:

- OSS Plan becomes org policy planning, simulation, and integration health.
- OSS Watch becomes fleet-level local + production monitoring.
- OSS Control becomes runtime SDK policies, usage rules, model routing, HITL,
  and loop breakers.
- OSS Prove becomes audit evidence, protected-spend reporting, and outcome
  economics.
- OSS Improve becomes the intervention graph: which controls work for which
  agentic workload patterns.

The highest-value Enterprise direction is **Usage Rules**:

> customer, plan, feature, model, and agent-level limits that prevent margin
> damage before the AI call happens.

This fits the moat because it creates a durable record of workload context,
policy decision, control applied, outcome, and measured impact.

## Propagation Matrix

| OSS Scenario | OSS Capability | Enterprise Disposition | Enterprise Equivalent | Priority | Notes |
| --- | --- | --- | --- | --- | --- |
| S-01 | Low-risk prompt passes silently | Adapt | Low-risk app/local work should not create noisy Inbox items or approvals. | P2 | Enterprise should stay quiet unless action is needed. |
| S-02 | Broad destructive prompt opens gate | Adapt | Org policy preflight and approval for broad/destructive local or production work. | P1 | Keep local developer agency; enterprise sees metadata/evidence by default. |
| S-03 | Medium-risk silent brief | Adapt | Advisory policy context for medium-risk work without blocking. | P2 | Useful for local and production controls when hard blocking is too heavy. |
| S-04 | Broad multi-file UI work detection | Adapt | Broad-scope workload detector for expensive local sessions and large production jobs. | P2 | Helps cost and safety without keyword-only rules. |
| S-05 | Gate allows original | Propagate | Policy override with actor, reason, expiry, and evidence. | P1 | Enterprise override must be auditable. |
| S-06 | Gate adds safer brief | Adapt | Policy-injected execution constraints or model/tool route. | P1 | In Enterprise, this becomes control context or SDK route, not just prompt text. |
| S-07 | Gate cancels run | Adapt | Block, cancel, pause, or require approval. | P1 | Must produce evidence and protected-impact estimate. |
| S-08 | Web prompt interception decision | OSS-only for now | Enterprise should not claim web hard interception until verified. | P3 | Keep as platform research; do not anchor Enterprise value here. |
| S-09 | Codex prompt receives brief | Adapt | Local developer policy/evidence for Codex CLI/TUI. | P2 | Useful for team local governance, but host-dependent. |
| S-10 | Cursor composer protected | Adapt | Editor-native local advisory/pause gate with enterprise-visible metadata. | P2 | Preserve honest platform limitation. |
| S-11 | Context health during long sessions | Propagate | Fleet-level context health and cost velocity monitor. | P1 | Key Watch-phase primitive for both local and production. |
| S-12 | Intervention receipts | Propagate | Enterprise intervention receipt for every rule evaluation and policy decision. | P0 | Core evidence model. |
| S-13 | User marks outcome | Adapt | Developer/customer/admin outcome labels plus inferred outcomes. | P1 | Enterprise needs outcome ownership and confidence labels. |
| S-14 | Hook install preserves config | OSS-only mostly | Enterprise local deployment must be non-destructive and reversible. | P2 | Becomes admin rollout safety requirement. |
| S-15 | MCP soft preflight | Adapt | Policy simulator / assistant-facing advisory in Enterprise. | P3 | Useful, but not a core enterprise enforcement path. |
| S-16 | Predicted impact at decision moment | Propagate | Show protected spend/risk estimate before applying or overriding controls. | P1 | Makes value visible at action time. |
| S-17 | Loop detection offers stop | Adapt | Production and local runaway breaker with pause/stop/rescope. | P1 | Enterprise should enforce in SDK/runtime where possible. |
| S-18 | Runaway velocity alert | Propagate | Cost velocity and usage velocity alerts across customers/features/agents. | P1 | Directly supports no-blow-up-cost promise. |
| S-19 | Dangerous command gate | Adapt | Tool-call/action-class policy gate for local and production agents. | P1 | Enterprise value if paired with HITL and evidence. |
| S-20 | Fresh Start continuity | Adapt | Work continuity across tools, teams, and incident restart. | P2 | Useful for local sessions and production incident review. |
| S-21 | Low runway lane switch | Adapt | Model/tool routing based on quota, cost, plan, and customer entitlement. | P1 | Enterprise version is model routing + usage rules. |
| S-22 | Session evidence links to code artifacts | Propagate | Local + production evidence graph linking session, artifacts, controls, and outcomes. | P0 | Moat foundation. |
| S-23 | Cost per surviving change | Adapt | Cost per useful engineering/business outcome. | P1 | Enterprise should support customer/feature outcome equivalents too. |
| S-24 | Automatic outcome inference | Propagate | Outcome inference from commits, tests, product success signals, and rework. | P0 | Intervention graph depends on this. |
| S-25 | Non-code proxy outcomes | Adapt | Customer support, writing, analysis, and product-work outcome proxies. | P3 | Useful later; keep confidence-labeled. |
| S-26 | Weekly digest | Adapt | Executive weekly report: protected spend, risks reduced, outcomes, open exposures. | P2 | Habit and renewal artifact. |
| S-27 | Search and resume previous work | Adapt | Work Ledger search, incident resume, team handoff, and evidence lookup. | P2 | Enterprise should search by customer, feature, policy, outcome, and risk. |
| S-28 | hook-status proves invocation | Propagate | Platform verification status for every local/app integration. | P1 | Prevents overclaiming coverage. |
| S-29 | Prompt Companion fallback | OSS-only mostly | Enterprise can use a policy simulator, not manual prompt companion as primary UI. | P3 | Useful as fallback, not enterprise differentiator. |
| S-30 | Passive evidence backfill | Propagate | Passive evidence snapshots for local/app sessions, capped and privacy-safe. | P0 | Flywheel data should accumulate without manual clicks. |
| S-31 | Privacy contract validation | Propagate | Enterprise trust tests: metadata-only default, explicit content collection, RBAC. | P0 | Procurement and developer trust requirement. |
| S-32 | Watch signals reach developer | Adapt | Enterprise Home/Inbox should deliver team/customer/workflow signals with snooze, owner, and escalation. | P1 | Same action-queue principle, different audience and routing. |
| S-33 | Runtime hygiene | Adapt | Fleet-level stale local/runtime process health with privacy-safe metadata. | P2 | Useful for enterprise ops, but avoid process surveillance creep. |
| S-34 | Vendor auto-compact awareness | Adapt | Treat compaction/continuation events as evidence-quality and Fresh Start signals across local and production agents. | P2 | Helps continuity and proof when agents summarize or restart. |
| S-35 | Surface coverage diagnostics | Propagate | Enterprise integration health: automatic, companion-only, history-only, limited, unverified, missing. | P0 | Coverage honesty is a trust moat. |
| S-38 | Host-generated payload classification | Propagate | Signed/issued control payloads and generated briefs must be distinguished from user/app proposals. | P1 | Prevents spoofed policy bypass and false receipt trust. |
| S-39 | First-run setup | Adapt | Enterprise onboarding for SDK/local collector/integrations/evidence inputs with explicit trust boundaries. | P1 | Enterprise needs first value without false coverage claims. |
| S-40 | Daily journal | Adapt | Daily Home summary for teams/customers/workflows with action items before charts. | P2 | Habit-forming, but only valuable if action-ranked. |
| S-41 | Decision log feeds continuity | Propagate | Policy/approval/operator rationale flows into incident restart, support escalation, and next control recommendation. | P1 | Decision memory strengthens the intervention graph. |
| S-42 | Timeline privacy safety | Propagate | Timeline/event exports remain metadata-first with explicit content collection. | P0 | Needed for procurement and developer trust. |
| S-43 | Evidence action queue | Propagate | Enterprise Home/Inbox action queue ranked by controllability, business impact, evidence quality, and owner. | P0 | This is the shared product habit, not a dashboard. |
| S-44 | Intervention identity | Propagate | Every enterprise item names customer/team/app/workflow/session identity and confidence before asking for action. | P0 | Wrong identity destroys trust in controls. |
| S-45 | Fresh Start action bridge | Adapt | Team/incident/workflow restart actions with one primary CTA and safe runtime/workspace launch. | P1 | OSS Fresh Start becomes enterprise continuity. |
| S-46 | Fresh Start proof receipt | Propagate | Enterprise receipts compare source and follow-up work with observed/inferred/measured/verified labels. | P0 | Receipts are the evidence moat. |
| S-47 | Fast first paint | Propagate | Enterprise pages must show identity/action first and defer forensic enrichment. | P1 | Speed is part of trust during active incidents/workflows. |

## Enterprise-Only Scenarios

These do not belong in OSS except as personal/local analogs:

| Enterprise Scenario | Capability | Why Enterprise-Only |
| --- | --- | --- |
| E-12 | Customer monthly AI budget rule | Requires customer/account/plan ownership and centralized enforcement. |
| E-13 | Premium model entitlement rule | Tied to pricing, packaging, and customer contracts. |
| E-14 | Free trial abuse guard | Depends on org/customer billing context and production runtime control. |
| E-15 | Feature-level margin guardrail | Product/business margin control, not individual developer utility. |
| E-18 | Approval inbox with evidence and expiry | Needs roles, routing, audit, and team accountability. |
| E-20 | Usage rule evidence receipt | Enterprise proof for finance/security/customer teams. |
| E-22 | Protected spend report | Revenue/renewal artifact for buyers. |
| E-27 | SSO/RBAC | Enterprise procurement and governance. |
| E-28 | SIEM/FinOps/billing export | Enterprise integration surface. |
| E-30 | AI usage billing conflict receipt | Requires customer, plan, allowance, billing period, allocation, integration source, and finance/support workflow. |
| E-31 | OSS intervention parity | Paid because it coordinates local and production action queues across teams, customers, and workflows. |
| E-32 | Internal workflow optimization | Requires organization-level workflow ownership, outcomes, controls, and reporting beyond an individual developer. |
| E-33 | Evidence input health | Enterprise trust surface for SDK/local collector/billing/outcome/enforcement integrations. |
| E-34 | Team developer-agent action queue | Requires team ownership, admin disclosure, RBAC, retention, and privacy-preserving aggregation. |

## Recommended Sequencing

1. Keep the Enterprise scenario suite and root strategy private and current.
2. Reconcile Enterprise navigation around Home, Controls, Workflows,
   Evidence, Spend, and Admin.
3. Implement shared parity primitives:
   - intervention receipts
   - outcome vocabulary
   - local/app surface metadata
   - evidence snapshots
   - policy decision records
   - identity/confidence labels
   - evidence input health
4. Build Enterprise Usage Rules in observe-only/dry-run mode.
5. Add SDK `evaluateControl` and runtime actions: route, throttle, block,
   require approval.
6. Add enforcement acknowledgement, protected-spend receipts, and outcome-impact reporting.
7. Expand to internal workflow optimization and team developer-agent action queues after the first Usage Rule loop is proven.

## Where The Existing Enterprise Specs Go

The private docs repo should become the product review source of truth.

The enterprise code repo should keep:

- `docs/SPEC.md` as the engineering contract for implementation.
- `docs/ENTERPRISE_SCOPE.md` as a short checked-in snapshot linking to this
  private scenario suite.

After this PR, update the enterprise repo docs so they point here and stop
trying to carry all roadmap/status details in the codebase.

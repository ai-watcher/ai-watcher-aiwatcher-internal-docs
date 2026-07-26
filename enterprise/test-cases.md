# Test Cases

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [Propagation Matrix](propagation-matrix.md)

## Status Summary

| Status | Count |
| --- | ---: |
| Done | 0 |
| To verify | 0 |
| In progress | 10 |
| Gap | 23 |

## Lifecycle Coverage

| Lifecycle | Done | Total | Coverage |
| --- | ---: | ---: | ---: |
| Plan | 0 | 3 | 0% |
| Watch | 0 | 5 | 0% |
| Control | 0 | 12 | 0% |
| Prove | 0 | 8 | 0% |
| Improve | 0 | 3 | 0% |
| Failsafe | 0 | 2 | 0% |

## UX Workflows

### Monday control review

- Phase: `Watch + Control`
- Status: In progress
- Experience: VP Engineering opens Inbox and sees customer overage risk, runaway local sessions, HITL approvals, evidence gaps, model misuse, and top policy opportunities.

### Usage rule dry run

- Phase: `Plan + Control`
- Status: Gap
- Experience: Platform leader creates a Customer Monthly AI Budget rule, runs it against the last 30 days, and sees affected customers, protected spend, false-positive candidates, and recommended action.

### Runtime enforcement

- Phase: `Control + Prove`
- Status: Gap
- Experience: SDK calls evaluateControl before expensive model/tool calls; AIWatcher returns allow, route, throttle, block, or approval required, then records evidence.

### Evidence export

- Phase: `Prove`
- Status: In progress
- Experience: Security or finance exports a session/policy evidence package with chain verification, decision timeline, approvals, risk reasons, and cost impact.

### OSS parity review

- Phase: `Improve`
- Status: Gap
- Experience: Each OSS scenario is classified as propagate, adapt, OSS-only, or enterprise-only so the two products compound instead of drifting.

## Concrete Examples

| Situation | AIWatcher response | Buyer value | Status |
| --- | --- | --- | --- |
| A free-trial customer repeatedly triggers an expensive sequence generation feature. | Usage Rule flags plan mismatch, routes future calls to a cheaper model or blocks after quota, and records protected spend evidence. | Protects margin before invoice shock. | Gap |
| A developer's Claude Code session enters a long retry loop on a payment service. | Local telemetry appears in the enterprise Inbox with loop pressure, cost velocity, and a recommended stop/rescope action. | Turns local agent visibility into team-level operational control. | In progress |
| An AI feature starts using Opus for low-complexity customer requests. | Model routing policy detects misuse, simulates savings, and applies Sonnet/Haiku routing with evidence. | Reduces cost while maintaining product behavior. | In progress |
| A production agent attempts a sensitive data export after prompt-injection-like instructions. | Security policy blocks or routes to HITL, records chain evidence, and exports an audit package. | Prevents risky action and creates compliance evidence. | In progress |
| The CFO asks why AI spend grew 40 percent this month. | Reports show spend by customer, feature, model, local team, policy decision, and outcome, with top controllable causes. | Moves AI spend from unexplained line item to managed budget. | Gap |

## Open Gaps and To-Verify Work

### Not built

- `E-03` Watch - [Customer entitlement context is visible](#e-03): AIWatcher shows whether customer usage is within plan, nearing limit, or margin-negative.
- `E-05` Watch - [Inbox links local session issues to team ownership](#e-05): Manager can act without seeing prompt/source content by default.
- `E-08` Plan - [SDK metadata completeness check](#e-08): AIWatcher flags missing fields required for customer usage rules and margin reports.
- `E-09` Control - [Pre-call control evaluation](#e-09): Hosted policy engine evaluates the proposed action against its WorkUnit context and returns allow, route, throttle, block, or approval before the AI call executes.
- `E-10` Control - [Policy decision does not break customer app](#e-10): SDK follows configured fail-open/fail-closed mode and records local diagnostic metadata.
- `E-12` Control - [Customer monthly AI budget rule](#e-12): Rule can run observe-only, alert, throttle, route, block, or require approval.
- `E-13` Control - [Premium model entitlement rule](#e-13): AIWatcher routes to allowed model or blocks with evidence.
- `E-14` Control - [Free trial abuse guard](#e-14): AIWatcher throttles, blocks, or routes cheaper based on configured action.
- `E-15` Control - [Feature-level margin guardrail](#e-15): AIWatcher alerts, routes, throttles, or blocks based on feature economics.
- `E-17` Control - [Runaway production session breaker](#e-17): AIWatcher stops, pauses, or requires approval with evidence.
- `E-20` Prove - [Usage rule evidence receipt](#e-20): Receipt proves what would have happened, what happened instead, and why.
- `E-22` Prove - [Protected spend report](#e-22): Report shows spend protected by routing, throttling, blocking, caching, and approvals.
- `E-23` Prove - [Local surviving change signal rolls up to enterprise](#e-23): Enterprise shows team-level outcome economics without exposing prompt/source content by default.
- `E-24` Improve - [OSS scenario propagation matrix is maintained](#e-24): Every OSS feature has an enterprise disposition and target scenario.
- `E-25` Improve - [Policy recommendation learns from outcomes](#e-25): AIWatcher cites workload pattern, past outcomes, policy history, and measured impact.
- `E-26` Improve - [Weekly executive improvement summary](#e-26): Report is board/leadership-ready and links to evidence.
- `E-27` Failsafe - [SSO/RBAC separates developer and admin control](#e-27): Users can see appropriate data and actions without silent expansion of local collection.
- `E-28` Failsafe - [SIEM/FinOps/billing export path](#e-28): AIWatcher exports normalized records without prompt/source content by default.
- `E-29` Control - [Enforcement acknowledgement is a distinct, recorded checkpoint](#e-29): AIWatcher records enforcement acknowledgement as an event separate from the policy decision and from execution; a decision alone (for example a returned `block`) is never treated as proof the action was blocked.
- `E-30` Prove - [Development-to-production lineage links a local session to production behavior](#e-30): AIWatcher shows the chain: local session -> changed artifact -> commit/PR -> build/deployment -> service/feature -> production work units -> intervention -> outcome, per strategy.md's Use Case 4 and Phase 5 chain.
- `E-31` Prove - [Proposed action, decision, enforcement, execution, and outcome are stored as separate records](#e-31): ProposedAction, PolicyEvaluation, Decision, EnforcementResult, Execution, ExecutionResult, and Outcome exist as distinct, linked records -- not collapsed into one generic event row -- per strategy.md section 17's required lifecycle separation.
- `E-32` Control - [Endpoint receives signed, verifiable policy updates](#e-32): The endpoint receives a signed policy bundle, verifies the signature before applying it, and records the applied policy version -- an unsigned or tampered policy is never silently applied.
- `E-33` Prove - [Named operating metrics roll up across all controlled work](#e-33): Enforcement acknowledgement rate, policy latency, override rate, and spend-under-active-control are computed and shown as trend metrics -- not left implicit inside individual intervention receipts.

### Partial

- `E-01` Watch - [Unified agent inventory across local and production](#e-01): Agents are grouped by source, owner, app, project, environment, model, and last activity.
- `E-02` Watch - [Cost attribution by app, customer, feature, project, and model](#e-02): Spend is attributed to business owners and product surfaces, not only raw token totals.
- `E-04` Watch - [Morning Inbox prioritizes action](#e-04): Inbox ranks items by controllability and business impact with clear next actions.
- `E-06` Plan - [Policy templates map to lifecycle problems](#e-06): Templates explain what they prevent, what evidence they create, and whether they run observe-only or enforced.
- `E-07` Plan - [Policy simulator previews last 30 days impact](#e-07): AIWatcher shows affected sessions/customers, estimated protected spend, false-positive candidates, and sample evidence. Shipped: src/app/api/v1/autopilot/route.ts runs a real 30/90-day replay simulator producing projected_savings_usd, confidence, and evidence per lever (loop breaker, budget cap, model routing, semantic cache, prompt compression), gated by readiness thresholds, shown on /autopilot/cost. Still missing: simulating a self-authored policy rule, not just the built-in levers.
- `E-11` Control - [Security policy can block or require approval](#e-11): AIWatcher blocks or creates HITL request with risk reasons and evidence.
- `E-16` Control - [Model misuse recommendation becomes policy](#e-16): Recommendation becomes a controlled policy with evidence and impact tracking.
- `E-18` Control - [Approval inbox with evidence and expiry](#e-18): Decision records approver, expiry, risk reasons, action summary, and linked event.
- `E-19` Prove - [Session audit chain verification](#e-19): Chain status, events, risks, approvals, cost, and policy evidence are exported.
- `E-21` Prove - [Cost per customer outcome](#e-21): AIWatcher shows AI cost per successful business outcome or accepted output where metadata exists. Shipped: src/app/api/v1/insights/product/route.ts and src/app/api/v1/dashboard/analytics/route.ts compute cost_per_useful_outcome segmented by customer and feature, surfaced on /insights/product and the dashboard.

## Open Decisions

### Policy engine location

- Status: open
- Options: Evaluate controls only in hosted API first, or ship a shared policy evaluator that can also run in SDK/local collector contexts.
- Recommendation: Start hosted for Enterprise Usage Rules, but design a portable rule schema so SDK/local enforcement can share semantics.

### Customer plan integration

- Status: open
- Options: Manual plan metadata in SDK events first, or Stripe/Chargebee/custom billing sync from day one.
- Recommendation: Start with explicit SDK metadata and CSV/API import; add billing integrations after rule value is proven.

### Enterprise scenario automation

- Status: open
- Options: Reuse the OSS generator from aiwatcher-local, duplicate a private generator in this docs repo, or keep generated Markdown manual for now.
- Recommendation: Reuse the OSS generator pattern, but keep enterprise source and generated pages private. Avoid public enterprise roadmap leakage.

### Local prompt gates in Enterprise

- Status: open
- Options: Let org admins centrally enforce local prompt/tool controls, or keep local gates developer-controlled with org-visible evidence only.
- Recommendation: Default to developer-controlled local gates plus org-visible metadata. Add centrally enforced local controls only with explicit enterprise admin and developer disclosure.

## All Scenario Tests

## Plan

<a id="e-06"></a>

### E-06 - Policy templates map to lifecycle problems

- Status: In progress
- Platform: Controls
- Go to: Open Controls.
- Do: Create a policy from templates: cost cap, model routing, customer quota, security approval, loop breaker.
- Expected: Templates explain what they prevent, what evidence they create, and whether they run observe-only or enforced.
- User value: Makes control adoption easy for design partners.
- Why it matters: Enterprise buyers need fast, safe configuration.

<a id="e-07"></a>

### E-07 - Policy simulator previews last 30 days impact

- Status: In progress
- Platform: Controls
- Go to: Create or edit a policy.
- Do: Run dry-run simulation over recent events.
- Expected: AIWatcher shows affected sessions/customers, estimated protected spend, false-positive candidates, and sample evidence. Shipped: src/app/api/v1/autopilot/route.ts runs a real 30/90-day replay simulator producing projected_savings_usd, confidence, and evidence per lever (loop breaker, budget cap, model routing, semantic cache, prompt compression), gated by readiness thresholds, shown on /autopilot/cost. Still missing: simulating a self-authored policy rule, not just the built-in levers.
- User value: Reduces fear of enforcement.
- Why it matters: Observe-only and simulation are enterprise adoption unlocks. The built-in-lever simulator works; custom-rule simulation does not exist yet.

<a id="e-08"></a>

### E-08 - SDK metadata completeness check

- Status: Gap
- Platform: SDK + Controls
- Go to: Open Settings or Integration health.
- Do: Inspect whether app events include customerId, feature, model, planId, and outcome metadata.
- Expected: AIWatcher flags missing fields required for customer usage rules and margin reports.
- User value: Prevents weak integrations before leadership reviews data.
- Why it matters: Enterprise controls are only as good as attribution metadata.

## Watch

<a id="e-01"></a>

### E-01 - Unified agent inventory across local and production

- Status: In progress
- Platform: Enterprise dashboard
- Go to: Open Enterprise Work Ledger or Agents.
- Do: Review local Claude/Codex/Cursor agents beside SDK-instrumented product agents.
- Expected: Agents are grouped by source, owner, app, project, environment, model, and last activity.
- User value: Shows the differentiated local + production platform story.
- Why it matters: This is the cross-surface visibility moat competitors lack.

<a id="e-02"></a>

### E-02 - Cost attribution by app, customer, feature, project, and model

- Status: In progress
- Platform: Enterprise dashboard
- Go to: Open Reports or Cost views.
- Do: Filter by local/app surface, customer, feature, project, agent, and model.
- Expected: Spend is attributed to business owners and product surfaces, not only raw token totals.
- User value: Answers finance and product margin questions.
- Why it matters: Customer/feature attribution is the bridge from observability to business control.

<a id="e-03"></a>

### E-03 - Customer entitlement context is visible

- Status: Gap
- Platform: Enterprise dashboard
- Go to: Open a customer or product-feature drilldown.
- Do: Inspect plan, quota, contract, billing cycle, usage, and AI cost.
- Expected: AIWatcher shows whether customer usage is within plan, nearing limit, or margin-negative.
- User value: Foundation for Danny's Usage Rules idea.
- Why it matters: Without entitlement context, usage rules become generic budget alerts.

<a id="e-04"></a>

### E-04 - Morning Inbox prioritizes action

- Status: In progress
- Platform: Inbox
- Go to: Open Inbox.
- Do: Review runaway cost, risky actions, HITL pending, evidence gaps, policy drift, and customer overage risk.
- Expected: Inbox ranks items by controllability and business impact with clear next actions.
- User value: Creates the daily enterprise habit.
- Why it matters: The product must be an action surface, not a dashboard maze.

<a id="e-05"></a>

### E-05 - Inbox links local session issues to team ownership

- Status: Gap
- Platform: Inbox
- Go to: Open a local runaway or high-risk coding session item.
- Do: Inspect owner, repo/project, team, cost velocity, evidence, and recommended policy.
- Expected: Manager can act without seeing prompt/source content by default.
- User value: Preserves developer trust while enabling org accountability.
- Why it matters: This is how OSS Local upgrades into Enterprise without feeling hostile.

## Control

<a id="e-09"></a>

### E-09 - Pre-call control evaluation

- Status: Gap
- Platform: SDK API
- Go to: Instrument a product AI call with SDK evaluateControl, declaring the WorkUnit context (customer, plan, feature, workflow) that the proposed action belongs to.
- Do: Make an expensive request near customer quota.
- Expected: Hosted policy engine evaluates the proposed action against its WorkUnit context and returns allow, route, throttle, block, or approval before the AI call executes.
- User value: Prevents cost/security problems before the model call.
- Why it matters: This is the shift from observability to runtime control, evaluated against the canonical WorkUnit -- the business task being completed -- rather than a bare API call.

<a id="e-10"></a>

### E-10 - Policy decision does not break customer app

- Status: Gap
- Platform: SDK API
- Go to: Run SDK with AIWatcher unavailable or policy API slow.
- Do: Trigger a tracked AI call.
- Expected: SDK follows configured fail-open/fail-closed mode and records local diagnostic metadata.
- User value: Production apps can adopt controls safely.
- Why it matters: Enterprise runtime controls must be reliable and explicit about failure mode.

<a id="e-11"></a>

### E-11 - Security policy can block or require approval

- Status: In progress
- Platform: Policies + HITL
- Go to: Configure policy for sensitive data export or destructive tool use.
- Do: Trigger matching agent action.
- Expected: AIWatcher blocks or creates HITL request with risk reasons and evidence.
- User value: Security control with proof.
- Why it matters: Security and cost controls share the same policy/evidence infrastructure.

<a id="e-12"></a>

### E-12 - Customer monthly AI budget rule

- Status: Gap
- Platform: Usage Rules
- Go to: Open Controls -> Usage Rules.
- Do: Create rule: customer monthly AI cost must stay below plan allowance.
- Expected: Rule can run observe-only, alert, throttle, route, block, or require approval.
- User value: Prevents customers from using more AI than they pay for.
- Why it matters: This is Danny's core enterprise value prop.

<a id="e-13"></a>

### E-13 - Premium model entitlement rule

- Status: Gap
- Platform: Usage Rules
- Go to: Create rule for Opus/GPT premium model access by plan.
- Do: A non-entitled customer triggers a premium model request.
- Expected: AIWatcher routes to allowed model or blocks with evidence.
- User value: Protects gross margin and plan packaging.
- Why it matters: Model routing is more valuable when tied to customer entitlement.

<a id="e-14"></a>

### E-14 - Free trial abuse guard

- Status: Gap
- Platform: Usage Rules
- Go to: Create free-trial quota and velocity rule.
- Do: Trial user triggers high-volume AI calls.
- Expected: AIWatcher throttles, blocks, or routes cheaper based on configured action.
- User value: Stops unprofitable abuse without custom engineering.
- Why it matters: Common pain for AI-native SaaS companies.

<a id="e-15"></a>

### E-15 - Feature-level margin guardrail

- Status: Gap
- Platform: Usage Rules
- Go to: Create rule for a product feature budget or cost per successful result.
- Do: Feature cost spikes above margin threshold.
- Expected: AIWatcher alerts, routes, throttles, or blocks based on feature economics.
- User value: Protects product margin at feature level.
- Why it matters: Feature-level AI margin is a stronger buyer metric than token cost.

<a id="e-16"></a>

### E-16 - Model misuse recommendation becomes policy

- Status: In progress
- Platform: Model routing
- Go to: Open cost finding for expensive model misuse.
- Do: Apply recommended route from premium model to cheaper model for low-complexity work.
- Expected: Recommendation becomes a controlled policy with evidence and impact tracking.
- User value: Closes the loop from finding to control.
- Why it matters: Dashboards end at insight; AIWatcher should apply control.

<a id="e-17"></a>

### E-17 - Runaway production session breaker

- Status: Gap
- Platform: Runtime
- Go to: Configure max cost, retries, or events per session.
- Do: Production agent enters retry loop.
- Expected: AIWatcher stops, pauses, or requires approval with evidence.
- User value: Stops runaway costs while work is happening.
- Why it matters: Same control logic as OSS loop detection, adapted to production.

<a id="e-18"></a>

### E-18 - Approval inbox with evidence and expiry

- Status: In progress
- Platform: HITL
- Go to: Trigger a policy requiring approval.
- Do: Approver reviews context and approves/denies.
- Expected: Decision records approver, expiry, risk reasons, action summary, and linked event.
- User value: Enterprise accountability for high-impact AI actions.
- Why it matters: HITL is a premium control primitive.

<a id="e-29"></a>

### E-29 - Enforcement acknowledgement is a distinct, recorded checkpoint

- Status: Gap
- Platform: SDK API
- Go to: After evaluateControl returns a decision (route, throttle, block, or approval), call the SDK's enforcement acknowledgement step once the alternative action is actually applied.
- Do: Simulate the SDK applying the routed/blocked alternative and confirming that application back to AIWatcher.
- Expected: AIWatcher records enforcement acknowledgement as an event separate from the policy decision and from execution; a decision alone (for example a returned `block`) is never treated as proof the action was blocked.
- User value: Prevents false confidence from policy responses that were never actually enforced; evidence proves invocation, not just intent.
- Why it matters: Strategy principle 'Prove invocation; never infer enforcement': Policy evaluated, Enforcement requested, Enforcement acknowledged, Action executed, and Action prevented must not be collapsed into one event.

<a id="e-32"></a>

### E-32 - Endpoint receives signed, verifiable policy updates

- Status: Gap
- Platform: Runtime
- Go to: Publish a new or updated policy version from the Enterprise control plane to an enrolled local/endpoint agent.
- Do: Inspect what the endpoint receives and how it verifies it.
- Expected: The endpoint receives a signed policy bundle, verifies the signature before applying it, and records the applied policy version -- an unsigned or tampered policy is never silently applied.
- User value: Makes local policy enforcement trustworthy for security/compliance buyers, not just convenient.
- Why it matters: Named in strategy.md's architecture diagram (section 16, 'Signed endpoint policy distribution') and section 18.2 scope, but has no dedicated scenario -- only mentioned indirectly via the OSS propagation matrix.

## Prove

<a id="e-19"></a>

### E-19 - Session audit chain verification

- Status: In progress
- Platform: Evidence
- Go to: Open session evidence export.
- Do: Verify chain and inspect policy decisions.
- Expected: Chain status, events, risks, approvals, cost, and policy evidence are exported.
- User value: Security/compliance can trust the record.
- Why it matters: Tamper-evident evidence differentiates from normal dashboards.

<a id="e-20"></a>

### E-20 - Usage rule evidence receipt

- Status: Gap
- Platform: Evidence
- Go to: Open a fired Usage Rule.
- Do: Inspect matched telemetry, customer plan context, decision, action, and impact.
- Expected: Receipt proves what would have happened, what happened instead, and why.
- User value: Makes preventive controls credible to finance and customer teams.
- Why it matters: Protected spend needs evidence, not vibes.

<a id="e-21"></a>

### E-21 - Cost per customer outcome

- Status: In progress
- Platform: Reports
- Go to: Open Reports.
- Do: Filter by customer and product feature.
- Expected: AIWatcher shows AI cost per successful business outcome or accepted output where metadata exists. Shipped: src/app/api/v1/insights/product/route.ts and src/app/api/v1/dashboard/analytics/route.ts compute cost_per_useful_outcome segmented by customer and feature, surfaced on /insights/product and the dashboard.
- User value: Connects AI spend to revenue and margin.
- Why it matters: Outcome-aware cost is the enterprise version of OSS cost per useful change. Core computation is live; still needs broader coverage across more outcome types and report surfaces.

<a id="e-22"></a>

### E-22 - Protected spend report

- Status: Gap
- Platform: Reports
- Go to: Open Reports -> Controls impact.
- Do: Review policy decisions over a period.
- Expected: Report shows spend protected by routing, throttling, blocking, caching, and approvals.
- User value: Turns controls into ROI.
- Why it matters: This is the CFO/VP Eng proof loop.

<a id="e-23"></a>

### E-23 - Local surviving change signal rolls up to enterprise

- Status: Gap
- Platform: Work Ledger
- Go to: Review local coding work for a team.
- Do: Inspect useful/rework/abandoned outcomes and surviving change evidence.
- Expected: Enterprise shows team-level outcome economics without exposing prompt/source content by default.
- User value: Connects developer AI work to useful engineering output.
- Why it matters: This adapts OSS outcome moat into team value.

<a id="e-30"></a>

### E-30 - Development-to-production lineage links a local session to production behavior

- Status: Gap
- Platform: Evidence
- Go to: Merge a PR that originated from an AIWatcher Local session, deploy it, and let it run in production under the SDK.
- Do: Open Work Ledger or Evidence and look up the resulting production incident or feature.
- Expected: AIWatcher shows the chain: local session -> changed artifact -> commit/PR -> build/deployment -> service/feature -> production work units -> intervention -> outcome, per strategy.md's Use Case 4 and Phase 5 chain.
- User value: Lets a team trace a production cost, incident, or outcome back to the AI-assisted change and workflow that caused it -- the moat's evidence substrate.
- Why it matters: Strategy.md Use Case 4 and Phase 5 name this as a required capability, but no scenario or code (no GitHub/CI/deployment integration found in agentwatch) currently exists for it.

<a id="e-31"></a>

### E-31 - Proposed action, decision, enforcement, execution, and outcome are stored as separate records

- Status: Gap
- Platform: Evidence
- Go to: Trigger a full SDK evaluateControl -> enforce -> execute -> outcome cycle for one proposed action.
- Do: Inspect the stored evidence for that action.
- Expected: ProposedAction, PolicyEvaluation, Decision, EnforcementResult, Execution, ExecutionResult, and Outcome exist as distinct, linked records -- not collapsed into one generic event row -- per strategy.md section 17's required lifecycle separation.
- User value: Prevents a single ambiguous event row from being read as proof of something that didn't actually happen (see E-29); makes each stage independently auditable.
- Why it matters: Strategy.md section 17 explicitly requires this separation. Current schema, including the unmerged PR #13 foundation, still stores decision/enforcement/result in a single policyDecisions-style row.

<a id="e-33"></a>

### E-33 - Named operating metrics roll up across all controlled work

- Status: Gap
- Platform: Reports
- Go to: Accumulate a mix of policy evaluations, enforcements, overrides, and outcomes across at least one billing period.
- Do: Open Reports / Outcomes.
- Expected: Enforcement acknowledgement rate, policy latency, override rate, and spend-under-active-control are computed and shown as trend metrics -- not left implicit inside individual intervention receipts.
- User value: These are the exact metrics strategy.md section 24 names as what Enterprise should report; without rollups, buyers only see anecdotes, not a trend they can act on.
- Why it matters: Strategy.md section 24 explicitly lists these as Enterprise metrics; nothing currently aggregates them.

## Improve

<a id="e-24"></a>

### E-24 - OSS scenario propagation matrix is maintained

- Status: Gap
- Platform: Private docs + Enterprise planning
- Go to: Open enterprise propagation matrix.
- Do: Review each OSS scenario decision: propagate, adapt, OSS-only, enterprise-only.
- Expected: Every OSS feature has an enterprise disposition and target scenario.
- User value: Keeps product lines aligned.
- Why it matters: Prevents drift between OSS and Enterprise.

<a id="e-25"></a>

### E-25 - Policy recommendation learns from outcomes

- Status: Gap
- Platform: Controls
- Go to: Open control recommendation.
- Do: Review why a rule/model route/approval threshold is suggested.
- Expected: AIWatcher cites workload pattern, past outcomes, policy history, and measured impact.
- User value: Builds the intervention graph moat.
- Why it matters: The hard-to-copy asset is which controls work for which agentic workload patterns.

<a id="e-26"></a>

### E-26 - Weekly executive improvement summary

- Status: Gap
- Platform: Reports
- Go to: Open weekly report.
- Do: Review top controls applied, spend protected, risks reduced, outcomes improved, and remaining gaps.
- Expected: Report is board/leadership-ready and links to evidence.
- User value: Creates enterprise habit and renewal evidence.
- Why it matters: Enterprise needs recurring proof that AIWatcher changed behavior.

## Failsafe

<a id="e-27"></a>

### E-27 - SSO/RBAC separates developer and admin control

- Status: Gap
- Platform: Admin
- Go to: Open Settings -> Access.
- Do: Configure roles for viewer, approver, policy admin, and org admin.
- Expected: Users can see appropriate data and actions without silent expansion of local collection.
- User value: Enterprise trust and procurement requirement.
- Why it matters: Control without RBAC is not enterprise-ready.

<a id="e-28"></a>

### E-28 - SIEM/FinOps/billing export path

- Status: Gap
- Platform: Integrations
- Go to: Open Settings -> Integrations.
- Do: Configure evidence, spend, and policy-impact exports.
- Expected: AIWatcher exports normalized records without prompt/source content by default.
- User value: Fits existing enterprise workflows.
- Why it matters: Enterprises need AIWatcher to feed systems they already trust.

# AIWatcher

## Final Product Vision and Execution Strategy

**Status:** Product source of truth

**Date:** July 25th 2026

**Scope:** AIWatcher Local, Enterprise endpoint controls, production SDK, control plane, and evidence system

---

# 1. Executive decisions

## Category

**AI Work Control and Evidence**

## Tagline

> **Control what AI does. Prove what it delivered.**
>

## One-sentence value proposition

> **AIWatcher helps engineering and AI product teams control costly or risky AI work before execution, then prove whether the intervention preserved a successful outcome.**
> 

## Product thesis

AIWatcher connects:

```
Intent
→ Proposed AI work
→ Policy or intervention
→ Actual enforcement
→ Execution
→ Cost and risk
→ Artifact or business outcome
→ Durability and rework
```

Its purpose is not merely to record AI activity. Its purpose is to help a person or organization make a better decision before or during AI execution and produce credible evidence afterward.

## Initial paid wedge hypothesis

> **Outcome-aware Usage Rules for customer-facing AI products.**
> 

AIWatcher should initially help AI-native software companies:

- Enforce customer AI allowances
- Enforce premium-model entitlements
- Prevent free-trial abuse
- Control feature-level AI cost and margin
- Route work to lower-cost models
- Verify that routing or limits did not materially damage the outcome
- Resolve customer, plan, team, or feature billing conflicts with evidence about what AI usage was allowed, routed, throttled, blocked, or actually executed

This is adjacent to billing, not a replacement for billing. AIWatcher should explain and control AI usage before it becomes a billing or margin problem; Stripe, Chargebee, contracts, invoicing, payment collection, and general revenue ledgers remain integrations.

Plain-English first sale:

> **For AI-native SaaS companies with tiered plans, AIWatcher prevents premium-model and allowance leakage before execution, then gives product, support, and finance a receipt proving what was allowed, routed, executed, allocated, and accepted.**

## OSS role

> **AIWatcher Local is the trusted, private control loop for individual developers.**
> 

It creates direct user value, developer trust, adapter coverage, and development-side evidence. It must remain useful without Enterprise signup.

## Enterprise role

> **AIWatcher Enterprise coordinates policy, customer economics, approvals, evidence, and outcome learning across development and production AI work.**
> 

Enterprise scope is broader than customer-facing AI economics: it can eventually cover internal AI workflows across teams, projects, operations, support, sales, finance, and product development. The first paid wedge remains customer-facing AI economics because it has the clearest budget owner, allowance context, outcome signal, and urgency. Internal workflow optimization becomes an expansion path after the control/evidence loop is proven.

## Critical strategic distinction

Customers do not primarily buy “lineage.”

They buy outcomes such as:

- Protected product margin
- Reduced AI cost
- Fewer unsafe actions
- Less engineering rework
- Better model-routing decisions
- Defensible evidence
- Faster resolution of AI billing or credit disputes
- Clearer return on AI investment

Development-to-production lineage is the evidence substrate that makes those outcomes explainable and optimizable.

---

# 2. What is proven and what remains a hypothesis

## Proven or substantially supported

- Developers experience real waste from broad prompts, stale sessions, context growth, repeated work, and difficult cross-agent handoffs.
- AI product teams need cost attribution, runtime limits, routing, reliability, and guardrails.
- Agent governance and runtime control are becoming expected platform capabilities.
- AI activity metrics alone do not establish useful engineering or business outcomes.
- AIWatcher Local already demonstrates meaningful portions of a private plan–watch–control–prove–improve loop.

The OSS implementation includes normalized local sessions and events, prompt preflight, prompt gating, local receipts, cross-process-safe state, session-health analysis, handoff support, and code-outcome evidence.

## Not yet proven

- That companies will pay specifically for outcome-aware Usage Rules
- That customer outcome data will be available and reliable
- That AIWatcher can integrate into model-call paths without unacceptable friction
- That development-to-production lineage is sufficiently valuable to affect a purchase
- That AIWatcher can capture evidence competitors cannot obtain
- That accumulated history materially improves future controls
- That the resulting learning compounds faster than competitors can reproduce it
- That OSS adoption will generate Enterprise pipeline
- That switching costs will become meaningful

These are product and business hypotheses, not established facts.

---

# 3. First-principles problem definition

AI adoption creates three structural problems.

## 3.1 AI work is fragmented

AI work occurs across:

- Claude Code
- Codex
- Cursor
- IDEs and terminals
- MCP servers
- Product applications
- RAG workflows
- Internal agents
- Customer-facing agents
- Multi-agent systems
- Models and gateways from multiple vendors

Each surface stores different information and exposes different enforcement capabilities.

As a result, individuals and organizations cannot consistently answer:

- What AI work happened?
- What was the intent?
- Who or what initiated it?
- Which model and tools were used?
- What did the work cost?
- Which control applied?
- What happened afterward?
- Was the result useful?

---

## 3.2 Most systems observe after execution

Traditional observability explains what has already happened.

It does not necessarily prevent:

- A customer exceeding an AI allowance
- An unauthorized premium-model call
- A destructive agent tool action
- A broad and expensive coding task
- A long-running agent loop
- A stale coding session repeatedly resending context
- An action that should require approval
- A workflow that destroys product margin

AIWatcher must therefore operate at the decision point—not merely at the telemetry point.

---

## 3.3 AI activity is disconnected from value

Most systems measure:

- Calls
- Tokens
- Traces
- Latency
- Errors
- Security findings
- Prompt or response quality

Organizations ultimately need answers such as:

- Did the customer’s task complete successfully?
- Was the answer accepted?
- Did the code pass tests?
- Was the pull request merged?
- Did the change survive?
- Did a cheaper model preserve the result?
- Did an approval prevent meaningful risk?
- Did the agent reduce or create human rework?
- What is the cost per useful outcome?

AIWatcher should optimize for:

> **Cost and risk per successful outcome—not AI activity volume.**
> 

---

# 4. Vision and mission

## Vision

> **Every consequential unit of AI work should be observable, controllable, attributable, and connected to an outcome.**
> 

## Mission

> **Help people and organizations use AI more effectively by intervening at the right moment and proving what happened afterward.**
> 

## Product lifecycle

```
Plan → Watch → Control → Prove → Improve
```

### Plan

Understand intent and identify likely scope, cost, policy, or safety concerns before execution.

### Watch

Detect context degradation, loops, cost velocity, policy drift, quota pressure, and failed progress while work is underway.

### Control

Advise, rescope, route, throttle, require approval, pause, or block.

### Prove

Record the decision, enforcement result, execution, cost, evidence, and outcome.

### Improve

Use historical evidence to improve routing, policies, prompts, thresholds, and agent workflows.

---

# 5. Target customers

## Initial ideal customer profile

AIWatcher should initially target:

> **AI-native SaaS companies operating customer-facing AI features with tiered plans, material model spend, and measurable workflow outcomes.**
> 

Characteristics:

- AI is part of the product, not only an internal experiment.
- The company has multiple customer plans or usage entitlements.
- Model cost affects product margin.
- The product uses more than one model or could route between models.
- At least one workflow has a measurable outcome.
- Product or platform engineering can integrate a pre-call SDK or API.
- A named owner is responsible for AI cost, platform reliability, or feature economics.

## Initial buyers

Primary:

- Head of AI Platform
- AI Product Engineering leader
- VP Engineering
- Platform Engineering leader

Economic or operational stakeholder:

- FinOps
- Product leadership
- Finance responsible for AI feature margins

Expansion buyers:

- Security
- Governance
- Compliance
- Developer productivity

Security and compliance should not be the initial sales center of gravity.

---

# 6. Customer use cases

## Use case 1: Customer entitlement and product-margin control

### Problem

An AI product offers different service tiers, but model usage is not consistently enforced by customer plan, feature, or workflow.

### Customer questions

- Is this customer allowed to use the premium model?
- Has this customer exhausted the monthly AI allowance?
- Which user, team, feature, or workflow consumed the allowance?
- Is this customer billing or credit dispute backed by execution evidence?
- Is this free-trial workflow being abused?
- Is this feature still economically viable?
- Can we route this request to a cheaper model?
- Will routing reduce the success rate?

### AIWatcher action

- Evaluate customer, plan, feature, workflow, and estimated cost before execution.
- Allow, route, throttle, require approval, or block.
- Record actual execution and cost.
- Attach the workflow outcome.
- Generate an intervention receipt.
- Generate billing/allocation evidence showing allowance, entitlement, decision, execution, and outcome.

### Customer value

- Protect product margin
- Enforce packaging
- Reduce unpredictable overages
- Resolve AI billing and credit conflicts without rebuilding the billing platform
- Make routing decisions based on outcomes rather than price alone

---

## Use case 2: Runaway AI workflow control

### Problem

An agent repeats tool calls, retries unsuccessfully, or accumulates cost without meaningful progress.

### Customer questions

- Is this workflow making progress?
- Is it repeating the same failure?
- Should it pause, rescope, or terminate?
- What cost was avoided?
- Did stopping it prevent a valid outcome?

### AIWatcher action

- Detect unusual cost, call, retry, or loop velocity.
- Alert, pause, throttle, rescope, or stop.
- Preserve a handoff or recovery state.
- Record the outcome and protected-value estimate.

### Customer value

- Avoid runaway cost
- Reduce operational incidents
- Preserve debuggability
- Prevent silent workflow exhaustion

---

## Use case 3: Private developer AI control

### Problem

Developers use multiple coding agents but lack a private, cross-tool way to prevent poor runs and measure useful outcomes.

### Developer questions

- Is this request too broad or destructive?
- Should I continue this session or restart?
- Am I entering an expensive loop?
- Which prompt caused most of the work?
- How do I move from Claude to Codex without rebuilding context?
- Did this session produce a useful change?
- Did that change survive or require rework?
- What did AIWatcher read or retain?
- Did the hook actually protect this surface?

### AIWatcher action

- Preflight risky work
- Add an execution brief or open a decision gate
- Detect unhealthy sessions and loops
- Generate a handoff capsule
- Infer outcomes from commits, tests, changes, and later rework
- Keep prompts and source local by default

### Developer value

- Better-scoped work
- Less context waste
- Safer execution
- Easier agent switching
- Evidence of which AI work was useful
- Privacy without a cloud account

---

## Use case 4: AI-assisted development to production outcomes

### Problem

Organizations cannot connect AI-assisted development activity to deployed behavior, production cost, incidents, or business results.

### Customer questions

- Which AI-assisted change introduced this production behavior?
- Which repository or feature drives the highest AI cost?
- Did an AI-generated change create later rework?
- Which model or coding workflow produces durable code?
- Which deployed AI capabilities are economically inefficient?
- Did a production policy fix the problem?

### AIWatcher action

Connect:

```
Local agent session
→ changed artifact
→ commit and pull request
→ build and deployment
→ service and feature
→ production work units
→ intervention
→ outcome
```

### Customer value

- Better incident investigation
- Engineering AI ROI
- Feature-level economics
- Safer adoption
- Evidence for improving both development and production workflows

This is an expansion use case, not the first paid wedge.

---

## Use case 5: Runtime approval and evidence

### Problem

Some agent actions require human approval, but organizations lack reliable evidence of what was approved, what executed, and whether the approval helped.

### Customer questions

- Why was approval required?
- Who approved it?
- What exact action was authorized?
- Did the action change after approval?
- Did it execute?
- What result followed?
- Was the approval rule useful or merely friction?

### AIWatcher action

- Bind approval to an exact action and policy evaluation.
- Record approver identity, reason, scope, and expiry.
- Require enforcement acknowledgement.
- Link approval to execution and outcome.
- Measure approval effectiveness.

### Customer value

- Safer high-impact actions
- Stronger accountability
- Lower approval fatigue
- Evidence for retiring unnecessary rules

---

# 7. User experience by product

## AIWatcher Local

### Core experience

> **A private personal control loop that helps developers prevent bad AI runs and learn which agent work produces durable results.**
> 

Primary experiences:

1. **Today**
    - What AI work happened?
    - Which projects and tools drove usage?
    - What needs attention?
2. **Preflight**
    - Is this work broad, destructive, risky, or likely to become expensive?
    - What narrower execution brief preserves the intent?
3. **Watch**
    - Is context health degrading?
    - Is the session stale, repetitive, or losing efficiency?
4. **Control**
    - Run original
    - Add safer brief
    - Edit guidance
    - Cancel
    - Stop or hand off where supported
5. **Prove**
    - What decision was made?
    - What session resulted?
    - Did commits, tests, or changes appear?
    - Did the change survive?
6. **Improve**
    - What should I do differently next time?
    - Which agent or model fits this type of work?
    - Should I resume in a fresh session?

---

## AIWatcher Enterprise

### Core experience

> **A control and evidence system for AI product economics and organizational AI work.**
> 

Recommended navigation:

1. **Inbox**
    - Approvals
    - Runaway workflows
    - Policy violations
    - Billing and allocation conflicts
    - Integration failures
    - High-value findings
2. **Controls**
    - Usage Rules
    - Allowance and entitlement policies
    - Policy versions
    - Simulations
    - Routing
    - Approvals
    - Rollouts
3. **Work**
    - Work units
    - Customers
    - Features
    - Applications
    - Projects
    - Agents
    - Models
    - Tools
    - Evidence
4. **Outcomes**
    - Cost per outcome
    - Protected value
    - Billing allocation evidence
    - Rework
    - Success rates
    - Feature margins
    - Intervention effectiveness
5. **Settings**
    - Identities
    - Roles
    - Applications
    - Endpoints
    - SDKs
    - Data collection
    - Retention
    - Integrations

---

## OSS Free versus Enterprise Paid

| Dimension | AIWatcher Local - free OSS | AIWatcher Enterprise - paid |
| --- | --- | --- |
| Primary user | Individual AI-heavy developer | Product, platform, engineering, finance, support, and governance teams |
| Core job | Make local AI work safer, smaller, more resumable, and more measurable | Control AI work across customer-facing and internal workflows with policy, evidence, and outcomes |
| First value | Private Evidence Inbox, prompt/command gates, session health, handoff, local receipts | One controlled workflow with customer/plan/feature/allowance context, enforcement acknowledgement, outcome, and receipt |
| Evidence | Local metadata, hashes, decisions, cost, surface coverage, code survival, manual outcome correction | Organization-retained receipts, customer/workflow context, policy versions, enforcement, outcomes, protected value, exports |
| Controls | Personal prompt gates, command gates, preflight, handoff, local watch signals | Usage Rules, routing, throttling, blocking, approvals, signed policy distribution, retention, RBAC |
| Privacy stance | Prompt/source local by default; useful without account signup | Metadata/evidence by default; content collection explicit; developer-visible collection disclosure |
| Not included | SSO, central admin policy, customer entitlements, org retention, compliance exports | Billing system of record, hidden employee surveillance, generic gateway replacement, broad GRC as the first wedge |

This split matters: OSS must remain a complete developer product, not a crippled lead magnet. Enterprise must charge for organization-level control, retention, policy, customer economics, and evidence workflows.

---

# 8. Product principles

## 8.1 Control before dashboard

Every important Enterprise feature should answer:

> What decision or action can the user or system take?
> 

Charts support the product. They are not the product.

---

## 8.2 Evidence after every intervention

Every intervention should produce a receipt containing:

- Work-unit context
- Proposed action
- Relevant customer, feature, or development context
- Policy and immutable version
- Facts that matched
- Decision
- Enforcement attempt
- Enforcement acknowledgement
- Actual execution
- Observed cost
- Outcome
- Impact classification
- Confidence and comparison basis

Receipt types:

| Receipt | Purpose |
| --- | --- |
| Intervention Receipt | Shows the proposed action, matched facts, policy or local rule, decision, actor, and comparison basis. |
| Enforcement Receipt | Proves the decision was actually applied by a hook, SDK, policy enforcement point, gateway, or local control. |
| Outcome Receipt | Links the controlled work to a customer, product, operational, or developer outcome with confidence and evidence labels. |
| Billing Evidence Receipt | Explains customer, plan, allowance, billing period, feature, workflow, execution, allocation, and outcome for AI-usage disputes. |

These receipts may render together in one product view, but the facts must remain separate. A policy decision is not enforcement. A prevented premium call creates an inferred counterfactual, not observed savings. A customer-accepted result is outcome evidence, not proof that all future routing is safe.

---

## 8.3 Prove invocation; never infer enforcement

AIWatcher must distinguish:

```
Policy evaluated
Enforcement requested
Enforcement acknowledged
Action executed
Action prevented
```

A server returning `block` does not prove that the action was blocked.

A session log does not prove that a local hook executed.

Product claims must be based on verified invocation and enforcement evidence.

---

## 8.4 Outcome over token volume

Tokens and calls are input metrics.

The product should optimize for:

- Cost per successful workflow
- Cost per accepted response
- Cost per surviving code change
- Cost per merged pull request
- Customer margin
- Rework
- Successful lower-cost routing
- Protected value

---

## 8.5 Measured beats speculative

Impact must be labeled precisely.

| Label | Meaning |
| --- | --- |
| Predicted | Forecast before execution |
| Inferred | Derived from an unobserved counterfactual or indirect evidence |
| Observed | Directly recorded result |
| Measured | Compared through a credible experimental or historical method |
| Verified | Supported by independent or durable evidence |

### Correct example

```
Estimated premium-model cost: $11.00
Observed routed-model cost: $3.20
Inferred avoided cost: $7.80
Observed outcome: Customer accepted the result
Avoided-cost confidence: Medium
```

The $7.80 is not an observed reduction because the premium-model call did not execute.

---

## 8.6 Developer trust is non-negotiable

- Prompts and source stay local by default.
- Collection behavior is visible.
- Content collection is explicit.
- Management views emphasize projects, services, features, and teams.
- Individual ranking is not the default product experience.
- Endpoint controls are reversible.
- Platform limitations are disclosed.
- Enterprise value must not depend on weakening OSS trust.

---

## 8.7 Infer first; ask only to confirm

Outcome capture must not become administrative work.

AIWatcher should:

1. Infer likely outcomes from available evidence.
2. Show confidence and reasons.
3. Ask for one-click confirmation or correction where needed.
4. Learn from corrections.

---

## 8.8 One product system

OSS and Enterprise must share:

- Lifecycle terminology
- Canonical entities
- Evidence vocabulary
- Policy decisions
- Outcome semantics
- Privacy rules
- Adapter capabilities
- Integration-health language

Enterprise must not maintain an independent copy of the OSS collector logic.

---

## 8.9 Billing evidence, not billing software

AIWatcher can help companies answer customer billing and credit conflicts when those conflicts are caused by AI usage.

It should provide:

- Pre-execution entitlement and allowance decisions
- Enforcement acknowledgement
- Actual execution and cost records
- Allocation by customer, plan, feature, workflow, team, and billing period
- Outcome evidence showing whether the lower-cost or limited path still worked
- A receipt support, finance, product, or platform teams can cite

It should not become the source of truth for invoices, payment collection, revenue recognition, taxes, credits, refunds, or contract management. Those remain billing-platform responsibilities.

---

# 9. Product boundaries

## AIWatcher should build

- Private developer control loop
- Canonical WorkUnit model
- Outcome-aware Usage Rules
- Pre-execution control API
- Intervention receipts
- Outcome evidence
- Development-to-production lineage
- Protected-value reporting
- Billing and allocation evidence for AI usage controls
- Customer-specific control recommendations
- Shared local and production evidence model

## AIWatcher should integrate with rather than rebuild

- AI gateways
- General trace storage
- Model hosting
- Full agent runtimes
- Sandboxes
- DLP engines
- SIEM
- GRC systems
- Billing platforms
- CI/CD systems
- Product analytics
- General cloud FinOps

## Explicit non-goals

- Broadest AI security platform
- Full regulatory GRC suite
- Universal agent sandbox
- General-purpose AI gateway replacement
- Agent-hosting platform
- Generic employee-productivity ranking
- Universal browser or desktop interception
- Invoice, payment, tax, refund, or contract-management system of record
- Uploading developer content by default
- Supporting every SDK language before semantic parity exists
- Claiming protected value without an evidence basis

---

# 10. Competitive landscape

The market is active and increasingly capable. AIWatcher must assume that generic controls, observability, governance, and coding provenance will continue to commoditize.

## 10.1 AI gateways and cost controls

Portkey already documents conditional routing, fallbacks, caching, guardrails, budget limits, workspace-level usage policies, and rate limits. Its synchronous guardrails can deny, retry, or redirect requests.

### Implication

AIWatcher cannot differentiate through:

- Generic budgets
- Basic rate limits
- Model fallbacks
- Guardrails alone
- Generic conditional routing

### AIWatcher response

Add business context and outcomes:

```
Customer
+ plan
+ entitlement
+ allowance
+ billing period
+ feature
+ workflow
+ control
+ observed outcome
```

AIWatcher should be able to use an existing gateway as an enforcement point.

---

## 10.2 Observability, evaluation, and agent operations

LangSmith publicly spans agent observability, online and offline evaluation, human feedback, deployment, and production operations across multiple languages.

### Implication

AIWatcher should not compete on:

- Generic traces
- Prompt experiments
- Standard evaluations
- Agent deployment
- General production monitoring

### AIWatcher response

Consume trace and evaluation evidence where available, but specialize in:

- Pre-execution business controls
- Intervention receipts
- Work-unit outcomes
- Development-to-production evidence
- Policy effectiveness

---

## 10.3 Runtime governance and security

WitnessAI publicly describes discovery and control across IDEs, applications, custom agents, MCP servers, tools, and human identities. It claims organization-wide allow/block policies at the tool boundary and coverage for coding tools such as Claude Code and Codex.

Microsoft’s open-source Agent Governance Toolkit describes deterministic pre-execution policy enforcement, identity, approvals, kill switches, compliance evidence, framework integrations, and SDK support across several languages.

### Implication

AIWatcher cannot claim that:

- Runtime policy is unique
- Coding-agent governance is unique
- MCP controls are unique
- Approval workflows are unique
- Local plus production coverage is automatically unique
- Audit evidence alone creates a moat

### AIWatcher response

Implement the minimum trustworthy control depth required for the value proposition:

```
allow
advise
route
throttle
require approval
block
```

Then differentiate through:

- Customer and workflow context
- Enforcement-to-outcome linkage
- Development-to-production evidence
- Cost per successful outcome
- Intervention learning

---

## 10.4 Coding-agent provenance and governance

Origin publicly positions itself as an AI coding-history layer with session capture, prompt-to-line attribution, model and cost tracking, team governance, budgets, and audit trails across several coding agents.

### Implication

AIWatcher cannot claim:

- AI code attribution is unique
- Cross-agent coding-session capture is unique
- Team coding-agent budgets are unique
- Git-based AI provenance is an empty category

### AIWatcher response

Do not stop at coding provenance.

Connect it to:

```
AI-assisted work
→ artifact
→ deployment
→ production behavior
→ customer economics
→ intervention
→ durable outcome
```

---

# 11. Strategic differentiation

AIWatcher’s differentiated position is not one isolated feature.

It is the combination of:

1. Private developer-side control
2. Production pre-execution control
3. Business-context Usage Rules
4. Artifact and deployment lineage
5. Outcome evidence
6. Intervention-effectiveness learning

## Competitive positioning statement

> **Unlike products centered primarily on traces, generic gateway controls, security events, compliance workflows, or coding provenance, AIWatcher connects AI work to the intervention applied and the outcome that followed.**
> 

This is a strategic direction, not yet a proven exclusive capability.

---

# 12. Wedge, advantage, flywheel, and moat

These terms must not be conflated.

## 12.1 Wedge

The narrow problem that wins the first paid customer:

> **Protect customer-facing AI product margins with outcome-aware Usage Rules.**
> 

## 12.2 Initial advantage

Why AIWatcher may solve the wedge better:

- Customer and feature context
- Pre-execution policy
- Enforcement evidence
- Outcome attachment
- Honest protected-value receipts

## 12.3 Flywheel hypothesis

Each controlled work unit adds evidence about:

- Task type
- Customer and plan
- Model
- Policy
- Intervention
- Cost
- Result
- Outcome
- Rework

That evidence may improve:

- Model routing
- Policy thresholds
- Cost forecasting
- Outcome prediction
- False-positive reduction
- Approval decisions

## 12.4 Moat hypothesis

> **AIWatcher may become defensible if its local, delivery, and production integrations create uniquely complete causal evidence, and that evidence improves customer-specific controls enough to create workflow dependence and switching costs.**
> 

## 12.5 Current status

| Stage | Status |
| --- | --- |
| Wedge | Plausible but unvalidated |
| OSS product advantage | Emerging |
| Enterprise advantage | Hypothesis |
| Data flywheel | Designed, not proven |
| Switching cost | Not established |
| Durable moat | Not established |

---

# 13. Why this might become defensible

## 13.1 Difficult evidence acquisition

AIWatcher must capture more than events.

The high-value record is:

```
Proposed action
→ Policy decision
→ Enforced alternative
→ Actual execution
→ Outcome
```

Passive telemetry is not equivalent to causal intervention evidence.

## 13.2 Cross-surface workflow position

AIWatcher can potentially operate across:

- Local developer work
- CI/CD
- Runtime model decisions
- Outcome evaluation
- Policy improvement

Deeper workflow embedding makes replacement harder.

## 13.3 Customer-specific learning

A broad cross-customer model may be limited by privacy and data-isolation requirements.

The stronger initial defensibility may come from customer-specific history:

- Which models work for their workflows
- Which policies create false positives
- Which customers drive margin pressure
- Which controls preserve their outcomes
- Which approvals protect meaningful value

## 13.4 Switching cost

A customer removing AIWatcher may lose:

- Policy-effectiveness history
- Outcome baselines
- Customer and feature economics
- Intervention receipts
- Artifact lineage
- Routing recommendations
- Integration mappings
- Audit evidence

## 13.5 OSS distribution and trust

OSS may provide:

- Developer adoption
- Adapter contributions
- Lower distribution cost
- Access to local evidence
- Credibility with engineering users
- A trusted endpoint architecture

This is an advantage only if OSS remains genuinely developer-first.

---

# 14. Why competitors may still replicate it

AIWatcher should assume that well-funded competitors can technically implement:

- Outcome fields
- Customer context
- Git integrations
- Routing recommendations
- Policy receipts
- Additional dashboards

Capital, installed customers, and existing control points are material advantages.

The strategy must therefore not rely on:

> “Competitors cannot build this.”
> 

It must rely on:

> **AIWatcher can focus earlier, acquire higher-quality evidence, integrate more deeply into this specific workflow, and create enough customer-specific learning and trust to remain valuable when competitors respond.**
> 

If AIWatcher cannot do that, the proposed moat will not materialize.

---

# 15. Company versus feature test

Development-to-production lineage alone may be:

- A feature in a coding-provenance product
- A module in an AI governance suite
- An observability integration
- A developer-platform capability

AIWatcher becomes a standalone company only if customers pay for the business decision it improves.

## Company-level value proposition

> **Control AI product economics and operational risk while preserving successful outcomes.**
> 

## Supporting capability

> Development-to-production lineage explains where the behavior came from and helps improve it.
> 

## Validation rule

If customers value lineage but will not pay to:

- Evaluate before execution
- Enforce a decision
- Attach an outcome
- Review protected value

then lineage is probably an integration feature rather than a sufficient company wedge.

---

# 16. Canonical product architecture

```
flowchart TB
    subgraph Sources["AI Work Sources"]
        Local["Claude, Codex, Cursor and local tools"]
        Product["Production AI applications"]
        Agents["Agent and multi-agent workflows"]
        MCP["MCP servers and external tools"]
    end

    subgraph SharedCore["AIWatcher Shared Core"]
        Adapters["Surface adapters"]
        WorkModel["Canonical WorkUnit model"]
        EvidenceModel["Evidence and outcome schemas"]
        Privacy["Privacy transforms"]
        Capability["Capability and coverage registry"]
    end

    subgraph Edge["Endpoint and Runtime Layer"]
        LocalPDP["Local policy decision point"]
        SDK["Python and TypeScript SDK"]
        Context["Identity and business-context resolver"]
        PEP["Policy enforcement point"]
        Buffer["Durable local buffer"]
    end

    subgraph Control["Enterprise Control Plane"]
        Registry["Identity, application and work registry"]
        Policies["Immutable policy registry"]
        Usage["Usage and entitlement engine"]
        Evaluate["Control evaluation service"]
        Approval["Approval and escalation"]
        Routing["Model and tool routing"]
        Distribution["Signed endpoint policy distribution"]
    end

    subgraph Evidence["Evidence and Outcome Plane"]
        Ledger["Append-only work ledger"]
        Lineage["Artifact and deployment lineage"]
        Graph["Intervention–Outcome Graph"]
        Outcomes["Outcome evaluation"]
        Impact["Intervention effectiveness"]
        Export["Signed evidence export"]
    end

    subgraph Experience["Product Experiences"]
        Developer["Developer experience"]
        Inbox["Inbox"]
        Controls["Controls"]
        Work["Work ledger"]
        Reports["Outcome economics"]
        Leadership["Leadership rollups"]
        Integrations["SIEM, GRC and FinOps"]
    end

    Local --> Adapters
    Product --> SDK
    Agents --> SDK
    MCP --> SDK

    Adapters --> WorkModel
    SDK --> WorkModel
    WorkModel --> Context
    EvidenceModel --> Context

    Context --> LocalPDP
    Context --> Evaluate
    Distribution --> LocalPDP
    Policies --> Evaluate
    Usage --> Evaluate

    LocalPDP --> PEP
    Evaluate --> PEP
    Evaluate --> Approval
    Evaluate --> Routing

    PEP --> Sources
    PEP --> Privacy
    Privacy --> Buffer
    Buffer --> Ledger

    Evaluate --> Ledger
    Approval --> Ledger
    Ledger --> Lineage
    Lineage --> Graph
    Graph --> Outcomes
    Outcomes --> Impact
    Ledger --> Export

    Adapters --> Developer
    Graph --> Inbox
    Policies --> Controls
    Ledger --> Work
    Impact --> Reports
    Reports --> Leadership
    Export --> Integrations
```

---

# 17. Canonical data model

## Core abstraction: WorkUnit

A `WorkUnit` represents the human or business task being completed.

Examples:

- Implement authentication support
- Resolve a customer case
- Summarize a contract
- Process a refund
- Reconcile an invoice
- Research a topic
- Execute an infrastructure change

A WorkUnit may span multiple:

- Sessions
- Agents
- Models
- Tools
- Developers
- Deployments
- Outcomes

## Essential entities

```
Organization
Principal
Identity
Application
Project
Repository
Customer
Plan
Entitlement
UsageAllowance
Feature
Agent
AgentVersion
Model
Tool
WorkUnit
Session
Intent
ProposedAction
Policy
PolicyVersion
PolicyEvaluation
Decision
Intervention
Approval
EnforcementResult
Execution
Artifact
Build
Deployment
Outcome
Evidence
CostAllocation
BillingPeriod
BillingEvidenceReceipt
InterventionImpact
```

## Required lifecycle separation

```
ProposedAction
→ PolicyEvaluation
→ Decision
→ EnforcementResult
→ Execution
→ ExecutionResult
→ Outcome
```

These must not be collapsed into a generic event.

---

# 18. Product scope by layer

## 18.1 AIWatcher Local — OSS

### Purpose

Complete individual developer value.

### Scope

- Tool discovery
- Local activity normalization
- Prompt preflight
- Prompt and command gates
- Session-health warnings
- Loop and cost-velocity detection
- Cross-agent handoff
- Outcome evidence
- Cost per surviving change
- Privacy-safe receipts
- Export and portability
- Surface coverage diagnostics

### Enterprise features excluded

- Central organization enforcement
- SSO and RBAC
- Customer entitlements
- Organization retention
- Central approval routing
- Compliance exports
- Leadership reporting

---

## 18.2 Enterprise endpoint

### Purpose

Extend trusted local controls across managed teams.

### Scope

- Endpoint enrollment and identity
- Shared-core adapters
- Signed policy distribution
- Local evaluation
- Privacy transformation
- Evidence upload
- Integration-health verification
- Repository and team ownership
- Developer-visible collection disclosure
- Auditable temporary overrides

---

## 18.3 Production SDK

### Purpose

Control customer-facing and internal production AI applications.

### Initial languages

- Python
- TypeScript/JavaScript

Additional languages follow only after parity.

### SDK sequence

```
Declare context
→ Propose action
→ Evaluate
→ Enforce
→ Acknowledge
→ Execute
→ Record result
→ Attach outcome
```

---

## 18.4 Enterprise control and evidence plane

### Purpose

Coordinate policies, evidence, outcomes, and improvement.

Enterprise should support three layers over time:

1. **First wedge: customer-facing AI economics** - plan allowances, entitlements, premium-model leakage, feature margin, billing evidence, and outcome-preserving routing.
2. **Expansion: internal AI workflow optimization** - team, project, support, sales, finance, operations, and product-development workflows where AI cost, rework, quality, or approval burden can be tied to a useful outcome.
3. **Later platform: organization-wide governance** - SSO/RBAC, retention, endpoint policy distribution, audit exports, SIEM/FinOps integrations, and centrally managed controls.

The product should be architected for all three, but the first paid pilot should prove the first layer only.

### Scope

- Usage Rules
- Policy versions
- Simulations
- Routing
- Approvals
- Work ledger
- Outcome economics
- Protected-value reporting
- Organizational rollups
- Integrations and exports

---

# 19. Product-market-fit hypothesis

## Hypothesis

> **AI-native SaaS companies with tiered plans and measurable workflow outcomes will pay to enforce customer-level AI economics before execution because existing gateways and observability systems do not adequately show whether cost controls preserve successful product outcomes.**
> 

## Assumptions to validate

1. Customer- or feature-level AI margin is a recurring, material problem.
2. Customer billing or credit conflicts caused by AI usage are recurring enough to justify evidence-backed controls.
3. A named buyer owns the problem.
4. Existing gateway limits are insufficient.
5. Customers will place AIWatcher in the decision path.
6. Customers will provide plan, feature, workflow, allowance, and billing-period context.
7. Customers can define a meaningful outcome.
8. The value protected exceeds implementation and subscription cost.
9. Outcome-aware evidence affects operational decisions.
10. The product can deliver value without replacing the existing gateway, observability platform, or billing platform.

---

# 20. The first ten-minute Enterprise demonstration

## Scenario

A Standard-plan customer initiates an expensive AI workflow.

### Step 1: Context

```
Customer: Acme
Plan: Standard
Feature: Advanced research
Monthly allowance: $100
Current usage: $94
Billing period: August 2026
Proposed model: Premium
Estimated request cost: $11.00
```

### Step 2: Evaluation

```
Policy: Standard Plan Premium-Model Entitlement
Version: 8
Decision: Route
Selected model: Standard
Reason: Premium model unavailable after allowance threshold
```

### Step 3: Enforcement

The SDK acknowledges that the selected standard model—not the original premium model—was called.

### Step 4: Result

```
Observed routed-model cost: $3.20
Observed result: Completed
Observed outcome: Customer accepted
```

### Step 5: Receipt

```
Estimated premium-model cost: $11.00
Observed routed-model cost: $3.20
Inferred avoided cost: $7.80
Observed outcome: Accepted
Historical success-rate difference: Insufficient data
Confidence: Medium
```

The demo must show a decision and a result—not merely a dashboard.

Support or finance can use the same receipt to explain why the customer allowance changed, which workflow consumed it, and whether the controlled path preserved the result.

## What the first demo must not lead with

The first Enterprise demo should not lead with:

- Total tokens
- Total calls
- Total agents
- Generic traces
- Generic dashboards
- Employee rankings
- Broad compliance maps
- Security posture summaries
- Development provenance
- Full billing integrations
- Leadership rollups

Those surfaces may matter later, but they are already crowded by gateways, observability systems, security tools, provenance products, and FinOps dashboards. The first demo must show one controlled WorkUnit: customer context, decision, enforcement acknowledgement, actual execution, outcome, and receipt.

---

# 21. Go-to-market strategy

## Track A: OSS product

Target:

- Heavy Claude, Codex, and Cursor users
- Staff and principal engineers
- AI-native developers
- Open-source contributors

Goals:

- Deliver independent value
- Build trust
- Improve adapters
- Learn developer workflows
- Establish development-side evidence

OSS success must not depend on Enterprise conversion.

---

## Track B: Enterprise validation

Run in parallel with OSS development, but keep engineering scope narrow.

### Discovery target

Interview approximately 15–20 companies matching the initial ICP.

### Design-partner target

Secure three serious design partners that have:

- A customer-facing AI feature
- Tiered plans or entitlements
- Meaningful AI cost
- A measurable outcome
- Willingness to instrument one workflow

### Paid validation

At least two design partners should be willing to pay for a narrowly scoped pilot.

A free pilot validates interest, not willingness to pay.

---

## Initial pilot scope

One:

- Application
- Workflow
- Customer-plan dimension
- Billing-period or allowance dimension
- Usage Rule
- Model-routing or limit action
- Outcome
- Evidence report

Do not build the broad Enterprise platform before this loop is validated.

---

# 22. Pricing hypothesis

## OSS

Free and useful without signup.

## Design-partner pilot

Fixed paid pilot covering:

- One application
- One or two controlled workflows
- Integration support
- Usage Rule configuration
- Outcome and protected-value report

## General Enterprise pricing hypothesis

Annual platform fee based on a combination of:

- Number of controlled applications or workflows
- Work-unit or event-volume tier
- Enterprise endpoint add-on
- Retention and integration requirements

Do not initially price as a percentage of “savings.” Protected-value measurement will not be sufficiently mature or uncontested.

Do not price primarily per policy or dashboard seat; those do not reflect customer value.

---

# 23. Execution strategy

## Phase 0: Finalize product truth

### Deliverables

- This vision document
- Canonical WorkUnit model
- Control decision semantics
- Intervention-receipt schema
- Outcome schema
- Evidence-label definitions
- Privacy contract
- OSS-to-Enterprise propagation rules
- Usage Rule definitions
- Product non-goals

### Exit criterion

Every proposed feature can state:

- User
- WorkUnit
- Decision
- Control
- Evidence
- Outcome
- Value

---

## Phase 1: Make AIWatcher Local excellent

### Priorities

1. Installation and first value within minutes
2. Reliable tool and surface detection
3. Accurate hook invocation status
4. Low-noise prompt preflight
5. Session-health and loop detection
6. Smooth cross-agent handoff
7. Clear intervention receipts
8. Strong commit, test, survival, and rework evidence
9. Privacy and threat-model documentation
10. Signed and dependable distribution
11. Adapter compatibility fixtures
12. Shared-core extraction

### Exit criteria

- Users return weekly.
- Interventions are helpful and low-noise.
- Surface protection is verifiable.
- Outcomes require minimal manual effort.
- Privacy claims are testable.
- The product remains useful without Enterprise.

---

## Phase 2: Validate Enterprise concurrently

This phase runs while OSS improves.

### Build only

- WorkUnit context
- Customer and plan context
- One immutable Usage Rule
- Pre-call evaluation API
- Allow and route decisions
- Enforcement acknowledgement
- Actual-cost record
- Outcome attachment
- Evidence receipt

### Do not build yet

- Broad dashboards
- Full GRC
- Universal agent inventory
- Every policy type
- Multiple additional SDK languages
- Full developer-fleet governance
- Complex compliance mappings

---

## Phase 3: Prove one paid control loop

### Objective

Demonstrate that outcome-aware Usage Rules protect meaningful value.

### Exit criteria

- The decision occurs before execution.
- Python and TypeScript have equivalent behavior.
- Enforcement is acknowledged.
- Original and selected models are recorded.
- The business outcome is attached.
- The counterfactual is correctly labeled.
- A design partner uses the evidence to make a real decision.
- A budget owner agrees to pay.

### Kill or rethink criteria

Rethink the Enterprise wedge if any of these remain true after serious design-partner attempts:

- Customers will not place AIWatcher in the pre-call decision path.
- Customers cannot provide customer, plan, feature, workflow, allowance, or billing-period context.
- Customers cannot attach any meaningful outcome signal.
- Enforcement acknowledgement is skipped or treated as optional.
- Evidence does not change a product, finance, support, or platform decision.
- The protected value is too small or too speculative to justify implementation effort.
- Buyers only want a dashboard, report, or after-the-fact attribution.
- A budget owner will not pay after one controlled workflow proves useful.

---

## Phase 4: Build the shared product core

```
aiwatcher-core
├── canonical models
├── adapters
├── capability declarations
├── privacy transforms
├── evidence schemas
├── outcome primitives
├── pricing semantics
├── policy interfaces
└── compatibility fixtures
```

Products:

```
aiwatcher-local
├── CLI
├── local dashboard
└── personal workflows

aiwatcher-enterprise-agent
├── enrollment
├── endpoint identity
├── signed policy sync
├── evidence upload
└── collection disclosure
```

---

## Phase 5: Connect development to production

### Required links

```
Local session
→ changed artifact
→ commit
→ pull request
→ build
→ deployment
→ service version
→ feature
→ production work units
```

### Initial integrations

- GitHub
- CI build metadata
- Deployment metadata
- OpenTelemetry resource attributes
- AIWatcher production SDK

Leadership views should default to:

- Repository
- Service
- Feature
- Workflow
- Team

Not individual developer rankings.

---

## Phase 6: Add organization-wide local controls

Capabilities:

- Endpoint enrollment
- Signed policies
- Observe-only rollout
- Advisory controls
- Context-health rollups
- Dangerous-action policies
- Auditable overrides
- Integration coverage
- Privacy-aware retention

Hard blocking should follow:

- Observe-only measurement
- False-positive review
- Verified enforcement
- Clear override paths
- Developer disclosure

---

## Phase 7: Build the learning flywheel

Capabilities:

- Intervention effectiveness by task type
- Model cost-versus-outcome comparison
- Policy false-positive analysis
- Approval-value analysis
- Customer and feature economics
- Rework prediction
- Routing recommendations
- Policy recommendations
- Confidence calibration
- Matched historical comparisons

Example:

> Similar document-analysis workflows completed successfully 94% of the time on Model B at 38% lower observed cost. Human-review rate was statistically similar across 420 comparable WorkUnits.
> 

That is the point where AIWatcher starts becoming a learning system.

---

# 24. Success metrics

## North-star metric

> **Verified protected value from interventions that preserve successful outcomes.**
> 

Protected value may include:

- Avoided model cost
- Preserved product margin
- Prevented unauthorized actions
- Reduced rework
- Successful lower-cost routing
- Durable code changes
- Reduced incident exposure

## Supporting product metric

> **Percentage of controlled WorkUnits that reach a successful outcome at equal or lower cost and risk.**
> 

---

## OSS metrics

- Weekly active controlled sessions
- Intervention acceptance
- Cancellation rate
- False-positive rate
- Handoff use
- Sessions with outcome evidence
- Cost per surviving change
- Rework after intervention
- Verified surface coverage
- Privacy test pass rate

## Enterprise metrics

- Calls evaluated before execution
- Enforcement acknowledgement rate
- WorkUnits with complete customer and feature context
- Policy latency
- Override rate
- Outcome capture rate
- Cost per successful outcome
- Outcome difference after intervention
- Inferred and measured protected value
- Spend under active control
- Applications with healthy integrations

## Metrics not to lead with

- Total tokens
- Total calls
- Total events
- Alerts generated
- Policies created
- Agents discovered
- Dashboard visits

These indicate activity, not customer value.

---

# 25. Validation and falsification criteria

## Strong validation signals

- Customers have a recurring, material feature-margin problem.
- Existing gateways do not answer the outcome question.
- Customers provide plan and workflow context.
- Customers integrate pre-call evaluation.
- Customers attach a meaningful outcome.
- The control changes real execution.
- The evidence changes a product or finance decision.
- Customers pay for the pilot.
- Historical evidence improves routing or policy decisions.

## Warning signals

- Customers only want a dashboard.
- Customers say their gateway is sufficient.
- Customers will not put AIWatcher in the call path.
- Customers cannot define outcomes.
- Customer-level savings are too small.
- Integration effort exceeds expected value.
- OSS users have no connection to Enterprise buyers.
- Design partners want broad compliance before the core loop.
- Outcome data remains sparse or untrustworthy.

## Moat falsification signals

The moat hypothesis should be reconsidered if:

- Competitors can access equivalent evidence with less friction.
- AIWatcher recommendations do not improve with history.
- Customers will not provide outcome context.
- Cross-layer lineage does not affect purchasing decisions.
- Customers can remove AIWatcher without losing meaningful operational value.
- The product remains a collection of independent features rather than an embedded decision system.

---

# 26. Strategic risks

## Product sprawl

Attempting to build observability, security, GRC, gateways, sandboxing, developer analytics, and FinOps simultaneously will prevent excellence in the core loop.

### Response

Every roadmap item must strengthen:

```
Control → Evidence → Outcome
```

---

## Competitor replication

Larger competitors may add customer context, outcome fields, lineage integrations, or protected-value reports.

### Response

Focus on:

- Higher-quality causal evidence
- Narrow product economics
- Deeper workflow embedding
- Customer-specific learning
- OSS trust and distribution
- Faster iteration with design partners

Do not assume technical uniqueness.

---

## Weak outcome attribution

If AIWatcher cannot reliably connect work to results, it becomes another telemetry platform.

### Response

Prioritize outcome, artifact, deployment, and product-context integrations ahead of additional dashboards.

---

## Surveillance perception

Developer trust can collapse if Enterprise silently expands collection.

### Response

- Local content by default
- Visible disclosure
- Team/service-first reporting
- Individual permissioning
- Auditable collection settings
- No hidden telemetry expansion

---

## Control without enforcement

A policy response callers can ignore creates false confidence.

### Response

Require explicit enforcement acknowledgement and execution evidence.

---

## Adapter brittleness

Local tools use changing and often undocumented formats.

### Response

- Adapter SDK
- Version fixtures
- Capability declarations
- Surface diagnostics
- Honest degradation states
- Incremental collection

---

## Counterfactual overclaiming

Protected-value claims can lose credibility if hypothetical savings are described as observed.

### Response

Show:

- Evidence label
- Comparison basis
- Sample size
- Confidence
- Outcome impact
- Assumptions

---

## OSS and Enterprise audience mismatch

OSS users and AI-product economic buyers may not naturally overlap.

### Response

Treat OSS as a product and technical distribution advantage—not as a guaranteed Enterprise funnel.

Test the conversion path rather than assuming it.

---

# 27. Final strategic choices

## Keep

- Local-first OSS
- Plan–Watch–Control–Prove–Improve
- Developer privacy
- Outcome orientation
- Usage Rules
- Production SDK
- Intervention receipts
- Development-to-production lineage
- Customer-specific learning

## Narrow

- Initial ICP
- First paid use case
- Supported SDK languages
- Policy actions
- Product navigation
- Buyer personas
- Security claims
- Platform coverage claims

## Defer

- Broad GRC
- Universal sandboxing
- Agent hosting
- Every framework and language
- Universal web interception
- Employee productivity scoring
- Autonomous policy generation
- Percentage-of-savings pricing
- Broad non-code outcome inference

---

# 28. Final product statement

## Category

**AI Work Control and Evidence**

## Tagline

> **Control what AI does. Prove what it delivered.**
> 

## Product value proposition

> **AIWatcher controls costly or risky AI work across developer agents and production applications before execution, then connects the decision to actual enforcement, cost, and outcome evidence.**
> 

## Initial paid wedge

> **Outcome-aware Usage Rules that protect AI product margins without blindly reducing product quality.**
> 

## Strategic differentiation

> **AIWatcher combines business context, pre-execution control, enforcement evidence, and durable outcomes across both AI-assisted development and production AI workflows.**
> 

## Moat hypothesis

> **AIWatcher can become defensible if its local, delivery, and production integrations produce uniquely complete intervention-to-outcome evidence, and that evidence improves customer-specific controls enough to create workflow dependence and switching costs.**
> 

## Product system

```
AIWatcher Local
    Developer value, privacy, trust and development evidence

Shared Core
    Canonical models, adapters, privacy and evidence semantics

Enterprise Endpoint
    Managed local policy and privacy-safe organizational rollups

Production SDK
    Pre-execution customer and workflow controls

Control Plane
    Policies, entitlements, routing and approvals

Evidence Plane
    Enforcement, lineage, outcomes and protected value

Intervention–Outcome Graph
    Learning about what works for each customer and workflow
```

## Final strategic rule

> **Do not build the broadest AI governance platform. Build the most credible system for controlling AI work and proving whether the control improved the outcome.**
>

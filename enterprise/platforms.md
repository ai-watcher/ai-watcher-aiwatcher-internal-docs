# Platform Coverage

[Review Home](README.md) · [Scope](scope.md) · [Requirements](requirements.md) · [Platforms](platforms.md) · [Test Cases](test-cases.md) · [Usage Controls Mockup](mockups/outcome-usage-billing-controls.html) · [Propagation Matrix](propagation-matrix.md)

> Do not claim enterprise, local, SDK, billing, SIEM, or FinOps coverage until the matching integration is verified. Enterprise docs may reference private roadmap details here because this repository stays private.

| Surface | Current mechanism | Coverage | Status | What to verify |
| --- | --- | --- | --- | --- |
| AIWatcher Enterprise Web App | Next.js dashboard, APIs, org auth, and Postgres-backed evidence/control model | Home, Controls, Workflows, Evidence, Spend, and Admin target navigation | In progress | Confirm current routes map to the lifecycle and remove/merge redundant dashboards. |
| JavaScript/TypeScript SDK | track, trackLLM, trackStream, session APIs, metadata, and future evaluateControl | Production app telemetry today; runtime controls pending | In progress | Add customerId, planId, feature, entitlement context, and pre-call control evaluation. |
| Python SDK | App instrumentation package for backend agents and AI workflows | Telemetry/evidence foundation; parity with JS control API pending | In progress | Align event fields and policy evaluation with JS SDK. |
| Local Collector / AIWatcher Local | Zero-code local scanner and developer control loop | Local work visibility; enterprise sync/parity pending | In progress | Decide which OSS events/evidence sync to Enterprise and how developer consent/admin disclosure works. |
| Billing / Plan Systems | SDK metadata first; later Stripe, Chargebee, or custom billing import | Required for customer entitlement rules and billing/allocation evidence; AIWatcher is not the billing system of record | Gap | Define plan, quota, allowance, contract, billing-cycle, credit, refund, and invoice identifiers without taking ownership of invoicing or payment state. |
| SIEM / Security | Evidence exports and future webhook/SIEM sink | Audit evidence target, not primary workflow yet | Gap | Define minimal export and alert payloads for security teams. |
| FinOps / Enterprise Dashboards | Grafana/dashboard export and reports | Cost reporting exists in pieces; protected spend and rule effectiveness pending | In progress | Connect cost reports to controls, not only charts. |
| Internal Workflow Systems | SDK metadata and outcome callbacks for support, sales, finance, product ops, QA, and back-office agents | Team/workflow attribution, controls, receipts, and outcome optimization for non-customer-facing AI usage | Gap | E-32: prove a workflow can be controlled without customer-facing product metadata. |
| Evidence Inputs | Admin health page over SDK, local collector, billing import, plan metadata, outcome callbacks, enforcement acknowledgement, and exports | Receipt trust and insufficiency labels | Gap | E-33: missing fields produce explicit insufficient-data states. |

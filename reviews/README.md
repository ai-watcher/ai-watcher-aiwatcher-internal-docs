# Product Docs Reviews

This folder stores private review records created from source repo changes.

Each review record answers one question:

> Did a code change require product-doc, scenario, or propagation updates?

Humans own the decision. Automation owns the bookkeeping.

## Flow

1. A source repo dispatches `product_docs_review_requested`.
2. This repo creates or updates a private docs-review PR.
3. The team updates the product-owned source files if needed:
   - `aiwatcher-local/scenarios.json`
   - `enterprise/scenarios.json`
   - `enterprise/propagation-matrix.md`
4. Generated Markdown and HTML are refreshed from the JSON source.

Use `docs-impact:none` only when the code change does not affect product
scenarios, enterprise propagation, or implementation/spec alignment.

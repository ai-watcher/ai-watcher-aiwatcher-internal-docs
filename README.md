# AIWatcher Internal Docs

Owner-only status and planning docs for AIWatcher.

This repository exists because `ai-watcher/aiwatcher-local` is public. Keep
scenario status, planning details, roadmap decisions, and generated review
surfaces here instead of in the OSS repo.

## Layout

```text
strategy.md

product-prototype/
  README.md
  index.html

aiwatcher-local/
  scenarios.json
  mockups/
  README.md
  scope.md
  requirements.md
  platforms.md
  test-cases.md
  index.html

enterprise/
  scenarios.json
  mockups/
  README.md
  scope.md
  requirements.md
  platforms.md
  test-cases.md
  propagation-matrix.md
  index.html
```

- `strategy.md` is the locked product source of truth: category, wedge,
  product lifecycle, scope by layer, metrics, risks, and execution phases.
- `product-prototype/index.html` is the current combined OSS/Enterprise
  clickable product-shape prototype. Use it to review navigation, scope split,
  and shared product language.
- `*/scenarios.json` is the source of truth.
- `README.md`, `scope.md`, `requirements.md`, `platforms.md`,
  `test-cases.md`, `propagation-matrix.md`, and `index.html` are generated or
  derived review surfaces.
- Use Markdown pages for GitHub review.
- Use `index.html` for offline interactive viewing.
- Product docs review records live under `reviews/`.
- Product automation is configured by `.github/product-docs.json`.
- Do not put secret values in git. GitHub Actions secrets stay in repository
  or organization Actions secrets.

## Review Hubs

- [Product Strategy](strategy.md)
- [Combined OSS/Enterprise Product Prototype](product-prototype/index.html) — primary current UX/scope review artifact
- [AIWatcher Local](aiwatcher-local/README.md)
- [AIWatcher Enterprise](enterprise/README.md)
- [OSS to Enterprise Propagation Matrix](enterprise/propagation-matrix.md)

Focused older mockups remain available for specific interaction details, but
the combined prototype above is the current source for product navigation and
OSS/Enterprise scope split:

- [AIWatcher Local Evidence Inbox Mockup](aiwatcher-local/mockups/evidence-inbox.html)
- [AIWatcher Enterprise Usage Controls Mockup](enterprise/mockups/outcome-usage-billing-controls.html)

## How To Use This Repo

Use `strategy.md` to decide whether a proposed feature belongs in AIWatcher at
all. Use the Local and Enterprise scenario files to track implementation status,
manual verification, UX workflows, platform coverage, and gaps. Code changes in
the OSS or Enterprise repos should create a docs-review PR here; the reviewer
then decides whether to update Local scenarios, Enterprise scenarios, or the OSS
to Enterprise propagation matrix.

## Automation

Render generated docs locally:

```bash
python3 scripts/render_product_docs.py
```

Check generated docs are current:

```bash
python3 scripts/check_generated_docs.py
```

Source repos should notify this repo with the `product_docs_review_requested`
repository dispatch event. The payload should contain source metadata only:

```json
{
  "product": "aiwatcher-local",
  "source_repo": "ai-watcher/aiwatcher-local",
  "source_pr": "24",
  "source_sha": "abc123",
  "source_ref": "feature/example",
  "source_url": "https://github.com/ai-watcher/aiwatcher-local/pull/24"
}
```

Private product content stays in this repo. Public and enterprise code repos
send metadata; they do not edit these docs directly.

### Required Secrets

Source repos that dispatch review requests need:

- `AIWATCHER_PRIVATE_DOCS_REPO`: `ai-watcher/ai-watcher-aiwatcher-internal-docs`
- `AIWATCHER_PRIVATE_DOCS_TOKEN`: fine-grained PAT with `Contents: Read and write`
  on this private docs repo, so it can send `repository_dispatch`.

This private docs repo also needs `AIWATCHER_PRIVATE_DOCS_TOKEN`. The
organization blocks PR creation with the default `GITHUB_TOKEN`, so the token
used here must have:

- `Contents: Read and write`
- `Pull requests: Read and write`

Limit the token to `ai-watcher/ai-watcher-aiwatcher-internal-docs`.
